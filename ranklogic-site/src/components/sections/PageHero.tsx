import type { Rich } from "@/lib/copy";
import { Reveal } from "@/components/ui/Reveal";
import { RichText } from "@/components/ui/RichText";
import { PillBadge } from "@/components/ui/PillBadge";

export function PageHero({
  kicker,
  h1,
  sub,
  children,
}: {
  kicker: string;
  h1: Rich;
  sub: string;
  children?: React.ReactNode;
}) {
  return (
    <section className="relative pt-10 pb-8 sm:pt-14">
      <div className="container-site flex flex-col items-center text-center">
        <Reveal>
          <PillBadge>{kicker}</PillBadge>
        </Reveal>
        <Reveal delay={0.08}>
          <h1 className="mt-5 max-w-4xl font-display text-[2.4rem] font-black leading-[1.07] text-ink sm:text-5xl lg:text-[3.3rem]">
            <RichText value={h1} />
          </h1>
        </Reveal>
        <Reveal delay={0.16}>
          <p className="mt-5 max-w-2xl text-base leading-relaxed text-ink-soft sm:text-lg">
            {sub}
          </p>
        </Reveal>
        {children && (
          <Reveal delay={0.24}>
            <div className="mt-8">{children}</div>
          </Reveal>
        )}
      </div>
    </section>
  );
}
