/**
 * Single source of truth for all site copy.
 * Components must never hardcode user-facing strings — import from here.
 *
 * `Rich` segments let a heading mix plain text, gradient-italic emphasis (`em`),
 * and highlight-bar text (`highlight`) without HTML in the copy layer.
 */

export type RichSeg = { text: string; em?: boolean; highlight?: boolean };
export type Rich = RichSeg[];

export const tradeOptions = [
  "Roofing",
  "HVAC",
  "Plumbing",
  "Pool",
  "Restoration",
  "Electrical",
] as const;

export const nav = {
  links: [
    { label: "How It Works", href: "/#how" },
    { label: "Pricing", href: "/pricing" },
    { label: "Blog", href: "/resources" },
    { label: "Results", href: "/#results" },
    { label: "FAQ", href: "/#faq" },
  ],
  cta: { label: "Free Audit", href: "/audit" },
};

export const topBar = {
  middle: "South Florida · NJ · NYC",
  right: "One client per trade per city",
};

export const hero = {
  badge: "Performance-Guaranteed SEO · South Florida",
  h1: [
    { text: "We " },
    { text: "Guarantee", highlight: true },
    { text: " Clients for Home Service Businesses." },
  ] as Rich,
  sub: "We get South Florida roofers, HVAC techs, and plumbers found, called, and booked. One client per trade, per city — or we don't take you on.",
  ctaPrimary: { label: "Get My Free Audit", href: "/audit" },
  ctaWhatsApp: "Chat on WhatsApp",
  reassure: "Free audit · No contracts past 90 days · Zero obligation",
  phoneIntro: "Or call",
  phoneOutro: "— Izzy answers, not a call center.",
  trust: "331+ five-star reviews · Wayne's Roofing Co., #1 in Ocean County",
};

export const proofStrip = {
  heading: "Quietly Trusted By Real Businesses · Real Names · Real Results",
};

export const steak = {
  quote: [
    { text: "There are a thousand SEO agencies. " },
    { text: "We're the steak amongst meatballs.", em: true },
  ] as Rich,
  bullets: [
    {
      title: "One client per trade, per city.",
      body: "We won't take your competitor. Ever. Lock the zip code or lose it to someone who will.",
    },
    {
      title: "No 12-month lock-ins.",
      body: "Pay month-to-month or pay for results. 90-day floor, then cancel anytime, no drama.",
    },
    {
      title: "No agency-speak.",
      body: "If your phone isn't ringing more in 90 days, you fire us. That simple.",
    },
  ],
};

export const pain = {
  pill: "Sound Familiar?",
  h2: [
    { text: "You've been " },
    { text: "SEO'd in the gonads", em: true },
    { text: " before." },
  ] as Rich,
  sub: "Most agencies sell you reports. We sell you ringing phones and booked calendars.",
  cards: [
    {
      tag: "Stuck on Page 2",
      problem:
        "Your competition is taking calls in your zip code that should be coming to you. Every. Single. Day.",
      fix: "We put your name first — even when they ask AI instead of Google.",
    },
    {
      tag: "Paying for Leads",
      problem:
        "Renting clicks from HomeAdvisor, Angi, Thumbtack — paying $80 for a lead three competitors also got.",
      fix: "Stop renting. Start owning your pipeline. Direct from Google to your phone.",
    },
    {
      tag: "Burned by an Agency",
      problem:
        "You paid $2K, $5K, $8K a month for vague reports. No more clients. Just more dashboards.",
      fix: "You're not crazy. Most of them are useless. We're not. Track us by booked jobs.",
    },
  ],
};

export const howItWorks = {
  h2: [
    { text: "How we " },
    { text: "actually", em: true },
    { text: " get you booked." },
  ] as Rich,
  steps: [
    {
      step: "Step One",
      name: "Audit",
      body: "Free, no-BS look at your site, your Google Business Profile, and your top 3 local competitors. You get a written report — whether you hire us or not. We'll show you exactly why calls are going to them instead of you.",
    },
    {
      step: "Step Two",
      name: "Deploy",
      body: "We fix the technical mess, build the city and service pages your customers actually search for, and lock down your Google Business Profile. Most wins start showing up in weeks one through six.",
    },
    {
      step: "Step Three",
      name: "Dominate",
      body: "Reviews. Rankings. Booked calls. We run a monthly review-velocity flywheel, weekly content, and a Job Attribution Log so you know exactly which calls came from our work. Phones — not vanity metrics.",
    },
  ],
};

