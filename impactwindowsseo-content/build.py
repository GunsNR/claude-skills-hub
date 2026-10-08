#!/usr/bin/env python3
"""Build WordPress-ready HTML (with JSON-LD) from posts.py.

Usage:  python3 build.py
Output: dist/<slug>.html  (paste into a WordPress "Custom HTML" block)
        dist/schema-sitewide.json  (Organization + WebSite, for the homepage/header)

Checks: JSON-LD parses, FAQ markup matches visible FAQ, no em dashes,
title/meta length sane, every internal link resolves to a known slug.
"""
import html
import json
import re
from pathlib import Path

from posts import POSTS

BASE = "https://impactwindowsseo.com"          # confirm
CONTACT_URL = BASE + "/contact/"                # confirm path
PUBLISHED = "2026-10-08"

ORG = {
    "@type": "ProfessionalService",
    "@id": BASE + "/#organization",
    "name": "Impact Windows SEO",
    "url": BASE + "/",
    "telephone": "+1-954-706-6785",
    "description": "SEO agency for impact window contractors and window and door installation companies.",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "5840 Lakeshore Drive",
        "addressLocality": "Fort Lauderdale",
        "addressRegion": "FL",
        "postalCode": "33312",
        "addressCountry": "US",
    },
    "areaServed": {"@type": "State", "name": "Florida"},
    "knowsAbout": [
        "Local SEO",
        "Google Business Profile optimization",
        "SEO for window and door contractors",
        "Impact window marketing",
    ],
}
# Deliberately omitted until real: aggregateRating, review, logo, image,
# openingHours, geo, sameAs. Fake or unverifiable markup risks a manual action.

STYLE = """<style>
.iws-tldr{background:#f3f6fa;border-left:4px solid #0b5cab;padding:14px 18px;margin:24px 0;border-radius:4px}
.iws-cta{background:#0b2545;color:#fff;padding:28px;border-radius:8px;margin:40px 0;text-align:center}
.iws-cta h2{color:#fff;margin-top:0}
.iws-cta a.iws-btn{display:inline-block;background:#ff7a3d;color:#fff;padding:14px 26px;border-radius:999px;font-weight:700;text-decoration:none;margin:8px 0}
.iws-cta a.iws-tel{color:#fff;font-weight:700}
.iws-faq h3{margin-bottom:4px}
.iws-faq p{margin-top:0}
article.iws-post table{border-collapse:collapse;width:100%;margin:20px 0}
article.iws-post th,article.iws-post td{border:1px solid #d5dbe3;padding:10px;text-align:left}
</style>"""

CTA = """<section class="iws-cta">
<h2>Want to see where your window company stands?</h2>
<p>Request a free SEO audit. We review your Google Business Profile, your website, and your top local competitors, then send you a written report.</p>
<p><a class="iws-btn" href="%(contact)s">Request my free audit</a></p>
<p>Or call <a class="iws-tel" href="tel:+19547066785">(954) 706-6785</a></p>
<p>Impact Windows SEO &middot; 5840 Lakeshore Drive, Fort Lauderdale, FL 33312</p>
</section>"""


def url_for(slug):
    return "%s/%s/" % (BASE, slug)


def resolve_links(body, slugs):
    def sub(m):
        slug = m.group(1)
        if slug not in slugs:
            raise SystemExit("Unknown internal link slug: " + slug)
        return url_for(slug)
    return re.sub(r"\{\{LINK:([a-z0-9-]+)\}\}", sub, body)


def graph(post):
    url = url_for(post["slug"])
    return {
        "@context": "https://schema.org",
        "@graph": [
            dict(ORG),
            {
                "@type": "WebPage",
                "@id": url + "#webpage",
                "url": url,
                "name": post["title"],
                "isPartOf": {"@id": BASE + "/#website"},
                "breadcrumb": {"@id": url + "#breadcrumb"},
                "inLanguage": "en-US",
            },
            {
                "@type": "BlogPosting",
                "@id": url + "#article",
                "mainEntityOfPage": {"@id": url + "#webpage"},
                "headline": post["title"],
                "description": post["meta"],
                "datePublished": PUBLISHED,
                "dateModified": PUBLISHED,
                "author": {"@id": BASE + "/#organization"},
                "publisher": {"@id": BASE + "/#organization"},
                "inLanguage": "en-US",
                "keywords": ", ".join([post["primary_kw"]] + post["secondary_kw"]),
            },
            {
                "@type": "BreadcrumbList",
                "@id": url + "#breadcrumb",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"},
                    {"@type": "ListItem", "position": 2, "name": "Blog", "item": BASE + "/blog/"},
                    {"@type": "ListItem", "position": 3, "name": post["title"], "item": url},
                ],
            },
            {
                "@type": "FAQPage",
                "@id": url + "#faq",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a},
                    }
                    for q, a in post["faq"]
                ],
            },
        ],
    }


def faq_html(post):
    parts = ['<section class="iws-faq">', "<h2>Frequently asked questions</h2>"]
    for q, a in post["faq"]:
        parts.append("<h3>%s</h3>\n<p>%s</p>" % (html.escape(q), html.escape(a)))
    parts.append("</section>")
    return "\n".join(parts)


def check(post, rendered, ld):
    assert "—" not in rendered and "—" not in json.dumps(ld, ensure_ascii=False), \
        "em dash found in " + post["slug"]
    assert len(post["meta"]) <= 160, "meta too long (%d) in %s" % (len(post["meta"]), post["slug"])
    assert len(post["title"]) <= 70, "title too long (%d) in %s" % (len(post["title"]), post["slug"])
    for q, a in post["faq"]:
        assert html.escape(q) in rendered and html.escape(a) in rendered, "FAQ mismatch in " + post["slug"]
    json.loads(json.dumps(ld))  # round-trips


def main():
    out = Path(__file__).parent / "dist"
    out.mkdir(exist_ok=True)
    slugs = {p["slug"] for p in POSTS}
    report = []
    for post in POSTS:
        body = resolve_links(post["body"].strip(), slugs)
        ld = graph(post)
        rendered = "\n".join([
            STYLE,
            '<article class="iws-post">',
            "<h1>%s</h1>" % html.escape(post["title"]),
            body,
            faq_html(post),
            CTA % {"contact": CONTACT_URL},
            "</article>",
            '<script type="application/ld+json">',
            json.dumps(ld, indent=2, ensure_ascii=False),
            "</script>",
            "",
        ])
        check(post, rendered, ld)
        (out / (post["slug"] + ".html")).write_text(rendered, encoding="utf-8")
        words = len(re.sub(r"<[^>]+>", " ", body).split())
        report.append((post["slug"], len(post["title"]), len(post["meta"]), words, len(post["faq"])))

    sitewide = {
        "@context": "https://schema.org",
        "@graph": [
            dict(ORG),
            {
                "@type": "WebSite",
                "@id": BASE + "/#website",
                "url": BASE + "/",
                "name": "Impact Windows SEO",
                "publisher": {"@id": BASE + "/#organization"},
                "inLanguage": "en-US",
            },
        ],
    }
    (out / "schema-sitewide.json").write_text(json.dumps(sitewide, indent=2), encoding="utf-8")

    print("%-48s %5s %5s %6s %4s" % ("slug", "title", "meta", "words", "faq"))
    for r in report:
        print("%-48s %5d %5d %6d %4d" % r)


if __name__ == "__main__":
    main()
