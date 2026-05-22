import { proofStrip } from "@/lib/copy";
import { clientProof } from "@/lib/clients";
import { Reveal } from "@/components/ui/Reveal";

export function ProofStrip() {
  return (
    <section className="relative py-10">
      <div className="container-site">
        <Reveal>
          <p className="eyebrow text-center text-[0.74rem] font-semibold text-ink-faint">
            {proofStrip.heading}
          </p>
        </Reveal>

        <div className="mt-7 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
          {clientProof.map((client, i) => (
            <Reveal key={client.name} delay={i * 0.08}>
              <div className="glass lift h-full rounded-3xl p-6">
                <div className="text-base tracking-tight text-amber">
                  {client.rating}
                </div>
                <h3 className="mt-3 font-display text-lg font-bold text-ink">
                  {client.name}
                </h3>
                <p className="font-caps mt-1 text-sm font-semibold uppercase tracking-wide text-coral-deep">
                  {client.stat}
                </p>
                <p className="mt-3 text-xs text-ink-faint">
                  {client.location} · {client.trade}
                </p>
              </div>
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  );
}
