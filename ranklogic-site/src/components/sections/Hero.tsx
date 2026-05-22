import { hero } from "@/lib/copy";
import { site } from "@/lib/site";
import { AuditForm } from "@/components/AuditForm";
import { Reveal } from "@/components/ui/Reveal";
import { RichText } from "@/components/ui/RichText";
import { PillBadge } from "@/components/ui/PillBadge";

export function Hero() {
  return (
    <section className="relative pt-10 pb-16 sm:pt-14 sm:pb-24">
      <div className="container-site grid items-center gap-12 lg:grid-cols-[1.08fr_0.92fr]">
        <div>
          <Reveal>
            <PillBadge>Make More Money · Get More Clients</PillBadge>
          </Reveal>

          <Reveal delay={0.08}>
            <h1 className="mt-6 font-display text-[2.5rem] font-black leading-[1.06] text-ink sm:text-5xl lg:text-[3.55rem]">
              <RichText value={hero.h1} />
            </h1>
          </Reveal>

          <Reveal delay={0.16}>
            <p className="mt-6 max-w-xl text-base leading-relaxed text-ink-soft sm:text-lg">
              {hero.sub}
            </p>
          </Reveal>

          <Reveal delay={0.24}>
            <div className="mt-8 flex flex-wrap items-center gap-x-3 gap-y-2">
              <p className="text-sm text-ink-soft">
                {hero.phoneLine}{" "}
                <a
                  href={site.phoneHref}
                  className="font-display text-lg font-bold text-coral-deep"
                >
                  {site.phoneDisplay}
                </a>{" "}
                <span className="text-ink-faint">{hero.phoneLineEnd}</span>
              </p>
            </div>
          </Reveal>

          <Reveal delay={0.32}>
            <div className="mt-6 flex items-center gap-3">
              <span className="text-lg tracking-tight text-amber">
                ★★★★★
              </span>
              <span className="text-sm text-ink-soft">
                <strong className="text-ink">331+ reviews</strong> · Wayne&apos;s
                Roofing Co. — #1 in Ocean County
              </span>
            </div>
          </Reveal>
        </div>

        <Reveal delay={0.18}>
          <AuditForm
            badge={hero.form.badge}
            heading={hero.form.heading}
            cta={hero.form.cta}
            finePrint={hero.form.finePrint}
          />
        </Reveal>
      </div>
    </section>
  );
}
