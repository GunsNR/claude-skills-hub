"use client";

import { useState } from "react";
import { tradeOptions } from "@/lib/copy";
import { site } from "@/lib/site";
import { cn } from "@/lib/utils";

type Status = "idle" | "submitting" | "success" | "error";

interface AuditFormProps {
  badge: string;
  heading: string;
  cta: string;
  finePrint: string;
}

export function AuditForm({ badge, heading, cta, finePrint }: AuditFormProps) {
  const [name, setName] = useState("");
  const [phone, setPhone] = useState("");
  const [trade, setTrade] = useState<string>("");
  const [status, setStatus] = useState<Status>("idle");

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    if (!name.trim() || !phone.trim()) {
      setStatus("error");
      return;
    }
    setStatus("submitting");
    try {
      const res = await fetch("/api/lead", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, phone, trade }),
      });
      if (!res.ok) throw new Error("Request failed");
      setStatus("success");
    } catch {
      setStatus("error");
    }
  }

  if (status === "success") {
    return (
      <div className="glass rounded-[28px] p-8 text-center sm:p-10">
        <div
          className="mx-auto mb-5 flex h-16 w-16 items-center justify-center rounded-full text-3xl text-white"
          style={{ background: "var(--grad-hot)" }}
          aria-hidden
        >
          ✓
        </div>
        <h3 className="font-display text-2xl font-bold text-ink">
          Got it. We&apos;re on it.
        </h3>
        <p className="mt-3 text-ink-soft">
          Your free audit is in the queue. We&apos;ll review your site and get
          back to you within 48 hours — no spam, no pitch.
        </p>
        <p className="mt-4 text-sm text-ink-faint">
          Need us sooner? Call{" "}
          <a
            href={site.phoneHref}
            className="font-semibold text-coral-deep underline"
          >
            {site.phoneDisplay}
          </a>
        </p>
      </div>
    );
  }

  return (
    <form
      onSubmit={handleSubmit}
      className="glass rounded-[28px] p-6 sm:p-8"
      noValidate
    >
      <span className="eyebrow inline-flex rounded-full bg-white/70 px-3 py-1 text-[0.62rem] font-semibold text-coral-deep">
        {badge}
      </span>
      <h3 className="mt-4 font-display text-2xl font-bold leading-tight text-ink sm:text-[1.7rem]">
        {heading}
      </h3>

      <div className="mt-6 space-y-4">
        <Field
          id="name"
          label="Your Name"
          type="text"
          placeholder="First and last name"
          value={name}
          onChange={setName}
          autoComplete="name"
        />
        <Field
          id="phone"
          label="Phone Number"
          type="tel"
          placeholder="(555) 123-4567"
          value={phone}
          onChange={setPhone}
          autoComplete="tel"
        />

        <fieldset>
          <legend className="eyebrow mb-2 block text-[0.66rem] font-semibold text-ink-soft">
            Your Trade
          </legend>
          <div className="grid grid-cols-3 gap-2">
            {tradeOptions.map((t) => {
              const selected = trade === t;
              return (
                <button
                  key={t}
                  type="button"
                  onClick={() => setTrade(t)}
                  aria-pressed={selected}
                  className={cn(
                    "font-caps rounded-xl px-2 py-2.5 text-[0.74rem] font-semibold uppercase tracking-wide transition-all duration-200",
                    selected
                      ? "text-white"
                      : "neo-inset text-ink-soft hover:text-coral-deep",
                  )}
                  style={
                    selected
                      ? { background: "var(--grad-hot)" }
                      : undefined
                  }
                >
                  {t}
                </button>
              );
            })}
          </div>
        </fieldset>
      </div>

      {status === "error" && (
        <p className="mt-4 text-sm font-medium text-coral-deep">
          Please add your name and phone — or just call {site.phoneDisplay}.
        </p>
      )}

      <button
        type="submit"
        disabled={status === "submitting"}
        className="font-caps mt-6 flex w-full items-center justify-center rounded-full py-4 text-[0.92rem] font-semibold uppercase tracking-[0.06em] text-white shadow-[0_12px_32px_rgba(214,105,63,0.35)] transition-all duration-300 hover:-translate-y-0.5 disabled:opacity-70"
        style={{ background: "var(--grad-hot)" }}
      >
        {status === "submitting" ? "Sending…" : cta}
      </button>

      <p className="mt-3 text-center text-xs text-ink-faint">{finePrint}</p>
    </form>
  );
}

function Field({
  id,
  label,
  type,
  placeholder,
  value,
  onChange,
  autoComplete,
}: {
  id: string;
  label: string;
  type: string;
  placeholder: string;
  value: string;
  onChange: (v: string) => void;
  autoComplete: string;
}) {
  return (
    <div>
      <label
        htmlFor={id}
        className="eyebrow mb-2 block text-[0.66rem] font-semibold text-ink-soft"
      >
        {label}
      </label>
      <input
        id={id}
        name={id}
        type={type}
        placeholder={placeholder}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        autoComplete={autoComplete}
        className="neo-inset w-full rounded-xl px-4 py-3 text-ink placeholder:text-ink-faint/70 focus:outline-none focus:ring-2 focus:ring-coral/50"
      />
    </div>
  );
}
