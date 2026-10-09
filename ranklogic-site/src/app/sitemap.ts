import type { MetadataRoute } from "next";
import { site } from "@/lib/site";
import { trades } from "@/lib/trades";
import { caseStudyList } from "@/lib/clients";
import { blogPosts } from "@/lib/blog";

/** XML sitemap. /book is intentionally excluded (low SEO value, scheduler page). */
export default function sitemap(): MetadataRoute.Sitemap {
  const now = new Date();

  const core = ["/", "/pricing", "/about", "/audit"].map((path) => ({
    url: `${site.url}${path}`,
    lastModified: now,
    changeFrequency: "weekly" as const,
    priority: path === "/" ? 1 : 0.8,
  }));

  const tradePages = trades.map((t) => ({
    url: `${site.url}/${t.slug}`,
    lastModified: now,
    changeFrequency: "weekly" as const,
    priority: 0.9,
  }));

  const caseStudyPages = caseStudyList.map((cs) => ({
    url: `${site.url}/case-studies/${cs.slug}`,
    lastModified: now,
    changeFrequency: "monthly" as const,
    priority: 0.7,
  }));

  const blogHub = [{
    url: `${site.url}/resources`,
    lastModified: now,
    changeFrequency: "weekly" as const,
    priority: 0.8,
  }];

  const blogPages = blogPosts.map((p) => ({
    url: `${site.url}/resources/${p.slug}`,
    lastModified: new Date(p.date),
    changeFrequency: "monthly" as const,
    priority: 0.7,
  }));

  return [...core, ...tradePages, ...caseStudyPages, ...blogHub, ...blogPages];
}
