#!/usr/bin/env python3
"""
Build script — Toca Geek
Fonte única de dados (CATEGORIES + PRODUCTS). A partir daqui:
  1. Gera data.js (usado pelo catálogo em index.html)
  2. Gera uma página HTML por produto em produtos/{slug}.html

Para adicionar um produto novo:
  - adicione um dict na lista PRODUCTS abaixo
  - garanta que "img_key" exista em IMAGES (images-data.js)
  - rode: python3 build.py
"""
import json
import os

CATEGORIES = [
    {"key": "anime",    "label": "Anime & Mangá",     "tagline": "Pra quem já chorou com final de temporada."},
    {"key": "herois",   "label": "Heróis Marvel & DC", "tagline": "Poder, capa e uma dose de justiça."},
    {"key": "starwars", "label": "Star Wars",          "tagline": "Que a força (e o algodão) esteja com você."},
    {"key": "pixar",    "label": "Disney & Pixar",     "tagline": "Nostalgia com estampa boa."},
    {"key": "bandas",   "label": "Bandas & Rock",      "tagline": "Palco, distorção e camiseta preta."},
    {"key": "series",   "label": "Séries & Animação",  "tagline": "Maratona renderizada em tecido."},
    {"key": "kawaii",   "label": "Kawaii & Sanrio",    "tagline": "Fofura com uma pitada de sombrio."},
]

