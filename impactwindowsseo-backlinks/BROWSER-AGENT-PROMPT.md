# Browser session prompt: find and post free backlinks

Paste everything below the line into a Claude session that has **Claude in Chrome** connected. Keep the session in Chrome profile where you are already signed in to WordPress.

---

You are building free, legitimate backlinks for **Impact Windows SEO** (impactwindowsseo.com), using Claude in Chrome. Work in new tabs. Read `impactwindowsseo-backlinks/business-profile.txt` and `impactwindowsseo-backlinks/daily/` in the GitHub repo `GunsNR/claude-skills-hub`, branch `claude/lucid-mccarthy-o3me1a`, before you start. Use only the business facts in that file.

## Goal each run
Find up to **5 new** free backlink opportunities that pass the checks below, submit them, and log every result. Fewer is fine. Never pad the count with weak sites.

## Where to look
1. The targets already prepared in `daily/day-01-2026-10-08.md` (GoodFirms, Clutch, Crunchbase, Bing Places, Apple Business Connect), then any later `daily/day-NN` packets.
2. Free business and agency listings that a real agency would be on: Better Business Bureau, Yelp for Business, Facebook Business Page, LinkedIn Company Page, Manta, Yellow Pages, Trustpilot, UpCity, Expertise.com, the Greater Fort Lauderdale chamber and Broward business organizations, window and door trade associations.
3. Roundup articles ("best window and door marketing agencies") where a real, relevant inclusion request fits. Send a short honest note through the site's own contact form. Use the pitch template in `impactwindowsseo-content/LINK-GAP.md`.
4. Anything new you find by searching. Confirm it passes every check below first.

## A target must pass ALL of these
- It is free, with no purchase, trial, or card needed.
- It is relevant to an SEO or marketing agency, or to the window and door industry, or it is a real local business listing.
- It is a real directory or publication with real users, not a "submit your link" farm, link exchange, or private network.
- The site's terms allow a business to create its own listing. If the terms forbid automated or bulk submissions, do the submission manually and slowly, one form at a time.
- It asks for nothing untrue and nothing that requires a reciprocal link.

## Never do these
- No blog or forum comment spam, no profile pages created only to hold a link, no fake accounts, no fake reviews, no fake case studies or client names, no invented details.
- Never solve or get around a CAPTCHA, a phone or SMS check, an email verification, a postcard, an ID or document upload, or any payment screen. Stop and tell me exactly what is needed.
- Do not enter claims that are not in `business-profile.txt` (no guarantees, no exclusivity, no cities served, no hours unless I give them).
- Do not create passwords you will then write down in chat, the repo, or any file. Let Chrome's password prompt handle it, or ask me.
- Before pressing the final Submit on any form, show me the filled fields and ask. After I approve once for a given site, you may submit.

## Details to ask me for once, up front
- The business email to use on listings (the file leaves it blank).
- Real business hours, if any.
- Whether the "Google Business Profile, website pages, and reviews" services in the medium description are accurate.

## For each target
1. Open the page, read the terms, and check the rules above.
2. Fill the form with the exact name, phone, address, website, category, and description from `business-profile.txt`. Keep it identical everywhere.
3. Submit after my approval, or stop at a human-only step.
4. Note the result honestly: submitted, pending review, needs verification (say which kind), rejected, or skipped (say why).
5. Later runs: revisit earlier entries, check whether the listing is live, and record the live URL. A link that is not live and visible does not count.
6. Whether the link carries `rel="nofollow"`: view the page source if you can and record it. If you cannot tell, write "unknown". Do not claim any link passes ranking value.

## Log everything
Append one row per target to `impactwindowsseo-backlinks/backlink-log.csv`. Do not put passwords or private codes in it. Commit and push it to the same branch if you can. If not, paste the rows in chat.

## WordPress drafts (if I ask)
In my signed-in WordPress admin, create the posts in `impactwindowsseo-content/dist/` as **drafts**, not published: slug = file name without `.html`, one Custom HTML block with the whole file, SEO title and meta description from `posts.py`. Give me the edit links. Do not publish.

## Finish with a plain report
What was submitted, what is pending and why, what needs me, what you skipped and why, and one line on anything that did not go as planned. Do not call anything done unless you saw it live.
