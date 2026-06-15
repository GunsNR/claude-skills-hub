# Impact Windows SEO — 30 Backlink Build Guide

**Business:** Impact Windows SEO  
**Target:** 30 high-quality citations & directory backlinks  
**Current DR:** 0 (fresh domain — every link counts)

---

## Step 1 — Run the Automated Script (Cloudways Server)

```bash
# SSH into your Cloudways server, then:
cd ~
python3 submit.py
```

This auto-submits to 10 directories. Before running:
1. Open `submit.py` and set `BIZ["email"]` to your business email
2. Optionally add a Foursquare API key (free at foursquare.com/developers)

---

## Step 2 — Manual High-Value Submissions (Do These First)

These 20 directories cannot be automated (CAPTCHA / phone verification required).  
They are ordered by DR and SEO value. Knock out 3–4 per day.

### 🔴 CRITICAL — Do These This Week

| # | Directory | DR | URL | Time |
|---|-----------|-----|-----|------|
| 1 | Google Business Profile | 100 | https://business.google.com/create | 20 min |
| 2 | Bing Places for Business | 94 | https://www.bingplaces.com | 10 min |
| 3 | Apple Maps Connect | 100 | https://mapsconnect.apple.com | 15 min |
| 4 | Facebook Business Page | 100 | https://www.facebook.com/pages/create | 15 min |
| 5 | LinkedIn Company Page | 99 | https://www.linkedin.com/company/setup/new | 10 min |
| 6 | G2 | 92 | https://sell.g2.com/ | 15 min |
| 7 | TrustPilot Business | 91 | https://business.trustpilot.com | 10 min |
| 8 | Clutch.co | 80 | https://clutch.co/get-listed | 20 min |

**Notes for each:**
- **GBP:** Use exact NAP from business-profile.txt. Choose "Marketing Agency" as primary category + "SEO Agency" secondary. Upload logo. Verify via phone.
- **Bing Places:** After GBP is live, import directly from GBP — saves time.
- **Apple Maps:** Use Apple ID. Verify via phone call.
- **G2:** List under "SEO Software" and "Local SEO." DR 92 — one of the best backlinks possible for an SEO agency.
- **Clutch:** Takes 1–2 weeks to approve. Submit now. Once live, ask 3 clients for Clutch reviews — each review dramatically boosts your profile visibility.

---

### 🟡 HIGH VALUE — Do Within 2 Weeks

| # | Directory | DR | URL |
|---|-----------|-----|-----|
| 9 | Yelp for Business | 94 | https://biz.yelp.com/signup |
| 10 | Better Business Bureau | 93 | https://www.bbb.org/get-accredited |
| 11 | UpCity | 62 | https://upcity.com/get-listed |
| 12 | Expertise.com | 61 | https://expertise.com/contact |
| 13 | Yellow Pages | 76 | https://www.yellowpages.com/business/start |
| 14 | Manta | 61 | https://www.manta.com/claim |
| 15 | Superpages | 70 | https://www.superpages.com/manage |

**Notes:**
- **BBB:** Free listing available even without paid accreditation. Apply anyway.
- **UpCity:** List under "SEO Agencies" in Fort Lauderdale. Free tier is fine.
- **Expertise.com:** Email them requesting to be considered for their "Best SEO Companies in Fort Lauderdale" list. Subject line: "Nomination for Best SEO Companies - Fort Lauderdale."
- **Yellow Pages:** Still DR 76 and feeds many auto-aggregators downstream.

---

### 🟢 STANDARD — Complete in Month 1

| # | Directory | DR | URL |
|---|-----------|-----|-----|
| 16 | Angi / HomeAdvisor | 84 | https://www.angi.com/join/ |
| 17 | Thumbtack | 80 | https://www.thumbtack.com/pros/ |
| 18 | Houzz | 89 | https://www.houzz.com/pro/create-profile |
| 19 | ChamberofCommerce.com | 56 | https://www.chamberofcommerce.com |
| 20 | Agency Spotter | 48 | https://www.agencyspotter.com/get-listed |

---

## Step 3 — Automated Submissions Tracker

The `submit.py` script handles these 10 automatically:

| # | Directory | DR | Status |
|---|-----------|-----|--------|
| 21 | Hotfrog | 52 | Script |
| 22 | Brownbook.net | 49 | Script |
| 23 | n49 | 44 | Script |
| 24 | 2FindLocal | 43 | Script |
| 25 | EZlocal | 42 | Script |
| 26 | ShowMeLocal | 41 | Script |
| 27 | Cylex USA | 40 | Script |
| 28 | MerchantCircle | 55 | Script |
| 29 | USDirectory | 38 | Script |
| 30 | Foursquare | 89 | Script (needs API key) |

---

## Copy Reference

All descriptions are in `business-profile.txt`. Use:
- **50-word version** for smaller citation sites
- **150-word version** for major directories (GBP, Yelp, BBB)
- **300-word version** for Clutch, UpCity, G2, BBB full profile

---

## What Happens Next

1. **Week 1–2:** GBP, Facebook, LinkedIn, G2, Clutch go live
2. **Week 3–4:** Bing, Apple, Yelp, BBB, UpCity live
3. **Month 2:** Automated citations start indexing in Google
4. **Month 3:** DR starts moving from 0 → 10–20 range
5. **Month 4–6:** DR 20–35 achievable with these 30 links + content

**Pro tip:** After each submission, go back 2 weeks later and check if the listing is live. Some directories require email confirmation that gets missed. Any rejected or unconfirmed listing = a missed backlink.

---

## Foursquare API Key (Highest ROI Automated Link)

Foursquare feeds Apple Maps, Snapchat Maps, and 40+ downstream apps.
One submission here = potentially 40+ citations.

1. Go to https://foursquare.com/developers/signup
2. Create a free account
3. Create an app → copy the API key
4. In `submit.py`, update: `submit_foursquare(api_key="YOUR_KEY_HERE")`
5. Run the script — the venue creates automatically
