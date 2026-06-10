"""Auto-research queue.

Queue questions ("what's working in local SEO for plumbers in 2026?"),
and the system drafts a structured research brief via the model gateway
using the research route class — cheap by default, never blocking the UI.
Briefs land back in the queue and can be pushed to Obsidian as notes.
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from . import wiki
from .models import ResearchItem

BRIEF_PROMPT = """You are the research analyst for Rank Logic SEO.
Question: {question}
Context: {context}

Produce a research brief in markdown with sections:
## Answer (3 sentences max)
## What to do about it (numbered, concrete)
## Risks / unknowns
## Suggested delegation (what Dilshan should own vs the CEO)
"""


def enqueue(db: Session, question: str, context: str = "") -> ResearchItem:
    item = ResearchItem(question=question.strip(), context=context.strip())
    db.add(item)
    db.commit()
    return item


def list_items(db: Session, status: str | None = None) -> list[ResearchItem]:
    stmt = select(ResearchItem).order_by(ResearchItem.created_at.desc())
    if status:
        stmt = stmt.where(ResearchItem.status == status)
    return list(db.scalars(stmt))


def run(db: Session, item_id: int, gateway, cost_router) -> ResearchItem | None:
    item = db.get(ResearchItem, item_id)
    if item is None:
        return None
    playbook = wiki.get_context(db, "growth")
    prompt = BRIEF_PROMPT.format(question=item.question, context=item.context)
    try:
        result = gateway.generate(
            "research", prompt,
            system=f"Operating playbook for context:\n{playbook}")
    except Exception as exc:  # network/provider failure must not lose the item
        item.status = "failed"
        item.brief = f"Research run failed: {type(exc).__name__}"
        db.commit()
        return item
    cost_router.record_usage("research", result["model"], result["tokens"],
                             result["est_cost"])
    item.brief = result["text"]
    item.model_used = result["model"]
    item.status = "done"
    db.commit()
    return item
