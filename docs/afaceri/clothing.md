---
outline: false
---

<style>
.ach {
  --ink: #0c0c0e;
  --panel: #18181b;
  --panel2: #202024;
  --line: #34343b;
  --text: #f4f4f5;
  --mute: #a1a1aa;
  --red: #dc2626;
  --acc: #f472b6;
  --acc-soft: rgba(244, 114, 182, 0.13);
  max-width: 960px;
  margin: 0 auto;
  color: var(--text);
}
.ach *, .ach *::before, .ach *::after { box-sizing: border-box; }
.ach p, .ach li { margin: 0; line-height: 1.6; color: var(--text); }
.ach ul, .ach ol { list-style: none; padding: 0; margin: 0; }
.ach li + li { margin-top: 0; }
.ach b { color: #fff; font-weight: 650; }
.ach code { white-space: normal; overflow-wrap: anywhere; }
.ach a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.ach a:hover { color: #fecaca; }
.ach a:focus-visible { outline: 3px solid var(--acc); outline-offset: 3px; border-radius: 6px; }
/* hero */
.ach .ach-hero {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr)); gap: 1.5rem; align-items: center;
  background: radial-gradient(90% 120% at 100% 0%, rgba(244, 114, 182, 0.15), transparent 60%),
              radial-gradient(110% 120% at 0% 100%, rgba(185, 28, 28, 0.26), var(--ink) 65%);
  border: 1px solid var(--line); border-radius: 22px; padding: clamp(1.25rem, 4vw, 2.5rem); overflow: hidden;
}
.ach .ach-kicker { font-size: 0.78rem; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: var(--acc); margin-bottom: 0.6rem; }
.ach .ach-hero h1 {
  margin: 0 0 0.8rem; border: 0; padding: 0;
  font-size: clamp(2.1rem, 7vw, 3.3rem); line-height: 1.02; font-weight: 800; letter-spacing: -0.03em; color: #fff;
}
.ach .ach-lede { color: var(--mute); font-size: 1.05rem; max-width: 46ch; }
.ach .ach-art { display: block; width: 100%; max-width: 300px; height: auto; margin: 0 auto; }
.ach-art .rail { stroke: var(--mute); stroke-width: 4; stroke-linecap: round; }
.ach-art .hanger { fill: none; stroke: var(--text); stroke-width: 3; stroke-linecap: round; stroke-linejoin: round; }
.ach-art .shirt { fill: var(--panel2); stroke: var(--acc); stroke-width: 2.5; stroke-linejoin: round; }
.ach-art .shirt.red { stroke: var(--red); }
.ach-art .tag { fill: var(--acc); }
.ach-art .swing { transform-box: view-box; animation: ach-swing 4s ease-in-out infinite; }
.ach-art .s1 { transform-origin: 70px 30px; }
.ach-art .s2 { transform-origin: 150px 30px; animation-delay: 0.6s; }
.ach-art .s3 { transform-origin: 230px 30px; animation-delay: 1.2s; }
@keyframes ach-swing { 0%, 100% { transform: rotate(-3deg); } 50% { transform: rotate(3deg); } }
/* facts */
.ach .ach-facts { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 190px), 1fr)); gap: 0.7rem; margin-top: 1rem; }
.ach .ach-facts li { background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 0.9rem 1rem; }
.ach .ach-facts b { display: block; font-size: 1.5rem; line-height: 1.1; color: var(--acc); font-variant-numeric: tabular-nums; }
.ach .ach-facts span { color: var(--mute); font-size: 0.92rem; }
/* sections */
.ach h2 {
  display: flex; align-items: center; gap: 0.65rem;
  margin: 3rem 0 1rem; border: 0; padding: 0;
  font-size: 1.45rem; font-weight: 750; letter-spacing: -0.015em; color: #fff;
}
.ach h2::before {
  content: ''; flex: none; width: 1.1rem; height: 0.75rem;
  background: var(--acc); clip-path: polygon(50% 0, 100% 100%, 0 100%);
}
.ach .ach-sub { color: var(--mute); margin: -0.4rem 0 1rem; max-width: 64ch; }
/* categories as price tags */
.ach .ach-cats { display: flex; flex-wrap: wrap; gap: 0.5rem; }
.ach .ach-cats li {
  position: relative; background: var(--panel); border: 1px solid var(--line); border-radius: 6px 999px 999px 6px;
  padding: 0.3rem 0.95rem 0.3rem 1.5rem; font-size: 0.92rem;
}
.ach .ach-cats li::before {
  content: ''; position: absolute; left: 0.6rem; top: 50%; width: 0.4rem; height: 0.4rem; margin-top: -0.2rem;
  border-radius: 50%; background: var(--acc);
}
.ach .ach-cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 240px), 1fr)); gap: 0.8rem; margin-top: 1rem; }
.ach .ach-card { background: var(--panel); border: 1px solid var(--line); border-left: 3px solid var(--acc); border-radius: 14px; padding: 0.9rem 1rem; }
.ach .ach-card b { display: block; margin-bottom: 0.2rem; }
.ach .ach-card span { color: var(--mute); font-size: 0.93rem; }
/* supply flow */
.ach .ach-flow { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 200px), 1fr)); gap: 0.7rem; counter-reset: ach; }
.ach .ach-flow li {
  counter-increment: ach; background: linear-gradient(180deg, var(--acc-soft), var(--panel) 55%);
  border: 1px solid var(--line); border-radius: 14px; padding: 1rem 1.05rem;
}
.ach .ach-flow li::before {
  content: counter(ach); display: grid; place-items: center; width: 1.8rem; height: 1.8rem; margin-bottom: 0.6rem;
  border-radius: 50%; background: var(--acc); color: var(--ink); font-weight: 800;
}
.ach .ach-flow b { display: block; }
.ach .ach-flow span { color: var(--mute); font-size: 0.93rem; }
.ach .ach-notes { display: grid; gap: 0.5rem; margin-top: 1rem; }
.ach .ach-notes li { position: relative; padding-left: 1.3rem; color: var(--mute); }
.ach .ach-notes li::before { content: ''; position: absolute; left: 0.2rem; top: 0.62em; width: 0.45rem; height: 0.45rem; border-radius: 2px; background: var(--acc); transform: rotate(45deg); }
/* locations */
.ach .ach-locs { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 190px), 1fr)); gap: 0.7rem; }
.ach .ach-loc { background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 0.9rem 1rem; }
.ach .ach-loc b { display: block; }
.ach .ach-loc span { display: block; margin-top: 0.35rem; color: var(--mute); font-size: 0.9rem; }
.ach .ach-loc code { color: var(--acc); }
.ach .ach-foot { margin-top: 2.5rem; padding: 1rem 1.2rem; border: 1px dashed var(--line); border-radius: 14px; color: var(--mute); }
@media (prefers-reduced-motion: reduce) {
  .ach-art .swing { animation: none; }
}
</style>

