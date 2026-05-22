import Link from "next/link";
import { Check, Minus } from "lucide-react";
import { pricingTiers, pricingNote } from "@/lib/pricing";
import { pricingSection } from "@/lib/copy";
import { cn } from "@/lib/utils";
import { Reveal } from "@/components/ui/Reveal";
import { RichText } from "@/components/ui/RichText";
import { GradientText } from "@/components/ui/GradientText";
import { PillBadge } from "@/components/ui/PillBadge";

export function PricingGrid({ showHeading = true }: { showHeading?: boolean }) {
  return (
    <section id="pricing" className="relative scroll-mt-28 py-16 sm:py-20">
      <div className="container-site">
        {showHeading && (
          <Reveal className="flex flex-col items-center text-center">
            <PillBadge>Pricing</PillBadge>
            <h2 className="mt-5 max-w-3xl font-display text-3xl font-black leading-tight text-ink sm:text-[2.7rem]">
              <RichText value={pricingSection.h2} />
            </h2>
            <p className="mt-4 max-w-2xl text-base text-ink-soft sm:text-lg">
              {pricingSection.sub}
            </p>
          </Reveal>
        )}

        <div className="mt-14 grid items-center gap-6 lg:grid-cols-3">
          {pricingTiers.map((tier, i) => (
            <Reveal key={tier.id} delay={i * 0.1}>
              <div
                className={cn(
                  "relative flex h-full flex-col rounded-[28px] p-7 sm:p-8",
                  tier.featured
                    ? "glass ring-2 ring-coral/60 lg:scale-[1.04]"
                    : "neo lift",
                )}
              >
                {tier.ribbon && (
                  <span
                    className="font-caps absolute -top-3.5 left-1/2 -translate-x-1/2 rounded-full px-4 py-1.5 text-[0.66rem] font-bold uppercase tracking-[0.1em] text-white shadow-[0_8px_20px_rgba(255,107,157,0.4)]"
                    style={{ background: "var(--grad-hot)" }}
                  >
                    {tier.ribbon}
                  </span>
                )}

                <p className="font-caps text-sm font-semibold uppercase tracking-[0.14em] text-ink-faint">
                  {tier.name}
                </p>

                <div className="mt-3 flex items-baseline gap-1.5">
                  <span className="font-display text-5xl font-black">
                    <GradientText>{tier.amount}</GradientText>
                  </span>
                  <span className="font-caps text-sm font-semibold uppercase text-ink-faint">
                    / mo
                  </span>
                </div>
                <p className="mt-2 min-h-[2.5rem] text-sm leading-snug text-ink-soft">
                  {tier.amountSub}
                </p>

                <span className="font-caps mt-4 inline-flex self-start rounded-full bg-aqua/20 px-3 py-1 text-[0.66rem] font-bold uppercase tracking-[0.08em] text-ink-soft">
                  Best for: {tier.bestFor}
                </span>

                <ul className="mt-6 space-y-3 border-t border-white/70 pt-6">
                  {tier.features.map((f) => (
                    <li
                      key={f.label}
                      className={cn(
                        "flex items-start gap-2.5 text-sm",
                        f.included ? "text-ink" : "text-ink-faint/70",
                      )}
                    >
                      {f.included ? (
                        <span
                          className="mt-0.5 flex h-4.5 w-4.5 shrink-0 items-center justify-center rounded-full text-white"
                          style={{ background: "var(--grad-hot)" }}
                        >
                          <Check size={11} strokeWidth={3.5} />
                        </span>
                      ) : (
                        <span className="mt-0.5 flex h-4.5 w-4.5 shrink-0 items-center justify-center rounded-full bg-ink-faint/15 text-ink-faint">
                          <Minus size={11} strokeWidth={3} />
                        </span>
                      )}
                      <span>{f.label}</span>
                    </li>
                  ))}
                </ul>

                <Link
                  href="/audit"
                  className={cn(
                    "font-caps mt-7 flex items-center justify-center rounded-full py-3.5 text-[0.82rem] font-semibold uppercase tracking-[0.06em] transition-transform hover:-translate-y-0.5",
                    tier.featured
                      ? "text-white shadow-[0_12px_32px_rgba(214,105,63,0.35)]"
                      : "neo-sm text-coral-deep",
                  )}
                  style={
                    tier.featured
                      ? { background: "var(--grad-hot)" }
                      : undefined
                  }
                >
                  Start with {tier.name} →
                </Link>
              </div>
            </Reveal>
          ))}
        </div>

        <Reveal delay={0.1}>
          <p className="mx-auto mt-10 max-w-2xl text-center text-sm text-ink-soft">
            {pricingNote.split("Auto-grandfathered").map((part, i) =>
              i === 0 ? (
                <span key={i}>{part}</span>
              ) : (
                <span key={i}>
                  <strong className="text-ink">Auto-grandfathered</strong>
                  {part}
                </span>
              ),
            )}
          </p>
        </Reveal>
      </div>
    </section>
  );
}