export const pricingSection = {
  h2: [
    { text: "Three ways to work with us. " },
    { text: "You pick.", em: true },
  ] as Rich,
  sub: "Lower-risk entry, full-build standard, or full-market domination. No setup fees over $500. No contracts past 90 days.",
};

export const founder = {
  pill: "Who's actually doing the work",
  h2: [
    { text: "Two guys. " },
    { text: "One mission.", em: true },
    { text: " Your phone ringing." },
  ] as Rich,
  body: [
    { text: "Izzy", bold: true },
    {
      text: " ran the calls. Got tired of watching roofers, HVAC guys, and plumbers fork over $5K a month to agencies that couldn't tell them what a backlink was. ",
    },
    { text: "Dilshan", bold: true },
    {
      text: " — two-time national award-winning developer — builds the tech so the sites actually load fast and rank where they're supposed to. We work with one client per trade per city. If we take you, your competitor is locked out. That's how this works. That's why it works.",
    },
  ],
  signatures: [
    { name: "Izzy", role: "Founder · Strategy" },
    { name: "Dilshan", role: "Co-founder · Tech Lead" },
  ],
};

export const faq = {
  pill: "Straight Answers",
  heading: "Questions you're actually asking.",
  items: [
    {
      q: "Do you really only work with one client per trade per city?",
      a: "Yes — and we mean it. Once we take a roofer in your city, every other roofer who calls us gets a no. Your zip code is locked. It's the whole model: your competitor can't hire the agency that's beating them, because that agency is us, and we already work for you.",
    },
    {
      q: "What's the contract length?",
      a: "90-day floor so the work has time to actually land, then month-to-month. No 12-month handcuffs. If the phone isn't ringing more, you walk — no drama, no cancellation maze.",
    },
    {
      q: "How is the KPI Plan's price calculated?",
      a: "$900/mo base, plus $75 per verified lead, with the per-lead bonus capped at $1,500. So your ceiling is $2,400/mo total — and you only pay the bonus when we actually deliver booked leads. Zero-risk entry by design.",
    },
    {
      q: "What counts as a 'verified lead'?",
      a: "A real inbound phone call or form submission from a potential customer in your service area, logged in your Job Attribution Log. Wrong numbers, spam, robocalls, and your existing customers don't count. You only pay for the real thing.",
    },
    {
      q: "How fast will I see results?",
      a: "Most clients see early movement in weeks one through six — Google Business Profile fixes and technical wins land first. Meaningful ranking and call volume usually builds over 90 days. Anyone promising you page one in a week is lying to you.",
    },
    {
      q: "Will my price ever go up?",
      a: "Not for 12 months. Your rate is locked for a full year from your start date and auto-grandfathered against future increases. When we raise prices for new clients, you keep yours.",
    },
    {
      q: "Do you do SEO for trades outside roofing and HVAC?",
      a: "Our core is high-end home services — roofing, HVAC, plumbing, pool, restoration, and electrical. We also work with select boutique businesses (we run SEO for a Brooklyn dental practice and a home-staging company). Not sure if you fit? Call Izzy and ask.",
    },
    {
      q: "What if it doesn't work?",
      a: "After the 90-day floor you cancel anytime, no drama. We track everything by booked jobs — not vanity metrics — so you'll know exactly what you got for your money. If your phone isn't ringing more, you fire us. That simple.",
    },
  ],
};

export const bottomCta = {
  pill: "Last Thing",
  h2: [
    { text: "Phone's not ringing? " },
    { text: "Let's fix that.", em: true },
  ] as Rich,
  sub: "Free audit. Zero obligation. We'll tell you straight if we can help or not. 15 minutes. No pitch.",
  primary: { label: "Get My Free SEO Audit →", href: "/audit" },
  secondary: { label: "Book a 15-min Call", href: "/book" },
};

