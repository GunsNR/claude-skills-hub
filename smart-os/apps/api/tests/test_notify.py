import httpx
import pytest

from smartos_ceo import business, notify, tasks

NOTIFY_VARS = ["SMARTOS_CALLMEBOT_PHONE", "SMARTOS_CALLMEBOT_APIKEY",
               "SMARTOS_SMTP_HOST", "SMARTOS_SMTP_USER", "SMARTOS_SMTP_PASS",
               "SMARTOS_NOTIFY_EMAIL", "SMARTOS_NOTIFY_WEBHOOK"]


@pytest.fixture(autouse=True)
def clean_env(monkeypatch):
    for var in NOTIFY_VARS:
        monkeypatch.delenv(var, raising=False)


def test_all_channels_skip_when_unconfigured():
    result = notify.notify_dilshan("Fix sitemap")
    assert all(v == "skipped (not configured)" for v in result.values())


def test_whatsapp_sends_when_configured(monkeypatch):
    calls = {}

    def fake_get(url, params=None, timeout=None):
        calls["url"] = url
        calls["params"] = params
        return httpx.Response(200, request=httpx.Request("GET", url))

    monkeypatch.setenv("SMARTOS_CALLMEBOT_PHONE", "+94770000000")
    monkeypatch.setenv("SMARTOS_CALLMEBOT_APIKEY", "test-key")
    monkeypatch.setattr(httpx, "get", fake_get)
    result = notify.notify_dilshan("Fix sitemap", details="ASAP")
    assert result["whatsapp"] == "sent"
    assert "Fix sitemap" in calls["params"]["text"]
    assert "ASAP" in calls["params"]["text"]


def test_failures_are_swallowed_not_raised(monkeypatch):
    def boom(*args, **kwargs):
        raise httpx.ConnectError("no network")

    monkeypatch.setenv("SMARTOS_CALLMEBOT_PHONE", "+94770000000")
    monkeypatch.setenv("SMARTOS_CALLMEBOT_APIKEY", "test-key")
    monkeypatch.setenv("SMARTOS_NOTIFY_WEBHOOK", "https://hooks.example/x")
    monkeypatch.setattr(httpx, "get", boom)
    monkeypatch.setattr(httpx, "post", boom)
    result = notify.notify_dilshan("Fix sitemap")
    assert result["whatsapp"] == "failed (ConnectError)"
    assert result["webhook"] == "failed (ConnectError)"


def test_delegate_reports_notification_status(db):
    result = business.delegate(db, "Backlink audit")
    assert "notified" in result
    assert result["notified"]["whatsapp"] == "skipped (not configured)"


def test_set_owner_flips_and_validates(db):
    t = tasks.capture(db, "organize my desk")
    moved = tasks.set_owner(db, t.id, "dilshan")
    assert moved.owner == "dilshan"
    back = tasks.set_owner(db, t.id, "izzy")
    assert back.owner == "izzy"
    with pytest.raises(ValueError):
        tasks.set_owner(db, t.id, "bob")
    assert tasks.set_owner(db, 9999, "dilshan") is None
