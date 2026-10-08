import { generatePageMeta } from "@/lib/seo";
import { breadcrumbGraph } from "@/lib/schema";
import { aboutPage } from "@/lib/copy";
import { JsonLd } from "@/components/ui/JsonLd";
import { PageHero } from "@/components/sections/PageHero";
import { FounderSection } from "@/components/sections/FounderSection";
import { BottomCTA } from "@/components/sections/BottomCTA";
import { Reveal } from "@/components/ui/Reveal";

export const metadata = generatePageMeta({
  title: "About RankLogic SEO",
  description:
    "Two founders, one mission: get South Florida home service contractors found and paid. No account managers, no agency-speak — just booked jobs and one client per trade per city.",
  path: "/about",
});

export default function AboutPage() {
  return (
    <>
      <JsonLd
        data={breadcrumbGraph([
          { name: "Home", path: "/" },
          { name: "About", path: "/about" },
        ])}
      />
      <PageHero
        kicker={aboutPage.kicker}
        h1={aboutPage.h1}
        sub={aboutPage.sub}
      />

      <section className="relative py-10">
        <div className="container-site mx-auto max-w-3xl space-y-5">
          {aboutPage.story.map((block, i) => (
            <Reveal key={block.heading} delay={i * 0.06}>
              <div className="glass rounded-3xl p-7 sm:p-9">
                <div className="flex items-start gap-4">
                  <span
                    className="font-display flex h-10 w-10 shrink-0 items-center justify-center rounded-xl text-lg font-black text-white"
                    style={{ background: "var(--grad-hot)" }}
                  >
                    {i + 1}
                  </span>
                  <div>
                    <h2 className="font-display text-xl font-bold text-ink sm:text-2xl">
                      {block.heading}
                    </h2>
                    <p className="mt-3 text-[0.98rem] leading-relaxed text-ink-soft">
                      {block.body}
                    </p>
                  </div>
                </div>
              </div>
            </Reveal>
          ))}
        </div>
      </section>

      <section className="relative py-12">
        <div className="container-site">
          <Reveal>
            <h2 className="text-center font-display text-3xl font-black text-ink sm:text-4xl">
              What we actually stand for.
            </h2>
          </Reveal>
          <div className="mt-10 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
            {aboutPage.values.map((value, i) => (
              <Reveal key={value.title} delay={i * 0.08}>
                <div className="neo lift h-full rounded-3xl p-6">
                  <h3 className="font-display text-lg font-bold text-ink">
                    {value.title}
                  </h3>
                  <p className="mt-2 text-sm leading-relaxed text-ink-soft">
                    {value.body}
                  </p>
                </div>
              </Reveal>
            ))}
          </div>
        </div>
      </section>

      <FounderSection />
      <BottomCTA />
    </>
  );
}
