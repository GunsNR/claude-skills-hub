import Script from "next/script";
import { site } from "@/lib/site";

/**
 * GA4 analytics stub. Renders nothing until a real measurement ID is set
 * in src/lib/site.ts (analyticsId). Loaded lazily to protect LCP.
 */
export function Analytics() {
  if (!site.analyticsId) return null;

  return (
    <>
      <Script
        src={`https://www.googletagmanager.com/gtag/js?id=${site.analyticsId}`}
        strategy="lazyOnload"
      />
      <Script id="ga4-init" strategy="lazyOnload">
        {`window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','${site.analyticsId}');`}
      </Script>
    </>
  );
}
