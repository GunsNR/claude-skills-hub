from smartos_ceo import tax_guard
from smartos_ceo.seed import apply_seed

SEED = {
    "business": {"name": "Rank Logic SEO", "owner": "Izzy", "tax_rate": 0.30},
    "clients": [
        {"name": "Acme Plumbing", "domain": "acme.com", "mrr": 1500},
        {"name": "Best Roofing", "mrr": 900, "status": "lead"},
    ],
}


def test_seed_creates_clients_and_rate(db):
    result = apply_seed(db, SEED)
    assert result["clients_created"] == 2
    assert tax_guard.get_rate(db) == 0.30


def test_seed_is_idempotent(db):
    apply_seed(db, SEED)
    seed2 = {**SEED, "clients": [{"name": "Acme Plumbing", "mrr": 2000}]}
    result = apply_seed(db, seed2)
    assert result["clients_created"] == 0
    assert result["clients_updated"] == 1
