import { notFound } from "next/navigation";
import Link from "next/link";
import type { Metadata } from "next";
import { blogPostMap, blogPosts, CATEGORY_LABELS } from "@/lib/blog";
import { BlogThumb } from "@/components/ui/BlogThumb";

interface Props {
  params: Promise<{ slug: string }>;
}

export async function generateStaticParams() {
  return blogPosts.map((p) => ({ slug: p.slug }));
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { slug } = await params;
  const post = blogPostMap[slug];
  if (!post) return {};
  return {
    title: `${post.title} | RankLogic SEO`,
    description: post.excerpt,
  };
}

export default async function BlogPostPage({ params }: Props) {
  const { slug } = await params;
  const post = blogPostMap[slug];
  if (!post) notFound();

  const related = blogPosts
    .filter((p) => p.category === post.category && p.slug !== post.slug)
    .slice(0, 3);

  const formatted = new Date(post.date).toLocaleDateString("en-US", {
    year: "numeric",
    month: "long",
    day: "numeric",
  });

  return (
    <main className="pb-24">
      {/* hero thumbnail */}
      <div className="container-site pt-8">
        <BlogThumb
          category={post.category}
          className="w-full rounded-2xl overflow-hidden"
        />
      </div>

      <article className="container-site mt-10 max-w-3xl">
        {/* meta row */}
        <div className="mb-5 flex items-center gap-3 text-sm text-ink-faint">
          <Link href="/resources" className="hover:text-coral-deep transition-colors">
            ← All guides
          </Link>
          <span>·</span>
          <span className="rounded-full bg-surface px-3 py-1 text-[0.72rem] font-semibold uppercase tracking-[0.07em] text-coral-deep">
            {CATEGORY_LABELS[post.category]}
          </span>
          <span>·</span>
          <time dateTime={post.date}>{formatted}</time>
          <span>·</span>
          <span>{post.readMin} min read</span>
        </div>

        <h1 className="font-display text-[2rem] font-black leading-[1.1] text-ink sm:text-[2.5rem]">
          {post.title}
        </h1>

        <p className="mt-4 text-lg leading-relaxed text-ink-soft">{post.excerpt}</p>

        <hr className="my-8 border-surface" />

        <div className="space-y-6">
          {post.body.map((para, i) => (
            <p key={i} className="text-base leading-[1.75] text-ink-soft sm:text-[1.05rem]">
              {para}
            </p>
          ))}
        </div>

        {/* CTA block */}
        <div className="mt-12 rounded-2xl bg-navy p-8 text-center text-white">
          <p className="font-display text-xl font-bold">
            Ready to put this into practice?
          </p>
          <p className="mt-2 text-sm text-white/70">
            We'll review your site, your GBP, and your top competitors — free, no obligation.
          </p>
          <Link
            href="/audit"
            className="mt-5 inline-flex rounded-full px-6 py-3 text-sm font-semibold text-white shadow-[0_8px_24px_rgba(214,105,63,0.35)] transition-transform hover:-translate-y-0.5"
            style={{ background: "var(--grad-hot)" }}
          >
            Get My Free Audit →
          </Link>
        </div>
      </article>

      {/* related posts */}
      {related.length > 0 && (
        <section className="container-site mt-16 max-w-3xl">
          <h2 className="mb-6 font-display text-xl font-bold text-ink">
            More in {CATEGORY_LABELS[post.category]}
          </h2>
          <div className="grid gap-6 sm:grid-cols-3">
            {related.map((r) => (
              <Link
                key={r.slug}
                href={`/resources/${r.slug}`}
                className="group flex flex-col overflow-hidden rounded-xl bg-bg-raised shadow-[0_2px_12px_rgba(0,0,0,0.06)] transition-transform hover:-translate-y-0.5"
              >
                <BlogThumb category={r.category} />
                <div className="p-4">
                  <p className="font-display text-sm font-bold leading-snug text-ink transition-colors group-hover:text-coral-deep">
                    {r.title}
                  </p>
                  <p className="mt-1 text-[0.72rem] font-semibold text-coral-deep">
                    Read →
                  </p>
                </div>
              </Link>
            ))}
          </div>
        </section>
      )}
    </main>
  );
}
