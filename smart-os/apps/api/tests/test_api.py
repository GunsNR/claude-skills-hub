import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from smartos_ceo.router import router


@pytest.fixture()
def client(db, vault, monkeypatch):
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    # Build the app directly so we keep the db fixture's in-memory engine
    # instead of create_app() re-configuring a file-backed one.
    app = FastAPI()
    app.include_router(router)
    return TestClient(app)


def test_capture_brief_done_flow(client):
    r = client.post("/api/ceo/capture",
                    json={"text": "send overdue invoice to Acme"})
    assert r.status_code == 200
    task = r.json()
    assert task["category"] == "finance"

    brief = client.get("/api/ceo/brief").json()
    assert brief["top3"][0]["id"] == task["id"]

    r = client.post(f"/api/ceo/tasks/{task['id']}/done",
                    json={"learning": "Invoice on the 1st, not the 15th"})
    assert r.status_code == 200
    page = client.get("/api/ceo/wiki/finance").json()
    assert "Invoice on the 1st" in page["content"]


def test_income_and_tax_flow(client):
    client.post("/api/ceo/income", json={"amount": 2000, "description": "retainer"})
    status = client.get("/api/ceo/tax/status").json()
    assert status["unswept_balance"] == 600.0
    brief = client.get("/api/ceo/brief").json()
    assert any(a["kind"] == "tax" for a in brief["alerts"])
    client.post("/api/ceo/tax/sweep")
    assert client.get("/api/ceo/tax/status").json()["unswept_balance"] == 0


def test_client_and_delegation_flow(client):
    r = client.post("/api/ceo/clients", json={"name": "Acme Plumbing", "mrr": 1500})
    cid = r.json()["id"]
    client.post(f"/api/ceo/clients/{cid}/log",
                json={"entry": "Monthly report sent", "kind": "deliverable"})
    r = client.post("/api/ceo/delegate",
                    json={"title": "Backlink audit for Acme", "client_id": cid})
    assert r.json()["obsidian_note"] is not None
    queue = client.get("/api/ceo/delegate/queue").json()
    assert len(queue) == 1


def test_obsidian_endpoints(client):
    notes = client.get("/api/ceo/obsidian/index").json()
    assert any(n["title"] == "Acme Plumbing" for n in notes)
    r = client.post("/api/ceo/obsidian/note",
                    json={"rel_path": "Inbox/idea.md", "content": "# Idea"})
    assert r.json()["written"].startswith("SmartOS")
    r = client.post("/api/ceo/obsidian/note",
                    json={"rel_path": "../escape.md", "content": "x"})
    assert r.status_code == 403


def test_research_and_usage(client):
    r = client.post("/api/ceo/research",
                    json={"question": "AEO tactics for service businesses?"})
    item_id = r.json()["id"]
    r = client.post(f"/api/ceo/research/{item_id}/run")
    assert r.json()["status"] == "done"
    usage = client.get("/api/ceo/usage").json()
    assert "spend_today_usd" in usage


def test_dashboard_serves(client):
    r = client.get("/api/ceo/dashboard")
    assert r.status_code == 200
    assert "Brain dump" in r.text


def test_404s(client):
    assert client.post("/api/ceo/tasks/999/done", json={}).status_code == 404
    assert client.post("/api/ceo/clients/999/log",
                       json={"entry": "x"}).status_code == 404
