import type { Metadata } from "next";
import { Playfair_Display, Oswald, Inter } from "next/font/google";
import "./globals.css";
import { site } from "@/lib/site";
import { homeGraph } from "@/lib/schema";
import { AnimatedBlobs } from "@/components/ui/AnimatedBlobs";
import { JsonLd } from "@/components/ui/JsonLd";
import { Analytics } from "@/components/Analytics";
import { TopBar } from "@/components/sections/TopBar";
import { Nav } from "@/components/sections/Nav";
import { Footer } from "@/components/sections/Footer";
import { StickyCallBar } from "@/components/sections/StickyCallBar";
import { FloatingWhatsApp } from "@/components/sections/FloatingWhatsApp";

const playfair = Playfair_Display({
  subsets: ["latin"],
  variable: "--font-playfair",
  display: "swap",
  style: ["normal", "italic"],
});

const oswald = Oswald({
  subsets: ["latin"],
  variable: "--font-oswald",
  display: "swap",
});

const inter = Inter({
  subsets: ["latin"],
  variable: "--font-inter",
  display: "swap",
});

export const metadata: Metadata = {
  metadataBase: new URL(site.url),
  title: `${site.name} — South Florida SEO for Home Service Contractors`,
  description:
    "RankLogic SEO gets South Florida roofers, HVAC, plumbers, and home service pros found, chosen, and paid. One client per trade per city. Make more money, get more clients.",
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html
      lang="en"
      className={`${playfair.variable} ${oswald.variable} ${inter.variable}`}
    >
      <body className="flex min-h-screen flex-col">
        <AnimatedBlobs />
        <JsonLd data={homeGraph()} />
        <TopBar />
        <Nav />
        <main className="flex-1">{children}</main>
        <Footer />
        <StickyCallBar />
        <FloatingWhatsApp />
        <Analytics />
      </body>
    </html>
  );
}