<div class="ach">
<section class="ach-hero">
<div>
<p class="ach-kicker">Afaceri · Locatii</p>
<h1>Magazin de haine</h1>
<p class="ach-lede">Aici iti cumperi hainele. Fiecare magazin e o firma: conducerea pune preturile pe categorii, iar angajatii tin rafturile pline.</p>
</div>
<svg class="ach-art" viewBox="0 0 300 200" role="img" aria-label="Umerase cu haine pe o bara">
<line class="rail" x1="20" y1="24" x2="280" y2="24"/>
<g class="swing s1"><path class="hanger" d="M70 24v10a6 6 0 1 1-6 6M70 40l-34 22h68z"/><path class="shirt" d="M42 64l-16 14 10 14 10-6v70h48V86l10 6 10-14-16-14H86a16 8 0 0 1-32 0z"/></g>
<g class="swing s2"><path class="hanger" d="M150 24v10a6 6 0 1 1-6 6M150 40l-34 22h68z"/><path class="shirt red" d="M122 64l-20 18 10 12 12-8v80h52V86l12 8 10-12-20-18h-14l-12 14-12-14z"/><circle class="tag" cx="164" cy="112" r="5"/></g>
<g class="swing s3"><path class="hanger" d="M230 24v10a6 6 0 1 1-6 6M230 40l-34 22h68z"/><path class="shirt" d="M206 64h48l6 106h-24l-6-70-6 70h-24z"/></g>
</svg>
</section>
<ul class="ach-facts">
<li><b>7</b><span>magazine de haine pe harta</span></li>
<li><b>15</b><span>categorii de haine si accesorii</span></li>
<li><b>2</b><span>marimi de ghiozdan, la raftul de langa</span></li>
</ul>
<h2>Ce cumperi</h2>
<p class="ach-sub">Probezi hainele, le pui in cos si platesti tot la final. Fiecare categorie are pretul ei, pus de conducerea magazinului.</p>
<ul class="ach-cats">
<li>Tricouri</li><li>Bluze</li><li>Geci</li><li>Pantaloni</li><li>Incaltaminte</li><li>Palarii</li><li>Masti</li><li>Ochelari</li><li>Cercei</li><li>Ceasuri</li><li>Bratari</li><li>Esarfe si lanturi</li><li>Genti</li><li>Veste antiglont</li><li>Decaluri</li>
</ul>
<div class="ach-cards">
<div class="ach-card"><b>Stoc pe categorii</b><span>Fiecare piesa cumparata scade o bucata din stocul categoriei ei. O categorie fara stoc nu se poate cumpara pana nu o aduc angajatii.</span></div>
<div class="ach-card"><b>Tinutele tale</b><span>In magazin te poti imbraca si cu o tinuta salvata. Platesti o taxa, care merge la firma.</span></div>
<div class="ach-card"><b>Ghiozdane</b><span>Langa magazin e un raft cu ghiozdan mic si ghiozdan mare, din stocul aceleiasi firme.</span></div>
</div>
<h2>Cum tii magazinul plin</h2>
<p class="ach-sub">Pentru angajatii unui magazin de haine. Stocul il vezi oricand in Tableta firma, la Stoc.</p>
<ol class="ach-flow">
<li><b>Mergi la furnizor</b><span>Furnizor Magazin Haine, langa ceilalti furnizori, la codul postal <code>313</code>. Vinde doar angajatilor unui magazin de haine.</span></li>
<li><b>Cumperi cutii</b><span>Alegi categoria si cantitatea, platesti din banii tai si primesti o cutie, cu cel mult 10 bucati.</span></li>
<li><b>Deschizi cutia in magazin</b><span>Trebuie sa fii langa magazinul tau. Bucatile intra direct in stocul firmei.</span></li>
</ol>
<ul class="ach-notes">
<li>Fiecare categorie are o limita de stoc. Ce nu mai incape ramane in cutie.</li>
<li>Preturile pe categorii si la ghiozdane le schimba conducerea din Tableta firma, la Preturi, pana la un plafon.</li>
<li>Firma primeste o parte din fiecare vanzare. Partea creste cu fiecare angajat pontat aflat la cel mult 100 m de magazin.</li>
</ul>
<h2>Locatii</h2>
<p class="ach-sub">Scrie in chat <code>/cod</code> si numarul de mai jos, ca sa pui punct pe harta. Pe langa ele mai exista si magazine de haine fara patron.</p>
<ul class="ach-locs">
<li class="ach-loc"><b>Rockford Hills</b><span>Cod postal <code>643</code></span></li>
<li class="ach-loc"><b>Burton</b><span>Cod postal <code>619</code></span></li>
<li class="ach-loc"><b>Alta</b><span>Cod postal <code>616</code></span></li>
<li class="ach-loc"><b>Textile City</b><span>Cod postal <code>759</code></span></li>
<li class="ach-loc"><b>Strawberry</b><span>Cod postal <code>849</code></span></li>
<li class="ach-loc"><b>Vespucci Canals</b><span>Cod postal <code>714</code></span></li>
<li class="ach-loc"><b>Paleto Bay</b><span>Cod postal <code>026</code></span></li>
</ul>
<p class="ach-foot">Cum cumperi o firma, cum angajezi oameni si cum se platesc salariile afli la <a href="/afaceri/elite-business-center">Elite Business Center</a>.</p>
</div>
