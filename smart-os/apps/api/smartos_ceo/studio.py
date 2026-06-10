"""AI Studio: labeled one-click actions for all LLM work.

Each action is a pre-engineered prompt bound to a route class (so cost
routing applies automatically) and an output kind:
- markdown: rendered in the UI
- html:     extracted, saved to the studio output folder, previewed live
- svg:      extracted, saved, rendered inline (logos)

Generated files live under SMARTOS_STUDIO_DIR (default ./studio_output),
one folder per job, served read-only through the API.
"""

import os
import re
from pathlib import Path

from sqlalchemy import select
from sqlalchemy.orm import Session

from . import wiki
from .models import StudioJob

BUSINESS_CONTEXT = (
    "You work for Izzy, the CEO of Rank Logic SEO, an SEO agency. "
    "Outputs must be client-ready, conversion-focused, and concrete. "
    "Never use placeholder lorem ipsum; write real copy from the given input."
)

# Sidebar registry. Order here = order of buttons in the UI.
ACTIONS: dict[str, dict] = {
    "ask": {
        "label": "Ask a Question",
        "icon": "💬",
        "category": "Think",
        "route_class": "fast",
        "output_kind": "markdown",
        "placeholder": "Ask anything…",
        "system": "Answer directly and concisely. Lead with the answer.",
        "prompt": "{input}",
    },
    "strategy": {
        "label": "Strategy Session",
        "icon": "🧠",
        "category": "Think",
        "route_class": "reasoning",
        "output_kind": "markdown",
        "playbook": "growth",
        "placeholder": "Describe the business decision or problem…",
        "system": "You are a sharp business advisor for an SEO agency CEO. "
                  "Give a recommendation first, then reasoning, then risks, "
                  "then a 3-step action plan with what to delegate to Dilshan.",
        "prompt": "{input}",
    },
    "explain": {
        "label": "Explain It Fast",
        "icon": "⚡",
        "category": "Think",
        "route_class": "fast",
        "output_kind": "markdown",
        "placeholder": "Paste or name the thing to understand…",
        "system": "Explain for a smart but busy ADHD reader: 5 bullets max, "
                  "then one 'why you care' line.",
        "prompt": "Explain this:\n{input}",
    },
    "wp_site": {
        "label": "Create WP Website",
        "icon": "🌐",
        "category": "Create",
        "route_class": "coding",
        "output_kind": "html",
        "placeholder": "Business name, trade/niche, location, services, phone…",
        "system": BUSINESS_CONTEXT + " You are an expert web designer.",
        "prompt": (
            "Create a complete, modern, mobile-first one-page website for this "
            "business:\n{input}\n\n"
            "Requirements: single self-contained HTML file (inline CSS, no "
            "external assets), hero with clear CTA, services section, "
            "trust/reviews section, FAQ with schema.org FAQPage JSON-LD, "
            "LocalBusiness JSON-LD, contact section with click-to-call, "
            "SEO title/meta description. Return ONLY the HTML in a ```html "
            "code block, followed by a short markdown section titled "
            "'## WordPress build notes' explaining how to recreate it in WP "
            "(theme suggestion, blocks/plugins, page structure)."
        ),
    },
    "landing": {
        "label": "Create Landing Page",
        "icon": "📄",
        "category": "Create",
        "route_class": "coding",
        "output_kind": "html",
        "placeholder": "Offer, audience, goal of the page…",
        "system": BUSINESS_CONTEXT + " You are a conversion copywriter and designer.",
        "prompt": (
            "Create a high-converting landing page for:\n{input}\n\n"
            "Single self-contained HTML file, inline CSS, mobile-first, one "
            "clear CTA repeated, social proof, objection-handling section. "
            "Return ONLY the HTML in a ```html code block."
        ),
    },
    "logo": {
        "label": "Create Logo",
        "icon": "🎨",
        "category": "Create",
        "route_class": "coding",
        "output_kind": "svg",
        "placeholder": "Brand name, vibe, colors, industry…",
        "system": "You are a minimalist logo designer who outputs clean SVG.",
        "prompt": (
            "Design a simple, professional vector logo for:\n{input}\n\n"
            "Return ONLY one complete <svg> element (viewBox 0 0 400 120, "
            "scalable, no external fonts — use simple shapes and svg <text> "
            "with a generic font-family). Flat design, max 3 colors."
        ),
    },
    "blog": {
        "label": "Write Blog Post",
        "icon": "✍️",
        "category": "Create",
        "route_class": "growth",
        "output_kind": "markdown",
        "playbook": "growth",
        "placeholder": "Topic, target keyword, audience, client site…",
        "system": BUSINESS_CONTEXT + " You write SEO content that ranks and reads naturally.",
        "prompt": (
            "Write an SEO-optimized blog post about:\n{input}\n\n"
            "Include: compelling title (under 60 chars), meta description "
            "(under 155 chars), H2/H3 structure, FAQ section, and a short "
            "internal-linking suggestion list at the end."
        ),
    },
    "social": {
        "label": "Social Posts Pack",
        "icon": "📣",
        "category": "Create",
        "route_class": "growth",
        "output_kind": "markdown",
        "placeholder": "Topic or piece of content to promote…",
        "system": BUSINESS_CONTEXT,
        "prompt": (
            "Create a social pack for:\n{input}\n\n"
            "Deliver: 3 LinkedIn posts (different hooks), 5 X/Twitter posts, "
            "2 Instagram captions with hashtag sets, 1 short video script "
            "(30s, spoken style)."
        ),
    },
    "proposal": {
        "label": "Client Proposal",
        "icon": "🤝",
        "category": "Sell",
        "route_class": "growth",
        "output_kind": "markdown",
        "playbook": "sales",
        "placeholder": "Client name, their business, what they need, budget feel…",
        "system": BUSINESS_CONTEXT + " Anchor on outcomes (leads, rankings, revenue), not deliverables.",
        "prompt": (
            "Write an SEO services proposal for:\n{input}\n\n"
            "Structure: situation summary, goals, recommended plan (3 phases), "
            "deliverables per month, expected outcomes timeline, investment "
            "options (3 tiers), next step. Confident, no fluff."
        ),
    },
    "outreach": {
        "label": "Cold Outreach Email",
        "icon": "📧",
        "category": "Sell",
        "route_class": "growth",
        "output_kind": "markdown",
        "playbook": "sales",
        "placeholder": "Who you're emailing and the angle/observation…",
        "system": BUSINESS_CONTEXT,
        "prompt": (
            "Write a cold outreach email for:\n{input}\n\n"
            "Under 120 words, personal opening based on the input, one "
            "specific value observation, soft CTA. Then give 2 alternative "
            "subject lines and a 3-line follow-up email for day 4."
        ),
    },
    "audit": {
        "label": "SEO Audit Plan",
        "icon": "🔍",
        "category": "SEO",
        "route_class": "growth",
        "output_kind": "markdown",
        "playbook": "seo_delivery",
        "placeholder": "Site URL, niche, known issues…",
        "system": BUSINESS_CONTEXT + " You are a senior technical SEO.",
        "prompt": (
            "Create a prioritized SEO audit plan for:\n{input}\n\n"
            "Sections: quick wins (first 7 days), technical checks, on-page, "
            "content gaps, local SEO if relevant, links. For each item: what "
            "to check, tool to use, who should do it (Dilshan vs CEO). "
            "Format as a checklist Dilshan can execute."
        ),
    },
    "keywords": {
        "label": "Keyword Ideas",
        "icon": "🔑",
        "category": "SEO",
        "route_class": "growth",
        "output_kind": "markdown",
        "placeholder": "Client niche, location, services…",
        "system": BUSINESS_CONTEXT,
        "prompt": (
            "Generate a keyword strategy for:\n{input}\n\n"
            "Deliver a table of 25 keywords: keyword, intent (info/commercial/"
            "transactional/local), difficulty guess (low/med/high), suggested "
            "page type. Then list 5 content cluster ideas."
        ),
    },
    "rewrite": {
        "label": "Rewrite / Improve",
        "icon": "🪄",
        "category": "Polish",
        "route_class": "fast",
        "output_kind": "markdown",
        "placeholder": "Paste the text to improve (note the goal if any)…",
        "system": "Rewrite to be clearer, tighter, and more persuasive. "
                  "Keep the author's voice. Return only the rewrite, then a "
                  "one-line note on what you changed.",
        "prompt": "{input}",
    },
    "summarize": {
        "label": "Summarize Anything",
        "icon": "📝",
        "category": "Polish",
        "route_class": "summarization",
        "output_kind": "markdown",
        "placeholder": "Paste the long thing…",
        "system": "Summarize for a busy CEO: 5 bullets, then action items if any.",
        "prompt": "Summarize:\n{input}",
    },
    "code": {
        "label": "Code Helper",
        "icon": "👨‍💻",
        "category": "Polish",
        "route_class": "coding",
        "output_kind": "markdown",
        "placeholder": "Describe the code you need or paste the error…",
        "system": "You are a pragmatic senior developer. Working code first, "
                  "brief explanation after.",
        "prompt": "{input}",
    },
}

