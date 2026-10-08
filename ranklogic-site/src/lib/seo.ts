import type { Metadata } from "next";
import { site } from "./site";

export interface PageMeta {
  title: string;
  description: string;
  path: string;
  image?: string;
}

/** Builds a consistent Metadata object for every page. */
export function generatePageMeta({
  title,
  description,
  path,
  image,
}: PageMeta): Metadata {
  const url = `${site.url}${path}`;
  const ogImage = image || "/og-default.svg";

  return {
    title: `${title} | ${site.name}`,
    description,
    alternates: { canonical: url },
    openGraph: {
      title: `${title} | ${site.name}`,
      description,
      url,
      siteName: site.name,
      type: "website",
      images: [{ url: ogImage, width: 1200, height: 630, alt: title }],
    },
    twitter: {
      card: "summary_large_image",
      title: `${title} | ${site.name}`,
      description,
      images: [ogImage],
    },
  };
}
