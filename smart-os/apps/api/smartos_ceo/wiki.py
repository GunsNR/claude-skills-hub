"""Self-improving task wiki (Karpathy-style).

Every task category gets a living playbook page. When a task is completed
with a learning ("what worked / what to do differently"), the learning is
appended to that category's playbook. Future work in the same category
pulls the playbook in as context, so the system gets better at how Izzy
actually works — without any fine-tuning.

Periodically, distill() can compress accumulated raw learnings into a
cleaner playbook via the model gateway (cheap summarization route).
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import Learning, WikiPage, utcnow

SEED_PLAYBOOKS = {
    "client": "# Client Playbook\n\n- Log every client touch the moment it happens (one line is enough).\n- Follow up within 24h of any call.\n",
    "sales": "# Sales Playbook\n\n- Proposals go out within 48h of a discovery call.\n- Always anchor on outcomes (leads, rankings, revenue), not deliverables.\n",
    "seo_delivery": "# SEO Delivery Playbook\n\n- Production SEO work routes to Dilshan with a written brief.\n- Briefs include: client, goal, pages/keywords, deadline, definition of done.\n",
    "tax": "# Tax Playbook\n\n- Every payment received: set aside the configured % immediately.\n- Sweep to the tax account weekly.\n",
    "growth": "# Growth Playbook\n\n- One growth experiment at a time. Ship, measure, learn, log.\n",
}


def get_page(db: Session, category: str) -> WikiPage:
    page = db.scalar(select(WikiPage).where(WikiPage.category == category))
    if page is None:
        page = WikiPage(category=category,
                        content=SEED_PLAYBOOKS.get(
                            category, f"# {category.title()} Playbook\n"))
        db.add(page)
        db.commit()
    return page


def list_pages(db: Session) -> list[WikiPage]:
    return list(db.scalars(select(WikiPage).order_by(WikiPage.category)))


def add_learning(db: Session, category: str, text: str,
                 source_task_id: int | None = None) -> Learning:
    learning = Learning(category=category, text=text.strip(),
                        source_task_id=source_task_id)
    db.add(learning)
    page = get_page(db, category)
    page.content = page.content.rstrip() + f"\n- {text.strip()}\n"
    page.updated_at = utcnow()
    db.commit()
    return learning


def get_context(db: Session, category: str) -> str:
    """Playbook text to inject into prompts for tasks in this category."""
    return get_page(db, category).content


def distill(db: Session, category: str, gateway, cost_router) -> WikiPage:
    """Compress a noisy playbook into a clean one via cheap summarization."""
    page = get_page(db, category)
    result = gateway.generate(
        "summarization",
        f"Rewrite this playbook as a tight, deduplicated set of rules. "
        f"Keep it under 30 bullet points. Preserve specifics.\n\n{page.content}",
        system="You maintain operating playbooks for the CEO of an SEO agency.",
    )
    cost_router.record_usage("summarization", result["model"],
                             result["tokens"], result["est_cost"])
    page.content = result["text"]
    page.updated_at = utcnow()
    db.commit()
    return page
