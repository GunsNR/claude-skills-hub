import { Check } from "lucide-react";
import { generatePageMeta } from "@/lib/seo";
import { breadcrumbGraph } from "@/lib/schema";
import { auditPage } from "@/lib/copy";
import { site } from "@/lib/site";
import { JsonLd } from "@/components/ui/JsonLd";
import { AuditForm } from "@/components/AuditForm";
import { HowItWorks } from "@/components/sections/HowItWorks";
import { Reveal } from "@/components/ui/Reveal";
import { RichText } from "@/components/ui/RichText";
import { PillBadge } from "@/components/ui/PillBadge";

export const metadata = generatePageMeta({
  title: "Free SEO Audit",
  description:
    "Get a free, no-BS SEO audit of your home service business. We review your site, your Google Business Profile, and your top 3 competitors — written report in 48 hours.",
  path: "/audit",
});

export default function AuditPage() {
  return (
    <>
      <JsonLd
        data={breadcrumbGraph([
          { name: "Home", path: "/" },
          { name: "Free Audit", path: "/audit" },
        ])}
      />

      <section className="relative pt-10 pb-12 sm:pt-14">
        <div className="container-site grid items-start gap-12 lg:grid-cols-[1.05fr_0.95fr]">
          <div>
            <Reveal>
              <PillBadge>{auditPage.kicker}</PillBadge>
            </Reveal>
            <Reveal delay={0.08}>
              <h1 className="mt-5 font-display text-[2.4rem] font-black leading-[1.07] text-ink sm:text-5xl lg:text-[3.1rem]">
                <RichText value={auditPage.h1} />
              </h1>
            </Reveal>
            <Reveal delay={0.16}>
              <p className="mt-5 max-w-xl text-base leading-relaxed text-ink-soft sm:text-lg">
                {auditPage.sub}
              </p>
            </Reveal>
            <Reveal delay={0.24}>
              <div className="neo mt-8 rounded-3xl p-7">
                <p className="font-caps text-xs font-semibold uppercase tracking-[0.14em] text-ink-faint">
                  What you get
                </p>
                <ul className="mt-4 space-y-3">
                  {auditPage.checklist.map((item) => (
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
              </div>
            </Reveal>
            <Reveal delay={0.32}>
              <p className="mt-6 text-sm text-ink-soft">
                Prefer to talk?{" "}
                <a
                  href={site.phoneHref}
                  className="font-display text-lg font-bold text-coral-deep"
                >
                  {site.phoneDisplay}
                </a>{" "}
                — Izzy answers.
              </p>
            </Reveal>
          </div>

          <Reveal delay={0.18}>
            <AuditForm
              badge={auditPage.form.badge}
              heading={auditPage.form.heading}
              cta={auditPage.form.cta}
              finePrint={auditPage.form.finePrint}
            />
          </Reveal>
        </div>
      </section>

      <HowItWorks />
    </>
  );
}
