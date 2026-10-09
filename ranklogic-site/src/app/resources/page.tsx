import Link from "next/link";
import { blogPosts, blogPhotoUrls, CATEGORY_LABELS } from "@/lib/blog";
import { BlogThumb } from "@/components/ui/BlogThumb";
import { PageHero } from "@/components/sections/PageHero";
import { Reveal } from "@/components/ui/Reveal";

export const metadata = {
  title: "Resources & Guides | RankLogic SEO",
  description:
    "Practical local SEO guides for roofers, HVAC, plumbers, and home service contractors. No fluff — just what actually moves the needle.",
};

const resourcesHero = {
  kicker: "Resources",
  h1: [
    { text: "Guides that " },
    { text: "actually work.", em: true },
  ] as import("@/lib/copy").Rich,
  sub: "Practical local SEO strategy for home service contractors — written by people who do this every day, not content farms.",
};

export default function ResourcesPage() {
  return (
    <main>
      <PageHero
        kicker={resourcesHero.kicker}
        h1={resourcesHero.h1}
        sub={resourcesHero.sub}
      />

      <section className="container-site pb-20 pt-4">
        <Reveal>
          <div className="grid gap-8 sm:grid-cols-2 lg:grid-cols-3">
            {blogPosts.map((post, i) => (
              <Reveal key={post.slug} delay={Math.min(i * 0.04, 0.3)}>
                <Link
                  href={`/resources/${post.slug}`}
                  className="group flex flex-col overflow-hidden rounded-2xl bg-bg-raised shadow-[0_2px_16px_rgba(0,0,0,0.07)] transition-transform duration-300 hover:-translate-y-1"
                >
                  <BlogThumb
                    category={post.category}
                    photo={blogPhotoUrls[post.slug]}
                    alt={post.title}
                  />

                  <div className="flex flex-1 flex-col gap-3 p-5">
                    <div className="flex items-center justify-between">
                      <span className="eyebrow rounded-full bg-surface px-3 py-1 text-[0.68rem] font-semibold uppercase tracking-[0.07em] text-coral-deep">
                        {CATEGORY_LABELS[post.category]}
                      </span>
                      <span className="text-[0.72rem] text-ink-faint">
                        {post.readMin} min read
                      </span>
                    </div>

                    <h2 className="font-display text-[1.05rem] font-bold leading-snug text-ink transition-colors group-hover:text-coral-deep">
                      {post.title}
                    </h2>

                    <p className="line-clamp-3 flex-1 text-sm leading-relaxed text-ink-soft">
                      {post.excerpt}
                    </p>

                    <span className="mt-1 inline-flex items-center gap-1 text-[0.8rem] font-semibold text-coral-deep">
                      Read the guide
                      <svg
                        className="transition-transform group-hover:translate-x-0.5"
                        width="14"
                        height="14"
                        viewBox="0 0 14 14"
                        fill="none"
                      >
                        <path
                          d="M2.5 7h9M8 3.5 11.5 7 8 10.5"
                          stroke="currentColor"
                          strokeWidth="1.5"
                          strokeLinecap="round"
                          strokeLinejoin="round"
                        />
                      </svg>
                    </span>
                  </div>
                </Link>
              </Reveal>
            ))}
          </div>
        </Reveal>
      </section>
    </main>
  );
}
