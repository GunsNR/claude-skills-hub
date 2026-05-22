import { NextResponse } from "next/server";

/**
 * Lead intake endpoint for the free-audit forms.
 *
 * PLACEHOLDER: this currently logs the lead server-side only. Before launch,
 * forward to an email service (Resend/SendGrid) or CRM so Izzy is notified.
 */
export async function POST(req: Request) {
  let payload: unknown;
  try {
    payload = await req.json();
  } catch {
    return NextResponse.json(
      { ok: false, error: "Invalid request." },
      { status: 400 },
    );
  }

  const { name, phone, trade } = (payload ?? {}) as Record<string, unknown>;

  if (
    typeof name !== "string" ||
    typeof phone !== "string" ||
    !name.trim() ||
    !phone.trim()
  ) {
    return NextResponse.json(
      { ok: false, error: "Name and phone are required." },
      { status: 422 },
    );
  }

  console.log("[ranklogic:lead]", {
    name: name.trim(),
    phone: phone.trim(),
    trade: typeof trade === "string" ? trade : "Unspecified",
    at: new Date().toISOString(),
  });

  return NextResponse.json({ ok: true });
}
