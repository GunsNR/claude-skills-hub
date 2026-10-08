#!/usr/bin/env python3
"""Build the daily plain-text digest that gets sent to office@ranklogicseo.com.

Usage:
  python3 make_digest.py --date 2026-10-09 \
      --slugs slug-one,slug-two \
      --packet ../impactwindowsseo-backlinks/daily/day-02-2026-10-09.md \
      [--links slug-one=https://impactwindowsseo.com/?p=123&preview=true,...]

Writes digests/<date>.txt. Draft links come only from --links. A post with no
link says "not created yet", never a made-up address.
"""
import argparse
import html
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
from posts import POSTS  # noqa: E402

BASE = "https://impactwindowsseo.com"


def to_text(h):
    h = re.sub(r"\{\{LINK:([a-z0-9-]+)\}\}", lambda m: "%s/%s/" % (BASE, m.group(1)), h)
    h = re.sub(r"</(h2|h3)>", "\n", h)
    h = h.replace("<h2>", "\n\n## ").replace("<h3>", "\n### ")
    h = h.replace("<li>", "\n- ")
    h = re.sub(r"</p>|</aside>|</tr>", "\n", h)
    h = re.sub(r"<td>|<th>", " | ", h)
    h = re.sub(r"<[^>]+>", "", h)
    return re.sub(r"\n{3,}", "\n\n", html.unescape(h)).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True)
    ap.add_argument("--slugs", required=True)
    ap.add_argument("--packet", required=True)
    ap.add_argument("--links", default="")
    a = ap.parse_args()

    links = dict(kv.split("=", 1) for kv in a.links.split(",") if "=" in kv)
    by_slug = {p["slug"]: p for p in POSTS}
    slugs = [s for s in a.slugs.split(",") if s]
    missing = [s for s in slugs if s not in by_slug]
    if missing:
        raise SystemExit("Unknown slugs: " + ", ".join(missing))

    out = ["IMPACT WINDOWS SEO: DAILY CONTENT, " + a.date, "",
           "Drafts and prepared packets only. Nothing here is published or submitted unless a line says so.",
           "Starred (*) facts in SOURCES.md (repo: impactwindowsseo-content) need a human check before publishing.",
           "", "=" * 60, "PART 1: NEW BLOG POSTS", "=" * 60]
    for s in slugs:
        p = by_slug[s]
        out += ["", "TITLE: " + p["title"], "SLUG: " + s, "META DESCRIPTION: " + p["meta"],
                "PRIMARY KEYWORD: " + p["primary_kw"],
                "WORDPRESS DRAFT: " + links.get(s, "not created yet"), "", to_text(p["body"]),
                "", "## Frequently asked questions"]
        for q, ans in p["faq"]:
            out += ["", "Q: " + q, "A: " + ans]
        out += ["", "-" * 60]

    packet = Path(a.packet).read_text(encoding="utf-8")
    packet = re.sub(r"^#+ ", "", packet, flags=re.M).replace("**", "").replace("`", "")
    profile = (HERE.parent / "impactwindowsseo-backlinks" / "business-profile.txt").read_text(encoding="utf-8")
    out += ["", "=" * 60, "PART 2: BACKLINK TARGETS (prepared, not submitted)", "=" * 60, "", packet,
            "", "=" * 60, "BUSINESS DETAILS TO USE ON EVERY FORM", "=" * 60, "", profile]

    text = "\n".join(out)
    if "—" in text:
        raise SystemExit("em dash in digest")
    dest = HERE / "digests"
    dest.mkdir(exist_ok=True)
    (dest / (a.date + ".txt")).write_text(text, encoding="utf-8")
    print("wrote digests/%s.txt (%d words)" % (a.date, len(text.split())))


if __name__ == "__main__":
    main()
