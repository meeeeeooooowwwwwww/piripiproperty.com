/* Independent Piripi Property lead intake.
 * BREVO_API_KEY is a secret on this Pages project; destination is a private
 * ENQUIRY_TO_EMAIL variable. Without recipient configuration route to the
 * verified business owner's public email, NOT to a hard-coded private Gmail.
 */
const json = (data, status = 200) => new Response(JSON.stringify(data), {
  status,
  headers: { "Content-Type": "application/json; charset=utf-8", "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" }
});
const emailOk = (s) => typeof s === "string" && s.length <= 254 && /^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9](?:[A-Za-z0-9.-]*[A-Za-z0-9])?\.[A-Za-z]{2,}$/.test(s);
const interests = new Set(["Selling a property", "Buying a property", "A property appraisal", "A general enquiry"]);
const clean = (x, max) => typeof x === "string" ? x.trim().slice(0, max + 1) : "";
const allowedOrigins = new Set(["https://piripiproperty.com", "https://piripiproperty.pages.dev"]);

export async function onRequestPost({ request, env }) {
  const origin = request.headers.get("Origin");
  if (!origin || !allowedOrigins.has(origin)) return json({ ok: false, error: "Invalid request origin" }, 403);
  const type = request.headers.get("Content-Type") || "";
  if (!type.toLowerCase().startsWith("application/json")) return json({ ok: false, error: "JSON required" }, 415);
  if (Number(request.headers.get("Content-Length") || 0) > 5500) return json({ ok: false, error: "Request too large" }, 413);

  let payload;
  try {
    const raw = await request.text();
    if (raw.length > 5500) return json({ ok: false, error: "Request too large" }, 413);
    payload = JSON.parse(raw);
  } catch {
    return json({ ok: false, error: "Invalid request" }, 400);
  }
  if (!payload || typeof payload !== "object" || Array.isArray(payload)) return json({ ok: false, error: "Invalid request" }, 400);
  if (clean(payload.company_website, 500)) return json({ ok: true }); // honeypot: do not transmit
  const name = clean(payload.name, 100);
  const email = clean(payload.email, 254);
  const interest = clean(payload.interest, 50);
  const message = clean(payload.message || "", 1500);
  const elapsed = Date.now() - Number(payload.openedAt);
  if (!name || name.length > 100 || !emailOk(email) || !interests.has(interest) ||
      message.length > 1500 || !Number.isFinite(elapsed) || elapsed < 2000 || elapsed > 86400000) {
    return json({ ok: false, error: "Please check your details" }, 400);
  }
  const apiKey = typeof env.BREVO_API_KEY === "string" ? env.BREVO_API_KEY.trim() : "";
  if (!apiKey) return json({ ok: false, error: "Email delivery is not configured" }, 503);
  const destination = typeof env.ENQUIRY_TO_EMAIL === "string" && env.ENQUIRY_TO_EMAIL.trim()
    ? env.ENQUIRY_TO_EMAIL.trim() : "david@americafirst.co.nz";
  const sender = typeof env.BREVO_FROM_EMAIL === "string" && env.BREVO_FROM_EMAIL.trim()
    ? env.BREVO_FROM_EMAIL.trim() : "david@grideater.com";
  if (!emailOk(destination) || !emailOk(sender)) return json({ ok: false, error: "Email delivery misconfigured" }, 503);

  const emailPayload = {
    sender: { name: "Piripi & Sons Website", email: sender },
    to: [{ email: destination }],
    replyTo: { email, name },
    subject: "Piripi & Sons enquiry: " + interest,
    textContent: [
      "New website enquiry for Corrie Piripi",
      "",
      "Name: " + name,
      "Email: " + email,
      "Interest: " + interest,
      "",
      "Message:",
      message || "(not provided)",
      "",
      "Submitted through piripiproperty.com."
    ].join("\n")
  };
  try {
    const response = await fetch("https://api.brevo.com/v3/smtp/email", {
      method: "POST",
      headers: { "Content-Type": "application/json", "Accept": "application/json", "api-key": apiKey },
      body: JSON.stringify(emailPayload),
      signal: AbortSignal.timeout(10000)
    });
    if (!response.ok) return json({ ok: false, error: "Email provider declined the enquiry" }, 502);
    const result = await response.json();
    if (!result || typeof result.messageId !== "string" || !result.messageId) return json({ ok: false, error: "Email provider did not acknowledge the enquiry" }, 502);
    return json({ ok: true });
  } catch {
    return json({ ok: false, error: "Email delivery temporarily unavailable" }, 502);
  }
}

export function onRequestGet() { return json({ ok: false, error: "Method not allowed" }, 405); }
