import Link from "next/link";
import { cn } from "@/lib/utils";

/** RankLogic wordmark: gradient "R" mark + Playfair name + Oswald "SEO". */
export function Logo({
  className,
  tone = "ink",
}: {
  className?: string;
  tone?: "ink" | "white";
}) {
  return (
    <Link
      href="/"
      className={cn("inline-flex items-center gap-2.5", className)}
      aria-label="RankLogic SEO — home"
    >
      <span
        className="font-display flex h-9 w-9 items-center justify-center rounded-[6px] text-xl font-black text-white"
        style={{ background: "var(--grad-hot)" }}
      >
        R
      </span>
      <span className="flex items-baseline gap-1.5">
        <span
          className={cn(
            "font-display text-xl font-bold tracking-tight",
            tone === "white" ? "text-white" : "text-ink",
          )}
        >
          RankLogic
        </span>
        <span className="font-caps text-sm font-semibold uppercase tracking-[0.12em] text-coral-deep">
          SEO
        </span>
      </span>
    </Link>
  );
}
