import { hero } from "@/lib/copy";
import { site } from "@/lib/site";
import { Reveal } from "@/components/ui/Reveal";
import { RichText } from "@/components/ui/RichText";
import { PillBadge } from "@/components/ui/PillBadge";
import { Button } from "@/components/ui/Button";
import { WhatsAppIcon } from "@/components/ui/WhatsAppIcon";

export function Hero() {
  return (
    <section className="relative flex min-h-[84vh] items-center py-14 sm:py-20">
      <div className="container-site flex flex-col items-center text-center">
        <Reveal>
          <PillBadge>{hero.badge}</PillBadge>
        </Reveal>

        <Reveal delay={0.08}>
          <h1 className="mt-7 max-w-[18ch] text-balance font-display text-[2.8rem] font-black leading-[1.02] text-ink sm:text-6xl lg:text-[5.1rem]">
            <RichText value={hero.h1} />
          </h1>
        </Reveal>

        <Reveal delay={0.16}>
          <p className="mt-7 max-w-2xl text-lg leading-relaxed text-ink-soft sm:text-xl">
            {hero.sub}
          </p>
        </Reveal>

        <Reveal delay={0.24}>
          <div className="mt-10 flex w-full flex-col gap-3.5 sm:w-auto sm:flex-row">
            <Button href={hero.ctaPrimary.href} size="xl">
              {hero.ctaPrimary.label} →
            </Button>
            <a
              href={site.whatsapp}
              target="_blank"
              rel="noopener noreferrer"
              className="glass font-caps inline-flex items-center justify-center gap-2.5 rounded-full px-9 py-5 text-[1rem] font-semibold uppercase tracking-[0.06em] text-ink transition-all duration-300 hover:-translate-y-0.5"
            >
              <WhatsAppIcon className="h-5 w-5 text-[#25d366]" />
              {hero.ctaWhatsApp}
            </a>
          </div>
        </Reveal>

        <Reveal delay={0.3}>
          <p className="font-caps mt-5 text-[0.72rem] font-semibold uppercase tracking-[0.14em] text-ink-faint">
            {hero.reassure}
          </p>
        </Reveal>

        <Reveal delay={0.36}>
          <div className="mt-11 flex flex-col items-center gap-3">
            <p className="text-base text-ink-soft">
              {hero.phoneIntro}{" "}
              <a
                href={site.phoneHref}
                className="font-display text-xl font-bold text-coral-deep"
              >
                {site.phoneDisplay}
              </a>{" "}
              <span className="text-ink-faint">{hero.phoneOutro}</span>
            </p>
            <div className="flex items-center gap-2.5">
              <span className="text-lg tracking-tight text-amber">★★★★★</span>
              <span className="text-sm text-ink-soft">{hero.trust}</span>
            </div>
          </div>
        </Reveal>
      </div>
    </section>
  );
}
