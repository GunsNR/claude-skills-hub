export type BlogCategory =
  | "local-seo"
  | "gbp"
  | "reviews"
  | "content"
  | "strategy"
  | "trade";

export const CATEGORY_LABELS: Record<BlogCategory, string> = {
  "local-seo": "Local SEO",
  gbp: "Google Business",
  reviews: "Reviews",
  content: "Content",
  strategy: "Strategy",
  trade: "Trade Guide",
};

export interface BlogPost {
  slug: string;
  title: string;
  category: BlogCategory;
  excerpt: string;
  date: string;
  readMin: number;
  body: string[];
}

export const blogPosts: BlogPost[] = [
  /* ─── Local SEO ─── */
  {
    slug: "why-roofers-lose-map-pack",
    title: "Why Roofers Lose Calls to the Map Pack Every Day",
    category: "local-seo",
    excerpt:
      "The Map Pack shows three businesses. The fourth spot doesn't exist. Here's the exact reason calls go to your competitor and not you.",
    date: "2026-05-28",
    readMin: 6,
    body: [
      "The Google Map Pack shows exactly three results — no more. If you're number four, you're invisible for most searchers. Eighty-five percent of clicks go to the top three, and the majority of those calls go to whoever holds position one. That's not speculation; that's what we see across every roofer market we track.",
      "The three factors that determine Map Pack position are proximity, prominence, and relevance. Proximity is where Google thinks the searcher is — you can't change that. Relevance comes from your GBP categories, your service pages, and the keywords on your site. Prominence is the part most contractors underestimate: it's the combination of reviews (quantity, recency, and response rate), backlinks from local sources, and your Google Business Profile completeness score.",
      "Most roofers we audit are missing the same three things: they chose only one GBP category instead of five, they haven't posted anything to their profile in six months, and their reviews dropped off after a strong start. Google treats a stalling review velocity as a negative signal. You don't need to know why — you just need to know how to fix it.",
      "The fix isn't complicated. Lock down your GBP with all relevant categories, upload 15–20 real jobsite photos, build a consistent review-ask system into your post-job process, and create dedicated pages on your site for every service area zip code you want to rank in. Do those four things and you'll be inside the Map Pack within 60–90 days in most markets.",
    ],
  },
  {
    slug: "rank-google-maps-hvac",
    title: "How to Rank Your HVAC Business in Google Maps (2026 Guide)",
    category: "local-seo",
    excerpt:
      "Google Maps rankings aren't random. This is the exact playbook we use to move HVAC companies from invisible to top-3 in under 90 days.",
    date: "2026-05-12",
    readMin: 8,
    body: [
      "HVAC is one of the most competitive local verticals on Google Maps. Homeowners searching 'AC repair near me' at 11pm in July are ready to book immediately — and they're calling whoever shows up first. That urgency is exactly why the Map Pack is so valuable for HVAC companies, and why every serious operator needs to understand how to rank in it.",
      "Start with your Google Business Profile. Set your primary category to 'HVAC Contractor' and add every applicable secondary category: 'Air Conditioning Repair Service,' 'Heating Contractor,' 'Furnace Repair Service.' Incomplete category selection is the single most common mistake we see on HVAC profiles. Google can't show you for searches you haven't told it you're relevant for.",
      "Your service area matters more than most people realize. GBP allows you to set up to 20 service area cities. Most HVAC companies we audit have two or three. Fill all 20 with the actual towns, zip codes, and communities you serve. Cross-reference this with the city pages on your website — every service area you list in GBP should have a corresponding page on your site.",
      "Reviews are the fuel. HVAC businesses that consistently add 5–10 new reviews per month outrank competitors with 200+ older reviews that stopped accumulating. Google weighs recency heavily. Build a review ask into every completed job: text the customer a direct link to your review page within 24 hours of the job closeout while the experience is still fresh.",
    ],
  },
  {
    slug: "local-pack-explained",
    title: "What the Local Pack Actually Is — and How to Get In It",
    category: "local-seo",
    excerpt:
      "The three-pack controls the majority of local clicks. Here's exactly how it works and the specific levers that move your position.",
    date: "2026-04-20",
    readMin: 5,
    body: [
      "When someone searches 'roofer near me' or 'HVAC repair Hollywood FL,' Google shows a map with three businesses highlighted. That's the Local Pack — sometimes called the Map Pack or three-pack. It's the most valuable real estate on any local search results page, and it's separate from the organic blue links below it.",
      "The Local Pack is driven by Google Maps data, which means it's your Google Business Profile — not just your website — that determines whether you appear. A business with a great website but a neglected GBP will lose to a competitor with a simpler site but a fully optimized profile. This surprises contractors who spent $5,000 on a website and still can't get calls.",
      "Three factors move the needle: proximity (how close the business is to the searcher), relevance (how well your profile and website match the search query), and prominence (how trusted and well-known Google believes you are in your market). You can't control proximity, but you have full control over relevance and prominence.",
      "To build prominence, you need consistent NAP citations across the web (same name, address, and phone number on every directory), a steady flow of recent reviews, links from local news and community websites, and regular activity on your GBP itself. Google treats an inactive profile as a signal that the business may not be operating. Post at least twice a month, even if it's just a photo of a completed job.",
    ],
  },
  {
    slug: "pool-seo-zip-code",
    title: "Pool Service SEO: How to Dominate Your Zip Code This Season",
    category: "local-seo",
    excerpt:
      "Pool service is hyper-local. One zip code, one season, one dominant company. Here's how to make sure that's you before your competition figures it out.",
    date: "2026-04-05",
    readMin: 7,
    body: [
      "Pool service is one of the few home service trades where geography is everything. A homeowner in Weston, FL isn't calling a pool company in Coral Springs unless they have no other option. The customer base is literally limited to the neighborhoods within a 10–15 mile radius of your shop. That means winning your specific zip code is more valuable — and more achievable — than trying to rank across a metro.",
      "Start with the Google Business Profile for your primary service area. Your GBP address should be your actual location, but your service area should include every zip code and neighborhood name where you actively take customers. Be specific: don't just put 'Weston' — add 'Weston Hills,' 'The Ridges,' 'Sector 7' and other specific neighborhood names that residents use to describe where they live.",
      "Pool season has a clear search spike pattern. In South Florida, search volume for 'pool cleaning service' and 'pool maintenance near me' climbs from February through May and peaks in June. You need to have built your rankings before the spike — not during it. SEO takes 60–90 days to fully land. If you're reading this in April, you need to start now to capture peak summer volume.",
      "Service pages convert better than generic home pages. Create a dedicated page for each service: weekly pool maintenance, pool opening, pool closing, equipment repair, salt system conversion, green pool rescue. Each page should include the service areas you serve, real photos of your team doing that service, and a clear call to action. These pages rank individually and each one represents a different search intent — someone searching 'green pool rescue' is in a different buying moment than someone searching 'weekly pool maintenance.'",
    ],
  },
  {
    slug: "local-seo-vs-national",
    title: "Local SEO vs. National SEO: Why the Strategy Is Completely Different",
    category: "local-seo",
    excerpt:
      "An e-commerce brand and a roofing company need completely different SEO strategies. Using the wrong one is why most contractors get zero results.",
    date: "2026-03-18",
    readMin: 6,
    body: [
      "Most of what's written about SEO online is about national or e-commerce SEO — link building at scale, domain authority scores, massive content operations. None of that is how you win local search. Local SEO has its own distinct signals and strategies, and applying national SEO thinking to a local contracting business is like bringing a suitcase to a swim meet.",
      "The biggest difference is the role of the Google Business Profile. For national SEO, there's no GBP — it doesn't exist. For local search, the GBP is equal to or more important than your website. A business with a great GBP and a mediocre website will consistently outrank a business with a great website and a neglected GBP in local results.",
      "Citation consistency is another local-only factor. For national SEO, the exact same business name and address across directories is irrelevant. For local SEO, mismatches in your NAP data (name, address, phone) are a trust signal to Google that your listing might be outdated or inaccurate. We've seen businesses rank significantly better within weeks just from cleaning up inconsistent citations across Yelp, YellowPages, Angi, and other directories.",
      "Content strategy is also fundamentally different. National SEO wins by creating content that ranks for high-volume informational queries. Local SEO wins by creating city and service pages that match exactly what your customers search within your geographic area. That means 'roofing contractor Hollywood FL' beats a 3,000-word blog post about roof types — every time.",
    ],
  },
  {
    slug: "google-maps-vs-organic",
    title: "Google Maps vs. Organic Rankings: Which One Drives More Calls?",
    category: "local-seo",
    excerpt:
      "Contractors debate this constantly. Here's the data from a hundred accounts: the answer isn't what most people expect.",
    date: "2026-02-28",
    readMin: 5,
    body: [
      "The short answer: Google Maps drives more calls, but organic rankings drive higher-intent conversions. The longer answer requires understanding the difference in searcher behavior at each placement. Map Pack clicks are exploratory — the searcher sees three options and often compares all three. Organic ranking clicks are often destination clicks — the searcher has gone past the Map Pack and specifically chosen to dig deeper.",
      "For emergency-intent searches — 'emergency roofer near me,' 'AC repair open now,' 'burst pipe plumber' — the Map Pack dominates. Searchers in a crisis click the first thing that looks available. They want a phone number, they want it fast, and they're not comparison shopping. Being in the Map Pack for emergency queries is worth more than anything else in local SEO.",
      "For research-intent searches — 'how much does a new roof cost,' 'what HVAC brand is most reliable,' 'how long does a water heater last' — organic rankings matter more. These searchers aren't ready to call yet. They're gathering information. A blog post that answers their question establishes you as the trusted expert before they're ready to buy.",
      "The practical takeaway: don't choose. Map Pack and organic rankings are complementary, not competing. Build your GBP and reviews system to own the Map Pack for high-intent queries, and create service and city pages on your website to rank organically for the full range of searches in your market. The businesses that win long-term show up in both placements.",
    ],
  },

  /* ─── Google Business Profile ─── */
  {
    slug: "google-business-profile-checklist",
    title: "The Only Google Business Profile Checklist Contractors Need",
    category: "gbp",
    excerpt:
      "Twenty-two GBP fields. Most contractors have filled out four. Here's every one that matters — and what filling them out actually does to your ranking.",
    date: "2026-05-20",
    readMin: 9,
    body: [
      "The Google Business Profile has 22 fields that affect visibility. The average contractor we audit has filled out five. Every unfilled field is a missed opportunity to tell Google exactly what you do and who you serve — and to show up for searches your competitor doesn't. This isn't complicated, but it requires actually sitting down and completing the work.",
      "Start with business name (use your real legal name, no keyword stuffing), primary category (be specific — 'Roofing Contractor' not just 'Contractor'), secondary categories (add every applicable one — most contractors leave all of these blank), business description (tell Google and customers what you do, what areas you serve, what makes you different — it's indexed by Google), and services (list every single service you offer, including seasonal ones).",
      "Photos are consistently underestimated. Google has confirmed that profiles with photos receive more clicks and direction requests than those without. Upload at least 20 real photos: your team at work, finished projects, your vehicle, your storefront or office, and at minimum 5–10 before-and-after jobsite shots. Do not use stock photos. Google can identify stock imagery and it provides no trust signal.",
      "Posts are the most neglected feature on GBP. Google Business Posts expire after 7 days but they signal to Google that your business is active and engaged. Post at least twice a week: new projects, seasonal promotions, answers to common questions, tips for homeowners. It's 10 minutes of work that most of your competitors don't bother doing — which means doing it is a competitive advantage.",
    ],
  },
  {
    slug: "gbp-photos-guide",
    title: "GBP Photos: The 15 Images That Actually Improve Your Rankings",
    category: "gbp",
    excerpt:
      "Not all photos are equal. These are the specific 15 photo types that Google rewards — and why random job photos aren't enough.",
    date: "2026-04-28",
    readMin: 6,
    body: [
      "Google has confirmed in their own documentation that photos on a Google Business Profile improve click-through rates from search results. What they haven't told you is that the type, quality, and diversity of photos matters as much as quantity. Uploading 50 blurry photos of finished roofs won't move the needle. Uploading 15 specific, high-quality photos in the right categories will.",
      "The 15 photo categories that matter: (1) team at work — action shots of your crew doing the job, (2) before and after pairs — Google surfaces these in comparison searches, (3) your vehicle or fleet with branding visible, (4) your storefront or office, (5) equipment close-ups, (6) your logo in high resolution, (7) cover photo — the first image customers see in Maps (make it count), (8) project overview — wide shots of finished work, (9) local landmarks in the background if possible (helps geographic relevance), (10) crew portraits.",
      "Quality matters. Photos taken on a modern smartphone are acceptable if the lighting is good. Don't upload blurry, underlit, or heavily filtered photos. Google's algorithm evaluates photo quality as a signal of business professionalism. Bright, sharp, natural-light photos outperform dark interior shots every time.",
      "Recency is a ranking factor that almost no contractor tracks. Google weights recent photos more heavily than older ones. Build a habit of uploading one or two new jobsite photos every week. Over a year, that's 52–100 photos showing consistent, active work — a signal Google reads as a thriving, trustworthy business.",
    ],
  },
  {
    slug: "gbp-posts-strategy",
    title: "How to Use Google Business Posts Without Wasting Your Time",
    category: "gbp",
    excerpt:
      "GBP Posts take 5 minutes. Most contractors skip them. The ones who don't are quietly picking up clicks and calls their competitors are missing.",
    date: "2026-03-30",
    readMin: 5,
    body: [
      "Google Business Posts are short updates — similar to a social media post — that appear directly in your Google Business Profile listing in Maps and Search. They expire after 7 days (events post stay up for their duration), they're indexed by Google, and they signal active business engagement. Most contractors have posted exactly once since they created their GBP and then forgot posts exist.",
      "What to post: completed projects (photo + 2-3 sentences about the job and location), seasonal promotions, answers to common customer questions, tips for homeowners in your trade, reminders about your service area. The best-performing posts include a photo, a short description, and a call-to-action button (Book, Call Now, Learn More).",
      "Post frequency recommendation: twice per week minimum. Yes, that's more than most businesses do — and that's exactly why doing it is a competitive advantage. Set a calendar reminder. On Monday post a completed job from the previous week. On Thursday post a tip or FAQ answer. The whole process takes under 10 minutes.",
      "Don't overthink the content. A photo of a completed roofing job with the caption 'Just wrapped up a full replacement in [city name]. If your roof is 15+ years old, this summer is the time to have it inspected.' is a perfect post. It's local, it's relevant, it shows active work, and it has a clear seasonal call to action. That's all you need.",
    ],
  },
  {
    slug: "gbp-suspension-prevention",
    title: "Why Google Suspends Business Profiles and How to Prevent It",
    category: "gbp",
    excerpt:
      "A suspended GBP means invisible on Maps — instantly. These are the exact things that trigger suspensions and how to make sure you never get hit.",
    date: "2026-02-15",
    readMin: 7,
    body: [
      "Google suspends Google Business Profiles for violations of their guidelines — and a suspension means your profile disappears from Maps and Search immediately. For a contractor who gets 70% of their calls from Google, a suspension is catastrophic. The reinstatement process can take weeks. Prevention is worth more than any amount of reactive damage control.",
      "The most common suspension triggers: keyword stuffing in your business name (adding 'Top Rated' or 'Best in Miami' to your name when those words aren't part of your actual legal business name), using a PO Box or virtual office address instead of your real location, having multiple profiles for the same location, using a toll-free number instead of a local one, or having a sudden spike in reviews that looks unnatural.",
      "What you should do proactively: use your exact legal business name with no additions, use only a real physical address (home address is allowed for service-area businesses that hide their address), claim your profile using a real Google account that's been active for at least 6 months, build reviews gradually rather than asking your entire customer list at once, and never offer incentives for reviews.",
      "If you do get suspended, don't panic but act quickly. Log into your GBP dashboard, look for a notification about why the profile was suspended, fix the stated issue, and submit a reinstatement request through the GBP support page. Include documentation: utility bills showing your business address, photos of your business location or vehicle with branding, your business license. Detailed documentation gets faster reinstatements.",
    ],
  },

  /* ─── Reviews ─── */
  {
    slug: "get-100-google-reviews",
    title: "How to Get 100 Google Reviews Without Begging",
    category: "reviews",
    excerpt:
      "100 reviews in a year is realistic for any contractor doing 3 or more jobs a week. Here's the exact system that doesn't feel like begging.",
    date: "2026-05-05",
    readMin: 7,
    body: [
      "A hundred Google reviews in a year means getting a review from roughly 1 in 12 customers if you're doing 25 jobs per month. That's not an ambitious goal — it's a conservative one. But most contractors are getting zero to two reviews per month because they're leaving the ask to chance. Reviews don't happen organically at scale; they happen when you build a system.",
      "The system has three parts: timing, frictionlessness, and a direct link. Timing: ask within 24 hours of job completion while the customer is still emotionally satisfied. Don't wait until you invoice — that's when the relationship becomes transactional. Frictionlessness: send a text message with a direct link to your Google review page. Don't send them to a website, don't ask them to find you on Google, don't email them. A text with a one-tap link removes every barrier.",
      "The message: 'Hi [Name], it was great working on your [service] today. If you had a good experience, we'd love a Google review — it takes about 2 minutes and really helps our small business. Here's a direct link: [link]. No pressure, and thanks for trusting us with your home.' That's it. That message, sent within 24 hours, converts at 20–30% in our experience across hundreds of clients.",
      "One warning: don't batch ask. If you text 50 customers in one day asking for reviews and 20 of them leave reviews in 48 hours, Google flags it as unnatural and may suppress or remove those reviews. Spread the asks organically with your job flow. Five reviews a week from real customers beats 50 reviews in a spike — both because it looks natural and because recency keeps signaling to Google that you're actively working.",
    ],
  },
  {
    slug: "review-velocity-system",
    title: "The Review Velocity System That Pushed Wayne's Roofing to #1",
    category: "reviews",
    excerpt:
      "Wayne's went from almost no reviews to 331+ five-star reviews and #1 in Ocean County. The system is simpler than you think.",
    date: "2026-04-14",
    readMin: 6,
    body: [
      "When Wayne's Roofing came to us, they had a handful of reviews and an online footprint that didn't reflect the quality of their work at all. Two years later, they're the #1 rated roofing company in Ocean County, NJ, with 331+ five-star Google reviews. The system we built is replicable for any contractor doing consistent volume. Here's exactly what we did.",
      "Step one was fixing the basics: getting them a direct review link, setting up a professional text template, and training their crew to mention the review ask verbally at job close before the office sent the text. The verbal mention ('Hey, you'll get a text from the office — if everything went well today, we'd really appreciate a review') primes the customer so the text doesn't feel cold.",
      "Step two was review velocity management. We tracked review count weekly and flagged any week with zero new reviews so the team could follow up with recent customers who hadn't responded. Gaps in review activity are a negative signal on Google. Consistent, weekly new reviews signal an active, working business.",
      "Step three was review responses. Wayne responds personally to every review within 48 hours — positive or negative. For negative reviews (rare, but they happen), the response is always professional, empathetic, and offers to resolve offline. Google notices response patterns and rewards engagement. Customers reading reviews also notice — a business that responds to every review appears more trustworthy than one with 300 reviews and zero responses.",
    ],
  },
  {
    slug: "competitor-review-attacks",
    title: "What Happens When a Competitor Attacks Your Google Reviews",
    category: "reviews",
    excerpt:
      "Fake negative reviews are a real and growing problem for contractors. Here's how to identify them, report them, and protect your rating.",
    date: "2026-03-22",
    readMin: 6,
    body: [
      "Fake negative reviews — one or two stars left by people who were never your customers — are more common in competitive contracting markets than most owners realize. When your competitor sees you climbing in the rankings, some of them will try to drag you down. Google has systems to detect this, but they're not perfect. You need to know how to fight back.",
      "How to identify a fake review: the reviewer has never interacted with your business (no matching job record, no recognizable name), the reviewer's Google account is new or has only ever left reviews for your direct competitors, the review has no specific details about the job or the crew (a real customer would mention something specific), or multiple negative reviews arrive within a short window.",
      "How to report: on the Google Business Profile dashboard, click the flagged review and choose 'Report review.' Select the most accurate reason — 'not a customer,' 'conflict of interest,' or 'off-topic.' If you have multiple suspicious reviews, use the Google Business Profile Community forum to escalate to a human reviewer. Document your case: screenshots of the reviews, timestamps, records of your actual customer list showing no match.",
      "How to protect yourself long-term: high review volume is the best defense. A competitor dropping two fake 1-star reviews on a profile with 250 reviews barely moves the needle. A competitor dropping two fake reviews on a profile with 12 reviews is devastating. Building volume isn't just about ranking — it's about resilience. Keep adding real reviews consistently and you make yourself attack-proof.",
    ],
  },
  {
    slug: "review-response-templates",
    title: "How to Respond to Every Google Review (Templates for Contractors)",
    category: "reviews",
    excerpt:
      "Most contractors either don't respond or write one-line responses that waste the opportunity. These templates are what actually works — for five-star and one-star reviews alike.",
    date: "2026-02-10",
    readMin: 5,
    body: [
      "Responding to Google reviews does two things: it signals to Google that you're an engaged, active business (which helps rankings), and it shows potential customers reading those reviews that you care about every customer experience. Most contractors either never respond or post the same generic 'Thanks for the review!' on every one. Neither approach is wrong — but neither one is leaving money on the table.",
      "For five-star reviews: personalize. Mention a specific detail from the review. 'Thanks so much, Karen — really happy the new shingle system came out exactly as we discussed. The team worked hard on that pitch and it shows. Looking forward to the inspection next spring!' A personal response turns a review into a genuine testimonial that anyone reading it can trust.",
      "For four-star reviews: acknowledge what they mentioned and offer follow-up. 'Appreciate the review, Mike — we're glad the installation went smoothly. If there was anything that didn't meet expectations, feel free to call us directly and we'll make it right.' This often prompts customers to update their review to five stars when they see you care.",
      "For negative reviews: stay professional, never get defensive, and take the conversation offline. 'We're sorry your experience didn't go as expected, [Name]. We take this seriously. Please call us directly at [phone] so we can understand what happened and make it right.' Never argue with the specifics of a negative review publicly. Even if the review is factually wrong, potential customers reading your response will judge your professionalism, not the accuracy of the original complaint.",
    ],
  },

  /* ─── Content ─── */
  {
    slug: "city-pages-vs-service-pages",
    title: "City Pages vs. Service Pages: What Actually Ranks Locally",
    category: "content",
    excerpt:
      "Most contractors build one or the other. The ones who dominate build both — and here's exactly how they do it without duplicate content penalties.",
    date: "2026-05-15",
    readMin: 7,
    body: [
      "City pages and service pages serve different ranking purposes and target different search queries. A service page for 'emergency roof repair' targets everyone searching that term regardless of location. A city page for 'roofing contractor Boca Raton' targets people searching specifically in that city. The contractors who rank everywhere build a matrix — every service page crossed with every service city.",
      "Service pages need to be comprehensive. They should cover what the service is, how you do it, what it costs (ranges are fine if exact pricing varies), how long it takes, what the customer needs to do before and after, warranties, and why your approach is better than competitors. A service page with 200 words of copy will not rank. A service page with 800–1200 words of genuinely useful information will.",
      "City pages need to feel local, not copy-pasted. The most common city page mistake is creating 15 pages that are identical except for the city name swapped out. Google knows. Instead, include actual local details: nearby landmarks ('we serve homeowners from the Las Olas area down to Hallandale Beach'), local weather patterns that affect your trade ('South Florida's daily afternoon storms mean even a small roof leak becomes a major problem fast'), local permit information, or customer references to specific local events.",
      "The matrix approach: if you offer 8 services and want to rank in 12 cities, that's 96 pages. That sounds overwhelming until you build a template that handles the structure and you customize the local details for each. Over 12–18 months, a well-built service-city matrix is the single most powerful organic ranking asset a local contractor can build.",
    ],
  },
  {
    slug: "seo-content-contractors",
    title: "How to Write SEO Content That Ranks AND Converts",
    category: "content",
    excerpt:
      "Content that ranks but doesn't convert is a waste of your time. Here's how to write content that does both — without sounding like a robot wrote it.",
    date: "2026-04-10",
    readMin: 8,
    body: [
      "There's a trap that most contractors fall into when they start taking content seriously: they optimize for robots and forget about humans. The page ranks because it has the right keywords, but nobody calls because the copy reads like it was generated by software and edited by nobody. Good SEO content ranks and converts. The two goals are not at odds — they're achieved with the same approach.",
      "Write for one specific person. Not 'homeowners,' not 'potential customers.' A specific person: a 47-year-old homeowner in Pembroke Pines who just noticed water stains on his ceiling after last night's storm and is stressed about what it's going to cost. Write every sentence as if you're talking directly to that person. That specificity is what makes content resonate — and it's also what Google's helpful content algorithms are trying to measure.",
      "Answer the question first. Every piece of local service content starts with a question the customer is actually asking. Lead with the answer. Don't make them read three paragraphs of background before getting to the information they need. 'How much does a roof replacement cost in Miami? Most homeowners pay between $8,000 and $18,000 depending on roof size, material, and pitch.' That's your opening. Then explain the variables. Then tell them how to know where they fall in that range.",
      "Include specific local details. Prices that reflect your actual market. Permit process specific to your county. Common local issues — 'in South Florida, flat roofs are common but they require specific waterproofing systems that aren't used in most of the country.' Content with specific, accurate local details signals both to Google and to customers that this was written by someone who actually does this work in this area.",
    ],
  },
  {
    slug: "five-page-website",
    title: "The 5-Page Website Formula That Generates Most of Our Clients' Calls",
    category: "content",
    excerpt:
      "Before you build 100 pages, build 5 pages that actually convert. This is the foundation every contractor site needs before anything else.",
    date: "2026-03-08",
    readMin: 6,
    body: [
      "There's a common misconception that a contractor website needs to be big to work. The most effective sites we've built start with five pages and generate most of the client's calls before we add anything else. Building more content on top of a weak foundation doesn't work. Getting the foundation right first is what the industry gets wrong.",
      "Page 1 — Homepage: your value proposition, your primary service area, social proof (reviews count, logos, short testimonials), a clear primary call to action (call or request an audit), and a brief explanation of what you do. No fluff, no stock photography of people shaking hands. Visitors decide in 4 seconds whether to stay or leave. Make the first 400 pixels of your homepage answer 'what do you do and why should I trust you.'",
      "Pages 2–4 — Core Service Pages: one page per primary service you want to rank for. Each page should be 800–1200 words, include real job photos, explain the service process, mention pricing ranges, and have a clear call to action. These are your ranking workhorses — they're what will get you to page one for high-intent searches.",
      "Page 5 — Contact/Audit Page: a simple form with minimal fields (name, phone, address, service needed, brief message), your phone number prominent at the top, your service area listed, and trust signals (licenses, insurance, years in business). Make it easy. Every additional form field reduces conversion rate by 10–15%. Three to four fields is the maximum.",
    ],
  },
  {
    slug: "blogging-wont-save-you",
    title: "Why Blogging Won't Save Your Local SEO (And What Will)",
    category: "content",
    excerpt:
      "A hundred blog posts won't move your rankings if the foundation is broken. Here's where the leverage actually is for home service contractors.",
    date: "2026-02-22",
    readMin: 5,
    body: [
      "The SEO advice most contractors get sounds like this: 'You need to blog consistently. Post twice a week. Content is king.' This advice is not wrong for national SEO or e-commerce. For a local contractor competing for calls in a specific metro, blogging is probably the tenth most important thing you should be doing — not the first.",
      "Here's the honest priority list. First: fix your Google Business Profile (categories, photos, completeness, service area). Second: build a review velocity system. Third: correct your NAP citations across directories. Fourth: create or fix your core service pages with real copy and real photos. Fifth: build city pages for every market you want to rank in. Sixth through tenth: technical SEO, page speed, schema markup, internal linking, backlinks from local sources. Blogging comes after all of that.",
      "Blogging does work — but only if the foundation is solid. A blog post about 'how to know if you need a new roof' will rank and convert if your site already has domain authority from citations and backlinks, if your GBP is fully optimized and you're getting regular reviews, and if your core service pages are already performing. Without that foundation, your blog posts go nowhere.",
      "The contractors who misuse blogging are the ones who use it to avoid doing the harder structural work. Writing a blog post is creative and feels productive. Auditing 40 directory listings for NAP consistency is tedious. One of those activities moves the needle far more than the other in the first six months. Do the structural work first. Then blog.",
    ],
  },

  /* ─── Strategy ─── */
  {
    slug: "homeadvisor-vs-seo",
    title: "The True Cost of HomeAdvisor Leads vs. Organic SEO",
    category: "strategy",
    excerpt:
      "Running the real math on shared leads vs. owned pipeline. Most contractors are shocked by how the numbers actually compare.",
    date: "2026-05-22",
    readMin: 7,
    body: [
      "HomeAdvisor, Angi, and Thumbtack charge between $15 and $120 per lead depending on the trade and market. Those leads are sold to three to five contractors simultaneously. You're not getting an exclusive lead — you're getting a race. The customer gets called by all three to five contractors within minutes, and whoever answers first and quotes best wins. Most contractors don't win most of those races.",
      "Run the real math. If a lead costs $50 and you close 20% of the leads you buy, your cost per acquired job is $250 in lead spend alone — before your time, fuel, and follow-up cost. A decent-sized roofing job at $10,000 makes that math work. An HVAC tune-up at $150 doesn't. And next month, you're back buying the same leads from the same platform at the same price. You own nothing.",
      "Organic SEO has a different cost structure. The investment is front-loaded: 90–120 days before you see meaningful results, and a monthly retainer to maintain and grow rankings. But the leads that come from Google organic rankings and your Map Pack are exclusively yours. Nobody else is bidding on your spot in Maps or on your website's organic listing. Every call from those placements costs you nothing incremental after the SEO investment.",
      "By month 18, the math almost always flips dramatically in favor of organic SEO. A contractor spending $1,500/month on SEO and $3,000/month on HomeAdvisor leads will typically get more owned, exclusive, higher-quality leads from the SEO than from the paid platform — and the SEO compound in value over time while the paid platform delivers nothing the moment you stop paying.",
    ],
  },
  {
    slug: "90-day-seo-timeline",
    title: "90-Day SEO Timeline: What Actually Happens Month by Month",
    category: "strategy",
    excerpt:
      "SEO results don't happen overnight — but they don't take forever either. Here's the honest, month-by-month breakdown of what to expect.",
    date: "2026-04-02",
    readMin: 6,
    body: [
      "The most common question we get from new clients is 'how long will this take?' The honest answer is 90 days before meaningful, trackable results, and 6–12 months before you're dominating your market. Anyone promising results in 30 days is either lying or optimizing for a metric that doesn't translate to calls. Here's what actually happens month by month.",
      "Month 1: technical and foundational work. Google Business Profile optimization, citation audit and cleanup, technical website fixes (page speed, mobile optimization, schema markup), keyword research, and mapping out the content structure. You probably won't see ranking movement yet. This is the pre-game — it's essential and it's invisible.",
      "Month 2: content build-out and early signals. Service pages published or overhauled, city pages going live, link outreach beginning, review velocity system launched and running. You'll start seeing GBP metrics improve: more profile views, more direction requests, more clicks. Organic rankings may start to move for lower-competition keywords.",
      "Month 3: consolidation and early wins. By the end of month 3, clients consistently report increased phone volume from Google. Map Pack appearances for target keywords typically stabilize in top-5 during this month. The review count should be visibly climbing. This is when the work starts paying in calls — not because we flipped a switch, but because the foundation has been solid for 90 days and Google's trust in the profile and website has accumulated.",
    ],
  },
  {
    slug: "fire-seo-agency",
    title: "How to Fire Your SEO Agency Without Getting Burned",
    category: "strategy",
    excerpt:
      "You own your website. You own your GBP. But do you actually have access? How to exit cleanly and make sure your rankings survive the transition.",
    date: "2026-03-15",
    readMin: 6,
    body: [
      "The second most common thing we hear from new clients after 'my old agency didn't deliver results' is 'my old agency won't give me my own website.' It happens more often than you'd think. Agencies that use proprietary platforms or own the domain registration hold all the leverage when you want to leave. Before you sign with any SEO provider, ask: who owns the domain, who owns the hosting account, and who has access to the Google Analytics and Search Console properties.",
      "Before you cancel, take inventory of everything you own and everything you need. List every account: Google Analytics, Google Search Console, Google Business Profile, all social accounts, your domain registrar, your hosting account, and your website CMS. For each one, confirm that you (not the agency) are the primary owner. If the agency is the primary owner on anything, get that changed before you give notice.",
      "When you do cancel, do it in writing. Specify a transition date and request a full handoff: all login credentials, access to any content or design files they've created, any active campaign data, and written documentation of the work they've done. Agencies are legally obligated to hand over assets you've paid for. Having your termination request in writing protects you if they're difficult.",
      "For rankings: expect a slight dip for 30–60 days after agency transition, even with a smooth handoff. This is normal — it reflects the gap in activity, not damage. The rankings that were built on legitimate work (real content, real citations, real reviews) will recover quickly once the new team is active. Rankings built on shortcuts or thin content may not recover and that's a sign the previous work wasn't solid to begin with.",
    ],
  },
  {
    slug: "exclusivity-model",
    title: "Why We Only Take One Contractor Per Trade Per City",
    category: "strategy",
    excerpt:
      "Every other SEO agency will take your competitor tomorrow. Here's why we don't — and why that's the only model that makes sense for contractors.",
    date: "2026-02-05",
    readMin: 5,
    body: [
      "Every SEO agency you call will give you a pitch about their proprietary process, their proven results, their certified team. Then you'll ask whether they're working with any of your competitors in your city and they'll hesitate. Because most of them are. Or will be as soon as someone writes a bigger check. We don't operate that way, and here's why the exclusivity model is the only model that actually serves contractors.",
      "The conflict of interest in multi-client models is fundamental. If an agency is doing SEO for you and your main competitor in the same city, they can't be maximally aggressive on your behalf. The tactic that pushes you to number one pushes them down. They're managing a portfolio of clients in the same market, not fighting for one of them to win. They're selling the illusion of exclusive service while doing commodity work for everyone.",
      "The way we think about it: when a Miami roofer pays us to get them to the top of Google, we're working for that contractor and against their competition. Full stop. That's what the client is paying for. If we also work for a competing Miami roofer, then we're taking money from two parties who have directly opposing interests. We'd either do mediocre work for both or sabotage one to benefit the other. Neither is acceptable.",
      "The business consequence for you: lock in your market before your competitor does. Once we have a roofer in Miami, we turn down every other Miami roofing inquiry permanently. The exclusivity is the product. If you're in a market we don't serve yet, that window is open — but it closes when your competitor calls us first.",
    ],
  },

  /* ─── Trade Guides ─── */
  {
    slug: "seo-for-roofers-guide",
    title: "SEO for Roofers: The Complete 2026 Field Guide",
    category: "trade",
    excerpt:
      "Everything a roofing contractor needs to know about local SEO — from the first Google Business Profile setup to dominating an entire county.",
    date: "2026-05-30",
    readMin: 12,
    body: [
      "Roofing is one of the highest-value local service verticals — average job tickets over $10,000, high competition, and customers who make decisions based almost entirely on what they find in the first 30 seconds of a Google search. That combination makes roofing SEO both high-stakes and high-reward. Here's everything you need to know to build an unfair competitive advantage online.",
      "Your Google Business Profile is the starting point. Set your primary category to 'Roofing Contractor.' Add secondary categories: 'Roof Repair Service,' 'Gutter Cleaning Service,' 'Skylight Installation Service.' Upload at least 25 photos including before-and-after sets, crew at work, close-ups of materials, and finished projects. Set your service area to every city, town, and community you actually serve — not just your home market. Post at least twice a week.",
      "Reviews are the ranking currency for roofing more than almost any other trade, because the job size creates more memorable experiences and the 'roofing scam' perception means customers research reviews more carefully than they would for a plumber fixing a leaky faucet. Build your review ask system: text customers within 24 hours of job completion, a direct link to your Google review page, a short personal message from a named person on your team. Track weekly. Respond to everything.",
      "For your website, roofing SEO requires both service pages and geography pages. Create a service page for every type of roofing you do: shingle replacement, flat roof installation, TPO roofing, metal roofing, tile roofing, emergency tarping, storm damage assessment. Create a city page for every market within your drive radius. Each page should be 800+ words with real photos and specific local detail. The combination of service pages and city pages creates the matrix that lets you rank for hundreds of specific local queries.",
    ],
  },
  {
    slug: "hvac-seo-guide",
    title: "HVAC SEO: Get Found When the AC Breaks at 11pm",
    category: "trade",
    excerpt:
      "The searcher who types 'AC repair near me' at 11pm is calling the first company they see. Here's how to make sure that company is yours.",
    date: "2026-04-25",
    readMin: 10,
    body: [
      "HVAC is a perfect SEO trade because the purchase intent is so clear. Someone searching 'AC repair near me' in July isn't browsing — they're in their house, they're hot, and they're ready to pay whoever answers. The challenge is getting your business to the top of that search before your competitor does. In competitive South Florida and NJ markets, this requires deliberate, consistent SEO work — but the payoff is enormous.",
      "Emergency search terms are your most valuable ranking targets. 'AC not working,' 'furnace not heating,' 'HVAC emergency,' 'AC repair open now' — these have massive conversion value because they're last-resort searches. Build dedicated pages for emergency HVAC services that are clear and fast-loading. Prominently display your phone number and whether you offer 24/7 service. An emergency page without 'available now' or 'same-day service' near the top is leaving conversions on the table.",
      "Seasonality is the HVAC competitive dynamic that most companies don't manage proactively. AC-related searches spike in April–May in Florida as temperatures rise and homeowners realize their equipment hasn't run since October. Heating searches spike in November–December in the Northeast. Your SEO work needs to be active 90 days before the season — not during it. Rankings take time to build. The companies that own summer searches in May started building those rankings in February.",
      "For Google Business Profile, HVAC-specific categories matter: 'Air Conditioning Repair Service,' 'Air Conditioning Contractor,' 'Heating Contractor,' 'HVAC Contractor.' Add all that apply. Your business description should include the brands you service (Carrier, Trane, Lennox, Rheem, etc.) because some customers search by brand and GBP keyword matching on descriptions is real.",
    ],
  },
  {
    slug: "plumber-seo-guide",
    title: "Plumber SEO: Why Emergency Searches Are Your Golden Ticket",
    category: "trade",
    excerpt:
      "Plumbing emergencies produce the highest-value, lowest-comparison searches in all of home services. Here's how to own them in your market.",
    date: "2026-04-08",
    readMin: 9,
    body: [
      "A burst pipe, a backed-up sewer, a water heater failure — these are plumbing emergencies where the customer is not comparison shopping. They search, they see who's available, they call. The research stage is compressed into seconds. That makes emergency plumbing searches the single most valuable search queries in local services: high intent, low comparison, ready to pay.",
      "Start with your emergency-specific GBP optimization. Set your hours accurately — if you offer 24/7 emergency service, that should be reflected in your GBP hours. Set up messaging if available in your market (Google Messages allows customers to message you directly through your GBP listing). Make sure your phone number is a local number, not a toll-free or tracking number that isn't associated with your area code.",
      "Emergency service pages are a separate category from standard service pages. Create a standalone page for emergency plumbing services with a clear headline, your emergency phone number in the first paragraph, a list of emergencies you respond to, your average response time, and your service area. Keep this page simple, fast-loading, and mobile-optimized. Someone on their phone with water coming through the ceiling doesn't need a beautiful website — they need a phone number and confidence you're available.",
      "Standard service pages matter too. Water heater installation and repair is a high-ticket service with moderate urgency. Drain cleaning is high-frequency with regular repeat customers. Whole-home repiping is a large project with longer consideration. Each service category represents a different customer psychology and requires a different content approach — but all of them need pages that rank in your local market.",
    ],
  },
  {
    slug: "restoration-seo-guide",
    title: "Restoration SEO: How to Rank for Water Damage in 72 Hours",
    category: "trade",
    excerpt:
      "Restoration is the most time-sensitive of all contractor searches. When a pipe bursts, the customer calls the first company they find. Here's how to be that company.",
    date: "2026-03-25",
    readMin: 8,
    body: [
      "Water damage, fire damage, and mold remediation are the most urgent of all home service searches. When a customer has water coming through their ceiling at 2am, they search, they call, and whoever answers first gets the job. There's no price comparison, no multiple quote requests. The ranking position advantage in restoration is more direct and more immediate than in any other trade.",
      "Insurance relationships are a ranking factor that most restoration SEO guides ignore. Many restoration jobs are insurance-covered, and customers will often ask their insurance adjuster for a referral before searching Google. Building relationships with local insurance adjusters is both a business development and SEO strategy — when those adjusters have a website or a local citation for your business, that's a trust signal. Mention insurance claim assistance prominently in your GBP and on your website.",
      "The 72-hour urgency window is the decision frame for water damage. Customers searching 'water damage restoration near me' need someone today — and they'll only wait a few hours before calling the next company if you don't respond. Your GBP should show your response time prominently. Your website should have a clear headline about same-day response availability. If you offer 24/7 emergency response, that should be the first thing visitors see.",
      "Mold remediation is a separate search market from water damage restoration, even though you likely offer both. Create distinct service pages for each — mold inspection, mold testing, mold remediation, and post-remediation verification. These searches come at different stages: water damage is acute, mold concerns are often discovered weeks after an event. The content needs to match the emotional state of each searcher: urgent vs. concerned-but-not-panicking.",
    ],
  },
];

export const blogPostMap = Object.fromEntries(blogPosts.map((p) => [p.slug, p]));
