"""Blog post source for impactwindowsseo.com.

Each post: slug, title, meta, primary/secondary keywords, three alternate titles
(for A/B tests), body HTML, FAQ list. build.py turns these into WordPress-ready
HTML with JSON-LD (BlogPosting + WebPage + BreadcrumbList + FAQPage +
ProfessionalService). The visible FAQ and the FAQPage markup come from the same
list, so they cannot drift apart.

Internal links use {{LINK:slug}}. Search volumes are Semrush US database,
pulled 2026-10-08.
"""

POSTS = [
    # ------------------------------------------------------------------ 1
    {
        "slug": "seo-for-window-companies",
        "title": "SEO for Window Companies: What Gets the Phone Ringing",
        "meta": "Most window companies lose local searches to rivals with better Google profiles. Here is the five-part SEO plan that fixes it, in the order that matters.",
        "primary_kw": "seo for window companies",
        "secondary_kw": ["window company marketing", "window contractor marketing", "window replacement near me"],
        "alt_titles": [
            "Your Next Window Customer Is Already Searching. Will They Find You?",
            "Why Window Companies With Better Work Lose Jobs on Google",
            "The 5-Part SEO Plan for Window and Door Companies",
        ],
        "body": """
<p>Someone in your service area searched "window replacement near me" today. Semrush's US data puts that phrase at about 33,100 searches a month, and most of those searchers call one of the first three businesses they see.</p>
<p>If your company is not one of those three, you did not lose the job on price or quality. You lost it before the homeowner knew you existed.</p>
<aside class="iws-tldr"><strong>The short version:</strong> Window SEO comes down to five things: a complete Google Business Profile, a steady flow of recent reviews, one real page for every product and city you serve, proof on every page, and call tracking so you know what works. Do them in that order.</aside>

<h2>Why window SEO behaves differently</h2>
<p>A window or door replacement is a big, considered purchase. Homeowners compare photos, reviews, warranties, financing, and installers before anyone picks up a phone. Two kinds of searches matter at the same time:</p>
<ul>
<li><strong>Local searches</strong> like "window replacement near me" or "window installers in Fort Lauderdale." These trigger the Google map results and they send calls.</li>
<li><strong>Product searches</strong> like "impact windows cost" or "casement vs double hung." These send researchers, who call later if you were the helpful one.</li>
</ul>
<p>Fix the local side first. Those searchers are closest to calling, so it pays fastest.</p>

<h2>1. Finish your Google Business Profile</h2>
<p>Your profile is what shows up in the map results, so for most "near me" searches it matters more than your website. Most profiles we see are half filled out. Here is what a complete one has:</p>
<ul>
<li>The closest primary category, plus every secondary category that truly applies.</li>
<li>Every product and service you install, each with a short description.</li>
<li>Real photos of finished installs, your crew, and your trucks, with new ones added every week.</li>
<li>A service area that lists the cities you actually work in.</li>
<li>A post at least twice a month. A photo of a finished job counts.</li>
</ul>
<p>We walk through every field in our <a href="{{LINK:google-business-profile-for-window-companies}}">Google Business Profile checklist for window companies</a>.</p>

<h2>2. Build a review habit, not a review burst</h2>
<p>Reviews are the closest thing local SEO has to a scoreboard. Google reads them and so does the homeowner. What counts is a steady flow of recent, specific reviews, not a pile collected in one weekend.</p>
<p>The simplest system: when an install is signed off, text the customer a direct link to your Google review page within a day or two, while they are still happy. Reply to every review, good or bad, within 48 hours.</p>
<p>Our sister company, RankLogic SEO, used this approach to take Wayne's Roofing Co. in Ocean County, New Jersey, past 331 Google reviews and to the number one rated roofing company in the county. Roofing and windows are different trades, but the buying behavior matches: homeowners trust what other homeowners say.</p>

<h2>3. Build one real page for every product and city</h2>
<p>Google can only send a homeowner to a page that exists. If you install impact windows in Fort Lauderdale, Pompano Beach, and Hollywood, each city deserves its own page with the products you install there, photos of local jobs, and the permit details for that area.</p>
<p>Do not clone one page and swap the city name. Google treats that as thin content and homeowners see through it. Write each page so it would still be useful with your logo removed.</p>

<h2>4. Put proof on every page</h2>
<p>A homeowner choosing between three installers is hunting for the reason to trust one. Hand it to them:</p>
<ul>
<li>Product approvals and warranty terms in plain English.</li>
<li>Photos of real installs, ideally with the city named.</li>
<li>What affects price, so the first call is not a shock.</li>
<li>Financing options, license numbers, and your best reviews.</li>
</ul>

<h2>5. Track calls, not rankings</h2>
<p>A ranking report does not pay your crew. Set up call tracking and form tracking so you can see which searches and pages produce estimates. Then judge your SEO on booked estimates and signed jobs.</p>

<h2>How long it takes</h2>
<p>Profile and technical fixes can move results within weeks. Steady call volume usually builds over about 90 days as pages get indexed and reviews stack up. Anyone who promises page one in a week is guessing.</p>
<p>Compare this with paying for leads in our guide to <a href="{{LINK:window-replacement-leads}}">renting versus owning window replacement leads</a>.</p>
""",
        "faq": [
            ("How much does SEO cost for a window company?",
             "It depends on how many cities you serve and how competitive each one is. A one-city shop needs less than a company covering a whole county. Any agency should be able to review your profile, site, and competitors, then tell you what the work costs before you commit."),
            ("Is SEO better than paying for window leads?",
             "They do different jobs. Paid leads and ads are faster but stop when you stop paying. SEO takes longer to build, then keeps sending calls without a per-lead fee. Many companies use both while organic search ramps up."),
            ("How long does SEO take to work for a window company?",
             "Profile and technical fixes can move results in weeks. Steady call volume usually builds over about 90 days. Anyone promising page one in a week is guessing."),
            ("Do I need a blog to rank?",
             "Not first. Fix your Google Business Profile, your reviews, and your product and city pages before anything else. Blog posts help later, once those foundations are in place."),
        ],
    },
    # ------------------------------------------------------------------ 2
    {
        "slug": "window-replacement-leads",
        "title": "Window Replacement Leads: Rent Them or Own Them?",
        "meta": "Shared lead sites and ads rent you customers by the click. See how organic search compares for window companies, with the math to check it yourself.",
        "primary_kw": "window replacement leads",
        "secondary_kw": ["window replacement near me", "window contractor marketing"],
        "alt_titles": [
            "Stop Renting Window Replacement Leads. Here Is the Math.",
            "What a Window Replacement Lead Really Costs You",
            "Paid Leads vs SEO for Window Companies: A Fair Comparison",
        ],
        "body": """
<p>Search "window replacement leads" and you land in a wall of lead vendors. Semrush's US data shows advertisers paying an average of about $22.57 a click on that phrase and about $30.60 a click on "window replacement near me." Those are market estimates, but they say one thing clearly: other companies have decided your customers are worth fighting over.</p>
<p>The question is whether you want to keep renting access to them.</p>
<aside class="iws-tldr"><strong>The short version:</strong> Paid leads and ads are fast and they stop the day you stop paying. Organic search is slower and it keeps working. Track cost per signed job for each channel and let the numbers decide.</aside>

<h2>What renting leads really costs</h2>
<p>There are two common ways to rent customers:</p>
<ul>
<li><strong>Shared lead sites.</strong> The same homeowner request goes to several contractors. You race to call first and quote best.</li>
<li><strong>Pay-per-click ads.</strong> You pay for every click, whether or not that person ever calls.</li>
</ul>
<p>Neither one is wrong. Both share one trait: the moment you stop paying, the phone stops ringing.</p>

<h2>Do the math with your own numbers</h2>
<p>Cost per lead is the wrong number. The number that matters is cost per signed job:</p>
<p><strong>Cost per signed job = what you spent on the channel &divide; jobs you signed from it</strong></p>
<p>Here is an illustration with made-up numbers, not a benchmark. Say you spend $3,000 and get 40 leads. 12 become booked estimates and 4 become signed jobs. That is $750 per signed job in lead cost alone, before your estimator's time and drive. Your own numbers will differ, which is the point. Run them.</p>

<h2>What owning leads looks like</h2>
<p>Owning leads means showing up in the map results and on page one when a homeowner searches, so they call you directly. Nobody else gets the same call and there is no per-lead fee.</p>
<table>
<thead><tr><th>&nbsp;</th><th>Renting (leads, ads)</th><th>Owning (organic search)</th></tr></thead>
<tbody>
<tr><td>Speed</td><td>Days</td><td>Weeks to months</td></tr>
<tr><td>Cost behavior</td><td>Pay every time</td><td>Mostly upfront and monthly work</td></tr>
<tr><td>Who else gets the call</td><td>Often several rivals</td><td>The homeowner picked you</td></tr>
<tr><td>If you stop paying</td><td>Leads stop immediately</td><td>Results fade slowly</td></tr>
<tr><td>Compounds over time</td><td>No</td><td>Yes, reviews and pages stay</td></tr>
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
             "It depends on your cost per signed job. Shared leads go to several contractors, so your close rate is usually lower than with a lead only you receive. Track spend against signed jobs for 90 days before deciding."),
            ("Can SEO replace paid leads for a window company?",
             "Over time it can replace much of them. SEO builds slowly, so most companies keep a smaller paid budget while organic rankings and reviews grow."),
            ("How do I know if a lead is exclusive?",
             "Ask the vendor in writing how many contractors receive each lead. If the answer is more than one, it is a shared lead."),
            ("How much does a window replacement lead cost?",
             "Prices vary by market and vendor. Semrush's US data shows advertisers averaging about $22.57 per click on the phrase 'window replacement leads,' and a click is not yet a lead, so true cost per signed job runs higher."),
        ],
    },
    # ------------------------------------------------------------------ 3
    {
        "slug": "local-seo-for-contractors",
        "title": "Local SEO for Contractors: The 90-Day Plan",
        "meta": "A month-by-month local SEO plan for contractors: what to fix first, what to skip, and what to expect by day 90. No jargon, no vanity metrics.",
        "primary_kw": "local seo for contractors",
        "secondary_kw": ["seo for contractors", "local seo for home services"],
        "alt_titles": [
            "Local SEO for Contractors, Explained in 90 Days",
            "What to Fix First if Your Contracting Business Is Invisible on Google",
            "The Contractor's Month-by-Month Local SEO Checklist",
        ],
        "body": """
<p>About 3,600 people a month search "seo for contractors" in the US, according to Semrush, and 1,600 more search "local seo for contractors." Contractors are looking for help. Most of what they find is an agency selling reports.</p>
<p>This plan is built around one result: calls from homeowners in your service area.</p>
<aside class="iws-tldr"><strong>The short version:</strong> Month 1 is foundation, month 2 is pages and reviews, month 3 is expansion and measurement. Skip blogging, link buying, and directory blasts until the basics are done.</aside>

<h2>Month 1: Foundation</h2>
<ul>
<li><strong>Claim and complete your Google Business Profile.</strong> Categories, services, photos, service area, hours.</li>
<li><strong>Make your name, address, and phone number identical everywhere.</strong> Small mismatches confuse Google about which listing is yours.</li>
<li><strong>Set up call and form tracking.</strong> Without it you are guessing.</li>
<li><strong>Fix the technical basics.</strong> The site must load fast on a phone and work on a phone.</li>
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
<li><strong>Close the review gap.</strong> Count how many new reviews the top three map results add per month and aim to match or beat it.</li>
</ul>

<h2>What to skip at first</h2>
<ul>
<li><strong>Blogging before the foundation.</strong> Posts help later. They do not rescue a thin profile.</li>
<li><strong>Buying links.</strong> It is risky and it is the fastest way to a penalty.</li>
<li><strong>Submitting to 200 directories.</strong> A handful of accurate, relevant listings beats a blast.</li>
</ul>

<h2>What to expect by day 90</h2>
<p>You should see more profile views, more direction and call taps, and early movement in the map results for your core services. Meaningful call volume usually keeps building after that. If someone promises page one in a week, they are guessing.</p>
<p>For a trade-specific version of this plan, see <a href="{{LINK:seo-for-window-companies}}">SEO for window companies</a>.</p>
""",
        "faq": [
            ("How long does local SEO take for contractors?",
             "Early movement often shows in weeks, and steady call volume usually builds over about 90 days. Competitive markets take longer."),
            ("What should a contractor fix first for local SEO?",
             "Your Google Business Profile. Complete every field, add real photos, list your services, and set your service area. It is the fastest improvement for map results."),
            ("Do citations and directory listings still matter?",
             "Accurate listings on a small number of relevant sites help Google confirm your business details. Quantity matters far less than consistency."),
            ("How many Google reviews does a contractor need?",
             "There is no magic number. Look at the top three map results for your main service and city, then match or beat both their total and how fast they add new reviews."),
        ],
    },
    # ------------------------------------------------------------------ 4
    {
        "slug": "google-business-profile-for-window-companies",
        "title": "Google Business Profile for Window Companies: A Checklist",
        "meta": "A field-by-field Google Business Profile checklist for window and door companies, plus the mistakes that get listings suspended and a 15-minute weekly routine.",
        "primary_kw": "google business profile for contractors",
        "secondary_kw": ["google maps ranking contractors", "window company marketing"],
        "alt_titles": [
            "The Google Business Profile Checklist Every Window Company Needs",
            "Is Your Google Business Profile Costing You Window Jobs?",
            "15 Minutes a Week: Keeping a Window Company's Google Profile Strong",
        ],
        "body": """
<p>When a homeowner searches for a window installer, your Google Business Profile is often the first thing they see. It sits above the regular results, shows your reviews and photos, and has a button that calls you.</p>
<p>Most window companies fill out the name and phone number and stop. Use this checklist to finish the job.</p>
<aside class="iws-tldr"><strong>The short version:</strong> Complete every field honestly, show real work, collect reviews steadily, and avoid the handful of mistakes that get listings suspended.</aside>

<h2>The checklist</h2>
<h3>Basics</h3>
<ul>
<li><strong>Business name:</strong> your real, legal name. Do not add keywords or city names that are not part of it.</li>
<li><strong>Address:</strong> a real location where you operate. If customers do not visit you, set the profile as a service-area business and hide the address.</li>
<li><strong>Phone:</strong> a local number that matches your website.</li>
<li><strong>Website link:</strong> point it to the page that best matches the profile, usually your homepage or a main service page.</li>
<li><strong>Hours:</strong> accurate hours, updated for holidays.</li>
</ul>
<h3>Categories and services</h3>
<ul>
<li><strong>Primary category:</strong> pick the closest match, such as "Window installation service," and confirm the exact wording in your dashboard.</li>
<li><strong>Secondary categories:</strong> add every other category that truly applies to work you do.</li>
<li><strong>Services:</strong> list each product and service you install, with a short description.</li>
</ul>
<h3>Photos and proof</h3>
<ul>
<li>Real photos of finished installs, before and after pairs, your crew, and your trucks.</li>
<li>A fresh batch each week. Recent photos tell customers you are active.</li>
<li>No stock images. They add nothing and homeowners can tell.</li>
</ul>
<h3>Reviews</h3>
<ul>
<li>Create your direct review link and use it in every follow-up text.</li>
<li>Ask within a day or two of sign-off, while the customer is happy.</li>
<li>Reply to every review within 48 hours.</li>
</ul>
<h3>Activity</h3>
<ul>
<li>Post at least twice a month: a finished job, a seasonal reminder, a short tip.</li>
<li>Keep products, services, and hours current.</li>
</ul>

<h2>Mistakes that can get a listing suspended</h2>
<ul>
<li>Stuffing keywords or cities into the business name.</li>
<li>Using a virtual office or mailbox as your address.</li>
<li>Creating several listings for the same business.</li>
<li>Offering gifts or discounts in exchange for reviews.</li>
</ul>
<p>Check Google's current guidelines before making big changes, since they update them.</p>

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
             "You choose one primary category and can add several secondary ones. Add every secondary category that truly describes work you do, and skip the rest."),
            ("Can a window company rank without a storefront?",
             "Yes. Service-area businesses can hide their street address and list the cities they serve. Your ranking still depends on reviews, profile completeness, and how well your website supports the profile."),
            ("How often should I post on my Google Business Profile?",
             "At least twice a month. A photo of a finished job with one or two sentences is enough."),
            ("Why did my Google Business Profile get suspended?",
             "Common causes include keywords in the business name, a virtual office address, duplicate listings, or incentivized reviews. Google's guidelines have the full list, and a reinstatement request with proof of your business helps."),
        ],
    },
    # ------------------------------------------------------------------ 5
    {
        "slug": "impact-window-marketing-florida",
        "title": "Impact Window Marketing in Florida: Win Before the Storm",
        "meta": "Impact window demand in Florida follows hurricane season. Build the pages, proof, and reviews that win the search before the forecast cone appears.",
        "primary_kw": "impact windows florida",
        "secondary_kw": ["impact window installation", "hurricane windows cost", "impact windows cost"],
        "alt_titles": [
            "Florida Impact Window Companies: Be Findable Before the Storm Is",
            "How Impact Window Companies Win Search Season After Season",
            "The Pages Every Florida Impact Window Company Should Already Have",
        ],
        "body": """
<p>Florida's hurricane season runs June 1 through November 30, and homeowners think about impact windows when the weather makes them think about it. Searches tend to rise when a storm is in the forecast. The companies that win those calls are the ones whose pages were live and indexed weeks earlier.</p>
<p>Semrush's US data shows what people look for: "impact windows florida" and "impact windows cost" each draw about 720 searches a month, "hurricane windows cost" about 1,000, and "impact window installation" about 720 with an average ad cost of roughly $20 per click.</p>
<aside class="iws-tldr"><strong>The short version:</strong> Publish product, cost, and city pages before you need them, show your product approvals, explain insurance and permit steps, and make it easy to book an estimate fast. Do it with care. Homeowners under stress reward calm, clear help.</aside>

<h2>1. Build the pages before the season</h2>
<p>Pages need time to be crawled, indexed, and trusted. Publishing during a storm warning is too late. Aim to have these live well before June:</p>
<ul>
<li>One page per product type you install.</li>
<li>A "what do impact windows cost" page that explains the factors, such as size, frame, glass, and permit, even if you only give ranges.</li>
<li>A page for each city or county you serve, with local jobs and permit details.</li>
<li>A page explaining your estimate and installation process from first call to final inspection.</li>
</ul>

<h2>2. Show your product approvals</h2>
<p>Miami-Dade and Broward sit in the High Velocity Hurricane Zone, which has stricter product approval rules than most of the country. Homeowners, permit offices, and inspectors all care that the product you install is approved for where it goes.</p>
<p>Put the relevant approval numbers and documents on each product page, and explain in plain English what they mean. It builds trust, and it answers a question buyers have in their head.</p>

<h2>3. Explain the insurance and permit steps</h2>
<p>Florida law requires insurers to offer discounts for qualifying wind-mitigation features, and homeowners ask about them. You do not need to quote percentages. Explain what a wind mitigation inspection is, tell homeowners to ask their insurer what applies to them, and describe how you handle permits. A clear page here earns links and calls.</p>

<h2>4. Make the next step easy</h2>
<p>A worried homeowner who finds you at 9 p.m. will not read five pages. Give them a click-to-call button, a short estimate form, and honest expectations on timing. Then answer fast. Speed to first reply wins jobs.</p>

<h2>5. Keep reviews moving all year</h2>
<p>Do not wait for storm season to ask for reviews. A steady flow of recent reviews, plus photos of real Florida installs, is what separates the map results you want from the ones you do not. The <a href="{{LINK:google-business-profile-for-window-companies}}">Google Business Profile checklist</a> covers how.</p>

<h2>A note on tone</h2>
<p>People searching during a storm are frightened. Help them understand their options and let them decide. Fear-based ads backfire and they do not build the reputation that keeps working after the season ends.</p>
<p>The general framework is in <a href="{{LINK:seo-for-window-companies}}">SEO for window companies</a>.</p>
""",
        "faq": [
            ("When should an impact window company publish its pages?",
             "Before the season, ideally by spring. Pages need time to be indexed and to earn trust, so publishing when a storm is already forecast is too late to capture that demand."),
            ("Do I need separate pages for Miami-Dade and Broward?",
             "Yes. Each county has its own permit process and local searchers, so separate pages let you show relevant details, local jobs, and approvals for each."),
            ("What should an impact window product page include?",
             "The product type and features, approval numbers and documents, warranty terms, photos of real installs, what affects price, and a clear way to request an estimate."),
            ("Should I run ads during storm season?",
             "Ads can fill demand while organic results build, but click costs rise when demand does. Track cost per signed job, and keep your organic pages and reviews working in the background."),
        ],
    },
    # ------------------------------------------------------------------ 6
    {
        "slug": "how-to-hire-seo-agency-for-window-company",
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
<p>Many window company owners have paid an agency for months and received a stack of reports and no extra calls. The fix is asking sharper questions before you sign.</p>
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
<p><strong>Good answer:</strong> A system for asking real customers after real jobs, with replies handled. <strong>Red flag:</strong> Buying reviews or offering rewards for them.</p>
<h3>6. How do you build links?</h3>
<p><strong>Good answer:</strong> Relevant local and industry sources earned through useful content and real relationships. <strong>Red flag:</strong> Bulk packages of links, or a private blog network.</p>
<h3>7. Who will actually work on my account?</h3>
<p><strong>Good answer:</strong> Named people you can speak with. <strong>Red flag:</strong> A sales rep up front and an anonymous team afterward.</p>
<h3>8. Do you know my trade and my market?</h3>
<p><strong>Good answer:</strong> They can talk about your products, approvals, seasons, and local competitors without notes. <strong>Red flag:</strong> The same pitch they gave a dentist yesterday.</p>
<h3>9. What happens if it is not working?</h3>
<p><strong>Good answer:</strong> A review point, a straight conversation, and an exit. <strong>Red flag:</strong> Excuses and a longer contract.</p>

<h2>Red flags that should end the call</h2>
<ul>
<li>Guaranteed number one rankings, or page one in days.</li>
<li>No questions about your business before quoting.</li>
<li>Pressure to sign today.</li>
<li>Refusing to show you any process or sample work.</li>
</ul>

<h2>What a good first month looks like</h2>
<p>You should see your profile fully built, tracking numbers live, a written plan for pages and cities, and the first review requests going out. Rankings come after that, not before.</p>
<p>For the full strategy behind these questions, read <a href="{{LINK:seo-for-window-companies}}">SEO for window companies</a>, and compare options in <a href="{{LINK:window-replacement-leads}}">renting versus owning window replacement leads</a>.</p>
""",
        "faq": [
            ("How much should a window company pay for SEO?",
             "Cost depends on how many cities you serve and how competitive they are. A reputable agency should review your profile, site, and competitors, then give you a scope and a price before you commit."),
            ("How long should an SEO contract be?",
             "Look for a short initial term, around 90 days, followed by month-to-month. Long lock-ins shift risk onto you."),
            ("Should I hire a niche agency or a general one?",
             "A team that understands your trade, your products, and your market will usually move faster. Ask for examples relevant to window and door companies, and confirm they can talk about approvals and seasons."),
            ("What should I own when an SEO engagement ends?",
             "Your Google Business Profile, website, domain, analytics, and any content written for you. Confirm ownership in writing before you sign."),
        ],
    },
]
