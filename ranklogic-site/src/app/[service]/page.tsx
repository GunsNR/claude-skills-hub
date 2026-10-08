import Link from "next/link";
import { notFound } from "next/navigation";
import { Search } from "lucide-react";
import { generatePageMeta } from "@/lib/seo";
import { site } from "@/lib/site";
import { serviceGraph, faqGraph, breadcrumbGraph } from "@/lib/schema";
import { trades, tradeMap } from "@/lib/trades";
import { faq } from "@/lib/copy";
import { JsonLd } from "@/components/ui/JsonLd";
import { Reveal } from "@/components/ui/Reveal";
import { RichText } from "@/components/ui/RichText";
import { PillBadge } from "@/components/ui/PillBadge";
import { Button } from "@/components/ui/Button";
import { PainBlock } from "@/components/sections/PainBlock";
import { HowItWorks } from "@/components/sections/HowItWorks";
import { PricingGrid } from "@/components/sections/PricingGrid";
import { FAQAccordion } from "@/components/sections/FAQAccordion";
import { BottomCTA } from "@/components/sections/BottomCTA";

export const dynamicParams = false;

export function generateStaticParams() {
  return trades.map((t) => ({ service: t.slug }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ service: string }>;
}) {
  const { service } = await params;
  const trade = tradeMap[service];
  if (!trade) return {};
  return generatePageMeta({
    title: trade.metaTitle,
    description: trade.metaDescription,
    path: `/${service}`,
  });
}

export default async function ServicePage({
  params,
}: {
  params: Promise<{ service: string }>;
}) {
  const { service } = await params;
  const trade = tradeMap[service];
  if (!trade) notFound();

  const path = `/${service}`;

  return (
    <>
      <JsonLd
        data={serviceGraph({
          name: `${trade.metaTitle} — RankLogic SEO`,
          description: trade.metaDescription,
          url: `${site.url}${path}`,
        })}
      />
      <JsonLd data={faqGraph(faq.items)} />
      <JsonLd
        data={breadcrumbGraph([
          { name: "Home", path: "/" },
          { name: trade.metaTitle, path },
        ])}
      />

      <section className="relative pt-9 pb-8 sm:pt-12">
        <div className="container-site flex flex-col items-center text-center">
          <nav className="font-caps mb-6 self-start text-xs uppercase tracking-[0.1em] text-ink-faint">
            <Link href="/" className="hover:text-coral-deep">
              Home
            </Link>
            <span className="mx-2">/</span>
            <span className="text-ink-soft">{trade.hero.kicker}</span>
          </nav>

          <Reveal>
            <PillBadge>{trade.hero.kicker}</PillBadge>
          </Reveal>
          <Reveal delay={0.08}>
            <h1 className="mt-5 max-w-4xl font-display text-[2.4rem] font-black leading-[1.07] text-ink sm:text-5xl lg:text-[3.3rem]">
              <RichText value={trade.hero.h1} />
            </h1>
          </Reveal>
          <Reveal delay={0.16}>
            <p className="mt-5 max-w-2xl text-base leading-relaxed text-ink-soft sm:text-lg">
              {trade.hero.sub}
            </p>
          </Reveal>
          <Reveal delay={0.24}>
            <div className="mt-8 flex flex-col gap-3 sm:flex-row">
              <Button href="/audit" size="lg">
                Get My Free Audit →
              </Button>
              <Button href={site.phoneHref} variant="ghost" size="lg">
                Call {site.phoneDisplay}
              </Button>
            </div>
          </Reveal>
        </div>
      </section>

      <section className="relative py-10">
        <div className="container-site grid items-start gap-6 lg:grid-cols-[1.1fr_0.9fr]">
          <Reveal>
            <div className="glass h-full rounded-[32px] p-8 sm:p-10">
              <h2 className="font-display text-2xl font-bold text-ink sm:text-3xl">
                Why {trade.plural} win — or lose — on Google.
              </h2>
              <p className="mt-4 text-[0.98rem] leading-relaxed text-ink-soft">
                {trade.intro}
              </p>
            </div>
          </Reveal>

          <Reveal delay={0.1}>
            <div className="neo h-full rounded-[28px] p-7">
              <p className="font-caps text-xs font-semibold uppercase tracking-[0.14em] text-ink-faint">
                What your customers type into Google
              </p>
              <div className="mt-4 flex flex-wrap gap-2.5">
                {trade.searches.map((q) => (
                  <span
                    key={q}
                    className="neo-inset inline-flex items-center gap-1.5 rounded-full px-3.5 py-2 text-[0.78rem] text-ink-soft"
                  >
                    <Search size={12} className="text-coral-deep" />
                    {q}
                  </span>
                ))}
              </div>
            </div>
          </Reveal>
        </div>
      </section>

      <PainBlock />

      <section className="relative py-14 sm:py-16">
        <div className="container-site">
          <Reveal className="flex flex-col items-center text-center">
            <PillBadge>What We Build</PillBadge>
            <h2 className="mt-5 max-w-2xl font-display text-3xl font-black leading-tight text-ink sm:text-4xl">
              The full system that gets {trade.plural} booked.
            </h2>
          </Reveal>
          <div className="mt-11 grid gap-5 md:grid-cols-2 lg:grid-cols-3">
            {trade.deliverables.map((d, i) => (
              <Reveal key={d.title} delay={(i % 3) * 0.08}>
                <div className="neo lift h-full rounded-3xl p-7">
                  <h3 className="font-display text-lg font-bold text-ink">
                    {d.title}
                  </h3>
                  <p className="mt-2.5 text-sm leading-relaxed text-ink-soft">
                    {d.body}
                  </p>
                </div>
              </Reveal>
            ))}
          </div>
        </div>
      </section>

      <HowItWorks />
      <PricingGrid />
      <FAQAccordion />
      <BottomCTA />
    </>
  );
}
