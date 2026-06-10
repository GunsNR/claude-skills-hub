"""The CEO Brief: one payload that answers "what should I do right now?"

This is the heart of the ADHD UX. No dashboards to wander, no lists to
groom. Top 3 for Izzy, quick wins for low-energy moments, who's waiting
on Dilshan, which clients are going cold, and whether tax money is sitting
unswept. Everything else is noise until these are clear.
"""

from sqlalchemy.orm import Session

from . import business, tasks, tax_guard


def _task_dict(t) -> dict:
    return {
        "id": t.id,
        "title": t.title,
        "category": t.category,
        "owner": t.owner,
        "impact": t.impact,
        "urgency": t.urgency,
        "minutes": t.minutes,
        "score": round(tasks.score(t), 2),
    }


def build(db: Session) -> dict:
    tax = tax_guard.status(db)
    health = business.client_health(db)
    attention = [c for c in health if c["needs_attention"]]
    dilshan = business.delegation_queue(db)

    alerts = []
    if tax["unswept_balance"] > 0:
        alerts.append({
            "kind": "tax",
            "message": (f"${tax['unswept_balance']:.2f} of tax money is not "
                        f"swept to the tax account yet."),
        })
    for c in attention:
        days = c["days_since_contact"]
        msg = (f"{c['name']}: no contact logged yet" if days is None
               else f"{c['name']}: {days} days since last contact")
        alerts.append({"kind": "client", "message": msg})

    return {
        "top3": [_task_dict(t) for t in tasks.top3(db)],
        "quick_wins": [_task_dict(t) for t in tasks.quick_wins(db)],
        "alerts": alerts,
        "dilshan_queue": [_task_dict(t) for t in dilshan],
        "clients_needing_attention": attention,
        "tax": tax,
        "open_task_count": len(tasks.open_tasks(db, owner="izzy")),
    }
