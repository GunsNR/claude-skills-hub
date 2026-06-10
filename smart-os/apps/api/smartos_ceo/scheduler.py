"""In-app scheduler: the part of the system that chases Izzy.

Every tick (default once a minute, started from run.py):
- After SMARTOS_BRIEF_HOUR local time (default 8), send the Morning Brief
  to Izzy via his configured channels — once per day.
- Spawn any recurring task templates due today — once per day each.
- Take a daily backup of the SQLite database into SMARTOS_BACKUP_DIR
  (default ./backups), keeping the newest 14.

All "once per day" guards persist in the settings table, so restarts
don't double-send. Uses PC-local time on purpose: mornings are local.
"""

import os
import shutil
import threading
import time
from datetime import date, datetime
from pathlib import Path

from sqlalchemy import select
from sqlalchemy.orm import Session

from . import ceo_brief, notify, tasks
from .db import get_session
from .models import RecurringTemplate, Setting, Task

BACKUP_KEEP = 14


def _get_setting(db: Session, key: str) -> str:
    row = db.get(Setting, key)
    return row.value if row else ""


def _set_setting(db: Session, key: str, value: str) -> None:
    row = db.get(Setting, key)
    if row is None:
        db.add(Setting(key=key, value=value))
    else:
        row.value = value
    db.commit()


# ---------- morning brief ----------

def brief_hour() -> int:
    try:
        return int(os.environ.get("SMARTOS_BRIEF_HOUR", "8"))
    except ValueError:
        return 8


def format_brief(brief: dict, today: date) -> str:
    lines = [f"Smart OS Morning Brief — {today:%a %b %d}", ""]
    if brief["top3"]:
        lines.append("YOUR TOP 3:")
        for i, t in enumerate(brief["top3"], 1):
            lines.append(f"{i}. {t['title']} (~{t['minutes']}m)")
    else:
        lines.append("Top 3: clear. Go sell or go rest.")
    if brief["quick_wins"]:
        lines.append(f"\nQuick wins queued: {len(brief['quick_wins'])}")
    tax = brief["tax"]
    if tax["unswept_balance"] > 0:
        lines.append(f"\n💰 TAX: ${tax['unswept_balance']:.2f} not swept yet")
    cold = brief["clients_needing_attention"]
    if cold:
        names = ", ".join(c["name"] for c in cold[:5])
        lines.append(f"\n🥶 Going cold: {names}")
    if brief["dilshan_queue"]:
        lines.append(f"\nDilshan queue: {len(brief['dilshan_queue'])} open")
    return "\n".join(lines)


def send_morning_brief(db: Session, now: datetime | None = None,
                       force: bool = False) -> dict | None:
    now = now or datetime.now()
    today = now.date().isoformat()
    if not force:
        if now.hour < brief_hour():
            return None
        if _get_setting(db, "last_brief_date") == today:
            return None
    brief = ceo_brief.build(db)
    text = format_brief(brief, now.date())
    result = notify.notify_izzy(
        f"[Smart OS] Morning Brief {now.date():%b %d}", text)
    _set_setting(db, "last_brief_date", today)
    return {"sent": result, "text": text}


# ---------- recurring tasks ----------

def _due_today(template: RecurringTemplate, now: datetime) -> bool:
    today = now.date().isoformat()
    if not template.active or template.last_spawned == today:
        return False
    if template.cadence == "daily":
        return True
    if template.cadence == "weekly":
        return now.weekday() == template.day
    if template.cadence == "monthly":
        return now.day == min(max(template.day, 1), 28)
    return False


def spawn_recurring(db: Session, now: datetime | None = None) -> list[Task]:
    now = now or datetime.now()
    spawned = []
    for template in db.scalars(select(RecurringTemplate)):
        if not _due_today(template, now):
            continue
        meta = tasks.classify(template.title)
        if template.owner:
            meta["owner"] = template.owner
        if template.category:
            meta["category"] = template.category
        task = Task(title=template.title, details=template.details, **meta)
        db.add(task)
        template.last_spawned = now.date().isoformat()
        spawned.append(task)
    db.commit()
    return spawned


# ---------- backups ----------

def _db_file() -> Path | None:
    url = os.environ.get("SMARTOS_CEO_DB", "sqlite:///smartos_ceo.db")
    if not url.startswith("sqlite:///"):
        return None  # Postgres etc: handled by the host's backup story
    path = Path(url[len("sqlite:///"):])
    return path if path.is_file() else None


def backup_dir() -> Path:
    path = Path(os.environ.get("SMARTOS_BACKUP_DIR", "backups"))
    path.mkdir(parents=True, exist_ok=True)
    return path


def run_backup(db: Session, now: datetime | None = None,
               force: bool = False) -> Path | None:
    now = now or datetime.now()
    today = now.date().isoformat()
    if not force and _get_setting(db, "last_backup_date") == today:
        return None
    source = _db_file()
    if source is None:
        return None
    target = backup_dir() / f"smartos_ceo-{today}.db"
    shutil.copy2(source, target)
    _set_setting(db, "last_backup_date", today)
    backups = sorted(backup_dir().glob("smartos_ceo-*.db"))
    for old in backups[:-BACKUP_KEEP]:
        old.unlink(missing_ok=True)
    return target


# ---------- loop ----------

def tick(now: datetime | None = None) -> None:
    db = get_session()
    try:
        spawn_recurring(db, now)
        send_morning_brief(db, now)
        run_backup(db, now)
    finally:
        db.close()


def start(interval_seconds: int = 60) -> threading.Thread:
    def loop():
        while True:
            try:
                tick()
            except Exception:
                pass  # the scheduler must never die; next tick retries
            time.sleep(interval_seconds)

    thread = threading.Thread(target=loop, daemon=True,
                              name="smartos-scheduler")
    thread.start()
    return thread
