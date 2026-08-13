import Link from "next/link";
import { cn } from "@/lib/utils";

/** The R-mark: a blocky R with an integrated coral "rank-up" arrow. */
function RMark({ dark, className }: { dark: string; className?: string }) {
  return (
    <svg
      viewBox="0 0 100 100"
      className={className}
      fill="none"
      aria-hidden
    >
      <g fill={dark}>
        <rect x="17" y="13" width="24" height="74" rx="4" />
        <path
          fillRule="evenodd"
          d="M17 13 H56 A22 22 0 0 1 56 57 H17 Z M40 28 H49 A7.5 7.5 0 0 1 49 43 H40 Z"
        />
        <path d="M39 50 H60 L88 87 H67 Z" />
      </g>
      <polygon points="68,15 68,45 38,15" fill="#fd8973" />
      <path
        d="M52 32 L30 54"
        stroke="#fd8973"
        strokeWidth="13"
        strokeLinecap="round"
      />
    </svg>
  );
}

export function Logo({
  className,
  tone = "ink",
}: {
  className?: string;
  tone?: "ink" | "white";
}) {
  const dark = tone === "white" ? "#f0eeeb" : "#13181b";

  return (
    <Link
      href="/"
      className={cn("inline-flex items-center gap-2.5", className)}
      aria-label="RankLogic SEO — home"
    >
      <span className="flex flex-col leading-[0.82]">
        <span
          className="font-body text-[1.02rem] font-black uppercase tracking-[-0.02em]"
          style={{ color: dark }}
        >
          Rank
        </span>
        <span
          className="font-body text-[1.02rem] font-black uppercase tracking-[-0.02em]"
          style={{ color: dark }}
        >
          Logic
        </span>
        <span className="font-body text-[0.5rem] font-extrabold uppercase tracking-[0.34em] text-coral-deep">
          SEO
        </span>
      </span>
      <RMark dark={dark} className="h-10 w-10" />
    </Link>
  );
}
