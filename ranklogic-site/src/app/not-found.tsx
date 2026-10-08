import { Button } from "@/components/ui/Button";
import { GradientText } from "@/components/ui/GradientText";

export default function NotFound() {
  return (
    <section className="relative flex min-h-[60vh] items-center py-20">
      <div className="container-site flex flex-col items-center text-center">
        <div className="font-display text-7xl font-black sm:text-8xl">
          <GradientText>404</GradientText>
        </div>
        <h1 className="mt-4 font-display text-3xl font-black text-ink sm:text-4xl">
          This page got buried on page 2.
        </h1>
        <p className="mt-3 max-w-md text-ink-soft">
          The link you followed doesn&apos;t exist — but your free audit still
          does. Let&apos;s get your phone ringing instead.
        </p>
        <div className="mt-8 flex flex-col gap-3 sm:flex-row">
          <Button href="/" variant="ghost" size="lg">
            Back Home
          </Button>
          <Button href="/audit" size="lg">
            Get My Free Audit →
          </Button>
        </div>
      </div>
    </section>
  );
}