HTML_FALLBACK = ("<!DOCTYPE html><html><head><meta charset='utf-8'>"
                 "<title>Draft</title></head><body><pre style='white-space:"
                 "pre-wrap;font-family:sans-serif;max-width:720px;margin:40px "
                 "auto'>{text}</pre></body></html>")
SVG_FALLBACK = ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 400 120'>"
                "<rect width='400' height='120' fill='#181b25'/>"
                "<text x='200' y='66' text-anchor='middle' fill='#6ee7b7' "
                "font-family='sans-serif' font-size='20'>draft — rerun with "
                "a live model</text></svg>")


def studio_dir() -> Path:
    path = Path(os.environ.get("SMARTOS_STUDIO_DIR", "studio_output"))
    path.mkdir(parents=True, exist_ok=True)
    return path


def list_actions() -> list[dict]:
    return [{"id": aid, "label": a["label"], "icon": a["icon"],
             "category": a["category"], "output_kind": a["output_kind"],
             "placeholder": a["placeholder"], "route_class": a["route_class"]}
            for aid, a in ACTIONS.items()]


def _extract_html(text: str) -> tuple[str, str]:
    """Return (html, remaining_notes)."""
    fence = re.search(r"```html\s*(.*?)```", text, re.S)
    if fence:
        return fence.group(1).strip(), (text[fence.end():]).strip()
    doc = re.search(r"<!DOCTYPE html.*</html>", text, re.S | re.I)
    if doc:
        return doc.group(0), ""
    return HTML_FALLBACK.format(text=text[:4000]), text


