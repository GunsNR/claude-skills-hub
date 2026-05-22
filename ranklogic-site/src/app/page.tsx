import { generatePageMeta } from "@/lib/seo";
import { faqGraph } from "@/lib/schema";
import { faq } from "@/lib/copy";
import { JsonLd } from "@/components/ui/JsonLd";
import { Hero } from "@/components/sections/Hero";
import { ProofStrip } from "@/components/sections/ProofStrip";
import { SteakSection } from "@/components/sections/SteakSection";
import { PainBlock } from "@/components/sections/PainBlock";
import { CaseStudyFeature } from "@/components/sections/CaseStudyFeature";
import { HowItWorks } from "@/components/sections/HowItWorks";
import { PricingGrid } from "@/components/sections/PricingGrid";
import { FounderSection } from "@/components/sections/FounderSection";
import { FAQAccordion } from "@/components/sections/FAQAccordion";
import { BottomCTA } from "@/components/sections/BottomCTA";

export const metadata = generatePageMeta({
  title: "South Florida SEO for High-End Home Services",
  description:
    "Phone-ringing SEO for South Florida roofers, HVAC, plumbers, pool, restoration, and electrical contractors. One client per trade per city. Make more money, get more clients.",
  path: "/",
});

export default function Home() {
  return (
    <>
      <JsonLd data={faqGraph(faq.items)} />
      <Hero />
      <ProofStrip />
      <SteakSection />
      <PainBlock />
      <CaseStudyFeature />
      <HowItWorks />
      <PricingGrid />
      <FounderSection />
      <FAQAccordion />
      <BottomCTA />
    </>
  );
}
