/* Enquiries are delivered through our same-origin Pages Function.
   Never put private destination emails or provider keys in browser code. */
(() => {
  const form = document.getElementById("property-enquiry-form");
  const status = document.getElementById("enquiry-status");
  const fallback = document.getElementById("enquiry-fallback");
  if (!form || !status) return;
  const button = form.querySelector('button[type="submit"]');
  const note = form.querySelector(".enquiry-form__note");
  const openedAt = Date.now();
  let directReady = false;

  // Stay usable while the server-side email credential is being provisioned.
  fetch("/api/enquiry", { cache: "no-store", credentials: "same-origin" })
    .then(async (response) => response.ok ? await response.json() : null)
    .then((result) => {
      directReady = Boolean(result && result.ready);
      if (!directReady) {
        button.firstChild.textContent = "Prepare enquiry email ";
        if (note) note.textContent = "This opens your email application. Please press Send there to complete your enquiry.";
      }
    })
    .catch(() => {
      button.firstChild.textContent = "Prepare enquiry email ";
      if (note) note.textContent = "This opens your email application. Please press Send there to complete your enquiry.";
    });

  function prepareEmail(payload) {
    const body = [
      "Hello, please pass this enquiry to Corrie Piripi.",
      "",
      "Name: " + payload.name,
      "Email: " + payload.email,
      "Interest: " + payload.interest,
      "Message: " + (payload.message || "(not provided)")
    ].join("\\n");
    const link = "mailto:david@americafirst.co.nz?subject=" +
      encodeURIComponent("Piripi Property enquiry: " + payload.interest) +
      "&body=" + encodeURIComponent(body);
    if (fallback) { fallback.href = link; fallback.hidden = false; }
    return link;
  }

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
    if (!directReady) {
      const emailLink = prepareEmail(payload);
      status.dataset.state = "";
      status.textContent = "Your email application should open now. Please press Send there to complete the enquiry.";
      window.location.href = emailLink;
      return;
    }
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
      prepareEmail(payload);
    } finally {
      button.disabled = false;
    }
  });
})();
