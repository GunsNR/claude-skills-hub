/**
 * Global site configuration. Single source of truth for contact details,
 * URLs, and anything that needs to stay identical across every page.
 *
 * PLACEHOLDERS — replace before launch:
 *  - phoneDisplay / phoneHref: real business number
 *  - calendlyUrl: real Calendly scheduling link
 *  - analyticsId: real GA4 measurement ID
 */
export const site = {
  name: "RankLogic SEO",
  url: "https://ranklogicseo.com",
  tagline: "Make More Money. Get More Clients.",

  // PLACEHOLDER — confirm real number, then this updates every CTA at once.
  phoneDisplay: "(954) 555-0100",
  phoneHref: "tel:+19545550100",

  // PLACEHOLDER — confirm real Calendly link.
  calendlyUrl: "https://calendly.com/ranklogicseo/15min",

  // PLACEHOLDER — confirm real WhatsApp business number (digits only in wa.me).
  whatsapp:
    "https://wa.me/19545550100?text=Hi%20RankLogic%2C%20I%27d%20like%20a%20free%20SEO%20audit.",

  // PLACEHOLDER — confirm GA4 measurement ID (G-XXXXXXXX).
  analyticsId: "",

  email: "izzy@ranklogicseo.com",
  markets: ["Hollywood, FL", "Lakewood, NJ", "Brooklyn, NY"],
} as const;
