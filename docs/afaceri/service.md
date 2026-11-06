---
outline: false
---

<style>
.asv {
  --ink: #0c0c0e;
  --panel: #18181b;
  --panel2: #202024;
  --line: #34343b;
  --text: #f4f4f5;
  --mute: #a1a1aa;
  --red: #dc2626;
  --acc: #fb923c;
  --acc-soft: rgba(251, 146, 60, 0.13);
  max-width: 960px;
  margin: 0 auto;
  color: var(--text);
}
.asv *, .asv *::before, .asv *::after { box-sizing: border-box; }
.asv p, .asv li { margin: 0; line-height: 1.6; color: var(--text); }
.asv ul, .asv ol { list-style: none; padding: 0; margin: 0; }
.asv li + li { margin-top: 0; }
.asv b { color: #fff; font-weight: 650; }
.asv code { white-space: normal; overflow-wrap: anywhere; }
.asv a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.asv a:hover { color: #fecaca; }
.asv a:focus-visible { outline: 3px solid var(--acc); outline-offset: 3px; border-radius: 6px; }
/* hero */
.asv .asv-hero {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr)); gap: 1.5rem; align-items: center;
  background: radial-gradient(90% 120% at 100% 0%, rgba(251, 146, 60, 0.15), transparent 60%),
              radial-gradient(110% 120% at 0% 100%, rgba(185, 28, 28, 0.26), var(--ink) 65%);
  border: 1px solid var(--line); border-radius: 22px; padding: clamp(1.25rem, 4vw, 2.5rem); overflow: hidden;
}
.asv .asv-kicker { font-size: 0.78rem; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: var(--acc); margin-bottom: 0.6rem; }
.asv .asv-hero h1 {
  margin: 0 0 0.8rem; border: 0; padding: 0;
  font-size: clamp(2.1rem, 7vw, 3.3rem); line-height: 1.02; font-weight: 800; letter-spacing: -0.03em; color: #fff;
}
.asv .asv-lede { color: var(--mute); font-size: 1.05rem; max-width: 46ch; }
.asv .asv-cta { display: flex; flex-wrap: wrap; gap: 0.6rem; margin-top: 1.3rem; }
.asv .asv-cta a {
  display: inline-flex; align-items: center; text-decoration: none; border-radius: 999px; padding: 0.5rem 1.1rem;
  font-weight: 700; color: var(--ink); background: var(--acc);
}
.asv .asv-cta a:hover { color: var(--ink); background: #fdba74; }
.asv .asv-art { display: block; width: 100%; max-width: 280px; height: auto; margin: 0 auto; }
.asv-art .arc { fill: none; stroke: var(--line); stroke-width: 14; stroke-linecap: round; }
.asv-art .arc.hot { stroke: var(--red); stroke-dasharray: 60 400; stroke-dashoffset: -232; }
.asv-art .tick { stroke: var(--mute); stroke-width: 3; stroke-linecap: round; }
.asv-art .needle { stroke: var(--acc); stroke-width: 5; stroke-linecap: round; transform-origin: 140px 140px; animation: asv-rev 3.2s ease-in-out infinite; }
.asv-art .hub { fill: var(--acc); }
.asv-art .lbl { fill: var(--mute); font: 700 13px ui-monospace, Menlo, Consolas, monospace; }
@keyframes asv-rev { 0%, 100% { transform: rotate(-70deg); } 35% { transform: rotate(62deg); } 50% { transform: rotate(48deg); } 65% { transform: rotate(66deg); } }
/* facts */
.asv .asv-facts { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 190px), 1fr)); gap: 0.7rem; margin-top: 1rem; }
.asv .asv-facts li { background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 0.9rem 1rem; }
.asv .asv-facts b { display: block; font-size: 1.5rem; line-height: 1.1; color: var(--acc); font-variant-numeric: tabular-nums; }
.asv .asv-facts span { color: var(--mute); font-size: 0.92rem; }
/* sections */
.asv h2 {
  display: flex; align-items: center; gap: 0.65rem;
  margin: 3rem 0 1rem; border: 0; padding: 0;
  font-size: 1.45rem; font-weight: 750; letter-spacing: -0.015em; color: #fff;
}
.asv h2::before {
  content: ''; flex: none; width: 1rem; height: 1rem; border-radius: 50%;
  background: radial-gradient(circle, var(--ink) 0 32%, transparent 33%), conic-gradient(var(--acc) 0 12.5%, transparent 0 25%, var(--acc) 0 37.5%, transparent 0 50%, var(--acc) 0 62.5%, transparent 0 75%, var(--acc) 0 87.5%, transparent 0);
  box-shadow: 0 0 0 2px var(--acc) inset;
}
.asv .asv-sub { color: var(--mute); margin: -0.4rem 0 1rem; max-width: 64ch; }
/* two columns: client / firm */
.asv .asv-split { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr)); gap: 0.9rem; }
.asv .asv-col { background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 1.1rem 1.2rem; }
.asv .asv-col h3 { margin: 0 0 0.7rem; border: 0; padding: 0; font-size: 1.05rem; font-weight: 750; color: var(--acc); text-transform: uppercase; letter-spacing: 0.08em; }
.asv .asv-list li { padding: 0.55rem 0; border-top: 1px solid var(--line); color: var(--mute); }
.asv .asv-list li:first-child { border-top: 0; padding-top: 0; }
.asv .asv-list b { display: block; color: #fff; }
/* supplier categories */
.asv .asv-parts { display: flex; flex-wrap: wrap; gap: 0.45rem; margin-top: 0.4rem; }
.asv .asv-parts li { background: var(--panel2); border: 1px solid var(--line); border-radius: 8px; padding: 0.2rem 0.7rem; font-size: 0.9rem; font-family: ui-monospace, Menlo, Consolas, monospace; }
.asv .asv-tabs { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 210px), 1fr)); gap: 0.6rem; }
.asv .asv-tabs li { background: var(--panel); border: 1px solid var(--line); border-left: 3px solid var(--acc); border-radius: 12px; padding: 0.75rem 0.95rem; color: var(--mute); font-size: 0.93rem; }
.asv .asv-tabs b { display: block; color: #fff; }
/* locations */
.asv .asv-locs { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 200px), 1fr)); gap: 0.7rem; }
.asv .asv-loc { background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 0.9rem 1rem; }
.asv .asv-loc b { display: block; }
.asv .asv-loc span { display: block; margin-top: 0.35rem; color: var(--mute); font-size: 0.9rem; }
.asv .asv-loc code { color: var(--acc); }
.asv .asv-loc em { display: inline-block; margin-top: 0.45rem; font-style: normal; font-size: 0.75rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; color: var(--ink); background: var(--acc); border-radius: 999px; padding: 0.05rem 0.55rem; }
.asv .asv-foot { margin-top: 2.5rem; padding: 1rem 1.2rem; border: 1px dashed var(--line); border-radius: 14px; color: var(--mute); }
@media (prefers-reduced-motion: reduce) {
  .asv-art .needle { animation: none; transform: rotate(40deg); }
}
</style>

