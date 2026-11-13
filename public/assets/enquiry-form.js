/* Enquiries are delivered through our same-origin Pages Function.
   Never put private destination emails or provider keys in browser code. */
(() => {
  const form = document.getElementById("property-enquiry-form");
  const status = document.getElementById("enquiry-status");
  const fallback = document.getElementById("enquiry-fallback");
  if (!form || !status) return;
  const button = form.querySelector('button[type="submit"]');
  const openedAt = Date.now();

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    if (!form.reportValidity() || button.disabled) return;
    const data = new FormData(form);
    const payload = {
      name: String(data.get("name") || "").trim(),
      email: String(data.get("email") || "").trim(),
      interest: String(data.get("interest") || ""),
      message: String(data.get("message") || "").trim(),
      company_website: String(data.get("company_website") || ""),
      openedAt
    };
    if (fallback) fallback.hidden = true;
    button.disabled = true;
    status.dataset.state = "";
    status.textContent = "Sending your enquiry…";
    try {
      const response = await fetch(form.action, {
        method: "POST",
        headers: { "Content-Type": "application/json", "Accept": "application/json" },
        body: JSON.stringify(payload),
        credentials: "same-origin",
        cache: "no-store"
      });
      const result = await response.json().catch(() => ({}));
      if (!response.ok || !result.ok) throw new Error("Delivery unavailable");
      status.dataset.state = "success";
      status.textContent = "Thanks, your enquiry has been submitted. Corrie will be in touch.";
      form.reset();
      if (fallback) fallback.hidden = true;
    } catch {
      status.dataset.state = "error";
      status.textContent = "Sorry, the website couldn't send your enquiry. Nothing has been submitted. Please call Corrie or use your email app below.";
      if (fallback) {
        const body = [
          "Hello, please pass this enquiry to Corrie Piripi.",
          "",
          "Name: " + payload.name,
          "Email: " + payload.email,
          "Interest: " + payload.interest,
          "Message: " + (payload.message || "(not provided)")
        ].join("\n");
        fallback.href = "mailto:david@americafirst.co.nz?subject=" + encodeURIComponent("Piripi Property enquiry: " + payload.interest) + "&body=" + encodeURIComponent(body);
        fallback.hidden = false;
      }
    } finally {
      button.disabled = false;
    }
  });
})();
