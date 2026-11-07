---
outline: false
---

<style>
.xcar {
  --pit: #0f1012;
  --floor: #17191c;
  --bay: #202328;
  --edge: #343941;
  --text: #ecedee;
  --mute: #9ea4ab;
  --steel: #b7bec6;
  --steel-dark: #6c747d;
  --hazard: #f5b301;
  --hazard-soft: rgba(245, 179, 1, 0.13);
  --siren: #ff5a4f;
  --siren-soft: rgba(255, 90, 79, 0.12);
  --mono: ui-monospace, 'SFMono-Regular', 'Cascadia Mono', Consolas, monospace;
  max-width: 920px;
  margin: 0 auto;
  color: var(--text);
  font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.xcar *, .xcar *::before, .xcar *::after { box-sizing: border-box; }
.xcar p, .xcar li { line-height: 1.6; color: var(--text); margin: 0; }
.xcar ul, .xcar ol { list-style: none; padding: 0; margin: 0; }
.xcar li + li { margin-top: 0; }
.xcar b { color: #fff; font-weight: 650; }

/* hero: the target photo Nelu hands you */
.xcar-hero {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 300px), 1fr));
  gap: clamp(1.2rem, 3vw, 2rem);
  align-items: center;
  background:
    repeating-linear-gradient(135deg, var(--hazard) 0 14px, var(--pit) 14px 28px) top / 100% 8px no-repeat,
    radial-gradient(90% 80% at 0% 100%, var(--hazard-soft), transparent 60%),
    var(--pit);
  border: 1px solid var(--edge);
  border-radius: 22px;
  padding: clamp(1.5rem, 4vw, 2.6rem) clamp(1.25rem, 4vw, 2.5rem) clamp(1.25rem, 4vw, 2.5rem);
  overflow: hidden;
}
.xcar .xcar-hero h1 {
  margin: 0 0 0.7rem;
  border: 0;
  padding: 0;
  font-size: clamp(2rem, 6.5vw, 3.4rem);
  line-height: 1.05;
  font-weight: 850;
  letter-spacing: -0.02em;
  color: #fff;
}
.xcar-hrs { display: inline-flex; gap: 0.3em; white-space: nowrap; color: var(--hazard); }
.xcar .xcar-lead { max-width: 46ch; color: var(--mute); font-size: 1.05rem; }
.xcar .xcar-chips { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1.1rem; }
.xcar .xcar-chips li {
  margin: 0;
  font-size: 0.88rem;
  background: var(--bay);
  border: 1px solid var(--edge);
  border-left: 4px solid var(--hazard);
  border-radius: 6px;
  padding: 0.3rem 0.75rem;
}
.xcar-photo {
  justify-self: center;
  width: min(100%, 330px);
  background: #f2efe8;
  padding: 12px 12px 14px;
  border-radius: 4px;
  transform: rotate(2.5deg);
  box-shadow: 0 22px 45px rgba(0, 0, 0, 0.55);
}
.xcar-photo svg { display: block; width: 100%; height: auto; border-radius: 2px; }
.xcar-photo .sky { fill: #2b3138; }
.xcar-photo .ground { fill: #1b1e22; }
.xcar-photo .body { fill: #59616b; }
.xcar-photo .glass { fill: #9fb3c4; opacity: 0.55; }
.xcar-photo .tyre { fill: #0c0d0f; }
.xcar-photo .rim { fill: var(--steel); }
.xcar-photo .lamp { fill: var(--hazard); }
.xcar-photo .plate { fill: #f7f7f2; stroke: #111; stroke-width: 1; }
.xcar-photo .eu { fill: #1f47b8; }
.xcar-photo .ptxt { fill: #111; font: 700 11px ui-monospace, Consolas, monospace; letter-spacing: 1px; }
.xcar-photo .stamp { fill: none; stroke: var(--siren); stroke-width: 2.5; }
.xcar-photo .stxt { fill: var(--siren); font: 800 12px system-ui, sans-serif; letter-spacing: 2px; }
.xcar .xcar-photo p {
  margin-top: 0.55rem;
  color: #2a2722;
  font-family: var(--mono);
  font-size: 0.78rem;
  line-height: 1.45;
}
.xcar .xcar-photo .xcar-warn { color: #a3271f; font-weight: 700; }

.xcar h2 {
  margin: 3rem 0 1rem;
  border: 0;
  padding: 0;
  font-size: 1.45rem;
  font-weight: 750;
  letter-spacing: -0.01em;
  color: #fff;
}
.xcar .xcar-intro { color: var(--mute); max-width: 62ch; margin-bottom: 1rem; }

/* requirements: a stamped VIN plate */
.xcar-vin {
  position: relative;
  background: linear-gradient(160deg, #3b4148, #262a30 55%, #30353b);
  border: 1px solid #4b525a;
  border-radius: 10px;
  padding: 1.6rem clamp(1rem, 4vw, 2rem);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.12), 0 10px 30px rgba(0, 0, 0, 0.35);
}
.xcar-vin::before, .xcar-vin::after {
  content: '';
  position: absolute;
  top: 0.6rem;
  width: 0.7rem;
  height: 0.7rem;
  border-radius: 50%;
  background: radial-gradient(circle at 35% 35%, #d9dee3, #5d646c);
}
.xcar-vin::before { left: 0.6rem; }
.xcar-vin::after { right: 0.6rem; }
.xcar .xcar-vin-head {
  font-family: var(--mono);
  font-size: 0.75rem;
  letter-spacing: 0.25em;
  color: var(--steel);
  text-align: center;
  margin-bottom: 1rem;
}
.xcar .xcar-specs { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 360px), 1fr)); gap: 0.6rem 1.4rem; }
.xcar .xcar-specs li {
  margin: 0;
  display: grid;
  grid-template-columns: 7.5rem 1fr;
  gap: 0.6rem;
  align-items: baseline;
  padding: 0.45rem 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}
.xcar .xcar-specs .xcar-key {
  font-family: var(--mono);
  font-size: 0.72rem;
  letter-spacing: 0.12em;
  color: var(--steel-dark);
  text-transform: uppercase;
}
.xcar .xcar-specs .xcar-val { color: #fff; font-family: var(--mono); font-weight: 700; text-shadow: 0 1px 0 #000; }
.xcar .xcar-specs .xcar-val.xcar-red { color: var(--siren); }
.xcar .xcar-specs .xcar-note { display: block; color: var(--mute); font-family: inherit; font-weight: 400; font-size: 0.88rem; text-shadow: none; }

/* Nelu */
.xcar-nelu {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 1rem 1.2rem;
  align-items: start;
  background: var(--floor);
  border: 1px solid var(--edge);
  border-radius: 16px;
  padding: 1.2rem 1.3rem;
}
.xcar-avatar { width: 56px; height: 56px; }
.xcar-avatar .head { fill: var(--bay); stroke: var(--hazard); stroke-width: 2; }
.xcar-avatar .cup { fill: var(--hazard); }
.xcar .xcar-nelu p { color: var(--mute); }
.xcar .xcar-menu { grid-column: 1 / -1; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 190px), 1fr)); gap: 0.5rem; }
.xcar .xcar-menu li {
  margin: 0;
  background: var(--bay);
  border: 1px solid var(--edge);
  border-radius: 10px;
  padding: 0.6rem 0.8rem;
  font-size: 0.92rem;
  color: var(--mute);
}
.xcar .xcar-menu .xcar-opt { display: block; color: #fff; font-weight: 650; }

/* flow: a route with road-sign markers */
.xcar .xcar-route { position: relative; counter-reset: xcar-step; }
.xcar .xcar-route::before {
  content: '';
  position: absolute;
  left: 17px;
  top: 6px;
  bottom: 6px;
  width: 3px;
  background: repeating-linear-gradient(to bottom, var(--hazard) 0 10px, transparent 10px 20px);
  opacity: 0.55;
}
.xcar .xcar-route li {
  counter-increment: xcar-step;
  position: relative;
  margin: 0;
  padding: 0 0 1.35rem 3.3rem;
}
.xcar .xcar-route li:last-child { padding-bottom: 0; }
/* ::before draws the rotated diamond, ::after holds the upright step number on top of it */
.xcar .xcar-route li::before, .xcar .xcar-route li::after {
  position: absolute;
  left: 0;
  top: 0;
  width: 37px;
  height: 37px;
}
.xcar .xcar-route li::after {
  content: counter(xcar-step);
  display: grid;
  place-items: center;
  font-size: 0.9rem;
  font-weight: 800;
  color: var(--pit);
}
.xcar .xcar-route li::before {
  content: '';
  background: var(--hazard);
  border: 3px solid var(--pit);
  outline: 2px solid var(--hazard);
  border-radius: 8px;
  transform: rotate(45deg) scale(0.82);
}
.xcar .xcar-route li.xcar-risk::before { background: var(--siren); outline-color: var(--siren); }
.xcar .xcar-route .xcar-t { display: block; color: #fff; font-weight: 700; font-size: 1.05rem; margin-bottom: 0.15rem; }
.xcar .xcar-route p { color: var(--mute); }
.xcar .xcar-route .xcar-alert { display: block; margin-top: 0.35rem; color: var(--siren); font-size: 0.92rem; }
.xcar kbd {
  font-family: var(--mono);
  font-size: 0.85em;
  font-weight: 800;
  color: var(--pit);
  background: var(--hazard);
  border: 0;
  border-radius: 5px;
  box-shadow: 0 2px 0 #9b7100;
  padding: 0.05rem 0.45rem;
}

/* chop diagram */
.xcar-chop {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr));
  gap: 1.2rem;
  align-items: center;
  background: var(--floor);
  border: 1px solid var(--edge);
  border-radius: 16px;
  padding: clamp(1rem, 3vw, 1.5rem);
}
.xcar-plan { display: block; width: 100%; max-width: 360px; height: auto; margin: 0 auto; }
.xcar-plan .shell { fill: var(--bay); stroke: var(--steel-dark); stroke-width: 2; }
.xcar-plan .cabin { fill: #2c3138; stroke: var(--steel-dark); stroke-width: 1.5; }
.xcar-plan .part { fill: var(--hazard-soft); stroke: var(--hazard); stroke-width: 2; stroke-dasharray: 6 4; }
.xcar-plan .wheel { fill: #0b0c0e; stroke: var(--hazard); stroke-width: 2; }
.xcar-plan .lbl { fill: var(--steel); font: 600 12px system-ui, sans-serif; }
.xcar-plan .cut { stroke: var(--hazard); stroke-width: 1.5; }
.xcar-plan .march { animation: xcar-march 1.6s linear infinite; }
@keyframes xcar-march { to { stroke-dashoffset: -20; } }
.xcar .xcar-parts li {
  margin: 0;
  display: flex;
  gap: 0.7rem;
  align-items: baseline;
  padding: 0.55rem 0;
  border-top: 1px solid var(--edge);
}
.xcar .xcar-parts li:first-child { border-top: 0; }
.xcar .xcar-parts .xcar-item { color: var(--hazard); font-family: var(--mono); font-size: 0.85rem; white-space: nowrap; }
.xcar .xcar-parts p { color: var(--mute); }
.xcar .xcar-chop-note { color: var(--mute); font-size: 0.93rem; margin-top: 0.9rem; }

/* team */
.xcar-team { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr)); gap: 1rem; }
.xcar-card { background: var(--floor); border: 1px solid var(--edge); border-radius: 16px; padding: 1.2rem 1.3rem; }
.xcar-card.xcar-lead-card { border-color: rgba(245, 179, 1, 0.55); background: linear-gradient(160deg, var(--hazard-soft), var(--floor) 60%); }
.xcar .xcar-card h3 { margin: 0 0 0.45rem; border: 0; padding: 0; font-size: 1.1rem; color: #fff; }
.xcar .xcar-card p { color: var(--mute); }

/* risks */
.xcar-risks { border: 1px solid rgba(255, 90, 79, 0.4); border-radius: 16px; background: linear-gradient(180deg, var(--siren-soft), transparent 70%), var(--floor); padding: clamp(1rem, 3vw, 1.5rem); }
.xcar .xcar-risks li {
  margin: 0;
  position: relative;
  padding: 0.65rem 0 0.65rem 1.6rem;
  border-top: 1px solid rgba(255, 90, 79, 0.16);
}
.xcar .xcar-risks li:first-child { border-top: 0; padding-top: 0; }
.xcar .xcar-risks li::before {
  content: '!';
  position: absolute;
  left: 0;
  top: 0.75rem;
  width: 1.05rem;
  height: 1.05rem;
  display: grid;
  place-items: center;
  font-size: 0.75rem;
  font-weight: 900;
  color: var(--pit);
  background: var(--siren);
  border-radius: 3px;
}
.xcar .xcar-risks li:first-child::before { top: 0.1rem; }

.xcar a:focus-visible { outline: 3px solid var(--hazard); outline-offset: 2px; border-radius: 4px; }
@media (prefers-reduced-motion: reduce) {
  .xcar-plan .march { animation: none; }
}
</style>

<div class="xcar">

<section class="xcar-hero">
<div>
<h1>Jaf la masini <span class="xcar-hrs"><span>-</span> <span>30h</span></span></h1>
<p class="xcar-lead">Nelu iti da poza unei masini si o zona pe harta. Tu o gasesti, o spargi, o duci la dezmembrat si vinzi piesele. Poti lucra singur sau cu un partener.</p>
<ul class="xcar-chips">
<li>Singur sau in echipa de maxim 2</li>
<li>Nu e nevoie de politisti in serviciu</li>
<li>Piese, bani si obiecte</li>
</ul>
</div>
<div class="xcar-photo">
<svg viewBox="0 0 300 170" role="img" aria-label="Poza masinii tinta, cu numarul de inmatriculare si o stampila care spune tinta">
<rect class="sky" x="0" y="0" width="300" height="120"/>
<rect class="ground" x="0" y="118" width="300" height="52"/>
<path class="body" d="M30 112 L 38 92 Q 44 82 58 80 L 98 76 L 124 56 Q 132 50 146 50 L 196 50 Q 210 50 220 60 L 238 76 L 262 82 Q 274 86 274 98 L 274 112 Z"/>
<path class="glass" d="M106 77 L 128 58 Q 133 55 142 55 L 168 55 L 168 77 Z"/>
<path class="glass" d="M174 55 L 196 55 Q 206 55 213 62 L 226 77 L 174 77 Z"/>
<rect class="lamp" x="262" y="90" width="10" height="6" rx="2"/>
<circle class="tyre" cx="84" cy="114" r="19"/>
<circle class="rim" cx="84" cy="114" r="8"/>
<circle class="tyre" cx="226" cy="114" r="19"/>
<circle class="rim" cx="226" cy="114" r="8"/>
<rect class="plate" x="112" y="138" width="86" height="20" rx="2"/>
<rect class="eu" x="112" y="138" width="12" height="20"/>
<text class="ptxt" x="130" y="152">B482913</text>
<rect class="stamp" x="204" y="12" width="84" height="26" rx="4" transform="rotate(8 246 25)"/>
<text class="stxt" x="246" y="30" text-anchor="middle" transform="rotate(8 246 25)">TINTA</text>
</svg>
<p>Imagine cu masina. Nr. inmatriculare: B482913.</p>
<p class="xcar-warn">Atentie! Culoarea vehiculului poate sa NU corespunda!</p>
</div>
</section>

<h2>Ce iti trebuie</h2>
<div class="xcar-vin">
<p class="xcar-vin-head">FISA JAFULUI</p>
<ul class="xcar-specs">
<li><span class="xcar-key">Ore jucate</span><span class="xcar-val">30h<span class="xcar-note">pentru fiecare om din echipa</span></span></li>
<li><span class="xcar-key">Echipa</span><span class="xcar-val">1 - 2 jucatori<span class="xcar-note">singur sau cu un partener</span></span></li>
<li><span class="xcar-key">Politie</span><span class="xcar-val">0 in serviciu<span class="xcar-note">poti incepe oricand</span></span></li>
<li><span class="xcar-key">Scule</span><span class="xcar-val">Lockpick simplu<span class="xcar-note">de la Home depot; ia mai multe, se consuma la fiecare incercare</span></span></li>
<li><span class="xcar-key">Inventar</span><span class="xcar-val">Loc liber<span class="xcar-note">piesele sunt grele si le iei in brate</span></span></li>
<li><span class="xcar-key">Interzis</span><span class="xcar-val xcar-red">Politisti, medici<span class="xcar-note">nici ca parteneri</span></span></li>
</ul>
</div>

<h2>Nelu, omul cu masinile</h2>
<div class="xcar-nelu">
<svg class="xcar-avatar" viewBox="0 0 56 56" aria-hidden="true">
<circle class="head" cx="28" cy="28" r="26"/>
<path class="cup" d="M18 22 h16 l-2 18 h-12 z"/>
<path d="M34 26 q6 0 6 6 t-6 6" fill="none" stroke="#f5b301" stroke-width="2.5"/>
</svg>
<p>Nelu bea o cafea undeva prin oras si nu apare pe harta. Afla de la altii unde il gasesti. Cand ajungi la el, apasa <kbd>E</kbd> si vorbesti cu el.</p>
<ul class="xcar-menu">
<li><span class="xcar-opt">De ce am nevoie?</span>iti spune ce scule sa iei</li>
<li><span class="xcar-opt">Meniu echipa</span>faci sau gestionezi echipa</li>
<li><span class="xcar-opt">Incepe jaf</span>pornesti jaful, singur sau ca lider</li>
<li><span class="xcar-opt">Opreste/finalizeaza jaf</span>inchizi jaful, doar ca lider</li>
</ul>
</div>

<h2>Pas cu pas</h2>
<ol class="xcar-route">
<li><p><span class="xcar-t">Porneste jaful de la Nelu</span>Alege <b>Incepe jaf</b>. In echipa, doar liderul il poate porni. Daca cineva din echipa nu indeplineste conditiile, toata echipa vede cine si de ce.</p></li>
<li><p><span class="xcar-t">Studiaza poza</span>Fiecare primeste o <b>Imagine cu masina</b>, cu modelul si numarul de inmatriculare. Pe harta apare un cerc cu zona in care e parcata. Culoarea din poza poate fi alta decat cea reala, asa ca te iei dupa numar.</p></li>
<li><p><span class="xcar-t">Gaseste masina</span>Masina apare cand intri in zona marcata. E incuiata. Ai un timp limitat pentru tot jaful, din momentul in care l-ai pornit.</p></li>
<li class="xcar-risk"><p><span class="xcar-t">Sparge usa</span>Foloseste un <b>Lockpick simplu</b> langa masina si treci minijocul. Masina tinta o poti sparge chiar si intr-o zona protejata.<span class="xcar-alert">Lockpick-ul se consuma la fiecare incercare, reusita sau nu. Daca gresesti, politia poate primi o alerta.</span></p></li>
<li class="xcar-risk"><p><span class="xcar-t">Leaga firele</span>Nu ai cheie. Urca la volan si apasa <kbd>H</kbd> ca sa legi firele. Alarma masinii suna cat lucrezi. Nu iese din prima de fiecare data: incearca din nou.<span class="xcar-alert">Cand legi firele gresit, politia poate primi o alerta.</span></p></li>
<li><p><span class="xcar-t">Goleste portbagajul si torpedoul</span>In ele gasesti bani, bani murdari si diverse obiecte. Ia tot inainte sa distrugi masina.</p></li>
<li><p><span class="xcar-t">Du masina la dezmembrat</span>Zona de dezmembrare e la codul postal 826. Primesti o notificare cand intri cu masina in ea.</p></li>
<li><p><span class="xcar-t">Dezmembreaza piesele</span>Tine apasat <kbd>G</kbd> pe masina si alege piesa. Fiecare piesa ajunge in inventarul celui care a scos-o.</p></li>
<li><p><span class="xcar-t">Distruge masina</span>Cand ai terminat, alege <b>Distruge masina</b> din acelasi meniu de pe <kbd>G</kbd>.</p></li>
<li><p><span class="xcar-t">Vinde piesele</span>Mergi la <b>Vanzare parti auto</b>, chiar langa zona de dezmembrare (o vezi pe harta). Acolo iei bani curati pe piese.</p></li>
</ol>

<h2>Ce scoti de pe masina</h2>
<div class="xcar-chop">
<svg class="xcar-plan" viewBox="0 0 240 360" role="img" aria-label="Masina vazuta de sus, cu rotile, usile, capota si portbagajul marcate pentru dezmembrare">
<rect class="shell" x="50" y="20" width="140" height="320" rx="46"/>
<rect class="part march" x="62" y="30" width="116" height="62" rx="26"/>
<rect class="cabin" x="66" y="104" width="108" height="150" rx="18"/>
<rect class="part march" x="54" y="110" width="20" height="62" rx="6"/>
<rect class="part march" x="166" y="110" width="20" height="62" rx="6"/>
<rect class="part march" x="54" y="182" width="20" height="62" rx="6"/>
<rect class="part march" x="166" y="182" width="20" height="62" rx="6"/>
<rect class="part march" x="62" y="266" width="116" height="62" rx="22"/>
<rect class="wheel" x="30" y="56" width="22" height="46" rx="7"/>
<rect class="wheel" x="188" y="56" width="22" height="46" rx="7"/>
<rect class="wheel" x="30" y="256" width="22" height="46" rx="7"/>
<rect class="wheel" x="188" y="256" width="22" height="46" rx="7"/>
<text class="lbl" x="120" y="66" text-anchor="middle">capota</text>
<text class="lbl" x="120" y="182" text-anchor="middle">usi</text>
<text class="lbl" x="120" y="302" text-anchor="middle">portbagaj</text>
<text class="lbl" x="6" y="122">roata</text>
</svg>
<div>
<ul class="xcar-parts">
<li><span class="xcar-item">Roata de masina</span><p>de la fiecare roata</p></li>
<li><span class="xcar-item">Usa de masina</span><p>usile din fata, plus cele din spate daca masina are</p></li>
<li><span class="xcar-item">Capota de masina</span><p>capota din fata</p></li>
<li><span class="xcar-item">Portbagaj de masina</span><p>capacul portbagajului</p></li>
</ul>
<p class="xcar-chop-note">Piesele se scot doar cat masina sta in zona de dezmembrare. Cat cari o piesa o tii in brate: nu poti alerga si nu poti umbla in inventar.</p>
</div>
</div>

<h2>Singur sau in doi</h2>
<div class="xcar-team">
<div class="xcar-card">
<h3>Singur</h3>
<p>Pornesti si opresti jaful tu. Tot ce scoti de pe masina si tot ce gasesti in ea e al tau.</p>
</div>
<div class="xcar-card xcar-lead-card">
<h3>Cu un partener</h3>
<p>Faceti echipa din <b>Meniu echipa</b> de la Nelu, cel mult 2 oameni. Liderul porneste si opreste jaful. Fiecare primeste poza masinii, fiecare scoate piese pentru el. Daca unul iese de pe server, celalalt continua.</p>
</div>
</div>

<h2>Ce poate merge prost</h2>
<div class="xcar-risks">
<ul>
<li><p><b>Expira timpul.</b> Jaful se anuleaza singur, iar masina dispare cu tot ce era in ea.</p></li>
<li><p><b>Masina nu e in zona de dezmembrare.</b> Nu poti scoate nicio piesa pana nu o duci acolo.</p></li>
<li><p><b>Nu ai loc in inventar.</b> Piesa nu se scoate. Fa loc si incearca din nou.</p></li>
<li><p><b>Vrei sa opresti jaful prea devreme.</b> Liderul il poate opri de la Nelu abia dupa un timp de la pornire. La oprire, masina dispare.</p></li>
<li><p><b>Ati dat deja un jaf la masini.</b> Dupa fiecare jaf, fiecare om din echipa asteapta o pauza pana la urmatorul. Pauza porneste cand incepe jaful.</p></li>
<li><p><b>Ies toti de pe server.</b> Cand nu mai ramane nimeni din echipa, jaful se termina.</p></li>
</ul>
</div>

<h2>In plus</h2>
<div class="xcar-team">
<div class="xcar-card">
<h3>Happy Hour</h3>
<p>Cand Happy Hour e activ pentru jafurile la masini, gasesti mai multe lucruri in portbagaj si in torpedou.</p>
</div>
<div class="xcar-card">
<h3>Puncte pentru familie</h3>
<p>Daca faceti parte dintr-o familie care aduna puncte, familia primeste puncte cand dezmembrati masina complet (roti, usi, capota si portbagaj) si apoi o distrugeti.</p>
</div>
</div>

</div>
