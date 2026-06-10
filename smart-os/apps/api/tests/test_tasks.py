from datetime import timedelta

from smartos_ceo import tasks
from smartos_ceo.models import utcnow


def test_classify_routes_seo_work_to_dilshan():
    meta = tasks.classify("run a technical seo audit for the new client site")
    assert meta["owner"] == "dilshan"
    assert meta["category"] == "seo_delivery"


def test_classify_tax_is_top_priority():
    meta = tasks.classify("set aside money for quarterly taxes")
    assert meta["category"] == "tax"
    assert meta["impact"] == 3 and meta["urgency"] == 3


def test_classify_explicit_dilshan_prefix():
    meta = tasks.classify("dilshan: update the reporting dashboard")
    assert meta["owner"] == "dilshan"


def test_classify_quick_win_detection():
    meta = tasks.classify("reply to John's text")
    assert meta["minutes"] == 5


def test_capture_and_top3_ordering(db):
    low = tasks.capture(db, "organize my desk")
    high = tasks.capture(db, "send the overdue invoice to Acme")
    top = tasks.top3(db)
    assert top[0].id == high.id
    assert low.id in [t.id for t in top]


def test_top3_only_izzy_tasks(db):
    tasks.capture(db, "dilshan: fix sitemap")
    tasks.capture(db, "call the new client about onboarding")
    top = tasks.top3(db)
    assert all(t.owner == "izzy" for t in top)


def test_age_increases_score(db):
    t = tasks.capture(db, "organize my desk")
    fresh = tasks.score(t)
    aged = tasks.score(t, now=utcnow() + timedelta(days=5))
    assert aged > fresh


def test_snooze_hides_then_returns(db):
    t = tasks.capture(db, "organize my desk")
    tasks.snooze(db, t.id, hours=24)
    assert t.id not in [x.id for x in tasks.open_tasks(db)]
    t.snoozed_until = utcnow() - timedelta(hours=1)
    db.commit()
    assert t.id in [x.id for x in tasks.open_tasks(db)]


def test_complete_marks_done(db):
    t = tasks.capture(db, "organize my desk")
    done = tasks.complete(db, t.id)
    assert done.status == "done" and done.completed_at is not None
    assert tasks.complete(db, 99999) is None


def test_quick_wins_filter(db):
    tasks.capture(db, "reply to John's text")
    tasks.capture(db, "write the growth strategy roadmap")
    wins = tasks.quick_wins(db)
    assert len(wins) == 1 and wins[0].minutes <= 5
