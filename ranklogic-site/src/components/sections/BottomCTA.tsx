import { bottomCta } from "@/lib/copy";
import { site } from "@/lib/site";
import { Reveal } from "@/components/ui/Reveal";
import { Button } from "@/components/ui/Button";
import { PillBadge } from "@/components/ui/PillBadge";

export function BottomCTA() {
  return (
    <section className="relative py-16 sm:py-20">
      <div className="container-site">
        <Reveal>
          <div
            className="relative overflow-hidden rounded-[40px] px-7 py-14 text-center sm:px-12 sm:py-20"
            style={{
              background:
                "linear-gradient(125deg, #ff8a65 0%, #ff6b9d 50%, #4dd0e1 100%)",
            }}
          >
            <div
              className="absolute inset-0 opacity-30"
              style={{
                background:
                  "radial-gradient(ellipse at 20% 10%, rgba(255,255,255,0.5), transparent 55%)",
              }}
              aria-hidden
            />
            <div className="relative mx-auto flex max-w-2xl flex-col items-center">
              <PillBadge tone="white">{bottomCta.pill}</PillBadge>
              <h2 className="mt-5 font-display text-4xl font-black leading-tight text-white sm:text-[3.1rem]">
                {bottomCta.h2.map((seg, i) =>
                  seg.em ? (
                    <em
                      key={i}
                      className="font-display italic text-white/95"
                    >
                      {seg.text}
                    </em>
                  ) : (
                    <span key={i}>{seg.text}</span>
                  ),
                )}
              </h2>
              <p className="mt-4 max-w-lg text-base text-white/90 sm:text-lg">
                {bottomCta.sub}
              </p>

              <div className="mt-8 flex flex-col gap-3 sm:flex-row">
                <Button
                  href={bottomCta.primary.href}
                  variant="white"
                  size="lg"
                >
                  {bottomCta.primary.label}
                </Button>
                <Button
                  href={bottomCta.secondary.href}
                  variant="white-ghost"
                  size="lg"
                >
                  {bottomCta.secondary.label}
                </Button>
              </div>

              <a
                href={site.phoneHref}
                className="font-display mt-9 text-3xl font-black text-white sm:text-4xl"
              >
                {site.phoneDisplay}
              </a>
            </div>
          </div>
        </Reveal>
      </div>
    </section>
  );
}
