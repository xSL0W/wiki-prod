---
outline: false
---

<style>
.ags {
  --ink: #0c0c0e;
  --panel: #18181b;
  --panel2: #202024;
  --line: #34343b;
  --text: #f4f4f5;
  --mute: #a1a1aa;
  --red: #dc2626;
  --acc: #d4a24c;
  --acc-soft: rgba(212, 162, 76, 0.14);
  max-width: 960px;
  margin: 0 auto;
  color: var(--text);
}
.ags *, .ags *::before, .ags *::after { box-sizing: border-box; }
.ags p, .ags li { margin: 0; line-height: 1.6; color: var(--text); }
.ags ul, .ags ol { list-style: none; padding: 0; margin: 0; }
.ags li + li { margin-top: 0; }
.ags b { color: #fff; font-weight: 650; }
.ags code { white-space: normal; overflow-wrap: anywhere; }
.ags a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.ags a:hover { color: #fecaca; }
.ags a:focus-visible { outline: 3px solid var(--acc); outline-offset: 3px; border-radius: 6px; }
/* hero */
.ags .ags-hero {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr)); gap: 1.5rem; align-items: center;
  background: radial-gradient(90% 120% at 100% 0%, rgba(212, 162, 76, 0.16), transparent 60%),
              radial-gradient(110% 120% at 0% 100%, rgba(185, 28, 28, 0.26), var(--ink) 65%);
  border: 1px solid var(--line); border-radius: 22px; padding: clamp(1.25rem, 4vw, 2.5rem); overflow: hidden;
}
.ags .ags-kicker { font-size: 0.78rem; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: var(--acc); margin-bottom: 0.6rem; }
.ags .ags-hero h1 {
  margin: 0 0 0.8rem; border: 0; padding: 0;
  font-size: clamp(2.2rem, 7vw, 3.4rem); line-height: 1.02; font-weight: 800; letter-spacing: -0.03em; color: #fff;
}
.ags .ags-lede { color: var(--mute); font-size: 1.05rem; max-width: 46ch; }
.ags .ags-art { display: block; width: 100%; max-width: 260px; height: auto; margin: 0 auto; }
.ags-art .ring { fill: none; stroke: var(--line); stroke-width: 2; }
.ags-art .ring.hot { stroke: var(--acc); stroke-width: 3; }
.ags-art .ticks { fill: none; stroke: var(--acc); stroke-width: 6; stroke-dasharray: 2 13.7; transform-origin: 120px 120px; animation: ags-spin 24s linear infinite; }
.ags-art .cross { stroke: var(--text); stroke-width: 2; opacity: 0.8; }
.ags-art .dot { fill: var(--red); transform-origin: 120px 120px; animation: ags-pulse 2.4s ease-in-out infinite; }
@keyframes ags-spin { to { transform: rotate(360deg); } }
@keyframes ags-pulse { 0%, 100% { transform: scale(1); opacity: 1; } 50% { transform: scale(1.5); opacity: 0.6; } }
/* facts */
.ags .ags-facts { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 190px), 1fr)); gap: 0.7rem; margin-top: 1rem; }
.ags .ags-facts li { background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 0.9rem 1rem; }
.ags .ags-facts b { display: block; font-size: 1.5rem; line-height: 1.1; color: var(--acc); font-variant-numeric: tabular-nums; }
.ags .ags-facts span { color: var(--mute); font-size: 0.92rem; }
/* sections */
.ags h2 {
  display: flex; align-items: flex-start; gap: 0.65rem;
  margin: 3rem 0 1rem; border: 0; padding: 0;
  font-size: 1.45rem; font-weight: 750; letter-spacing: -0.015em; color: #fff;
}
.ags h2::before { margin-top: calc(0.5lh - 1rem / 2);
  content: ''; flex: none; width: 1rem; height: 1rem; border-radius: 50%;
  border: 2px solid var(--acc); box-shadow: inset 0 0 0 3px var(--ink), inset 0 0 0 6px var(--red);
}
.ags .ags-sub { color: var(--mute); margin: -0.4rem 0 1rem; max-width: 64ch; }
/* shelf */
.ags .ags-shelf { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 250px), 1fr)); gap: 0.8rem; }
.ags .ags-rack { background: var(--panel); border: 1px solid var(--line); border-top: 3px solid var(--acc); border-radius: 16px; padding: 1rem 1.1rem; }
.ags .ags-rack h3 { margin: 0 0 0.6rem; border: 0; padding: 0; font-size: 1.05rem; font-weight: 750; color: #fff; }
.ags .ags-tags { display: flex; flex-wrap: wrap; gap: 0.4rem; }
.ags .ags-tags li { background: var(--panel2); border: 1px solid var(--line); border-radius: 999px; padding: 0.15rem 0.7rem; font-size: 0.9rem; }
.ags .ags-rules { display: grid; gap: 0.6rem; margin-top: 1rem; }
.ags .ags-rules li { background: var(--acc-soft); border: 1px solid rgba(212, 162, 76, 0.45); border-radius: 12px; padding: 0.75rem 1rem; }
/* workshop steps */
.ags .ags-steps { counter-reset: ags; display: grid; gap: 0.7rem; }
.ags .ags-steps li {
  counter-increment: ags; position: relative; background: var(--panel); border: 1px solid var(--line);
  border-radius: 14px; padding: 1rem 1.1rem 1rem 3.6rem;
}
.ags .ags-steps li::before {
  content: counter(ags, decimal-leading-zero); position: absolute; left: 1rem; top: 1rem;
  font: 800 1rem/1.9rem ui-monospace, Menlo, Consolas, monospace; color: var(--acc);
}
.ags .ags-steps p { color: var(--mute); }
.ags .ags-steps b { display: block; color: #fff; }
/* locations */
.ags .ags-locs { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 200px), 1fr)); gap: 0.7rem; }
.ags .ags-loc {
  position: relative; background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 0.9rem 1rem;
}
.ags .ags-loc b { display: block; }
.ags .ags-loc span { display: block; margin-top: 0.35rem; color: var(--mute); font-size: 0.9rem; }
.ags .ags-loc code { color: var(--acc); }
.ags .ags-foot { margin-top: 2.5rem; padding: 1rem 1.2rem; border: 1px dashed var(--line); border-radius: 14px; color: var(--mute); }
@media (prefers-reduced-motion: reduce) {
  .ags-art .ticks, .ags-art .dot { animation: none; }
}
</style>

