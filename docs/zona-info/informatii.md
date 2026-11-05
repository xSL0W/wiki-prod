---
outline: false
---

<style>
.egi {
  --ink: #0c0c0e;
  --panel: #18181b;
  --panel2: #202024;
  --line: #34343b;
  --text: #f4f4f5;
  --mute: #a1a1aa;
  --red: #cc2b2b;
  --red-deep: #b91c1c;
  --red-soft: rgba(204, 43, 43, 0.14);
  max-width: 920px;
  margin: 0 auto;
  color: var(--text);
  font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.egi *, .egi *::before, .egi *::after { box-sizing: border-box; }
.egi p, .egi li { line-height: 1.6; color: var(--text); margin: 0; }
.egi ul, .egi ol { list-style: none; padding: 0; margin: 0; }
.egi li + li { margin-top: 0; }
.egi b { color: #fff; font-weight: 650; }
.egi a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.egi a:hover { color: #ffb4b4; }
.egi a:focus-visible { outline: 3px solid var(--red); outline-offset: 3px; border-radius: 6px; }
/* hero */
.egi-hero {
  position: relative;
  background: radial-gradient(110% 120% at 100% 0%, rgba(185, 28, 28, 0.32), var(--ink) 62%);
  border: 1px solid var(--line);
  border-radius: 22px;
  padding: clamp(1.25rem, 4vw, 2.5rem);
  overflow: hidden;
}
.egi .egi-kicker {
  font-size: 0.78rem; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: var(--red);
  margin-bottom: 0.6rem;
}
.egi-hero h1 {
  margin: 0 0 0.8rem; border: 0; padding: 0;
  font-size: clamp(2rem, 6vw, 3.3rem); line-height: 1.05; font-weight: 800; letter-spacing: -0.03em; color: #fff;
}
.egi-hero h1 span { color: var(--red); }
.egi .egi-lede { max-width: 56ch; color: var(--mute); font-size: 1.05rem; }
.egi .egi-stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 0.75rem; margin-top: 1.6rem; }
.egi .egi-stats li {
  background: rgba(24, 24, 27, 0.75); border: 1px solid var(--line); border-radius: 14px; padding: 0.85rem 1rem;
}
.egi .egi-stats b { display: block; font-size: 1.35rem; letter-spacing: -0.02em; color: #fff; }
.egi .egi-stats span { color: var(--mute); font-size: 0.9rem; }
/* section titles */
.egi h2 {
  margin: 3rem 0 1rem; border: 0; padding: 0;
  font-size: 1.5rem; font-weight: 750; letter-spacing: -0.015em; color: #fff;
}
.egi h2::before {
  content: ''; display: inline-block; width: 0.55rem; height: 0.55rem; margin-right: 0.6rem;
  border-radius: 2px; background: var(--red); vertical-align: middle; transform: translateY(-2px) rotate(45deg);
}
/* story: a short timeline */
.egi .egi-time { position: relative; margin-left: 0.4rem; }
.egi .egi-time::before {
  content: ''; position: absolute; left: 7px; top: 10px; bottom: 10px; width: 2px;
  background: linear-gradient(to bottom, var(--line), var(--red));
}
.egi .egi-time li { position: relative; padding: 0 0 1.4rem 2.4rem; }
.egi .egi-time li:last-child { padding-bottom: 0; }
.egi .egi-time li::before {
  content: ''; position: absolute; left: 0; top: 6px; width: 16px; height: 16px; border-radius: 50%;
  background: var(--ink); border: 3px solid var(--line);
}
.egi .egi-time li:last-child::before { border-color: var(--red); background: var(--red); }
.egi .egi-when {
  display: block; font-size: 0.8rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; color: var(--red);
}
.egi .egi-time p { color: var(--mute); }
.egi .egi-time b { display: block; font-size: 1.1rem; }
/* what makes it different: cards */
.egi .egi-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1rem; }
.egi .egi-card {
  background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 1.2rem 1.3rem;
  transition: border-color 0.2s ease, transform 0.2s ease;
}
.egi .egi-card:hover { border-color: var(--red); transform: translateY(-2px); }
.egi .egi-card h3 { margin: 0 0 0.45rem; border: 0; padding: 0; font-size: 1.08rem; font-weight: 700; color: #fff; }
.egi .egi-card p { color: var(--mute); }
.egi .egi-num {
  display: inline-grid; place-items: center; width: 2rem; height: 2rem; margin-bottom: 0.8rem;
  border-radius: 10px; background: var(--red-soft); color: var(--red); font-weight: 800; font-size: 0.9rem;
}
/* first steps: link rows */
.egi .egi-links { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 0.75rem; }
.egi .egi-links a {
  display: flex; flex-direction: column; gap: 0.15rem; height: 100%;
  background: var(--panel2); border: 1px solid var(--line); border-radius: 14px; padding: 0.95rem 1.1rem;
  text-decoration: none; color: #fff; font-weight: 650;
  transition: border-color 0.2s ease, background 0.2s ease;
}
.egi .egi-links a:hover { border-color: var(--red); background: var(--panel); color: #fff; }
.egi .egi-links span { color: var(--mute); font-weight: 400; font-size: 0.92rem; }
.egi .egi-note {
  margin-top: 1.25rem; background: var(--red-soft); border: 1px solid rgba(204, 43, 43, 0.45);
  border-radius: 14px; padding: 0.9rem 1.1rem;
}
.egi kbd {
  font: inherit; font-size: 0.85em; font-weight: 700; color: #fff; background: var(--red-deep);
  border-radius: 6px; padding: 0.05rem 0.45rem;
}
@media (prefers-reduced-motion: reduce) {
  .egi .egi-card, .egi .egi-links a { transition: none; }
  .egi .egi-card:hover { transform: none; }
}
</style>

<div class="egi">
<section class="egi-hero">
<p class="egi-kicker">Zona info</p>
<h1>Despre <span>EliteGamers</span></h1>
<p class="egi-lede">EliteGamers e o comunitate creata in 2019, construita pe respect, joc curat si sisteme facute de noi. Serverul de FiveM l-am inceput in 2023, iar pe 31 mai 2025 l-am lansat oficial.</p>
<ul class="egi-stats">
<li><b>31.05.2025</b><span>lansare oficiala pe FiveM</span></li>
<li><b>Imersiv RP</b><span>roleplay serios, realist</span></li>
<li><b>Sisteme proprii</b><span>scrise si optimizate de noi</span></li>
</ul>
</section>
<h2>Povestea noastra</h2>
<ol class="egi-time">
<li><span class="egi-when">2019</span><b>Servere de CS:GO</b><p>Am pornit in lumea CS:GO cu primele noastre servere.</p></li>
<li><span class="egi-when">Anii de CS:GO</span><b>Recorduri cu 6 servere</b><p>Cu cele 6 servere de CS:GO am doborat recorduri, atat in Romania, cat si international.</p></li>
<li><span class="egi-when">Trecerea la CS2</span><b>Inchidem un capitol</b><p>Odata cu venirea CS2, am lasat acea etapa in urma si ne-am reinventat.</p></li>
<li><span class="egi-when">2023</span><b>Incepem pe FiveM</b><p>Ne apucam de lucru la serverul de roleplay si construim sistemele de la zero.</p></li>
<li><span class="egi-when">31 mai 2025 - azi</span><b>Lansare oficiala</b><p>Deschidem serverul pentru toata lumea si il dezvoltam constant, impreuna cu comunitatea.</p></li>
</ol>
<h2>Ce gasesti la noi</h2>
<div class="egi-grid">
<div class="egi-card"><span class="egi-num">01</span><h3>Sisteme unice</h3><p>Joburi, jafuri, misiuni si afaceri facute de noi, nu luate gata facute.</p></div>
<div class="egi-card"><span class="egi-num">02</span><h3>Economie vie</h3><p>Preturile si recompensele sunt urmarite si ajustate constant, ca munca ta sa conteze.</p></div>
<div class="egi-card"><span class="egi-num">03</span><h3>Factiuni cu rol clar</h3><p>Fiecare factiune are locul ei in oras si reguli proprii.</p></div>
<div class="egi-card"><span class="egi-num">04</span><h3>Evenimente</h3><p>Evenimente speciale si continut nou care apare pe parcurs.</p></div>
<div class="egi-card"><span class="egi-num">05</span><h3>Update-uri dese</h3><p>Ascultam ce ne spuneti si bagam in joc. Noutatile apar pe Discord.</p></div>
<div class="egi-card"><span class="egi-num">06</span><h3>Staff matur si activ</h3><p>Echipa noastra e pregatita si te ajuta cand ai nevoie. Respectul reciproc e regula de baza.</p></div>
</div>
<h2>Primii pasi</h2>
<div class="egi-links">
<a href="/zona-info/cum-intru-pe-server">Cum intru pe server<span>Conectarea, pas cu pas</span></a>
<a href="/zona-info/regulament">Regulament<span>Citeste-l inainte sa intri</span></a>
<a href="/zona-info/faq">Intrebari si raspunsuri<span>Ce intreaba toata lumea la inceput</span></a>
<a href="/zona-info/store">Store<span>EG Coins, VIP si pachete</span></a>
</div>
<p class="egi-note">Wiki-ul il ai si in joc: apasa <kbd>F6</kbd> si se deschide peste ecran.</p>
</div>
