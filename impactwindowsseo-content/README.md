# Impact Windows SEO: blog drafts and schema

Six posts for impactwindowsseo.com, written for window and door companies, each with BlogPosting, WebPage, BreadcrumbList, FAQPage, and ProfessionalService JSON-LD. Nothing here has been published. This session cannot reach the WordPress site.

## What is in `dist/`

| File | Primary keyword | US searches/mo* | Difficulty* |
|---|---|---|---|
| `seo-for-window-companies.html` | seo for window companies | 40 | 4 |
| `window-replacement-leads.html` | window replacement leads | 90 | 4 |
| `local-seo-for-contractors.html` | local seo for contractors | 1,600 | 19 |
| `google-business-profile-for-window-companies.html` | google business profile for contractors | 70 | 19 |
| `impact-window-marketing-florida.html` | impact windows florida | 720 | 46 |
| `how-to-hire-seo-agency-for-window-company.html` | window contractor marketing | 320 | 9 |
| `schema-sitewide.json` | Organization + WebSite for the homepage | n/a | n/a |

*Semrush US database, 2026-10-08. The niche terms are small. The value is low difficulty and buyers who are ready to talk, not traffic volume. Broader terms like "seo for contractors" (3,600/mo, difficulty 19) are where growth is, and they take a longer content series to win.

## To publish each post

1. In WordPress, create a post. Set the slug to the file name without `.html`.
2. Add one **Custom HTML** block and paste the whole file, including the `<script type="application/ld+json">` block at the bottom.
3. Set the SEO title and meta description in your SEO plugin from `posts.py` (`title`, `meta`).
4. Add a featured image and one or two images inside the post. Use **your own install photos** with descriptive alt text, not stock.
5. Test with Google's Rich Results Test before requesting indexing in Search Console.

**If Yoast or Rank Math is active**, it already outputs Article/WebPage/Breadcrumb schema. Duplicates can confuse Google. In that case delete every node in the pasted JSON-LD except `FAQPage` and `ProfessionalService`.

## Confirm these before publishing

I made these assumptions and could not check them:

- **URLs.** Posts link to `https://impactwindowsseo.com/<slug>/` and the CTA points to `/contact/`. The breadcrumb uses `/blog/`. If your permalinks differ, change `BASE`, `CONTACT_URL`, and the breadcrumb in `build.py` and run `python3 build.py`.
- **The free audit offer.** The CTA promises a free SEO audit with a written report. That came from RankLogic SEO's site. Remove it if Impact Windows SEO does not offer it.
- **Wayne's Roofing mention** in the first post. The facts (331+ Google reviews, number one rated roofing company in Ocean County) come from RankLogic SEO's own client data. Keep it only if you are comfortable crediting the sister company this way.
- **Florida facts** in the Florida post: hurricane season dates, the High Velocity Hurricane Zone covering Miami-Dade and Broward, and insurers being required to offer wind-mitigation discounts. They are stated at a general level. Have someone in the trade read that post before it goes live.
- **No ratings, reviews, logo, hours, or social profiles** are in the schema because you have not given me real ones. Add `logo`, `openingHours`, and `sameAs` when you have them. Never add an `aggregateRating` unless it reflects reviews customers can see on the page.

## A/B title options

Each post has three alternates in `posts.py` under `alt_titles`. Run one at a time for at least a month, and judge by clicks in Search Console.

## Style notes (from the content-style-synthesizer pass)

- **Hook:** a specific number or a direct claim in the first two sentences, then a plain "short version" box.
- **Structure:** hook, summary box, numbered or checklist sections, honest limits, FAQ, one CTA.
- **Tone:** plain English, direct, no jargon, no guarantees of rankings.
- **Engagement:** each post links to two or three others, so readers keep moving toward the audit.
- **Format rule:** no em dashes.

## Honest limits

- These posts run roughly 600 to 900 words including the FAQ. That is enough to answer each question cleanly, but the competitors you are up against publish longer guides. The best upgrade is your own material: real install photos, local examples, actual numbers from clients you can name, and a short quote from someone doing the work.
- The blog drafts alone will not build the 175-domain gap to the competitors. See `LINK-GAP.md`.
