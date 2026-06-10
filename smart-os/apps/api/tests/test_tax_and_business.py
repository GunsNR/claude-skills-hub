import pytest

from smartos_ceo import business, tax_guard


def test_income_sets_aside_default_30_percent(db):
    e = tax_guard.record_income(db, 1000.0, "Acme monthly retainer")
    assert e.tax_set_aside == 300.0


def test_custom_rate_and_validation(db):
    tax_guard.set_rate(db, 0.25)
    e = tax_guard.record_income(db, 200.0)
    assert e.tax_set_aside == 50.0
    with pytest.raises(ValueError):
        tax_guard.set_rate(db, 1.5)
    with pytest.raises(ValueError):
        tax_guard.record_income(db, -5)


def test_sweep_clears_unswept_balance(db):
    tax_guard.record_income(db, 1000.0)
    tax_guard.record_income(db, 500.0)
    assert tax_guard.status(db)["unswept_balance"] == 450.0
    result = tax_guard.sweep(db)
    assert result["swept_amount"] == 450.0
    assert tax_guard.status(db)["unswept_balance"] == 0


def test_client_health_flags_stale_contact(db):
    c = business.create_client(db, "Acme Plumbing", mrr=1500)
    health = business.client_health(db)
    assert health[0]["needs_attention"] is True  # never contacted
    business.log_interaction(db, c.id, "Kickoff call went well", kind="call")
    health = business.client_health(db)
    assert health[0]["needs_attention"] is False
    assert health[0]["days_since_contact"] == 0


def test_delegate_creates_dilshan_task_and_brief(db, vault):
    result = business.delegate(db, "Audit Acme's backlinks",
                               details="Full backlink audit, flag toxic links")
    queue = business.delegation_queue(db)
    assert len(queue) == 1 and queue[0].owner == "dilshan"
    assert result["obsidian_note"] is not None
    note = vault / result["obsidian_note"]
    assert note.exists()
    assert "Definition of done" in note.read_text(encoding="utf-8")


def test_delegate_without_vault_still_creates_task(db):
    result = business.delegate(db, "Fix the sitemap")
    assert result["task_id"] is not None
    assert result["obsidian_note"] is None
