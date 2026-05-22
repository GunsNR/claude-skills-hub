import { founder } from "@/lib/copy";
import { Reveal } from "@/components/ui/Reveal";
import { PillBadge } from "@/components/ui/PillBadge";

export function FounderSection() {
  return (
    <section className="relative py-16 sm:py-20">
      <div className="container-site">
        <Reveal>
          <div className="relative overflow-hidden rounded-[36px] bg-navy p-6 sm:p-10">
            <div className="dots-light absolute inset-0" aria-hidden />
            <div className="relative grid items-stretch gap-8 lg:grid-cols-[0.85fr_1.15fr]">
              {/* Visual block — placeholder for real founder photo */}
              <div
                className="relative flex min-h-[320px] items-end overflow-hidden rounded-[28px]"
                style={{ background: "var(--grad-sunset)" }}
              >
                <span
                  className="font-display absolute inset-0 flex items-center justify-center text-[11rem] font-black text-white/15"
                  aria-hidden
                >
                  R
                </span>
                <div className="relative m-4 w-full rounded-2xl bg-cream/92 px-4 py-3 backdrop-blur">
                  <p className="font-display text-base font-bold text-ink">
                    Izzy · Dilshan
                  </p>
                  <p className="font-caps text-[0.62rem] font-semibold uppercase tracking-[0.12em] text-ink-faint">
                    Founders, RankLogic SEO
                  </p>
                </div>
              </div>

              <div className="flex flex-col justify-center">
                <PillBadge>{founder.pill}</PillBadge>
                <h2 className="mt-5 font-display text-3xl font-black leading-tight text-cream sm:text-[2.5rem]">
                  {founder.h2.map((seg, i) =>
                    seg.em ? (
                      <em
                        key={i}
                        className="font-display italic text-coral"
                      >
                        {seg.text}
                      </em>
                    ) : (
                      <span key={i}>{seg.text}</span>
                    ),
                  )}
                </h2>
                <p className="mt-5 text-[0.98rem] leading-relaxed text-cream/80">
                  {founder.body.map((seg, i) =>
                    seg.bold ? (
                      <strong key={i} className="font-bold text-cream">
                        {seg.text}
                      </strong>
                    ) : (
                      <span key={i}>{seg.text}</span>
                    ),
                  )}
                </p>

                <div className="mt-7 flex flex-wrap gap-3">
                  {founder.signatures.map((sig) => (
                    <div
                      key={sig.name}
                      className="neo-navy rounded-2xl px-5 py-3"
                    >
                      <p className="font-display text-base font-bold text-cream">
                        {sig.name}
                      </p>
                      <p className="font-caps text-[0.62rem] font-semibold uppercase tracking-[0.1em] text-amber">
                        {sig.role}
                      </p>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>
        </Reveal>
      </div>
    </section>
  );
}
