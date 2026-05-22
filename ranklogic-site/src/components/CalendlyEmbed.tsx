"use client";

import Script from "next/script";
import { site } from "@/lib/site";

/** Inline Calendly scheduler. Script is lazy-loaded to protect page LCP. */
export function CalendlyEmbed() {
  return (
    <>
      <div
        className="calendly-inline-widget overflow-hidden rounded-[28px]"
        data-url={site.calendlyUrl}
        style={{ minWidth: "320px", height: "700px" }}
      />
      <Script
        src="https://assets.calendly.com/assets/external/widget.js"
        strategy="lazyOnload"
      />
      <noscript>
        <a href={site.calendlyUrl} className="font-semibold text-coral-deep">
          Open the scheduler →
        </a>
      </noscript>
    </>
  );
}
