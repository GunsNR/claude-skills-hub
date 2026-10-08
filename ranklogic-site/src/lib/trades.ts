/** Trade (service) page data. Each entry powers a /seo-for-{trade} page. */

import type { Rich } from "./copy";

export interface Trade {
  slug: string;
  trade: string;
  plural: string;
  metaTitle: string;
  metaDescription: string;
  hero: { kicker: string; h1: Rich; sub: string };
  intro: string;
  searches: string[];
  deliverables: { title: string; body: string }[];
}

const sharedDeliverables = (trade: string) => [
  {
    title: "Google Business Profile lockdown",
    body: `Your profile is where most ${trade.toLowerCase()} jobs start. We optimize it, fix the categories, kill duplicate listings, and run a review-velocity system that buries your competitors.`,
  },
  {
    title: "City & service pages that rank",
    body: "We build the pages your customers actually search for — by service, by city, by emergency — with the schema and technical SEO that gets them indexed and ranked.",
  },
  {
    title: "Reviews on autopilot",
    body: "A review flywheel that turns happy customers into five-star Google reviews on a steady schedule. Reviews are the trust signal that wins the click.",
  },
  {
    title: "AI search visibility",
    body: "When a homeowner asks ChatGPT or Google's AI for a contractor, your name should come up. We structure your site so AI answers cite you, not them.",
  },
  {
    title: "Job Attribution Log",
    body: "Every lead, tracked and tied back to our work. You see exactly which calls came from SEO — no vanity metrics, no guessing.",
  },
  {
    title: "Technical SEO that loads fast",
    body: "Built by a two-time award-winning developer. Fast sites rank higher and convert better. Slow sites lose the job before the phone rings.",
  },
];

