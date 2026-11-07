---
outline: false
---

<style>
.rwd {
  --ink: #0b0b0d;
  --panel: #17171a;
  --panel2: #1f1f23;
  --line: #2f2f36;
  --text: #f4f4f5;
  --mute: #a1a1aa;
  --red: #ef4444;
  --red-deep: #b91c1c;
  --red-soft: rgba(239, 68, 68, 0.14);
  --gold: #f5b931;
  width: 960px;
  max-width: 100%;
  margin: 0 auto;
  color: var(--text);
  font-family: Inter, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.rwd *, .rwd *::before, .rwd *::after { box-sizing: border-box; }
.rwd p, .rwd li { line-height: 1.6; color: var(--text); margin: 0; }
.rwd ul, .rwd ol { list-style: none; padding: 0; margin: 0; }
.rwd li + li { margin-top: 0; }
.rwd b { color: #fff; font-weight: 650; }
.rwd a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.rwd a:hover { color: #fecaca; }
.rwd a:focus-visible { outline: 3px solid var(--red); outline-offset: 3px; border-radius: 6px; }
.rwd kbd, .rwd code.rwd-cmd {
  font: inherit; font-size: 0.88em; font-weight: 700; color: #fff; background: var(--red-deep);
  border-radius: 6px; padding: 0.05rem 0.45rem;
}
/* ---------- hero ---------- */
.rwd .rwd-hero {
  position: relative; overflow: hidden; isolation: isolate;
  background: radial-gradient(90% 120% at 100% 0%, rgba(245, 185, 49, 0.14), transparent 55%),
              radial-gradient(110% 120% at 0% 100%, rgba(185, 28, 28, 0.3), var(--ink) 62%);
  border: 1px solid var(--line); border-radius: 22px;
  padding: clamp(1.15rem, 4vw, 2.4rem);
}
.rwd .rwd-kicker { font-size: 0.78rem; font-weight: 700; letter-spacing: 0.16em; text-transform: uppercase; color: var(--red); margin-bottom: 0.55rem; }
.rwd .rwd-hero h1 {
  margin: 0 0 0.75rem; border: 0; padding: 0;
  font-size: clamp(2rem, 6.4vw, 3.4rem); line-height: 1.04; font-weight: 800; letter-spacing: -0.03em; color: #fff;
}
.rwd .rwd-hero h1 span { color: var(--gold); }
.rwd .rwd-lede { max-width: 58ch; color: var(--mute); font-size: 1.05rem; }
.rwd .rwd-track { display: block; width: 100%; height: auto; margin-top: 1.3rem; }
.rwd-track .rail { fill: #27272a; }
.rwd-track .fill { fill: url(#rwd-fill); }
.rwd-track .wipe { transform-box: fill-box; transform-origin: left center; animation: rwd-wipe 12s cubic-bezier(.4, .1, .4, 1) infinite; }
@keyframes rwd-wipe { 0% { transform: scaleX(0); } 78%, 94% { transform: scaleX(1); } 100% { transform: scaleX(1); } }
.rwd-track .lit { animation: rwd-lit 12s linear infinite; }
@keyframes rwd-lit { 0%, 94% { opacity: 1; } 99%, 100% { opacity: 0; } }
.rwd-track .box { fill: #1f1f23; stroke: #3f3f46; stroke-width: 1.5; }
.rwd-track .rib { fill: #3f3f46; }
.rwd-track .lbox { fill: var(--red-deep); stroke: #fca5a5; stroke-width: 1.5; }
.rwd-track .lrib { fill: var(--gold); }
.rwd-track .chest { fill: #3b2a0a; stroke: var(--gold); stroke-width: 2; }
.rwd-track .t { fill: var(--mute); font: 600 11px Inter, system-ui, sans-serif; text-anchor: middle; }
.rwd-track .glow { fill: none; stroke: var(--gold); stroke-width: 2; transform-box: fill-box; transform-origin: center; opacity: 0; animation: rwd-glow 12s ease-out infinite; }
@keyframes rwd-glow { 0%, 76% { opacity: 0; transform: scale(0.8); } 80% { opacity: 0.9; transform: scale(1); } 92% { opacity: 0; transform: scale(1.5); } 100% { opacity: 0; } }
.rwd .rwd-days { display: flex; flex-wrap: wrap; gap: 0.3rem; margin-top: 1rem; align-items: center; }
.rwd .rwd-days .lab { font-size: 0.72rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: var(--mute); margin-right: 0.35rem; }
.rwd .rwd-days i {
  width: 1.55rem; height: 1.55rem; border-radius: 7px; display: grid; place-items: center;
  font-style: normal; font-size: 0.66rem; font-weight: 800; color: #71717a;
  background: var(--panel2); border: 1px solid var(--line);
  animation: rwd-day 8s ease-in-out infinite;
}
@keyframes rwd-day { 0%, 6% { background: var(--panel2); color: #71717a; border-color: var(--line); } 12%, 80% { background: var(--red-deep); color: #fff; border-color: #f87171; } 90%, 100% { background: var(--panel2); color: #71717a; border-color: var(--line); } }
.rwd .rwd-days i:nth-of-type(2) { animation-delay: 0.2s; } .rwd .rwd-days i:nth-of-type(3) { animation-delay: 0.4s; }
.rwd .rwd-days i:nth-of-type(4) { animation-delay: 0.6s; } .rwd .rwd-days i:nth-of-type(5) { animation-delay: 0.8s; }
.rwd .rwd-days i:nth-of-type(6) { animation-delay: 1s; } .rwd .rwd-days i:nth-of-type(7) { animation-delay: 1.2s; }
.rwd .rwd-days i:nth-of-type(8) { animation-delay: 1.4s; } .rwd .rwd-days i:nth-of-type(9) { animation-delay: 1.6s; }
.rwd .rwd-days i:nth-of-type(10) { animation-delay: 1.8s; } .rwd .rwd-days i:nth-of-type(11) { animation-delay: 2s; }
.rwd .rwd-days i:nth-of-type(12) { animation-delay: 2.2s; } .rwd .rwd-days i:nth-of-type(13) { animation-delay: 2.4s; }
.rwd .rwd-days i:nth-of-type(14) { animation-delay: 2.6s; } .rwd .rwd-days i:nth-of-type(15) { animation-delay: 2.8s; }
.rwd .rwd-facts { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 130px), 1fr)); gap: 0.6rem; margin-top: 1.2rem; }
.rwd .rwd-facts li { background: rgba(23, 23, 26, 0.85); border: 1px solid var(--line); border-radius: 14px; padding: 0.7rem 0.9rem; }
.rwd .rwd-facts b { display: block; font-size: clamp(1.25rem, 4vw, 1.6rem); line-height: 1.1; font-weight: 800; color: #fff; }
.rwd .rwd-facts span { display: block; color: var(--mute); font-size: 0.82rem; line-height: 1.35; margin-top: 0.2rem; }
@media (prefers-reduced-motion: reduce) {
  .rwd-track .wipe, .rwd-track .lit, .rwd-track .glow, .rwd .rwd-days i { animation: none; }
  .rwd-track .wipe { transform: none; }
  .rwd .rwd-days i { background: var(--red-deep); color: #fff; border-color: #f87171; }
}
/* ---------- sections ---------- */
.rwd .rwd-h2 {
  display: flex; align-items: center; gap: 0.65rem;
  margin: 3rem 0 0.9rem; border: 0; padding: 0;
  font-size: 1.5rem; font-weight: 750; letter-spacing: -0.015em; line-height: 1.25; color: #fff;
}
.rwd .rwd-h2::before {
  content: ''; flex: none; width: 0.6rem; height: 0.6rem; border-radius: 2px; background: var(--red);
  transform: rotate(45deg); box-shadow: 0 0 0 4px var(--red-soft);
}
.rwd .rwd-intro { color: var(--mute); max-width: 68ch; margin-bottom: 1rem; }
.rwd .rwd-card { background: var(--panel); border: 1px solid var(--line); border-radius: 18px; padding: 1.1rem 1.2rem; }
.rwd .rwd-h3 { margin: 0 0 0.55rem; border: 0; padding: 0; font-size: 1.08rem; font-weight: 750; color: #fff; line-height: 1.3; }
.rwd .rwd-list li { position: relative; padding-left: 1.1rem; color: #d4d4d8; }
.rwd .rwd-list li + li { margin-top: 0.4rem; }
.rwd .rwd-list li::before { content: ''; position: absolute; left: 0; top: 0.62em; width: 6px; height: 6px; border-radius: 50%; background: var(--red); }
/* steps */
.rwd .rwd-steps { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr)); gap: 0.7rem; counter-reset: rwd; }
.rwd .rwd-steps li { position: relative; background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 2.6rem 1rem 1rem; counter-increment: rwd; }
.rwd .rwd-steps li::before {
  content: counter(rwd); position: absolute; top: 0.8rem; left: 1rem;
  width: 1.6rem; height: 1.6rem; border-radius: 8px; display: grid; place-items: center;
  font-weight: 800; font-size: 0.9rem; color: #fff; background: var(--red-deep);
}
.rwd .rwd-steps b { display: block; margin-bottom: 0.2rem; }
.rwd .rwd-steps span { color: var(--mute); font-size: 0.92rem; }
/* tiers timeline */
.rwd .rwd-tiers { position: relative; display: grid; gap: 0.55rem; padding-left: 1.6rem; }
.rwd .rwd-tiers::before { content: ''; position: absolute; left: 0.45rem; top: 0.6rem; bottom: 0.6rem; width: 2px; background: linear-gradient(var(--red), var(--gold)); border-radius: 2px; }
.rwd .rwd-tier { position: relative; display: flex; flex-wrap: wrap; align-items: center; gap: 0.5rem 0.9rem; background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 0.7rem 0.9rem; }
.rwd .rwd-tier::before { content: ''; position: absolute; left: -1.45rem; top: 50%; width: 0.75rem; height: 0.75rem; margin-top: -0.375rem; border-radius: 50%; background: var(--ink); border: 2px solid var(--red); }
.rwd .rwd-tier.top { border-color: rgba(245, 185, 49, 0.55); background: linear-gradient(110deg, rgba(245, 185, 49, 0.1), var(--panel) 55%); }
.rwd .rwd-tier.top::before { border-color: var(--gold); background: var(--gold); }
.rwd .rwd-time { flex: 0 0 5.2rem; font-weight: 800; font-size: 1.05rem; color: #fff; font-variant-numeric: tabular-nums; }
.rwd .rwd-items { display: flex; flex-wrap: wrap; gap: 0.35rem; }
.rwd .rwd-item { font-size: 0.84rem; font-weight: 600; color: #e4e4e7; background: var(--panel2); border: 1px solid var(--line); border-radius: 999px; padding: 0.18rem 0.65rem; }
.rwd .rwd-item.cash { color: #bbf7d0; border-color: rgba(74, 222, 128, 0.4); }
/* streak */
.rwd .rwd-streak { display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 0.5rem; align-items: end; margin-top: 0.4rem; }
.rwd .rwd-step { display: flex; flex-direction: column; justify-content: flex-end; gap: 0.3rem; text-align: center; }
.rwd .rwd-bar { border-radius: 10px 10px 4px 4px; background: linear-gradient(180deg, var(--gold), var(--red-deep)); opacity: 0.9; }
.rwd .rwd-step:nth-child(1) .rwd-bar { height: 1.2rem; opacity: 0.45; }
.rwd .rwd-step:nth-child(2) .rwd-bar { height: 2.4rem; opacity: 0.6; }
.rwd .rwd-step:nth-child(3) .rwd-bar { height: 3.6rem; opacity: 0.72; }
.rwd .rwd-step:nth-child(4) .rwd-bar { height: 4.8rem; opacity: 0.85; }
.rwd .rwd-step:nth-child(5) .rwd-bar { height: 6.2rem; }
.rwd .rwd-step b { font-size: 0.95rem; }
.rwd .rwd-step span { font-size: 0.75rem; color: var(--mute); }
/* happy hour */
.rwd .rwd-hh { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr)); gap: 0.8rem; }
.rwd .rwd-acts { display: flex; flex-wrap: wrap; gap: 0.35rem; margin-top: 0.4rem; }
.rwd .rwd-act { font-size: 0.84rem; font-weight: 600; color: #e4e4e7; background: var(--panel2); border: 1px solid var(--line); border-left: 3px solid var(--c); border-radius: 8px; padding: 0.2rem 0.6rem; }
.rwd .rwd-sub { font-size: 0.72rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: var(--mute); margin-top: 0.9rem; }
.rwd .rwd-sub:first-child { margin-top: 0; }
.rwd .rwd-see { display: flex; flex-wrap: wrap; gap: 0.6rem; margin-top: 0.4rem; }
.rwd .rwd-see a {
  display: inline-flex; flex-direction: column; text-decoration: none; min-width: 12rem;
  background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 0.7rem 0.95rem;
}
.rwd .rwd-see a:hover { border-color: var(--red); color: #fff; }
.rwd .rwd-see a span { font-size: 0.85rem; color: var(--mute); }
@media (max-width: 520px) {
  .rwd .rwd-time { flex-basis: 100%; }
  .rwd .rwd-step span { font-size: 0.68rem; }
  .rwd .rwd-see a { flex: 1 1 100%; }
}
</style>

<div class="rwd">
<header class="rwd-hero">
<p class="rwd-kicker">Sisteme generale</p>
<h1>Premii <span>zilnice</span></h1>
<p class="rwd-lede">Cu cat joci mai mult intr-o zi, cu atat iei mai multe premii. Scrie <code class="rwd-cmd">/premii</code> ca sa vezi cat ai jucat azi si ce poti revendica.</p>
<svg class="rwd-track" viewBox="0 0 640 150" role="img" aria-label="Bara timpului jucat azi, cu opt premii pe drum pana la 12 ore">
<defs>
<linearGradient id="rwd-fill" x1="0" x2="1"><stop offset="0" stop-color="#b91c1c"/><stop offset="1" stop-color="#f5b931"/></linearGradient>
<clipPath id="rwd-clip"><rect class="wipe" x="20" y="0" width="600" height="150"/></clipPath>
<g id="rwd-gift"><rect x="-13" y="-9" width="26" height="20" rx="3"/><rect x="-15" y="-15" width="30" height="7" rx="2"/></g>
</defs>
<rect class="rail" x="20" y="96" width="600" height="8" rx="4"/>
<g fill="#1f1f23" stroke="#3f3f46" stroke-width="1.5">
<use href="#rwd-gift" x="62" y="62"/><use href="#rwd-gift" x="132" y="62"/><use href="#rwd-gift" x="202" y="62"/><use href="#rwd-gift" x="272" y="62"/><use href="#rwd-gift" x="342" y="62"/><use href="#rwd-gift" x="412" y="62"/><use href="#rwd-gift" x="482" y="62"/>
</g>
<path class="box" d="M556 46h52v32h-52z M552 36h60v12h-60z"/>
<g clip-path="url(#rwd-clip)">
<g class="lit">
<rect class="fill" x="20" y="96" width="600" height="8" rx="4"/>
<g fill="#b91c1c" stroke="#fca5a5" stroke-width="1.5">
<use href="#rwd-gift" x="62" y="62"/><use href="#rwd-gift" x="132" y="62"/><use href="#rwd-gift" x="202" y="62"/><use href="#rwd-gift" x="272" y="62"/><use href="#rwd-gift" x="342" y="62"/><use href="#rwd-gift" x="412" y="62"/><use href="#rwd-gift" x="482" y="62"/>
</g>
<g class="lrib"><rect x="60" y="47" width="4" height="26"/><rect x="130" y="47" width="4" height="26"/><rect x="200" y="47" width="4" height="26"/><rect x="270" y="47" width="4" height="26"/><rect x="340" y="47" width="4" height="26"/><rect x="410" y="47" width="4" height="26"/><rect x="480" y="47" width="4" height="26"/></g>
<path class="chest" d="M556 46h52v32h-52z M552 36h60v12h-60z"/>
<rect class="lrib" x="579" y="36" width="6" height="42"/>
</g>
</g>
<circle class="glow" cx="582" cy="58" r="34"/>
<g class="t"><text x="62" y="126">30m</text><text x="132" y="126">1h</text><text x="202" y="126">2h</text><text x="272" y="126">4h</text><text x="342" y="126">6h</text><text x="412" y="126">8h</text><text x="482" y="126">10h</text><text x="582" y="126">12h</text></g>
</svg>
<div class="rwd-days" aria-hidden="true"><span class="lab">Serie</span><i>1</i><i>2</i><i>3</i><i>4</i><i>5</i><i>6</i><i>7</i><i>8</i><i>9</i><i>10</i><i>11</i><i>12</i><i>13</i><i>14</i><i>15</i></div>
<ul class="rwd-facts">
<li><b>8</b><span>praguri de timp jucat pe zi</span></li>
<li><b>12 ore</b><span>ultimul prag, cu EliteBox</span></li>
<li><b>00:00</b><span>totul o ia de la capat (ora Romaniei)</span></li>
<li><b>15+ zile</b><span>serie la rand pentru cel mai mare bonus</span></li>
</ul>
</header>
<h2 class="rwd-h2" id="cum-functioneaza">Cum functioneaza</h2>
<ol class="rwd-steps">
<li><b>Joci</b><span>Se aduna timpul jucat azi. Cat esti AFK sau dormi, nu se numara.</span></li>
<li><b>Deschizi /premii</b><span>Vezi cat ai jucat si cat mai ai pana la urmatorul premiu.</span></li>
<li><b>Revendici</b><span>Apesi pe premiu cand ai atins pragul. Le iei in ordine, de la primul.</span></li>
<li><b>A doua zi</b><span>La miezul noptii timpul revine la zero si poti lua din nou toate premiile.</span></li>
</ol>
<h2 class="rwd-h2" id="premii">Ce primesti</h2>
<p class="rwd-intro">Fiecare prag inseamna timp jucat in aceeasi zi. La toate primesti si bani cash. Cantitatile le vezi in <code class="rwd-cmd">/premii</code>.</p>
<div class="rwd-tiers">
<div class="rwd-tier"><span class="rwd-time">30 min</span><span class="rwd-items"><span class="rwd-item">Bandaj</span><span class="rwd-item cash">Bani cash</span></span></div>
<div class="rwd-tier"><span class="rwd-time">1 ora</span><span class="rwd-items"><span class="rwd-item">Cola</span><span class="rwd-item">Tigari</span><span class="rwd-item cash">Bani cash</span></span></div>
<div class="rwd-tier"><span class="rwd-time">2 ore</span><span class="rwd-items"><span class="rwd-item">Baton Snikkel</span><span class="rwd-item">Lockpick simplu</span><span class="rwd-item">Tigari</span><span class="rwd-item cash">Bani cash</span></span></div>
<div class="rwd-tier"><span class="rwd-time">4 ore</span><span class="rwd-items"><span class="rwd-item">Telefon</span><span class="rwd-item cash">Bani cash</span></span></div>
<div class="rwd-tier"><span class="rwd-time">6 ore</span><span class="rwd-items"><span class="rwd-item">Vodka</span><span class="rwd-item">Tigari</span><span class="rwd-item cash">Bani cash</span></span></div>
<div class="rwd-tier"><span class="rwd-time">8 ore</span><span class="rwd-items"><span class="rwd-item">Bormasina</span><span class="rwd-item cash">Bani cash</span></span></div>
<div class="rwd-tier"><span class="rwd-time">10 ore</span><span class="rwd-items"><span class="rwd-item">SmartWatch (GPS)</span><span class="rwd-item">Lockpick avansat</span><span class="rwd-item cash">Bani cash</span></span></div>
<div class="rwd-tier top"><span class="rwd-time">12 ore</span><span class="rwd-items"><span class="rwd-item">EliteBox</span><span class="rwd-item">Whiskey</span><span class="rwd-item cash">Bani cash</span></span></div>
</div>
<h2 class="rwd-h2" id="serie">Seria de zile</h2>
<p class="rwd-intro">Fiecare zi in care revendici cel putin un premiu iti creste seria cu o zi. Cu cat seria e mai lunga, cu atat bonusul la premii e mai mare. Bonusul se adauga si la obiecte, si la bani.</p>
<div class="rwd-card">
<div class="rwd-streak">
<div class="rwd-step"><div class="rwd-bar"></div><b>1-2</b><span>zile</span></div>
<div class="rwd-step"><div class="rwd-bar"></div><b>3-5</b><span>zile</span></div>
<div class="rwd-step"><div class="rwd-bar"></div><b>6-9</b><span>zile</span></div>
<div class="rwd-step"><div class="rwd-bar"></div><b>10-14</b><span>zile</span></div>
<div class="rwd-step"><div class="rwd-bar"></div><b>15+</b><span>zile</span></div>
</div>
<ul class="rwd-list" style="margin-top:1rem">
<li>Daca o zi intreaga nu revendici niciun premiu, seria o ia de la capat de la prima zi.</li>
<li>Nu conteaza cate premii iei intr-o zi: seria creste o singura data pe zi.</li>
<li>Bonusul activ il vezi in <code class="rwd-cmd">/premii</code>.</li>
</ul>
</div>
<h2 class="rwd-h2" id="bune-de-stiut">Bune de stiut</h2>
<div class="rwd-card">
<ul class="rwd-list">
<li>Ziua se schimba la <b>00:00, ora Romaniei</b>. Premiile pe care nu le-ai revendicat pana atunci se pierd.</li>
<li>Cand intri pe server primesti un mesaj cu timpul jucat azi si cat mai ai pana la urmatorul premiu.</li>
<li>Daca nu ai loc in inventar, nu primesti nimic. Fa loc si revendica din nou.</li>
<li>Cat esti la inchisoare nu poti revendica premii.</li>
</ul>
</div>
<h2 class="rwd-h2" id="happy-hour">Happy Hour</h2>
<p class="rwd-intro">La anumite ore, unele joburi si jafuri dau mai mult. Calendarul il vezi cu <code class="rwd-cmd">/happyhour</code>.</p>
<div class="rwd-hh">
<div class="rwd-card">
<p class="rwd-sub">Joburi</p>
<div class="rwd-acts"><span class="rwd-act" style="--c:#a16207">Miner</span><span class="rwd-act" style="--c:#22d3ee">Pescar</span><span class="rwd-act" style="--c:#f97316">Tirist</span><span class="rwd-act" style="--c:#facc15">Taxi</span><span class="rwd-act" style="--c:#22c55e">Electrician</span><span class="rwd-act" style="--c:#22c55e">Gunoier</span><span class="rwd-act" style="--c:#a855f7">Ciupercar</span></div>
<p class="rwd-sub">Ilegale</p>
<div class="rwd-acts"><span class="rwd-act" style="--c:#ef4444">Mina Secreta</span><span class="rwd-act" style="--c:#ef4444">Furt auto</span><span class="rwd-act" style="--c:#ef4444">Jaf magazin</span><span class="rwd-act" style="--c:#ef4444">Jaf ATM</span><span class="rwd-act" style="--c:#ef4444">Jaf casa</span></div>
</div>
<div class="rwd-card">
<ul class="rwd-list">
<li>Primesti un mesaj pe ecran cand incepe si cand se termina un Happy Hour.</li>
<li>Unele activitati au Happy Hour ziua intr-o saptamana si noaptea in saptamana urmatoare.</li>
<li>Orele din calendar sunt ora Romaniei.</li>
</ul>
</div>
</div>
<h2 class="rwd-h2" id="vezi-si">Vezi si</h2>
<div class="rwd-see">
<a href="../joburi/misiuni"><b>Misiuni</b><span>Misiunile de la Mike si premiile lor</span></a>
<a href="./skin-uri-arme"><b>Skin-uri arme</b><span>Skin-urile din evenimente si cum le pui</span></a>
</div>
</div>
