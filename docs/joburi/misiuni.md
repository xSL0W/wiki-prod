---
outline: false
---

<style>
.ms {
  --desk: #0b0c09;
  --folder: #17180f;
  --sheet: #1e1f15;
  --rule: #34352a;
  --text: #ece6d4;
  --mute: #a59e88;
  --khaki: #cdbd8c;
  --khaki-soft: rgba(205, 189, 140, 0.12);
  --red: #e5484d;
  --red-soft: rgba(229, 72, 77, 0.14);
  --ink: #050504;
  max-width: 940px;
  margin: 0 auto;
  color: var(--text);
  font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.ms *, .ms *::before, .ms *::after { box-sizing: border-box; }
.ms p, .ms li { line-height: 1.6; color: var(--text); margin: 0; }
.ms ul, .ms ol { list-style: none; padding: 0; margin: 0; }
.ms b { color: #fff; font-weight: 650; }
.ms code { font-size: 0.88em; }
.ms kbd {
  font: inherit; font-size: 0.82em; font-weight: 800; color: var(--ink); background: var(--khaki);
  border-radius: 5px; padding: 0.05rem 0.45rem; box-shadow: 0 2px 0 #8a7d55;
}
.ms a:focus-visible { outline: 3px solid var(--khaki); outline-offset: 2px; border-radius: 4px; }
.ms-mono { font-family: ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; }
/* hero: a dossier on the desk */
.ms-dossier {
  position: relative; margin-top: 1.6rem;
  background: linear-gradient(170deg, #22231a, var(--folder) 55%);
  border: 1px solid var(--rule); border-radius: 4px 18px 18px 18px;
  padding: clamp(1.25rem, 4vw, 2.4rem);
}
.ms-dossier::before {
  content: 'DOSAR  /  ECHIPA'; position: absolute; left: -1px; top: -1.55rem; height: 1.6rem;
  padding: 0.35rem 1rem 0; border: 1px solid var(--rule); border-bottom: 0; border-radius: 10px 10px 0 0;
  background: #22231a; font: 700 0.7rem/1 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; letter-spacing: 0.16em; color: var(--khaki);
}
.ms-stamp {
  position: absolute; top: 1.1rem; right: 1.1rem; transform: rotate(8deg);
  border: 3px solid var(--red); border-radius: 6px; padding: 0.25rem 0.6rem;
  font: 800 0.8rem/1 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; letter-spacing: 0.18em; color: var(--red); opacity: 0.85;
}
@media (max-width: 480px) { .ms-stamp { position: static; display: inline-block; margin-bottom: 0.9rem; } }
.ms .ms-dossier h1 {
  margin: 0 0 0.7rem; border: 0; padding: 0; max-width: 16ch;
  font-size: clamp(2.1rem, 7vw, 3.6rem); line-height: 1.02; font-weight: 850; letter-spacing: -0.03em; color: #fff;
}
.ms-hrs { display: inline-flex; gap: 0.3em; white-space: nowrap; color: var(--khaki); }
.ms-hrs .hard { color: var(--red); }
.ms .ms-dossier > p { max-width: 54ch; color: var(--mute); font-size: 1.05rem; }
.ms-brief { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1.15fr); gap: 1.4rem; margin-top: 1.5rem; align-items: center; }
@media (max-width: 680px) { .ms-brief { grid-template-columns: minmax(0, 1fr); } }
.ms .ms-fields li {
  margin: 0; display: grid; grid-template-columns: 7.5rem minmax(0, 1fr); gap: 0.6rem;
  padding: 0.5rem 0; border-bottom: 1px dashed var(--rule); font-size: 0.93rem;
}
.ms .ms-fields li span { font: 700 0.72rem/1.9 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; letter-spacing: 0.12em; color: var(--mute); }
.ms .ms-fields li strong { color: #fff; font-weight: 650; }
.ms-redact { display: inline-block; width: 6.5em; height: 0.95em; vertical-align: -0.1em; background: var(--ink); border-radius: 2px; margin-right: 0.4em; }
.ms-map { display: block; width: 100%; height: auto; border-radius: 12px; background: #12130d; border: 1px solid var(--rule); }
.ms-map .topo { fill: none; stroke: #2c2d22; stroke-width: 1.2; }
.ms-map .road { fill: none; stroke: #3a3b2e; stroke-width: 6; stroke-linecap: round; }
.ms-map .route {
  fill: none; stroke: var(--khaki); stroke-width: 2.5; stroke-dasharray: 6 6; stroke-linecap: round;
  animation: ms-march 1.6s linear infinite;
}
.ms-map .zone { fill: var(--red-soft); stroke: var(--red); stroke-width: 2; stroke-dasharray: 4 4; }
.ms-map .cross { stroke: var(--red); stroke-width: 2; }
.ms-map .foe { stroke: #f07a7d; stroke-width: 2.5; stroke-linecap: round; }
.ms-map .scan { fill: none; stroke: var(--red); stroke-width: 1.5; transform-box: fill-box; transform-origin: center; animation: ms-scan 2.8s ease-out infinite; }
.ms-map .giver { fill: var(--khaki); }
.ms-map text { fill: var(--mute); font: 700 10px ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; letter-spacing: 0.1em; }
.ms-map .t-red { fill: var(--red); }
@keyframes ms-march { to { stroke-dashoffset: -24; } }
@keyframes ms-scan { 0% { transform: scale(0.4); opacity: 0.9; } 100% { transform: scale(1.25); opacity: 0; } }
@media (prefers-reduced-motion: reduce) { .ms-map .route, .ms-map .scan { animation: none; } }
/* headings: file tabs */
.ms h2 {
  display: flex; align-items: baseline; gap: 0.75rem;
  margin: 3rem 0 1.1rem; border: 0; padding: 0;
  font-size: 1.5rem; font-weight: 780; letter-spacing: -0.015em; color: #fff;
}
.ms h2 .no { font: 700 0.8rem/1 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; letter-spacing: 0.12em; color: var(--khaki); }
.ms .ms-lead { max-width: 66ch; color: var(--mute); }
.ms .ms-lead + .ms-lead { margin-top: 0.7rem; }
.ms .ms-lead b { color: var(--text); }
.ms .ms-after-files { margin-top: 1rem; }
/* requirements: checklist */
.ms .ms-check { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr)); gap: 0.6rem; }
.ms .ms-check li {
  margin: 0; position: relative; padding: 0.8rem 1rem 0.8rem 2.8rem;
  border: 1px solid var(--rule); border-radius: 10px; background: var(--sheet); color: var(--mute); font-size: 0.95rem;
}
.ms .ms-check li::before {
  content: ''; position: absolute; left: 1rem; top: 1.05rem; width: 1rem; height: 1rem; border: 2px solid var(--khaki); border-radius: 3px;
}
.ms .ms-check li::after {
  content: ''; position: absolute; left: 1.32rem; top: 1.12rem; width: 0.35rem; height: 0.65rem;
  border: solid var(--khaki); border-width: 0 2px 2px 0; transform: rotate(45deg);
}
.ms .ms-check li.no::before { border-color: var(--red); }
.ms .ms-check li.no::after { left: 1.18rem; top: 1.47rem; width: 0.65rem; height: 0; border-width: 2px 0 0 0; border-color: var(--red); transform: rotate(45deg); }
.ms .ms-check li b { color: #fff; }
/* difficulties: two files */
.ms-files { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr)); gap: 1rem; }
.ms-file { border: 1px solid var(--rule); border-top: 4px solid var(--khaki); border-radius: 6px 6px 16px 16px; padding: 1.2rem 1.3rem; background: var(--sheet); }
.ms-file.hard { border-top-color: var(--red); background: linear-gradient(170deg, var(--red-soft), var(--sheet) 55%); }
.ms-file header { display: flex; justify-content: space-between; align-items: baseline; gap: 1rem; margin-bottom: 0.7rem; }
.ms .ms-file h3 { margin: 0; border: 0; padding: 0; font-size: 1.2rem; color: #fff; }
.ms-file .hrs { font: 800 1.35rem/1 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; color: var(--khaki); }
.ms-file.hard .hrs { color: var(--red); }
.ms .ms-file p { color: var(--mute); font-size: 0.94rem; }
.ms .ms-file p + p { margin-top: 0.5rem; }
.ms .ms-file p b { color: var(--text); }
/* operation phases */
.ms .ms-phases { counter-reset: ms-phase; display: grid; gap: 0; border-left: 2px solid var(--rule); margin-left: 0.6rem; }
.ms .ms-phases li { margin: 0; position: relative; counter-increment: ms-phase; padding: 0 0 1.4rem 1.8rem; }
.ms .ms-phases li:last-child { padding-bottom: 0; }
.ms .ms-phases li::before {
  content: ''; position: absolute; left: -0.62rem; top: 0.15rem;
  width: 1.1rem; height: 1.1rem; border-radius: 50%; background: var(--desk); border: 3px solid var(--khaki);
}
.ms .ms-phases li.fight::before { border-color: var(--red); background: var(--red); }
.ms .ms-phases li .tag { display: block; font: 700 0.7rem/1.4 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; letter-spacing: 0.14em; color: var(--khaki); }
.ms .ms-phases li.fight .tag { color: var(--red); }
.ms .ms-phases li strong { display: block; color: #fff; font-size: 1.04rem; margin: 0.1rem 0 0.2rem; }
.ms .ms-phases li p { color: var(--mute); font-size: 0.95rem; max-width: 66ch; }
.ms .ms-phases li p b { color: var(--text); }
/* rules of engagement */
.ms-rules { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 270px), 1fr)); gap: 0.75rem; }
.ms .ms-rules li { margin: 0; position: relative; padding: 1rem 1.1rem; border: 1px solid var(--rule); border-radius: 12px; background: var(--sheet); color: var(--mute); font-size: 0.94rem; }
.ms .ms-rules li b { display: block; color: #fff; margin-bottom: 0.25rem; padding-right: 4.2rem; }
.ms .ms-rules li .st {
  position: absolute; top: 0.85rem; right: 0.9rem; transform: rotate(6deg);
  border: 2px solid var(--red); border-radius: 4px; padding: 0.1rem 0.35rem;
  font: 800 0.62rem/1.2 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; letter-spacing: 0.14em; color: var(--red);
}
.ms .ms-rules li .st.ok { border-color: var(--khaki); color: var(--khaki); }
/* loot */
.ms-loot { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr)); gap: 1rem; }
.ms-crate { border: 1px solid var(--rule); border-radius: 16px; padding: 1.1rem 1.2rem; background: var(--sheet); }
.ms-crate.hard { border-color: rgba(229, 72, 77, 0.5); }
.ms .ms-crate h3 {
  margin: 0 0 0.8rem; border: 0; padding: 0; font: 700 0.78rem/1.2 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace;
  letter-spacing: 0.12em; text-transform: uppercase; color: var(--khaki);
}
.ms .ms-crate.hard h3 { color: var(--red); }
.ms .ms-crate h4 { margin: 0.9rem 0 0.45rem; border: 0; padding: 0; font-size: 0.85rem; font-weight: 650; color: var(--mute); }
.ms .ms-items { display: flex; flex-wrap: wrap; gap: 0.4rem; }
.ms .ms-items li { margin: 0; font-size: 0.88rem; padding: 0.15rem 0.65rem; border-radius: 999px; border: 1px solid var(--rule); color: var(--text); background: rgba(5, 5, 4, 0.5); }
.ms .ms-items li.key { border-color: var(--khaki); color: #fff; }
.ms .ms-note { margin-top: 1rem; color: var(--mute); font-size: 0.94rem; max-width: 66ch; }
.ms .ms-note b { color: var(--text); }
/* after the mission */
.ms .ms-after li { margin: 0; padding: 0.85rem 0; border-top: 1px solid var(--rule); color: var(--mute); }
.ms .ms-after li:last-child { border-bottom: 1px solid var(--rule); }
.ms .ms-after li b { color: #fff; }
</style>

<div class="ms">
<section class="ms-dossier">
<span class="ms-stamp" aria-hidden="true">STRICT SECRET</span>
<h1>Misiuni <span class="ms-hrs"><span>-</span> <span>150h/<span class="hard">200h</span></span></span></h1>
<p>Mike are o tinta. Tu ai o echipa. Mergeti in zona marcata, eliminati toti inamicii si strangeti castigurile lasate pe jos.</p>
<div class="ms-brief">
<ul class="ms-fields">
<li><span>CONTACT</span><strong>Mike</strong></li>
<li><span>ECHIPA</span><strong>2-6 jucatori</strong></li>
<li><span>AUTORIZARE</span><strong>150h normala / 200h grea</strong></li>
<li><span>TINTA</span><strong>Toti inamicii din zona</strong></li>
<li><span>LOCATIE</span><strong><span class="ms-redact" aria-hidden="true"></span>primesti GPS</strong></li>
</ul>
<svg class="ms-map" viewBox="0 0 360 220" role="img" aria-label="Harta misiunii: traseul de la Mike pana la zona marcata, unde asteapta inamicii">
<path class="topo" d="M-10 60 Q80 20 170 55 T370 40"/>
<path class="topo" d="M-10 95 Q90 60 180 92 T370 80"/>
<path class="topo" d="M-10 150 Q100 120 190 150 T370 140"/>
<path class="topo" d="M-10 190 Q110 165 200 190 T370 185"/>
<path class="road" d="M30 200 Q90 140 150 150 T255 100"/>
<path class="route" d="M30 200 Q90 140 150 150 T255 100"/>
<circle class="giver" cx="30" cy="200" r="7"/>
<text x="44" y="212">MIKE</text>
<circle class="zone" cx="262" cy="92" r="58"/>
<circle class="scan" cx="262" cy="92" r="58"/>
<line class="cross" x1="262" y1="40" x2="262" y2="144"/>
<line class="cross" x1="210" y1="92" x2="314" y2="92"/>
<path class="foe" d="M236 70 l8 8 m0 -8 l-8 8"/>
<path class="foe" d="M280 62 l8 8 m0 -8 l-8 8"/>
<path class="foe" d="M292 108 l8 8 m0 -8 l-8 8"/>
<path class="foe" d="M246 112 l8 8 m0 -8 l-8 8"/>
<path class="foe" d="M268 122 l8 8 m0 -8 l-8 8"/>
<text class="t-red" x="222" y="24">ZONA MISIUNII</text>
</svg>
</div>
</section>
<h2><span class="no">01</span>Conditii</h2>
<ul class="ms-check">
<li><b>Echipa de 2-6 jucatori.</b> Singur nu poti porni o misiune. Echipa o faci din <b>Meniu echipa</b>.</li>
<li><b>Doar liderul porneste misiunea</b>, stand langa Mike.</li>
<li><b>Fiecare membru are orele jucate:</b> 150h pentru misiunea normala, 200h pentru cea grea.</li>
<li><b>Nimeni nu e in pauza</b> dupa ultima misiune si nimeni nu e deja in alta misiune.</li>
<li class="no"><b>Fara politisti si medici.</b> Daca un membru e politist sau medic, echipa nu poate pleca.</li>
</ul>
<h2><span class="no">02</span>Doua dificultati</h2>
<div class="ms-files">
<div class="ms-file">
<header><h3>Misiune normala</h3><span class="hrs">150h</span></header>
<p>Inamici cu pistoale si revolvere, fara vesta.</p>
<p>Zonele sunt in nordul hartii, in jurul <b>Sandy Shores</b> si <b>Grapeseed</b>.</p>
</div>
<div class="ms-file hard">
<header><h3>Misiune grea</h3><span class="hrs">200h</span></header>
<p>Inamici cu vesta, mai rezistenti, care tintesc mai bine. Pe langa pistoale au si pistoale-mitraliera si shotgun-uri. Sunt si mai multi.</p>
<p>Zonele sunt la <b>Harmony</b>, <b>Stab City</b>, pe malul lacului Alamo si in <b>Sandy Shores</b>.</p>
</div>
</div>
<p class="ms-lead ms-after-files">La ambele, numarul de inamici creste cu marimea echipei: cu cat veniti mai multi, cu atat sunt mai multi.</p>
<h2><span class="no">03</span>Desfasurare</h2>
<ol class="ms-phases">
<li><span class="tag">FAZA 1</span><strong>Strange echipa</strong><p>Apasa <kbd>E</kbd> la Mike si deschide <b>Meniu echipa</b>. Colegii intra in echipa ta, iar tu ramai lider.</p></li>
<li><span class="tag">FAZA 2</span><strong>Alege misiunea</strong><p>Liderul alege <b>Incepe o misiune</b> si apoi dificultatea. Daca toate zonele sunt ocupate de alte echipe, asteptati putin si incercati din nou.</p></li>
<li><span class="tag">FAZA 3</span><strong>Mergeti la zona</strong><p>Toata echipa primeste pe harta zona marcata cu cerc si traseu GPS pana acolo.</p></li>
<li class="fight"><span class="tag">FAZA 4</span><strong>Contact</strong><p>Cand primul membru se apropie de zona, misiunea porneste: inamicii apar si va ataca. Dupa fiecare inamic eliminat vezi cati au mai ramas.</p></li>
<li class="fight"><span class="tag">FAZA 5</span><strong>Curatati zona</strong><p>Misiunea e reusita cand ultimul inamic cade. Din masina poti trage, dar nu ai voie sa calci pe nimeni.</p></li>
<li><span class="tag">FAZA 6</span><strong>Strangeti castigurile</strong><p>Inamicii lasa castigurile pe jos. Le pot lua doar membrii echipei, iar cine ajunge primul, ia. Dupa ultimul inamic aveti un timp limitat sa le strangeti.</p></li>
</ol>
<h2><span class="no">04</span>Reguli de lupta</h2>
<ul class="ms-rules">
<li><span class="st">ESEC</span><b>Calci un inamic cu masina</b>Misiunea pica pe loc pentru toata echipa.</li>
<li><span class="st ok">PERMIS</span><b>Tragi din masina</b>Drive-by-ul e voie, doar nu-i lovi cu vehiculul.</li>
<li><span class="st">ESEC</span><b>Toata echipa e la pamant</b>Daca toti membrii sunt morti sau incapacitati, misiunea pica.</li>
<li><span class="st">ESEC</span><b>Plecati toti din zona</b>Primiti un avertisment. Daca nu se intoarce nimeni la timp, misiunea pica.</li>
<li><span class="st">ESEC</span><b>Liderul iese din joc</b>Misiunea pica pentru toti. Daca iese alt membru, doar el pierde misiunea.</li>
<li><span class="st">BLOCAT</span><b>Nu poti chema ajutor</b>In timpul luptei, membrii echipei nu pot suna la politie sau la ambulanta.</li>
</ul>
<p class="ms-note">Liderul poate anula misiunea doar de la Mike, din meniul lui, cu <b>Anuleaza misiunea</b>. Toata echipa pierde progresul.</p>
<h2><span class="no">05</span>Castiguri</h2>
<div class="ms-loot">
<div class="ms-crate">
<h3>Misiune normala</h3>
<h4>Orice inamic poate lasa</h4>
<ul class="ms-items">
<li>Munitie de pistol</li>
<li>Bandaj</li>
<li>Vesta anti-glont usoara</li>
<li>Vesta anti-glont grea</li>
</ul>
<h4>Ultimul inamic lasa</h4>
<ul class="ms-items">
<li class="key">Bani murdari</li>
</ul>
</div>
<div class="ms-crate hard">
<h3>Misiune grea</h3>
<h4>Orice inamic poate lasa</h4>
<ul class="ms-items">
<li>Munitie de pistol</li>
<li>Munitie de pusca</li>
<li>Bandaj</li>
<li>Vesta anti-glont usoara</li>
<li>Vesta anti-glont grea</li>
</ul>
<h4>Ultimul inamic lasa</h4>
<ul class="ms-items">
<li class="key">Bani murdari</li>
<li class="key">uneori Card acces</li>
</ul>
</div>
</div>
<p class="ms-note">Ultimul inamic lasa mereu <b>Bani murdari</b>, mai multi la misiunea grea. <b>Card acces</b> deschide usa interioara la jaful magazinului de bijuterii.</p>
<h2><span class="no">06</span>Dupa misiune</h2>
<ul class="ms-after">
<li><b>Pauza pentru toata echipa.</b> Dupa orice misiune, reusita sau nu, fiecare membru asteapta o vreme pana la urmatoarea. In meniul lui Mike vezi cat mai ai.</li>
<li><b>Zona ramane goala o vreme.</b> Locul in care ati fost nu mai poate fi ales de nicio echipa pana trece pauza zonei.</li>
<li><b>Familia ta castiga puncte</b> pentru fiecare misiune terminata cu bine.</li>
</ul>
</div>
