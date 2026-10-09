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
]
