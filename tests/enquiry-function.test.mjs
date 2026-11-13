import test from "node:test";
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";

const source = await readFile(new URL("../functions/api/enquiry.js", import.meta.url), "utf8");
const { onRequestPost } = await import("data:text/javascript," + encodeURIComponent(source));
const base = {
  name: "Jane Buyer", email: "jane@example.com", phone: "+64 21 234 5678", interest: "Buying a property",
  message: "Hello Corrie", company_website: "", openedAt: Date.now() - 5000
};
function req(payload = base, origin = "https://piripiproperty.com") {
  return new Request("https://piripiproperty.com/api/enquiry", {
    method: "POST", headers: { Origin: origin, "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  });
}
test("without configured secret fails closed and does not claim success", async () => {
  const response = await onRequestPost({ request: req(), env: {} });
  assert.equal(response.status, 503);
  assert.equal((await response.json()).ok, false);
});
test("rejects cross-site posts", async () => {
  const response = await onRequestPost({ request: req(base, "https://example.com"), env: {} });
  assert.equal(response.status, 403);
});
test("honeypot discards automation before accessing provider", async () => {
  const response = await onRequestPost({ request: req({...base, company_website: "spam.test"}), env: {} });
  assert.equal(response.status, 200);
});
test("valid inquiry routes privately to temporary owner inbox via Brevo", async () => {
  const originalFetch = globalThis.fetch;
  let sent;
  globalThis.fetch = async (_url, opts) => {
    sent = JSON.parse(opts.body);
    return new Response(JSON.stringify({messageId: "<ack@brevo>"}), {status:201,headers:{"Content-Type":"application/json"}});
  };
  try {
    const response = await onRequestPost({request:req(),env:{BREVO_API_KEY:"private-test-value"}});
    assert.equal(response.status, 200);
    assert.equal((await response.json()).ok, true);
    assert.equal(sent.to[0].email,"david@americafirst.co.nz");
    assert.equal(sent.replyTo.email,base.email);
    assert.ok(sent.textContent.includes("Phone: +64 21 234 5678"));
  } finally { globalThis.fetch = originalFetch; }
});
test("private recipient overrides fallback without appearing in static source", async () => {
  const originalFetch = globalThis.fetch;
  let sent;
  globalThis.fetch = async (_url, opts) => {
    sent = JSON.parse(opts.body);
    return new Response(JSON.stringify({messageId:"accepted"}),{status:201});
  };
  try {
    const response = await onRequestPost({request:req(),env:{BREVO_API_KEY:"private-test-value",ENQUIRY_TO_EMAIL:"private-recipient@example.net"}});
    assert.equal((await response.json()).ok,true);
    assert.equal(sent.to[0].email,"private-recipient@example.net");
    assert.equal(source.includes("private-recipient@example.net"),false);
  } finally { globalThis.fetch = originalFetch; }
});

test("rejects missing mandatory phone number", async () => {
  const response = await onRequestPost({request:req({...base,phone:""}),env:{BREVO_API_KEY:"private-test-value"}});
  assert.equal(response.status,400);
  assert.equal((await response.json()).ok,false);
});
test("rejects missing mandatory message", async () => {
  const response = await onRequestPost({request:req({...base,message:"  "}),env:{BREVO_API_KEY:"private-test-value"}});
  assert.equal(response.status,400);
  assert.equal((await response.json()).ok,false);
});
test("rejects an invalid telephone number", async () => {
  const response = await onRequestPost({request:req({...base,phone:"HELLO-123"}),env:{BREVO_API_KEY:"private-test-value"}});
  assert.equal(response.status,400);
});
test("rejects an unselected interest", async () => {
  const response = await onRequestPost({request:req({...base,interest:""}),env:{BREVO_API_KEY:"private-test-value"}});
  assert.equal(response.status,400);
});
