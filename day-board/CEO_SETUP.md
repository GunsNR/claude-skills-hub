# CEO Layer — setup

Three things, each with one job. Total setup time: about 30 minutes, once.

| Layer | What it's for | Where it lives |
|---|---|---|
| **Day Board — Clients tab** | Who needs you today, and whether each retainer is defensible | Already on your phone |
| **Money sheet** | The financial truth, syncing everywhere | Google Sheets |
| **Claude Project** | The coach — where to aim, pitfall checks | Claude phone app |

---

## Part 1 — The Clients tab (already done, nothing to install)

Open your Day Board. There are now two tabs at the top: **Today** and **Clients**.

Your five clients are already loaded with their real fees. Every one currently shows **red**, because none has a proof metric set yet. That's accurate, not a bug — it's the actual state of things.

### What to do, once per client (about 5 minutes each)

1. Tap a client
2. **Proof metric** — type the one number they care about. Not a dashboard. Examples:
   - ABA / medical intake (Bridge Care, Atlas Care, PHC): `form submissions`
   - Dental (Toothology): `calls from Google` or `appointment requests`
3. **Where it comes from** — tap one. All free, all things you already have:
   - **GA4 form submits** — for lead forms
   - **Calls from Google** — Google Business Profile Insights
   - **GSC clicks** — use only as backup; it proves visibility, not business
   - **They tell me** — if the client reports their own numbers
4. **This month's number** — type the real figure from that source. Never an estimate.
5. **Last report sent** and **Last contact** — pick the real dates
6. **Contract renewal date** — from the signed agreement
7. Save

### Daily use

- Open the Clients tab. The line at the top — **"Where to aim today"** — names the one client who needs you most, and what it costs you if you ignore it. That's the whole feature.
- Tap **Spoke today** or **Report sent** after any client contact. Two seconds, and it keeps the board honest.

### What the colours mean

| | |
|---|---|
| **Red** | No proof metric, or 45+ days without a report, or 21+ days without contact, or renewal inside 30 days |
| **Amber** | Metric declining two months running, or a report/contact getting late, or renewal inside 60 days |
| **Green** | Reported, contacted, evidenced |

**No proof metric outranks everything else.** An un-evidenced $2,700/month retainer is more at risk than a well-evidenced one you're a week late on.

---

## Part 2 — The money sheet (10 minutes, once)

I've sent you `ranklogic-money.xlsx`. It has your real numbers already in it.

1. Open **drive.google.com** on your PC
2. Drag the file into the browser window — it uploads
3. Right-click it → **Open with** → **Google Sheets**
4. Go to **File → Save as Google Sheets** so it becomes a live sheet
5. Copy the address from your browser's address bar
6. In your Day Board, tap **⚙**, and add a line to Quick Access:
   ```
   Money | PASTE-THE-ADDRESS-HERE
   ```
7. Tap Save

### How to read it

- **Blue numbers** — you type these. Client fees, costs, the two rates in column D.
- **Black numbers** — calculated. Don't type over them or you break the sheet.
- **Yellow** — the tax rate. It's set to 30% as a conservative placeholder. **This is not tax advice.** Confirm your real rate with an accountant and change that one cell.

### The number that matters

The green row, **"Real take-home after set-aside"** — currently about **$3,500/month**, not the $4,997 net. The difference is tax money that isn't yours. Right now you aren't setting it aside, so treat that gap as a debt accumulating quietly.

### Monthly, on the 1st (20 minutes)

1. Update any fee or cost that changed
2. Log each client's proof metric number in the Day Board
3. **Move the tax set-aside amount into a separate account.** Not a mental note — an actual transfer.
4. Check the top-2 concentration figure

---

## Part 3 — The Claude Project (10 minutes, once)

This is your coach. It lives on your phone.

1. Open the **Claude** app
2. Tap the menu (☰, top left) → **Projects** → **+ New Project**
3. Name it: `Rank Logic CEO`
4. Find **Project instructions** (or "Set custom instructions") and paste everything in the box below
5. Save

