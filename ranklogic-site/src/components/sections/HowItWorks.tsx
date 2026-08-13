import { howItWorks } from "@/lib/copy";
import { Reveal } from "@/components/ui/Reveal";
import { RichText } from "@/components/ui/RichText";
import { PillBadge } from "@/components/ui/PillBadge";

export function HowItWorks() {
  return (
    <section id="how" className="relative scroll-mt-28 py-16 sm:py-20">
      <div className="container-site">
        <Reveal className="flex flex-col items-center text-center">
          <PillBadge>The Process</PillBadge>
          <h2 className="mt-5 max-w-3xl font-display text-3xl font-black leading-tight text-ink sm:text-[2.7rem]">
            <RichText value={howItWorks.h2} />
          </h2>
        </Reveal>

        <div className="mt-12 grid gap-5 md:grid-cols-3">
          {howItWorks.steps.map((step, i) => (
            <Reveal key={step.name} delay={i * 0.1}>
              <div className="neo lift flex h-full flex-col rounded-3xl p-7">
                <div className="flex items-center gap-3">
                  <span
                    className="font-display flex h-12 w-12 items-center justify-center rounded-2xl text-xl font-black text-white"
                    style={{ background: "var(--grad-hot)" }}
                  >
                    {i + 1}
                  </span>
                  <div>
                    <p className="font-caps text-[0.66rem] font-semibold uppercase tracking-[0.14em] text-ink-faint">
                      {step.step}
                    </p>
                    <p className="font-display text-xl font-bold text-ink">
                      {step.name}
                    </p>
                  </div>
                </div>
                <p className="mt-5 text-sm leading-relaxed text-ink-soft">
                  {step.body}
                </p>
              </div>
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  );
}
