---
title: Targul Auto
outline: false
---

<style>
.ta {
  --ink: #09090b;
  --panel: #151518;
  --panel2: #1c1c20;
  --line: #2c2c33;
  --text: #f4f4f5;
  --mute: #a1a1aa;
  --red: #ef4444;
  --red-deep: #b91c1c;
  --red-soft: rgba(239, 68, 68, 0.14);
  --tag: #facc15;
  --tag-soft: rgba(250, 204, 21, 0.13);
  --asphalt: #18181b;
  max-width: 940px;
  margin: 0 auto;
  color: var(--text);
  font-family: Inter, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.ta *, .ta *::before, .ta *::after { box-sizing: border-box; }
.ta p, .ta li { line-height: 1.6; color: var(--text); margin: 0; }
.ta ul, .ta ol { list-style: none; padding: 0; margin: 0; }
.ta li + li { margin-top: 0; }
.ta b { color: #fff; font-weight: 650; }
.ta code { white-space: normal; overflow-wrap: anywhere; }
.ta a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.ta a:focus-visible { outline: 3px solid var(--red); outline-offset: 3px; border-radius: 6px; }
.ta kbd {
  font: inherit; font-size: 0.85em; font-weight: 700; color: var(--ink); background: var(--tag);
  border-radius: 6px; padding: 0.05rem 0.45rem;
}
/* ---------- hero: the lot in cross-section, exposition above, three garage floors below ---------- */
.ta .ta-hero {
  position: relative; overflow: hidden; isolation: isolate;
  background: radial-gradient(90% 120% at 100% 0%, rgba(250, 204, 21, 0.1), transparent 55%),
              radial-gradient(110% 120% at 0% 100%, rgba(185, 28, 28, 0.26), var(--ink) 62%);
  border: 1px solid var(--line); border-radius: 22px;
  padding: clamp(1.15rem, 4vw, 2.4rem);
}
.ta .ta-kicker { font-size: 0.78rem; font-weight: 700; letter-spacing: 0.16em; text-transform: uppercase; color: var(--tag); margin-bottom: 0.55rem; }
.ta .ta-hero h1 {
  margin: 0 0 0.75rem; border: 0; padding: 0;
  font-size: clamp(2.1rem, 6.6vw, 3.5rem); line-height: 1.04; font-weight: 850; letter-spacing: -0.03em; color: #fff;
}
.ta .ta-hero h1 span { color: var(--red); }
.ta .ta-lede { max-width: 60ch; color: var(--mute); font-size: 1.05rem; }
.ta .ta-lot { display: block; width: 100%; height: auto; margin-top: 1.4rem; border-radius: 14px; }
.ta-lot .sky { fill: #0e0e12; }
.ta-lot .ground { fill: #232329; }
.ta-lot .earth { fill: #0b0b0d; }
.ta-lot .slab { fill: #1b1b20; }
.ta-lot .stripe { stroke: #3f3f46; stroke-width: 2; stroke-dasharray: 10 10; }
.ta-lot .car { fill: #3f3f46; }
.ta-lot .car.hot { fill: #b91c1c; }
.ta-lot .car.gold { fill: #a16207; }
.ta-lot .glass { fill: #0e0e12; opacity: 0.8; }
.ta-lot .wheel { fill: #09090b; stroke: #52525b; stroke-width: 1.5; }
.ta-lot .lbl { fill: #a1a1aa; font: 700 10px Inter, system-ui, sans-serif; letter-spacing: 0.12em; }
.ta-lot .lbl.hi { fill: var(--tag); }
.ta-lot .shaft { fill: #111114; stroke: #2c2c33; }
.ta-lot .cab { fill: var(--tag); animation: ta-lift 9s ease-in-out infinite; }
.ta-lot .tag { transform-box: fill-box; transform-origin: 50% 0; animation: ta-swing 3.2s ease-in-out infinite; }
.ta-lot .tag rect { fill: var(--tag); }
.ta-lot .tag text { fill: #09090b; font: 800 8px Inter, system-ui, sans-serif; }
.ta-lot .string { stroke: var(--tag); stroke-width: 1; }
.ta-lot .lamp { fill: #fde68a; opacity: 0.15; animation: ta-lamp 4.5s ease-in-out infinite; }
.ta-lot .lamp.l2 { animation-delay: 1.5s; }
.ta-lot .lamp.l3 { animation-delay: 3s; }
@keyframes ta-lift { 0%, 12% { transform: translateY(0); } 30%, 42% { transform: translateY(48px); } 60%, 72% { transform: translateY(96px); } 90%, 100% { transform: translateY(0); } }
@keyframes ta-swing { 0%, 100% { transform: rotate(-7deg); } 50% { transform: rotate(7deg); } }
@keyframes ta-lamp { 0%, 100% { opacity: 0.15; } 50% { opacity: 0.65; } }
@media (prefers-reduced-motion: reduce) {
  .ta-lot .cab, .ta-lot .tag, .ta-lot .lamp { animation: none; }
  .ta-lot .lamp { opacity: 0.4; }
}
/* ---------- sections ---------- */
.ta h2 {
  display: flex; align-items: center; gap: 0.65rem;
  margin: 3rem 0 1rem; border: 0; padding: 0;
  font-size: 1.5rem; font-weight: 750; letter-spacing: -0.015em; color: #fff;
}
.ta h2::before {
  content: ''; flex: none; width: 14px; height: 18px;
  background: var(--tag); clip-path: polygon(50% 0, 100% 28%, 100% 100%, 0 100%, 0 28%);
}
.ta h3 { margin: 0; border: 0; padding: 0; color: #fff; }
.ta .ta-lead { max-width: 66ch; }
.ta .ta-lead + .ta-lead { margin-top: 0.8rem; }
.ta .ta-gap { margin-top: 1rem; }
/* three markets */
.ta .ta-markets { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 250px), 1fr)); gap: 0.9rem; }
.ta .ta-market { position: relative; background: var(--panel); border: 1px solid var(--line); border-radius: 18px; padding: 1.15rem 1.25rem 1.2rem; }
.ta .ta-market svg { display: block; width: 46px; height: 30px; margin-bottom: 0.7rem; }
.ta .ta-market h3 { font-size: 1.15rem; }
.ta .ta-market .ta-who { display: block; margin: 0.15rem 0 0.7rem; color: var(--tag); font-weight: 650; font-size: 0.92rem; }
.ta .ta-market .ta-facts li { display: flex; justify-content: space-between; gap: 1rem; padding: 0.35rem 0; font-size: 0.92rem; color: var(--mute); }
.ta .ta-market .ta-facts li + li { border-top: 1px solid var(--line); }
.ta .ta-market .ta-facts li span:last-child { color: var(--text); text-align: right; font-weight: 600; }
.ta .ta-market .ta-path { display: block; margin-top: 0.8rem; font-size: 0.82rem; color: var(--mute); }
.ta .ta-market.main { border-color: #4a3d12; background: linear-gradient(160deg, rgba(250, 204, 21, 0.08), var(--panel) 55%); }
/* floors */
.ta .ta-floors { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1.2fr); gap: 1rem 1.6rem; align-items: start; }
.ta .ta-stack { display: grid; gap: 0.4rem; }
.ta .ta-stack li {
  display: flex; align-items: center; justify-content: space-between; gap: 0.8rem;
  padding: 0.75rem 1rem; border-radius: 12px; border: 1px solid var(--line);
  background: repeating-linear-gradient(90deg, var(--asphalt) 0 34px, #202026 34px 36px);
  font-size: 0.93rem;
}
.ta .ta-stack li b { font-weight: 700; }
.ta .ta-stack li span { color: var(--mute); font-size: 0.85rem; }
.ta .ta-stack li.expo { background: linear-gradient(100deg, rgba(250, 204, 21, 0.16), var(--panel2) 70%); border-color: #4a3d12; }
.ta .ta-stack li.expo span { color: var(--tag); }
.ta .ta-notes { display: grid; gap: 0.55rem; }
.ta .ta-notes li { position: relative; padding-left: 1.3rem; font-size: 0.95rem; }
.ta .ta-notes li::before { content: ''; position: absolute; left: 0; top: 0.6rem; width: 8px; height: 8px; border-radius: 2px; background: var(--tag); }
@media (max-width: 720px) { .ta .ta-floors { grid-template-columns: minmax(0, 1fr); } }
/* sell steps */
.ta .ta-steps { display: grid; gap: 0.7rem; counter-reset: ta-step; }
.ta .ta-steps li {
  position: relative; counter-increment: ta-step;
  background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 0.9rem 1rem 0.9rem 3.6rem;
}
.ta .ta-steps li::before {
  content: counter(ta-step); position: absolute; left: 1rem; top: 0.85rem;
  width: 1.9rem; height: 1.9rem; border-radius: 50%; display: grid; place-items: center;
  background: var(--tag); color: var(--ink); font-weight: 800; font-size: 0.95rem;
}
.ta .ta-steps h3 { font-size: 1rem; margin-bottom: 0.15rem; }
.ta .ta-steps p { color: var(--mute); font-size: 0.93rem; }
/* the sale form as a ticket */
.ta .ta-form { margin-top: 1rem; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 200px), 1fr)); gap: 0.6rem; }
.ta .ta-form li { background: var(--panel2); border: 1px dashed #3f3f46; border-radius: 12px; padding: 0.75rem 0.9rem; }
.ta .ta-form h3 { font-size: 0.95rem; margin-bottom: 0.2rem; }
.ta .ta-form p { color: var(--mute); font-size: 0.88rem; line-height: 1.45; }
/* checklists */
.ta .ta-check { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr)); gap: 0.5rem 1rem; margin-top: 1rem; }
.ta .ta-check li { position: relative; padding: 0.55rem 0.8rem 0.55rem 2.2rem; background: var(--panel); border: 1px solid var(--line); border-radius: 10px; font-size: 0.93rem; line-height: 1.45; }
.ta .ta-check li::before { content: ''; position: absolute; left: 0.85rem; top: 0.95rem; width: 9px; height: 5px; border-left: 2px solid #4ade80; border-bottom: 2px solid #4ade80; transform: rotate(-45deg); }
.ta .ta-check li.no::before { width: 10px; height: 2px; border: 0; background: var(--red); transform: none; top: 1.05rem; }
.ta .ta-subhead { margin: 1.4rem 0 0.2rem; font-size: 1.05rem; }
/* buyer panel */
.ta .ta-panel { display: grid; grid-template-columns: minmax(0, 1.25fr) minmax(0, 1fr); gap: 1rem 1.4rem; align-items: start; }
.ta .ta-screen { background: #0f0f12; border: 1px solid var(--line); border-radius: 16px; padding: 1rem 1.1rem; }
.ta .ta-screen h3 { font: 700 0.72rem/1.3 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; letter-spacing: 0.12em; text-transform: uppercase; color: var(--tag); margin: 0 0 0.4rem; }
.ta .ta-screen h3 + .ta-pills { margin-bottom: 0.9rem; }
.ta .ta-pills { display: flex; flex-wrap: wrap; gap: 0.35rem; }
.ta .ta-pills li { font-size: 0.82rem; border: 1px solid var(--line); border-radius: 999px; padding: 0.12rem 0.6rem; color: var(--text); }
.ta .ta-keys { display: grid; gap: 0.55rem; }
.ta .ta-keys li { display: flex; gap: 0.8rem; align-items: flex-start; background: var(--panel); border: 1px solid var(--line); border-radius: 12px; padding: 0.75rem 0.9rem; }
.ta .ta-keys kbd { flex: none; min-width: 2.4rem; text-align: center; font-size: 0.95rem; padding: 0.25rem 0.45rem; }
.ta .ta-keys p { font-size: 0.92rem; color: var(--mute); }
.ta .ta-keys p b { display: block; color: #fff; }
@media (max-width: 720px) { .ta .ta-panel { grid-template-columns: minmax(0, 1fr); } }
/* money flow */
.ta .ta-money { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 240px), 1fr)); gap: 0.8rem; }
.ta .ta-money li { background: var(--panel); border: 1px solid var(--line); border-left: 3px solid var(--tag); border-radius: 14px; padding: 0.95rem 1.05rem; }
.ta .ta-money li.out { border-left-color: var(--red); }
.ta .ta-money h3 { font-size: 1rem; margin-bottom: 0.25rem; }
.ta .ta-money p { color: var(--mute); font-size: 0.92rem; }
</style>

<div class="ta">

<section class="ta-hero">
<div class="ta-kicker">Locatii / vanzari intre jucatori</div>
<h1>Targul <span>Auto</span></h1>
<p class="ta-lead ta-lede">Aici iti pui masina la vanzare, cu pretul tau. Cumparatorii vin, se uita la ea si o pot cumpara pe loc, fara sa te mai caute. Banii iti intra in banca, chiar daca nu esti pe server.</p>
<svg class="ta-lot" viewBox="0 0 640 260" role="img" aria-label="Sectiune prin targ: expozitia afara si trei etaje de parcare subterana, cu liftul intre ele">
<rect class="sky" x="0" y="0" width="640" height="78"/>
<rect class="ground" x="0" y="78" width="640" height="10"/>
<rect class="earth" x="0" y="88" width="640" height="172"/>
<g>
<path class="car gold" d="M70 78 v-12 l14 -10 h40 l16 10 h14 v12 z"/>
<path class="glass" d="M90 58 h32 l10 8 h-48 z"/>
<circle class="wheel" cx="92" cy="78" r="7"/><circle class="wheel" cx="138" cy="78" r="7"/>
<path class="car hot" d="M210 78 v-12 l14 -10 h40 l16 10 h14 v12 z"/>
<path class="glass" d="M230 58 h32 l10 8 h-48 z"/>
<circle class="wheel" cx="232" cy="78" r="7"/><circle class="wheel" cx="278" cy="78" r="7"/>
<path class="car" d="M350 78 v-12 l14 -10 h40 l16 10 h14 v12 z"/>
<path class="glass" d="M370 58 h32 l10 8 h-48 z"/>
<circle class="wheel" cx="372" cy="78" r="7"/><circle class="wheel" cx="418" cy="78" r="7"/>
<line class="string" x1="246" y1="48" x2="246" y2="40"/>
<g class="tag"><rect x="230" y="22" width="34" height="18" rx="3"/><text x="234" y="34">VAND</text></g>
<line class="string" x1="106" y1="48" x2="106" y2="40"/>
<g class="tag"><rect x="90" y="22" width="34" height="18" rx="3"/><text x="94" y="34">VAND</text></g>
</g>
<text class="lbl hi" x="470" y="40">EXPOZITIE</text>
<text class="lbl" x="470" y="56">cele mai scumpe</text>
<rect class="slab" x="0" y="132" width="560" height="4"/>
<rect class="slab" x="0" y="180" width="560" height="4"/>
<rect class="slab" x="0" y="228" width="560" height="4"/>
<line class="stripe" x1="0" y1="131" x2="560" y2="131"/>
<line class="stripe" x1="0" y1="179" x2="560" y2="179"/>
<line class="stripe" x1="0" y1="227" x2="560" y2="227"/>
<rect class="lamp" x="40" y="96" width="60" height="3" rx="1"/>
<rect class="lamp l2" x="240" y="144" width="60" height="3" rx="1"/>
<rect class="lamp l3" x="420" y="192" width="60" height="3" rx="1"/>
<path class="car" d="M60 131 v-10 l12 -8 h34 l14 8 h12 v10 z"/><circle class="wheel" cx="80" cy="131" r="6"/><circle class="wheel" cx="118" cy="131" r="6"/>
<path class="car" d="M200 131 v-10 l12 -8 h34 l14 8 h12 v10 z"/><circle class="wheel" cx="220" cy="131" r="6"/><circle class="wheel" cx="258" cy="131" r="6"/>
<path class="car" d="M330 131 v-10 l12 -8 h34 l14 8 h12 v10 z"/><circle class="wheel" cx="350" cy="131" r="6"/><circle class="wheel" cx="388" cy="131" r="6"/>
<path class="car" d="M130 179 v-10 l12 -8 h34 l14 8 h12 v10 z"/><circle class="wheel" cx="150" cy="179" r="6"/><circle class="wheel" cx="188" cy="179" r="6"/>
<path class="car" d="M380 179 v-10 l12 -8 h34 l14 8 h12 v10 z"/><circle class="wheel" cx="400" cy="179" r="6"/><circle class="wheel" cx="438" cy="179" r="6"/>
<path class="car" d="M250 227 v-10 l12 -8 h34 l14 8 h12 v10 z"/><circle class="wheel" cx="270" cy="227" r="6"/><circle class="wheel" cx="308" cy="227" r="6"/>
<rect class="shaft" x="580" y="88" width="40" height="144"/>
<rect class="cab" x="586" y="94" width="28" height="36" rx="3"/>
<text class="lbl" x="476" y="124">ETAJ 1</text>
<text class="lbl" x="476" y="172">ETAJ 2</text>
<text class="lbl" x="476" y="220">ETAJ 3</text>
</svg>
</section>

<h2>Trei targuri</h2>
<p class="ta-lead">Fiecare targ primeste doar un anumit tip de vehicul. Le gasesti pe harta (<code>Telefon → Harti → Targ auto</code>). La fiecare te asteapta un vanzator: apropie-te si apasa <kbd>E</kbd>.</p>
<div class="ta-markets ta-gap">
<div class="ta-market main">
<svg viewBox="0 0 46 30" aria-hidden="true"><path d="M3 24v-7l7-6h22l9 6h2v7z" fill="#facc15"/><circle cx="12" cy="24" r="4" fill="#09090b" stroke="#facc15" stroke-width="2"/><circle cx="34" cy="24" r="4" fill="#09090b" stroke="#facc15" stroke-width="2"/></svg>
<h3>Vehicule</h3>
<span class="ta-who">Nea Marian</span>
<ul class="ta-facts">
<li><span>Primeste</span><span>masini si motociclete</span></li>
<li><span>Expozitie afara</span><span>10 locuri</span></li>
<li><span>Parcare subterana</span><span>3 etaje x 38 locuri</span></li>
</ul>
<span class="ta-path">Harti → Targ auto → Targ auto - Vehicule</span>
</div>
<div class="ta-market">
<svg viewBox="0 0 46 30" aria-hidden="true"><path d="M4 18h38l-6 9H10z" fill="#facc15"/><path d="M14 18V6l12 12z" fill="#a1a1aa"/></svg>
<h3>Ambarcatiuni</h3>
<span class="ta-who">Nea Vasile</span>
<ul class="ta-facts">
<li><span>Primeste</span><span>barci si submarine</span></li>
<li><span>Locuri</span><span>8</span></li>
</ul>
<span class="ta-path">Harti → Targ auto → Targ auto - Ambarcatiuni</span>
</div>
<div class="ta-market">
<svg viewBox="0 0 46 30" aria-hidden="true"><path d="M2 16h42l-4 4H6z" fill="#facc15"/><path d="M18 16 26 4h4l-4 12zM20 20l6 8h4l-4-8z" fill="#a1a1aa"/></svg>
<h3>Aeronave</h3>
<span class="ta-who">Nea Grigore</span>
<ul class="ta-facts">
<li><span>Primeste</span><span>elicoptere si avioane</span></li>
<li><span>Locuri</span><span>10</span></li>
</ul>
<span class="ta-path">Harti → Targ auto → Targ auto - Aeronave</span>
</div>
</div>

<h2>Expozitia si parcarea subterana</h2>
<div class="ta-floors">
<ul class="ta-stack">
<li class="expo"><b>Expozitie</b><span>afara, cele mai scumpe masini</span></li>
<li><b>Etaj 1</b><span>parcare subterana</span></li>
<li><b>Etaj 2</b><span>parcare subterana</span></li>
<li><b>Etaj 3</b><span>parcare subterana</span></li>
</ul>
<ul class="ta-notes">
<li>La targul de vehicule, masinile cele mai scumpe stau afara, la expozitie. Daca listezi una mai scumpa decat cea mai ieftina de afara, ii ia locul, iar cealalta coboara in parcare.</li>
<li>Restul masinilor stau in parcarea subterana. Ca sa ajungi la ele: <b>Nea Marian → Intra in parcare</b> si alegi etajul. Langa fiecare etaj vezi cate masini sunt.</li>
<li>In parcare intri doar pe jos. La intrarea din parcare apesi <kbd>E</kbd> ca sa schimbi etajul sau sa iesi afara.</li>
</ul>
</div>

<h2>Iti vinzi masina</h2>
<ol class="ta-steps">
<li><h3>Mergi la vanzatorul targului</h3><p>Trebuie sa fii langa el. Vehiculul nu trebuie sa fie la tine: il alegi din lista ta de vehicule.</p></li>
<li><h3>Vinde vehicul</h3><p>In meniu apesi <b>Vinde vehicul</b> si alegi vehiculul. In lista apar doar cele pe care le primeste targul.</p></li>
<li><h3>Completezi anuntul</h3><p>Pui pretul, cate zile sta la vanzare si, daca vrei, cateva cuvinte pentru cumparatori. Confirmi.</p></li>
<li><h3>Platesti parcarea</h3><p>Platesti pe loc taxa de parcare pentru toate zilele (din cash, apoi din banca). Vehiculul dispare din garaj si apare la targ.</p></li>
</ol>
<ul class="ta-form">
<li><h3>Pret de vanzare</h3><p>Intre pretul minim si maxim al targului. Formularul iti arata si cat la suta din pret se retine ca taxa la vanzare.</p></li>
<li><h3>Informatii aditionale</h3><p>Optional, maxim 100 de caractere. Le vede oricine se uita la masina.</p></li>
<li><h3>Nr. de zile in parc</h3><p>Minim o zi, maximul e scris in formular, la fel si pretul pe zi.</p></li>
<li><h3>Nr. telefon</h3><p>Se completeaza singur. Fara numar de telefon nu poti pune masina la vanzare.</p></li>
</ul>
<h3 class="ta-subhead">Ce nu poti vinde</h3>
<ul class="ta-check">
<li class="no">Vehicule de job sau de factiune.</li>
<li class="no">Vehicule VIP.</li>
<li class="no">Un vehicul confiscat sau ridicat de politie.</li>
<li class="no">Un vehicul in care sta cineva.</li>
<li class="no">Un tip de vehicul pe care targul nu il primeste (barca la Nea Marian, de exemplu).</li>
<li class="no">Nimic, cand targul e plin.</li>
</ul>

<h2>Cumperi o masina</h2>
<div class="ta-panel">
<div class="ta-screen">
<h3>Informatii vanzare</h3>
<ul class="ta-pills"><li>Pret vanzator</li><li>Pret de lista</li><li>Telefon vanzator</li><li>Parcat pana la</li><li>Note vanzator</li></ul>
<h3>Informatii generale</h3>
<ul class="ta-pills"><li>Categorie</li><li>Viteza maxima (stock si full tuning)</li><li>Portbagaj</li><li>Capacitate</li><li>Kilometraj</li></ul>
<h3>Tuning si piese</h3>
<ul class="ta-pills"><li>Motor</li><li>Frane</li><li>Transmisie</li><li>Suspensie</li><li>Blindaj</li><li>Modificari custom</li><li>Starea pieselor de motor</li><li>Km ramasi la piesele de service</li></ul>
</div>
<ul class="ta-keys">
<li><kbd>H</kbd><p><b>Cumpara</b>Confirmi si masina e a ta pe loc.</p></li>
<li><kbd>G</kbd><p><b>Suna</b>Il suni pe vanzator ca sa negociezi.</p></li>
<li><kbd>E</kbd><p><b>Scroll</b>Derulezi panoul. Iesi cu <kbd>ESC</kbd>.</p></li>
</ul>
</div>
<p class="ta-lead ta-gap">Panoul apare cand te apropii de o masina scoasa la vanzare. Platesti pretul cerut de vanzator (din cash, apoi din banca), iar vehiculul ajunge in garajul tau, cu cheile in inventar.</p>
<ul class="ta-check">
<li>Iti trebuie un loc liber in garaj (limita de vehicule personale).</li>
<li class="no">Nu iti poti cumpara propria masina.</li>
</ul>

<h2>Banii</h2>
<ul class="ta-money">
<li class="out"><h3>Vanzatorul plateste</h3><p>Taxa de parcare pe zi, pentru toate zilele, cand pune masina la vanzare. Nu se returneaza daca o retragi mai devreme.</p></li>
<li><h3>Vanzatorul primeste</h3><p>Pretul de vanzare minus taxa targului, direct in banca, chiar daca e offline. Daca e online, primeste si o notificare.</p></li>
<li class="out"><h3>Cumparatorul plateste</h3><p>Exact pretul din anunt, fara alte taxe.</p></li>
</ul>

<h2>Retragere si expirare</h2>
<ul class="ta-notes">
<li>Te razgandesti? La vanzatorul targului: <b>Scoate vehicul de la vanzare</b>. Vehiculul se intoarce in garajul tau.</li>
<li>Cand trec zilele platite, vehiculul se intoarce singur in garaj (verificarea se face la cateva minute).</li>
<li>Anuntul dispare si daca schimbi numarul de inmatriculare sau daca vehiculul trece la alt proprietar.</li>
<li>Masinile stau la targ si dupa restartul serverului.</li>
<li>La fiecare 25 de minute, tot serverul primeste o notificare cu cate vehicule sunt la vanzare in fiecare targ.</li>
</ul>

</div>
