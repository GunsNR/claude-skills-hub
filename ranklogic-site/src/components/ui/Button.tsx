import Link from "next/link";
import { cn } from "@/lib/utils";

type Variant = "primary" | "ghost" | "white" | "white-ghost";
type Size = "md" | "lg";

const base =
  "font-caps inline-flex items-center justify-center gap-2 rounded-full font-semibold uppercase tracking-[0.06em] transition-all duration-300 will-change-transform";

const sizes: Record<Size, string> = {
  md: "px-6 py-3 text-[0.82rem]",
  lg: "px-8 py-4 text-[0.92rem]",
};

const variants: Record<Variant, string> = {
  primary:
    "text-white shadow-[0_12px_32px_rgba(214,105,63,0.35)] hover:-translate-y-0.5 hover:shadow-[0_18px_44px_rgba(255,107,157,0.5)] cta-pulse",
  ghost:
    "glass text-ink hover:-translate-y-0.5 hover:text-coral-deep",
  white:
    "bg-white text-coral-deep shadow-[0_12px_32px_rgba(13,27,42,0.18)] hover:-translate-y-0.5",
  "white-ghost":
    "border border-white/70 text-white hover:bg-white/15 hover:-translate-y-0.5",
};

interface ButtonProps {
  children: React.ReactNode;
  href: string;
  variant?: Variant;
  size?: Size;
  className?: string;
}

export function Button({
  children,
  href,
  variant = "primary",
  size = "md",
  className,
}: ButtonProps) {
  const isExternal = href.startsWith("http") || href.startsWith("tel:");
  const classes = cn(base, sizes[size], variants[variant], className);
  const style =
    variant === "primary"
      ? { background: "var(--grad-hot)" }
      : undefined;

  if (isExternal) {
    return (
      <a href={href} className={classes} style={style}>
        {children}
      </a>
    );
  }

  return (
    <Link href={href} className={classes} style={style}>
      {children}
    </Link>
  );
}
