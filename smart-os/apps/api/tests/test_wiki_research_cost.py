from smartos_ceo import auto_research, wiki
from smartos_ceo.cost_router import CostRouter
from smartos_ceo.gateway import MockGateway, build_gateway


def test_learning_appends_to_playbook(db):
    wiki.add_learning(db, "client", "Acme prefers Loom videos over calls")
    content = wiki.get_context(db, "client")
    assert "Loom videos" in content
    assert content.startswith("# Client Playbook")


def test_new_category_gets_seeded_page(db):
    page = wiki.get_page(db, "podcasting")
    assert "Podcasting Playbook" in page.content


def test_distill_uses_cheap_route(db):
    cr = CostRouter(db)
    wiki.add_learning(db, "client", "something")
    page = wiki.distill(db, "client", MockGateway(), cr)
    assert page.content.startswith("[mock:summarization]")


def test_research_queue_roundtrip(db):
    item = auto_research.enqueue(db, "Best local SEO tactics for plumbers?")
    cr = CostRouter(db)
    done = auto_research.run(db, item.id, MockGateway(), cr)
    assert done.status == "done"
    assert done.brief.startswith("[mock:research]")
    assert auto_research.run(db, 9999, MockGateway(), cr) is None


def test_cost_router_downgrades_over_budget(db):
    cr = CostRouter(db)
    assert cr.choose_model("reasoning") == "anthropic/claude-opus-4.8"
    # blow past soft cap
    cr.record_usage("reasoning", "anthropic/claude-opus-4.8", 100000, 3.0)
    model = cr.choose_model("reasoning")
    assert model == "anthropic/claude-sonnet-4.6"  # cheapest in route
    # blow past hard cap → free fallback only
    cr.record_usage("reasoning", "anthropic/claude-opus-4.8", 100000, 3.0)
    assert cr.choose_model("reasoning") == cr.config["free_fallback"]


def test_cost_estimation_and_summary(db):
    cr = CostRouter(db)
    cost = cr.estimate_cost("anthropic/claude-sonnet-4.6", 1_000_000)
    assert cost == 9.0
    cr.record_usage("fast", "google/gemini-2.5-flash-lite", 1000, 0.0003)
    summary = cr.usage_summary()
    assert summary["spend_today_usd"] == 0.0003
    assert summary["downgraded"] is False


def test_gateway_falls_back_to_mock_without_key(db, monkeypatch):
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    gw = build_gateway(CostRouter(db))
    assert isinstance(gw, MockGateway)
