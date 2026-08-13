import Link from "next/link";
import { notFound } from "next/navigation";
import { generatePageMeta } from "@/lib/seo";
import { site } from "@/lib/site";
import { articleGraph, breadcrumbGraph } from "@/lib/schema";
import { caseStudies, caseStudyList } from "@/lib/clients";
import { JsonLd } from "@/components/ui/JsonLd";
import { GradientText } from "@/components/ui/GradientText";
import { PillBadge } from "@/components/ui/PillBadge";
import { Reveal } from "@/components/ui/Reveal";
import { BottomCTA } from "@/components/sections/BottomCTA";

export const dynamicParams = false;

export function generateStaticParams() {
  return caseStudyList.map((cs) => ({ slug: cs.slug }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const cs = caseStudies[slug];
  if (!cs) return {};
  return generatePageMeta({
    title: `${cs.client} — SEO Case Study`,
    description: cs.summary,
    path: `/case-studies/${slug}`,
  });
}

export default async function CaseStudyPage({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const cs = caseStudies[slug];
  if (!cs) notFound();

  const path = `/case-studies/${slug}`;

  return (
    <>
      <JsonLd
        data={articleGraph({
          headline: `${cs.headline} ${cs.headlineEm}`,
          description: cs.summary,
          url: `${site.url}${path}`,
        })}
      />
      <JsonLd
        data={breadcrumbGraph([
          { name: "Home", path: "/" },
          { name: "Case Studies", path: "/case-studies/waynes-roofing" },
          { name: cs.client, path },
        ])}
      />

      <section className="relative pt-8 pb-10 sm:pt-12">
        <div className="container-site">
          <nav className="font-caps text-xs uppercase tracking-[0.1em] text-ink-faint">
            <Link href="/" className="hover:text-coral-deep">
              Home
            </Link>
            <span className="mx-2">/</span>
            <span className="text-ink-soft">Case Study</span>
          </nav>

          <div className="mt-6 max-w-3xl">
            <Reveal>
              <PillBadge>Featured Case Study</PillBadge>
            </Reveal>
            <Reveal delay={0.08}>
              <p className="font-caps mt-5 text-sm font-semibold uppercase tracking-[0.12em] text-ink-faint">
                {cs.client} · {cs.location} · {cs.trade}
              </p>
            </Reveal>
            <Reveal delay={0.14}>
              <h1 className="mt-3 font-display text-[2.4rem] font-black leading-[1.07] text-ink sm:text-5xl lg:text-[3.2rem]">
                {cs.headline}{" "}
                <em className="font-display italic grad-text">
                  {cs.headlineEm}
                </em>
              </h1>
            </Reveal>
            <Reveal delay={0.2}>
              <p className="mt-5 text-base leading-relaxed text-ink-soft sm:text-lg">
                {cs.summary}
              </p>
            </Reveal>
          </div>

          <Reveal delay={0.26}>
            <div className="mt-10 grid gap-3 sm:grid-cols-4">
              {cs.stats.map((stat) => (
                <div
                  key={stat.label}
                  className="neo rounded-3xl px-5 py-7 text-center"
                >
                  <div className="font-display text-4xl font-black sm:text-5xl">
                    <GradientText>{stat.value}</GradientText>
                  </div>
                  <div className="font-caps mt-2 text-[0.64rem] font-semibold uppercase tracking-[0.1em] text-ink-faint">
                    {stat.label}
                  </div>
                </div>
              ))}
            </div>
          </Reveal>
        </div>
      </section>

      <section className="relative pb-12">
        <div className="container-site">
          <Reveal>
            <div className="glass mx-auto max-w-3xl rounded-[32px] p-8 sm:p-12">
              <h2 className="font-display text-2xl font-bold text-ink">
                The breakdown
              </h2>
              <div className="mt-5 space-y-5">
                {cs.body.map((para, i) => (
                  <p
                    key={i}
                    className="text-[1rem] leading-relaxed text-ink-soft"
                  >
                    {para}
                  </p>
                ))}
              </div>

              <div className="neo-inset mt-8 rounded-2xl p-6">
                <p className="font-caps text-xs font-semibold uppercase tracking-[0.14em] text-coral-deep">
                  The result
                </p>
                <p className="mt-2 font-display text-lg font-bold text-ink">
                  {cs.result}
                </p>
              </div>
            </div>
          </Reveal>
        </div>
      </section>

      <BottomCTA />
    </>
  );
}
