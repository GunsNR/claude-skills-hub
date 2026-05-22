import { pain } from "@/lib/copy";
import { Reveal } from "@/components/ui/Reveal";
import { RichText } from "@/components/ui/RichText";
import { PillBadge } from "@/components/ui/PillBadge";

export function PainBlock() {
  return (
    <section className="relative py-16 sm:py-20">
      <div className="container-site">
        <Reveal className="flex flex-col items-center text-center">
          <PillBadge>{pain.pill}</PillBadge>
          <h2 className="mt-5 max-w-3xl font-display text-3xl font-black leading-tight text-ink sm:text-[2.7rem]">
            <RichText value={pain.h2} />
          </h2>
          <p className="mt-4 max-w-xl text-base text-ink-soft sm:text-lg">
            {pain.sub}
          </p>
        </Reveal>

        <div className="mt-12 grid gap-5 md:grid-cols-3">
          {pain.cards.map((card, i) => (
            <Reveal key={card.tag} delay={i * 0.1}>
              <div className="neo lift flex h-full flex-col rounded-3xl p-7">
                <span className="font-caps inline-flex self-start rounded-full bg-coral/15 px-3 py-1 text-[0.68rem] font-bold uppercase tracking-[0.1em] text-coral-deep">
                  {card.tag}
                </span>
                <p className="mt-5 text-[0.98rem] font-medium leading-relaxed text-ink">
                  {card.problem}
                </p>
                <div className="mt-5 flex items-start gap-2.5 border-t border-ink/10 pt-5">
                  <span
                    className="mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded-full text-[0.7rem] font-black text-white"
                    style={{ background: "var(--grad-hot)" }}
                    aria-hidden
                  >
                    ✓
                  </span>
                  <p className="text-sm leading-relaxed text-ink-soft">
                    {card.fix}
                  </p>
                </div>
              </div>
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  );
}
