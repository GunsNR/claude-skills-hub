/** Real client data. Never embellish these numbers — they appear on a client-facing site. */

export interface ClientProof {
  name: string;
  rating: string;
  stat: string;
  location: string;
  trade: string;
}

export const clientProof: ClientProof[] = [
  {
    name: "Wayne's Roofing Co.",
    rating: "★★★★★",
    stat: "331+ Google Reviews",
    location: "Ocean County, NJ",
    trade: "Roofing",
  },
  {
    name: "AtlasCare ABA",
    rating: "★★★★★",
    stat: "5-State Coverage",
    location: "Multi-state",
    trade: "ABA Therapy",
  },
  {
    name: "Toothology",
    rating: "★★★★★",
    stat: "Boutique Specialists",
    location: "Williamsburg, NY",
    trade: "Dental",
  },
  {
    name: "Stageitus",
    rating: "★★★★★",
    stat: "NJ + Philadelphia",
    location: "Investment Properties",
    trade: "Home Staging",
  },
];

export interface CaseStudy {
  slug: string;
  client: string;
  trade: string;
  location: string;
  headline: string;
  headlineEm: string;
  summary: string;
  stats: { label: string; value: string }[];
  body: string[];
  result: string;
}

export const caseStudies: Record<string, CaseStudy> = {
  "waynes-roofing": {
    slug: "waynes-roofing",
    client: "Wayne's Roofing Co.",
    trade: "Roofing",
    location: "Ocean County, NJ",
    headline: "From scattered calls to",
    headlineEm: "#1 in the county.",
    summary:
      "How a solid roofing trade with almost no online footprint became the #1 rated roofing company in Ocean County — and locked every competitor out.",
    stats: [
      { label: "Google Reviews", value: "331+" },
      { label: "Star Rating", value: "5.0 ★" },
      { label: "Market Position", value: "#1" },
      { label: "NJ Expansion", value: "21" },
    ],
    body: [
      "Wayne's came to us with a solid trade and almost no online footprint. Great work, great crew, almost invisible on Google. The calls that should have been theirs were going to competitors with worse work and better websites.",
      "We locked down the Google Business Profile, built out the county and city pages their customers actually search for, and ran a review velocity system that took them from no reviews to 331+ five-star Google reviews — making them the #1 rated roofing company in Ocean County.",
      "Now we're rolling out the same county-by-county system across all 21 New Jersey counties. Their competitors are locked out, one county at a time. That's how the model works — and that's why it works.",
    ],
    result:
      "#1 rated roofing company in Ocean County, NJ. Expansion underway across all 21 New Jersey counties.",
  },
};

export const caseStudyList = Object.values(caseStudies);
