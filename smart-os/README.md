# Smart OS v0.2 — CEO Layer

The business brain for Smart OS, built for running **Rank Logic SEO** as an
ADHD CEO. Sits on top of the v0.1 platform (FastAPI + Next.js, built by
Codex on Izzy's PC) and answers one question all day: **"what should I do
right now?"**

## What it does

- **One-line capture** → auto-classified (client / sales / finance / tax /
  growth / SEO delivery), auto-routed: production SEO work goes straight to
  **Dilshan's queue** with a generated brief in Obsidian.
- **CEO Brief** — exactly 3 tasks for Izzy, quick wins for low-energy
  moments, stale-client alerts, tax status. Nothing else.
- **Tax Guard** — every income event sets aside 30% automatically (ledger +
  nag; never moves money).
- **Client memory** — one-line interaction logs; flags any active client
  untouched for 14 days.
- **Self-improving wiki** — completed tasks feed learnings into per-category
  playbooks that get injected into future AI calls (Karpathy-style: improve
  the context, not the weights).
- **Auto-research** — queue questions, get structured briefs with a
  delegation split (Dilshan vs CEO).
- **Cost-routed OpenRouter** — free/cheap models for ~90% of traffic, daily
  budget caps with automatic downgrade. Spend shown on the dashboard.
- **ADHD dashboard** — one page, dark, big buttons, installable on iPhone
  as a PWA over LAN/Tailscale.

## Quick start (standalone)

```powershell
pip install fastapi uvicorn sqlalchemy httpx pyyaml
$env:SMARTOS_VAULT = "C:\path\to\Obsidian\vault"     # optional
$env:OPENROUTER_API_KEY = "<new key>"                 # optional (mock without)
cd apps\api
python -m smartos_ceo.seed ..\..\config\rank_logic_seed.yaml
python -m smartos_ceo.run
# open http://localhost:8100
```

Tests: `cd apps/api && python -m pytest tests -q` (37 tests).

## Docs

| Doc | What |
|---|---|
| [ARCHITECTURE_V0.2.md](docs/ARCHITECTURE_V0.2.md) | design + how it fits the v0.1 spec |
| [INTEGRATION_GUIDE.md](docs/INTEGRATION_GUIDE.md) | run standalone or mount into Smart OS |
| [NEXT_AGENT_RESUME_PROMPT.md](docs/NEXT_AGENT_RESUME_PROMPT.md) | paste into the local agent to integrate |
| [IPHONE_ACCESS.md](docs/IPHONE_ACCESS.md) | home-screen app via LAN/Tailscale |

## Safety

Same non-negotiables as v0.1: API key via env only; Obsidian writes
physically restricted to the vault's `SmartOS/` folder; no publishing, no
money movement, no shell. Fully functional offline via the mock gateway.

⚠️ The v0.1 spec notes an OpenRouter key was exposed earlier — revoke it and
create a fresh one before setting `OPENROUTER_API_KEY`.
