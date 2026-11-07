---
outline: false
---

<style>
.pz {
  --pz-oven: #170f0c;
  --pz-brick: #241713;
  --pz-edge: #43291f;
  --pz-crust: #e0a052;
  --pz-cheese: #f7d97a;
  --pz-tomato: #e5482f;
  --pz-basil: #5fb36a;
  --pz-paper: #faf6ee;
  --pz-ink: #231a14;
  --pz-text: #f3e9df;
  --pz-mute: #c4ad9d;
  max-width: 920px;
  margin: 0 auto;
  color: var(--pz-text);
  font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.pz *, .pz *::before, .pz *::after { box-sizing: border-box; }
.pz p, .pz li { line-height: 1.6; color: var(--pz-text); margin: 0; }
.pz ul, .pz ol { list-style: none; padding: 0; margin: 0; }
.pz b { color: #fff; font-weight: 650; }
.pz code { white-space: normal; }

/* hero: the oven, with a pizza that is missing slices */
.pz-hero {
  display: grid;
  grid-template-columns: minmax(0, 1.25fr) minmax(0, 1fr);
  gap: clamp(1rem, 4vw, 2.5rem);
  align-items: center;
  padding: clamp(1.25rem, 4vw, 2.5rem);
  border-radius: 22px;
  border: 1px solid var(--pz-edge);
  background: radial-gradient(120% 90% at 85% 50%, rgba(229, 72, 47, 0.22), transparent 60%), var(--pz-oven);
  overflow: hidden;
}
@media (max-width: 640px) { .pz-hero { grid-template-columns: 1fr; } }
.pz-hero h1 {
  margin: 0 0 0.6rem;
  border: 0;
  padding: 0;
  font-size: clamp(2rem, 6.5vw, 3.3rem);
  line-height: 1.05;
  font-weight: 850;
  letter-spacing: -0.03em;
  color: #fff;
}
.pz-hrs { color: var(--pz-cheese); white-space: nowrap; }
.pz-hero p { color: var(--pz-mute); font-size: 1.05rem; max-width: 46ch; }
.pz .pz-chips { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1rem; }
.pz-chips li {
  padding: 0.3rem 0.8rem;
  border-radius: 999px;
  background: var(--pz-brick);
  border: 1px solid var(--pz-edge);
  font-size: 0.9rem;
}
.pz-pie { display: block; width: 100%; max-width: 300px; height: auto; margin: 0 auto; }
.pz-pie .crust { fill: var(--pz-crust); }
.pz-pie .sauce { fill: var(--pz-tomato); }
.pz-pie .cheese { fill: var(--pz-cheese); }
.pz-pie .cut { stroke: var(--pz-crust); stroke-width: 3; }
.pz-pie .pep { fill: #b8321f; }
.pz-pie .leaf { fill: var(--pz-basil); }
.pz-pie .slice { transform-origin: 150px 150px; animation: pz-serve 3.6s ease-in-out infinite; }
@keyframes pz-serve {
  0%, 20% { transform: translate(0, 0); opacity: 1; }
  55%, 70% { transform: translate(26px, -26px); opacity: 1; }
  85% { transform: translate(40px, -40px); opacity: 0; }
  100% { transform: translate(0, 0); opacity: 0; }
}
@media (prefers-reduced-motion: reduce) {
  .pz-pie .slice { animation: none; transform: translate(18px, -18px); }
}

/* sections */
.pz h2 {
  margin: 3rem 0 1rem;
  border: 0;
  padding: 0;
  font-size: 1.5rem;
  font-weight: 750;
  letter-spacing: -0.015em;
  color: #fff;
}
.pz-lead { max-width: 62ch; }
.pz kbd {
  font: inherit; font-size: 0.85em; font-weight: 800; color: var(--pz-ink); background: var(--pz-cheese);
  border-radius: 6px; padding: 0.05rem 0.45rem;
}

/* grades as two order tickets */
.pz-tickets { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.25rem; align-items: start; }
.pz-ticket {
  position: relative;
  background: var(--pz-paper);
  color: var(--pz-ink);
  padding: 1.1rem 1.2rem 1.6rem;
  font-family: ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace;
  border-radius: 4px 4px 0 0;
}
.pz-ticket::after {
  content: '';
  position: absolute; left: 0; right: 0; bottom: -10px; height: 10px;
  background:
    linear-gradient(135deg, var(--pz-paper) 50%, transparent 50%) 0 0 / 14px 10px repeat-x,
    linear-gradient(225deg, var(--pz-paper) 50%, transparent 50%) 0 0 / 14px 10px repeat-x;
}
.pz-ticket h3 {
  margin: 0 0 0.6rem;
  border: 0;
  padding: 0 0 0.6rem;
  border-bottom: 2px dashed #b9a99a;
  font: 800 1.1rem/1.2 ui-monospace, Menlo, Consolas, monospace;
  color: var(--pz-ink);
}
.pz-ticket h3 small { display: block; font-size: 0.72rem; letter-spacing: 0.14em; color: #7a6656; }
.pz-ticket li {
  display: flex; justify-content: space-between; gap: 0.75rem;
  padding: 0.3rem 0;
  font-size: 0.88rem;
  color: var(--pz-ink);
  border-bottom: 1px dotted #cdbfb1;
}
.pz-ticket li span:last-child { font-weight: 800; text-align: right; }
.pz-ticket.up { background: #fff3cf; }
.pz-ticket.up::after {
  background:
    linear-gradient(135deg, #fff3cf 50%, transparent 50%) 0 0 / 14px 10px repeat-x,
    linear-gradient(225deg, #fff3cf 50%, transparent 50%) 0 0 / 14px 10px repeat-x;
}
.pz .pz-note { margin-top: 1.6rem; color: var(--pz-mute); max-width: 62ch; }

/* the shift as a menu with numbered courses */
.pz-steps { counter-reset: pz; display: grid; gap: 0.75rem; }
.pz-steps li {
  counter-increment: pz;
  position: relative;
  display: grid;
  grid-template-columns: 3rem 1fr;
  gap: 0.9rem;
  align-items: start;
  padding: 1rem 1.1rem;
  border-radius: 14px;
  background: var(--pz-brick);
  border: 1px solid var(--pz-edge);
}
.pz-steps li::before {
  content: counter(pz);
  display: grid; place-items: center;
  width: 3rem; height: 3rem;
  border-radius: 50%;
  background: var(--pz-tomato);
  box-shadow: inset 0 0 0 4px var(--pz-crust);
  color: #fff;
  font-weight: 850;
  font-size: 1.15rem;
}
.pz-steps p { color: var(--pz-mute); }
.pz-steps strong { display: block; color: #fff; font-size: 1.05rem; margin-bottom: 0.15rem; }

/* tips */
.pz-tips { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 0.75rem; }
.pz-tips li { padding: 0.9rem 1rem; border-left: 4px solid var(--pz-basil); background: rgba(95, 179, 106, 0.08); border-radius: 0 12px 12px 0; }
.pz-tips li.warn { border-left-color: var(--pz-tomato); background: rgba(229, 72, 47, 0.1); }
.pz-tips p { color: var(--pz-mute); font-size: 0.95rem; }

.pz a:focus-visible { outline: 3px solid var(--pz-cheese); outline-offset: 2px; }
</style>

<div class="pz">

<section class="pz-hero">
<div>
<h1>Livrator pizza <span class="pz-hrs">- 0h/10h</span></h1>
<p>Iei cutiile calde de la pizzerie, sari pe scuter si le duci la clienti prin tot orasul. Cu timpul treci la gradul de expert si primesti si masina.</p>
<ul class="pz-chips">
<li>Job public, singur</li>
<li>Scuter, apoi masina</li>
<li>Plata la fiecare livrare</li>
</ul>
</div>
<svg class="pz-pie" viewBox="0 0 300 300" role="img" aria-label="O pizza din care o felie pleaca spre client">
<circle class="crust" cx="150" cy="150" r="128"/>
<circle class="sauce" cx="150" cy="150" r="112"/>
<circle class="cheese" cx="150" cy="150" r="104"/>
<line class="cut" x1="150" y1="46" x2="150" y2="254"/>
<line class="cut" x1="46" y1="150" x2="254" y2="150"/>
<line class="cut" x1="76" y1="76" x2="224" y2="224"/>
<line class="cut" x1="76" y1="224" x2="224" y2="76"/>
<circle class="pep" cx="110" cy="105" r="11"/>
<circle class="pep" cx="95" cy="170" r="11"/>
<circle class="pep" cx="150" cy="205" r="11"/>
<circle class="pep" cx="200" cy="185" r="11"/>
<circle class="pep" cx="128" cy="140" r="9"/>
<ellipse class="leaf" cx="175" cy="120" rx="10" ry="5" transform="rotate(-30 175 120)"/>
<ellipse class="leaf" cx="120" cy="200" rx="10" ry="5" transform="rotate(25 120 200)"/>
<g class="slice">
<path class="crust" d="M150 150 L150 22 A128 128 0 0 1 240.5 59.5 Z"/>
<path class="cheese" d="M150 150 L150 40 A110 110 0 0 1 227.8 72.2 Z"/>
<circle class="pep" cx="180" cy="80" r="10"/>
<ellipse class="leaf" cx="165" cy="112" rx="9" ry="4.5" transform="rotate(-50 165 112)"/>
</g>
</svg>
</section>

<h2>Cum incep?</h2>
<p class="pz-lead">Angajeaza-te ca <b>Livrator pizza</b> la Primarie (<code>Telefon → Harti → Locatii importante → Primarie</code>). Nu ai nevoie de ore jucate. Apoi mergi la pizzerie, in Vinewood, si vorbeste cu <b>seful pizzeriei</b>. Locul il gasesti si pe harta de la Primarie. Te poti angaja si direct de la el.</p>

<h2>Gradele jobului</h2>
<div class="pz-tickets">
<div class="pz-ticket">
<h3><small>BON 01</small>Livrator</h3>
<ul>
<li><span>Ore necesare</span><span>0h</span></li>
<li><span>Vehicul</span><span>Scuter</span></li>
<li><span>Comenzi pe tura</span><span>Putine</span></li>
</ul>
</div>
<div class="pz-ticket up">
<h3><small>BON 02</small>Livrator expert</h3>
<ul>
<li><span>Ore necesare</span><span>10h</span></li>
<li><span>Vehicul</span><span>Scuter sau masina</span></li>
<li><span>Comenzi pe tura</span><span>Mai multe</span></li>
<li><span>Plata pe livrare</span><span>Mai mare</span></li>
</ul>
</div>
</div>
<p class="pz-note">Promovarea e automata. Cand ai 10 ore jucate, deschide meniul sefului pizzeriei si urci singur la <b>Livrator expert</b>. Progresul il vezi la <b>Skill-uri si promovare</b>, in acelasi meniu. Daca te angajezi direct cu 10 ore, incepi de la gradul de expert.</p>

<h2>O tura, pe scurt</h2>
<ol class="pz-steps">
<li><div><strong>Porneste tura</strong><p>La seful pizzeriei alege <b>Incepe tura</b>. Primesti uniforma pe tine si cutiile de pizza direct in inventar, cate una pentru fiecare comanda. Ai grija sa ai loc in inventar.</p></div></li>
<li><div><strong>Ia un vehicul</strong><p>Garajul jobului e chiar langa pizzerie. Ca Livrator primesti scuterul, iar ca Livrator expert poti lua si masina.</p></div></li>
<li><div><strong>Urmeaza GPS-ul</strong><p>Pe harta apare <b>Urmatorul client</b>. Clientii sunt imprastiati prin tot orasul.</p></div></li>
<li><div><strong>Scoate pizza din vehicul</strong><p>Cand ai ajuns aproape de client, tine apasat <kbd>G</kbd> pe vehicul si alege <b>Scoate pizza din vehicul</b>. Daca te-ai grabit, o poti pune la loc cu <b>Pune pizza in vehicul</b>.</p></div></li>
<li><div><strong>Livreaza</strong><p>Mergi la client si apasa <kbd>E</kbd>. Plata intra in contul din banca dupa fiecare livrare, apoi primesti comanda urmatoare.</p></div></li>
<li><div><strong>Inapoi la pizzerie</strong><p>Dupa ultima comanda, GPS-ul te duce inapoi la pizzerie si tura se incheie singura. Poti porni oricand o tura noua.</p></div></li>
</ol>

<h2>Sfaturi</h2>
<ul class="pz-tips">
<li><p><b>Parcheaza aproape.</b> Pizza se scoate din vehicul doar langa client, iar vehiculul jobului trebuie sa ramana in apropiere cand livrezi.</p></li>
<li><p><b>Nu livra in fuga.</b> Intre doua livrari trebuie sa treaca un timp minim.</p></li>
<li><p><b>Uniforma vine singura.</b> O primesti la inceputul turei. Din meniul sefului o poti alege sau schimba.</p></li>
<li class="warn"><p><b>Nu lasa tura neterminata.</b> Daca termini tura de la sef, iesi de pe server sau renunti la job, cutiile ramase dispar.</p></li>
</ul>

</div>
