from datetime import datetime

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from smartos_ceo import scheduler, tasks, tax_guard
from smartos_ceo.models import RecurringTemplate
from smartos_ceo.router import router

NOTIFY_VARS = ["SMARTOS_CALLMEBOT_PHONE", "SMARTOS_CALLMEBOT_APIKEY",
               "SMARTOS_IZZY_PHONE", "SMARTOS_IZZY_APIKEY",
               "SMARTOS_SMTP_HOST", "SMARTOS_SMTP_USER", "SMARTOS_SMTP_PASS",
               "SMARTOS_NOTIFY_EMAIL", "SMARTOS_IZZY_EMAIL",
               "SMARTOS_NOTIFY_WEBHOOK"]

MONDAY_9AM = datetime(2026, 6, 8, 9, 0)  # a Monday
MONDAY_6AM = datetime(2026, 6, 8, 6, 0)


@pytest.fixture(autouse=True)
def clean_env(monkeypatch):
    for var in NOTIFY_VARS:
        monkeypatch.delenv(var, raising=False)
    monkeypatch.delenv("SMARTOS_BRIEF_HOUR", raising=False)


@pytest.fixture()
def client(db):
    app = FastAPI()
    app.include_router(router)
    return TestClient(app)


# ---------- morning brief ----------

def test_brief_not_sent_before_hour(db):
    assert scheduler.send_morning_brief(db, now=MONDAY_6AM) is None


def test_brief_sent_once_per_day(db):
    tasks.capture(db, "send overdue invoice to Acme")
    tax_guard.record_income(db, 1000.0)
    result = scheduler.send_morning_brief(db, now=MONDAY_9AM)
    assert result is not None
    assert "send overdue invoice to Acme" in result["text"]
    assert "$300.00 not swept" in result["text"]
    assert result["sent"]["whatsapp"] == "skipped (not configured)"
    # second tick same day: no resend
    assert scheduler.send_morning_brief(db, now=MONDAY_9AM) is None
    # next day: sends again
    assert scheduler.send_morning_brief(
        db, now=datetime(2026, 6, 9, 9, 0)) is not None


def test_brief_force_ignores_guards(db):
    assert scheduler.send_morning_brief(db, now=MONDAY_6AM, force=True) is not None


# ---------- recurring ----------

def test_daily_weekly_monthly_spawning(db):
    db.add(RecurringTemplate(title="check email inbox", cadence="daily"))
    db.add(RecurringTemplate(title="sweep tax money", cadence="weekly",
                             day=0))  # Mondays
    db.add(RecurringTemplate(title="invoice all clients", cadence="monthly",
                             day=8, owner="izzy", category="finance"))
    db.commit()
    spawned = scheduler.spawn_recurring(db, now=MONDAY_9AM)  # June 8 = Monday
    titles = [t.title for t in spawned]
    assert "check email inbox" in titles
    assert "sweep tax money" in titles
    assert "invoice all clients" in titles  # day 8 of month
    # same day again: nothing
    assert scheduler.spawn_recurring(db, now=MONDAY_9AM) == []
    # Tuesday: only daily
    spawned = scheduler.spawn_recurring(db, now=datetime(2026, 6, 9, 9, 0))
    assert [t.title for t in spawned] == ["check email inbox"]


def test_recurring_respects_owner_and_classification(db):
    db.add(RecurringTemplate(title="update client report dashboards",
                             cadence="daily", owner="dilshan"))
    db.commit()
    spawned = scheduler.spawn_recurring(db, now=MONDAY_9AM)
    assert spawned[0].owner == "dilshan"


def test_inactive_template_skipped(db):
    db.add(RecurringTemplate(title="old habit", cadence="daily", active=False))
    db.commit()
    assert scheduler.spawn_recurring(db, now=MONDAY_9AM) == []


# ---------- backup ----------

def test_backup_copies_and_prunes(db, tmp_path, monkeypatch):
    source = tmp_path / "smartos_ceo.db"
    source.write_bytes(b"sqlite-bytes")
    monkeypatch.setenv("SMARTOS_CEO_DB", f"sqlite:///{source}")
    monkeypatch.setenv("SMARTOS_BACKUP_DIR", str(tmp_path / "backups"))
    # seed old backups beyond the keep limit
    bdir = tmp_path / "backups"
    bdir.mkdir()
    for i in range(1, 17):
        (bdir / f"smartos_ceo-2026-05-{i:02d}.db").write_bytes(b"old")

    target = scheduler.run_backup(db, now=MONDAY_9AM)
    assert target is not None and target.read_bytes() == b"sqlite-bytes"
    assert len(list(bdir.glob("smartos_ceo-*.db"))) == scheduler.BACKUP_KEEP
    # once per day
    assert scheduler.run_backup(db, now=MONDAY_9AM) is None


def test_backup_skips_non_sqlite(db, monkeypatch):
    monkeypatch.setenv("SMARTOS_CEO_DB", "postgresql://x/y")
    assert scheduler.run_backup(db, now=MONDAY_9AM, force=True) is None


# ---------- API ----------

def test_recurring_crud_api(client):
    r = client.post("/api/ceo/recurring",
                    json={"title": "Invoice all clients", "cadence": "monthly",
                          "day": 1})
    assert r.status_code == 200
    rid = r.json()["id"]
    assert len(client.get("/api/ceo/recurring").json()) == 1
    assert client.delete(f"/api/ceo/recurring/{rid}").json()["deleted"] == rid
    assert client.delete("/api/ceo/recurring/999").status_code == 404
    assert client.post("/api/ceo/recurring",
                       json={"title": "x", "cadence": "hourly"}).status_code == 422


def test_brief_send_and_blocker_api(client):
    r = client.post("/api/ceo/brief/send")
    assert r.status_code == 200
    assert "Morning Brief" in r.json()["text"]

    task = client.post("/api/ceo/capture",
                       json={"text": "dilshan: fix sitemap"}).json()
    r = client.post(f"/api/ceo/tasks/{task['id']}/blocker",
                    json={"note": "Need WP admin access"})
    assert r.status_code == 200
    assert r.json()["notified"]["whatsapp"] == "skipped (not configured)"
    assert client.post("/api/ceo/tasks/999/blocker",
                       json={"note": "x"}).status_code == 404


def test_pages_serve(client):
    assert "Dilshan" in client.get("/api/ceo/dilshan").text
    assert "Repeats" in client.get("/api/ceo/repeats").text
