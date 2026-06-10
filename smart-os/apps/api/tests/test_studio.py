import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from smartos_ceo import studio
from smartos_ceo.cost_router import CostRouter
from smartos_ceo.gateway import MockGateway
from smartos_ceo.router import router


@pytest.fixture(autouse=True)
def studio_dir(tmp_path, monkeypatch):
    monkeypatch.setenv("SMARTOS_STUDIO_DIR", str(tmp_path / "studio"))
    return tmp_path / "studio"


@pytest.fixture()
def client(db, monkeypatch):
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    app = FastAPI()
    app.include_router(router)
    return TestClient(app)


class HtmlGateway:
    def generate(self, route_class, prompt, system=""):
        return {"text": "```html\n<!DOCTYPE html><html><body><h1>Acme</h1>"
                        "</body></html>\n```\n## WordPress build notes\nUse "
                        "Astra theme.",
                "model": "test", "tokens": 100, "est_cost": 0.001}


class SvgGateway:
    def generate(self, route_class, prompt, system=""):
        return {"text": "Here you go: <svg xmlns='http://www.w3.org/2000/svg' "
                        "viewBox='0 0 400 120'><circle cx='60' cy='60' r='40' "
                        "fill='#6ee7b7'/></svg> Enjoy!",
                "model": "test", "tokens": 50, "est_cost": 0.0005}


def test_registry_is_complete():
    actions = studio.list_actions()
    assert len(actions) >= 12
    labels = [a["label"] for a in actions]
    assert "Create WP Website" in labels
    assert "Create Logo" in labels
    assert "Ask a Question" in labels
    assert all(a["placeholder"] for a in actions)


def test_markdown_action_with_mock(db):
    job = studio.run(db, "ask", "What is AEO?", MockGateway(), CostRouter(db))
    assert job.status == "done"
    assert job.output_text.startswith("[mock:fast]")
    assert studio.run(db, "nope", "x", MockGateway(), CostRouter(db)) is None


def test_html_action_extracts_and_saves(db, studio_dir):
    job = studio.run(db, "wp_site", "Acme Plumbing, Boston",
                     HtmlGateway(), CostRouter(db))
    assert job.file_name == "index.html"
    saved = (studio_dir / str(job.id) / "index.html").read_text(encoding="utf-8")
    assert "<h1>Acme</h1>" in saved
    assert "```" not in saved
    assert "WordPress build notes" in job.output_text


def test_html_fallback_wraps_plain_text(db, studio_dir):
    job = studio.run(db, "landing", "anything", MockGateway(), CostRouter(db))
    saved = (studio_dir / str(job.id) / "index.html").read_text(encoding="utf-8")
    assert saved.startswith("<!DOCTYPE html>")


def test_svg_action_extracts(db, studio_dir):
    job = studio.run(db, "logo", "Rank Logic, green",
                     SvgGateway(), CostRouter(db))
    assert job.file_name == "logo.svg"
    assert job.output_text.startswith("<svg")
    assert "Enjoy" not in job.output_text


def test_svg_fallback_with_mock(db):
    job = studio.run(db, "logo", "x", MockGateway(), CostRouter(db))
    assert "<svg" in job.output_text  # placeholder, still renders


def test_run_records_cost(db):
    cr = CostRouter(db)
    studio.run(db, "wp_site", "Acme", HtmlGateway(), cr)
    assert cr.spend_today() == 0.001


def test_gateway_failure_marks_job_failed(db):
    class Boom:
        def generate(self, *a, **k):
            raise RuntimeError("provider down")
    job = studio.run(db, "ask", "hi", Boom(), CostRouter(db))
    assert job.status == "failed"
    assert "RuntimeError" in job.output_text


def test_api_run_and_history(client):
    r = client.post("/api/ceo/studio/run",
                    json={"action_id": "ask", "input": "What is AEO?"})
    assert r.status_code == 200
    assert r.json()["status"] == "done"
    jobs = client.get("/api/ceo/studio/jobs").json()
    assert len(jobs) == 1
    assert client.post("/api/ceo/studio/run",
                       json={"action_id": "nope", "input": "x"}).status_code == 404


def test_file_serving_blocks_traversal(client, db, studio_dir):
    job = studio.run(db, "wp_site", "Acme", HtmlGateway(), CostRouter(db))
    r = client.get(f"/api/ceo/studio/files/{job.id}/index.html")
    assert r.status_code == 200
    r = client.get(f"/api/ceo/studio/files/{job.id}/..%2F..%2Fetc%2Fpasswd")
    assert r.status_code == 404


def test_studio_page_serves(client):
    r = client.get("/api/ceo/studio")
    assert r.status_code == 200
    assert "Studio" in r.text
