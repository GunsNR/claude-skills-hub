import { site } from "@/lib/site";
import { topBar } from "@/lib/copy";

export function TopBar() {
  return (
    <div
      className="relative z-40 text-white"
      style={{ background: "var(--grad-bar)" }}
    >
      <div className="container-site flex items-center justify-center gap-2.5 py-2 text-center">
        <a
          href={site.phoneHref}
          className="font-caps text-[0.74rem] font-semibold uppercase tracking-[0.08em] sm:text-[0.8rem]"
        >
          {site.phoneDisplay}
        </a>
        <span className="hidden text-white/45 sm:inline">|</span>
        <span className="font-caps hidden text-[0.74rem] uppercase tracking-[0.08em] sm:inline">
          {topBar.middle}
        </span>
        <span className="hidden text-white/45 md:inline">|</span>
        <span className="font-caps hidden text-[0.74rem] uppercase tracking-[0.08em] md:inline">
          {topBar.right}
        </span>
      </div>
    </div>
  );
}
