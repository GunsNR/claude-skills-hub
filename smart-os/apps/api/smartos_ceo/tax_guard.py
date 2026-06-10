"""Tax set-aside guard.

Every income event automatically computes a set-aside amount (default 30%,
configurable via setting key 'tax_rate'). The unswept balance is surfaced
in the daily brief until the user confirms the money was moved to the tax
account ("sweep"). Nothing moves money automatically — this is a ledger
and a nag, by design.
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import IncomeEvent, Setting

DEFAULT_RATE = 0.30


def get_rate(db: Session) -> float:
    row = db.get(Setting, "tax_rate")
    if row is None:
        return DEFAULT_RATE
    try:
        rate = float(row.value)
    except ValueError:
        return DEFAULT_RATE
    return rate if 0 < rate < 1 else DEFAULT_RATE


def set_rate(db: Session, rate: float) -> float:
    if not 0 < rate < 1:
        raise ValueError("tax rate must be between 0 and 1")
    row = db.get(Setting, "tax_rate")
    if row is None:
        db.add(Setting(key="tax_rate", value=str(rate)))
    else:
        row.value = str(rate)
    db.commit()
    return rate


def record_income(db: Session, amount: float, description: str = "",
                  client_id: int | None = None) -> IncomeEvent:
    if amount <= 0:
        raise ValueError("amount must be positive")
    event = IncomeEvent(
        amount=amount,
        description=description[:500],
        client_id=client_id,
        tax_set_aside=round(amount * get_rate(db), 2),
    )
    db.add(event)
    db.commit()
    return event


def status(db: Session) -> dict:
    events = list(db.scalars(select(IncomeEvent)))
    unswept = [e for e in events if not e.swept]
    return {
        "tax_rate": get_rate(db),
        "total_income": round(sum(e.amount for e in events), 2),
        "total_set_aside": round(sum(e.tax_set_aside for e in events), 2),
        "unswept_balance": round(sum(e.tax_set_aside for e in unswept), 2),
        "unswept_events": len(unswept),
    }


def sweep(db: Session) -> dict:
    """Mark all unswept set-asides as moved to the tax account."""
    events = list(db.scalars(select(IncomeEvent).where(IncomeEvent.swept == False)))  # noqa: E712
    total = round(sum(e.tax_set_aside for e in events), 2)
    for e in events:
        e.swept = True
    db.commit()
    return {"swept_amount": total, "events_swept": len(events)}
