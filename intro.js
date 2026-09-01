/* =========================================================
   INTRO — TOCA GEEK
   Fade minimalista da logo ao carregar a home. Roda uma vez
   (sessionStorage), é rápida, pode ser pulada com clique/tecla,
   e respeita prefers-reduced-motion.
   ========================================================= */

(function () {
  const alreadySeen = sessionStorage.getItem("toca-geek-intro-seen");
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  if (alreadySeen || reduceMotion) return;

  const overlay = document.createElement("div");
  overlay.id = "intro-overlay";
  overlay.innerHTML = `<img id="intro-logo" alt="Toca Geek">`;
  document.body.appendChild(overlay);

  const logo = overlay.querySelector("#intro-logo");
  logo.src = (typeof IMAGES !== "undefined" && IMAGES.logo) ? IMAGES.logo : "";

  function finish() {
    sessionStorage.setItem("toca-geek-intro-seen", "1");
    overlay.classList.add("fade-out");
    setTimeout(() => overlay.remove(), 500);
    document.removeEventListener("click", finish);
    document.removeEventListener("keydown", finish);
  }

  requestAnimationFrame(() => {
    requestAnimationFrame(() => logo.classList.add("show"));
  });

  overlay.addEventListener("click", finish);
  document.addEventListener("keydown", finish);
  setTimeout(finish, 1400);
})();
