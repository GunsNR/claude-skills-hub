# Resume prompt for the local agent (Claude Code / Codex on Izzy's PC)

Paste everything below into your local coding agent inside
`C:\Users\izzy\OneDrive\Documents\Smart OS`.

---

You are resuming the Smart OS build (see docs/agent-checkpoint.md for the
v0.1 state: 181 backend tests passing, FastAPI + Next.js + SQLite).

A new phase — **v0.2 CEO Layer** — has been built and tested in the GitHub
repo `GunsNR/claude-skills-hub`, branch `claude/peaceful-edison-rn5tcq`,
under the `smart-os/` directory. Your job is to integrate it.

## Steps

1. Pull the `smart-os/` directory from that branch into this repo:
   - `apps/api/smartos_ceo/` → `apps/api/smartos_ceo/`
   - `apps/api/tests/test_tasks.py, test_tax_and_business.py, test_obsidian.py,
     test_wiki_research_cost.py, test_api.py, test_seed.py, conftest.py
     fixtures` → merge into `apps/api/tests/` (rename on collision; merge the
     `db`/`vault` fixtures into the existing conftest rather than overwriting).
   - `config/openrouter_routing.json`, `config/rank_logic_seed.yaml` → `config/`
   - `docs/*.md` → `docs/`
   - `obsidian-vault-template/` → repo root (Izzy copies it into his vault).
2. Read `docs/INTEGRATION_GUIDE.md` Option B and do it:
   - bind `smartos_ceo.db.configure(engine=...)` to the existing engine,
   - `app.include_router(ceo_router)` in the FastAPI app factory.
3. Adapt `smartos_ceo.gateway` to the existing model gateway so CEO-layer
   calls flow through v0.1's routing/metadata/approval machinery. Map route
   classes: classification/summarization→fast, research→reasoning,
   growth→growth.
4. Add `ceo_` tables to Alembic (autogenerate revision; verify no changes to
   existing tables).
5. Run the full suite: `$env:PYTHONPATH="apps/api"; .\.venv\Scripts\python -m
   pytest apps\api\tests -q`. All previous tests plus the 37 new ones must pass.
6. Add a "Today" card to the dashboard home page linking to
   `/api/ceo/dashboard`, and a Daily Review section fed by `GET /api/ceo/brief`.
7. Seed the business profile after Izzy edits `config/rank_logic_seed.yaml`
   with real clients: `python -m smartos_ceo.seed config/rank_logic_seed.yaml`.
8. Update docs/agent-checkpoint.md and docs/build-log.md per the resume
   protocol. Do not store or print any API keys.

## Constraints (non-negotiable, same as v0.1)

- No secrets in code, config tables, logs, or frontend responses.
- Obsidian writes stay restricted to the vault's `SmartOS/` folder; if you
  add writes elsewhere, gate them behind v0.1 pending actions.
- No publishing, money movement, or shell writes from the CEO layer.
