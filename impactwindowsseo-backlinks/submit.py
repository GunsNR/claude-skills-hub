#!/usr/bin/env python3
"""
Impact Windows SEO — Automated Directory Submission Script
Run this on the Cloudways server: python3 submit.py

Handles directories that accept programmatic submissions.
Outputs a log of what was submitted and what needs manual work.
"""

import json
import time
import urllib.request
import urllib.parse
import urllib.error
from datetime import datetime

# ── Business NAP ─────────────────────────────────────────────────────────────
BIZ = {
    "name":        "Impact Windows SEO",
    "phone":       "9547066785",
    "phone_fmt":   "(954) 706-6785",
    "address1":    "5840 Lakeshore Drive",
    "city":        "Fort Lauderdale",
    "state":       "FL",
    "state_full":  "Florida",
    "zip":         "33312",
    "country":     "US",
    "website":     "https://impactwindowsseo.com",
    "email":       "",          # fill in before running
    "category":    "SEO Agency",
    "lat":         "26.0942",   # Fort Lauderdale approximate
    "lng":         "-80.1973",
    "desc_short":  (
        "Impact Windows SEO is a Fort Lauderdale digital marketing agency "
        "specializing exclusively in SEO for impact window and door contractors. "
        "We help installation companies dominate local Google search results, "
        "generate qualified leads, and lock out competitors — one client per "
        "market, guaranteed."
    ),
    "desc_long": (
        "Impact Windows SEO is a Fort Lauderdale-based SEO agency dedicated "
        "exclusively to impact window and door installation companies across "
        "South Florida and beyond. We combine proven local SEO expertise with "
        "deep niche knowledge of the impact window industry. Our services include "
        "Google Business Profile optimization, review building, local content "
        "strategy, citation management, and technical SEO. We work with only one "
        "impact window company per city — permanently locking out local competitors. "
        "Month-to-month contracts, 90-day performance guarantee. Serving Fort "
        "Lauderdale, Miami, Boca Raton, West Palm Beach, Naples, and all of Florida."
    ),
}

LOG = []

def log(directory, status, url="", note=""):
    entry = {
        "directory": directory,
        "status": status,
        "url": url,
        "note": note,
        "time": datetime.now().isoformat(),
    }
    LOG.append(entry)
    icon = "✓" if status == "submitted" else ("⚠" if status == "manual" else "✗")
    print(f"  {icon}  {directory}: {status}" + (f" — {note}" if note else ""))


def post_form(url, data, directory):
    """Submit a simple HTML form via POST."""
    try:
        payload = urllib.parse.urlencode(data).encode()
        req = urllib.request.Request(url, data=payload, method="POST")
        req.add_header("User-Agent", "Mozilla/5.0 (compatible; CitationBot/1.0)")
        req.add_header("Content-Type", "application/x-www-form-urlencoded")
        with urllib.request.urlopen(req, timeout=15) as resp:
            code = resp.getcode()
            log(directory, "submitted", url, f"HTTP {code}")
            return True
    except urllib.error.HTTPError as e:
        log(directory, "failed", url, f"HTTP {e.code}")
        return False
    except Exception as e:
        log(directory, "failed", url, str(e)[:80])
        return False


# ── 1. Foursquare (Places API) ────────────────────────────────────────────────
def submit_foursquare(api_key=""):
    """
    Create a venue on Foursquare. This feeds into Apple Maps, Snapchat,
    Snapchat, and dozens of downstream apps automatically.
    Get a free API key at: https://foursquare.com/developers/signup
    """
    if not api_key:
        log("Foursquare", "manual",
            "https://foursquare.com/developers/signup",
            "Add your Foursquare API key to the api_key parameter")
        return

    url = "https://api.foursquare.com/v3/places"
    headers = {
        "Authorization": api_key,
        "Content-Type": "application/json",
    }
    body = json.dumps({
        "name": BIZ["name"],
        "location": {
            "address": BIZ["address1"],
            "locality": BIZ["city"],
            "region": BIZ["state"],
            "postcode": BIZ["zip"],
            "country": BIZ["country"],
        },
        "tel": BIZ["phone"],
        "website": BIZ["website"],
        "categories": [17069],  # Professional Services > Marketing Services
    }).encode()

    try:
        req = urllib.request.Request(url, data=body, method="POST")
        for k, v in headers.items():
            req.add_header(k, v)
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.load(resp)
            log("Foursquare", "submitted",
                f"https://foursquare.com/v/{result.get('fsq_id','')}",
                f"Venue ID: {result.get('fsq_id','')}")
    except Exception as e:
        log("Foursquare", "failed", url, str(e)[:80])


# ── 2. Hotfrog ───────────────────────────────────────────────────────────────
def submit_hotfrog():
    data = {
        "businessName": BIZ["name"],
        "phone": BIZ["phone_fmt"],
        "addressLine1": BIZ["address1"],
        "city": BIZ["city"],
        "state": BIZ["state"],
        "zip": BIZ["zip"],
        "country": BIZ["country"],
        "website": BIZ["website"],
        "email": BIZ["email"],
        "description": BIZ["desc_short"],
    }
    post_form("https://www.hotfrog.com/business/create", data, "Hotfrog")


