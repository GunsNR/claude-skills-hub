import Link from "next/link";
import { Phone } from "lucide-react";
import { site } from "@/lib/site";

/** Always-visible mobile tap-to-call bar. Hidden on desktop. */
export function StickyCallBar() {
  return (
    <div className="fixed inset-x-0 bottom-0 z-50 md:hidden">
      <div className="glass m-2.5 flex items-center gap-2.5 rounded-2xl p-2.5">
        <a
          href={site.phoneHref}
          className="font-caps flex flex-1 items-center justify-center gap-2 rounded-xl py-3 text-[0.84rem] font-semibold uppercase tracking-[0.05em] text-white shadow-[0_8px_22px_rgba(214,105,63,0.34)]"
          style={{ background: "var(--grad-hot)" }}
        >
          <Phone size={15} />
          Call Now
        </a>
        <Link
          href="/audit"
          className="font-caps neo-sm flex flex-1 items-center justify-center rounded-xl py-3 text-[0.84rem] font-semibold uppercase tracking-[0.05em] text-coral-deep"
        >
          Free Audit
        </Link>
      </div>
    </div>
  );
}