export const trades: Trade[] = [
  {
    slug: "seo-for-roofers",
    trade: "Roofing",
    plural: "roofers",
    metaTitle: "SEO for Roofers",
    metaDescription:
      "SEO for roofers in South Florida. Rank #1 for roof repair and replacement searches, win storm-damage and insurance jobs, and lock competitors out of your city.",
    hero: {
      kicker: "SEO for Roofers",
      h1: [
        { text: "When a roof leaks in your city, you should be " },
        { text: "the first call.", em: true },
      ],
      sub: "Storm damage. Full replacements. Insurance jobs. The homeowner grabs their phone and searches. We make sure your name is what they find — on Google and in AI answers.",
    },
    intro:
      "Roofing is the most competitive home-service trade online. Every roofer in your county is fighting for the same searches — and most are losing to the one company that figured out SEO. We make that company you, then we lock the rest out. One roofer per city: yours or theirs.",
    searches: [
      "roof repair near me",
      "roof replacement [city]",
      "emergency roofer",
      "roof leak repair",
      "storm damage roofing",
      "metal roof installation",
    ],
    deliverables: sharedDeliverables("Roofing"),
  },
  {
    slug: "seo-for-hvac",
    trade: "HVAC",
    plural: "HVAC companies",
    metaTitle: "SEO for HVAC Companies",
    metaDescription:
      "SEO for HVAC companies in South Florida. Capture AC repair and install searches in your zip code, win emergency calls, and own your local market.",
    hero: {
      kicker: "SEO for HVAC",
      h1: [
        { text: "Every broken AC in your zip is " },
        { text: "a search right now.", em: true },
      ],
      sub: "It's 95 degrees and a homeowner's AC just died. They're not flipping through a phone book — they're searching. We make sure the company they find is yours.",
    },
    intro:
      "In South Florida, AC isn't optional — and neither is showing up when it breaks. HVAC searches spike with the heat, and the company ranking first takes the emergency calls, the installs, and the maintenance contracts. We get you to the top and keep you there.",
    searches: [
      "ac repair near me",
      "hvac installation [city]",
      "emergency ac repair",
      "air conditioning service",
      "ac not cooling",
      "hvac maintenance plan",
    ],
    deliverables: sharedDeliverables("HVAC"),
  },
  {
    slug: "seo-for-plumbers",
    trade: "Plumbing",
    plural: "plumbers",
    metaTitle: "SEO for Plumbers",
    metaDescription:
      "SEO for plumbers in South Florida. Rank for emergency plumbing, water heater, and repipe searches — and turn urgent searches into booked jobs.",
    hero: {
      kicker: "SEO for Plumbers",
      h1: [
        { text: "Burst pipes don't wait. " },
        { text: "Neither do searches.", em: true },
      ],
      sub: "Plumbing emergencies are won in minutes. The homeowner searches, calls the first name they trust, and the job is gone. We make that first name yours.",
    },
    intro:
      "Plumbing is urgency-driven — and urgency rewards whoever ranks first. From burst pipes to water heaters to full repipes, the plumber at the top of Google takes the call before anyone else gets a shot. We put you there and lock the city down.",
    searches: [
      "emergency plumber near me",
      "water heater repair [city]",
      "drain cleaning service",
      "burst pipe repair",
      "plumber near me",
      "repipe specialist",
    ],
    deliverables: sharedDeliverables("Plumbing"),
  },
  {
    slug: "seo-for-pool-service",
    trade: "Pool Service",
    plural: "pool companies",
    metaTitle: "SEO for Pool Service Companies",
    metaDescription:
      "SEO for pool service and pool repair companies in South Florida. Win recurring maintenance contracts and repair jobs from local search.",
    hero: {
      kicker: "SEO for Pool Service",
      h1: [
        { text: "Your next pool won't " },
        { text: "find itself.", em: true },
      ],
      sub: "South Florida is wall-to-wall pools — and every one needs service, repairs, and a company the homeowner trusts. We make sure that company is yours.",
    },
    intro:
      "Pool service is a recurring-revenue goldmine — one ranked search becomes a contract that pays every month for years. We get you found for service, repair, and renovation searches across your market, and lock your competitors out one zip code at a time.",
    searches: [
      "pool service near me",
      "pool cleaning [city]",
      "pool repair company",
      "weekly pool maintenance",
      "pool resurfacing",
      "pool pump replacement",
    ],
    deliverables: sharedDeliverables("Pool Service"),
  },
  {
    slug: "seo-for-restoration",
    trade: "Restoration",
    plural: "restoration companies",
    metaTitle: "SEO for Restoration Companies",
    metaDescription:
      "SEO for water, fire, and mold restoration companies in South Florida. Capture high-urgency emergency searches and insurance jobs.",
    hero: {
      kicker: "SEO for Restoration",
      h1: [
        { text: "Water damage calls go to whoever shows up " },
        { text: "first.", em: true },
      ],
      sub: "Flooding, fire, mold — these are panic searches. The homeowner needs help now and calls the first credible company they find. We make sure that's you.",
    },
    intro:
      "Restoration is the highest-urgency trade online. Water and fire damage can't wait, and the insurance jobs are big. The company ranking first for emergency restoration searches wins the call, the claim, and the revenue. We get you to that spot and defend it.",
    searches: [
      "water damage restoration near me",
      "fire damage cleanup [city]",
      "mold remediation",
      "emergency water removal",
      "flood damage repair",
      "storm damage restoration",
    ],
    deliverables: sharedDeliverables("Restoration"),
  },
  {
    slug: "seo-for-electricians",
    trade: "Electrical",
    plural: "electricians",
    metaTitle: "SEO for Electricians",
    metaDescription:
      "SEO for electricians in South Florida. Rank for panel upgrade, EV charger, and emergency electrical searches — and turn them into booked jobs.",
    hero: {
      kicker: "SEO for Electricians",
      h1: [
        { text: "Panel upgrades and emergencies " },
        { text: "start with a search.", em: true },
      ],
      sub: "From dead outlets to full panel upgrades to EV chargers, homeowners search before they call. We make sure the electrician they find — and trust — is you.",
    },
    intro:
      "Electrical work spans quick fixes and high-ticket upgrades, and every one of them starts on Google. The electrician ranking first gets the emergency calls and the big panel and EV-charger jobs. We get you ranked and keep your competitors off the page.",
    searches: [
      "electrician near me",
      "panel upgrade [city]",
      "ev charger installation",
      "emergency electrician",
      "electrical repair service",
      "generator installation",
    ],
    deliverables: sharedDeliverables("Electrical"),
  },
];

export const tradeMap = Object.fromEntries(trades.map((t) => [t.slug, t]));
