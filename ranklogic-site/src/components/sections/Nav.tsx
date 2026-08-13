"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { Menu, X } from "lucide-react";
import { nav } from "@/lib/copy";
import { cn } from "@/lib/utils";
import { Logo } from "./Logo";

export function Nav() {
  const [scrolled, setScrolled] = useState(false);
  const [open, setOpen] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 16);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  return (
    <header className="sticky top-3 z-50 px-3">
      <nav
        className={cn(
          "container-site flex items-center justify-between rounded-full px-4 py-2.5 transition-all duration-300 sm:px-5",
          "glass",
          scrolled && "shadow-[0_18px_50px_rgba(174,184,200,0.4)]",
        )}
      >
        <Logo />

        <div className="hidden items-center gap-7 md:flex">
          {nav.links.map((link) => (
            <Link
              key={link.label}
              href={link.href}
              className="font-caps text-[0.82rem] font-medium uppercase tracking-[0.06em] text-ink-soft transition-colors hover:text-coral-deep"
            >
              {link.label}
            </Link>
          ))}
        </div>

        <div className="flex items-center gap-2">
          <Link
            href={nav.cta.href}
            className="font-caps hidden rounded-full px-5 py-2.5 text-[0.78rem] font-semibold uppercase tracking-[0.06em] text-white shadow-[0_10px_26px_rgba(214,105,63,0.32)] transition-transform hover:-translate-y-0.5 sm:inline-flex"
            style={{ background: "var(--grad-hot)" }}
          >
            {nav.cta.label} →
          </Link>
          <button
            type="button"
            onClick={() => setOpen((v) => !v)}
            aria-label={open ? "Close menu" : "Open menu"}
            aria-expanded={open}
            className="neo-sm flex h-10 w-10 items-center justify-center rounded-full text-ink md:hidden"
          >
            {open ? <X size={18} /> : <Menu size={18} />}
          </button>
        </div>
      </nav>

      {open && (
        <div className="container-site mt-2 md:hidden">
          <div className="glass flex flex-col gap-1 rounded-3xl p-3">
            {nav.links.map((link) => (
              <Link
                key={link.label}
                href={link.href}
                onClick={() => setOpen(false)}
                className="font-caps rounded-2xl px-4 py-3 text-sm font-medium uppercase tracking-[0.06em] text-ink-soft transition-colors hover:bg-white/60 hover:text-coral-deep"
              >
                {link.label}
              </Link>
            ))}
            <Link
              href={nav.cta.href}
              onClick={() => setOpen(false)}
              className="font-caps mt-1 rounded-2xl px-4 py-3 text-center text-sm font-semibold uppercase tracking-[0.06em] text-white"
              style={{ background: "var(--grad-hot)" }}
            >
              {nav.cta.label} →
            </Link>
          </div>
        </div>
      )}
    </header>
  );
}
