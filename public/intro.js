/* =========================================================
   INTRO — TOCA GEEK
   Animação de entrada centrada na logo, exibida a cada
   carregamento. Pode ser pulada com clique ou qualquer tecla.
   ========================================================= */

(function () {
  const overlay = document.getElementById("boot-overlay");
  const logo = document.getElementById("intro-logo");
  if (!overlay || !logo) return;

  /* A logo vem do catálogo de imagens já carregado */
  if (typeof IMAGES !== "undefined" && IMAGES.logo) {
    logo.src = IMAGES.logo;
  }

  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduceMotion) {
    finish(true);
    return;
  }

  const INTRO_DURATION = 3200; /* ms até a revelação automática */
  let done = false;
  let autoTimer = setTimeout(() => finish(false), INTRO_DURATION);

  function finish(instant) {
    if (done) return;
    done = true;
    clearTimeout(autoTimer);
    document.removeEventListener("keydown", skip);
    overlay.removeEventListener("click", skip);

    document.body.classList.remove("booting");

    if (instant) {
      overlay.remove();
      return;
    }
    overlay.classList.add("boot-off");
    overlay.addEventListener("animationend", () => overlay.remove(), { once: true });
    /* Fallback caso animationend não dispare */
    setTimeout(() => overlay.remove(), 800);
  }

  function skip() {
    finish(false);
  }

  document.addEventListener("keydown", skip);
  overlay.addEventListener("click", skip);
})();
