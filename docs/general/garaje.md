---
outline: deep
---

<style>
.grj {
  --ink: #0b0b0d;
  --panel: #17171a;
  --panel2: #1f1f23;
  --line: #2f2f36;
  --text: #f4f4f5;
  --mute: #a1a1aa;
  --red: #ef4444;
  --red-deep: #b91c1c;
  --red-soft: rgba(239, 68, 68, 0.14);
  --lamp: #fde68a;
  --green: #4ade80;
  max-width: 960px;
  margin: 0 auto;
  color: var(--text);
  font-family: Inter, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.grj *, .grj *::before, .grj *::after { box-sizing: border-box; }
.grj p, .grj li { line-height: 1.6; color: var(--text); margin: 0; }
.grj ul, .grj ol { list-style: none; padding: 0; margin: 0; }
.grj li + li { margin-top: 0; }
.grj b { color: #fff; font-weight: 650; }
.grj a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.grj a:hover { color: #fecaca; }
.grj a:focus-visible { outline: 3px solid var(--red); outline-offset: 3px; border-radius: 6px; }
.grj kbd {
  font: inherit; font-size: 0.85em; font-weight: 700; color: #fff; background: var(--red-deep);
  border-radius: 6px; padding: 0.05rem 0.45rem; white-space: nowrap;
}
.grj code { font-size: 0.88em; color: #fecaca; background: #26262b; border-radius: 6px; padding: 0.05rem 0.35rem; }
/* ---------- hero ---------- */
.grj .grj-hero {
  position: relative; overflow: hidden; isolation: isolate;
  background: radial-gradient(90% 120% at 100% 0%, rgba(253, 230, 138, 0.08), transparent 55%),
              radial-gradient(110% 120% at 0% 100%, rgba(185, 28, 28, 0.3), var(--ink) 62%);
  border: 1px solid var(--line); border-radius: 22px;
  padding: clamp(1.15rem, 4vw, 2.4rem);
}
.grj .grj-kicker { font-size: 0.78rem; font-weight: 700; letter-spacing: 0.16em; text-transform: uppercase; color: var(--red); margin-bottom: 0.55rem; }
.grj .grj-hero h1 {
  margin: 0 0 0.75rem; border: 0; padding: 0;
  font-size: clamp(2rem, 6.4vw, 3.4rem); line-height: 1.04; font-weight: 800; letter-spacing: -0.03em; color: #fff;
}
.grj .grj-hero h1 span { color: var(--red); }
.grj .grj-lede { max-width: 60ch; color: var(--mute); font-size: 1.05rem; }
/* garage scene */
.grj .grj-scene { display: block; width: 100%; height: auto; margin-top: 1.3rem; border-radius: 14px; }
.grj-scene .wall { fill: #121215; }
.grj-scene .brick { stroke: #1c1c21; stroke-width: 1; }
.grj-scene .frame { fill: #0c0c0e; stroke: #34343b; stroke-width: 2; }
.grj-scene .inside { fill: #070708; }
.grj-scene .floor { fill: #0d0d10; }
.grj-scene .sign { fill: var(--red-deep); }
.grj-scene .sign-t { fill: #fff; font: 800 13px Inter, system-ui, sans-serif; letter-spacing: 0.2em; }
.grj-scene .car { fill: #1d1d22; stroke: #3a3a42; stroke-width: 1.5; }
.grj-scene .glass { fill: #0f1116; stroke: #3a3a42; stroke-width: 1; }
.grj-scene .tyre { fill: #050506; stroke: #2a2a30; stroke-width: 2; }
.grj-scene .grille { fill: #0a0a0c; }
.grj-scene .lamp { fill: var(--lamp); }
.grj-scene .tail { fill: var(--red); }
.grj-scene .beam { fill: url(#grj-beam); }
.grj-scene .slat { fill: #26262c; stroke: #17171b; stroke-width: 1; }
.grj-scene .handle { fill: #4a4a52; }
.grj-scene .slot { fill: none; stroke: #2c2c33; stroke-width: 2; }
.grj-scene .slot-on { fill: none; stroke: var(--green); stroke-width: 2; opacity: 0.12; }
.grj-scene .lamp-glow { fill: var(--lamp); opacity: 0; }
/* door rolls up, lights come on, door closes again */
.grj-scene .door { animation: grj-door 12s cubic-bezier(.55, .05, .35, 1) infinite; }
.grj-scene .lamps { opacity: 0.15; animation: grj-lamps 12s linear infinite; }
.grj-scene .beam { opacity: 0; animation: grj-beam 12s linear infinite; }
.grj-scene .lamp-glow { animation: grj-glow 12s linear infinite; }
@keyframes grj-door { 0%, 8% { transform: translateY(0); } 30%, 78% { transform: translateY(-150px); } 96%, 100% { transform: translateY(0); } }
@keyframes grj-lamps { 0%, 30% { opacity: 0.15; } 33% { opacity: 1; } 35% { opacity: 0.4; } 37%, 76% { opacity: 1; } 82%, 100% { opacity: 0.15; } }
@keyframes grj-beam { 0%, 34% { opacity: 0; } 40%, 74% { opacity: 1; } 80%, 100% { opacity: 0; } }
@keyframes grj-glow { 0%, 34% { opacity: 0; } 40%, 74% { opacity: 0.35; } 80%, 100% { opacity: 0; } }
.grj-scene .slot-on { animation: grj-slot 12s linear infinite; }
.grj-scene .slot-on:nth-of-type(1) { animation-delay: 0.5s; }
.grj-scene .slot-on:nth-of-type(2) { animation-delay: 0.8s; }
.grj-scene .slot-on:nth-of-type(3) { animation-delay: 1.1s; }
.grj-scene .slot-on:nth-of-type(4) { animation-delay: 1.4s; }
.grj-scene .slot-on:nth-of-type(5) { animation-delay: 1.7s; }
.grj-scene .slot-on:nth-of-type(6) { animation-delay: 2s; }
@keyframes grj-slot { 0%, 30% { opacity: 0.12; } 36%, 70% { opacity: 0.95; } 80%, 100% { opacity: 0.12; } }
/* hero stats */
.grj .grj-stats { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 0.6rem; margin-top: 1.2rem; }
.grj .grj-stats li { background: rgba(23, 23, 26, 0.85); border: 1px solid var(--line); border-radius: 14px; padding: 0.7rem 0.9rem; }
.grj .grj-stats b { display: block; font-size: clamp(1.35rem, 4vw, 1.8rem); line-height: 1.1; font-weight: 800; color: #fff; font-variant-numeric: tabular-nums; }
.grj .grj-stats span { display: block; color: var(--mute); font-size: 0.82rem; line-height: 1.35; margin-top: 0.2rem; }
@media (max-width: 520px) { .grj .grj-stats { grid-template-columns: minmax(0, 1fr); } }
@media (prefers-reduced-motion: reduce) {
  .grj .grj-scene .door, .grj .grj-scene .lamps, .grj .grj-scene .beam, .grj .grj-scene .lamp-glow, .grj .grj-scene .slot-on { animation: none; }
  .grj .grj-scene .door { transform: translateY(-150px); }
  .grj .grj-scene .lamps { opacity: 1; }
  .grj .grj-scene .beam { opacity: 1; }
  .grj .grj-scene .lamp-glow { opacity: 0.35; }
  .grj .grj-scene .slot-on { opacity: 0.95; }
}
/* ---------- sections ---------- */
.grj .grj-h2 {
  display: flex; align-items: center; gap: 0.65rem;
  margin: 3rem 0 0.9rem; border: 0; padding: 0;
  font-size: 1.5rem; font-weight: 750; letter-spacing: -0.015em; line-height: 1.25; color: #fff;
}
.grj .grj-h2::before {
  content: ''; flex: none; width: 0.6rem; height: 0.6rem; border-radius: 2px; background: var(--red);
  transform: rotate(45deg); box-shadow: 0 0 0 4px var(--red-soft);
}
.grj .grj-h3 { margin: 0 0 0.35rem; border: 0; padding: 0; font-size: 1.05rem; font-weight: 700; color: #fff; line-height: 1.3; }
.grj .grj-sub { color: var(--mute); max-width: 68ch; margin-bottom: 1rem; }
.grj .grj-card { background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 1.1rem 1.25rem; }
.grj .grj-card p { color: var(--mute); font-size: 0.96rem; }
.grj .grj-card p + p { margin-top: 0.5rem; }
.grj .grj-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 250px), 1fr)); gap: 0.75rem; }
/* steps */
.grj .grj-steps { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 200px), 1fr)); gap: 0.75rem; counter-reset: grj-step; }
.grj .grj-steps li {
  position: relative; counter-increment: grj-step;
  background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 2.6rem 1.15rem 1.05rem;
}
.grj .grj-steps li::before {
  content: counter(grj-step); position: absolute; top: 0.9rem; left: 1.15rem;
  width: 1.5rem; height: 1.5rem; border-radius: 50%; display: grid; place-items: center;
  font-size: 0.8rem; font-weight: 800; color: #fff; background: var(--red-deep);
}
.grj .grj-steps p { color: var(--mute); font-size: 0.95rem; }
/* garage types */
.grj .grj-type { position: relative; padding-top: 1.05rem; border-top: 3px solid var(--c, var(--red)); }
.grj .grj-type .grj-tag {
  display: inline-block; margin-bottom: 0.45rem; font-size: 0.7rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: var(--c, var(--red));
}
.grj .grj-type.v { --c: #4ade80; }
.grj .grj-type.a { --c: #22d3ee; }
.grj .grj-type.b { --c: #60a5fa; }
.grj .grj-type.u { --c: #fb923c; }
.grj .grj-type.j { --c: #facc15; }
.grj .grj-type.f { --c: #c084fc; }
/* bullet list */
.grj .grj-list li { position: relative; padding-left: 1.2rem; color: var(--mute); font-size: 0.96rem; }
.grj .grj-list li + li { margin-top: 0.45rem; }
.grj .grj-list li::before { content: ''; position: absolute; left: 0.1rem; top: 0.62em; width: 0.42rem; height: 0.42rem; border-radius: 50%; background: var(--red); }
.grj .grj-list b { color: var(--text); }
/* kept-state chips */
.grj .grj-chips { display: flex; flex-wrap: wrap; gap: 0.45rem; margin-top: 0.8rem; }
.grj .grj-chips li { font-size: 0.83rem; font-weight: 650; color: var(--text); background: var(--panel2); border: 1px solid var(--line); border-radius: 999px; padding: 0.25rem 0.75rem; }
/* note */
.grj .grj-note {
  margin-top: 0.9rem; background: linear-gradient(160deg, var(--red-soft), var(--panel) 65%);
  border: 1px solid #4a2323; border-radius: 16px; padding: 0.95rem 1.2rem; color: var(--mute); font-size: 0.95rem;
}
.grj .grj-note b { color: #fff; }
</style>

<div class="grj">
<section class="grj-hero" aria-labelledby="grj-title">
<p class="grj-kicker">Sisteme generale</p>
<h1 id="grj-title">Garaje<span>.</span></h1>
<p class="grj-lede">Aici stau vehiculele tale cand nu le conduci. Parchezi, scoti, iti vezi starea masinii si, daca ai ramas fara loc, iti cumperi sloturi in plus.</p>
<svg class="grj-scene" viewBox="0 0 640 260" role="img" aria-label="O usa de garaj se ridica, farurile masinii din interior se aprind, iar locurile de parcare din fata se lumineaza">
<defs>
<linearGradient id="grj-beam" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#fde68a" stop-opacity="0.45"/>
<stop offset="1" stop-color="#fde68a" stop-opacity="0"/>
</linearGradient>
<clipPath id="grj-opening"><rect x="190" y="60" width="260" height="150"/></clipPath>
</defs>
<rect class="wall" x="0" y="0" width="640" height="260"/>
<g class="brick">
<line x1="0" y1="30" x2="640" y2="30"/><line x1="0" y1="60" x2="190" y2="60"/><line x1="450" y1="60" x2="640" y2="60"/>
<line x1="0" y1="90" x2="190" y2="90"/><line x1="450" y1="90" x2="640" y2="90"/><line x1="0" y1="120" x2="190" y2="120"/>
<line x1="450" y1="120" x2="640" y2="120"/><line x1="0" y1="150" x2="190" y2="150"/><line x1="450" y1="150" x2="640" y2="150"/>
<line x1="0" y1="180" x2="190" y2="180"/><line x1="450" y1="180" x2="640" y2="180"/>
</g>
<rect class="sign" x="250" y="14" width="140" height="30" rx="6"/>
<text class="sign-t" x="320" y="34" text-anchor="middle">GARAJ</text>
<rect class="frame" x="184" y="54" width="272" height="160" rx="4"/>
<rect class="inside" x="190" y="60" width="260" height="150"/>
<g clip-path="url(#grj-opening)">
<ellipse class="lamp-glow" cx="320" cy="160" rx="120" ry="40"/>
<rect class="car" x="232" y="110" width="176" height="74" rx="18"/>
<path class="glass" d="M262 112 L280 84 L360 84 L378 112 Z"/>
<rect class="grille" x="292" y="150" width="56" height="14" rx="4"/>
<g class="lamps">
<rect class="lamp" x="244" y="140" width="34" height="12" rx="5"/>
<rect class="lamp" x="362" y="140" width="34" height="12" rx="5"/>
</g>
<rect class="tyre" x="240" y="178" width="30" height="22" rx="5"/>
<rect class="tyre" x="370" y="178" width="30" height="22" rx="5"/>
<g class="door">
<rect class="slat" x="190" y="60" width="260" height="15"/><rect class="slat" x="190" y="75" width="260" height="15"/>
<rect class="slat" x="190" y="90" width="260" height="15"/><rect class="slat" x="190" y="105" width="260" height="15"/>
<rect class="slat" x="190" y="120" width="260" height="15"/><rect class="slat" x="190" y="135" width="260" height="15"/>
<rect class="slat" x="190" y="150" width="260" height="15"/><rect class="slat" x="190" y="165" width="260" height="15"/>
<rect class="slat" x="190" y="180" width="260" height="15"/><rect class="slat" x="190" y="195" width="260" height="15"/>
<rect class="handle" x="300" y="200" width="40" height="5" rx="2"/>
</g>
</g>
<rect class="floor" x="0" y="214" width="640" height="46"/>
<path class="beam" d="M244 214 L278 214 L250 260 L170 260 Z"/>
<path class="beam" d="M362 214 L396 214 L470 260 L390 260 Z"/>
<rect class="slot" x="18" y="222" width="46" height="30" rx="3"/>
<rect class="slot" x="74" y="222" width="46" height="30" rx="3"/>
<rect class="slot" x="130" y="222" width="46" height="30" rx="3"/>
<rect class="slot" x="464" y="222" width="46" height="30" rx="3"/>
<rect class="slot" x="520" y="222" width="46" height="30" rx="3"/>
<rect class="slot" x="576" y="222" width="46" height="30" rx="3"/>
<g>
<rect class="slot-on" x="18" y="222" width="46" height="30" rx="3"/>
<rect class="slot-on" x="74" y="222" width="46" height="30" rx="3"/>
<rect class="slot-on" x="130" y="222" width="46" height="30" rx="3"/>
<rect class="slot-on" x="464" y="222" width="46" height="30" rx="3"/>
<rect class="slot-on" x="520" y="222" width="46" height="30" rx="3"/>
<rect class="slot-on" x="576" y="222" width="46" height="30" rx="3"/>
</g>
</svg>
<ul class="grj-stats">
<li><b>12</b><span>sloturi pentru vehicule personale, de la inceput</span></li>
<li><b>4</b><span>feluri de garaj personal: vehicule, aeronave, barci, utilitare</span></li>
<li><b><kbd>E</kbd></b><span>la punctul de parcare sau de intrare in garaj</span></li>
</ul>
</section>

<h2 class="grj-h2" id="cum-folosesti-garajul">Cum folosesti garajul</h2>
<p class="grj-sub">Garajele apar pe harta cu blip. Fiecare are doua puncte: unul unde parchezi si unul unde intri ca sa scoti un vehicul.</p>
<ol class="grj-steps">
<li><h3 class="grj-h3">Parchezi</h3><p>Intra cu vehiculul pe punctul <b>Parcheaza in garaj</b> si apasa <kbd>E</kbd>. Toti cei din masina coboara, iar vehiculul intra in garaj.</p></li>
<li><h3 class="grj-h3">Intri in garaj</h3><p>Pe jos, mergi la punctul <b>Intra in garaj</b> si apasa <kbd>E</kbd>. Se deschide lista cu vehiculele tale parcate.</p></li>
<li><h3 class="grj-h3">Alegi vehiculul</h3><p>Cauti dupa nume sau numar, filtrezi pe categorii, vezi starea lui si apesi <b>Scoate din garaj</b>.</p></li>
<li><h3 class="grj-h3">Pleci</h3><p>Vehiculul apare pe un loc liber din parcare, <b>descuiat</b>. Incuie-l cu <kbd>L</kbd>, motorul il pornesti cu <kbd>X</kbd>.</p></li>
</ol>
<div class="grj-grid" style="margin-top:0.75rem">
<div class="grj-card"><h3 class="grj-h3">Un singur garaj, peste tot</h3><p>Garajele personale nu tin masina unde ai lasat-o. Orice garaj personal de tipul potrivit iti arata toate vehiculele tale parcate de acel tip.</p></div>
<div class="grj-card"><h3 class="grj-h3">Garaje cu interior</h3><p>Unele garaje de masini au un hangar in care te plimbi printre masinile tale. Te urci in cea dorita si apesi <kbd>W</kbd> ca sa iesi cu ea. Daca stai mai mult de 5 minute inauntru, esti scos afara.</p></div>
<div class="grj-card"><h3 class="grj-h3">Favorite</h3><p>Marcheaza cu steluta vehiculele pe care le folosesti des. Le gasesti in categoria <b>Favorite</b> din lista.</p></div>
</div>

<h2 class="grj-h2" id="tipuri-de-garaje">Tipuri de garaje</h2>
<div class="grj-grid">
<div class="grj-card grj-type v"><span class="grj-tag">Personal</span><h3 class="grj-h3">Vehicule</h3><p>Masini, motociclete si biciclete. Sunt cele mai multe garaje din oras.</p></div>
<div class="grj-card grj-type a"><span class="grj-tag">Personal</span><h3 class="grj-h3">Aeronave</h3><p>Avioane si elicoptere. Le gasesti la aeroporturi, pe acoperisuri si langa unele case.</p></div>
<div class="grj-card grj-type b"><span class="grj-tag">Personal</span><h3 class="grj-h3">Barci</h3><p>Garaje la apa, pentru barcile tale.</p></div>
<div class="grj-card grj-type u"><span class="grj-tag">Personal</span><h3 class="grj-h3">Utilitare</h3><p>Dube si vehicule de lucru, plus vehiculele premium.</p></div>
<div class="grj-card grj-type j"><span class="grj-tag">Job</span><h3 class="grj-h3">Garaje de job</h3><p>Politie, mecanici, taxi, livrator de pizza. Vezi doar vehiculele permise pentru gradul tau si primesti o cheie temporara.</p></div>
<div class="grj-card grj-type f"><span class="grj-tag">Factiune</span><h3 class="grj-h3">Garaje de factiune</h3><p>Medici (masini, elicoptere, barci) si EG Business Center. Vehiculele de job sau factiune se parcheaza doar in garajul lor.</p></div>
</div>
<p class="grj-note"><b>Cayo Perico:</b> vehiculele cumparate pentru insula stau doar in garajele de pe insula si nu apar in garajele din oras.</p>

<h2 class="grj-h2" id="sloturi">Sloturi</h2>
<div class="grj-grid">
<div class="grj-card">
<h3 class="grj-h3">Ce ocupa un slot</h3>
<ul class="grj-list">
<li>Ai <b>12 sloturi</b> la inceput, pentru toate vehiculele personale: masini, motociclete, aeronave, barci.</li>
<li>Vehiculele <b>VIP</b> nu ocupa slot. Le vezi in garaj doar cat timp ai VIP-ul cerut.</li>
<li>Vehiculele de job si de factiune nu ocupa slot.</li>
</ul>
</div>
<div class="grj-card">
<h3 class="grj-h3">Cand ai sloturile pline</h3>
<ul class="grj-list">
<li>Nu mai poti cumpara vehicule de la dealer sau din <a href="/general/parcauto">Targul Auto</a>.</li>
<li>Nu poti primi un vehicul prin contract de vanzare.</li>
<li>Sloturi in plus iei din <a href="/zona-info/store">magazinul EG</a> (<code>/store</code>) si, uneori, din magazinele de eveniment.</li>
</ul>
</div>
</div>

<h2 class="grj-h2" id="starea-vehiculului">Ce se pastreaza</h2>
<div class="grj-card">
<p>Cand parchezi, garajul retine starea vehiculului. Il scoti exact cum l-ai lasat.</p>
<ul class="grj-chips">
<li>Combustibil</li><li>Motor</li><li>Caroserie</li><li>Tuning</li><li>Kilometraj</li>
</ul>
<p style="margin-top:0.8rem">In lista din garaj vezi si starea pieselor (motor, frane, suspensie, transmisie), blindajul, viteza maxima, plus engine swap sau turbo, daca ai.</p>
<p>Un vehicul scos care dispare din oras (sters sau la restart) se intoarce singur in garaj.</p>
</div>

<h2 class="grj-h2" id="chei">Chei si telefon</h2>
<div class="grj-grid">
<div class="grj-card"><h3 class="grj-h3">Cheia masinii</h3><p>Cheia e un item in inventar (<b><img class="eg-item" src="/items/vehiclekey.webp" alt="">Vehicle Keys</b>). Pune-le pe toate in <b><img class="eg-item" src="/items/keybag.webp" alt="">Key Bag</b>, ca sa nu-ti umple inventarul.</p><p>Ti-ai pierdut cheia? Urca in masina ta si foloseste o <b><img class="eg-item" src="/items/clonekeystool.webp" alt="">Trusa de clonat cheile unei masini</b>, din magazinele 24/7. Merge doar pe masinile tale.</p></div>
<div class="grj-card"><h3 class="grj-h3">Telefon → Garaj</h3><p>Vezi ce vehicule ai si care sunt scoase. Pentru cele scoase pui destinatia pe harta. Pe cele din apropiere le incui sau descui din aplicatie.</p></div>
<div class="grj-card"><h3 class="grj-h3"><kbd>K</kbd> → Vehicul</h3><p><b>Localizeaza-ti masinile</b> pune pe harta pozitia vehiculelor scoase. <b>Tracteaza vehicule distruse</b> aduce in garaj, contra cost, un vehicul distrus lasat afara.</p><p>Nu poti tracta daca alt jucator e la mai putin de 50 m de vehicul.</p></div>
</div>

<h2 class="grj-h2" id="vehicul-blocat">Vehicul blocat</h2>
<p class="grj-sub">Un vehicul blocat apare in garaj cu lacat si nu il poti scoate pana nu rezolvi motivul.</p>
<div class="grj-grid">
<div class="grj-card"><h3 class="grj-h3">Ridicat la Impound</h3><p>Politia poate cere ridicarea unui vehicul, iar un mecanic il duce la Impound.</p><p>Il recuperezi de la omul de la <b>Impound</b> (blip pe harta): <b>Recuperare vehicule</b>, platesti taxa si vehiculul se intoarce in garaj. Taxa depinde de valoarea vehiculului.</p></div>
<div class="grj-card"><h3 class="grj-h3">Scos la vanzare</h3><p>Cat timp vehiculul e pus la vanzare in <a href="/general/parcauto">Targul Auto</a>, ramane blocat in garaj. Se deblocheaza daca il retragi de la vanzare.</p></div>
<div class="grj-card"><h3 class="grj-h3">Poprire</h3><p>Daca nu ai bani pentru impozitul pe vehicule la payday, primesti poprire si nu mai intri in garajul personal sau de factiune.</p><p>Platesti din <kbd>K</kbd> → <b>Jucator</b> → <b>Plateste taxe</b> sau cu <code>/paytaxes</code>.</p></div>
</div>

<h2 class="grj-h2" id="vanzare">Vanzarea unui vehicul</h2>
<div class="grj-card">
<ul class="grj-list">
<li><b>Catre un jucator:</b> mergi la <b>Notar</b> (Birou notarial) → <b>Vanzare vehicul</b>. Cumparatorul trebuie sa fie langa tine si sa aiba un slot liber. Vehiculele VIP nu se pot vinde asa.</li>
<li><b>La targ:</b> il pui la vanzare in <a href="/general/parcauto">Targul Auto</a> si il cumpara cine vrea.</li>
</ul>
</div>
</div>
