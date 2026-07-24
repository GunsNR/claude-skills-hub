# Run the Smart OS optimization on your PC

The full Smart OS codebase (FastAPI + Next.js, 359 backend tests) lives only on
your PC — no cloud agent can see it. So the audit/optimization prompt below
must run in Claude Code **on your PC**, inside the Smart OS folder.

Follow these steps exactly.

---

## Step 1 — Open a terminal in the Smart OS folder

Press the Windows key, type `powershell`, press Enter. Then paste:

```powershell
cd "C:\Users\izzy\OneDrive\Documents\Smart OS"
```

## Step 2 — Start Claude Code

Paste:

```powershell
claude
```

If you get an error that `claude` is not recognized, install it first:

```powershell
irm https://claude.ai/install.ps1 | iex
```

then close PowerShell, reopen it, and repeat Steps 1–2.

## Step 3 — Turn on Plan Mode

Once Claude Code is running, press **Shift+Tab** until the bottom of the
screen says **plan mode**. This makes the agent audit and propose before it
touches anything. You will approve its plan before any edit happens.

## Step 4 — Paste the prompt

Copy everything inside the box below — from `You are optimizing` down to the
final line — paste it into Claude Code, and press Enter.

---

## The prompt

```
You are optimizing my local-first AI operating system called Smart OS.

Your role is senior product architect, UX researcher, full-stack engineer, AI systems engineer, security reviewer, and workflow designer.

First inspect the actual repository and current implementation. Do not invent features based only on this prompt. Treat the source code, migrations, tests, docs, and runtime behavior as the source of truth. Also read the repo's docs/ folder and the recent git history (git log --oneline -30) as planning input.

PRE-FLIGHT GATE — do this before proposing or changing anything:
1. Run git status. The working tree must be clean. If it is not, stop and show me what is uncommitted.
2. Record the current commit hash. I believe it is 96b1542; if it differs, tell me and continue with whatever it actually is.
3. Run the full backend test suite once, unchanged, to reproduce the baseline (last known: 359 passed, 2 skipped). If the baseline does not reproduce, stop, report exactly what failed, and fix nothing else until I respond.
4. Create a work branch named optimize/ux-audit and do all work there. Never commit to main directly. One small verified checkpoint per commit.

About me and how I work:

- My name is Izzy.
- I am building an AI operating system for running an agency and managing real clients.
- I want the product to be simple, practical, useful, and fast.
- I do not want a bloated enterprise dashboard.
- I want one clear next action at a time.
- I want to add real clients and immediately work with their real data.
- I want CSV imports to be easy, forgiving, clearly explained, and previewable.
- I want the system to tell me exactly what file to upload, where it came from, what columns it expects, and what will happen next.
- I want AI to do most routine analysis, organization, drafting, comparison, and preparation automatically.
- I want human approval mainly at meaningful boundaries such as client onboarding completion, publishing, sending, spending, payments, external changes, and final financial-plan activation.
- I care deeply about privacy, workspace separation, redaction, local SQLite operation, reliable backups, and not losing data.
- I dislike unnecessary settings, duplicate screens, excessive warnings, unclear labels, and workflows that make me guess what to do.
- I want the system to feel like a calm operating partner, not a complicated admin console.

Safety and architectural constraints:

- Preserve workspace isolation.
- Preserve existing permissions.
- Preserve secret redaction.
- Never expose API keys, raw credentials, account numbers, or sensitive CSV values.
- Keep SQLite local mode working.
- Do not silently delete user data.
- Do not rewrite existing migrations or source-control history.
- Do not add payments, transfers, creditor communication, credit applications, Plaid, or external financial execution unless explicitly requested later.
- Do not use an LLM for financial arithmetic.
- Keep monetary calculations deterministic with integer minor units or Decimal.
- Preserve approval gates for consequential external actions.
- Do not add new abstraction layers unless they remove real complexity.
- Keep mock/local tests deterministic.
- Use synthetic fixtures for tests.
- Do not claim something works unless it is actually tested.

Your task:

1. Audit the current system against my actual goals.
2. Map every major user journey from first launch to daily use.
3. Identify where I still have to guess what to upload, what to click, what approval means, or what happens next.
4. Identify duplicate screens, unnecessary concepts, dead controls, placeholder behavior, confusing terminology, and incomplete workflows.
5. Prioritize improvements by user value:
   - P0: blocks adding clients, importing real data, starting work, or safely storing data.
   - P1: creates repeated confusion or manual work.
   - P2: polish, speed, clarity, and convenience.
6. Test the existing behavior before changing it.
7. Improve the system in small verified checkpoints.
8. For every change, add focused tests.
9. Run the full backend suite after backend changes.
10. Build the frontend after frontend changes.
11. Use browser verification for the most important journeys:
    - first launch
    - add client
    - client switching
    - CSV upload and preview
    - import approval
    - growth data linked to the correct client
    - finance review
    - debt scenario creation
    - approval and activation
    - OpenRouter configuration
    - MCP diagnostics
12. Prefer one consolidated status source per page instead of many competing API calls.
13. Make every page explain:
    - What this page is for
    - What data it needs
    - Exactly what file or folder to provide
    - What format is accepted
    - What happens after upload
    - Whether the action is read-only, local write, or external write
    - Whether approval is required
    - What the next recommended action is
14. Keep the primary interface calm and compact.
15. Move advanced diagnostics and implementation metadata behind expandable details.
16. Remove UI bloat instead of adding more panels.
17. Make empty states actionable and specific.
18. Make errors understandable and recoverable.
19. Ensure the client is selected and visible whenever client-specific work is being performed.
20. Prevent accidental cross-client data mixing.
21. Make imports idempotent and easy to retry.
22. Make the AI proactive for safe analysis and drafting, but cautious at external side-effect boundaries.
23. Preserve an audit trail for important changes.
24. Never silently overwrite saved scenarios, plans, client data, or imported records.

SCOPE GUARD — how to sequence the work:

- Work the P0 journey first: first launch → add a real client → CSV upload, preview, and approval → growth data linked to the correct client. Finish and verify that end-to-end before touching P1 or P2.
- One checkpoint at a time. Do not attempt a large multi-area rewrite in a single pass. If a fix touches more than roughly 10 files, split it and tell me the split.
- After each checkpoint: run the relevant tests, then the full backend suite for backend changes, commit on the work branch with a clear message, and give me the short report below before starting the next checkpoint.

OPTIONAL RESOURCE (only after P0 is done, and only if it serves the "one clear next action" goal):

An ADHD-first CEO layer already exists at https://github.com/GunsNR/claude-skills-hub under smart-os/ — one-line task capture with automatic classification, Top 3 priorities, quick wins, delegation to my developer Dilshan with WhatsApp/email notify, tax set-aside tracking, Obsidian memory, morning brief, and recurring tasks, with 65 passing tests. Its docs/NEXT_AGENT_RESUME_PROMPT.md and docs/INTEGRATION_GUIDE.md describe exactly how to mount it into this backend (ceo_db.configure(engine=...) plus include_router; all its tables are prefixed ceo_ so they coexist cleanly). Integrating it is optional — propose it to me as its own checkpoint if you think it fits; do not fold it into the P0 work.

For every proposed or implemented improvement, report:

- User problem
- Evidence in the current code or tests
- Exact files changed
- Behavior before
- Behavior after
- Tests added or run
- Remaining uncertainty
- Whether the change is safe to release

At the end, produce:

- A plain-English map of the system
- A prioritized product backlog
- A simplified ideal navigation structure
- A list of workflows that are fully verified
- A list of workflows requiring live/manual verification
- A list of risky or intentionally unbuilt capabilities
- A proposed next checkpoint with a narrow scope

Do not regenerate a giant specification. Work from the repository and improve the highest-value user journey first.
```

