import { site } from "@/lib/site";
import { WhatsAppIcon } from "@/components/ui/WhatsAppIcon";

/** Always-available WhatsApp contact button, fixed bottom-right (desktop). */
export function FloatingWhatsApp() {
  return (
    <a
      href={site.whatsapp}
      target="_blank"
      rel="noopener noreferrer"
      aria-label="Chat with us on WhatsApp"
      className="group fixed bottom-6 right-6 z-50 hidden items-center gap-3 md:flex"
    >
      <span className="glass pointer-events-none rounded-full px-4 py-2 text-sm font-semibold text-ink opacity-0 transition-opacity duration-300 group-hover:opacity-100">
        Chat with us
      </span>
      <span className="relative flex h-14 w-14 items-center justify-center rounded-full bg-[#25d366] text-white shadow-[0_14px_32px_rgba(37,211,102,0.45)] transition-transform duration-300 group-hover:-translate-y-0.5">
        <span className="absolute inset-0 animate-ping rounded-full bg-[#25d366] opacity-30" />
        <WhatsAppIcon className="relative h-7 w-7" />
      </span>
    </a>
  );
}