PRODUCTS = [
    # ---------------- ANIME & MANGÁ ----------------
    {
        "slug": "spy-x-family", "name": "Spy x Family — Dossiê Anya", "category": "anime",
        "img_key": "spyXFamily", "price": "", "url": "#",
        "description": "Spy x Family acompanha o espião Loid Forger, que monta uma família falsa pra cumprir uma missão e acaba se pegando com uma telepata mirim e uma assassina profissional sem saber. Anya, a filha adotiva, é o coração cômico da série — e a estampa brinca com o clima de \"ficha de investigação\" em cima dela.",
    },
    {
        "slug": "jujutsu-kaisen-megumi", "name": "Jujutsu Kaisen — Megumi", "category": "anime",
        "img_key": "jujutsuKaisen", "price": "", "url": "#",
        "description": "Jujutsu Kaisen se passa num mundo onde emoções negativas geram amaldiçoados, e só feiticeiros treinados conseguem enfrentá-los. Megumi Fushiguro é um dos protagonistas: sério, estratégico e dono de uma técnica que invoca sombras de animais pra lutar.",
    },
    {
        "slug": "demon-slayer-tipografia", "name": "Demon Slayer — Tipografia", "category": "anime",
        "img_key": "demonSlayer", "price": "", "url": "#",
        "description": "Demon Slayer conta a jornada de Tanjiro Kamado, que vira caçador de demônios depois que sua família é atacada e sua irmã Nezuko se transforma numa demônia. A estampa aposta na tipografia forte do título com Nezuko ao fundo.",
    },
    {
        "slug": "hunter-x-hunter-yorknew", "name": "Hunter x Hunter — Yorknew City", "category": "anime",
        "img_key": "hunterXHunter", "price": "", "url": "#",
        "description": "Hunter x Hunter segue Gon Freecss em busca do pai desaparecido, cruzando caminho com provas perigosas e leilões clandestinos na Yorknew City — um dos arcos mais queridos pelos fãs. A estampa retrata o elenco reunido nesse cenário urbano.",
    },
    {
        "slug": "demon-slayer-trio", "name": "Demon Slayer — Trio", "category": "anime",
        "img_key": "demonSlayerTrio", "price": "", "url": "#",
        "description": "Essa estampa reúne o trio mais icônico de Demon Slayer: Tanjiro, Nezuko e Zenitsu — o corajoso, a protetora e o covarde que só fica forte quando dorme. Uma homenagem colorida ao time que carrega boa parte do humor e da emoção da série.",
    },
    {
        "slug": "corredor-mistico", "name": "Mangá — Corredor Místico", "category": "anime",
        "img_key": "mysteryRunner", "price": "", "url": "#",
        "description": "Estampa discreta no peito com um personagem em plena corrida, num traço que remete aos mangás de ação e aventura. Perfeita pra quem gosta de um toque geek mais sutil no dia a dia.",
    },

    # ---------------- HERÓIS MARVEL & DC ----------------
    {
        "slug": "venom", "name": "Venom — Simbionte", "category": "herois",
        "img_key": "venom", "price": "", "url": "#",
        "description": "Venom nasceu quando um simbionte alienígena se uniu ao jornalista Eddie Brock, criando um dos anti-heróis mais icônicos da Marvel — forte, instável e com um apetite peculiar. A estampa captura bem o caos orgânico do personagem.",
    },
    {
        "slug": "superman-superdaddy", "name": "Superman — Superdaddy", "category": "herois",
        "img_key": "superdaddy", "price": "", "url": "#",
        "description": "Um clássico: Superman, o Homem de Aço, com seus poderes listados como se fosse uma ficha técnica — visão de raio-X, voo, força e invulnerabilidade. A brincadeira \"Superdaddy\" é perfeita pra pais geek que também são super-heróis em casa.",
    },
    {
        "slug": "spider-man-brand-new-day", "name": "Spider-Man — Brand New Day", "category": "herois",
        "img_key": "spiderman", "price": "", "url": "#",
        "description": "Peter Parker balança entre a vida normal e as responsabilidades de ser o Homem-Aranha, sempre com aquele humor ácido no meio da ação. A estampa remete à estética clássica de quadrinho, com o icônico \"THWIP\" das teias.",
    },
    {
        "slug": "batman-classico", "name": "Batman — Capa Clássica", "category": "herois",
        "img_key": "batman", "price": "", "url": "#",
        "description": "Bruce Wayne veste o capuz à noite pra proteger Gotham City, sem superpoderes — só disciplina, tecnologia e trauma bem administrado. Essa arte resgata o visual clássico de HQ do Cavaleiro das Trevas.",
    },
    {
        "slug": "miles-morales", "name": "Spider-Man — Além do Aranhaverso", "category": "herois",
        "img_key": "milesSpiderman", "price": "", "url": "#",
        "description": "Miles Morales é o Homem-Aranha que expandiu o conceito de multiverso pros quadrinhos e telas — cada versão dele com um traço e personalidade únicos. A estampa reúne várias dessas variantes ao redor do protagonista.",
    },
    {
        "slug": "supergirl-unstoppable", "name": "Supergirl — Unstoppable", "category": "herois",
        "img_key": "supergirl", "price": "", "url": "#",
        "description": "Kara Zor-El, prima de Superman, cresceu escondendo seus poderes até assumir o manto de Supergirl. \"Unstoppable\" resume bem o espírito da personagem: determinação que não aceita \"não\" como resposta.",
    },
    {
        "slug": "iron-man-kids", "name": "Iron Man — Kids", "category": "herois",
        "img_key": "ironManKids", "price": "", "url": "#",
        "description": "Tony Stark é o gênio bilionário que constrói sua própria armadura pra virar o Homem de Ferro — ícone de tecnologia e ironia fina no time dos Vingadores. Versão descomplicada e colorida, pensada pro público infantil.",
    },
    {
        "slug": "batman-psychic-siren", "name": "Batman — Psychic Siren", "category": "herois",
        "img_key": "batmanSecret", "price": "", "url": "#",
        "description": "Inspirada nas capas clássicas de HQ, essa estampa traz o Batman em pleno voo sobre Gotham, remetendo às histórias policiais e misteriosas que marcaram o personagem desde os anos 1940.",
    },

    # ---------------- STAR WARS ----------------
    {
        "slug": "boba-fett", "name": "Boba Fett — Galactic Outlaw", "category": "starwars",
        "img_key": "bobaFett", "price": "", "url": "#",
        "description": "Boba Fett é o caçador de recompensas mais temido da galáxia de Star Wars — capacete mandaloriano, blaster na cintura e fama de nunca falhar um contrato. \"Galactic Outlaw\" resume bem essa reputação fora da lei.",
    },
    {
        "slug": "mandalorian-this-is-the-way", "name": "The Mandalorian — This Is The Way", "category": "starwars",
        "img_key": "mandalorian", "price": "", "url": "#",
        "description": "The Mandalorian segue Din Djarin, um caçador de recompensas que assume o dever de proteger a pequena criatura conhecida como Grogu. \"This Is The Way\" é o lema mandaloriano — código de honra acima de tudo.",
    },
    {
        "slug": "grogu-little-bounty", "name": "Grogu — Little Bounty", "category": "starwars",
        "img_key": "grogu", "price": "", "url": "#",
        "description": "Grogu, da mesma espécie de Yoda, virou um dos personagens mais amados do universo Star Wars por misturar fofura com um poder incrível na Força. Aqui ele aparece aconchegado no colo do Mandaloriano.",
    },

    # ---------------- DISNEY & PIXAR ----------------
    {
        "slug": "toy-story-classico", "name": "Toy Story — Woody & Buzz", "category": "pixar",
        "img_key": "toyStoryClassic", "price": "", "url": "#",
        "description": "Toy Story acompanha os brinquedos do quarto do Andy, com o xerife Woody e o astronauta Buzz Lightyear como dupla central — dois líderes que aprendem a dividir o protagonismo. Uma estampa clássica do início dessa amizade.",
    },
    {
        "slug": "toy-story-5", "name": "Toy Story 5 — Turma Completa", "category": "pixar",
        "img_key": "toyStory5", "price": "", "url": "#",
        "description": "Toy Story 5 dá continuidade às aventuras dos brinquedos, reunindo Woody, Buzz, Jessie e a turma em novas confusões. A estampa celebra o elenco completo desse novo capítulo da franquia.",
    },
    {
        "slug": "toy-story-buzz", "name": "Toy Story — All The Buzz", "category": "pixar",
        "img_key": "toyStoryBuzz", "price": "", "url": "#",
        "description": "Buzz Lightyear é o astronauta que jura nunca desistir de uma missão — mesmo achando, por boa parte do primeiro filme, que era um Ranger Espacial de verdade. \"All The Buzz\" é só um trocadilho pra celebrar o personagem em modo repetição.",
    },

    # ---------------- BANDAS & ROCK ----------------
    {
        "slug": "metallica", "name": "Metallica — Guitarra", "category": "bandas",
        "img_key": "metallica", "price": "", "url": "#",
        "description": "Metallica é uma das bandas mais influentes do heavy metal, com riffs pesados e décadas de shows lotados ao redor do mundo. A estampa traz a guitarra como símbolo máximo dessa sonoridade.",
    },

    # ---------------- SÉRIES & ANIMAÇÃO ----------------
    {
        "slug": "rick-and-morty", "name": "Rick and Morty — Portal C-137", "category": "series",
        "img_key": "rickAndMorty", "price": "", "url": "#",
        "description": "Rick and Morty segue um cientista genial e cínico e seu neto ansioso em viagens interdimensionais que misturam humor ácido com ficção científica pesada. O portal verde é a marca registrada da dupla.",
    },

    # ---------------- KAWAII & SANRIO ----------------
    {
        "slug": "kuromi-bruxinha", "name": "Kuromi — Bruxinha", "category": "kawaii",
        "img_key": "kuromiBanner", "price": "", "url": "#",
        "description": "Kuromi é a rival fofa-e-rebelde da Sanrio, sempre com seu gorrinho preto de caveira e um quê de travessura. Aqui ela aparece em clima de bruxinha, com direito a xícara de chá.",
    },
    {
        "slug": "kuromi-painel-retro", "name": "Kuromi — Painel Retrô", "category": "kawaii",
        "img_key": "kuromiGrid", "price": "", "url": "#",
        "description": "Um painel estilo pôster retrô reúne Kuromi e amigos em composições gráficas inspiradas na estética Y2K que voltou com tudo. Ideal pra quem curte o universo Sanrio com uma pegada mais alternativa.",
    },
    {
        "slug": "kuromi-cherry-soda", "name": "Kuromi — Cherry Soda", "category": "kawaii",
        "img_key": "kuromiDrink", "price": "", "url": "#",
        "description": "Kuromi relaxando dentro de um copo de refrigerante com cereja — a fofura açucarada que é a cara da linha kawaii da Sanrio, num visual doce e colorido.",
    },
    {
        "slug": "kuromi-pochacco", "name": "Kuromi — Com Pochacco", "category": "kawaii",
        "img_key": "kuromiPlush", "price": "", "url": "#",
        "description": "Kuromi aparece ao lado de Pochacco, o cachorrinho branco e travesso da Sanrio, numa combinação que já virou clássica entre os fãs da marca.",
    },
    {
        "slug": "hello-kitty-tokyo-speed", "name": "Hello Kitty — Tokyo Speed", "category": "kawaii",
        "img_key": "helloKittyTokyo", "price": "", "url": "#",
        "description": "Hello Kitty é o maior ícone da Sanrio, presente em produtos ao redor do mundo desde os anos 1970. Nessa versão \"Tokyo Speed\", ela ganha uma estética de corrida urbana japonesa, cheia de referências ao motorsport.",
    },
]

