"use client";

import * as Accordion from "@radix-ui/react-accordion";
import { ChevronDown } from "lucide-react";
import { faq } from "@/lib/copy";
import { Reveal } from "@/components/ui/Reveal";
import { PillBadge } from "@/components/ui/PillBadge";

export function FAQAccordion({
  showHeading = true,
}: {
  showHeading?: boolean;
}) {
  return (
    <section id="faq" className="relative scroll-mt-28 py-16 sm:py-20">
      <div className="container-site">
        {showHeading && (
          <Reveal className="flex flex-col items-center text-center">
            <PillBadge>{faq.pill}</PillBadge>
            <h2 className="mt-5 max-w-2xl font-display text-3xl font-black leading-tight text-ink sm:text-[2.7rem]">
              {faq.heading}
            </h2>
          </Reveal>
        )}

        <Reveal delay={0.08}>
          <Accordion.Root
            type="single"
            collapsible
            className="mx-auto mt-10 max-w-3xl space-y-3"
          >
            {faq.items.map((item, i) => (
              <Accordion.Item
                key={i}
                value={`item-${i}`}
                className="neo faq-item overflow-hidden rounded-2xl"
              >
                <Accordion.Header>
                  <Accordion.Trigger className="group flex w-full items-center justify-between gap-4 px-6 py-5 text-left">
                    <span className="font-display text-[1.02rem] font-bold text-ink">
                      {item.q}
                    </span>
                    <span
                      className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full text-white"
                      style={{ background: "var(--grad-hot)" }}
                    >
                      <ChevronDown size={16} className="acc-chevron" />
                    </span>
                  </Accordion.Trigger>
                </Accordion.Header>
                <Accordion.Content className="acc-content">
                  <p className="px-6 pb-5 text-sm leading-relaxed text-ink-soft">
                    {item.a}
                  </p>
                </Accordion.Content>
              </Accordion.Item>
            ))}
          </Accordion.Root>
        </Reveal>
      </div>
    </section>
  );
}
