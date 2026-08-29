/* =========================================================
   CATÁLOGO — TOCA GEEK
   As imagens ficam em images-data.js (embutidas em base64,
   por isso sempre carregam, mesmo fora de um servidor).

   Para adicionar preço: preencha o campo "price" (ex: "R$ 79,90").
   Para adicionar link de compra: preencha o campo "url".
   Para adicionar um produto novo: copie um objeto do array,
   ajuste os campos e adicione a imagem correspondente em
   images-data.js (chave IMAGES.suaChave).
   ========================================================= */

const CATEGORIES = [
  { key:"anime",   label:"Anime & Mangá",        tagline:"Pra quem já chorou com final de temporada." },
  { key:"herois",  label:"Heróis Marvel & DC",    tagline:"Poder, capa e uma dose de justiça." },
  { key:"starwars",label:"Star Wars",             tagline:"Que a força (e o algodão) esteja com você." },
  { key:"pixar",   label:"Disney & Pixar",        tagline:"Nostalgia com estampa boa." },
  { key:"bandas",  label:"Bandas & Rock",         tagline:"Palco, distorção e camiseta preta." },
  { key:"series",  label:"Séries & Animação",     tagline:"Maratona renderizada em tecido." },
  { key:"kawaii",  label:"Kawaii & Sanrio",       tagline:"Fofura com uma pitada de sombrio." },
];

const PRODUCTS = [
  // ANIME & MANGÁ
  { name:"Spy x Family — Dossiê Anya",       category:"anime",   img:IMAGES.spyXFamily,      price:"", url:"#" },
  { name:"Jujutsu Kaisen — Megumi",          category:"anime",   img:IMAGES.jujutsuKaisen,   price:"", url:"#" },
  { name:"Demon Slayer — Tipografia",        category:"anime",   img:IMAGES.demonSlayer,     price:"", url:"#" },
  { name:"Hunter x Hunter — Yorknew City",   category:"anime",   img:IMAGES.hunterXHunter,   price:"", url:"#" },
  { name:"Demon Slayer — Trio",              category:"anime",   img:IMAGES.demonSlayerTrio, price:"", url:"#" },
  { name:"Mangá — Corredor Místico",         category:"anime",   img:IMAGES.mysteryRunner,   price:"", url:"#" },

  // HERÓIS MARVEL & DC
  { name:"Venom — Simbionte",                category:"herois",  img:IMAGES.venom,           price:"", url:"#" },
  { name:"Superman — Superdaddy",            category:"herois",  img:IMAGES.superdaddy,      price:"", url:"#" },
  { name:"Spider-Man — Brand New Day",       category:"herois",  img:IMAGES.spiderman,       price:"", url:"#" },
  { name:"Batman — Capa Clássica",           category:"herois",  img:IMAGES.batman,          price:"", url:"#" },
  { name:"Spider-Man — Além do Aranhaverso",category:"herois",  img:IMAGES.milesSpiderman,  price:"", url:"#" },
  { name:"Supergirl — Unstoppable",          category:"herois",  img:IMAGES.supergirl,       price:"", url:"#" },
  { name:"Iron Man — Kids",                  category:"herois",  img:IMAGES.ironManKids,     price:"", url:"#" },
  { name:"Batman — Psychic Siren",           category:"herois",  img:IMAGES.batmanSecret,    price:"", url:"#" },

  // STAR WARS
  { name:"Boba Fett — Galactic Outlaw",      category:"starwars",img:IMAGES.bobaFett,        price:"", url:"#" },
  { name:"The Mandalorian — This Is The Way",category:"starwars",img:IMAGES.mandalorian,     price:"", url:"#" },
  { name:"Grogu — Little Bounty",            category:"starwars",img:IMAGES.grogu,           price:"", url:"#" },

  // DISNEY & PIXAR
  { name:"Toy Story — Woody & Buzz",         category:"pixar",   img:IMAGES.toyStoryClassic, price:"", url:"#" },
  { name:"Toy Story 5 — Turma Completa",     category:"pixar",   img:IMAGES.toyStory5,       price:"", url:"#" },
  { name:"Toy Story — All The Buzz",         category:"pixar",   img:IMAGES.toyStoryBuzz,    price:"", url:"#" },

  // BANDAS & ROCK
  { name:"Metallica — Guitarra",             category:"bandas",  img:IMAGES.metallica,       price:"", url:"#" },

  // SÉRIES & ANIMAÇÃO
  { name:"Rick and Morty — Portal C-137",    category:"series",  img:IMAGES.rickAndMorty,    price:"", url:"#" },

  // KAWAII & SANRIO
  { name:"Kuromi — Bruxinha",                category:"kawaii",  img:IMAGES.kuromiBanner,    price:"", url:"#" },
  { name:"Kuromi — Painel Retrô",            category:"kawaii",  img:IMAGES.kuromiGrid,      price:"", url:"#" },
  { name:"Kuromi — Cherry Soda",             category:"kawaii",  img:IMAGES.kuromiDrink,     price:"", url:"#" },
  { name:"Kuromi — Com Pochacco",            category:"kawaii",  img:IMAGES.kuromiPlush,     price:"", url:"#" },
  { name:"Hello Kitty — Tokyo Speed",        category:"kawaii",  img:IMAGES.helloKittyTokyo, price:"", url:"#" },
];

/* ---------- RENDER ---------- */

function renderLogos(){
  document.querySelectorAll(".js-logo").forEach(img => { img.src = IMAGES.logo; });
}

function renderNav(){
  const nav = document.getElementById("cat-pills");
  nav.innerHTML = CATEGORIES.map(c => `<a href="#${c.key}">${c.label}</a>`).join("");
}

function renderCatalog(){
  const root = document.getElementById("catalog");
  document.getElementById("stat-total").textContent = PRODUCTS.length;
  document.getElementById("stat-cats").textContent = CATEGORIES.length;

  root.innerHTML = CATEGORIES.map(cat => {
    const items = PRODUCTS.filter(p => p.category === cat.key);
    if(items.length === 0) return "";
    const cards = items.map(p => `
      <article class="card">
        <div class="card-img-wrap">
          <span class="card-chip">${cat.label}</span>
          <img src="${p.img}" alt="${p.name}" loading="lazy">
        </div>
        <div class="card-body">
          <h3>${p.name}</h3>
          <div class="card-footer">
            ${p.price ? `<span class="card-price">${p.price}</span>` : `<span></span>`}
            <a href="${p.url}" class="card-cta">Ver produto</a>
          </div>
        </div>
      </article>
    `).join("");

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
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if(entry.isIntersecting){
      entry.target.classList.add("in-view");
      observer.unobserve(entry.target);
    }
  });
}, { threshold:0.12 });

document.querySelectorAll(".card").forEach(card => observer.observe(card));