---

## What changed from your draft (so you know it wasn't just copied)

1. **Removed** the line about the "Self improvement" home-chats project.
   Claude Code on your PC cannot read your claude.ai chat projects — that line
   would have been silently ignored or, worse, guessed at. Replaced with:
   read the repo's own docs and git history.
2. **Added a pre-flight gate**: clean tree check, commit hash check, and one
   baseline test run BEFORE any change. If 359-passed doesn't reproduce, it
   stops and tells you instead of building on a broken base.
3. **Added branch discipline**: all work on `optimize/ux-audit`, never on
   main, one small verified commit per checkpoint.
4. **Added a scope guard**: P0 journey first (launch → add client → CSV
   import → linked growth data), finished end-to-end before anything else.
   No giant one-pass rewrite.
5. **Added the CEO layer as an optional, clearly-fenced resource** — the
   agent may propose integrating it (it is exactly the "one clear next
   action" experience you asked for), but only after P0 and only as its own
   checkpoint you approve.
6. Everything else — your goals, all safety constraints, the reporting
   format, the final deliverables — kept word for word.

## When it finishes

Paste the agent's final prioritized backlog and its two workflow lists
(verified / needs-manual-verification) back into a cloud session if you want
a second-opinion review. Otherwise, just keep approving checkpoints one at a
time — the prompt is built so you never have to approve more than one small
change at once.
