/* =========================================================
   PÁGINA DE PRODUTO — TOCA GEEK
   Lê o produto atual (window.CURRENT_PRODUCT_SLUG) a partir do
   array PRODUCTS (definido em data.js) e preenche a página.
   ========================================================= */

(function () {
  function normalize(str) {
    return str.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase();
  }

  function renderLogos() {
    document.querySelectorAll(".js-logo").forEach((img) => { img.src = IMAGES.logo; });
  }

  const slug = window.CURRENT_PRODUCT_SLUG;
  const product = PRODUCTS.find((p) => p.slug === slug);

  renderLogos();

  if (!product) {
    document.querySelector(".product-page").innerHTML =
      '<p style="padding:60px 0;">Produto não encontrado. <a href="../index.html" style="color:var(--blue-neon);">Voltar ao catálogo</a></p>';
    return;
  }

  document.title = product.name + " — Toca Geek";

  const img = document.querySelector(".js-product-img");
  if (img) { img.src = product.img; img.alt = product.name; }

  const buyLink = document.querySelector(".js-buy-link");
  if (buyLink) { buyLink.href = product.url || "#"; }

  /* ---------- RELACIONADOS ---------- */
  const relatedGrid = document.getElementById("related-grid");
  if (relatedGrid) {
    const related = PRODUCTS.filter(
      (p) => p.category === product.category && p.slug !== product.slug
    ).slice(0, 4);

    if (related.length === 0) {
      relatedGrid.innerHTML = '<p style="color:var(--text-muted);">Nenhum outro modelo nessa seção ainda.</p>';
    } else {
      const cat = CATEGORIES.find((c) => c.key === product.category);
      relatedGrid.innerHTML = related.map((p) => `
        <a class="card card-link" href="${p.slug}.html">
          <div class="card-img-wrap">
            <img src="${p.img}" alt="${p.name}" loading="lazy">
          </div>
          <div class="card-body">
            <span class="card-category">${cat ? cat.label : ""}</span>
            <h3>${p.name}</h3>
            <div class="card-footer">
              ${p.price ? `<span class="card-price">${p.price}</span>` : `<span></span>`}
              <span class="card-cta">Ver produto →</span>
            </div>
          </div>
        </a>
      `).join("");
    }
  }
})();