# ── 3. Brownbook ─────────────────────────────────────────────────────────────
def submit_brownbook():
    data = {
        "entry[name]":        BIZ["name"],
        "entry[telephone]":   BIZ["phone_fmt"],
        "entry[address]":     BIZ["address1"],
        "entry[town]":        BIZ["city"],
        "entry[region]":      BIZ["state_full"],
        "entry[postcode]":    BIZ["zip"],
        "entry[country]":     "United States",
        "entry[url]":         BIZ["website"],
        "entry[description]": BIZ["desc_short"],
        "entry[category]":    "Marketing",
    }
    post_form("https://www.brownbook.net/add-business/save", data, "Brownbook")


# ── 4. n49 ───────────────────────────────────────────────────────────────────
def submit_n49():
    data = {
        "name":        BIZ["name"],
        "phone":       BIZ["phone_fmt"],
        "address":     BIZ["address1"],
        "city":        BIZ["city"],
        "province":    BIZ["state"],
        "postal_code": BIZ["zip"],
        "website":     BIZ["website"],
        "description": BIZ["desc_short"],
        "email":       BIZ["email"],
    }
    post_form("https://www.n49.com/biz/add/save/", data, "n49")


# ── 5. 2FindLocal ────────────────────────────────────────────────────────────
def submit_2findlocal():
    data = {
        "businessName": BIZ["name"],
        "phone":        BIZ["phone_fmt"],
        "address":      BIZ["address1"],
        "city":         BIZ["city"],
        "state":        BIZ["state"],
        "zip":          BIZ["zip"],
        "website":      BIZ["website"],
        "description":  BIZ["desc_short"],
        "email":        BIZ["email"],
        "category":     "Marketing",
    }
    post_form("https://www.2findlocal.com/set/addBusiness", data, "2FindLocal")


# ── 6. EZlocal ───────────────────────────────────────────────────────────────
def submit_ezlocal():
    data = {
        "business_name": BIZ["name"],
        "phone":         BIZ["phone_fmt"],
        "address":       BIZ["address1"],
        "city":          BIZ["city"],
        "state":         BIZ["state"],
        "zip":           BIZ["zip"],
        "website":       BIZ["website"],
        "description":   BIZ["desc_short"],
        "email":         BIZ["email"],
    }
    post_form("https://ezlocal.com/add-listing", data, "EZlocal")


# ── 7. ShowMeLocal ───────────────────────────────────────────────────────────
def submit_showmelocal():
    data = {
        "BusinessName":  BIZ["name"],
        "Phone":         BIZ["phone_fmt"],
        "Address":       BIZ["address1"],
        "City":          BIZ["city"],
        "State":         BIZ["state"],
        "Zip":           BIZ["zip"],
        "Website":       BIZ["website"],
        "Description":   BIZ["desc_short"],
        "Email":         BIZ["email"],
    }
    post_form("https://www.showmelocal.com/add-business.aspx", data, "ShowMeLocal")


# ── 8. Cylex USA ─────────────────────────────────────────────────────────────
def submit_cylex():
    data = {
        "company":       BIZ["name"],
        "phone":         BIZ["phone_fmt"],
        "street":        BIZ["address1"],
        "city":          BIZ["city"],
        "state":         BIZ["state"],
        "zip":           BIZ["zip"],
        "website":       BIZ["website"],
        "description":   BIZ["desc_short"],
        "email":         BIZ["email"],
    }
    post_form("https://www.cylex-usa.com/add-company", data, "Cylex USA")


# ── 9. MerchantCircle ────────────────────────────────────────────────────────
def submit_merchantcircle():
    data = {
        "business_name":  BIZ["name"],
        "phone":          BIZ["phone_fmt"],
        "address_street": BIZ["address1"],
        "address_city":   BIZ["city"],
        "address_state":  BIZ["state"],
        "address_zip":    BIZ["zip"],
        "website":        BIZ["website"],
        "description":    BIZ["desc_short"],
        "email":          BIZ["email"],
    }
    post_form("https://www.merchantcircle.com/signup", data, "MerchantCircle")


# ── 10. USDirectory ──────────────────────────────────────────────────────────
def submit_usdirectory():
    data = {
        "businessname": BIZ["name"],
        "phone":        BIZ["phone_fmt"],
        "address":      BIZ["address1"],
        "city":         BIZ["city"],
        "state":        BIZ["state"],
        "zip":          BIZ["zip"],
        "website":      BIZ["website"],
        "description":  BIZ["desc_short"],
        "email":        BIZ["email"],
        "category":     "Marketing & Advertising",
    }
    post_form("https://www.usdirectory.com/add-business/", data, "USDirectory")


