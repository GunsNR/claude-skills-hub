# Impact Windows SEO: blog drafts and schema

Thirteen posts for impactwindowsseo.com, written for window and door companies, each with BlogPosting, WebPage, BreadcrumbList, FAQPage, and ProfessionalService JSON-LD.

**Nothing here is published.** Some posts exist as WordPress drafts (see `publish-log.csv`); none are live. A person must review and publish each draft.

## Ground rules for every post

- No guarantees, no promised results, no promised timelines. `build.py` fails the build on phrases like "we guarantee" or "you will rank."
- Every outside fact is logged in `SOURCES.md` with where it came from and how well it was checked. Starred items need a person to confirm them on the official page before publishing.
- No em dashes, no fake ratings, no invented client results.

## Posts in `dist/`

| File | Primary keyword | US searches/mo* | Difficulty* | Batch |
|---|---|---|---|---|
| `seo-for-window-companies.html` | seo for window companies | 40 | 4 | start |
| `window-replacement-leads.html` | window replacement leads | 90 | 4 | start |
| `local-seo-for-contractors.html` | local seo for contractors | 1,600 | 19 | start |
| `google-business-profile-for-window-companies.html` | google business profile for contractors | 70 | 19 | start |
| `impact-window-marketing-florida.html` | impact windows florida | 720 | 46 | start |
| `how-to-hire-seo-agency-for-window-company.html` | window contractor marketing | 320 | 9 | start |
| `product-approvals-impact-window-pages.html` | florida product approval | 4,400 | 40 | Day 1 |
| `wind-mitigation-inspection-window-companies.html` | wind mitigation inspection | 3,600 | 22 | Day 1 |
| `google-review-request-wording-window-companies.html` | how to ask for google reviews | not checked** | not checked** | Day 2 |
| `reply-to-negative-reviews-window-companies.html` | how to respond to negative reviews | not checked** | not checked** | Day 2 |
| `city-pages-for-window-companies.html` | location pages seo | 480 | 21 | Day 3*** |
| `call-tracking-for-window-companies.html` | call tracking numbers | 390 | 21 | Day 3*** |
| `faq-schema-for-contractors.html` | faq schema | 2,400 | 22 | Run 2026-11-12 (2)*** |
| `schema-sitewide.json` | Organization + WebSite for the homepage | n/a | n/a | |

*Semrush US database, 2026-10-08, monthly estimates.

**Semrush was not available in the 2026-11-11 session, so Day 2 topics have no demand data. Check them in Semrush before investing in promotion.

***Semrush US database, 2026-11-12.

## Blog design (2026-11-12)

`build.py` now outputs a styled post: hero with kicker, date and reading time; a reading progress bar; a contents box; fade-in sections as you scroll; FAQ accordions; a styled Sources list and CTA. Everything is scoped to `article.iws-post`, so it does not restyle the theme.

- **Animation is progressive.** Content is fully visible if the script is stripped, and motion turns off for visitors who set "reduce motion".
- **Images:** add `"images": [{"src": ..., "alt": ..., "caption": ...}]` to a post and place `{{IMAGE:1}}` in the body. Use only your own photos, or illustrations clearly labeled as such.
- **`{{PROFILE_CARD}}`** inserts a labeled illustration of the parts of a business profile. It has no Google logo and no star rating on purpose.
- **Brand color:** one line in `build.py`, `--accent:` inside `article.iws-post{...}`. It drives the button, progress bar, heading bars, and summary accent. Set it to your brand hex and run `python3 build.py`.
- **Optional `"kicker"`** sets the small label above the title (default "Window company marketing").
- WordPress must allow the `<script>` in a Custom HTML block (administrators can by default). Without it, posts still display, just without animation.

## To publish each post

1. In WordPress, create a post. Set the slug to the file name without `.html`.
2. Add one **Custom HTML** block and paste the whole file, including the `<script type="application/ld+json">` block at the bottom.
3. Set the SEO title and meta description in your SEO plugin from `posts.py` (`title`, `meta`).
4. Add a featured image and one or two images inside the post. Use **your own install photos** with descriptive alt text, not stock.
5. Update `date` in `posts.py` to the real publish date and run `python3 build.py` again, so the schema date is right.
6. Test with Google's Rich Results Test before requesting indexing in Search Console.

**If Yoast or Rank Math is active**, it already outputs Article/WebPage/Breadcrumb schema. Duplicates can confuse Google. In that case delete every node in the pasted JSON-LD except `FAQPage` and `ProfessionalService`.

## Confirm these before publishing

