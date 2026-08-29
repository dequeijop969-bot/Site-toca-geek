/* =========================================================
   POPUP DE REDES SOCIAIS — TOCA GEEK
   Botão flutuante que abre um popup com o link do Instagram.
   Instagram: @toca_geekt
   ========================================================= */

(function () {
  const fab = document.getElementById("social-fab");
  const backdrop = document.getElementById("social-modal-backdrop");
  const closeBtn = document.getElementById("social-modal-close");
  if (!fab || !backdrop) return;

  function openModal() {
    backdrop.classList.add("open");
    document.addEventListener("keydown", onKeydown);
  }

  function closeModal() {
    backdrop.classList.remove("open");
    document.removeEventListener("keydown", onKeydown);
  }

  function onKeydown(e) {
    if (e.key === "Escape") closeModal();
  }

  fab.addEventListener("click", openModal);
  closeBtn?.addEventListener("click", closeModal);
  backdrop.addEventListener("click", (e) => {
    if (e.target === backdrop) closeModal();
  });

  /* Mostra o botão com um pequeno atraso pra não competir com a animação de entrada */
  window.addEventListener("load", () => {
    setTimeout(() => fab.classList.add("visible"), 900);
  });
})();
