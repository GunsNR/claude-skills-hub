import { steak } from "@/lib/copy";
import { Reveal } from "@/components/ui/Reveal";

export function SteakSection() {
  return (
    <section className="relative py-16 sm:py-20">
      <div className="container-site grid items-center gap-6 lg:grid-cols-[1.05fr_0.95fr]">
        <Reveal>
          <div className="relative h-full overflow-hidden rounded-[32px] bg-navy p-9 sm:p-12">
            <div className="dots-light absolute inset-0" aria-hidden />
            <span
              className="font-display absolute -top-10 left-5 text-[12rem] leading-none text-coral/30"
              aria-hidden
            >
              &ldquo;
            </span>
            <blockquote className="relative font-display text-3xl font-bold leading-[1.18] text-cream sm:text-[2.6rem]">
              {steak.quote.map((seg, i) =>
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
            </blockquote>
            <p className="font-caps relative mt-8 text-xs font-semibold uppercase tracking-[0.16em] text-amber">
              The RankLogic difference
            </p>
          </div>
        </Reveal>

        <div className="grid gap-4">
          {steak.bullets.map((bullet, i) => (
            <Reveal key={bullet.title} delay={i * 0.1}>
              <div className="neo lift rounded-3xl p-6">
                <div className="flex items-start gap-4">
                  <span
                    className="font-display flex h-9 w-9 shrink-0 items-center justify-center rounded-xl text-base font-black text-white"
                    style={{ background: "var(--grad-hot)" }}
                  >
                    {i + 1}
                  </span>
                  <div>
                    <h3 className="font-display text-lg font-bold text-ink">
                      {bullet.title}
                    </h3>
                    <p className="mt-1.5 text-sm leading-relaxed text-ink-soft">
                      {bullet.body}
                    </p>
                  </div>
                </div>
              </div>
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  );
}