- **URLs.** Posts link to `https://impactwindowsseo.com/<slug>/`, the CTA points to `/contact/`, and the breadcrumb uses `/blog/`. If your permalinks differ, change `BASE`, `CONTACT_URL`, and the breadcrumb in `build.py`, then run `python3 build.py`.
- **The free audit offer.** The CTA offers a free SEO audit with a written report. That came from RankLogic SEO's site. Remove it if Impact Windows SEO does not offer it.
- **Wayne's Roofing mention** in the first post. The numbers come from RankLogic SEO's own client data. Keep it only if you are comfortable crediting the sister company this way.
- **Starred items in `SOURCES.md`.** Have a person confirm the Florida statute, form, and product-approval details on the official pages. The Florida posts are the highest-risk content.
- **Schema.** No ratings, reviews, logo, hours, or social profiles are included because none were provided. Add `logo`, `openingHours`, and `sameAs` when you have real ones. Never add an `aggregateRating` unless it reflects reviews customers can see on the page.

## Daily cadence

You asked for two posts and five backlinks per day. What that takes in practice:

- **Posts.** Each needs a topic with real search demand (check Semrush), facts checked against sources, and a person to confirm the Florida items. Add the next ones to `posts.py` and log their sources in `SOURCES.md`. Publishing daily is realistic only if the topics stay narrow enough to verify. Quantity should never outrun accuracy.
- **Backlinks.** Each daily packet lives in `../impactwindowsseo-backlinks/daily/`. These need a person (or a browser-connected session) to fill in forms, pass CAPTCHAs, and verify by phone, postcard, or email.

## What it takes to publish automatically

A cloud session can only publish if it can reach the site and has credentials. Neither is set up. Both are changed in the environment settings (the cloud environment menu in the session title bar, then Edit), never by pasting secrets into chat:

1. **Network access.** Add `impactwindowsseo.com` under Allowed domains.
2. **Credentials.** In WordPress, create an Application Password (Users, your profile, Application Passwords). Store the username and that password as environment secrets, for example `IWS_WP_USER` and `IWS_WP_APP_PASSWORD`, and the site address as `IWS_WP_URL`. A new session can then publish through WordPress's REST API over HTTPS.

SSH to Cloudways is a different path and may not work through the environment's network proxy. The REST API route is the one to try first.

## Honest limits

- The posts run about 400 to 730 words, plus a FAQ. That answers each question cleanly, but competitors publish longer guides. The best upgrades are your own install photos, local examples, and real client numbers.
- Drafts alone will not close the gap with competitors that have thousands of linking domains. See `LINK-GAP.md`.

## Daily run log

**2026-11-12 (second run, unattended).** 1 new post (draft), 1 refresh (draft), 3 backlink targets, 1 outreach draft, 1 GBP post saved. Nothing published live.
- New: `faq-schema-for-contractors` as WordPress draft 1023. It passed every content gate, but its internal links point to posts that are not live in WordPress, so it was held as a draft. No post on the site is live yet.
- Refresh: `city-pages-for-window-companies` (draft 1021) updated with question H2s, a direct answer, a Sources section, and a link to the new post.
- Added `publish_wp.py` (standard library; checks for an existing slug before creating) and `OWNER-INPUT.md` (template, empty).
- GBP post saved in `gbp-posts/2026-11-12.txt` for manual posting (no GBP API credentials). Do not post until the article is live.
- Outreach: 1 of 2 drafts (`../impactwindowsseo-backlinks/outreach/2026-11-12.md`); Gmail connector failed, so no Gmail draft.
- Digest: `digests/2026-11-12-run2.txt` (named to avoid overwriting the first run's digest). Email NOT sent.
- Full report: `run-reports/2026-11-12.md`.

**2026-11-12 (Day 3).** 2 posts, 5 backlink targets.
- Tools: Semrush (demand data for both topics), WebSearch, and Firecrawl page reads in place of WebFetch. Google's spam policy page and Business Profile guidelines were opened and quoted directly.
- WordPress: all three `IWS_WP_*` variables set and the site returned 200. Drafts created: post 1021 (`city-pages-for-window-companies`) and post 1022 (`call-tracking-for-window-companies`), status draft. Logged in `publish-log.csv`.
- Delivery: digest in `digests/2026-11-12.txt`. No Drive share or email-send tool was available, so it was **not emailed** to office@ranklogicseo.com (see final summary for the Drive doc status).
- Starred items: the vendor-recommended GBP tracking-number setup and the Florida all-party recording consent rule (statute page would not render; confirm at leg.state.fl.us).

**2026-11-11 (Day 2).** 2 posts, 5 backlink targets.
- Tools: WebSearch only. Semrush not available (no demand data for the new topics). Google Drive tools not available, so the digest was **not emailed**; it is in `digests/2026-11-11.txt`.
- WordPress: `IWS_WP_URL`, `IWS_WP_USER`, and `IWS_WP_APP_PASSWORD` were all missing, and impactwindowsseo.com was blocked by the environment's network proxy. No drafts created.
- All new facts are strength C (search summaries); support.google.com could not be opened directly. Starred items in `SOURCES.md` need a human check.
