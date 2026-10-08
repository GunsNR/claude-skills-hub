/** Pricing tier data. Verified numbers — do not change without sign-off from Izzy. */

export interface PricingTier {
  id: string;
  name: string;
  amount: string;
  amountSub: string;
  bestFor: string;
  featured: boolean;
  ribbon?: string;
  features: { label: string; included: boolean }[];
}

export const pricingTiers: PricingTier[] = [
  {
    id: "kpi",
    name: "KPI Plan",
    amount: "$900",
    amountSub: "+ $75 / verified lead, capped at $1,500 bonus",
    bestFor: "Zero-risk entry",
    featured: false,
    features: [
      { label: "Google Business Profile optimization", included: true },
      { label: "2 service / city pages", included: true },
      { label: "Job Attribution Log", included: true },
      { label: "Verified-lead reporting", included: true },
      { label: "Monthly content", included: false },
      { label: "Google LSA management", included: false },
    ],
  },
  {
    id: "standard",
    name: "Standard",
    amount: "$2,000",
    amountSub: "Full build. Monthly strategy call.",
    bestFor: "Most South Florida shops",
    featured: true,
    ribbon: "★ Most Picked",
    features: [
      { label: "Google Business Profile optimization", included: true },
      { label: "6 service + city pages", included: true },
      { label: "2 monthly blog posts", included: true },
      { label: "Review velocity flywheel", included: true },
      { label: "Monthly strategy call + report", included: true },
      { label: "Full schema + technical SEO", included: true },
    ],
  },
  {
    id: "dominate",
    name: "Dominate",
    amount: "$3,500",
    amountSub: "Lock the whole market.",
    bestFor: "Own the city",
    featured: false,
    features: [
      { label: "Everything in Standard", included: true },
      { label: "12 service + city pages", included: true },
      { label: "4 monthly blog posts", included: true },
      { label: "Google LSA management", included: true },
      { label: "Bi-weekly reporting + calls", included: true },
      { label: "Priority Slack channel", included: true },
    ],
  },
];

export const pricingNote =
  "Pricing locked for 12 months from start date. Auto-grandfathered against future rate increases. No contracts past 90 days.";
