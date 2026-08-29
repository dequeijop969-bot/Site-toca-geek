/* =========================================================
   CATÁLOGO — TOCA GEEK
   CATEGORIES e PRODUCTS vêm de data.js (gerado por build.py).
   As imagens ficam em images-data.js (base64, sempre carregam,
   mesmo fora de um servidor).

   Para adicionar/editar produtos, preços ou descrições:
   edite build.py e rode "python3 build.py" de novo.
   ========================================================= */

function normalize(str) {
  return str.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase();
}

function renderLogos(){
  document.querySelectorAll(".js-logo").forEach(img => { img.src = IMAGES.logo; });
}

function renderNav(){
  const nav = document.getElementById("cat-pills");
  nav.innerHTML = CATEGORIES.map(c => `<a href="#${c.key}">${c.label}</a>`).join("");
}

function cardHTML(p, cat){
  const searchBlob = normalize(`${p.name} ${cat.label}`);
  return `
    <a class="card card-link" href="produtos/${p.slug}.html" data-search="${searchBlob}" data-category="${p.category}">
      <div class="card-img-wrap">
        <span class="card-chip">${cat.label}</span>
        <img src="${p.img}" alt="${p.name}" loading="lazy">
      </div>
      <div class="card-body">
        <h3>${p.name}</h3>
        <div class="card-footer">
          ${p.price ? `<span class="card-price">${p.price}</span>` : `<span></span>`}
          <span class="card-cta">Ver produto</span>
        </div>
      </div>
    </a>
  `;
}

function renderCatalog(){
  const root = document.getElementById("catalog");
  document.getElementById("stat-total").textContent = PRODUCTS.length;
  document.getElementById("stat-cats").textContent = CATEGORIES.length;

  root.innerHTML = CATEGORIES.map(cat => {
    const items = PRODUCTS.filter(p => p.category === cat.key);
    if(items.length === 0) return "";
    const cards = items.map(p => cardHTML(p, cat)).join("");

    return `
      <div class="section-block" id="${cat.key}">
        <div class="section-head">
          <div class="section-head-left">
            <span class="section-tag">// Seção</span>
            <h2>${cat.label}</h2>
            <p>${cat.tagline}</p>
          </div>
          <span class="section-count">${items.length} ${items.length === 1 ? "modelo" : "modelos"}</span>
        </div>
        <div class="grid">${cards}</div>
      </div>
    `;
  }).join("");
}

renderLogos();
renderNav();
renderCatalog();

/* ---------- SCROLL REVEAL ---------- */
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if(entry.isIntersecting){
      entry.target.classList.add("in-view");
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold:0.12 });

function observeCards(){
  document.querySelectorAll(".card:not(.in-view)").forEach(card => revealObserver.observe(card));
}
observeCards();

/* ---------- BUSCA ---------- */
const searchInput = document.getElementById("search-input");
const searchEmpty = document.getElementById("search-empty");

function runSearch(rawQuery){
  const query = normalize(rawQuery.trim());
  const sections = document.querySelectorAll(".section-block");
  let totalVisible = 0;

  sections.forEach(section => {
    let visibleInSection = 0;
    section.querySelectorAll(".card").forEach(card => {
      const match = query === "" || card.dataset.search.includes(query);
      card.style.display = match ? "" : "none";
      if(match) visibleInSection++;
    });
    section.style.display = visibleInSection === 0 ? "none" : "";
    totalVisible += visibleInSection;
  });

  if(searchEmpty){
    searchEmpty.style.display = (query !== "" && totalVisible === 0) ? "block" : "none";
  }
}

if(searchInput){
  searchInput.addEventListener("input", (e) => runSearch(e.target.value));
}
