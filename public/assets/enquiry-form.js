/* Small interim contact form. Email is composed in the visitor's own app,
 * not delivered or stored by the website. */
(() => {
  const form = document.getElementById("property-enquiry-form");
  const status = document.getElementById("enquiry-status");
  if (!form || !status) return;

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    if (!form.reportValidity()) return;

    const values = new FormData(form);
    const name = String(values.get("name") || "").trim();
    const email = String(values.get("email") || "").trim();
    const interest = String(values.get("interest") || "").trim();
    const message = String(values.get("message") || "").trim();
    const subject = "Piripi Property enquiry: " + interest;
    const body = [
      "Hello Corrie,",
      "",
      "I would like to enquire about: " + interest,
      "",
      "Name: " + name,
      "Email: " + email,
      "",
      message ? "Message:\n" + message : "Please contact me to discuss.",
      "",
      "Sent from an enquiry prepared on piripiproperty.com."
    ].join("\n");
    status.textContent = "Your email app should open. Please press Send there to complete your enquiry. If it doesn't open, email corrie@piripiproperty.com directly.";
    window.location.href = "mailto:corrie@piripiproperty.com?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
  });
})();
