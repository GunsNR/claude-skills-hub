# Impact Windows SEO: blog drafts and schema

Eight posts for impactwindowsseo.com, written for window and door companies, each with BlogPosting, WebPage, BreadcrumbList, FAQPage, and ProfessionalService JSON-LD.

**Nothing here is published.** This environment cannot reach the WordPress site. See "What it takes to publish automatically" at the bottom.

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
| `schema-sitewide.json` | Organization + WebSite for the homepage | n/a | n/a | |

*Semrush US database, 2026-10-08, monthly estimates.

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