<div class="asv">
<section class="asv-hero">
<div>
<p class="asv-kicker">Afaceri · Locatii</p>
<h1>Service auto</h1>
<p class="asv-lede">Un service e o firma de mecanici. Angajatii repara masini, schimba piese, ridica masini pentru Impound si fac tuning. Tot ce tine de munca de mecanic e pe pagina dedicata.</p>
<div class="asv-cta"><a href="/joburi/mecanic">Jobul de mecanic</a></div>
</div>
<svg class="asv-art" viewBox="0 0 280 190" role="img" aria-label="Turometru cu acul in miscare">
<path class="arc" d="M40 140a100 100 0 0 1 200 0"/>
<path class="arc hot" d="M40 140a100 100 0 0 1 200 0"/>
<line class="tick" x1="40" y1="140" x2="56" y2="140"/>
<line class="tick" x1="69" y1="69" x2="80" y2="80"/>
<line class="tick" x1="140" y1="40" x2="140" y2="56"/>
<line class="tick" x1="211" y1="69" x2="200" y2="80"/>
<line class="tick" x1="240" y1="140" x2="224" y2="140"/>
<line class="needle" x1="140" y1="140" x2="140" y2="62"/>
<circle class="hub" cx="140" cy="140" r="10"/>
<text class="lbl" x="140" y="178" text-anchor="middle">RPM x1000</text>
</svg>
</section>
<ul class="asv-facts">
<li><b>6</b><span>service-uri in oras</span></li>
<li><b>6</b><span>toate au si atelier de tuning</span></li>
<li><b>5</b><span>categorii de piese la furnizor</span></li>
</ul>
<h2>Ce gasesti la un service</h2>
<div class="asv-split">
<div class="asv-col">
<h3>Pentru clienti</h3>
<ul class="asv-list">
<li><b>Reparatii si revizii</b>Mecanicii pun masina pe tester, schimba piesele uzate, caroseria si fac revizia.</li>
<li><b>Tuning</b>La fiecare service iti modifici masina. Firma primeste o parte din fiecare modificare.</li>
<li><b>Plata cu Terminalul POS</b>Mecanicul iti trimite factura, iar tu o accepti sau o refuzi.</li>
<li><b>Politie si medici de serviciu</b>Facturile de la service le plateste statul, pana la o limita pe persoana, intr-un interval de timp. Peste ea, platesti tu.</li>
</ul>
</div>
<div class="asv-col">
<h3>Pentru firma</h3>
<ul class="asv-list">
<li><b>Bani din facturi</b>Factura data de un mecanic intra in contul firmei, iar mecanicul primeste o parte din ea.</li>
<li><b>Bani din tuning</b>Partea firmei creste cu fiecare angajat pontat aflat la cel mult 100 m de service.</li>
<li><b>Depozit comun si seif</b>Depozitul de piese e al tuturor angajatilor. Seiful il deschid doar patronul si sefii.</li>
<li><b>Salarii</b>Angajatii pontati primesc salariul din contul firmei, la fiecare payday.</li>
</ul>
</div>
</div>
<h2>Piese de la furnizor</h2>
<p class="asv-sub">Din Tableta firma, la Furnizor, orice angajat comanda piese si unelte cu banii lui. Comanda ajunge direct in depozitul service-ului.</p>
<ul class="asv-parts">
<li>Parti de caroserie</li><li>Parti principale</li><li>Parti de service</li><li>Kit-uri</li><li>Obiecte</li>
</ul>
<h2>Tableta firmei</h2>
<p class="asv-sub">O cumperi din magazinele de electronice. Ce vezi in ea depinde de functia ta.</p>
<ul class="asv-tabs">
<li><b>Mecanic</b>Pontaj, Furnizor si avertismentele firmei.</li>
<li><b>Sef sau patron</b>In plus: contul firmei, angajatii, angajarea de oameni, loguri si programul de lucru.</li>
<li><b>Program de lucru</b>Daca firma are program, pontajul merge doar in orele stabilite de conducere.</li>
</ul>
<h2>Locatii</h2>
<p class="asv-sub">Scrie in chat <code>/cod</code> si numarul de mai jos, ca sa pui punct pe harta.</p>
<ul class="asv-locs">
<li class="asv-loc"><b>Strawberry</b><span>Cod postal <code>851</code></span><em>Tuning</em></li>
<li class="asv-loc"><b>Burton</b><span>Cod postal <code>627</code></span><em>Tuning</em></li>
<li class="asv-loc"><b>East Vinewood</b><span>Cod postal <code>587</code></span><em>Tuning</em></li>
<li class="asv-loc"><b>Cypress Flats</b><span>Cod postal <code>804</code></span><em>Tuning</em></li>
<li class="asv-loc"><b>Murrieta Heights</b><span>Cod postal <code>768</code></span><em>Tuning</em></li>
<li class="asv-loc"><b>Grapeseed</b><span>Cod postal <code>317</code></span><em>Tuning</em></li>
</ul>
<p class="asv-foot">Cum cumperi o firma, cum angajezi oameni si cum se platesc salariile afli la <a href="/afaceri/elite-business-center">Elite Business Center</a>.</p>
</div>
