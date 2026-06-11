<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>VOLT — Eletrônicos Premium</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet" />
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --bg:       #0F0F14;
      --surface:  #1A1A24;
      --card:     #22222E;
      --border:   #2E2E3E;
      --blue:     #4F8EF7;
      --blue-dim: #1E3A6E;
      --text:     #F0F0F5;
      --muted:    #8888AA;
      --green:    #3DD68C;
      --red:      #F75A5A;
      --radius:   14px;
    }

    html { scroll-behavior: smooth; }

    body {
      background: var(--bg);
      color: var(--text);
      font-family: 'Inter', sans-serif;
      font-size: 15px;
      line-height: 1.6;
      min-height: 100vh;
    }

    /* ── NAV ── */
    nav {
      position: sticky; top: 0; z-index: 100;
      background: rgba(15,15,20,.85);
      backdrop-filter: blur(18px);
      border-bottom: 1px solid var(--border);
      display: flex; align-items: center; justify-content: space-between;
      padding: 0 5vw;
      height: 64px;
    }
    .logo {
      font-size: 1.5rem; font-weight: 900; letter-spacing: -.04em;
      background: linear-gradient(90deg, var(--blue), #A78BFA);
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .nav-links { display: flex; gap: 2rem; list-style: none; }
    .nav-links a {
      color: var(--muted); text-decoration: none; font-size: .875rem;
      font-weight: 500; transition: color .2s;
    }
    .nav-links a:hover { color: var(--text); }
    .nav-right { display: flex; align-items: center; gap: 1rem; }

    #cart-btn {
      position: relative; background: var(--blue); border: none;
      color: #fff; border-radius: 50px; padding: .5rem 1.25rem;
      font-family: inherit; font-size: .875rem; font-weight: 600;
      cursor: pointer; display: flex; align-items: center; gap: .5rem;
      transition: background .2s, transform .15s;
    }
    #cart-btn:hover { background: #3a7de5; transform: translateY(-1px); }
    #cart-count {
      background: #fff; color: var(--blue);
      border-radius: 50%; width: 20px; height: 20px;
      font-size: .75rem; font-weight: 800;
      display: flex; align-items: center; justify-content: center;
      transition: transform .3s cubic-bezier(.34,1.56,.64,1);
    }
    #cart-count.bump { transform: scale(1.5); }

    /* ── HERO ── */
    .hero {
      padding: 7rem 5vw 5rem;
      display: grid; grid-template-columns: 1fr 1fr;
      align-items: center; gap: 4rem;
      max-width: 1200px; margin: 0 auto;
    }
    .hero-tag {
      display: inline-block; background: var(--blue-dim); color: var(--blue);
      border-radius: 50px; padding: .3rem 1rem;
      font-size: .78rem; font-weight: 700; letter-spacing: .08em;
      text-transform: uppercase; margin-bottom: 1.5rem;
    }
    .hero h1 {
      font-size: clamp(2.4rem, 5vw, 3.6rem);
      font-weight: 900; line-height: 1.08; letter-spacing: -.04em;
      margin-bottom: 1.25rem;
    }
    .hero h1 span { color: var(--blue); }
    .hero p { color: var(--muted); font-size: 1.05rem; margin-bottom: 2rem; max-width: 440px; }
    .btn-primary {
      background: var(--blue); color: #fff; border: none;
      border-radius: 50px; padding: .75rem 2rem;
      font-family: inherit; font-size: .95rem; font-weight: 600;
      cursor: pointer; transition: background .2s, transform .15s;
    }
    .btn-primary:hover { background: #3a7de5; transform: translateY(-2px); }
    .btn-ghost {
      background: transparent; color: var(--muted); border: 1.5px solid var(--border);
      border-radius: 50px; padding: .75rem 1.75rem;
      font-family: inherit; font-size: .95rem; font-weight: 500;
      cursor: pointer; transition: border-color .2s, color .2s;
      margin-left: .75rem;
    }
    .btn-ghost:hover { border-color: var(--blue); color: var(--blue); }
    .hero-visual {
      background: linear-gradient(135deg, var(--surface) 0%, #181824 100%);
      border: 1px solid var(--border); border-radius: 24px;
      height: 340px; display: flex; align-items: center; justify-content: center;
      font-size: 7rem; position: relative; overflow: hidden;
    }
    .hero-visual::before {
      content: '';
      position: absolute; width: 280px; height: 280px;
      background: radial-gradient(circle, rgba(79,142,247,.18) 0%, transparent 70%);
      border-radius: 50%;
    }
    .hero-stats {
      display: flex; gap: 2.5rem; margin-top: 2.5rem;
    }
    .stat { border-left: 2px solid var(--blue); padding-left: .75rem; }
    .stat-num { font-size: 1.5rem; font-weight: 800; }
    .stat-label { font-size: .78rem; color: var(--muted); }

    /* ── SECTION ── */
    section { padding: 4rem 5vw; max-width: 1200px; margin: 0 auto; }
    .section-head {
      display: flex; align-items: baseline; justify-content: space-between;
      margin-bottom: 2rem;
    }
    .section-head h2 { font-size: 1.6rem; font-weight: 800; letter-spacing: -.03em; }
    .see-all {
      color: var(--blue); font-size: .875rem; font-weight: 600;
      text-decoration: none; cursor: pointer; background: none; border: none;
      font-family: inherit;
    }

    /* ── CATEGORIES ── */
    .cats { display: flex; gap: 1rem; flex-wrap: wrap; }
    .cat-pill {
      background: var(--surface); border: 1px solid var(--border);
      border-radius: 50px; padding: .55rem 1.25rem;
      font-size: .85rem; font-weight: 500; cursor: pointer;
      transition: background .2s, border-color .2s, color .2s;
      color: var(--muted);
    }
    .cat-pill.active, .cat-pill:hover {
      background: var(--blue-dim); border-color: var(--blue); color: var(--blue);
    }

    /* ── PRODUCTS GRID ── */
    #products-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
      gap: 1.25rem;
    }

    .product-card {
      background: var(--card); border: 1px solid var(--border);
      border-radius: var(--radius); overflow: hidden;
      transition: transform .25s, box-shadow .25s, border-color .25s;
      cursor: pointer;
      transform-style: preserve-3d;
    }
    .product-card:hover {
      transform: translateY(-6px);
      box-shadow: 0 20px 50px rgba(0,0,0,.4);
      border-color: var(--blue-dim);
    }
    .card-img {
      height: 180px; display: flex; align-items: center; justify-content: center;
      font-size: 4rem;
      background: linear-gradient(135deg, var(--surface), #1a1a28);
      position: relative;
    }
    .badge {
      position: absolute; top: .75rem; left: .75rem;
      background: var(--green); color: #0a2a1a;
      border-radius: 4px; padding: .2rem .55rem;
      font-size: .7rem; font-weight: 700; text-transform: uppercase;
    }
    .badge.hot { background: #F7A24F; color: #2a1200; }
    .badge.sale { background: var(--red); color: #fff; }
    .card-body { padding: 1rem 1.1rem 1.25rem; }
    .card-cat { font-size: .72rem; color: var(--muted); font-weight: 600; text-transform: uppercase; letter-spacing: .06em; }
    .card-name { font-size: 1rem; font-weight: 700; margin: .3rem 0 .15rem; }
    .card-desc { font-size: .8rem; color: var(--muted); line-height: 1.5; margin-bottom: .75rem; }
    .card-rating { display: flex; align-items: center; gap: .3rem; font-size: .8rem; color: #F7C948; margin-bottom: .8rem; }
    .card-rating span { color: var(--muted); }
    .card-footer { display: flex; align-items: center; justify-content: space-between; }
    .price { font-size: 1.25rem; font-weight: 800; }
    .price-old { font-size: .8rem; color: var(--muted); text-decoration: line-through; margin-left: .4rem; font-weight: 400; }
    .add-btn {
      background: var(--blue); color: #fff; border: none;
      border-radius: 8px; padding: .5rem .9rem;
      font-family: inherit; font-size: .8rem; font-weight: 600;
      cursor: pointer; transition: background .2s, transform .15s;
      white-space: nowrap;
    }
    .add-btn:hover { background: #3a7de5; transform: scale(1.05); }
    .add-btn.added { background: var(--green); color: #0a2a1a; }

    /* ── BANNER ── */
    .banner {
      background: linear-gradient(135deg, var(--blue-dim) 0%, #2A1A5E 100%);
      border: 1px solid var(--blue);
      border-radius: 20px; padding: 3rem 3.5rem;
      display: flex; align-items: center; justify-content: space-between;
      gap: 2rem; flex-wrap: wrap;
    }
    .banner h3 { font-size: 1.7rem; font-weight: 800; letter-spacing: -.03em; }
    .banner p { color: rgba(240,240,245,.7); margin-top: .4rem; font-size: .95rem; }
    .banner-emoji { font-size: 3.5rem; }

    /* ── CART DRAWER ── */
    #overlay {
      position: fixed; inset: 0; background: rgba(0,0,0,.6);
      z-index: 200; opacity: 0; pointer-events: none;
      transition: opacity .3s;
    }
    #overlay.open { opacity: 1; pointer-events: all; }

    #cart-drawer {
      position: fixed; top: 0; right: 0; bottom: 0;
      width: min(420px, 100vw);
      background: var(--surface); border-left: 1px solid var(--border);
      z-index: 201; display: flex; flex-direction: column;
      transform: translateX(100%); transition: transform .35s cubic-bezier(.4,0,.2,1);
    }
    #cart-drawer.open { transform: translateX(0); }

    .drawer-head {
      padding: 1.5rem; border-bottom: 1px solid var(--border);
      display: flex; align-items: center; justify-content: space-between;
    }
    .drawer-head h3 { font-size: 1.1rem; font-weight: 700; }
    #close-cart {
      background: none; border: none; color: var(--muted);
      font-size: 1.4rem; cursor: pointer; line-height: 1;
      transition: color .2s;
    }
    #close-cart:hover { color: var(--text); }

    #cart-items { flex: 1; overflow-y: auto; padding: 1rem 1.5rem; }
    .empty-cart {
      text-align: center; color: var(--muted); margin-top: 4rem;
    }
    .empty-cart .big { font-size: 4rem; }
    .empty-cart p { margin-top: .75rem; }

    .cart-item {
      display: flex; align-items: center; gap: 1rem;
      padding: .9rem 0; border-bottom: 1px solid var(--border);
    }
    .ci-icon { font-size: 2.2rem; width: 52px; text-align: center; }
    .ci-info { flex: 1; }
    .ci-name { font-weight: 600; font-size: .9rem; }
    .ci-price { color: var(--blue); font-weight: 700; font-size: .9rem; }
    .ci-controls { display: flex; align-items: center; gap: .5rem; margin-top: .4rem; }
    .qty-btn {
      width: 26px; height: 26px; border-radius: 6px;
      background: var(--card); border: 1px solid var(--border);
      color: var(--text); font-size: 1rem; cursor: pointer;
      display: flex; align-items: center; justify-content: center;
      transition: background .15s;
    }
    .qty-btn:hover { background: var(--border); }
    .qty-num { font-size: .9rem; font-weight: 600; min-width: 20px; text-align: center; }
    .ci-remove {
      background: none; border: none; color: var(--muted);
      cursor: pointer; font-size: 1.1rem; padding: .25rem;
      transition: color .2s;
    }
    .ci-remove:hover { color: var(--red); }

    .drawer-foot {
      padding: 1.25rem 1.5rem; border-top: 1px solid var(--border);
    }
    .subtotal {
      display: flex; justify-content: space-between;
      font-size: 1rem; font-weight: 700; margin-bottom: 1rem;
    }
    .subtotal span:last-child { color: var(--blue); font-size: 1.15rem; }
    #checkout-btn {
      width: 100%; background: var(--blue); color: #fff; border: none;
      border-radius: 12px; padding: .9rem;
      font-family: inherit; font-size: 1rem; font-weight: 700;
      cursor: pointer; transition: background .2s;
    }
    #checkout-btn:hover { background: #3a7de5; }
    #checkout-btn:disabled { background: var(--border); color: var(--muted); cursor: default; }

    /* ── TOAST ── */
    #toast {
      position: fixed; bottom: 2rem; left: 50%; transform: translateX(-50%) translateY(80px);
      background: var(--green); color: #0a2a1a;
      border-radius: 50px; padding: .65rem 1.5rem;
      font-weight: 700; font-size: .9rem; z-index: 300;
      transition: transform .4s cubic-bezier(.34,1.56,.64,1);
      white-space: nowrap;
    }
    #toast.show { transform: translateX(-50%) translateY(0); }

    /* ── FOOTER ── */
    footer {
      border-top: 1px solid var(--border); margin-top: 5rem;
      padding: 2.5rem 5vw;
      display: flex; align-items: center; justify-content: space-between;
      flex-wrap: wrap; gap: 1rem;
    }
    footer p { color: var(--muted); font-size: .85rem; }

    @media (max-width: 768px) {
      .hero { grid-template-columns: 1fr; gap: 2rem; padding: 4rem 5vw 2rem; }
      .hero-visual { display: none; }
      nav .nav-links { display: none; }
    }
  </style>
</head>
<body>

<!-- NAV -->
<nav>
  <div class="logo">VOLT</div>
  <ul class="nav-links">
    <li><a href="#produtos">Produtos</a></li>
    <li><a href="#ofertas">Ofertas</a></li>
    <li><a href="#sobre">Sobre</a></li>
  </ul>
  <div class="nav-right">
    <button id="cart-btn" onclick="toggleCart()">
      🛒 Carrinho
      <span id="cart-count">0</span>
    </button>
  </div>
</nav>

<!-- HERO -->
<div class="hero">
  <div>
    <div class="hero-tag">✦ Novidades 2026</div>
    <h1>Tecnologia que<br><span>transforma</span><br>o seu dia</h1>
    <p>Os melhores eletrônicos com entrega rápida e garantia estendida. Encontre tudo que você precisa em um só lugar.</p>
    <button class="btn-primary" onclick="document.getElementById('produtos').scrollIntoView({behavior:'smooth'})">Ver produtos</button>
    <button class="btn-ghost" onclick="document.getElementById('ofertas').scrollIntoView({behavior:'smooth'})">Ofertas do dia</button>
    <div class="hero-stats">
      <div class="stat"><div class="stat-num">12k+</div><div class="stat-label">clientes satisfeitos</div></div>
      <div class="stat"><div class="stat-num">98%</div><div class="stat-label">avaliações positivas</div></div>
      <div class="stat"><div class="stat-num">24h</div><div class="stat-label">entrega expressa</div></div>
    </div>
  </div>
  <div class="hero-visual">⚡</div>
</div>

<!-- CATEGORIES -->
<section>
  <div class="section-head">
    <h2>Categorias</h2>
  </div>
  <div class="cats" id="cats">
    <button class="cat-pill active" onclick="filterCat('Todos',this)">Todos</button>
    <button class="cat-pill" onclick="filterCat('Áudio',this)">🎧 Áudio</button>
    <button class="cat-pill" onclick="filterCat('Smartphones',this)">📱 Smartphones</button>
    <button class="cat-pill" onclick="filterCat('Notebooks',this)">💻 Notebooks</button>
    <button class="cat-pill" onclick="filterCat('Wearables',this)">⌚ Wearables</button>
    <button class="cat-pill" onclick="filterCat('Acessórios',this)">🔌 Acessórios</button>
  </div>
</section>

<!-- PRODUCTS -->
<section id="produtos">
  <div class="section-head">
    <h2>Produtos</h2>
    <button class="see-all" onclick="filterCat('Todos', document.querySelector('.cat-pill'))">Ver todos →</button>
  </div>
  <div id="products-grid"></div>
</section>

<!-- PROMO BANNER -->
<section id="ofertas" style="padding-top:0">
  <div class="banner">
    <div>
      <h3>Frete grátis em pedidos acima de R$ 299</h3>
      <p>Aproveite! Válido para todo o Brasil até o fim do mês.</p>
    </div>
    <div class="banner-emoji">🚀</div>
    <button class="btn-primary" onclick="document.getElementById('produtos').scrollIntoView({behavior:'smooth'})">Comprar agora</button>
  </div>
</section>

<!-- CART DRAWER -->
<div id="overlay" onclick="toggleCart()"></div>
<div id="cart-drawer">
  <div class="drawer-head">
    <h3>Seu carrinho</h3>
    <button id="close-cart" onclick="toggleCart()">✕</button>
  </div>
  <div id="cart-items"></div>
  <div class="drawer-foot">
    <div class="subtotal">
      <span>Total</span>
      <span id="cart-total">R$ 0,00</span>
    </div>
    <button id="checkout-btn" onclick="checkout()" disabled>Finalizar compra</button>
  </div>
</div>

<!-- TOAST -->
<div id="toast">✓ Adicionado ao carrinho!</div>

<!-- FOOTER -->
<footer>
  <div class="logo">VOLT</div>
  <p>© 2026 VOLT Eletrônicos. Todos os direitos reservados.</p>
  <p style="color:var(--muted)">Feito com ⚡</p>
</footer>

<script>
  /* ── DATA ── */
  const products = [
    { id:1,  name:'AirPods Pro Max', cat:'Áudio',       emoji:'🎧', desc:'Cancelamento ativo de ruído com qualidade de estúdio.', price:1899, old:2299, rating:4.9, reviews:812, badge:'sale' },
    { id:2,  name:'Galaxy S25 Ultra', cat:'Smartphones', emoji:'📱', desc:'Câmera de 200MP, S Pen integrada e IA avançada.', price:6499, old:null, rating:4.8, reviews:1043, badge:'hot' },
    { id:3,  name:'MacBook Air M4',   cat:'Notebooks',   emoji:'💻', desc:'Ultrafino, bateria de 18h e chip M4 ultrarrápido.', price:8999, old:9999, rating:4.9, reviews:590, badge:'sale' },
    { id:4,  name:'Galaxy Watch 7',   cat:'Wearables',   emoji:'⌚', desc:'Monitor cardíaco avançado e GPS sempre ligado.', price:1299, old:1599, rating:4.7, reviews:340, badge:'sale' },
    { id:5,  name:'JBL Charge 6',     cat:'Áudio',       emoji:'🔊', desc:'Som potente à prova d\'água com 30h de bateria.', price:699,  old:899,  rating:4.6, reviews:220, badge:null },
    { id:6,  name:'iPad Pro M4',      cat:'Notebooks',   emoji:'📟', desc:'Tela OLED de 11", chip M4 e Apple Pencil Pro.', price:7499, old:null, rating:4.8, reviews:480, badge:'new' },
    { id:7,  name:'Pixel 9 Pro',      cat:'Smartphones', emoji:'📲', desc:'Câmera computacional do Google com Magic Eraser Pro.', price:4799, old:5299, rating:4.7, reviews:320, badge:'sale' },
    { id:8,  name:'Cabo USB-C 240W',  cat:'Acessórios',  emoji:'🔌', desc:'Carregamento ultra-rápido e transferência de 40Gbps.', price:129,  old:null, rating:4.5, reviews:1200, badge:null },
    { id:9,  name:'Garmin Fenix 8',   cat:'Wearables',   emoji:'🏃', desc:'Smartwatch para atletas com mapa topográfico.', price:3299, old:3799, rating:4.8, reviews:198, badge:'sale' },
    { id:10, name:'Mousepad XL RGB',  cat:'Acessórios',  emoji:'🖱️', desc:'900×400mm com borda costurada e iluminação RGB.', price:189,  old:249,  rating:4.4, reviews:850, badge:null },
    { id:11, name:'Sony WH-1000XM6', cat:'Áudio',       emoji:'🎶', desc:'Melhor noise-cancelling do mercado em 2026.', price:2199, old:2699, rating:5.0, reviews:670, badge:'hot' },
    { id:12, name:'Xiaomi 15 Ultra',  cat:'Smartphones', emoji:'🌟', desc:'Câmera Leica, Snapdragon 8 Elite e 90W de carga.', price:4299, old:4999, rating:4.7, reviews:410, badge:'sale' },
  ];

  let cart = {};
  let activeFilter = 'Todos';

  /* ── RENDER PRODUCTS ── */
  function renderProducts(filter) {
    const grid = document.getElementById('products-grid');
    const list = filter === 'Todos' ? products : products.filter(p => p.cat === filter);
    grid.innerHTML = list.map(p => {
      const inCart = cart[p.id] ? cart[p.id].qty : 0;
      const stars = '★'.repeat(Math.floor(p.rating)) + (p.rating % 1 ? '½' : '');
      const badgeHtml = p.badge
        ? `<div class="badge ${p.badge === 'hot' ? 'hot' : p.badge === 'sale' ? 'sale' : ''}">${p.badge === 'hot' ? '🔥 Mais vendido' : p.badge === 'sale' ? 'Oferta' : 'Novo'}</div>`
        : '';
      return `
      <div class="product-card" id="card-${p.id}">
        <div class="card-img">
          ${badgeHtml}
          <span style="position:relative;z-index:1">${p.emoji}</span>
        </div>
        <div class="card-body">
          <div class="card-cat">${p.cat}</div>
          <div class="card-name">${p.name}</div>
          <div class="card-desc">${p.desc}</div>
          <div class="card-rating">${stars} <span>(${p.reviews})</span></div>
          <div class="card-footer">
            <div>
              <span class="price">${fmt(p.price)}</span>
              ${p.old ? `<span class="price-old">${fmt(p.old)}</span>` : ''}
            </div>
            <butto