INSTAGRAM_URL = "https://www.instagram.com/toca_geekt/"

CAT_BY_KEY = {c["key"]: c for c in CATEGORIES}


def js_string(s: str) -> str:
    """Escape a Python string for safe embedding inside a JS double-quoted string."""
    return json.dumps(s, ensure_ascii=False)


def build_data_js(path: str):
    lines = ["const CATEGORIES = ["]
    for c in CATEGORIES:
        lines.append(
            f'  {{ key:{js_string(c["key"])}, label:{js_string(c["label"])}, '
            f'tagline:{js_string(c["tagline"])} }},'
        )
    lines.append("];\n")

    lines.append("const PRODUCTS = [")
    for p in PRODUCTS:
        lines.append(
            "  { "
            f'slug:{js_string(p["slug"])}, '
            f'name:{js_string(p["name"])}, '
            f'category:{js_string(p["category"])}, '
            f'img:IMAGES.{p["img_key"]}, '
            f'price:{js_string(p["price"])}, '
            f'url:{js_string(p["url"])}, '
            f'description:{js_string(p["description"])} '
            "},"
        )
    lines.append("];\n")
    lines.append(f'const INSTAGRAM_URL = {js_string(INSTAGRAM_URL)};')

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"[ok] {path}")


PRODUCT_PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{name} — Toca Geek</title>
<meta name="description" content="{description_attr}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bungee&family=Space+Grotesk:wght@500;600;700&family=Space+Mono:wght@400;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../styles.css">
</head>
<body>

