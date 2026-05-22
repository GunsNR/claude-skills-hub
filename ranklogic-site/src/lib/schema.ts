/**
 * JSON-LD structured-data builders. Rendered via next/script as
 * application/ld+json. Never reference content not visible on the page.
 */
import { site } from "./site";

const ORG_ID = `${site.url}/#organization`;
const WEBSITE_ID = `${site.url}/#website`;

export function organizationNode() {
  return {
    "@type": ["Organization", "ProfessionalService"],
    "@id": ORG_ID,
    name: site.name,
    url: site.url,
    description:
      "South Florida SEO agency for high-end home service contractors — roofing, HVAC, plumbing, pool, restoration, and electrical.",
    telephone: site.phoneDisplay,
    email: site.email,
    areaServed: [
      "South Florida",
      "Lakewood, NJ",
      "Brooklyn, NY",
      "Ocean County, NJ",
    ],
    address: {
      "@type": "PostalAddress",
      addressLocality: "Hollywood",
      addressRegion: "FL",
      addressCountry: "US",
    },
    sameAs: [] as string[],
  };
}

export function websiteNode() {
  return {
    "@type": "WebSite",
    "@id": WEBSITE_ID,
    url: site.url,
    name: site.name,
    publisher: { "@id": ORG_ID },
  };
}

/** Homepage @graph: Organization + ProfessionalService + WebSite. */
export function homeGraph() {
  return {
    "@context": "https://schema.org",
    "@graph": [organizationNode(), websiteNode()],
  };
}

export function serviceGraph(opts: {
  name: string;
  description: string;
  url: string;
}) {
  return {
    "@context": "https://schema.org",
    "@graph": [
      organizationNode(),
      {
        "@type": "Service",
        name: opts.name,
        description: opts.description,
        serviceType: "Search Engine Optimization",
        url: opts.url,
        provider: { "@id": ORG_ID },
        areaServed: "South Florida",
      },
    ],
  };
}

export function faqGraph(items: { q: string; a: string }[]) {
  return {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    mainEntity: items.map((item) => ({
      "@type": "Question",
      name: item.q,
      acceptedAnswer: { "@type": "Answer", text: item.a },
    })),
  };
}

export function breadcrumbGraph(crumbs: { name: string; path: string }[]) {
  return {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    itemListElement: crumbs.map((c, i) => ({
      "@type": "ListItem",
      position: i + 1,
      name: c.name,
      item: `${site.url}${c.path}`,
    })),
  };
}

export function articleGraph(opts: {
  headline: string;
  description: string;
  url: string;
}) {
  return {
    "@context": "https://schema.org",
    "@type": "Article",
    headline: opts.headline,
    description: opts.description,
    url: opts.url,
    publisher: { "@id": ORG_ID },
    author: { "@id": ORG_ID },
  };
}
