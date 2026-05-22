import { Check } from "lucide-react";
import { generatePageMeta } from "@/lib/seo";
import { breadcrumbGraph } from "@/lib/schema";
import { bookPage } from "@/lib/copy";
import { site } from "@/lib/site";
import { JsonLd } from "@/components/ui/JsonLd";
import { PageHero } from "@/components/sections/PageHero";
import { CalendlyEmbed } from "@/components/CalendlyEmbed";
import { Reveal } from "@/components/ui/Reveal";

export const metadata = generatePageMeta({
  title: "Book a 15-Minute Call",
  description:
    "Book a free 15-minute call with RankLogic SEO. We'll talk through your market, your competitors, and whether we're the right fit — zero hard sell.",
  path: "/book",
});

export default function BookPage() {
  return (
    <>
      <JsonLd
        data={breadcrumbGraph([
          { name: "Home", path: "/" },
          { name: "Book a Call", path: "/book" },
        ])}
      />
      <PageHero kicker={bookPage.kicker} h1={bookPage.h1} sub={bookPage.sub} />

      <section className="relative py-8">
        <div className="container-site grid items-start gap-8 lg:grid-cols-[0.78fr_1.22fr]">
          <Reveal>
            <div className="neo rounded-3xl p-7">
              <p className="font-caps text-xs font-semibold uppercase tracking-[0.14em] text-ink-faint">
                What to expect
              </p>
              <ul className="mt-4 space-y-3">
                {bookPage.expectations.map((item) => (
                  <li key={item} className="flex items-start gap-3">
                    <span
                      className="mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded-full text-white"
                      style={{ background: "var(--grad-hot)" }}
                    >
                      <Check size={12} strokeWidth={3.5} />
                    </span>
                    <span className="text-sm leading-relaxed text-ink">
                      {item}
                    </span>
                  </li>
                ))}
              </ul>
              <div className="mt-6 border-t border-ink/10 pt-5">
                <p className="text-sm text-ink-soft">
                  Rather just call?
                </p>
                <a
                  href={site.phoneHref}
                  className="font-display mt-1 inline-block text-2xl font-black text-coral-deep"
                >
                  {site.phoneDisplay}
                </a>
              </div>
            </div>
          </Reveal>

          <Reveal delay={0.12}>
            <div className="glass rounded-[32px] p-3 sm:p-4">
              <CalendlyEmbed />
            </div>
          </Reveal>
        </div>
      </section>
    </>
  );
}
