import { cn } from "@/lib/utils";

/** Neomorphic card. `inset` renders the pressed state. */
export function NeoCard({
  children,
  className,
  inset = false,
  hover = false,
}: {
  children: React.ReactNode;
  className?: string;
  inset?: boolean;
  hover?: boolean;
}) {
  return (
    <div
      className={cn(
        "rounded-[24px]",
        inset ? "neo-inset" : "neo",
        hover && "lift",
        className,
      )}
    >
      {children}
    </div>
  );
}
