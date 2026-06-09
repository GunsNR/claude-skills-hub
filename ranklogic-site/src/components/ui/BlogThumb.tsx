import type { BlogCategory } from "@/lib/blog";
import { CATEGORY_LABELS } from "@/lib/blog";

const DESIGNS: Record<
  BlogCategory,
  { g0: string; g1: string; accent: string; pattern: React.ReactNode }
> = {
  "local-seo": {
    g0: "#003a6c",
    g1: "#001020",
    accent: "#fd8973",
    pattern: (
      <>
        {/* radiating arcs from bottom-right — "signal" motif */}
        {[90, 175, 260, 345, 430, 515].map((r, i) => (
          <circle
            key={i}
            cx="800"
            cy="450"
            r={r}
            fill="none"
            stroke="#fd8973"
            strokeWidth="1.2"
            opacity={0.12 + i * 0.02}
          />
        ))}
        {/* map-pin silhouette top-left */}
        <ellipse cx="130" cy="95" rx="38" ry="38" fill="#fd8973" opacity="0.11" />
        <path
          d="M130 133 L108 175 L152 175 Z"
          fill="#fd8973"
          opacity="0.11"
        />
        {/* horizontal rule accent */}
        <rect x="0" y="440" width="800" height="6" fill="#fd8973" opacity="0.55" />
      </>
    ),
  },

  gbp: {
    g0: "#054f50",
    g1: "#011e1f",
    accent: "#ffbf65",
    pattern: (
      <>
        {/* 5 stars centred mid-image */}
        {[0, 1, 2, 3, 4].map((i) => {
          const cx = 200 + i * 100;
          const cy = 200;
          const r = 36;
          const pts = Array.from({ length: 5 }, (_, k) => {
            const outer = (k * 72 - 90) * (Math.PI / 180);
            const inner = (k * 72 - 90 + 36) * (Math.PI / 180);
            return `${cx + r * Math.cos(outer)},${cy + r * Math.sin(outer)} ${cx + (r * 0.4) * Math.cos(inner)},${cy + (r * 0.4) * Math.sin(inner)}`;
          }).join(" ");
          return (
            <polygon
              key={i}
              points={pts}
              fill="#ffbf65"
              opacity="0.18"
            />
          );
        })}
        {/* scattered small stars */}
        {[[650, 80], [720, 340], [60, 320], [400, 380], [550, 60]].map(
          ([sx, sy], i) => {
            const r2 = 14;
            const pts2 = Array.from({ length: 5 }, (_, k) => {
              const outer = (k * 72 - 90) * (Math.PI / 180);
              const inner = (k * 72 - 90 + 36) * (Math.PI / 180);
              return `${sx + r2 * Math.cos(outer)},${sy + r2 * Math.sin(outer)} ${sx + r2 * 0.4 * Math.cos(inner)},${sy + r2 * 0.4 * Math.sin(inner)}`;
            }).join(" ");
            return (
              <polygon key={i} points={pts2} fill="#ffbf65" opacity="0.25" />
            );
          }
        )}
        <rect x="0" y="440" width="800" height="6" fill="#ffbf65" opacity="0.55" />
      </>
    ),
  },

  reviews: {
    g0: "#38106a",
    g1: "#120523",
    accent: "#fd8973",
    pattern: (
      <>
        {/* speech-bubble outlines */}
        <rect x="60" y="60" width="260" height="170" rx="22" fill="none" stroke="#fd8973" strokeWidth="2" opacity="0.18" />
        <path d="M90 230 L70 280 L140 230 Z" fill="none" stroke="#fd8973" strokeWidth="2" opacity="0.18" />
        <rect x="380" y="140" width="200" height="130" rx="18" fill="none" stroke="#fd8973" strokeWidth="2" opacity="0.14" />
        <path d="M400 270 L385 308 L450 270 Z" fill="none" stroke="#fd8973" strokeWidth="1.5" opacity="0.14" />
        {/* dot clusters — review stars hint */}
        {[0, 1, 2, 3, 4].map((i) => (
          <circle key={i} cx={130 + i * 40} cy={145} r="8" fill="#fd8973" opacity="0.22" />
        ))}
        <rect x="0" y="440" width="800" height="6" fill="#fd8973" opacity="0.55" />
      </>
    ),
  },

  content: {
    g0: "#154d2f",
    g1: "#062015",
    accent: "#ffbf65",
    pattern: (
      <>
        {/* diagonal ruled lines — "notebook paper" */}
        {Array.from({ length: 14 }, (_, i) => {
          const offset = i * 70;
          return (
            <line
              key={i}
              x1={offset - 200}
              y1={0}
              x2={offset + 250}
              y2={450}
              stroke="#ffbf65"
              strokeWidth="1"
              opacity="0.12"
            />
          );
        })}
        {/* pen-nib icon top-right */}
        <path
          d="M680 50 L760 90 L720 180 L660 160 Z"
          fill="#ffbf65"
          opacity="0.12"
        />
        <line x1="700" y1="100" x2="680" y2="200" stroke="#ffbf65" strokeWidth="2" opacity="0.18" />
        <rect x="0" y="440" width="800" height="6" fill="#ffbf65" opacity="0.55" />
      </>
    ),
  },

  strategy: {
    g0: "#121624",
    g1: "#060810",
    accent: "#ffbf65",
    pattern: (
      <>
        {/* dot grid */}
        {Array.from({ length: 10 }, (_, col) =>
          Array.from({ length: 6 }, (_, row) => (
            <circle
              key={`${col}-${row}`}
              cx={60 + col * 76}
              cy={55 + row * 72}
              r="3"
              fill="#ffbf65"
              opacity="0.18"
            />
          ))
        )}
        {/* ascending trend line */}
        <polyline
          points="80,370 200,310 340,260 460,190 580,140 720,80"
          fill="none"
          stroke="#ffbf65"
          strokeWidth="3"
          opacity="0.28"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
        {/* data points on the trend */}
        {[[80,370],[200,310],[340,260],[460,190],[580,140],[720,80]].map(([px, py], i) => (
          <circle key={i} cx={px} cy={py} r="6" fill="#ffbf65" opacity="0.4" />
        ))}
        <rect x="0" y="440" width="800" height="6" fill="#ffbf65" opacity="0.55" />
      </>
    ),
  },

  trade: {
    g0: "#7a3308",
    g1: "#2e1203",
    accent: "#ffbf65",
    pattern: (
      <>
        {/* hex grid (offset rows) */}
        {[0, 1, 2, 3].map((row) =>
          [0, 1, 2, 3, 4].map((col) => {
            const hx = 90 + col * 152 + (row % 2) * 76;
            const hy = 80 + row * 110;
            const r = 52;
            const pts = Array.from({ length: 6 }, (_, k) => {
              const angle = (k * 60 - 30) * (Math.PI / 180);
              return `${hx + r * Math.cos(angle)},${hy + r * Math.sin(angle)}`;
            }).join(" ");
            return (
              <polygon
                key={`${row}-${col}`}
                points={pts}
                fill="none"
                stroke="#ffbf65"
                strokeWidth="1.2"
                opacity="0.2"
              />
            );
          })
        )}
        <rect x="0" y="440" width="800" height="6" fill="#ffbf65" opacity="0.55" />
      </>
    ),
  },
};

export function BlogThumb({
  category,
  className = "",
}: {
  category: BlogCategory;
  className?: string;
}) {
  const { g0, g1, accent, pattern } = DESIGNS[category];
  const uid = `bg-${category}`;

  return (
    <div
      className={`relative overflow-hidden ${className}`}
      style={{ aspectRatio: "16/9" }}
    >
      <svg
        viewBox="0 0 800 450"
        xmlns="http://www.w3.org/2000/svg"
        className="absolute inset-0 w-full h-full"
        aria-hidden="true"
      >
        <defs>
          <linearGradient id={uid} x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stopColor={g0} />
            <stop offset="100%" stopColor={g1} />
          </linearGradient>
        </defs>
        <rect width="800" height="450" fill={`url(#${uid})`} />
        {pattern}
        {/* category chip */}
        <rect x="24" y="24" width="148" height="30" rx="15" fill={accent} opacity="0.9" />
        <text
          x="98"
          y="44"
          textAnchor="middle"
          fontSize="11"
          fontWeight="700"
          fontFamily="system-ui, sans-serif"
          fill="#13181b"
          letterSpacing="0.07em"
        >
          {CATEGORY_LABELS[category].toUpperCase()}
        </text>
      </svg>
    </div>
  );
}