def _extract_svg(text: str) -> str:
    match = re.search(r"<svg[^>]*>.*?</svg>", text, re.S | re.I)
    return match.group(0) if match else SVG_FALLBACK


def run(db: Session, action_id: str, user_input: str, gateway,
        cost_router) -> StudioJob | None:
    action = ACTIONS.get(action_id)
    if action is None:
        return None
    system = action["system"]
    if action.get("playbook"):
        system += ("\n\nOperating playbook (follow it):\n"
                   + wiki.get_context(db, action["playbook"]))
    prompt = action["prompt"].format(input=user_input)
    job = StudioJob(action_id=action_id, label=action["label"],
                    input_text=user_input, output_kind=action["output_kind"])
    try:
        result = gateway.generate(action["route_class"], prompt, system=system)
    except Exception as exc:
        job.status = "failed"
        job.output_text = f"Model call failed: {type(exc).__name__}"
        db.add(job)
        db.commit()
        return job
    cost_router.record_usage(action["route_class"], result["model"],
                             result["tokens"], result["est_cost"])
    job.model_used = result["model"]
    job.tokens = result["tokens"]
    job.est_cost = result["est_cost"]
    db.add(job)
    db.commit()  # commit first so job.id exists for the file folder

    text = result["text"]
    if action["output_kind"] == "html":
        html, notes = _extract_html(text)
        job_dir = studio_dir() / str(job.id)
        job_dir.mkdir(parents=True, exist_ok=True)
        (job_dir / "index.html").write_text(html, encoding="utf-8")
        job.file_name = "index.html"
        job.output_text = notes or "Site generated."
    elif action["output_kind"] == "svg":
        svg = _extract_svg(text)
        job_dir = studio_dir() / str(job.id)
        job_dir.mkdir(parents=True, exist_ok=True)
        (job_dir / "logo.svg").write_text(svg, encoding="utf-8")
        job.file_name = "logo.svg"
        job.output_text = svg
    else:
        job.output_text = text
    db.commit()
    return job


def get_file(job_id: int, file_name: str) -> Path:
    """Resolve a generated file safely inside the studio dir."""
    base = studio_dir().resolve()
    target = (base / str(job_id) / file_name).resolve()
    if not target.is_relative_to(base) or not target.is_file():
        raise FileNotFoundError(file_name)
    return target


def history(db: Session, limit: int = 30) -> list[StudioJob]:
    return list(db.scalars(select(StudioJob)
                           .order_by(StudioJob.created_at.desc())
                           .limit(limit)))