# ── MANUAL SUBMISSIONS (open these URLs and fill in the form) ─────────────────
MANUAL = [
    ("Google Business Profile",   "https://business.google.com/create",
     "HIGHEST VALUE. Requires phone verification. Use exact NAP from business-profile.txt."),
    ("Bing Places for Business",  "https://www.bingplaces.com/Dashboard/PendingListings",
     "Second most important. Import from GBP once GBP is live."),
    ("Apple Maps Connect",        "https://mapsconnect.apple.com",
     "Sign in with Apple ID. Add business manually."),
    ("Yelp for Business",         "https://biz.yelp.com/signup",
     "Create account, add business, verify via phone call."),
    ("Facebook Business Page",    "https://www.facebook.com/pages/create",
     "Create a Business page. Add all NAP. Add website link in About."),
    ("LinkedIn Company Page",     "https://www.linkedin.com/company/setup/new",
     "Create company page. Add website, description, Fort Lauderdale location."),
    ("Better Business Bureau",    "https://www.bbb.org/get-accredited",
     "Free listing available even without accreditation. DR 93."),
    ("Clutch.co",                 "https://clutch.co/get-listed",
     "HIGHEST VALUE for SEO agencies. DR 80. Free listing, then collect reviews."),
    ("UpCity",                    "https://upcity.com/get-listed",
     "Marketing agency directory. DR 60. Free basic listing."),
    ("Expertise.com",             "https://expertise.com/contact",
     "Nominate yourself for 'Best SEO Companies in Fort Lauderdale' list."),
    ("Manta",                     "https://www.manta.com/claim",
     "Search your business first, then claim or add. DR 60."),
    ("Angi (HomeAdvisor)",        "https://www.angi.com/join/",
     "Relevant if targeting impact window contractors as referral source too."),
    ("Thumbtack",                 "https://www.thumbtack.com/pros/",
     "Create pro profile under 'Marketing' category."),
    ("Houzz",                     "https://www.houzz.com/pro/create-profile",
     "Relevant for impact window + home improvement angle."),
    ("Yellow Pages (YP.com)",     "https://www.yellowpages.com/business/start",
     "Still has DR 75+ and feeds downstream directories."),
    ("Superpages",                "https://www.superpages.com/manage",
     "Feeds to multiple downstream directories. DR 70."),
    ("Foursquare (manual)",       "https://foursquare.com/add-place",
     "Use if API key not available. Feeds Apple Maps and others."),
    ("ChamberofCommerce.com",     "https://www.chamberofcommerce.com/united-states/florida/fort-lauderdale",
     "Add business to Fort Lauderdale category. DR 55."),
    ("TrustPilot",                "https://business.trustpilot.com",
     "Create a free business profile. Excellent DR 91 backlink."),
    ("G2",                        "https://sell.g2.com/",
     "List as a marketing service provider. DR 92 — extremely valuable."),
]


def print_manual_list():
    print("\n" + "="*70)
    print("MANUAL SUBMISSIONS REQUIRED (open in browser, 5-10 min each)")
    print("="*70)
    for i, (name, url, note) in enumerate(MANUAL, 1):
        print(f"\n{i:2}. {name}")
        print(f"    URL:  {url}")
        print(f"    Note: {note}")
        log(name, "manual", url, note)


# ── MAIN ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("\nImpact Windows SEO — Directory Submission")
    print("=" * 50)
    print(f"Business: {BIZ['name']}")
    print(f"Phone:    {BIZ['phone_fmt']}")
    print(f"Address:  {BIZ['address1']}, {BIZ['city']}, {BIZ['state']} {BIZ['zip']}")
    print(f"Website:  {BIZ['website']}")

    if not BIZ["email"]:
        print("\n⚠  WARNING: Set BIZ['email'] before running — required by most directories.")

    print("\n── Automated Submissions ──")

    # Run programmatic submissions with small delays between each
    submit_foursquare()          # needs api_key= param if you have one
    time.sleep(2)
    submit_hotfrog()
    time.sleep(2)
    submit_brownbook()
    time.sleep(2)
    submit_n49()
    time.sleep(2)
    submit_2findlocal()
    time.sleep(2)
    submit_ezlocal()
    time.sleep(2)
    submit_showmelocal()
    time.sleep(2)
    submit_cylex()
    time.sleep(2)
    submit_merchantcircle()
    time.sleep(2)
    submit_usdirectory()

    # Print manual submission list
    print_manual_list()

    # Save log
    log_path = f"submission-log-{datetime.now().strftime('%Y%m%d-%H%M')}.json"
    with open(log_path, "w") as f:
        json.dump(LOG, f, indent=2)

    submitted = sum(1 for e in LOG if e["status"] == "submitted")
    manual    = sum(1 for e in LOG if e["status"] == "manual")
    failed    = sum(1 for e in LOG if e["status"] == "failed")

    print(f"\n── Summary ──")
    print(f"  Submitted automatically: {submitted}")
    print(f"  Needs manual work:       {manual}")
    print(f"  Failed (retry manually): {failed}")
    print(f"  Total targeted:          {submitted + manual + failed}")
    print(f"\nLog saved to: {log_path}")
