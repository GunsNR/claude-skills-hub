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
article.iws-post{--ink:#0e1726;--muted:#5b6678;--line:#e3e8ef;--navy:#0b2545;--blue:#1565d8;--accent:#1565d8;--accent-ink:#ffffff;--soft:#f5f8fc;
  max-width:760px;margin:0 auto;color:var(--ink);font-size:18px;line-height:1.7;
  font-family:Inter,ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;-webkit-font-smoothing:antialiased}
article.iws-post *{box-sizing:border-box}
article.iws-post p,article.iws-post li{color:var(--ink)}
article.iws-post a{color:var(--blue);text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:3px}
article.iws-post a:hover{text-decoration-thickness:2px}
.iws-progress{position:fixed;top:0;left:0;right:0;height:4px;z-index:9999;background:transparent;pointer-events:none}
.iws-progress span{display:block;height:4px;background:var(--accent);transform:scaleX(0);transform-origin:0 50%}
.iws-hero{padding:8px 0 28px;border-bottom:1px solid var(--line);margin-bottom:32px}
.iws-kicker{display:inline-block;font-size:13px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--blue);background:#e8f0fd;padding:6px 12px;border-radius:999px;margin-bottom:16px}
article.iws-post h1{font-size:clamp(32px,5vw,46px);line-height:1.12;letter-spacing:-.02em;margin:0 0 14px;color:var(--navy);font-weight:800}
.iws-meta{color:var(--muted);font-size:15px;display:flex;flex-wrap:wrap;gap:6px 18px}
article.iws-post h2{font-size:clamp(24px,3.4vw,30px);line-height:1.25;letter-spacing:-.01em;color:var(--navy);margin:48px 0 14px;font-weight:750;scroll-margin-top:80px}
article.iws-post h2::before{content:"";display:block;width:44px;height:4px;border-radius:4px;background:var(--accent);margin-bottom:14px}
article.iws-post h3{font-size:20px;color:var(--navy);margin:28px 0 8px}
article.iws-post ul,article.iws-post ol{padding-left:1.3em}
article.iws-post li{margin:6px 0}
article.iws-post li::marker{color:var(--blue);font-weight:700}
.iws-tldr{display:block;position:relative;background:var(--soft);border:1px solid #d6e3f7;border-radius:16px;padding:22px 24px 22px 26px;margin:28px 0;box-shadow:0 1px 0 rgba(14,23,38,.03),0 12px 32px -18px rgba(21,101,216,.35)}
.iws-tldr::before{content:"";position:absolute;left:0;top:18px;bottom:18px;width:4px;border-radius:4px;background:var(--accent)}
.iws-tldr strong:first-child{display:block;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--blue);margin-bottom:6px}
.iws-toc{border:1px solid var(--line);border-radius:16px;padding:18px 22px;margin:8px 0 8px;background:#fff}
.iws-toc b{display:block;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin-bottom:8px}
.iws-toc ol{margin:0;padding-left:1.2em;display:grid;grid-template-columns:1fr 1fr;gap:2px 32px}
.iws-toc li{font-size:15.5px;margin:4px 0}
.iws-toc a{text-decoration:none}
article.iws-post table{border-collapse:separate;border-spacing:0;width:100%;margin:24px 0;font-size:16px;border:1px solid var(--line);border-radius:14px;overflow:hidden}
article.iws-post th{background:var(--navy);color:#fff;text-align:left;padding:12px 14px;font-weight:650}
article.iws-post td{padding:12px 14px;border-top:1px solid var(--line);vertical-align:top}
article.iws-post tr:nth-child(even) td{background:var(--soft)}
.iws-figure{margin:28px 0}
.iws-figure img{width:100%;height:auto;border-radius:16px;display:block;box-shadow:0 18px 40px -24px rgba(14,23,38,.45)}
.iws-figure figcaption{font-size:14px;color:var(--muted);margin-top:8px}
.iws-card{border:1px solid var(--line);border-radius:18px;overflow:hidden;margin:28px 0;background:#fff;box-shadow:0 24px 48px -30px rgba(14,23,38,.4)}
.iws-card-top{height:96px;background:linear-gradient(135deg,#dfe9f8,#f6efe9)}
.iws-card-body{padding:18px 22px 20px}
.iws-card-name{font-size:22px;font-weight:750;color:var(--navy);margin:0}
.iws-card-cat{color:var(--muted);font-size:15px;margin:2px 0 14px}
.iws-card-actions{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:14px}
.iws-card-actions span{border:1px solid #c9d6ea;color:var(--blue);border-radius:999px;padding:7px 14px;font-size:14px;font-weight:600}
.iws-card-rows{display:grid;gap:8px;font-size:15px}
.iws-card-rows div{display:flex;gap:10px}
.iws-card-rows i{font-style:normal;color:var(--muted);min-width:96px}
.iws-card-note{font-size:13px;color:var(--muted);padding:10px 22px;border-top:1px solid var(--line);background:var(--soft)}
.iws-faq{margin-top:48px}
.iws-faq details{border:1px solid var(--line);border-radius:14px;padding:4px 18px;margin:10px 0;background:#fff;transition:box-shadow .2s}
.iws-faq details[open]{box-shadow:0 14px 30px -22px rgba(14,23,38,.45)}
.iws-faq summary{cursor:pointer;list-style:none;font-weight:650;color:var(--navy);padding:14px 28px 14px 0;position:relative}
.iws-faq summary::-webkit-details-marker{display:none}
.iws-faq summary::after{content:"+";position:absolute;right:0;top:10px;font-size:24px;color:var(--blue);transition:transform .2s}
.iws-faq details[open] summary::after{transform:rotate(45deg)}
.iws-faq details p{margin:0 0 16px;color:var(--muted)}
.iws-sources{font-size:15px;background:var(--soft);border-radius:14px;padding:16px 20px 16px 2.2em}
article.iws-post .iws-cta{position:relative;overflow:hidden;display:block;background:var(--navy);color:#fff;padding:44px 32px;border-radius:22px;margin:56px 0 24px;text-align:center}
article.iws-post .iws-cta::after{content:"";position:absolute;width:320px;height:320px;right:-120px;top:-140px;border-radius:50%;background:radial-gradient(circle,rgba(21,101,216,.55),transparent 70%);pointer-events:none}
article.iws-post .iws-cta-inner{position:relative;z-index:1;display:flex;flex-direction:column;align-items:center;gap:0;max-width:560px;margin:0 auto}
article.iws-post .iws-cta h2{color:#fff;margin:0 0 12px;text-align:center}
article.iws-post .iws-cta h2::before{margin:0 auto 14px;background:#fff;opacity:.5}
article.iws-post .iws-cta p{display:block;float:none;width:auto;margin:0 0 20px;color:#dbe6f5;text-align:center}
article.iws-post .iws-cta-actions{display:flex;flex-direction:column;align-items:center;gap:12px;margin:4px 0 22px}
article.iws-post .iws-cta a.iws-btn{display:inline-block;background:var(--accent);color:var(--accent-ink);padding:15px 32px;border-radius:999px;font-weight:750;text-decoration:none;line-height:1.2;box-shadow:0 12px 26px -12px rgba(0,0,0,.6);transition:transform .2s,box-shadow .2s}
article.iws-post .iws-cta a.iws-btn:hover{transform:translateY(-2px)}
article.iws-post .iws-cta-or{color:#dbe6f5;font-size:16px}
article.iws-post .iws-cta a.iws-tel{color:#fff;font-weight:700}
article.iws-post .iws-cta-addr{font-size:14px;color:#a9bbd6;margin:0;padding-top:18px;border-top:1px solid rgba(255,255,255,.14);width:100%}
.iws-js .iws-reveal{opacity:0;transform:translateY(26px);transition:opacity .7s cubic-bezier(.2,.7,.2,1),transform .7s cubic-bezier(.2,.7,.2,1)}
.iws-js .iws-reveal.is-in{opacity:1;transform:none}
@media (max-width:640px){article.iws-post{font-size:17px}.iws-toc ol{grid-template-columns:1fr}article.iws-post .iws-cta{padding:34px 20px}article.iws-post table{display:block;overflow-x:auto}}
@media (prefers-reduced-motion:reduce){.iws-js .iws-reveal{opacity:1;transform:none;transition:none}.iws-progress{display:none}}
</style>"""

SCRIPT = """<script>
(function(){
  var a=document.querySelector('article.iws-post'); if(!a) return;
  a.classList.add('iws-js');
  var items=a.querySelectorAll('.iws-reveal');
  var still=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(still||!('IntersectionObserver' in window)){for(var i=0;i<items.length;i++){items[i].classList.add('is-in');}}
  else{var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('is-in');io.unobserve(e.target);}});},{rootMargin:'0px 0px -8% 0px'});
    for(var j=0;j<items.length;j++){io.observe(items[j]);}}
  var bar=a.querySelector('.iws-progress span');
  function prog(){if(!bar)return;var r=a.getBoundingClientRect();var h=r.height-window.innerHeight;var v=h>0?Math.min(1,Math.max(0,-r.top/h)):1;bar.style.transform='scaleX('+v+')';}
  window.addEventListener('scroll',prog,{passive:true}); prog();
})();
</script>"""

CTA = """<section class="iws-cta iws-reveal"><div class="iws-cta-inner">
<h2>Want to see where your window company stands?</h2>
<p>Request a free SEO audit. We review your Google Business Profile, your website, and your top local competitors, then send you a written report.</p>
<div class="iws-cta-actions"><a class="iws-btn" href="%(contact)s">Request my free audit</a><span class="iws-cta-or">Or call <a class="iws-tel" href="tel:+19547066785">(954) 706-6785</a></span></div>
<p class="iws-cta-addr">Impact Windows SEO &middot; 5840 Lakeshore Drive, Fort Lauderdale, FL 33312</p>
</div></section>"""

# Illustration of the parts of a business profile. Deliberately generic: no Google
# logo or trade dress, no star rating, no review count. Insert with {{PROFILE_CARD}}.
PROFILE_CARD = """<figure class="iws-card iws-reveal" aria-label="Illustration of the main parts of a business profile">
<div class="iws-card-top"></div>
<div class="iws-card-body">
<p class="iws-card-name">Your Window Company</p>
<p class="iws-card-cat">Primary category &middot; Fort Lauderdale, FL</p>
<div class="iws-card-actions"><span>Website</span><span>Directions</span><span>Call</span><span>Save</span></div>
<div class="iws-card-rows">
<div><i>Address</i><span>Your real street address, or a service area</span></div>
<div><i>Hours</i><span>Your real opening hours</span></div>
<div><i>Phone</i><span>Your main local number</span></div>
<div><i>Services</i><span>Every product you install, each described</span></div>
<div><i>Photos</i><span>Your own install, crew, and truck photos</span></div>
</div>
</div>
<figcaption class="iws-card-note">Illustration of the parts of a business profile. Not a screenshot of Google.</figcaption>
</figure>"""

MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]


def nice_date(d):
    y, m, dd = d.split("-")
    return "%s %d, %s" % (MONTHS[int(m) - 1], int(dd), y)


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", re.sub(r"<[^>]+>", "", text).lower()).strip("-")[:60]


def enhance(body, post):
    """Add ids to H2s, a contents box, reveal wrappers, figures, sources styling."""
    body = body.replace("{{PROFILE_CARD}}", PROFILE_CARD)
    for i, img in enumerate(post.get("images", [])):
        fig = '<figure class="iws-figure iws-reveal"><img src="%s" alt="%s" loading="lazy" decoding="async">%s</figure>' % (
            html.escape(img["src"], quote=True), html.escape(img["alt"], quote=True),
            "<figcaption>%s</figcaption>" % html.escape(img["caption"]) if img.get("caption") else "")
        body = body.replace("{{IMAGE:%d}}" % (i + 1), fig)
    body = re.sub(r"<h2>Sources</h2>\s*<ul>", '<h2 id="sources">Sources</h2>\n<ul class="iws-sources">', body)
    toc = []

    def h2(m):
        text = m.group(1)
        hid = slugify(text)
        if text.strip().lower() != "sources":
            toc.append((hid, re.sub(r"<[^>]+>", "", text)))
        return '<h2 id="%s">%s</h2>' % (hid, text)
    body = re.sub(r"<h2>(.*?)</h2>", h2, body)
    parts = re.split(r'(?=<h2 id=")', body)
    intro, sections = parts[0], parts[1:]
    wrapped = "".join('<section class="iws-reveal">\n%s</section>\n' % sec for sec in sections)
    toc_html = ""
    if len(toc) >= 3:
        toc_html = '<nav class="iws-toc" aria-label="In this guide"><b>In this guide</b><ol>%s</ol></nav>\n' % "".join(
            '<li><a href="#%s">%s</a></li>' % (hid, html.escape(t)) for hid, t in toc)
    return intro + toc_html + wrapped


def hero(post, body):
    words = len(re.sub(r"<[^>]+>", " ", body).split())
    mins = max(1, round(words / 230))
    return ('<div class="iws-progress" aria-hidden="true"><span></span></div>\n'
            '<header class="iws-hero">\n<span class="iws-kicker">%s</span>\n<h1>%s</h1>\n'
            '<div class="iws-meta"><span>By Impact Windows SEO</span><span>Updated %s</span><span>%d min read</span></div>\n'
            '</header>') % (html.escape(post.get("kicker", "Window company marketing")),
                            html.escape(post["title"]), nice_date(post["date"]), mins)


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
                "datePublished": post.get("date", PUBLISHED),
                "dateModified": post.get("date", PUBLISHED),
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
    parts = ['<section class="iws-faq iws-reveal">', '<h2 id="faq">Frequently asked questions</h2>']
    for i, (q, a) in enumerate(post["faq"]):
        parts.append("<details%s><summary>%s</summary>\n<p>%s</p></details>" % (
            " open" if i == 0 else "", html.escape(q), html.escape(a)))
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
    # No promises from us. Hard-fail on first-person guarantees and promised outcomes.
    banned = [r"\bwe guarantee\b", r"\bguaranteed? (results|leads|rankings|calls)\b(?! it)",
              r"\byou will (rank|save|get more|see)\b", r"\bwill rank\b", r"\b100%\b",
              r"\bpage one in\b(?! a week is guessing)"]
    text = re.sub(r"<(style|script)[^>]*>.*?</\1>", " ", rendered, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    for pat in banned:
        for m in re.finditer(pat, text, flags=re.I):
            ctx = text[max(0, m.start() - 60): m.end() + 60].replace("\n", " ")
            # allowed only inside a "never write / red flag" warning
            if re.search(r"never write|red flag|should end the call|not be|do not promise|cannot", ctx, re.I):
                continue
            raise AssertionError("possible guarantee in %s: ...%s..." % (post["slug"], ctx))


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
            hero(post, body),
            enhance(body, post),
            faq_html(post),
            CTA % {"contact": CONTACT_URL},
            "</article>",
            SCRIPT,
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