<header class="site-nav">
  <div class="nav-inner">
    <a href="../index.html" class="brand">
      <img class="js-logo" alt="Toca Geek">
      <span>TOCA <em>GEEK</em></span>
    </a>
    <a href="../index.html#{category_key}" class="back-link">&larr; Voltar ao catálogo</a>
  </div>
</header>

<main>
  <section class="product-page wrap">
    <p class="breadcrumb">
      <a href="../index.html">Início</a>
      <span>/</span>
      <a href="../index.html#{category_key}">{category_label}</a>
      <span>/</span>
      <span class="breadcrumb-current">{name}</span>
    </p>

    <div class="product-grid">
      <div class="product-image-wrap">
        <span class="card-chip">{category_label}</span>
        <img src="{img_placeholder}" alt="{name}" class="js-product-img">
      </div>

      <div class="product-info">
        <h1>{name}</h1>
        {price_block}
        <p class="product-description">{description}</p>
        <div class="product-ctas">
          <a href="{url}" class="btn-primary js-buy-link">Comprar agora</a>
          <a href="../index.html#{category_key}" class="btn-ghost">Ver mais da seção</a>
        </div>
      </div>
    </div>

    <div class="related-block">
      <div class="section-head">
        <div class="section-head-left">
          <span class="section-tag">// Você também pode gostar</span>
          <h2>Mais de {category_label}</h2>
        </div>
      </div>
      <div class="grid grid-related" id="related-grid"></div>
    </div>
  </section>
