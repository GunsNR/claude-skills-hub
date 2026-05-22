import Link from "next/link";
import { footer } from "@/lib/copy";
import { site } from "@/lib/site";
import { Logo } from "./Logo";

export function Footer() {
  return (
    <footer className="relative mt-24 pb-28 md:pb-12">
      <div className="container-site">
        <div className="glass rounded-[32px] p-8 sm:p-12">
          <div className="grid gap-10 md:grid-cols-[1.6fr_1fr_1fr_1fr]">
            <div>
              <Logo />
              <p className="mt-4 max-w-xs text-sm leading-relaxed text-ink-soft">
                {footer.description}
              </p>
              <a
                href={site.phoneHref}
                className="font-display mt-5 inline-block text-xl font-bold text-coral-deep"
              >
                {site.phoneDisplay}
              </a>
            </div>

            <FooterCol title="Services">
              {footer.services.map((s) => (
                <FooterLink key={s.href} href={s.href}>
                  {s.label}
                </FooterLink>
              ))}
            </FooterCol>

            <div>
              <h3 className="eyebrow mb-4 text-[0.72rem] font-semibold text-ink">
                Markets
              </h3>
              <ul className="space-y-2.5">
                {footer.markets.map((m) => (
                  <li key={m} className="text-sm text-ink-soft">
                    {m}
                  </li>
                ))}
              </ul>
            </div>

            <FooterCol title="Company">
              {footer.company.map((c) => (
                <FooterLink key={c.href} href={c.href}>
                  {c.label}
                </FooterLink>
              ))}
            </FooterCol>
          </div>

          <div className="mt-10 border-t border-ink/10 pt-6">
            <p className="text-xs text-ink-faint">{footer.legal}</p>
          </div>
        </div>
      </div>
    </footer>
  );
}

function FooterCol({
  title,
  children,
}: {
  title: string;
  children: React.ReactNode;
}) {
  return (
    <div>
      <h3 className="eyebrow mb-4 text-[0.72rem] font-semibold text-ink">
        {title}
      </h3>
      <ul className="space-y-2.5">{children}</ul>
    </div>
  );
}

function FooterLink({
  href,
  children,
}: {
  href: string;
  children: React.ReactNode;
}) {
  return (
    <li>
      <Link
        href={href}
        className="text-sm text-ink-soft transition-colors hover:text-coral-deep"
      >
        {children}
      </Link>
    </li>
  );
}
