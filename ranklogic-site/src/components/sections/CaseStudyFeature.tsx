import { caseStudies } from "@/lib/clients";
import { Reveal } from "@/components/ui/Reveal";
import { GradientText } from "@/components/ui/GradientText";
import { PillBadge } from "@/components/ui/PillBadge";
import { Button } from "@/components/ui/Button";

export function CaseStudyFeature() {
  const cs = caseStudies["waynes-roofing"];

  return (
    <section id="results" className="relative scroll-mt-28 py-16 sm:py-20">
      <div className="container-site">
        <Reveal>
          <div className="glass rounded-[36px] p-6 sm:p-10">
            <div className="grid items-center gap-8 lg:grid-cols-[0.85fr_1.15fr]">
              <div className="neo rounded-[28px] p-7 sm:p-8">
                <p className="font-display text-lg font-bold text-ink">
                  {cs.client}
                </p>
                <p className="font-caps mt-1 text-xs font-semibold uppercase tracking-[0.12em] text-ink-faint">
                  {cs.location} · {cs.trade}
                </p>
                <div className="mt-6 grid grid-cols-2 gap-3">
                  {cs.stats.map((stat) => (
                    <div
                      key={stat.label}
                      className="neo-inset rounded-2xl px-4 py-5 text-center"
                    >
                      <div className="font-display text-3xl font-black sm:text-4xl">
                        <GradientText>{stat.value}</GradientText>
                      </div>
                      <div className="font-caps mt-1.5 text-[0.62rem] font-semibold uppercase tracking-[0.1em] text-ink-faint">
                        {stat.label}
                      </div>
                    </div>
                  ))}
                </div>
              </div>

              <div>
                <PillBadge>Featured Case Study</PillBadge>
                <h2 className="mt-5 font-display text-3xl font-black leading-tight text-ink sm:text-[2.5rem]">
                  {cs.headline}{" "}
                  <em className="font-display italic grad-text">
                    {cs.headlineEm}
                  </em>
                </h2>
                <p className="mt-5 text-[0.98rem] leading-relaxed text-ink-soft">
                  {cs.body[0]} {cs.body[1]}
                </p>
                <div className="mt-7">
                  <Button
                    href={`/case-studies/${cs.slug}`}
                    variant="ghost"
                    size="md"
                  >
                    Read the full breakdown →
                  </Button>
                </div>
              </div>
            </div>
          </div>
        </Reveal>
      </div>
    </section>
  );
}
