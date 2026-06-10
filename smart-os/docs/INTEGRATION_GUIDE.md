# Integrating the CEO Layer into your local Smart OS

Two ways to run it. Start with Standalone today; integrate when convenient.

## Option A — Standalone (5 minutes, run it today)

```powershell
cd "C:\Users\izzy\OneDrive\Documents\Smart OS"
# copy the smart-os folder contents from this repo into the repo root, then:
.\.venv\Scripts\pip install fastapi uvicorn sqlalchemy httpx pyyaml
$env:SMARTOS_VAULT = "C:\path\to\your\Obsidian\vault"   # optional but recommended
$env:OPENROUTER_API_KEY = "<your NEW key>"               # optional; mock without it
cd apps\api
..\..\..\.venv\Scripts\python -m smartos_ceo.seed ..\..\config\rank_logic_seed.yaml
..\..\..\.venv\Scripts\python -m smartos_ceo.run
```

Open http://localhost:8100 — that's the ADHD dashboard. It binds to
0.0.0.0, so your iPhone on the same Wi-Fi can open
`http://<pc-lan-ip>:8100` and "Add to Home Screen" (see IPHONE_ACCESS.md).

Data lives in `smartos_ceo.db` (SQLite) next to where you run it, or set
`SMARTOS_CEO_DB=sqlite:///C:/path/smartos_ceo.db`.

## Option B — Integrated into the Smart OS backend

1. Copy `apps/api/smartos_ceo/` into your Smart OS repo's `apps/api/`.
2. In your FastAPI app factory (where other routers are included):

```python
from smartos_ceo import db as ceo_db
from smartos_ceo.router import router as ceo_router

ceo_db.configure(engine=your_engine)   # share the existing SQLite/Postgres engine
app.include_router(ceo_router)
```

All CEO tables are prefixed `ceo_` so they coexist cleanly with existing
tables. `configure()` runs `create_all` for just these tables; fold them
into Alembic later if you prefer migrations.

3. Replace the standalone gateway with your model gateway (optional but
   recommended): anything with a
   `generate(route_class, prompt, system) -> {text, model, tokens, est_cost}`
   method works — adapt your existing gateway and pass it where
   `build_gateway()` is called in `router.py`.

4. Surface `/api/ceo/brief` on your existing dashboard/Daily Review page,
   or just link to `/api/ceo/dashboard`.

5. Tests: copy `apps/api/tests/test_*.py` + `conftest.py` fixtures into your
   suite (fixtures are self-contained; they use an in-memory engine).

## Environment variables

| Var | Purpose | Default |
|---|---|---|
| `OPENROUTER_API_KEY` | OpenRouter auth (env only, never stored) | unset → mock gateway |
| `SMARTOS_VAULT` | absolute path to Obsidian vault | unset → vault features off |
| `SMARTOS_CEO_DB` | SQLAlchemy URL for standalone mode | `sqlite:///smartos_ceo.db` |
| `SMARTOS_CEO_PORT` | standalone port | 8100 |
| `SMARTOS_CALLMEBOT_PHONE` / `SMARTOS_CALLMEBOT_APIKEY` | WhatsApp to Dilshan (see NOTIFICATIONS.md) | unset → skipped |
| `SMARTOS_SMTP_HOST/PORT/USER/PASS`, `SMARTOS_NOTIFY_EMAIL` | email to Dilshan | unset → skipped |
| `SMARTOS_NOTIFY_WEBHOOK` | Zapier/Make fan-out hook | unset → skipped |

## Obsidian setup

Copy `obsidian-vault-template/` contents into your vault (or just let the
system create the `SmartOS/` folder on first write). Writes are physically
restricted to `SmartOS/` — everything else is read/index only.

## Security reminder

The spec notes an OpenRouter key was exposed during earlier setup. If you
haven't already: revoke it at openrouter.ai → Keys, create a fresh one, and
set it only via the environment variable. Never paste keys into chats, docs,
or config files.
