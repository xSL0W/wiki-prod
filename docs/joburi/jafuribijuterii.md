---
outline: false
---

<style>
.vjc {
  --velvet: #0f0912;
  --plush: #1a111e;
  --felt: #241829;
  --edge: #3b2a44;
  --text: #f2ebf4;
  --mute: #b5a5bb;
  --amethyst: #b57cff;
  --amethyst-soft: rgba(181, 124, 255, 0.14);
  --gold: #e8c27a;
  --laser: #ff2d55;
  --laser-soft: rgba(255, 45, 85, 0.12);
  max-width: 920px;
  margin: 0 auto;
  color: var(--text);
  font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.vjc *, .vjc *::before, .vjc *::after { box-sizing: border-box; }
.vjc p, .vjc li { line-height: 1.6; color: var(--text); margin: 0; }
.vjc ul, .vjc ol { list-style: none; padding: 0; margin: 0; }
.vjc li + li { margin-top: 0; }
.vjc b { color: #fff; font-weight: 650; }

/* hero: a display case under a laser grid */
.vjc .vjc-hero {
  position: relative;
  background: radial-gradient(120% 90% at 50% 0%, #2a1631 0%, var(--velvet) 62%);
  border: 1px solid var(--edge);
  border-radius: 22px;
  padding: clamp(1.25rem, 4vw, 2.5rem);
  overflow: hidden;
}
.vjc .vjc-hero h1 {
  margin: 0 0 0.6rem;
  border: 0;
  padding: 0;
  font-size: clamp(2rem, 6.4vw, 3.5rem);
  line-height: 1.05;
  font-weight: 800;
  letter-spacing: -0.03em;
  color: #fff;
}
.vjc .vjc-hrs { display: inline-flex; gap: 0.3em; white-space: nowrap; color: var(--gold); }
.vjc .vjc-lead { max-width: 54ch; color: var(--mute); font-size: 1.05rem; }
.vjc-case { display: block; width: 100%; height: auto; margin-top: 1.4rem; }
.vjc-case .glass { fill: rgba(181, 124, 255, 0.06); stroke: rgba(242, 235, 244, 0.35); stroke-width: 2; }
.vjc-case .shine { fill: none; stroke: rgba(255, 255, 255, 0.18); stroke-width: 3; stroke-linecap: round; }
.vjc-case .cab { fill: #24162a; stroke: var(--edge); stroke-width: 2; }
.vjc-case .pad { fill: #3a1d44; }
.vjc-case .gem { fill: var(--amethyst); stroke: #e3ccff; stroke-width: 1.5; }
.vjc-case .gold { fill: none; stroke: var(--gold); stroke-width: 3; stroke-linecap: round; }
.vjc-case .goldfill { fill: var(--gold); }
.vjc-case .face { fill: #120a14; stroke: var(--gold); stroke-width: 3; }
.vjc-case .beam { stroke: var(--laser); stroke-width: 2; opacity: 0.85; }
.vjc-case .glow { stroke: var(--laser); stroke-width: 8; opacity: 0.18; }
.vjc-case .sweep { animation: vjc-sweep 5.5s ease-in-out infinite alternate; }
.vjc-case .emitter { fill: var(--laser); }
.vjc-case text { fill: var(--mute); font-size: 13px; font-family: inherit; letter-spacing: 0.08em; }
@keyframes vjc-sweep {
  from { transform: translateX(-46px); }
  to { transform: translateX(46px); }
}
.vjc .vjc-tags { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 0.8rem; margin-top: 1.4rem; }
.vjc .vjc-tag {
  position: relative;
  margin: 0;
  background: var(--plush);
  border: 1px solid var(--edge);
  border-radius: 6px 14px 14px 6px;
  padding: 0.8rem 1rem 0.8rem 2.3rem;
}
.vjc .vjc-tag::before {
  content: '';
  position: absolute; left: 0.85rem; top: 50%;
  width: 10px; height: 10px; margin-top: -5px;
  border-radius: 50%;
  border: 2px solid var(--gold);
  background: var(--velvet);
}
.vjc .vjc-tag span { display: block; font-size: 0.78rem; letter-spacing: 0.08em; text-transform: uppercase; color: var(--mute); }
.vjc .vjc-tag strong { display: block; font-size: 1.15rem; color: #fff; }

/* sections */
.vjc h2 {
  margin: 3rem 0 1rem;
  border: 0;
  padding: 0;
  font-size: 1.5rem;
  font-weight: 750;
  letter-spacing: -0.015em;
  color: #fff;
}
.vjc .vjc-p { color: var(--mute); max-width: 68ch; }
.vjc .vjc-p + .vjc-p { margin-top: 0.7rem; }
.vjc .vjc-after { margin-top: 1rem; }

/* kit: a jeweller's tray */
.vjc .vjc-tray {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 0.75rem;
  background: var(--felt);
  border: 1px solid var(--edge);
  border-radius: 18px;
  padding: clamp(0.75rem, 2.5vw, 1.1rem);
}
.vjc .vjc-slot {
  margin: 0;
  display: grid;
  grid-template-columns: 44px 1fr;
  gap: 0.85rem;
  align-items: start;
  background: var(--velvet);
  border: 1px solid var(--edge);
  border-radius: 12px;
  padding: 0.9rem 1rem;
}
.vjc .vjc-slot svg { width: 44px; height: 44px; }
.vjc .vjc-slot h3 { margin: 0 0 0.2rem; border: 0; padding: 0; font-size: 1.02rem; color: #fff; }
.vjc .vjc-slot p { color: var(--mute); font-size: 0.95rem; }
.vjc .vjc-ico { fill: none; stroke: var(--amethyst); stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }

/* the plan: facets on a laser line */
.vjc .vjc-plan { position: relative; }
.vjc .vjc-plan::before {
  content: ''; position: absolute; left: 17px; top: 10px; bottom: 10px; width: 2px;
  background: linear-gradient(var(--laser), rgba(255, 45, 85, 0.15));
  box-shadow: 0 0 10px var(--laser);
}
.vjc .vjc-step { position: relative; margin: 0; padding: 0 0 1.4rem 3.4rem; }
.vjc .vjc-step:last-child { padding-bottom: 0; }
.vjc .vjc-step::before {
  content: attr(data-n);
  position: absolute; left: 2px; top: 0;
  width: 32px; height: 32px;
  display: grid; place-items: center;
  font-weight: 800; font-size: 0.9rem; color: var(--velvet);
  background: var(--amethyst);
  clip-path: polygon(50% 0, 100% 38%, 50% 100%, 0 38%);
}
.vjc .vjc-step h3 { margin: 0 0 0.25rem; border: 0; padding: 0; font-size: 1.08rem; color: #fff; }
.vjc .vjc-step p { color: var(--mute); }
.vjc kbd {
  font: inherit; font-size: 0.85em; font-weight: 800; color: var(--velvet); background: var(--gold);
  border-radius: 6px; padding: 0.05rem 0.45rem;
}

/* loot: two display drawers */
.vjc .vjc-loot { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1rem; }
.vjc .vjc-drawer { background: var(--plush); border: 1px solid var(--edge); border-radius: 16px; padding: 1.2rem 1.3rem; }
.vjc .vjc-drawer.safe { background: linear-gradient(160deg, var(--amethyst-soft), var(--plush) 65%); border-color: var(--amethyst); }
.vjc .vjc-drawer h3 { margin: 0 0 0.7rem; border: 0; padding: 0; font-size: 1.12rem; color: #fff; }
.vjc .vjc-chips { display: flex; flex-wrap: wrap; gap: 0.5rem; }
.vjc .vjc-chip {
  margin: 0;
  border: 1px solid var(--edge);
  background: var(--velvet);
  border-radius: 999px;
  padding: 0.3rem 0.85rem 0.3rem 0.7rem;
  font-size: 0.93rem;
}
.vjc .vjc-chip::before {
  content: ''; display: inline-block; width: 8px; height: 8px; margin-right: 0.5rem;
  background: var(--amethyst); transform: rotate(45deg);
}
.vjc .vjc-chip.gold::before { background: var(--gold); }
.vjc .vjc-chip.extra { border-style: dashed; color: var(--mute); }
.vjc .vjc-drawer .vjc-note { margin-top: 0.8rem; color: var(--mute); font-size: 0.93rem; }

/* alarm panel */
.vjc .vjc-alarm {
  background: linear-gradient(160deg, var(--laser-soft), var(--plush) 55%);
  border: 1px solid rgba(255, 45, 85, 0.5);
  border-radius: 16px;
  padding: 0.4rem 1.3rem;
}
.vjc .vjc-row { margin: 0; padding: 0.85rem 0; border-top: 1px solid rgba(255, 45, 85, 0.22); }
.vjc .vjc-row:first-child { border-top: 0; }
.vjc .vjc-row p { color: var(--mute); }

/* plain rows */
.vjc .vjc-list .vjc-li { margin: 0; padding: 0.8rem 0; border-top: 1px solid var(--edge); color: var(--mute); }
.vjc .vjc-list .vjc-li:last-child { border-bottom: 1px solid var(--edge); }

/* lifts */
.vjc .vjc-lifts { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1rem; }
.vjc .vjc-lift { display: grid; grid-template-columns: 40px 1fr; gap: 0.9rem; background: var(--plush); border: 1px solid var(--edge); border-radius: 14px; padding: 1rem 1.1rem; }
.vjc .vjc-lift svg { width: 40px; height: 52px; }
.vjc .vjc-lift p { color: var(--mute); font-size: 0.95rem; }

.vjc a:focus-visible { outline: 3px solid var(--gold); outline-offset: 2px; border-radius: 4px; }
@media (prefers-reduced-motion: reduce) {
  .vjc-case .sweep { animation: none; }
}
</style>

<div class="vjc">

<section class="vjc-hero">
<h1>Jaf la bijuterii <span class="vjc-hrs"><span>-</span> <span>300h</span></span></h1>
<p class="vjc-lead">Blochezi usile magazinului, spargi vitrinele cu arma in mana si deschizi seiful din spate. Totul in echipa si contra cronometru, cu politia pe drum.</p>
<svg class="vjc-case" viewBox="0 0 640 230" role="img" aria-label="O vitrina cu bijuterii, un ceas si un lantisor, traversata de raze laser rosii">
<rect class="cab" x="70" y="150" width="500" height="60" rx="6"/>
<rect class="pad" x="96" y="132" width="448" height="20" rx="4"/>
<rect class="glass" x="96" y="40" width="448" height="112" rx="6"/>
<path class="shine" d="M118 56 L150 56 M118 66 L134 66"/>
<polygon class="gem" points="170,112 186,96 202,112 186,132"/>
<polygon class="gem" points="214,118 224,108 234,118 224,130"/>
<path class="gold" d="M268 86 C 290 136, 350 136, 372 86"/>
<polygon class="gem" points="320,124 330,114 340,124 330,138"/>
<circle class="face" cx="440" cy="110" r="20"/>
<path class="gold" d="M440 98 L440 110 L449 116"/>
<rect class="goldfill" x="434" y="80" width="12" height="10" rx="2"/>
<rect class="goldfill" x="434" y="130" width="12" height="8" rx="2"/>
<polygon class="gem" points="494,116 506,102 518,116 506,132"/>
<g class="sweep">
<line class="glow" x1="140" y1="20" x2="300" y2="200"/>
<line class="beam" x1="140" y1="20" x2="300" y2="200"/>
<line class="glow" x1="500" y1="20" x2="340" y2="200"/>
<line class="beam" x1="500" y1="20" x2="340" y2="200"/>
<line class="glow" x1="320" y1="14" x2="320" y2="210"/>
<line class="beam" x1="320" y1="14" x2="320" y2="210"/>
</g>
<circle class="emitter" cx="40" cy="96" r="5"/>
<circle class="emitter" cx="600" cy="96" r="5"/>
<line class="beam" x1="40" y1="96" x2="600" y2="96"/>
<text x="70" y="226">VITRINA 01</text>
</svg>
<ul class="vjc-tags">
<li class="vjc-tag"><span>Ore jucate</span><strong>300h fiecare</strong></li>
<li class="vjc-tag"><span>Echipa</span><strong>2 - 8 jucatori</strong></li>
<li class="vjc-tag"><span>Politie de serviciu</span><strong>minim 4</strong></li>
<li class="vjc-tag"><span>Nu pot intra</span><strong>politisti, medici</strong></li>
</ul>
</section>

<h2>Cum il pornesti</h2>
<p class="vjc-p">Jaful il planifici la <b>Lester</b>. Locul lui il afli in joc. Din lista lui de jafuri alegi <b>Jaf de bijuterii</b>. Tot de acolo intri in <b>Meniu echipa</b>, unde faci echipa, si in <b>De ce am nevoie?</b>, unde vezi cerintele la zi.</p>
<p class="vjc-p">Doar liderul echipei porneste si opreste jaful. Fiecare membru are nevoie de minim 300 de ore jucate si de o geanta vizibila pe spate. Jaful nu porneste cat timp un jaf de banca este in desfasurare, nici dupa un jaf recent la bijuterii.</p>

<h2>Ce iei cu tine</h2>
<ul class="vjc-tray">
<li class="vjc-slot">
<svg viewBox="0 0 44 44" aria-hidden="true"><path class="vjc-ico" d="M8 30 C 8 14, 36 14, 36 30 M14 30 h16 M22 30 v6"/></svg>
<div><h3>Soricel</h3><p>Un singur soricel blocheaza toate usile magazinului. Il cumperi de la Home Depot.</p></div>
</li>
<li class="vjc-slot">
<svg viewBox="0 0 44 44" aria-hidden="true"><rect class="vjc-ico" x="8" y="12" width="28" height="20" rx="3"/><path class="vjc-ico" d="M8 18 h28 M13 26 h8"/></svg>
<div><h3>Card acces</h3><p>Deschide usa spre seif. Il poti gasi la ultimul inamic din misiunile grele, dar nu de fiecare data.</p></div>
</li>
<li class="vjc-slot">
<svg viewBox="0 0 44 44" aria-hidden="true"><path class="vjc-ico" d="M4 20 h26 l4 -4 h6 v8 h-10 l-3 3 h-6 l-2 7 h-5 l2 -7 H4 z"/></svg>
<div><h3>Arma de calibru mare</h3><p>Pusca de asalt, pusca cu alice sau SMG. Cu pistolul sau cu pumnii nu spargi vitrina.</p></div>
</li>
<li class="vjc-slot">
<svg viewBox="0 0 44 44" aria-hidden="true"><path class="vjc-ico" d="M12 16 h20 l3 22 H9 z M17 16 c0 -8 10 -8 10 0"/></svg>
<div><h3>Geanta vizibila</h3><p>Toata echipa o poarta la pornire. Fara geanta pe spate nu iei nimic din vitrine.</p></div>
</li>
<li class="vjc-slot">
<svg viewBox="0 0 44 44" aria-hidden="true"><path class="vjc-ico" d="M10 34 L30 14 M14 10 L34 30 M8 36 a4 4 0 1 0 0.1 0 M36 36 a4 4 0 1 0 0.1 0"/></svg>
<div><h3>Cutter (optional)</h3><p>Taie soricelul de pe usi. Il cumperi tot de la Home Depot.</p></div>
</li>
</ul>

<h2>Planul, pas cu pas</h2>
<ol class="vjc-plan">
<li class="vjc-step" data-n="1"><h3>Liderul porneste jaful</h3><p>Din meniul lui Lester, <b>Incepe jaful</b>. Ceasul porneste imediat, iar GPS-ul te duce la magazinul de bijuterii. Timpul ramas il vezi in meniu si in notificare.</p></li>
<li class="vjc-step" data-n="2"><h3>Blocheaza usile</h3><p>Langa usile de la intrare, foloseste <b>Soricel</b> din inventar. Usile se inchid pentru toata lumea si jaful devine activ. La scurt timp porneste alarma.</p></li>
<li class="vjc-step" data-n="3"><h3>Sparge vitrinele</h3><p>Cu arma in mana, apropie-te de o vitrina si apasa <kbd>E</kbd>. Spargi sticla si strangi bijuteriile. Pe o vitrina lucreaza un singur om si fiecare se sparge o singura data, asa ca impartiti-va.</p></li>
<li class="vjc-step" data-n="4"><h3>Deschide usa seifului</h3><p>La usa din spatele magazinului apasa <kbd>H</kbd> si scanezi <b>Card acces</b>. Cardul se consuma, iar usa ramane deschisa pentru toata echipa.</p></li>
<li class="vjc-step" data-n="5"><h3>Sparge seiful</h3><p>La seif apasa <kbd>H</kbd> si treci minijocul. Lucreaza un singur om odata. Daca gresesti, mai incerci. Seiful se goleste o singura data pe jaf.</p></li>
<li class="vjc-step" data-n="6"><h3>Iesi din magazin</h3><p>Cand ati terminat, liderul opreste jaful din meniu sau plecati din magazin. Usile se deblocheaza, iar vitrinele raman sparte o vreme.</p></li>
</ol>

<h2>Ce iei din magazin</h2>
<div class="vjc-loot">
<div class="vjc-drawer">
<h3>Din vitrine</h3>
<ul class="vjc-chips">
<li class="vjc-chip">Brosa cu ametist</li>
<li class="vjc-chip">Lantisor cu ametist</li>
<li class="vjc-chip gold">Ceas de aur</li>
</ul>
<p class="vjc-note">Nu toate vitrinele au ceva in ele. Uneori pleci cu mana goala.</p>
</div>
<div class="vjc-drawer safe">
<h3>Din seif</h3>
<ul class="vjc-chips">
<li class="vjc-chip">Lantisor de platina</li>
<li class="vjc-chip">Ceas de platina</li>
<li class="vjc-chip">Ceas cu diamante</li>
<li class="vjc-chip extra">uneori un Temporizator</li>
</ul>
<p class="vjc-note">Seiful are piesele cele mai scumpe. Il deschide un singur om si tot castigul ajunge la el.</p>
</div>
</div>
<p class="vjc-p vjc-after">Bijuteriile le vinzi la un cumparator de bijuterii care plateste in <b>bani murdari</b>. Unde sta, afli in joc. Plata depinde de piesa. Daca nu ai loc in inventar cand strangi, bijuteria se pierde.</p>

<h2>Alarma, politia si riscuri</h2>
<ul class="vjc-alarm">
<li class="vjc-row"><b>La scurt timp dupa ce blochezi usile</b><p>Politistii de serviciu primesc alerta, iar alarma suna in toata zona. Alarma nu se poate opri pana la finalul jafului. Trecatorii se ghemuiesc la pamant.</p></li>
<li class="vjc-row"><b>Politia taie soricelul</b><p>Cu un <b>Cutter</b>, politia deblocheaza usile si intra. Daca mai ai un <b>Soricel</b>, blochezi intrarea din nou si jaful continua.</p></li>
<li class="vjc-row"><b>Seiful nu e garantat</b><p>Fara <b>Card acces</b> nu ajungi la seif, iar fara arma potrivita nu spargi nicio vitrina.</p></li>
</ul>

<h2>Cand se termina jaful</h2>
<ul class="vjc-list">
<li class="vjc-li"><b>Expira timpul.</b> Jaful se opreste singur la limita de timp.</li>
<li class="vjc-li"><b>Liderul il opreste</b> din meniu. Doar el poate face asta.</li>
<li class="vjc-li"><b>Echipa cade.</b> Daca toti membrii sunt morti sau au iesit din magazin, jaful se opreste dupa cateva verificari.</li>
<li class="vjc-li"><b>Iesi de pe server sau te deloghezi.</b> Iesi din jaf, dar pauza de dupa jaf ti se aplica oricum.</li>
<li class="vjc-li"><b>Dupa jaf urmeaza o pauza</b>, atat pentru tine, cat si pentru magazinele de bijuterii.</li>
</ul>

<h2>Lifturile din zona</h2>
<div class="vjc-lifts">
<div class="vjc-lift">
<svg viewBox="0 0 40 52" aria-hidden="true"><rect class="vjc-ico" x="4" y="4" width="32" height="44" rx="3"/><path class="vjc-ico" d="M20 4 v44 M12 20 l-4 4 l4 4 M28 20 l4 4 l-4 4"/></svg>
<p><b>Din magazin pe acoperis.</b> Liftul din interiorul magazinului te urca direct pe acoperisul lui.</p>
</div>
<div class="vjc-lift">
<svg viewBox="0 0 40 52" aria-hidden="true"><rect class="vjc-ico" x="4" y="4" width="32" height="44" rx="3"/><path class="vjc-ico" d="M14 22 l6 -6 l6 6 M14 32 l6 6 l6 -6"/></svg>
<p><b>Cladirea de vizavi.</b> Un lift te urca pe acoperisul cladirii de peste drum, cu vedere spre magazin. Il pot folosi si hotii, si politia.</p>
</div>
</div>

</div>
