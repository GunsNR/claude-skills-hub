import Link from "next/link";
import { Phone } from "lucide-react";
import { site } from "@/lib/site";
import { WhatsAppIcon } from "@/components/ui/WhatsAppIcon";

/** Always-visible mobile contact bar: WhatsApp, call, and audit. Hidden on desktop. */
export function StickyCallBar() {
  return (
    <div className="fixed inset-x-0 bottom-0 z-50 md:hidden">
      <div className="glass m-2.5 flex items-center gap-2 rounded-2xl p-2">
        <a
          href={site.whatsapp}
          target="_blank"
          rel="noopener noreferrer"
          className="font-caps flex flex-1 items-center justify-center gap-1.5 rounded-xl bg-[#25d366] py-3 text-[0.72rem] font-bold uppercase tracking-[0.04em] text-white shadow-[0_8px_20px_rgba(37,211,102,0.4)]"
        >
          <WhatsAppIcon className="h-4 w-4" />
          WhatsApp
        </a>
        <a
          href={site.phoneHref}
          className="font-caps flex flex-1 items-center justify-center gap-1.5 rounded-xl py-3 text-[0.72rem] font-bold uppercase tracking-[0.04em] text-white shadow-[0_8px_20px_rgba(253,137,115,0.36)]"
          style={{ background: "var(--grad-hot)" }}
        >
          <Phone size={14} />
          Call
        </a>
        <Link
          href="/audit"
          className="font-caps neo-sm flex flex-1 items-center justify-center rounded-xl py-3 text-[0.72rem] font-bold uppercase tracking-[0.04em] text-coral-deep"
        >
          Free Audit
        </Link>
      </div>
    </div>
  );
}
