# Browser session prompt: find and post free backlinks

Paste everything below the line into a Claude session that has **Claude in Chrome** connected. Keep the session in Chrome profile where you are already signed in to WordPress.

---

You are building free, legitimate backlinks for **Impact Windows SEO** (impactwindowsseo.com), using Claude in Chrome. Work in new tabs. Read `impactwindowsseo-backlinks/business-profile.txt` and `impactwindowsseo-backlinks/daily/` in the GitHub repo `GunsNR/claude-skills-hub`, branch `claude/lucid-mccarthy-o3me1a`, before you start. Use only the business facts in that file.

## Goal each run
1. Find up to **5 new** free backlink opportunities that pass the checks below, submit them, and log every result. Fewer is fine. Never pad the count with weak sites.
2. Publish up to **2 blog posts** through the three-check gate in "Publishing blogs" below. Fewer is fine. Accuracy comes before volume.

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

## Publishing blogs (automatic, but only through this three-check gate)

Publish at most **2 posts per day**, from `impactwindowsseo-content/dist/`, oldest unpublished first. A post goes live only if it passes all three checks. If any check fails and you cannot fix it without adding unverified facts, leave it as a **draft**, say why, and move on.

Ask me once, up front: (a) is the free SEO audit offer in the call-to-action true for Impact Windows SEO; (b) what is the real permalink pattern and contact page URL; (c) which SEO plugin is active (Yoast, Rank Math, none); (d) are there real install photos in the Media Library I want used.

### Check 1: Accuracy (do this before touching WordPress)
- Open `impactwindowsseo-content/SOURCES.md`. For every starred (*) fact and every strength-C fact the post uses, open the **official page in a tab** and confirm it says what the post says today. Use leg.state.fl.us for statutes, floir.gov for the mitigation form, floridabuilding.org and Miami-Dade product control for approvals, and Google Business Profile Help for Google rules. Record the page URL and what you saw.
- Any claim you cannot confirm on the official page: remove it from the post, in WordPress and in the repo (`posts.py` and `SOURCES.md`), or leave the post as a draft. Never publish an unconfirmed legal, insurance, or product-approval claim.
- Search numbers carry a date (Semrush, 2026-10-08). Keep them as dated estimates. Do not change them unless you can re-check them.
- Confirm no guarantee, promise, fake proof, invented result, or em dash is in the text.

### Check 2: Technical, on a saved draft
- Create the draft: slug = file name without `.html`, one Custom HTML block with the whole file, SEO title and meta description from `posts.py`.
- **Links.** Open every link in preview: internal and external. Each must load a real page, not a 404 or a loop. Links to sibling posts only work once those posts are live, so publish in dependency order or remove the link until its target exists. Replace the assumed contact URL with the real one from (b).
- **Images.** Each post needs a featured image and at least one image in the body. Each image must load, display at the right proportions, be a reasonably small compressed file, and have a plain description as alt text (no keyword stuffing). Use only images from my Media Library or original graphics made for this post. Never use stock photos that show "our" crews or installs, or any picture that implies work Impact Windows SEO did. Never hotlink images from other sites. No suitable image means the post stays a draft and you ask me.
- **Layout.** Check desktop and phone preview. Text must be readable, tables must not overflow, the call-to-action button must work, and there must be only one H1. If the theme already prints the post title, remove the H1 from the pasted HTML.
- **Schema.** After saving, test the page in Google's Rich Results Test. If the SEO plugin already outputs Article or Breadcrumb schema, keep only the FAQPage and ProfessionalService blocks from my HTML. There must be zero errors. Note any warnings.

### Check 3: Engagement read-through
Read it as a window company owner would, and answer yes or no to each:
- Does the first sentence give a reason to keep reading?
- Is the headline's question answered on the first screen?
- Are the headings scannable, with at least one concrete step list or example?
- Is anything repeated, vague, or padded?
- Is the call-to-action clear, and does it match the real offer?

Any "no": fix the wording and mirror the edit in the repo. Do not add new facts while polishing. Then re-run check 1 on whatever you changed.

### Publish, then check again
Publish only when all three checks pass. Then open the live URL in a fresh tab and repeat links, images, schema, and phone view. If anything fails, set the post back to draft **immediately** and tell me. Do not request indexing or post to social media unless I ask.

### Log it
Append a row to `impactwindowsseo-content/publish-log.csv` for every post you touch: date, slug, WordPress post id, status (draft, published, or blocked), result of each check, live URL, and notes. No passwords or private codes.

## Finish with a plain report
What was submitted, what is pending and why, what needs me, what you skipped and why, and one line on anything that did not go as planned. Do not call anything done unless you saw it live.
