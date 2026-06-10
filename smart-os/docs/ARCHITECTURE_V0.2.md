# Smart OS v0.2 — The CEO Layer

This phase takes Smart OS from "safe AI infrastructure" (v0.1, built by
Codex) to "the most valuable assistant and advisor for running Rank Logic
SEO." Everything in v0.1 stays. v0.2 adds a business-aware layer on top.

## Why this layer exists

v0.1 answers: *how do I safely route models, index projects, and gate risky
actions?* It never answers the CEO's actual daily question: **"what should I
do right now?"** v0.2 is built around that question, designed for an ADHD
operator:

1. **Capture is one line.** No forms, no categories, no priorities to pick.
   Type a thought, the system classifies it (deterministic keyword rules —
   zero cost, zero latency; model-assisted classification is an optional
   upgrade on the cheap route).
2. **The system decides what matters.** The brief shows exactly 3 tasks.
   Score = impact×3 + urgency×2 + age×0.5, so important-but-quiet tasks
   creep up instead of rotting — the classic ADHD failure mode.
3. **Low-energy mode is a feature.** Quick wins (≤5 min) are surfaced
   separately so a bad-focus hour still produces motion.
4. **Delegation is structural.** Anything matching SEO production work
   auto-routes to Dilshan and generates a written brief in Obsidian with a
   definition of done. Izzy's Top 3 only ever contains Izzy's work.
5. **Tax money is guarded by default.** Every income event computes a 30%
   set-aside; the brief nags until it's swept. The system never moves money
   — it's a ledger plus an honest nag.

## Module map (apps/api/smartos_ceo/)

| Module | Responsibility |
|---|---|
| `tasks.py` | capture → classify → score → Top 3 / quick wins / snooze |
| `ceo_brief.py` | the single "what now?" payload |
| `business.py` | clients, interaction logs, health flags, Dilshan delegation |
| `tax_guard.py` | income events, set-aside ledger, sweep |
| `obsidian.py` | vault index/read anywhere; writes ONLY in `SmartOS/` |
| `wiki.py` | self-improving playbooks (Karpathy-style learning loop) |
| `auto_research.py` | queued research questions → structured briefs |
| `cost_router.py` | route class → model, daily budget caps, auto-downgrade |
| `gateway.py` | OpenRouter client (env key only) with offline mock fallback |
| `seed.py` | load business profile from `config/rank_logic_seed.yaml` |
| `router.py` | FastAPI router, mounts at `/api/ceo` |
| `static/dashboard.html` | one-page ADHD dashboard, PWA-installable on iPhone |

## The learning loop (auto-improvement)

Karpathy's observation: agents improve fastest when their *context* improves,
not their weights. The wiki implements that:

```
complete task (+optional one-line learning)
        → learning appended to that category's playbook
        → playbook injected as context into future model calls
          (research briefs, delegation drafts, distillation)
        → periodic distill() compresses the playbook on the cheap route
```

Over weeks, the playbooks become a written model of *how Izzy actually
works* — invoicing rules, client preferences, what to delegate — and every
AI call gets that context for free.

## Cost model

Routing config: `config/openrouter_routing.json`.

- Classification/summaries/logs → free or near-free models (DeepSeek free,
  Gemini Flash Lite). This is ~90% of CEO-layer traffic.
- Growth/research drafting → Sonnet-class.
- Strategy reasoning → Opus-class, only while under budget.
- **Soft cap** ($2/day default): every route downgrades to its cheapest model.
- **Hard cap** ($5/day): free models only.
- Spend is persisted per call and shown on the dashboard.

## Safety (inherits v0.1 non-negotiables)

- API key from `OPENROUTER_API_KEY` env only — never persisted, logged, or
  returned by any endpoint.
- Obsidian writes are physically restricted to `SmartOS/` (path-resolution
  check, not convention). Reads are .md-only and cannot escape the vault.
- No money moves, nothing publishes, no shell runs. The riskiest action in
  this layer is writing a markdown file into an inbox folder.
- Offline-safe: with no key configured, the mock gateway keeps everything
  testable and the daily workflow (tasks/tax/clients) fully functional.

## How it fits the v0.1 spec

- CEO brief = the "Daily Review" (spec §13), specialized for the business.
- cost_router = a concrete policy for the route classes in spec §4.
- wiki/learnings = the "growth learnings" loop (spec §10) generalized.
- obsidian.py = "safe Obsidian project memory indexing" (spec §18 item 10).
- The dashboard = the iPhone/LAN monitoring surface (spec §18 item 12).

Integration is additive: one router include + one engine bind. See
INTEGRATION_GUIDE.md.

## Deliberately not built yet

- Approval-gated writes outside `SmartOS/` (use v0.1 pending actions when
  integrating).
- Live GSC/analytics import (v0.1 connector shells already exist for this).
- Push notifications (PWA + LAN covers v0.2; Tailscale doc included).
- Auto-scheduling of distill/research runs (wire to the v0.1 scheduler).
