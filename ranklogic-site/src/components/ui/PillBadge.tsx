import { cn } from "@/lib/utils";

/** Small uppercase pill label. `tone` switches between glass and solid-gradient. */
export function PillBadge({
  children,
  className,
  tone = "glass",
}: {
  children: React.ReactNode;
  className?: string;
  tone?: "glass" | "gradient" | "white";
}) {
  return (
    <span
      className={cn(
        "eyebrow inline-flex items-center gap-2 rounded-full px-4 py-1.5 text-[0.7rem] font-semibold",
        tone === "glass" && "glass text-coral-deep",
        tone === "gradient" && "text-white",
        tone === "white" && "bg-white/85 text-coral-deep",
        className,
      )}
      style={
        tone === "gradient"
          ? { background: "var(--grad-hot)" }
          : undefined
      }
    >
      <span
        className="h-1.5 w-1.5 rounded-full"
        style={{
          background:
            tone === "gradient" || tone === "white"
              ? "currentColor"
              : "var(--grad-hot)",
        }}
      />
      {children}
    </span>
  );
}
