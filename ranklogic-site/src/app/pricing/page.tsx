import { generatePageMeta } from "@/lib/seo";
import { breadcrumbGraph, faqGraph } from "@/lib/schema";
import { pricingPage, faq } from "@/lib/copy";
import { JsonLd } from "@/components/ui/JsonLd";
import { PageHero } from "@/components/sections/PageHero";
import { PricingGrid } from "@/components/sections/PricingGrid";
import { FAQAccordion } from "@/components/sections/FAQAccordion";
import { BottomCTA } from "@/components/sections/BottomCTA";

export const metadata = generatePageMeta({
  title: "SEO Pricing for Home Service Contractors",
  description:
    "Three transparent SEO plans for South Florida contractors: KPI ($900/mo), Standard ($2,000/mo), and Dominate ($3,500/mo). No contracts past 90 days. Rate locked 12 months.",
  path: "/pricing",
});

export default function PricingPage() {
  return (
    <>
      <JsonLd data={faqGraph(faq.items)} />
      <JsonLd
        data={breadcrumbGraph([
          { name: "Home", path: "/" },
          { name: "Pricing", path: "/pricing" },
        ])}
      />
      <PageHero
        kicker={pricingPage.kicker}
        h1={pricingPage.h1}
        sub={pricingPage.sub}
      />
      <PricingGrid showHeading={false} />
      <FAQAccordion />
      <BottomCTA />
    </>
  );
}
