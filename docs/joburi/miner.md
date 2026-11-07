---
outline: false
---

<style>
.mnr {
  --rock: #111113;
  --stone: #1b1b1f;
  --slab: #26262c;
  --edge: #3a3a42;
  --text: #eeece8;
  --mute: #a8a49c;
  --lamp: #ffcf5a;
  --lamp-soft: rgba(255, 207, 90, 0.13);
  --ore: #e0843f;
  --gem: #4fd1c5;
  --danger: #ff5d5d;
  max-width: 920px;
  margin: 0 auto;
  color: var(--text);
  font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.mnr *, .mnr *::before, .mnr *::after { box-sizing: border-box; }
.mnr p, .mnr li { line-height: 1.6; color: var(--text); margin: 0; }
.mnr ul { list-style: none; padding: 0; margin: 0; }

/* hero: a cross-section of the mine */
.mnr-hero {
  background: var(--rock);
  border: 1px solid var(--edge);
  border-radius: 20px;
  padding: clamp(1.25rem, 4vw, 2.5rem);
  overflow: hidden;
}
.mnr-hero h1 {
  margin: 0 0 0.6rem;
  border: 0;
  padding: 0;
  font-size: clamp(2.1rem, 7vw, 3.6rem);
  line-height: 1;
  font-weight: 900;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: #fff;
}
.mnr-hero h1 .mnr-hrs {
  display: inline-block;
  font-size: 0.6em;
  color: var(--rock);
  background: var(--lamp);
  padding: 0.05em 0.35em;
  border-radius: 4px;
  transform: rotate(-3deg);
  text-transform: none;
  vertical-align: middle;
}
.mnr-hero > p { max-width: 54ch; color: var(--mute); font-size: 1.05rem; }
.mnr-cut { display: block; width: 100%; height: auto; margin-top: 1.5rem; }
.mnr-cut .sky { fill: #16161a; }
.mnr-cut .l1 { fill: #2a2420; }
.mnr-cut .l2 { fill: #221d1a; }
.mnr-cut .l3 { fill: #1a1615; }
.mnr-cut .grass { fill: none; stroke: #4c6b3c; stroke-width: 4; }
.mnr-cut .shaft { fill: #0b0b0c; }
.mnr-cut .tunnel { fill: #0b0b0c; }
.mnr-cut .rail { stroke: #4a4a52; stroke-width: 2; }
.mnr-cut .nug { fill: var(--ore); }
.mnr-cut .gem { fill: var(--gem); }
.mnr-cut .hut { fill: var(--slab); stroke: var(--edge); stroke-width: 2; }
.mnr-cut .cable { stroke: #6b6b74; stroke-width: 1.5; }
.mnr-cut .cage { fill: var(--lamp); }
.mnr-cut text { fill: var(--mute); font-size: 13px; font-family: inherit; }
.mnr-cut .tag { fill: var(--lamp); font-weight: 700; }
.mnr-cut .pulley { fill: var(--slab); stroke: var(--edge); stroke-width: 2; }
/* cage and cable share one timeline: the cable (52 units at rest) stretches to the cage top at every level */
.mnr-cut .lift { animation: mnr-lift 9s ease-in-out infinite; }
.mnr-cut .rope { transform-box: view-box; transform-origin: 137px 10px; animation: mnr-rope 9s ease-in-out infinite; }
@keyframes mnr-lift {
  0%, 8% { transform: translateY(0); }
  22%, 30% { transform: translateY(70px); }
  44%, 56% { transform: translateY(140px); }
  70%, 78% { transform: translateY(70px); }
  92%, 100% { transform: translateY(0); }
}
@keyframes mnr-rope {
  0%, 8% { transform: scaleY(1); }
  22%, 30% { transform: scaleY(2.3462); }
  44%, 56% { transform: scaleY(3.6923); }
  70%, 78% { transform: scaleY(2.3462); }
  92%, 100% { transform: scaleY(1); }
}
@media (prefers-reduced-motion: reduce) {
  .mnr-cut .lift, .mnr-cut .rope { animation: none; }
}

.mnr .mnr-facts { display: flex; flex-wrap: wrap; gap: 0.6rem; margin-top: 1.1rem; }
.mnr-facts li {
  background: var(--stone);
  border: 1px solid var(--edge);
  border-left: 4px solid var(--lamp);
  padding: 0.35rem 0.85rem;
  font-size: 0.92rem;
}

/* sections */
.mnr h2 {
  margin: 3rem 0 1rem;
  border: 0;
  padding: 0;
  font-size: 1.45rem;
  font-weight: 850;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: #fff;
}
.mnr b { color: #fff; font-weight: 650; }
.mnr code { overflow-wrap: anywhere; }
.mnr kbd {
  font: inherit; font-size: 0.85em; font-weight: 800; color: var(--rock); background: var(--lamp);
  border-radius: 4px; padding: 0.05rem 0.45rem; box-shadow: 0 2px 0 #a8862f;
}

/* grades as a depth gauge */
/* grades: lift floor indicator on a shaft, one level per grade, colored by what that level yields */
.mnr .mnr-depth { position: relative; display: grid; gap: 0.9rem; padding: 0; }
.mnr .mnr-depth::before {
  content: ''; position: absolute; left: 1.45rem; top: 1.5rem; bottom: 1.5rem; width: 4px; border-radius: 2px;
  background: repeating-linear-gradient(to bottom, var(--edge) 0 8px, transparent 8px 14px);
}
.mnr .mnr-depth li { position: relative; display: grid; grid-template-columns: 3rem minmax(0, 1fr); gap: 0.9rem; align-items: center; }
.mnr-floor {
  position: relative; z-index: 1; width: 3rem; height: 3rem; border-radius: 10px; display: grid; place-items: center;
  background: var(--rock); border: 2px solid var(--c); color: var(--c);
  font: 800 1.05rem/1 ui-monospace, 'SFMono-Regular', Menlo, monospace;
}
.mnr-card {
  display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: 0.2rem 1rem; align-items: center;
  background: linear-gradient(100deg, var(--soft), var(--stone) 55%); border: 1px solid var(--edge);
  border-left: 4px solid var(--c); border-radius: 12px; padding: 0.9rem 1.1rem;
}
.mnr-card svg { grid-row: 1 / span 2; grid-column: 2; width: 2.4rem; height: 2.4rem; }
.mnr-depth .lv { display: flex; flex-wrap: wrap; align-items: baseline; gap: 0.2rem 0.7rem; }
.mnr-depth .lv strong { font-size: 1.1rem; color: #fff; }
.mnr-depth .lv span { font-weight: 800; color: var(--c); }
.mnr .mnr-depth p { color: var(--mute); }
.mnr-depth .z1 { --c: #b9a48c; --soft: rgba(185, 164, 140, 0.1); }
.mnr-depth .z2 { --c: var(--ore); --soft: rgba(224, 132, 63, 0.12); }
.mnr-depth .z3 { --c: var(--gem); --soft: rgba(79, 209, 197, 0.12); }
.mnr-note { margin-top: 0.9rem !important; color: var(--mute) !important; font-size: 0.95rem; }

/* the shift: rails with sleepers */
.mnr-rail { position: relative; margin-left: 0.3rem; }
.mnr-rail::before, .mnr-rail::after {
  content: ''; position: absolute; top: 6px; bottom: 6px; width: 3px; background: #4a4a52;
}
.mnr-rail::before { left: 6px; }
.mnr-rail::after { left: 20px; }
.mnr-rail li { position: relative; padding: 0 0 1.35rem 3.2rem; }
.mnr-rail li:last-child { padding-bottom: 0; }
.mnr-rail li::before {
  content: ''; position: absolute; left: 0; top: 4px; width: 30px; height: 16px; border-radius: 3px 3px 6px 6px;
  background: var(--ore); z-index: 1;
}

/* zones */
.mnr-zones { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; }
.mnr-zone { background: var(--stone); border: 1px solid var(--edge); border-radius: 14px; padding: 1.1rem 1.25rem; }
.mnr-zone h3 { margin: 0 0 0.2rem; border: 0; padding: 0; font-size: 1.1rem; color: #fff; }
.mnr-zone .who { display: block; font-size: 0.85rem; color: var(--lamp); font-weight: 700; margin-bottom: 0.5rem; }
.mnr-zone p { color: var(--mute); }
.mnr-zone.gems { border-color: var(--gem); }
.mnr-zone.gems .who { color: var(--gem); }
.mnr-zone.secret {
  border-color: var(--danger);
  background: repeating-linear-gradient(135deg, rgba(255, 93, 93, 0.06) 0 10px, transparent 10px 20px), var(--stone);
}
.mnr-zone.secret .who { color: var(--danger); }

/* where the ore goes */
.mnr-flow { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; }
.mnr-flow div { border-top: 4px solid var(--ore); background: var(--stone); border-radius: 0 0 12px 12px; padding: 1rem 1.15rem; }
.mnr-flow h3 { margin: 0 0 0.4rem; border: 0; padding: 0; font-size: 1.05rem; color: #fff; }
.mnr-flow p { color: var(--mute); }

/* tips */
.mnr-tips li { padding: 0.8rem 0; border-top: 1px dashed var(--edge); }
.mnr-tips li:last-child { border-bottom: 1px dashed var(--edge); }

.mnr a:focus-visible { outline: 3px solid var(--lamp); outline-offset: 2px; }
/* block list: keeps the 8px row spacing the theme no longer adds to classed lists */
.mnr .mnr-rail > li + li, .mnr .mnr-tips > li + li { margin-top: 8px; }
</style>

<div class="mnr">

<section class="mnr-hero">
<h1>Miner <span class="mnr-hrs">- 10h/100h/300h</span></h1>
<p>Casca, tarnacop si rabdare. Spargi bolovani in cariera, afli ce minereu ai scos si il topesti sau il vinzi. Cu cat ai mai multe ore, cu atat sapi mai adanc.</p>
<svg class="mnr-cut" viewBox="0 0 640 260" role="img" aria-label="Sectiune printr-o mina cu trei niveluri: zona 1 de la 10 ore, zona 2 de la 100 de ore si zona 3 de la 300 de ore">
<rect class="sky" x="0" y="0" width="640" height="50"/>
<rect class="l1" x="0" y="50" width="640" height="70"/>
<rect class="l2" x="0" y="120" width="640" height="70"/>
<rect class="l3" x="0" y="190" width="640" height="70"/>
<path class="grass" d="M0 50 L640 50"/>
<rect class="hut" x="40" y="22" width="44" height="28"/>
<text x="38" y="16">sef</text>
<rect class="shaft" x="120" y="50" width="34" height="200"/>
<line class="cable rope" x1="137" y1="10" x2="137" y2="62"/>
<circle class="pulley" cx="137" cy="10" r="6"/>
<g class="lift">
<rect class="cage" x="125" y="62" width="24" height="22" rx="2"/>
</g>
<rect class="tunnel" x="154" y="70" width="430" height="30" rx="6"/>
<rect class="tunnel" x="154" y="140" width="430" height="30" rx="6"/>
<rect class="tunnel" x="154" y="210" width="430" height="30" rx="6"/>
<line class="rail" x1="160" y1="97" x2="578" y2="97"/>
<line class="rail" x1="160" y1="167" x2="578" y2="167"/>
<line class="rail" x1="160" y1="237" x2="578" y2="237"/>
<text class="tag" x="172" y="90">Zona 1 · 10h</text>
<text class="tag" x="172" y="160">Zona 2 · 100h</text>
<text class="tag" x="172" y="230">Zona 3 · 300h</text>
<circle class="nug" cx="330" cy="84" r="7"/>
<circle class="nug" cx="420" cy="88" r="5"/>
<circle class="nug" cx="520" cy="84" r="6"/>
<circle class="nug" cx="340" cy="154" r="7"/>
<circle class="nug" cx="440" cy="158" r="6"/>
<circle class="nug" cx="540" cy="153" r="7"/>
<circle class="nug" cx="350" cy="224" r="7"/>
<path class="gem" d="M450 216 l8 8 -8 8 -8 -8 Z"/>
<circle class="nug" cx="510" cy="226" r="6"/>
<path class="gem" d="M560 218 l6 6 -6 6 -6 -6 Z"/>
</svg>
<ul class="mnr-facts">
<li>Lucrezi singur, in ritmul tau</li>
<li>Tarnacopul il cumperi de la mina</li>
<li>Plata depinde de ce minezi si unde vinzi</li>
</ul>
</section>

<h2>Cum ma angajez?</h2>
<p>Ai nevoie de <b>10 ore jucate</b>. Angajeaza-te ca <b>Miner</b> la Primarie (<code>Telefon → Harti → Locatii importante → Primarie</code>) sau direct de la seful minei, cu <kbd>E</kbd>. Langa sef gasesti <b>Magazinul miner</b>, de unde iei tarnacopul. Zonele de minat apar pe harta ca cercuri verzi, <b>Zona miner 1, 2 si 3</b>, toate in cariera de langa sef.</p>

<h2>Grade</h2>
<ul class="mnr-depth">
<li class="z1">
<span class="mnr-floor" aria-hidden="true">1</span>
<div class="mnr-card">
<div class="lv"><strong>Miner incepator</strong><span>10 ore</span></div>
<p>Minezi in <b>Zona 1</b>. Minereu sarac, dar se sparge repede.</p>
<svg viewBox="0 0 40 40" aria-hidden="true"><path d="M6 30 L12 16 L22 11 L33 18 L35 30 Z" fill="#4a4038" stroke="#b9a48c" stroke-width="2" stroke-linejoin="round"/><path d="M14 22 L20 19 M24 24 L29 21" stroke="#6e6052" stroke-width="2" stroke-linecap="round"/></svg>
</div>
</li>
<li class="z2">
<span class="mnr-floor" aria-hidden="true">2</span>
<div class="mnr-card">
<div class="lv"><strong>Miner</strong><span>100 de ore</span></div>
<p>Se deschide <b>Zona 2</b>, cu minereu bun, si <b>mina secreta</b>.</p>
<svg viewBox="0 0 40 40" aria-hidden="true"><path d="M6 30 L12 16 L22 11 L33 18 L35 30 Z" fill="#3a3230" stroke="#6e6052" stroke-width="2" stroke-linejoin="round"/><circle cx="17" cy="22" r="4" fill="#e0843f"/><circle cx="26" cy="19" r="2.6" fill="#ffcf5a"/><circle cx="25" cy="26" r="2.2" fill="#e0843f"/></svg>
</div>
</li>
<li class="z3">
<span class="mnr-floor" aria-hidden="true">3</span>
<div class="mnr-card">
<div class="lv"><strong>Miner expert</strong><span>300 de ore</span></div>
<p>Se deschide <b>Zona 3</b>, singura in care gasesti pietre pretioase.</p>
<svg viewBox="0 0 40 40" aria-hidden="true"><path d="M20 6 L32 16 L20 34 L8 16 Z" fill="rgba(79,209,197,0.25)" stroke="#4fd1c5" stroke-width="2" stroke-linejoin="round"/><path d="M8 16 H32 M14 16 L20 34 L26 16 M14 16 L20 6 L26 16" fill="none" stroke="#4fd1c5" stroke-width="1.2" stroke-linejoin="round"/></svg>
</div>
</li>
</ul>
<p class="mnr-note">Promovarea tine doar de orele jucate: cand le ai, deschide meniul sefului si urci automat in grad. Progresul il vezi la <b>Skill-uri si promovare</b>. Daca te angajezi cand ai deja orele, incepi direct pe gradul potrivit. Un grad mai mare pastreaza si zonele de dinainte.</p>

<h2>O tura in mina</h2>
<ul class="mnr-rail">
<li><b>Ia-ti un tarnacop</b> de la Magazinul miner. Fara el nu poti mina.</li>
<li><b>Intra intr-o zona de minat.</b> Cand intri in cerc, intri automat in tura, iar bolovanii de minereu apar in jurul tau.</li>
<li><b>Tine apasat <kbd>G</kbd></b> uitandu-te la un bolovan si alege <b>Culege minereu</b>.</li>
<li><b>Stai pe loc</b> pana se umple bara <b>Minezi...</b> In Zona 1 merge de obicei mai repede decat in celelalte. Daca anulezi, nu primesti nimic.</li>
<li><b>Abia acum afli ce ai scos.</b> Toti bolovanii arata la fel, iar minereul il primesti direct in inventar.</li>
<li><b>Tarnacopul se degradeaza</b> putin la fiecare bolovan. Cand se strica, dispare si iti trebuie altul.</li>
<li><b>Cand iesi din zona,</b> iesi si din tura. Duci minereul la topitorie sau la vanzare.</li>
</ul>

<h2>Zonele</h2>
<div class="mnr-zones">
<div class="mnr-zone">
<h3>Zona 1</h3>
<span class="who">Miner incepator · 10h</span>
<p>Carbune inferior si minereu sarac de fier, cupru, staniu si bauxita. Nu se vinde: il topesti in bare inferioare, pentru crafting.</p>
</div>
<div class="mnr-zone">
<h3>Zona 2</h3>
<span class="who">Miner · 100h</span>
<p>Carbune, fier, cupru, staniu, plumb, sulf si bauxita. Daca ai noroc, si aur.</p>
</div>
<div class="mnr-zone gems">
<h3>Zona 3</h3>
<span class="who">Miner expert · 300h</span>
<p>Minereurile din Zona 2, plus <b>diamant, rubin, smarald si safir</b>.</p>
</div>
<div class="mnr-zone secret">
<h3>Mina secreta</h3>
<span class="who">Miner · 100h · 18:00 - 02:00</span>
<p>Nu apare pe harta. Se mineaza doar seara si noaptea si da mai ales carbune. Este intr-o zona <b>No Man's Land</b>: oricine te poate ataca sau jefui, iar dupa ce intri nu poti pleca imediat.</p>
</div>
</div>

<h2>Ce faci cu minereul</h2>
<div class="mnr-flow">
<div>
<h3>Topitorie Incepatori</h3>
<p>In cariera. Aici transformi minereul sarac din Zona 1 in bare inferioare.</p>
</div>
<div>
<h3>Topitorie</h3>
<p>In oras, langa punctul de vanzare. Din minereu si carbune scoti bare, nituri sau praf de pusca, materiale pentru crafting.</p>
</div>
<div>
<h3>Punct de vanzare miner</h3>
<p>Marcat pe harta. Cumpara minereul bun, aurul si pietrele pretioase. Plata depinde de ce vinzi.</p>
</div>
</div>

<h2>Sfaturi</h2>
<ul class="mnr-tips">
<li><b>Ai grija la greutate.</b> Minereul il primesti chiar daca trece peste greutatea maxima, dar cat timp esti supraincarcat nu mai poti mina. Vinde sau lasa ceva jos.</li>
<li><b>Pastreaza un slot liber.</b> Daca nu ai niciun slot liber in inventar, minereul scos se pierde.</li>
<li><b>Bolovanii sunt ai tuturor.</b> Ce sparge alt miner dispare si pentru tine. Bolovani noi apar dupa putin timp.</li>
<li><b>Prinde Happy Hour-ul.</b> In orele de Happy Hour primesti mai mult minereu din fiecare bolovan.</li>
<li><b>Uniforma o iei de la sef,</b> din garderoba jobului sau dintr-o tinuta salvata.</li>
</ul>
</div>