<div class="ags">
<section class="ags-hero">
<div>
<p class="ags-kicker">Afaceri · Locatii</p>
<h1>Magazin de arme</h1>
<p class="ags-lede">Magazinul de arme al orasului. Angajatii fabrica arme albe, pistolul SNS, pusca de vanatoare si munitia lor, apoi le pun la vanzare. Fiecare magazin are patronul lui.</p>
</div>
<svg class="ags-art" viewBox="0 0 240 240" role="img" aria-label="Luneta cu tinta">
<circle class="ring" cx="120" cy="120" r="108"/>
<circle class="ticks" cx="120" cy="120" r="96"/>
<circle class="ring hot" cx="120" cy="120" r="70"/>
<circle class="ring" cx="120" cy="120" r="38"/>
<line class="cross" x1="120" y1="8" x2="120" y2="96"/>
<line class="cross" x1="120" y1="144" x2="120" y2="232"/>
<line class="cross" x1="8" y1="120" x2="96" y2="120"/>
<line class="cross" x1="144" y1="120" x2="232" y2="120"/>
<circle class="dot" cx="120" cy="120" r="6"/>
</svg>
</section>
<ul class="ags-facts">
<li><b>6</b><span>magazine de arme in oras</span></li>
<li><b>40 ore</b><span>jucate, ca sa poti cumpara arme si munitie</span></li>
<li><b>1 masa</b><span>de fabricat arme in fiecare magazin</span></li>
</ul>
<h2>Ce gasesti pe raft</h2>
<p class="ags-sub">Raftul se umple doar cu ce au fabricat angajatii. Daca lipseste ceva, nu s-a fabricat inca. Preturile le pune conducerea magazinului, pana la un plafon.</p>
<div class="ags-shelf">
<div class="ags-rack">
<h3>Arme albe</h3>
<ul class="ags-tags">
<li>Bata</li><li>Rozeta</li><li>Ciocan</li><li>Pumnal</li><li>Cutit</li><li>Briceag</li><li>Topor</li><li>Topor de lupta</li>
</ul>
</div>
<div class="ags-rack">
<h3>Arme de foc</h3>
<ul class="ags-tags">
<li>Pistol SNS</li><li>Pusca de vanatoare</li>
</ul>
</div>
<div class="ags-rack">
<h3>Munitie</h3>
<ul class="ags-tags">
<li>.45 ACP, pentru SNS</li><li>Gloante pentru pusca de vanatoare</li>
</ul>
</div>
</div>
<ul class="ags-rules">
<li><b>Ai nevoie de 40 de ore jucate</b> ca sa cumperi arme sau munitie din magazinul de arme.</li>
<li><b>Armele de foc se vand doar cu licenta de port-arma.</b> Magazinul nu o verifica singur: vanzatorul ti-o cere inainte de vanzare.</li>
<li>Vanatorii isi iau de aici pusca si munitia. Detalii pe pagina <a href="/joburi/vanator">Vanator</a>.</li>
</ul>
<h2>Cum lucrezi la magazinul de arme</h2>
<p class="ags-sub">Te angajeaza conducerea magazinului. De acolo, drumul unei arme pana pe raft arata asa:</p>
<ol class="ags-steps">
<li><p><b>Strangi materialele</b>Bare de otel, fier, cupru, staniu si aluminiu, bare inferioare, lemn, carbune, praf de pusca si minereu de plumb. Barele inferioare le topesti din minereu sarac, la Topitoria Incepatori (vezi <a href="/joburi/miner">Miner</a>).</p></li>
<li><p><b>Fabrici la masa din magazin</b>Fiecare magazin de arme are o masa Crafting Arme Magazin. O folosesc doar angajatii unui magazin de arme.</p></li>
<li><p><b>Pui marfa in depozitul magazinului</b>Ce depui in depozitul de langa tejghea apare la vanzare. Stocul il vezi in Tableta firma, la Stoc.</p></li>
<li><p><b>Conducerea pune preturile</b>Din Tableta firma, la Preturi. Un produs fara pret nu se poate cumpara.</p></li>
</ol>
<ul class="ags-rules">
<li>Firma primeste o parte din fiecare vanzare. Partea creste cu fiecare angajat pontat aflat la cel mult 100 m de magazin.</li>
<li>Seiful din magazin il deschid doar patronul si sefii.</li>
</ul>
<h2>Locatii</h2>
<p class="ags-sub">Scrie in chat <code>/cod</code> si numarul de mai jos, ca sa pui punct pe harta.</p>
<ul class="ags-locs">
<li class="ags-loc"><b>Pillbox Hill</b><span>Cod postal <code>745</code></span></li>
<li class="ags-loc"><b>Hawick</b><span>Cod postal <code>608</code></span></li>
<li class="ags-loc"><b>Little Seoul</b><span>Cod postal <code>726</code></span></li>
<li class="ags-loc"><b>La Mesa</b><span>Cod postal <code>769</code></span></li>
<li class="ags-loc"><b>Cypress Flats</b><span>Cod postal <code>807</code></span></li>
<li class="ags-loc"><b>Sandy Shores</b><span>Cod postal <code>285</code></span></li>
</ul>
<p class="ags-foot">Cum cumperi o firma, cum angajezi oameni si cum se platesc salariile afli la <a href="/afaceri/elite-business-center">Elite Business Center</a>.</p>
</div>
