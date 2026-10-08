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
          {pricingTiers.map((tier, i) => {
            const dark = tier.featured;
            return (
              <Reveal key={tier.id} delay={i * 0.1}>
                <div
                  className={cn(
                    "relative flex h-full flex-col overflow-hidden rounded-[28px] p-7 sm:p-8",
                    dark
                      ? "bg-navy lg:scale-[1.05]"
                      : "neo lift",
                  )}
                >
                  {dark && (
                    <div className="dots-light absolute inset-0" aria-hidden />
                  )}
                  {tier.ribbon && (
                    <span
                      className="font-caps absolute -top-3.5 left-1/2 z-10 -translate-x-1/2 rounded-full px-4 py-1.5 text-[0.66rem] font-bold uppercase tracking-[0.1em] text-navy-deep shadow-[0_8px_20px_rgba(253,137,115,0.45)]"
                      style={{ background: "var(--grad-warm)" }}
                    >
                      {tier.ribbon}
                    </span>
                  )}

                  <div className="relative flex flex-1 flex-col">
                    <p
                      className={cn(
                        "font-caps text-sm font-semibold uppercase tracking-[0.14em]",
                        dark ? "text-amber" : "text-ink-faint",
                      )}
                    >
                      {tier.name}
                    </p>

                    <div className="mt-3 flex items-baseline gap-1.5">
                      <span className="font-display text-5xl font-black">
                        {dark ? (
                          <span className="text-cream">{tier.amount}</span>
                        ) : (
                          <GradientText>{tier.amount}</GradientText>
                        )}
                      </span>
                      <span
                        className={cn(
                          "font-caps text-sm font-semibold uppercase",
                          dark ? "text-cream/55" : "text-ink-faint",
                        )}
                      >
                        / mo
                      </span>
                    </div>
                    <p
                      className={cn(
                        "mt-2 min-h-[2.5rem] text-sm leading-snug",
                        dark ? "text-cream/75" : "text-ink-soft",
                      )}
                    >
                      {tier.amountSub}
                    </p>

                    <span
                      className={cn(
                        "font-caps mt-4 inline-flex self-start rounded-full px-3 py-1 text-[0.66rem] font-bold uppercase tracking-[0.08em]",
                        dark
                          ? "bg-white/12 text-cream"
                          : "bg-mist text-ink-soft",
                      )}
                    >
                      Best for: {tier.bestFor}
                    </span>

                    <ul
                      className={cn(
                        "mt-6 space-y-3 border-t pt-6",
                        dark ? "border-white/15" : "border-ink/10",
                      )}
                    >
                      {tier.features.map((f) => (
                        <li
                          key={f.label}
                          className={cn(
                            "flex items-start gap-2.5 text-sm",
                            f.included
                              ? dark
                                ? "text-cream"
                                : "text-ink"
                              : dark
                                ? "text-cream/40"
                                : "text-ink-faint/70",
                          )}
                        >
                          {f.included ? (
                            <span className="mt-0.5 flex h-4.5 w-4.5 shrink-0 items-center justify-center rounded-full bg-coral text-navy-deep">
                              <Check size={11} strokeWidth={3.5} />
                            </span>
                          ) : (
                            <span
                              className={cn(
                                "mt-0.5 flex h-4.5 w-4.5 shrink-0 items-center justify-center rounded-full",
                                dark
                                  ? "bg-white/10 text-cream/45"
                                  : "bg-ink-faint/15 text-ink-faint",
                              )}
                            >
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
                        dark
                          ? "text-navy-deep shadow-[0_12px_30px_rgba(253,137,115,0.4)]"
                          : "neo-sm text-coral-deep",
                      )}
                      style={
                        dark ? { background: "var(--grad-warm)" } : undefined
                      }
                    >
                      Start with {tier.name} →
                    </Link>
                  </div>
                </div>
              </Reveal>
            );
          })}
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
