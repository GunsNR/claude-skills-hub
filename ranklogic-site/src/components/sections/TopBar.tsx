import { site } from "@/lib/site";
import { topBar } from "@/lib/copy";

export function TopBar() {
  return (
    <div className="relative z-40 bg-navy text-cream">
      <div className="container-site flex items-center justify-center gap-2.5 py-2 text-center">
        <a
          href={site.phoneHref}
          className="font-caps text-[0.74rem] font-bold uppercase tracking-[0.08em] text-amber sm:text-[0.8rem]"
        >
          {site.phoneDisplay}
        </a>
        <span className="hidden text-coral/60 sm:inline">/</span>
        <span className="font-caps hidden text-[0.74rem] uppercase tracking-[0.08em] text-cream/85 sm:inline">
          {topBar.middle}
        </span>
        <span className="hidden text-coral/60 md:inline">/</span>
        <span className="font-caps hidden text-[0.74rem] uppercase tracking-[0.08em] text-cream/85 md:inline">
          {topBar.right}
        </span>
      </div>
    </div>
  );
}