```
You are my business coach and CEO adviser for Rank Logic SEO. Direct tone. No flattery, no lectures, no moralising, no reassurance essays.

WHO I AM
I'm Izzy, majority owner and CEO. My edge is people — trust, de-escalation, reading a room, community relationships in the frum Jewish world. That's how clients come to me. My gap is follow-through on unglamorous technical and admin work; it stalls, then I feel bad about it, then it stalls more. I have ADHD. I understand concepts fine; I struggle with technical detail. My recovery program anchors my day and comes before all business work.

THE BUSINESS (as of Aug 2026)
- 5 clients: PHC Medical $2,700 (starts Sept), Bridge Care $2,500, Stageit $1,750, Toothology $1,650, Atlas Care $1,450. All on signed contracts with real terms.
- MRR $10,050 from September. Net about $4,997/mo. After a 30% tax set-aside, real take-home is about $3,500/mo.
- Dilshan (Sri Lanka) is team manager, developer, engineer and lead strategist on a 35% royalty. He manages a junior SEO (Dheelakah, $375/mo) and a designer (Lakshani, $320/mo).
- Tracking budget is tight: clients won't fund more than ~$100/mo. We use GA4, GSC and Google Business Profile only. All free. Don't propose paid call-tracking.

THE THREE RISKS — hold me to these
1. Concentration: Bridge Care + PHC are 52% of revenue. Losing PHC costs about $1,755/mo net.
2. Dilshan is a single point of failure and I can't evaluate technical work myself. If he left I couldn't service one account.
3. I don't set aside tax money. About $1,500/mo should be moving to a separate account and isn't.

HOW TO WORK WITH ME
- Never write my task list. I set tasks; you interview, shape, and hold limits.
- Break work into 10-45 minute pieces with a checkable "Done =". Max 1-3 per day.
- For admin/technical tasks, make me name the exact first physical move — the tab, the file, the click.
- For anything I launch or sell, ask "how will we know it worked" BEFORE anything else. I launch faster than I measure.
- Be my QC layer. Assume I didn't read the fine print. Ask "what haven't you verified?" before any spend or commitment.
- If I lean on instinct ("I have a good feeling"), make me give 2-3 concrete written reasons first.
- If I'm beating myself up, don't reassure me — redirect to the next 10-minute action.
- If I'm generating new ideas while a committed deliverable sits unfinished, name it once, then help me finish the deliverable.
- Never invent numbers. Use ranges and label what's unknown.
- Protecting existing revenue beats chasing new revenue. Retention is priority one.
```

### The five prompts to use

Save these somewhere you can copy them, or just retype the gist — the Project instructions do most of the work.

**Weekly review (Friday, 15 min)**
```
Friday CEO review. One question at a time, evidence only.
1. What actually shipped this week?
2. What got dropped or carried 3+ days?
3. Which clients still have no proof metric or a declining one?
4. Did admin stall again? If so, which ONE admin task gets a 10-minute slice Monday?
5. Next week's ONE priority — I name it, you make me pick exactly one.
Then seed Monday: that priority plus 1-3 tasks I set myself.
```

**Before any client call**
```
I have a call with [CLIENT] in [TIME]. Brief me: what I should know, what they're likely to raise, what I should ask, and the one number I should be ready to defend. Ask me what I don't know before you assume it.
```

**Read my numbers**
```
Here's a figure from [GA4 / Google Business Profile / GSC] for [CLIENT]: [paste or describe]. Tell me in plain English what it means, whether it's good or bad for this client, and the one sentence I should put in their report.
```

**Translate Dilshan**
```
Dilshan sent me this technical update: [paste]. Give me: (1) what it means in plain English, (2) whether it's good, bad, or neutral for the client, (3) the one question I should ask him back.
```

**Before spending or committing**
```
I'm about to [spend / sign / commit to] this: [details]. You are my QC layer. Assume I did not read the fine print. What haven't I verified? What's the cancellation term? What happens in month 7? Give it to me straight, once.
```

---

## What you own, and what AI can carry

### Only you — never delegate these
- Every client relationship and retention conversation
- Pricing, and what gets sold
- The Dilshan relationship, and planning for what happens if he leaves
- Final sign-off on any spend or commitment
- **Actually moving the tax money**

### You can fully rely on AI today
- Drafting client reports from real data
- Proofreading and fact-checking everything client-facing before it ships
- Reading contracts and fine print, and flagging terms
- All monthly financial math
- Briefing you before any client call
- Turning Dilshan's technical updates into plain English
- Competitor and SERP research
- Follow-up sequences, check-in messages, content briefs, meta descriptions, GBP posts
- Catching a missing measurement loop before you launch anything

### What you need to learn — in priority order
1. **How to read a GA4 key-event report and a GBP Insights panel.** Under an hour to learn. It ends your dependence on someone else telling you whether your own clients are getting results. Highest-leverage technical skill on this list by a wide margin.
2. **What each client costs you to serve, and what margin each carries.** You have five clients — this is arithmetic, not accounting.
3. **Why 52% concentration is dangerous, and what number is safe.** (Rule of thumb: no client above 20%, no two above 35%.)
4. **What retention actually requires operationally** — a fixed reporting cadence and visible proof of value, not just a good relationship.
5. **Enough SEO literacy to evaluate Dilshan's work** — not to do it. Different skill, much smaller.

---

## The honest summary

Your margins are healthy — about 50% net, which is a well-run agency shape. Your constraint is scale, not efficiency. Five clients at ~$10K MRR is a real business but a small one, and the gap to where you want to be is years of steady client addition, not one clever move.

The two things that would move your trajectory most, starting this week:
1. **Get a proof metric on every client.** It's the cheapest retention insurance that exists, it costs $0, and right now you have none.
2. **Start moving the tax money.** Every month you don't is a bill growing in the dark.