</main>

<footer>
  <div class="wrap footer-inner">
    <div class="footer-brand">
      <img class="js-logo" alt="Toca Geek">
      <span>TOCA GEEK</span>
    </div>
    <p class="footer-note">Base do site gerada pra evoluir no Fable 5. Preços e links de compra: edite build.py e rode de novo.</p>
  </div>
</footer>

<button id="social-fab" aria-label="Redes sociais da Toca Geek" title="Siga a Toca Geek">
  <svg viewBox="0 0 24 24" width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="2.5" y="2.5" width="19" height="19" rx="6" stroke="white" stroke-width="1.6"/>
    <circle cx="12" cy="12" r="4.6" stroke="white" stroke-width="1.6"/>
    <circle cx="17.6" cy="6.4" r="1.1" fill="white"/>
  </svg>
</button>

<div id="social-modal-backdrop">
  <div id="social-modal" role="dialog" aria-modal="true" aria-labelledby="social-modal-title">
    <button id="social-modal-close" aria-label="Fechar">&times;</button>
    <div class="social-modal-icon">
      <svg viewBox="0 0 24 24" width="30" height="30" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect x="2.5" y="2.5" width="19" height="19" rx="6" stroke="white" stroke-width="1.6"/>
        <circle cx="12" cy="12" r="4.6" stroke="white" stroke-width="1.6"/>
        <circle cx="17.6" cy="6.4" r="1.1" fill="white"/>
      </svg>
    </div>
    <h3 id="social-modal-title">Siga a Toca Geek</h3>
    <p>Lançamentos, promoções e a raposa aprontando nos stories — tudo primeiro por lá.</p>
    <span class="social-handle">@toca_geekt</span>
    <a id="social-modal-link" href="{instagram_url}" target="_blank" rel="noopener noreferrer" class="btn-primary">Abrir Instagram</a>
  </div>
</div>

<script src="../images-data.js"></script>
<script src="../data.js"></script>
<script>window.CURRENT_PRODUCT_SLUG = {slug_json};</script>
<script src="../product.js"></script>
<script src="../social.js"></script>

</body>
</html>
"""


def build_product_pages(out_dir: str):
    os.makedirs(out_dir, exist_ok=True)
    for p in PRODUCTS:
        cat = CAT_BY_KEY[p["category"]]
        price_block = f'<p class="product-price">{p["price"]}</p>' if p["price"] else ""
        html = PRODUCT_PAGE_TEMPLATE.format(
            name=p["name"],
            description=p["description"],
            description_attr=p["description"].replace('"', "&quot;"),
            category_key=cat["key"],
            category_label=cat["label"],
            img_placeholder="",  # filled client-side from IMAGES to avoid duplicating base64 in every page
            price_block=price_block,
            url=p["url"],
            instagram_url=INSTAGRAM_URL,
            slug_json=js_string(p["slug"]),
        )
        out_path = os.path.join(out_dir, f'{p["slug"]}.html')
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
    print(f"[ok] {len(PRODUCTS)} páginas geradas em {out_dir}/")


if __name__ == "__main__":
    base = os.path.dirname(os.path.abspath(__file__))
    print(f"{len(CATEGORIES)} categorias, {len(PRODUCTS)} produtos carregados.")
    build_data_js(os.path.join(base, "data.js"))
    build_product_pages(os.path.join(base, "produtos"))
