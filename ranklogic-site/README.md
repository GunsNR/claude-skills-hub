# RankLogic SEO — Website

Production website for **RankLogic SEO**, South Florida's SEO agency for
high-end home service contractors (roofing, HVAC, plumbing, pool,
restoration, electrical).

Design direction: **Liquid Glass Neomorphism — Miami high-end construction.**

## Stack

- **Next.js 16** (App Router) + **React 19** + **TypeScript**
- **Tailwind CSS v4** (CSS-first `@theme` config)
- **Framer Motion** — scroll-triggered entrance animations
- **Radix UI** — accessible FAQ accordion
- **lucide-react** — icons

## Getting started

```bash
npm install
npm run dev      # http://localhost:3000
npm run build    # production build
npm start        # serve the production build
npm run lint     # ESLint
```

## Architecture

```
src/
  app/                  Routes (App Router)
    page.tsx            Homepage
    pricing/            3-tier pricing page
    about/              Founder story
    audit/              Free audit conversion page
    book/               Calendly scheduler
    case-studies/[slug] Dynamic case study pages
    [service]/          Flat trade pages (/seo-for-roofers, …)
    api/lead/           Lead intake endpoint
    sitemap.ts robots.ts
  components/
    ui/                 Button, GlassCard, NeoCard, GradientText, etc.
    sections/           Page sections (Hero, PricingGrid, Footer, …)
  lib/
    copy.ts             Single source of truth for ALL page copy
    site.ts             Contact details + global config (placeholders)
    clients.ts          Client + case study data
    pricing.ts          Pricing tier data
    trades.ts           Trade (service) page data
    seo.ts              generatePageMeta() metadata factory
    schema.ts           JSON-LD builders (Organization, Service, FAQ, …)
  styles/
    tokens.css          Design tokens (also the Bricks Builder handoff file)
```

All user-facing copy lives in `src/lib/copy.ts`. Contact details
(phone, Calendly, analytics) live in `src/lib/site.ts`.

## Launch blockers

These are placeholders — replace before going live. Each is centralized,
so a single edit updates the whole site.

| Item | Where |
| --- | --- |
| Real phone number | `src/lib/site.ts` → `phoneDisplay` / `phoneHref` |
| Calendly URL | `src/lib/site.ts` → `calendlyUrl` |
| Google Analytics ID | `src/lib/site.ts` → `analyticsId` |
| Lead form delivery (email/CRM) | `src/app/api/lead/route.ts` |
| Founder photo (Izzy + Dilshan) | `FounderSection.tsx` gradient block |
| Client logos (Wayne's, AtlasCare, Toothology, Stageitus) | `ProofStrip.tsx` |
| OG share image | `public/og-default.svg` (replace with 1200×630) |
| Production domain | `src/lib/site.ts` → `url` |
