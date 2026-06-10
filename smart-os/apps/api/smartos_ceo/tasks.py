"""ADHD-friendly task engine.

Design principles:
- Capture must be one line, zero friction. Classification is automatic.
- The system decides what matters (Top 3), the user just executes.
- Quick wins (<=5 min) surface separately for low-energy moments.
- Anything that smells like SEO production work routes to Dilshan.
"""

import re
from datetime import datetime, timedelta, timezone

from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import Task, utcnow

# Keyword rules: deterministic, fast, no model call needed for capture.
# (category, owner, impact, urgency) — first match wins.
RULES: list[tuple[str, dict]] = [
    (r"\b(tax|taxes|irs|set.?aside|quarterly)\b",
     {"category": "tax", "owner": "izzy", "impact": 3, "urgency": 3}),
    (r"\b(invoice|payment|paid|bill|charge|collect|overdue)\b",
     {"category": "finance", "owner": "izzy", "impact": 3, "urgency": 3}),
    (r"\b(proposal|lead|prospect|close|pitch|sales|discovery call)\b",
     {"category": "sales", "owner": "izzy", "impact": 3, "urgency": 2}),
    (r"\b(audit|backlink|on.?page|technical seo|gsc|search console|keyword|"
     r"rank|ranking|content brief|blog|publish|schema|sitemap|crawl)\b",
     {"category": "seo_delivery", "owner": "dilshan", "impact": 2, "urgency": 2}),
    (r"\b(client|call|meeting|follow.?up|check.?in|onboard)\b",
     {"category": "client", "owner": "izzy", "impact": 3, "urgency": 2}),
    (r"\b(hire|hiring|employee|team|payroll|1099|contractor)\b",
     {"category": "team", "owner": "izzy", "impact": 2, "urgency": 2}),
    (r"\b(automation|zapier|workflow|system|process|sop|tool)\b",
     {"category": "systems", "owner": "dilshan", "impact": 2, "urgency": 1}),
    (r"\b(strategy|growth|plan|roadmap|partnership|offer)\b",
     {"category": "growth", "owner": "izzy", "impact": 3, "urgency": 1}),
]

DEFAULTS = {"category": "admin", "owner": "izzy", "impact": 2, "urgency": 2}

QUICK_WIN_RE = re.compile(
    r"\b(quick|reply|respond|text|dm|forward|approve|confirm|remind)\b", re.I)


def classify(text: str) -> dict:
    """Classify a raw brain-dump line into category/owner/impact/urgency."""
    lowered = text.lower()
    meta = dict(DEFAULTS)
    for pattern, attrs in RULES:
        if re.search(pattern, lowered, re.I):
            meta.update(attrs)
            break
    meta["minutes"] = 5 if QUICK_WIN_RE.search(lowered) else 30
    # explicit owner override: "dilshan: do X" or "@dilshan"
    if re.match(r"^\s*(dilshan[:,]|@dilshan)", lowered):
        meta["owner"] = "dilshan"
    return meta


def capture(db: Session, text: str, client_id: int | None = None) -> Task:
    meta = classify(text)
    task = Task(title=text.strip()[:500], client_id=client_id, **meta)
    db.add(task)
    db.commit()
    return task


def score(task: Task, now: datetime | None = None) -> float:
    """Priority score. Impact dominates, urgency second, age breaks ties.

    Old tasks creep upward so nothing rots silently — a classic ADHD
    failure mode is the important-but-not-screaming task disappearing.
    """
    now = now or utcnow()
    created = task.created_at
    if created.tzinfo is None:
        created = created.replace(tzinfo=timezone.utc)
    age_days = min((now - created).days, 5)
    return task.impact * 3 + task.urgency * 2 + age_days * 0.5


def open_tasks(db: Session, owner: str | None = None) -> list[Task]:
    now = utcnow()
    stmt = select(Task).where(Task.status.in_(["open", "snoozed"]))
    if owner:
        stmt = stmt.where(Task.owner == owner)
    tasks = list(db.scalars(stmt))
    visible = []
    for t in tasks:
        if t.status == "snoozed":
            until = t.snoozed_until
            if until is not None and until.tzinfo is None:
                until = until.replace(tzinfo=timezone.utc)
            if until and until > now:
                continue
        visible.append(t)
    return visible


def top3(db: Session, owner: str = "izzy") -> list[Task]:
    tasks = open_tasks(db, owner=owner)
    return sorted(tasks, key=score, reverse=True)[:3]


def quick_wins(db: Session, owner: str = "izzy", limit: int = 5) -> list[Task]:
    tasks = [t for t in open_tasks(db, owner=owner) if t.minutes <= 5]
    return sorted(tasks, key=score, reverse=True)[:limit]


def complete(db: Session, task_id: int) -> Task | None:
    task = db.get(Task, task_id)
    if task is None:
        return None
    task.status = "done"
    task.completed_at = utcnow()
    db.commit()
    return task


def snooze(db: Session, task_id: int, hours: int = 24) -> Task | None:
    task = db.get(Task, task_id)
    if task is None:
        return None
    task.status = "snoozed"
    task.snoozed_until = utcnow() + timedelta(hours=hours)
    db.commit()
    return task
