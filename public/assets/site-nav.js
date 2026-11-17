/* Progressive-enhancement menu. With JavaScript disabled, CSS keeps links available. */
(() => {
  document.documentElement.classList.add("has-enhanced-nav");
  const toggle = document.querySelector(".site-header__toggle");
  const nav = document.getElementById("main-site-nav");
  if (!toggle || !nav) return;
  const close = () => {
    nav.classList.remove("is-open");
    toggle.setAttribute("aria-expanded", "false");
    toggle.setAttribute("aria-label", "Open navigation");
  };
  toggle.addEventListener("click", () => {
    const next = !nav.classList.contains("is-open");
    nav.classList.toggle("is-open", next);
    toggle.setAttribute("aria-expanded", String(next));
    toggle.setAttribute("aria-label", next ? "Close navigation" : "Open navigation");
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && nav.classList.contains("is-open")) {
      close();
      toggle.focus();
    }
  });
  document.addEventListener("pointerdown", (event) => {
    if (!nav.contains(event.target) && !toggle.contains(event.target)) close();
  });
  nav.addEventListener("click", (event) => {
    if (event.target.closest("a")) close();
  });
  window.addEventListener("resize", () => {
    if (window.innerWidth > 900) close();
  });
})();
