"""Blog post source for impactwindowsseo.com.

Rules every post follows:
  * No guarantees or promised results or timelines.
  * Every outside fact traces to an entry in SOURCES.md. If it is not there, it is
    not in the post.
  * Search numbers are Semrush US database, pulled 2026-10-08.
  * No em dashes.

Each post: slug, date, title, meta, primary/secondary keywords, alternate titles
(for A/B tests), body HTML, FAQ list. build.py turns these into WordPress-ready
HTML with JSON-LD. The visible FAQ and the FAQPage markup come from the same list.
Internal links use {{LINK:slug}}.
"""

POSTS = [
    # ------------------------------------------------------------------ 1
    {
        "slug": "seo-for-window-companies",
        "date": "2026-10-08",
        "title": "SEO for Window Companies: What Gets the Phone Ringing",
        "meta": "A plain-English, five-part SEO plan for window and door companies: Google profile, reviews, product and city pages, proof, and call tracking.",
        "primary_kw": "seo for window companies",
        "secondary_kw": ["window company marketing", "window contractor marketing", "window replacement near me"],
        "alt_titles": [
            "Your Next Window Customer Is Already Searching. Will They Find You?",
            "The 5-Part SEO Plan for Window and Door Companies",
            "Where Window Companies Lose Local Searches, and What to Fix First",
        ],
        "body": """
<p>Someone in your service area searched "window replacement near me" today. Semrush's US data puts that phrase at about 33,100 searches a month. Each of those searchers is a homeowner deciding who to call from whatever shows up on the screen.</p>
<p>If your company is not in those first results, the homeowner may never get the chance to compare your price or your quality.</p>
<p>This is the plan we recommend, in the order we recommend doing it.</p>
<aside class="iws-tldr"><strong>The short version:</strong> Window SEO comes down to five things: a complete Google Business Profile, a steady flow of recent reviews, one real page for every product and city you serve, proof on every page, and call tracking so you know what works. Start at the top of the list.</aside>

<h2>Why window SEO behaves differently</h2>
<p>A window or door replacement is a big, considered purchase. Homeowners tend to compare photos, reviews, warranties, financing, and installers before they pick up the phone. Two kinds of searches matter at the same time:</p>
<ul>
<li><strong>Local searches</strong> like "window replacement near me" or "window installers in Fort Lauderdale." These often show a map with local businesses, and they can send calls.</li>
<li><strong>Product searches</strong> like "impact windows cost" or "casement vs double hung." These bring researchers, who may call later if your page was the helpful one.</li>
</ul>
<p>Start with the local side. Those searchers are looking for someone to call.</p>

<h2>1. Finish your Google Business Profile</h2>
<p>Your profile is what appears in the map results. A half-filled profile gives Google and homeowners less to go on. A complete one has:</p>
<ul>
<li>The closest primary category, plus every secondary category that truly applies.</li>
<li>Every product and service you install, each with a short description.</li>
<li>Real photos of finished installs, your crew, and your trucks, with new ones added regularly.</li>
<li>A service area that lists the cities you actually work in.</li>
<li>Regular posts. A photo of a finished job counts.</li>
</ul>
<p>We walk through every field in our <a href="{{LINK:google-business-profile-for-window-companies}}">Google Business Profile checklist for window companies</a>.</p>

<h2>2. Build a review habit, not a review burst</h2>
<p>Homeowners read reviews, and your profile displays them. What helps is a steady flow of recent, specific reviews from real customers, not a pile collected in one weekend.</p>
<p>A simple system: when an install is signed off, text the customer a direct link to your Google review page within a day or two, while the job is fresh. Reply to every review, good or bad.</p>
<p>Our sister company, RankLogic SEO, worked with Wayne's Roofing Co. in Ocean County, New Jersey, which now has more than 331 Google reviews and is the number one rated roofing company in the county. Roofing and windows are different trades, and results vary by business, but both depend on homeowners trusting what other homeowners say.</p>

<h2>3. Build one real page for every product and city</h2>
<p>Google can only send a homeowner to a page that exists. If you install impact windows in Fort Lauderdale, Pompano Beach, and Hollywood, each city deserves its own page with the products you install there, photos of local jobs, and the permit details for that area.</p>
<p>Do not clone one page and swap the city name. Near-identical pages tell a homeowner nothing new. Write each page so it would still be useful with your logo removed.</p>

<h2>4. Put proof on every page</h2>
<p>A homeowner choosing between three installers is looking for a reason to trust one. Give them reasons:</p>
<ul>
<li>Product approvals and warranty terms in plain English.</li>
<li>Photos of real installs, ideally with the city named.</li>
<li>What affects price, so the first call is not a surprise.</li>
<li>Financing options, license numbers, and your best reviews.</li>
</ul>

<h2>5. Track calls, not rankings</h2>
<p>A ranking report does not pay your crew. Set up call tracking and form tracking so you can see which searches and pages produce estimates. Then judge your SEO on booked estimates and signed jobs.</p>

<h2>How long it takes</h2>
<p>There is no fixed timeline. It depends on how competitive your cities are and how much work your profile and website need. A sensible checkpoint is day 90: by then you should be able to see whether calls, profile actions, and map positions are moving the right way. Nobody outside Google controls rankings, so no agency can honestly guarantee a position or a date.</p>
<p>Compare this with paying for leads in our guide to <a href="{{LINK:window-replacement-leads}}">renting versus owning window replacement leads</a>.</p>
""",
        "faq": [
            ("How much does SEO cost for a window company?",
             "It depends on how many cities you serve and how competitive each one is. A one-city shop needs less than a company covering a whole county. Any agency should be able to review your profile, site, and competitors, then tell you what the work costs before you commit."),
            ("Is SEO better than paying for window leads?",
             "They do different jobs. Paid leads and ads usually bring calls faster, and they stop when you stop paying. SEO usually takes longer to build and has no per-lead fee. Many companies use both and compare cost per signed job."),
            ("How long does SEO take to work for a window company?",
             "There is no fixed timeline, because it depends on your market and the work needed. Check progress at 90 days by comparing calls, profile actions, and map positions with where you started. No one can guarantee a ranking or a date."),
            ("Do I need a blog to rank?",
             "Not first. Complete your Google Business Profile, build a review habit, and publish your product and city pages before anything else. Blog posts can support those pages later."),
        ],
    },
    # ------------------------------------------------------------------ 2
    {
        "slug": "window-replacement-leads",
        "date": "2026-10-08",
        "title": "Window Replacement Leads: Rent Them or Own Them?",
        "meta": "Shared lead sites and ads rent you customers by the click. See how organic search compares for window companies, with the math to check it yourself.",
        "primary_kw": "window replacement leads",
        "secondary_kw": ["window replacement near me", "window contractor marketing"],
        "alt_titles": [
            "What a Window Replacement Lead Really Costs You",
            "Paid Leads vs SEO for Window Companies: A Fair Comparison",
            "Stop Guessing: Cost per Signed Job for Window Companies",
        ],
        "body": """
<p>Search "window replacement leads" and you land in a wall of lead vendors. Semrush's US data shows advertisers paying an average of about $22.57 a click on that phrase and about $30.60 a click on "window replacement near me." Those are market estimates, but they show that other companies think your customers are worth bidding for.</p>
<p>The question is whether you want to keep renting access to them.</p>
<aside class="iws-tldr"><strong>The short version:</strong> Paid leads and ads usually bring calls faster, and they stop when you stop paying. Organic search usually takes longer and has no per-lead fee. Track cost per signed job for each channel and let the numbers decide.</aside>

<h2>What renting leads costs</h2>
<p>There are two common ways to rent customers:</p>
<ul>
<li><strong>Shared lead sites.</strong> The same homeowner request goes to more than one contractor. You race to call first and quote best.</li>
<li><strong>Pay-per-click ads.</strong> You pay for every click, whether or not that person ever calls.</li>
</ul>
<p>Neither one is wrong. Both share one trait: when you stop paying, the leads and clicks stop.</p>

<h2>Do the math with your own numbers</h2>
<p>Cost per lead is the wrong number. The number that matters is cost per signed job:</p>
<p><strong>Cost per signed job = what you spent on the channel &divide; jobs you signed from it</strong></p>
<p>Here is an illustration with made-up numbers, not a benchmark. Say you spend $3,000 and get 40 leads. Twelve become booked estimates and four become signed jobs. That is $750 per signed job in lead cost alone, before your estimator's time and drive. Your own numbers will differ, which is the point. Run them.</p>

<h2>What owning leads looks like</h2>
<p>Owning leads means showing up in the map results and on page one when a homeowner searches, so they call your business directly. You still compete with other companies for those positions, but there is no per-lead fee.</p>
<table>
<thead><tr><th>&nbsp;</th><th>Renting (leads, ads)</th><th>Owning (organic search)</th></tr></thead>
<tbody>
<tr><td>Time to first calls</td><td>Typically faster</td><td>Typically slower, depends on market</td></tr>
<tr><td>How you pay</td><td>Per lead or per click</td><td>Ongoing work, no per-lead fee</td></tr>
<tr><td>Competition</td><td>Shared leads go to several contractors; ads compete in an auction</td><td>You compete for rankings, but the call goes to your listing</td></tr>
<tr><td>If you stop paying</td><td>Leads and clicks stop</td><td>Rankings and reviews may persist, but need upkeep</td></tr>
</tbody>
</table>

<h2>When renting still makes sense</h2>
<ul>
<li>You are entering a new city and have no reviews yet.</li>
<li>Your crew has open capacity this month.</li>
<li>You need calls while your <a href="{{LINK:seo-for-window-companies}}">SEO work</a> builds.</li>
</ul>

<h2>A sane way to shift budget</h2>
<ol>
<li>Give every channel its own tracking phone number and form.</li>
<li>For 90 days, record leads, booked estimates, and signed jobs per channel.</li>
<li>Calculate cost per signed job for each.</li>
<li>Move budget toward the channels that win, a little at a time.</li>
</ol>
<p>Ask every lead vendor for their lead-to-signed rate for window companies in your area. If they cannot give you one, you now know how much they track.</p>
<p>Thinking about hiring help? Read <a href="{{LINK:how-to-hire-seo-agency-for-window-company}}">9 questions to ask before you hire an SEO agency</a>.</p>
""",
        "faq": [
            ("Are shared window replacement leads worth buying?",
             "It depends on your cost per signed job. Shared leads go to more than one contractor, so you are racing others for the same homeowner. Track spend against signed jobs for 90 days before deciding."),
            ("Can SEO replace paid leads for a window company?",
             "For some companies it can reduce reliance on paid leads, but results depend on your market and the work done. SEO builds slowly, so many companies keep a smaller paid budget while organic rankings and reviews grow."),
            ("How do I know if a lead is exclusive?",
             "Ask the vendor in writing how many contractors receive each lead. If the answer is more than one, it is a shared lead."),
            ("How much does a window replacement lead cost?",
             "Prices vary by market and vendor. Semrush's US data shows advertisers averaging about $22.57 per click on the phrase 'window replacement leads.' A click is not yet a lead, so your cost per signed job will be higher than the cost per click."),
        ],
    },
    # ------------------------------------------------------------------ 3
    {
        "slug": "local-seo-for-contractors",
        "date": "2026-10-08",
        "title": "Local SEO for Contractors: A 90-Day Plan",
        "meta": "A month-by-month local SEO plan for contractors: what to fix first, what to skip, and what to check at day 90. Plain language, no vanity metrics.",
        "primary_kw": "local seo for contractors",
        "secondary_kw": ["seo for contractors", "local seo for home services"],
        "alt_titles": [
            "Local SEO for Contractors, Explained in 90 Days",
            "What to Fix First if Your Contracting Business Is Hard to Find on Google",
            "The Contractor's Month-by-Month Local SEO Checklist",
        ],
        "body": """
<p>About 3,600 people a month search "seo for contractors" in the US, according to Semrush, and another 1,600 search "local seo for contractors." Contractors are looking for a clear starting point, so here is one.</p>
<p>This plan is built around one result: calls from homeowners in your service area.</p>
<aside class="iws-tldr"><strong>The short version:</strong> Month 1 is foundation, month 2 is pages and reviews, month 3 is expansion and measurement. Skip blogging first, link buying, and directory blasts until the basics are done.</aside>

<h2>Month 1: Foundation</h2>
<ul>
<li><strong>Claim and complete your Google Business Profile.</strong> Categories, services, photos, service area, hours.</li>
<li><strong>Keep your name, address, and phone number identical everywhere.</strong> Every listing should point to the same business.</li>
<li><strong>Set up call and form tracking.</strong> Without it you are guessing.</li>
<li><strong>Fix the technical basics.</strong> The site should load quickly and work well on a phone.</li>
<li><strong>Map your keywords.</strong> One service in one city equals one page.</li>
</ul>
<p>The profile work is detailed enough that we gave it its own guide: <a href="{{LINK:google-business-profile-for-window-companies}}">the Google Business Profile checklist</a>. It is written for window companies, but the structure fits most trades.</p>

<h2>Month 2: Pages and reviews</h2>
<ul>
<li><strong>Publish your core service pages.</strong> Real copy, real project photos, plain-English process, what affects price.</li>
<li><strong>Start the review habit.</strong> After each finished job, text a direct review link within a day or two.</li>
<li><strong>Reply to every review.</strong> Good and bad. Calm and specific.</li>
</ul>

<h2>Month 3: Expand and measure</h2>
<ul>
<li><strong>Add city pages</strong> for the areas you want more work in. Each one needs local detail, not a copy with a new city name.</li>
<li><strong>Look at the calls.</strong> Which pages and searches produced estimates? Do more of that.</li>
<li><strong>Look at the review gap.</strong> Count how many new reviews the top three map results add each month, and decide what pace you can match.</li>
</ul>

<h2>What to skip at first</h2>
<ul>
<li><strong>Blogging before the foundation.</strong> Posts can support your pages later. They do not replace a complete profile.</li>
<li><strong>Buying links.</strong> Google's guidelines treat links bought to influence rankings as a violation.</li>
<li><strong>Mass directory submissions.</strong> Start with a few accurate, relevant listings and add more only with a reason.</li>
</ul>

<h2>What to check at day 90</h2>
<p>Compare profile views, call and direction taps, form leads, and map positions with where you started. If numbers moved, find out which work caused it and do more of it. If they did not, look at the data before changing course. Results vary by market, and no one can promise a date or a ranking.</p>
<p>For a trade-specific version of this plan, see <a href="{{LINK:seo-for-window-companies}}">SEO for window companies</a>.</p>
""",
        "faq": [
            ("How long does local SEO take for contractors?",
             "There is no fixed timeline. It depends on how competitive your market is and how much your profile and website need. Use day 90 as a checkpoint to compare calls, profile actions, and map positions with where you started."),
            ("What should a contractor fix first for local SEO?",
             "Your Google Business Profile. Complete every field, add real photos, list your services, and set your service area."),
            ("Do citations and directory listings still matter?",
             "Listings on a small number of relevant sites keep your business details consistent across the web. Start with the platforms homeowners actually use, and make sure your name, address, and phone number match everywhere."),
            ("How many Google reviews does a contractor need?",
             "There is no set number. Look at the top three map results for your main service and city, compare their totals and how often they add new reviews, and set a pace you can keep."),
        ],
    },
    # ------------------------------------------------------------------ 4
    {
        "slug": "google-business-profile-for-window-companies",
        "date": "2026-10-08",
        "title": "Google Business Profile for Window Companies: A Checklist",
        "meta": "A field-by-field Google Business Profile checklist for window and door companies, the mistakes that break Google's guidelines, and a 15-minute weekly routine.",
        "primary_kw": "google business profile for contractors",
        "secondary_kw": ["google maps ranking contractors", "window company marketing"],
        "alt_titles": [
            "The Google Business Profile Checklist Every Window Company Needs",
            "Is Your Google Business Profile Costing You Window Jobs?",
            "15 Minutes a Week: Keeping a Window Company's Google Profile Strong",
        ],
        "body": """
<p>When a homeowner searches for a window installer, your Google Business Profile is often one of the first things they see. It can show your reviews, photos, hours, and a button that calls you.</p>
<p>Some profiles stop at the name and phone number. Use this checklist to finish the job.</p>
<aside class="iws-tldr"><strong>The short version:</strong> Complete every field honestly, show real work, collect reviews steadily, and avoid the handful of mistakes that break Google's guidelines.</aside>

<h2>The checklist</h2>
<h3>Basics</h3>
<ul>
<li><strong>Business name:</strong> the real-world name you use on your signs, website, and paperwork. Google's guidelines say not to add taglines, phone numbers, URLs, or other extra descriptors.</li>
<li><strong>Address:</strong> a real location where you operate. If customers do not visit you, set the profile up as a service-area business and hide the address.</li>
<li><strong>Phone:</strong> a local number that matches your website.</li>
<li><strong>Website link:</strong> point it to the page that best matches the profile, usually your homepage or a main service page.</li>
<li><strong>Hours:</strong> accurate hours, updated for holidays.</li>
</ul>
<h3>Categories and services</h3>
<ul>
<li><strong>Primary category:</strong> pick the closest match from the category list in your dashboard.</li>
<li><strong>Secondary categories:</strong> add every other category that truly applies to work you do.</li>
<li><strong>Services:</strong> list each product and service you install, with a short description.</li>
</ul>
<h3>Photos and proof</h3>
<ul>
<li>Real photos of finished installs, before and after pairs, your crew, and your trucks.</li>
<li>Add new photos on a regular schedule.</li>
<li>Skip stock images. They show customers nothing about your work.</li>
</ul>
<h3>Reviews</h3>
<ul>
<li>Create your direct review link and use it in every follow-up text.</li>
<li>Ask within a day or two of sign-off, while the job is fresh.</li>
<li>Reply to every review.</li>
</ul>
<h3>Activity</h3>
<ul>
<li>Post regularly: a finished job, a seasonal reminder, a short tip.</li>
<li>Keep products, services, and hours current.</li>
</ul>

<h2>Mistakes that break Google's guidelines</h2>
<ul>
<li><strong>Extra words in the business name.</strong> Google's guidelines say unnecessary information in the name can lead to suspension.</li>
<li><strong>A virtual office or mailbox as your address.</strong> Google says a rented mailing address where you do not operate is not eligible.</li>
<li><strong>More than one profile for the same business.</strong> Google says you can have only one Business Profile per business, and duplicates may be hidden.</li>
<li><strong>Offering a reward for reviews.</strong> Google prohibits incentives, financial or otherwise, in exchange for a review. Asking is fine. Rewarding is not.</li>
</ul>
<p>Google updates its guidelines, so check the current version in Business Profile Help before making big changes.</p>

<h2>A 15-minute weekly routine</h2>
<ol>
<li>Upload two or three new job photos.</li>
<li>Reply to any new reviews.</li>
<li>Send review requests for jobs signed off this week.</li>
<li>Check calls and direction taps in the profile insights.</li>
</ol>
<p>The profile is step one of a larger plan. See how it fits in <a href="{{LINK:local-seo-for-contractors}}">the 90-day local SEO plan</a> and in <a href="{{LINK:seo-for-window-companies}}">SEO for window companies</a>.</p>
""",
        "faq": [
            ("How many categories can a Google Business Profile have?",
             "You choose one primary category and can add secondary ones. Add every secondary category that truly describes work you do, and skip the rest. The category list in your dashboard shows the current options."),
            ("Can a window company use a Business Profile without a storefront?",
             "Yes, if it serves customers at their locations. Google lets service-area businesses hide their street address and list the areas they serve."),
            ("How often should I post on my Google Business Profile?",
             "Regularly. A photo of a finished job with one or two sentences is enough. Pick a schedule you can keep."),
            ("What can get a Google Business Profile suspended?",
             "Google's guidelines say extra descriptors in the business name can lead to suspension, and they also prohibit virtual-office addresses, duplicate profiles, and incentivized reviews. Read the current guidelines in Business Profile Help for the full list."),
        ],
    },
    # ------------------------------------------------------------------ 5
    {
        "slug": "impact-window-marketing-florida",
        "date": "2026-10-08",
        "title": "Impact Window Marketing in Florida: What to Build First",
        "meta": "A practical guide to the pages, product approvals, and reviews Florida impact window companies need so homeowners can find and trust them.",
        "primary_kw": "impact windows florida",
        "secondary_kw": ["impact window installation", "hurricane windows cost", "impact windows cost"],
        "alt_titles": [
            "Florida Impact Window Companies: The Pages Worth Building First",
            "How Impact Window Companies Earn Trust Online",
            "The Pages Every Florida Impact Window Company Should Have",
        ],
        "body": """
<p>Florida's Atlantic hurricane season runs June 1 through November 30. Semrush's US data shows people search for impact windows in every month of the past year, and it shows the scale of the searching: "impact windows florida" and "impact windows cost" each draw about 720 searches a month, "hurricane windows cost" about 1,000, and "impact window installation" about 720, with an average ad cost near $20 a click.</p>
<p>Semrush's twelve-month trend for these phrases moves up and down without one obvious peak, so we would not plan around a single predictable spike. Check your own Search Console data for your market.</p>
<aside class="iws-tldr"><strong>The short version:</strong> Publish product, cost, and city pages before you need them, show your product approvals, explain the insurance and permit steps carefully, and make the next step easy. Keep the tone calm and clear.</aside>

<h2>1. Build the pages before you need them</h2>
<p>New pages are not instantly visible in search, so publish them early. These are worth having:</p>
<ul>
<li>One page per product type you install.</li>
<li>A "what do impact windows cost" page that explains the factors, such as size, frame, glass, and permit, even if you only give ranges.</li>
<li>A page for each city or county you serve, with local jobs and permit details.</li>
<li>A page explaining your estimate and installation process from first call to final inspection.</li>
</ul>

<h2>2. Show your product approvals</h2>
<p>Miami-Dade and Broward counties make up Florida's High Velocity Hurricane Zone. Homeowners and building officials both care that the product installed is approved for where it goes. We cover how to present approvals in <a href="{{LINK:product-approvals-impact-window-pages}}">how to show product approvals on your impact window pages</a>.</p>

<h2>3. Explain the insurance and permit steps carefully</h2>
<p>Florida law requires insurers to provide discounts, credits, or other rate differentials for features that reduce windstorm damage, and homeowners document those features on the state's Uniform Mitigation Verification Inspection Form. Homeowners ask about this. Explain the process, point them to their insurer, and never promise a discount amount. Our guide to <a href="{{LINK:wind-mitigation-inspection-window-companies}}">what window companies should say about wind mitigation</a> goes deeper.</p>

<h2>4. Make the next step easy</h2>
<p>A worried homeowner who finds you late in the evening will not read five pages. Give them a click-to-call button, a short estimate form, and honest expectations on timing. Then answer quickly.</p>

<h2>5. Keep reviews moving all year</h2>
<p>Do not wait for storm season to ask for reviews. A steady flow of recent reviews, plus photos of real Florida installs, gives homeowners something to judge you by. The <a href="{{LINK:google-business-profile-for-window-companies}}">Google Business Profile checklist</a> covers how.</p>

<h2>A note on tone</h2>
<p>People searching around a storm are often worried. Help them understand their options and let them decide. Skip fear-based ads. Calm, clear information treats homeowners fairly and keeps your reputation intact.</p>
<p>The general framework is in <a href="{{LINK:seo-for-window-companies}}">SEO for window companies</a>.</p>
""",
        "faq": [
            ("When should an impact window company publish its pages?",
             "As early as you can. New pages are not instantly visible in search, so publish them before you need them."),
            ("Do I need separate pages for Miami-Dade and Broward?",
             "It is a good idea. Separate pages let you show local jobs and the details that matter in each county, instead of one page that tries to cover both."),
            ("What should an impact window product page include?",
             "The product type and features, approval numbers with links to the official records, warranty terms, photos of real installs, what affects price, and a clear way to request an estimate."),
            ("Should I run ads for impact windows?",
             "Ads can bring calls while organic results build. Check the cost per click in your ad platform, and track cost per signed job so you know whether the spend is worth it."),
        ],
    },
    # ------------------------------------------------------------------ 6
    {
        "slug": "how-to-hire-seo-agency-for-window-company",
        "date": "2026-10-08",
        "title": "How to Hire an SEO Agency for a Window Company: 9 Questions",
        "meta": "Nine questions to ask before hiring an SEO agency for your window company, what good answers sound like, and the red flags that should end the call.",
        "primary_kw": "window contractor marketing",
        "secondary_kw": ["seo for window companies", "window company marketing", "seo for contractors"],
        "alt_titles": [
            "9 Questions That Separate Real SEO Agencies From Report Sellers",
            "Before You Hire an SEO Agency, Ask These 9 Things",
            "Hiring an SEO Agency for Your Window Company? Start Here",
        ],
        "body": """
<p>A monthly report is easy to produce. More phone calls are harder to prove. Ask questions that show which one an agency delivers before you sign.</p>
<p>Use these nine. Ask them of every agency you talk to, including us.</p>
<aside class="iws-tldr"><strong>The short version:</strong> A good agency tells you who owns what, reports on calls and booked jobs, shows its process before you pay, and does not promise rankings it cannot control.</aside>

<h2>The nine questions</h2>
<h3>1. Who owns my Google Business Profile, website, and analytics?</h3>
<p><strong>Good answer:</strong> You do, and you are the owner or an admin on every account from day one. <strong>Red flag:</strong> They hold the accounts, or the site sits on their platform and cannot leave.</p>
<h3>2. What will you report on each month?</h3>
<p><strong>Good answer:</strong> Calls, form leads, booked estimates, and signed jobs, tied to tracked sources. <strong>Red flag:</strong> Impressions, traffic, and "keywords ranking" without calls.</p>
<h3>3. What is the contract length and how do I leave?</h3>
<p><strong>Good answer:</strong> A short initial term, then month to month, with a clear exit and an account handoff. <strong>Red flag:</strong> Twelve months locked in with penalties.</p>
<h3>4. What do you do in the first 30 days?</h3>
<p><strong>Good answer:</strong> Profile completion, tracking setup, a technical check, and a keyword and page plan, in specifics. <strong>Red flag:</strong> "We will optimize your site."</p>
<h3>5. How do you get reviews?</h3>
<p><strong>Good answer:</strong> A system for asking real customers after real jobs, with replies handled. <strong>Red flag:</strong> Buying reviews or offering rewards for them. Google prohibits incentivized reviews.</p>
<h3>6. How do you build links?</h3>
<p><strong>Good answer:</strong> Relevant local and industry sources earned through useful content and real relationships. <strong>Red flag:</strong> Bulk packages of links, or a private blog network. Google's guidelines treat links bought to influence rankings as a violation.</p>
<h3>7. Who will actually work on my account?</h3>
<p><strong>Good answer:</strong> Named people you can speak with. <strong>Red flag:</strong> A sales rep up front and an anonymous team afterward.</p>
<h3>8. Do you know my trade and my market?</h3>
<p><strong>Good answer:</strong> They can talk about your products, approvals, and local competitors without notes. <strong>Red flag:</strong> The same pitch they would give any business.</p>
<h3>9. What happens if it is not working?</h3>
<p><strong>Good answer:</strong> A review point, a straight conversation, and an exit. <strong>Red flag:</strong> Excuses and a longer contract.</p>

<h2>Red flags that should end the call</h2>
<ul>
<li>A guaranteed number one ranking, or page one by a set date. Nobody outside Google controls rankings.</li>
<li>No questions about your business before quoting.</li>
<li>Pressure to sign today.</li>
<li>Refusing to show you any process or sample work.</li>
</ul>

<h2>What a good first month looks like</h2>
<p>You should see your profile fully built, tracking numbers live, a written plan for pages and cities, and the first review requests going out. Rankings and calls come after the groundwork, and no one can promise when.</p>
<p>For the full strategy behind these questions, read <a href="{{LINK:seo-for-window-companies}}">SEO for window companies</a>, and compare options in <a href="{{LINK:window-replacement-leads}}">renting versus owning window replacement leads</a>.</p>
""",
        "faq": [
            ("How much should a window company pay for SEO?",
             "Cost depends on how many cities you serve and how competitive they are. A reputable agency should review your profile, site, and competitors, then give you a scope and a price before you commit."),
            ("How long should an SEO contract be?",
             "Ask what the minimum term is and what it costs to leave. Long lock-ins put the risk on you, so look for a short initial term followed by month to month."),
            ("Should I hire a niche agency or a general one?",
             "A team that knows your trade may understand your products, approvals, and market better. Ask for examples relevant to window and door companies, and check that they can talk about your products and local competitors."),
            ("What should I own when an SEO engagement ends?",
             "Your Google Business Profile, website, domain, analytics, and any content written for you. Confirm ownership in writing before you sign."),
        ],
    },
    # ------------------------------------------------------------------ 7  (Day 1, new)
    {
        "slug": "product-approvals-impact-window-pages",
        "date": "2026-10-08",
        "title": "How to Show Product Approvals on Your Impact Window Pages",
        "meta": "Miami-Dade NOA or Florida Product Approval? What each one is, how to present approval numbers on product pages, and how to keep them accurate.",
        "primary_kw": "florida product approval",
        "secondary_kw": ["miami dade noa", "impact window installation", "impact windows florida"],
        "alt_titles": [
            "Miami-Dade NOA vs Florida Product Approval: What to Put on Your Website",
            "Product Approvals on Impact Window Pages: A Practical Guide",
            "Show Your Approvals: Building Trust on Impact Window Product Pages",
        ],
        "body": """
<p>Homeowners, permit offices, and building officials all want to know one thing about an impact window: is this product approved for where it is going? Your product pages can answer that clearly, and clear answers build trust.</p>
<p>The search numbers show people look for this. Semrush's US data puts "florida product approval" at about 4,400 searches a month and "miami dade noa" at about 1,000.</p>
<aside class="iws-tldr"><strong>The short version:</strong> Name the approval type and number on every product page, link to the official record, explain it in plain English, and recheck it on a schedule. Do not guess. If you are unsure, ask the manufacturer or the building department.</aside>

<h2>The terms, in plain English</h2>
<ul>
<li><strong>High Velocity Hurricane Zone (HVHZ).</strong> The part of Florida with its own product approval requirements. Sources describe it as Miami-Dade and Broward counties.</li>
<li><strong>Miami-Dade Notice of Acceptance (NOA).</strong> An approval issued by Miami-Dade County. Sources say building-envelope products installed in the HVHZ generally need a valid one.</li>
<li><strong>Florida Product Approval (FPA).</strong> The statewide approval system run through the Florida Building Commission, used for products across Florida. The state maintains a database of approved products.</li>
</ul>
<p>The two are not interchangeable in every case. A statewide approval does not automatically satisfy a local building official, and whether an FPA is accepted in the HVHZ depends on the listing itself. Read the approval record for the exact product and use, and confirm current rules with the local building department before you publish a claim.</p>

<h2>What to put on each product page</h2>
<ul>
<li>The product name and series.</li>
<li>The approval type (NOA or FPA) and the approval number.</li>
<li>A link to the official record, so a homeowner or inspector can check it themselves.</li>
<li>A plain-English line about what the approval covers.</li>
<li>The date you last checked it.</li>
<li>Warranty terms and photos of real installs.</li>
</ul>

<h2>Keep it accurate</h2>
<ol>
<li>Assign one person to own approval records.</li>
<li>Recheck every product page on a set schedule, and whenever you add or change a product.</li>
<li>Remove or update pages for discontinued products.</li>
<li>If a record changes, change the page the same day.</li>
</ol>

<h2>What not to do</h2>
<ul>
<li>Do not write that a product is "approved everywhere" or "hurricane proof." Approvals are specific to a product, a use, and a place.</li>
<li>Do not copy approval numbers from a brochure without checking the record.</li>
<li>Do not guess. If you cannot confirm it, leave the claim off the page.</li>
</ul>

<h2>The SEO angle</h2>
<p>Product pages with clear headings, a visible approvals section, and honest detail answer more of a buyer's questions than a page with a photo and a phone number. They also give you something specific to link to from your <a href="{{LINK:impact-window-marketing-florida}}">Florida marketing pages</a>. Publishing approval numbers is a trust practice. This guide cannot tell you it is legally required, so ask your licensing or legal contact if you are unsure.</p>
""",
        "faq": [
            ("What is the difference between a Miami-Dade NOA and a Florida Product Approval?",
             "An NOA is issued by Miami-Dade County, and sources say products installed in the High Velocity Hurricane Zone generally need one. A Florida Product Approval is the statewide system. A statewide approval does not automatically satisfy a local building official, so check the exact record and the local requirement."),
            ("Which counties are in Florida's High Velocity Hurricane Zone?",
             "Sources describe the zone as Miami-Dade and Broward counties. Confirm with the building code and your local building department."),
            ("Do I have to publish approval numbers on my website?",
             "Publishing them is a trust practice, and this guide cannot tell you it is legally required. If you are unsure, ask your licensing or legal contact."),
            ("How often should I recheck product approvals?",
             "Whenever you add or change a product, and on a schedule you set, such as quarterly. Update the page the same day if a record changes."),
        ],
    },
    # ------------------------------------------------------------------ 8  (Day 1, new)
    {
        "slug": "wind-mitigation-inspection-window-companies",
        "date": "2026-10-08",
        "title": "Wind Mitigation and Window Companies: What to Say Online",
        "meta": "Homeowners ask about wind mitigation discounts when they shop for impact windows. Here is what window companies can explain, and what to leave to insurers.",
        "primary_kw": "wind mitigation inspection",
        "secondary_kw": ["wind mitigation form", "impact windows florida", "impact windows insurance discount"],
        "alt_titles": [
            "Wind Mitigation Inspections: A Guide for Florida Window Companies",
            "What Window Companies Can Say About Insurance Discounts (and What They Can't)",
            "Wind Mitigation Basics Your Impact Window Pages Should Explain",
        ],
        "body": """
<p>Homeowners who shop for impact windows often ask whether they will save on insurance. Semrush's US data shows people searching for the topic: "wind mitigation inspection" gets about 3,600 searches a month and "wind mitigation form" about 320.</p>
<p>A window company can help by explaining the basics clearly. The line to hold is simple: explain the process, do not promise a result.</p>
<aside class="iws-tldr"><strong>The short version:</strong> Explain what a wind mitigation inspection is, link to the official form, tell homeowners to ask their own insurer what applies, and never quote a discount amount.</aside>

<h2>What the law says, in brief</h2>
<p>Florida Statute 627.0629 requires insurers to provide discounts, credits, or other rate differentials for construction techniques that reduce damage and loss in windstorms. Opening protection and the strength of windows and doors are among the features it covers.</p>
<p>Homeowners document those features with the state's Uniform Mitigation Verification Inspection Form (OIR-B1-1802). State law lists which licensed professionals may sign it, and the form is revised from time to time. Link to the current version on the Office of Insurance Regulation's website instead of copying details onto your pages.</p>

<h2>What you can explain on your pages</h2>
<ul>
<li>What a wind mitigation inspection is, in two or three plain sentences.</li>
<li>That homeowners submit the form to their insurer to document features like opening protection.</li>
<li>That each insurer decides how it applies the credits, so the homeowner should ask theirs.</li>
<li>How your own process works: permits, installation, final inspection, and what paperwork you provide.</li>
</ul>

<h2>What to leave off</h2>
<ul>
<li><strong>Discount amounts.</strong> They vary by insurer, policy, and home. If you quote a number, you own the claim.</li>
<li><strong>Promises.</strong> Never write "you will save" or "guaranteed discount."</li>
<li><strong>Insurance advice.</strong> You are a window company. Send homeowners to their insurer or agent for coverage questions.</li>
</ul>

<h2>How to build the page</h2>
<ol>
<li>Title it for the question: "Wind Mitigation and Impact Windows in Florida."</li>
<li>Open with a two-sentence answer, then a short explanation of the form.</li>
<li>Link to the official form and to the statute.</li>
<li>Add a FAQ for the questions your estimators hear most.</li>
<li>End with a plain call to action: request an estimate.</li>
<li>Review the page every few months, since forms and rules change.</li>
</ol>

<h2>Where this fits</h2>
<p>This page works best next to your product pages and your <a href="{{LINK:product-approvals-impact-window-pages}}">product approvals</a>, and as part of the wider plan in <a href="{{LINK:impact-window-marketing-florida}}">impact window marketing in Florida</a>.</p>
""",
        "faq": [
            ("What is a wind mitigation inspection?",
             "It is an inspection that documents features of a home that reduce windstorm damage, such as opening protection, recorded on Florida's Uniform Mitigation Verification Inspection Form. The homeowner can submit the form to their insurer."),
            ("What does Florida law say about wind mitigation discounts?",
             "Florida Statute 627.0629 requires insurers to provide discounts, credits, or other rate differentials for construction techniques that reduce damage and loss in windstorms. How much a homeowner receives depends on the insurer and the policy."),
            ("Can a window company promise an insurance discount?",
             "No. Discounts depend on the insurer, the policy, and the home. Explain the process and send homeowners to their insurer."),
            ("Who can sign the wind mitigation form?",
             "State law lists the licensed professionals who may sign it, and the rules can change. Link to the Office of Insurance Regulation and the statute instead of repeating the list on your page."),
        ],
    },
    # ------------------------------------------------------------------ 9  (Day 2, 2026-11-11)
    {
        "slug": "google-review-request-wording-window-companies",
        "date": "2026-11-11",
        "title": "How to Ask for Google Reviews Without Breaking Google's Rules",
        "meta": "Review request wording for window and door companies that stays inside Google's review policy and the FTC review rule. Text, email, and in-person scripts.",
        "primary_kw": "how to ask for google reviews",
        "secondary_kw": ["google review request template", "google review policy", "review gating"],
        "alt_titles": [
            "Review Request Wording for Window Companies That Follows Google's Policy",
            "Asking for Google Reviews: Scripts That Stay Inside the Rules",
            "The Review Request Text Every Window Installer Can Copy",
        ],
        "body": """
<p>Reviews matter to a window company because homeowners read them before they call. But the way you ask for them matters too. Google's review policy and a federal rule both draw lines around what a business can and cannot do when it asks.</p>
<p>This guide gives you wording you can copy, and explains which kinds of requests cross those lines.</p>
<aside class="iws-tldr"><strong>The short version:</strong> Ask every customer the same way, ask for an honest review, never offer anything in return, and never screen out unhappy customers first. Use the review link or QR code from your own Business Profile. Keep staff names and quotas out of it.</aside>

<h2>What Google's policy allows</h2>
<p>Google's policy for user contributed content lets businesses ask customers for reviews that reflect a genuine experience. Asking is fine. The problems start with how you ask and what you offer.</p>
<p>Google Business Profile even gives you a tool for it. In your profile, open your reviews and look for the option to get more reviews. It creates a review link you can copy and a QR code you can download. Google's help page says the QR code can only be generated from a computer browser, and suggests sharing the link in places like thank-you emails and receipts.</p>

<h2>What Google's policy does not allow</h2>
<ul>
<li><strong>Incentives.</strong> No money, discounts, gift cards, free service, or prize drawings for posting a review. The same goes for offering something to get a customer to change or remove a negative review.</li>
<li><strong>Review gating.</strong> Google's policy says merchants may not discourage negative reviews or selectively ask only happy customers for positive ones. A "Were you happy? If yes, review us on Google" flow is the classic example.</li>
<li><strong>Staff quotas and staff names.</strong> Google's policy now also lists requiring staff to collect a certain number of reviews and asking customers to include specific content, such as naming a staff member.</li>
<li><strong>Reviews from your own side.</strong> Google's conflict of interest rule says people who own or work at a business should not review it.</li>
</ul>

<h2>The federal rule to know about</h2>
<p>The Federal Trade Commission's rule on consumer reviews and testimonials took effect in October 2024. Among other things, it bars buying fake reviews, paying or rewarding customers for reviews that express a particular sentiment, and certain reviews by company insiders that do not disclose the connection. The FTC can seek civil penalties for knowing violations. If you have questions about how it applies to you, ask your attorney.</p>

<h2>Wording you can copy</h2>
<p>Each script below asks for an honest review, offers nothing in return, and goes to every customer.</p>
<p><strong>Text message, the day the job is signed off:</strong></p>
<p>"Hi [first name], this is [your name] from [company]. Thanks for having us install your windows. If you have a minute, we would appreciate an honest review of your experience on Google: [review link]. Any feedback helps us and helps your neighbors choose."</p>
<p><strong>Email follow-up:</strong></p>
<p>"Subject: How did your installation go? Hi [first name], thank you for choosing [company]. We read every review, good or bad, and use what customers tell us to improve. If you are willing, you can leave a review here: [review link]. Thank you for your time."</p>
<p><strong>In person, at the final walkthrough:</strong></p>
<p>"We ask every customer for an honest review on Google. Here is a card with a QR code if you would like to leave one."</p>

<h2>Wording to avoid</h2>
<ul>
<li>"Leave us a 5-star review." That asks for a particular sentiment, not an honest review.</li>
<li>"Review us and get $25 off your next service." That is an incentive.</li>
<li>"Please mention Mike by name." That asks for specific staff content.</li>
<li>"If you were not happy, call us instead of posting." That discourages negative reviews.</li>
</ul>

<h2>A note on other review sites</h2>
<p>Each platform sets its own rules. Yelp, for example, is widely reported to discourage businesses from asking for reviews at all. Read each site's current guidelines before you add it to your follow-up messages.</p>

<h2>Where this fits</h2>
<p>Reviews are one part of a complete profile. See our <a href="{{LINK:google-business-profile-for-window-companies}}">Google Business Profile checklist for window companies</a>, the wider plan in <a href="{{LINK:seo-for-window-companies}}">SEO for window companies</a>, and our guide to <a href="{{LINK:reply-to-negative-reviews-window-companies}}">replying to negative reviews</a> for what to do once the reviews come in.</p>
""",
        "faq": [
            ("Is it against Google's rules to ask customers for reviews?",
             "No. Google's policy lets businesses ask for reviews that reflect a genuine experience. What it prohibits is offering incentives, discouraging negative reviews, and asking only satisfied customers."),
            ("Can I offer a discount or gift card for a Google review?",
             "No. Google's policy prohibits incentives for reviews, and the FTC's review rule bars paying or rewarding customers for reviews that express a particular sentiment."),
            ("What is review gating?",
             "Review gating means screening customers first and sending only happy ones to Google. Google's policy says merchants may not discourage negative reviews or selectively solicit positive ones."),
            ("Where do I get my Google review link?",
             "In your Google Business Profile, open your reviews and choose the option to get more reviews. Google provides a link to copy and a QR code to download from a computer browser."),
        ],
    },
    # ------------------------------------------------------------------ 10 (Day 2, 2026-11-11)
    {
        "slug": "reply-to-negative-reviews-window-companies",
        "date": "2026-11-11",
        "title": "How Window Companies Should Reply to Negative Reviews",
        "meta": "A calm, practical way for window and door companies to reply to negative Google reviews, report ones that break policy, and avoid replies that backfire.",
        "primary_kw": "how to respond to negative reviews",
        "secondary_kw": ["reply to google reviews", "remove google review", "negative review response example"],
        "alt_titles": [
            "Replying to a Bad Review: A Guide for Window and Door Installers",
            "What to Say When a Customer Leaves a One-Star Review",
            "Negative Reviews for Window Companies: Reply, Report, or Both",
        ],
        "body": """
<p>Every window company that does enough installs will get a negative review eventually. A delayed permit, a missed appointment, a scratched frame. The review is public, and so is your reply.</p>
<p>That second part is the opportunity. The reviewer reads your reply, but so does every homeowner who looks at your profile afterward.</p>
<aside class="iws-tldr"><strong>The short version:</strong> Reply calmly and briefly, protect the customer's privacy, move the details offline, and fix what you can. Report a review only if it breaks Google's policy. Never offer anything to get a review removed, and never threaten a reviewer.</aside>

<h2>What Google says about replies</h2>
<p>Google's Business Profile help pages describe replies as public and recommend keeping them positive and relevant. For negative reviews, Google advises protecting the reviewer's privacy and avoiding personal attacks.</p>
<p>Google also notes that the reviewer is notified when you reply and can update their review afterward. A constructive reply gives them a reason to.</p>

<h2>A simple structure for every negative reply</h2>
<ol>
<li><strong>Thank them and acknowledge the problem.</strong> Name the issue in plain words without arguing about it.</li>
<li><strong>Take responsibility for your part.</strong> If the crew was late, say so.</li>
<li><strong>Move it offline.</strong> Give a name and a direct way to reach you.</li>
<li><strong>Keep private details private.</strong> No invoice amounts, addresses, or job history in a public reply.</li>
<li><strong>Follow up.</strong> If you fix the problem, the customer may choose to update the review. Do not ask for that in exchange for the fix.</li>
</ol>

<h2>Example replies</h2>
<p><strong>A scheduling problem:</strong></p>
<p>"Thank you for letting us know, [first name]. You should not have had to wait on a missed install date, and we are sorry. I would like to make this right. Please call me directly at [number] so I can look into what happened. [Your name], [title]."</p>
<p><strong>A workmanship complaint:</strong></p>
<p>"We are sorry the finish on your new windows was not what you expected. We want to take a look. Please contact our service manager, [name], at [number] or [email] so we can schedule a visit."</p>
<p><strong>A review you do not recognize:</strong></p>
<p>"We take every review seriously, but we could not find a record matching this description. If you worked with us, please call [number] so we can help."</p>

<h2>Replies that backfire</h2>
<ul>
<li>Arguing the facts point by point in public.</li>
<li>Sharing the customer's job details, price, or address.</li>
<li>Copying the same reply onto every review.</li>
<li>Hinting at legal action. The FTC's consumer review rule bars using unfounded legal threats, intimidation, or certain false public accusations to prevent or remove a negative review.</li>
</ul>

<h2>When to report a review instead</h2>
<p>Disagreeing with a review is not a reason to report it. Reporting is for reviews that break Google's policies, such as spam, conflicts of interest, or off-topic content. Google's help pages describe a Reviews Management Tool where you can check the status of reviews you have reported and, in some cases, appeal a decision.</p>
<p>Whatever happens, do not offer a customer a refund, discount, or anything else to remove or change a review. Google's policy prohibits incentives for revising or removing reviews.</p>

<h2>Where this fits</h2>
<p>The best protection against one bad review is a steady flow of honest ones. Use the scripts in <a href="{{LINK:google-review-request-wording-window-companies}}">how to ask for Google reviews without breaking Google's rules</a>, keep your <a href="{{LINK:google-business-profile-for-window-companies}}">Business Profile</a> complete, and see how reviews fit into <a href="{{LINK:local-seo-for-contractors}}">local SEO for contractors</a>.</p>
""",
        "faq": [
            ("Should a window company reply to every negative review?",
             "Replying is recommended. Google describes replies as public and suggests keeping them positive and relevant, and the reviewer is notified when you reply and can update their review."),
            ("Can I get a negative Google review removed?",
             "Only if it breaks Google's policies, such as spam or a conflict of interest. You can report it and check its status in Google's Reviews Management Tool. Disagreeing with a review is not grounds for removal."),
            ("Can I offer a refund if the customer deletes their review?",
             "No. Google's policy prohibits offering incentives to revise or remove reviews. Fix the problem because it is the right thing to do, and let the customer decide about the review."),
            ("Can I threaten legal action over a bad review?",
             "Be careful. The FTC's consumer review rule bars using unfounded legal threats, intimidation, or certain false public accusations to prevent or remove a negative review. Talk to an attorney before taking any step."),
        ],
    },
    # ------------------------------------------------------------------ 11 (Day 3, 2026-11-12)
    {
        "slug": "city-pages-for-window-companies",
        "date": "2026-11-12",
        "title": "City Pages for Window Companies Without Duplicate Content",
        "meta": "How window and door companies can build city and location pages that help homeowners, stay clear of Google's doorway policy, and avoid copy-paste content.",
        "primary_kw": "location pages seo",
        "secondary_kw": ["city landing pages", "local landing pages", "doorway pages"],
        "alt_titles": [
            "Location Pages for Window Installers: Useful, Not Copy-Paste",
            "How to Build City Pages That Google and Homeowners Both Respect",
            "One Page per City, Done Right: A Guide for Window Companies",
        ],
        "body": """
<p>Most window companies work in more than one city, and most want a page for each. The common shortcut is to write one page, copy it, and swap the city name. That shortcut is the problem this guide is about.</p>
<p>People search for this. Semrush's US data puts "location pages seo" at about 480 searches a month and "local landing pages" at about 390.</p>
<aside class="iws-tldr"><strong>The short version:</strong> Build a city page only when you have something specific to say about that city: real jobs, local permit steps, the products you install there, and photos. Link every city page from a clear service-area hub. Never mass-produce near-identical pages with a new city name.</aside>

<h2>What Google's spam policy says</h2>
<p>Google's spam policies for web search describe "doorway abuse" as sites or pages created to rank for specific, similar search queries that lead users to intermediate pages less useful than the final destination. The examples Google lists include:</p>
<ul>
<li>Having multiple domain names or pages targeted at specific regions or cities that funnel users to one page.</li>
<li>Creating substantially similar pages that are closer to search results than a clearly defined, browseable hierarchy.</li>
</ul>
<p>The same policy page describes "scaled content abuse": many pages generated mainly to manipulate rankings rather than help users, no matter how they are created. Google says these behaviors can lead to a page or a whole site ranking lower or being left out of results.</p>
<p>None of that bans city pages. It bans city pages that exist only to catch a search and add nothing.</p>

<h2>The test for every city page</h2>
<p>Ask one question: would a homeowner in this city learn something here that they could not learn on your other city pages? If the honest answer is no, do not publish the page yet.</p>

<h2>What a useful city page includes</h2>
<ul>
<li><strong>Jobs you actually did there.</strong> Photos of real installs in that city, with a sentence on what the job involved.</li>
<li><strong>Local permit and inspection steps.</strong> How the process works with that building department, in plain English. Check it with the department before you publish.</li>
<li><strong>Products you install there.</strong> If the city sits in an area with specific product approval needs, say which approvals your products carry and link to the records. Our guide to <a href="{{LINK:product-approvals-impact-window-pages}}">showing product approvals</a> covers how.</li>
<li><strong>Questions you hear from that city.</strong> Older homes, condo association rules, HOA approvals, whatever your estimators actually get asked.</li>
<li><strong>A clear next step.</strong> Phone number, estimate form, and honest expectations on timing.</li>
</ul>

<h2>A simple structure</h2>
<ol>
<li><strong>One service-area hub page.</strong> Lists every city you serve and links to each city page.</li>
<li><strong>One page per city where you have real work to show.</strong> Linked from the hub and from relevant product pages.</li>
<li><strong>Product pages stay product pages.</strong> Link from them to the city pages where you install that product, instead of cloning the product page per city.</li>
</ol>
<p>That gives homeowners, and Google, a browseable hierarchy instead of a pile of near-duplicates.</p>

<h2>What not to do</h2>
<ul>
<li>Do not generate dozens of pages from a template and change only the city name.</li>
<li>Do not create pages for cities you do not actually serve.</li>
<li>Do not stuff a list of neighborhoods into a footer to catch searches.</li>
<li>Do not use AI or spinning tools to churn out "unique" versions of the same page. Google's policy applies no matter how the pages are made.</li>
</ul>

<h2>How many city pages to start with</h2>
<p>Start with the cities where you already have the most finished jobs and photos. Add a new city page when you have enough real material to make it useful. Fewer, better pages beat a long list of thin ones.</p>

<h2>Where this fits</h2>
<p>City pages are step three in our <a href="{{LINK:seo-for-window-companies}}">SEO plan for window companies</a>. Make sure the service area in your <a href="{{LINK:google-business-profile-for-window-companies}}">Google Business Profile</a> matches the cities your pages describe.</p>
""",
        "faq": [
            ("Are city pages against Google's guidelines?",
             "No. Google's spam policy targets doorway pages: pages aimed at specific cities that funnel users to one page, or substantially similar pages with little value. A city page with real local jobs, permit steps, and photos is not that."),
            ("Can I reuse some text across city pages?",
             "Some shared material, such as your warranty terms or contact details, is normal. The core of each page should be specific to that city: local jobs, local steps, and local questions."),
            ("How many city pages should a window company have?",
             "There is no set number. Build a page for each city where you have real work to show, and add more as you finish jobs in new areas."),
            ("Should I use AI to write city pages faster?",
             "Google's scaled content abuse policy applies to pages generated mainly to manipulate rankings, no matter how they are made. If you use any tool, add real local detail and check every fact before publishing."),
        ],
    },
    # ------------------------------------------------------------------ 12 (Day 3, 2026-11-12)
    {
        "slug": "call-tracking-for-window-companies",
        "date": "2026-11-12",
        "title": "Call Tracking for Window Companies: A Setup That Stays Clean",
        "meta": "How window companies can use call tracking numbers to see which pages and ads bring estimates, while keeping Google Business Profile details consistent.",
        "primary_kw": "call tracking numbers",
        "secondary_kw": ["dynamic number insertion", "call tracking for small business", "call tracking seo"],
        "alt_titles": [
            "Call Tracking Numbers for Window Installers, Explained",
            "Which Ads and Pages Bring Your Window Estimates? Call Tracking Basics",
            "Track Every Call Without Confusing Google: A Window Company Guide",
        ],
        "body": """
<p>Homeowners often call before they fill out a form, especially for a big job like windows. If you cannot tell which search, ad, or page produced a call, you cannot tell which marketing is paying for itself.</p>
<p>Semrush's US data shows people researching the tools: about 390 searches a month for "call tracking numbers" and about 880 for "dynamic number insertion."</p>
<aside class="iws-tldr"><strong>The short version:</strong> Give each marketing source its own tracking number, keep your real local number published and consistent, follow Google's phone rules on your Business Profile, and get proper consent before recording calls. Judge everything on booked estimates and signed jobs.</aside>

<h2>How call tracking works</h2>
<p>A tracking number is a phone number that forwards to your real line and records which source the call came from. There are two common setups:</p>
<ul>
<li><strong>One number per source.</strong> A different number on your Business Profile, your ads, your truck wrap, and your mailers.</li>
<li><strong>Dynamic number insertion.</strong> Your website shows a different number depending on how the visitor arrived, so a visitor from an ad sees one number and a visitor from organic search sees another.</li>
</ul>

<h2>What Google's Business Profile guidelines say about phone numbers</h2>
<p>Google's guidelines for representing your business say:</p>
<ul>
<li>Provide a phone number that connects to your individual business location.</li>
<li>Use a local phone number instead of a central call center helpline whenever possible.</li>
<li>Do not provide phone numbers that redirect or refer users to numbers other than those of the actual business.</li>
<li>The phone number must be under the direct control of the business.</li>
<li>Additional phone numbers can be used on Business Profile and other local surfaces.</li>
</ul>
<p>The guideline text does not mention call tracking numbers by name. Many call tracking vendors describe the same setup: a local tracking number that rings your business goes in the primary phone field, and your main business number goes in the additional phone field. That is a vendor recommendation, not a Google statement, so read the current guidelines yourself before you change your profile.</p>

<h2>Keep your real number consistent</h2>
<p>Your main local number is the one that should appear on your website footer, your directory listings, and your paperwork. Tracking numbers are for measurement. Pick tracking numbers that are local, that you control, and that you can keep long term, because a number printed on a truck or a yard sign stays out there.</p>

<h2>Recording calls in Florida</h2>
<p>Many tracking tools can record calls, which helps with training and with checking which calls became estimates. Florida's law on intercepting communications makes recording lawful when all parties to the call have given prior consent. If you record, tell callers at the start and talk to your attorney about how to get consent properly. If callers can be outside Florida, ask about their states' rules too.</p>

<h2>What to measure</h2>
<p>A call count is a start, not an answer. For each source, track:</p>
<ol>
<li>Calls from real prospects, not vendors or existing customers.</li>
<li>Booked estimates.</li>
<li>Signed jobs.</li>
<li>Spend, so you can work out cost per signed job.</li>
</ol>
<p>We walk through that math in <a href="{{LINK:window-replacement-leads}}">renting versus owning window replacement leads</a>.</p>

<h2>Common mistakes</h2>
<ul>
<li>Putting a different tracking number on every directory, which spreads several numbers across the web as if they were your main line.</li>
<li>Using numbers that belong to a vendor's account, so you lose them if you switch vendors. Ask who controls the numbers before you sign.</li>
<li>Recording calls without telling callers.</li>
<li>Reporting calls without checking which ones became booked estimates.</li>
</ul>

<h2>Where this fits</h2>
<p>Tracking is step five in our <a href="{{LINK:seo-for-window-companies}}">SEO plan for window companies</a> and part of month one in <a href="{{LINK:local-seo-for-contractors}}">the 90-day local SEO plan</a>.</p>
""",
        "faq": [
            ("Can I use a call tracking number on my Google Business Profile?",
             "Google's guidelines do not mention tracking numbers by name. They require a number that connects to your business, is under your direct control, and does not redirect callers to another business, and they allow additional phone numbers. Many vendors suggest a local tracking number as primary and your main number as additional. Check the current guidelines first."),
            ("What is dynamic number insertion?",
             "It is a website feature that shows a different phone number depending on how the visitor arrived, such as from an ad or from organic search, so each call can be traced to its source."),
            ("Is it legal to record customer calls in Florida?",
             "Florida's law makes recording lawful when all parties to the call have given prior consent. Tell callers at the start and ask your attorney how to handle consent properly."),
            ("What should a window company measure with call tracking?",
             "Calls from real prospects, booked estimates, signed jobs, and spend for each source, so you can compare cost per signed job across channels."),
        ],
    },
]
