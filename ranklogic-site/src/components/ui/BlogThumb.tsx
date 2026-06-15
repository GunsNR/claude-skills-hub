import type { BlogCategory } from "@/lib/blog";
import { CATEGORY_LABELS } from "@/lib/blog";

const CATEGORY_COLORS: Record<BlogCategory, { chip: string; fallback: string }> = {
  "local-seo": { chip: "#fd8973", fallback: "linear-gradient(135deg,#003a6c,#001020)" },
  gbp:         { chip: "#ffbf65", fallback: "linear-gradient(135deg,#054f50,#011e1f)" },
  reviews:     { chip: "#fd8973", fallback: "linear-gradient(135deg,#38106a,#120523)" },
  content:     { chip: "#ffbf65", fallback: "linear-gradient(135deg,#154d2f,#062015)" },
  strategy:    { chip: "#ffbf65", fallback: "linear-gradient(135deg,#121624,#060810)" },
  trade:       { chip: "#ffbf65", fallback: "linear-gradient(135deg,#7a3308,#2e1203)" },
};

export function BlogThumb({
  category,
  photo,
  alt = "",
  className = "",
}: {
  category: BlogCategory;
  photo?: string;
  alt?: string;
  className?: string;
}) {
  const { chip, fallback } = CATEGORY_COLORS[category];
  const label = CATEGORY_LABELS[category];

  return (
    <div
      className={`relative overflow-hidden ${className}`}
      style={{ aspectRatio: "16/9", background: fallback }}
    >
      {photo && (
        // eslint-disable-next-line @next/next/no-img-element
        <img
          src={photo}
          alt={alt}
          className="absolute inset-0 h-full w-full object-cover"
          loading="lazy"
        />
      )}

      {/* bottom gradient so category chip is readable on any photo */}
      <div
        className="absolute inset-0"
        style={{
          background:
            "linear-gradient(to bottom, rgba(0,0,0,0.18) 0%, transparent 40%, rgba(0,0,0,0.42) 100%)",
        }}
      />

      {/* category chip */}
      <span
        className="absolute left-3 top-3 rounded-full px-3 py-1 text-[0.68rem] font-bold uppercase tracking-[0.08em] text-ink shadow-sm"
        style={{ background: chip }}
      >
        {label}
      </span>
    </div>
  );
}