export const footer = {
  description:
    "South Florida's SEO agency for high-end home service contractors. We get your phone ringing — then we lock your competitors out.",
  services: [
    { label: "SEO for Roofers", href: "/seo-for-roofers" },
    { label: "SEO for HVAC", href: "/seo-for-hvac" },
    { label: "SEO for Plumbers", href: "/seo-for-plumbers" },
    { label: "SEO for Pool Service", href: "/seo-for-pool-service" },
    { label: "SEO for Restoration", href: "/seo-for-restoration" },
    { label: "SEO for Electricians", href: "/seo-for-electricians" },
  ],
  markets: [
    "South Florida",
    "Lakewood, NJ",
    "Brooklyn, NY",
    "Ocean County, NJ",
  ],
  company: [
    { label: "About", href: "/about" },
    { label: "Case Studies", href: "/case-studies/waynes-roofing" },
    { label: "Pricing", href: "/pricing" },
    { label: "Free Audit", href: "/audit" },
    { label: "Book a Call", href: "/book" },
  ],
  legal: "© 2026 RankLogic SEO. Hollywood, FL · Lakewood, NJ · Brooklyn, NY",
};

/* ---------- Standalone pages ---------- */

export const aboutPage = {
  kicker: "About RankLogic SEO",
  h1: [
    { text: "We're not an agency. We're the " },
    { text: "unfair advantage.", em: true },
  ] as Rich,
  sub: "Two guys who got tired of watching good contractors get fleeced by agencies that couldn't explain what they were paying for.",
  story: [
    {
      heading: "The problem we kept seeing.",
      body: "Izzy spent years on the phone with roofers, HVAC guys, and plumbers — real operators with real crews and great work. And almost every one of them had the same story: they'd handed $2K, $5K, even $8K a month to a marketing agency, and gotten back a stack of dashboards nobody read and a phone that rang exactly as much as before.",
    },
    {
      heading: "Why most SEO is broken for contractors.",
      body: "The agency model is built to sell reports, not results. They'd rather show you a graph of 'impressions' than admit your competitor is still getting the calls. We threw that model out. We track one thing that matters: booked jobs. If you can't see the work in your calendar, we haven't done our job.",
    },
    {
      heading: "The exclusivity model.",
      body: "Here's the part agencies hate: we only take one client per trade, per city. Once we take a Miami roofer, every other Miami roofer who calls us gets turned away. You're not one of fifty roofing clients getting a copy-paste playbook. You're the one. And your competitor is permanently locked out of working with the team that's beating them.",
    },
    {
      heading: "Two people. No account managers.",
      body: "Izzy runs strategy and answers the phone himself. Dilshan — a two-time national award-winning developer — builds the technical side so your site loads fast and ranks where it should. No junior account manager, no outsourced content mill. The two people you hire are the two people doing the work.",
    },
  ],
  values: [
    {
      title: "Booked jobs, not vanity metrics",
      body: "We report on calls and jobs. Impressions don't pay your crew.",
    },
    {
      title: "Plain English, always",
      body: "If we can't explain it to a 55-year-old roofer, we don't say it.",
    },
    {
      title: "Locked-in pricing",
      body: "Your rate holds for 12 months and grandfathers against increases.",
    },
    {
      title: "Earn the renewal monthly",
      body: "90-day floor, then month-to-month. We keep you by performing.",
    },
  ],
};

export const pricingPage = {
  kicker: "Pricing",
  h1: [
    { text: "Honest pricing. " },
    { text: "No surprises.", em: true },
  ] as Rich,
  sub: "Three ways to work with us — pick the risk level that fits your shop. No setup fees over $500. No contracts past 90 days. Your rate locked for a full year.",
};

export const auditPage = {
  kicker: "Free SEO Audit",
  h1: [
    { text: "See exactly what's " },
    { text: "costing you jobs.", em: true },
  ] as Rich,
  sub: "A real human reviews your site, your Google Business Profile, and your top 3 local competitors. You get a written report within 48 hours — whether you hire us or not.",
  checklist: [
    "Where you rank vs. your top 3 competitors",
    "What's broken on your Google Business Profile",
    "The searches your customers use that you're invisible for",
    "Technical issues quietly killing your rankings",
    "A straight answer on whether we can help",
  ],
  form: {
    badge: "Free Audit · Zero Obligation",
    heading: "Request your free audit.",
    cta: "Send My Free Audit →",
    finePrint:
      "No spam. No sales pitch. We'll review your site within 48 hours.",
  },
};

export const bookPage = {
  kicker: "Book a Call",
  h1: [
    { text: "15 minutes. " },
    { text: "No pitch.", em: true },
  ] as Rich,
  sub: "Grab a time that works. We'll talk through your market, your competitors, and whether we're the right fit. If we're not, we'll tell you straight.",
  expectations: [
    "A look at your local search landscape",
    "Straight talk on what's working and what isn't",
    "Whether your trade and city are still open",
    "Zero hard sell — Izzy hates them too",
  ],
};
