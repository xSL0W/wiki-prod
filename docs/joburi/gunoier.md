---
outline: false
---

<style>
.gz {
  --ink: #0e1012;
  --asphalt: #181b1e;
  --curb: #262a2e;
  --line: #3a4046;
  --text: #e9ecee;
  --mute: #9aa3aa;
  --vest: #ff7a1a;
  --vest-soft: rgba(255, 122, 26, 0.14);
  max-width: 920px;
  margin: 0 auto;
  color: var(--text);
  font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.gz *, .gz *::before, .gz *::after { box-sizing: border-box; }
.gz p, .gz li { line-height: 1.6; color: var(--text); margin: 0; }
.gz ul { list-style: none; padding: 0; margin: 0; }

/* hero: the route is the picture */
.gz-hero {
  background: var(--ink);
  border: 1px solid var(--line);
  border-radius: 20px;
  padding: clamp(1.25rem, 4vw, 2.5rem);
  overflow: hidden;
}
.gz-hero h1 {
  margin: 0 0 0.6rem;
  border: 0;
  padding: 0;
  font-size: clamp(2rem, 6vw, 3.4rem);
  line-height: 1.05;
  font-weight: 800;
  letter-spacing: -0.03em;
  color: #fff;
}
.gz-hours { color: var(--vest); white-space: nowrap; }
.gz-hero p { max-width: 52ch; color: var(--mute); font-size: 1.05rem; }
.gz-route { display: block; width: 100%; height: auto; margin-top: 1.5rem; }
.gz-route .road { fill: none; stroke: var(--curb); stroke-width: 14; stroke-linecap: round; stroke-linejoin: round; }
.gz-route .trip {
  fill: none; stroke: var(--vest); stroke-width: 3; stroke-linecap: round; stroke-dasharray: 2 9;
}
.gz-route .drive {
  fill: none; stroke: var(--vest); stroke-width: 3.5; stroke-linecap: round; stroke-linejoin: round;
  stroke-dasharray: 1; stroke-dashoffset: 1;
  animation: gz-draw 2.6s cubic-bezier(.5, 0, .2, 1) 0.2s forwards;
}
.gz-route .stop { fill: var(--ink); stroke: var(--vest); stroke-width: 3; }
.gz-route .depot { fill: var(--vest); }
.gz-route text { fill: var(--mute); font-size: 13px; font-family: inherit; }
@keyframes gz-draw { to { stroke-dashoffset: 0; } }
@media (prefers-reduced-motion: reduce) {
  .gz-route .drive { animation: none; stroke-dashoffset: 0; }
}

/* facts strip */
.gz .gz-facts { display: flex; flex-wrap: wrap; gap: 0.6rem; margin: 1rem 0 0; }
.gz-facts li {
  background: var(--asphalt);
  border: 1px solid var(--line);
  border-radius: 999px;
  padding: 0.35rem 0.9rem;
  font-size: 0.92rem;
  color: var(--text);
}

/* sections */
.gz h2 {
  margin: 3rem 0 1rem;
  border: 0;
  padding: 0;
  font-size: 1.5rem;
  font-weight: 750;
  letter-spacing: -0.015em;
  color: #fff;
}

/* the shift as a route: pins on a line */
.gz-steps { position: relative; margin-left: 0.4rem; }
.gz-steps::before {
  content: ''; position: absolute; left: 11px; top: 8px; bottom: 8px; width: 2px;
  background: repeating-linear-gradient(to bottom, var(--line) 0 6px, transparent 6px 12px);
}
.gz-steps li { position: relative; padding: 0 0 1.35rem 3rem; }
.gz-steps li:last-child { padding-bottom: 0; }
.gz-steps li::before {
  content: ''; position: absolute; left: 3px; top: 3px; width: 18px; height: 18px;
  border-radius: 50%; background: var(--ink); border: 3px solid var(--vest);
}
.gz-steps li:last-child::before { background: var(--vest); }
.gz-steps b { color: #fff; font-weight: 650; }
.gz kbd {
  font: inherit; font-size: 0.85em; font-weight: 700; color: var(--ink); background: var(--vest);
  border-radius: 6px; padding: 0.05rem 0.45rem;
}

/* solo vs team */
.gz-modes { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1rem; }
.gz-mode { background: var(--asphalt); border: 1px solid var(--line); border-radius: 16px; padding: 1.25rem 1.4rem; }
.gz-mode.team { background: linear-gradient(160deg, var(--vest-soft), var(--asphalt) 60%); border-color: var(--vest); }
.gz-mode h3 { margin: 0 0 0.5rem; border: 0; padding: 0; font-size: 1.15rem; color: #fff; }
.gz-mode p { color: var(--mute); }
.gz-mode strong { color: #fff; }

/* tips: plain rows */
.gz-tips li { padding: 0.8rem 0; border-top: 1px solid var(--line); }
.gz-tips li:last-child { border-bottom: 1px solid var(--line); }
.gz-tips b { color: #fff; }

.gz a:focus-visible { outline: 3px solid var(--vest); outline-offset: 2px; }
/* block list: keeps the 8px row spacing the theme no longer adds to classed lists */
.gz .gz-steps > li + li, .gz .gz-tips > li + li { margin-top: 8px; }
</style>

<div class="gz">

<section class="gz-hero">
<h1>Gunoier <span class="gz-hours">- 30h</span></h1>
<p>Un camion, un oras si o ruta de strans gunoiul. Mergi singur sau cu un prieten, iar ruta se termina langa depozit.</p>
<svg class="gz-route" viewBox="0 0 640 200" role="img" aria-label="O ruta pornind de la depozit, cu mai multe opriri, care se intoarce la depozit">
<path class="road" pathLength="1" d="M60 150 C 110 40, 190 40, 240 80 S 330 150, 390 100 S 500 30, 560 70 S 560 160, 470 168 S 300 190, 200 172 S 100 160, 60 150"/>
<path class="trip" d="M60 150 C 110 40, 190 40, 240 80 S 330 150, 390 100 S 500 30, 560 70 S 560 160, 470 168 S 300 190, 200 172 S 100 160, 60 150"/>
<path class="drive" pathLength="1" d="M60 150 C 110 40, 190 40, 240 80 S 330 150, 390 100 S 500 30, 560 70 S 560 160, 470 168 S 300 190, 200 172 S 100 160, 60 150"/>
<circle class="stop" cx="150" cy="60" r="7"/>
<circle class="stop" cx="240" cy="80" r="7"/>
<circle class="stop" cx="330" cy="125" r="7"/>
<circle class="stop" cx="420" cy="85" r="7"/>
<circle class="stop" cx="520" cy="45" r="7"/>
<circle class="stop" cx="560" cy="110" r="7"/>
<circle class="stop" cx="400" cy="172" r="7"/>
<circle class="stop" cx="290" cy="182" r="7"/>
<circle class="stop" cx="170" cy="168" r="7"/>
<rect class="depot" x="46" y="136" width="28" height="28" rx="7"/>
<text x="84" y="190">depozit</text>
</svg>
<ul class="gz-facts">
<li>Se poate lucra singur sau in doi</li>
<li>Camionul este al jobului</li>
<li>Plata vine la finalul fiecarei rute</li>
</ul>
</section>

<h2>Cum incep?</h2>
<p>Angajeaza-te ca <b>Gunoier</b> la Primarie (<code>Telefon → Harti → Locatii importante → Primarie</code>). Ai nevoie de minim 30 de ore jucate. Apoi mergi la depozitul de salubritate si vorbeste cu seful de la salubritate.</p>

<h2>O tura, pe scurt</h2>
<ul class="gz-steps">
<li><b>Porneste tura</b> de la seful din depozit. Liderul primeste camionul de gunoi.</li>
<li><b>Urmeaza GPS-ul</b> pana la prima oprire. Opririle sunt langa tomberoane, in tot orasul.</li>
<li><b>Ridica sacii</b> de langa tomberon cu <kbd>E</kbd>. Cari cate un sac odata.</li>
<li><b>Arunca sacul</b> in spatele camionului cu <kbd>E</kbd>. Cand nu mai ramane niciun sac, GPS-ul te trimite mai departe.</li>
<li><b>Ultimele opriri te aduc inapoi spre depozit.</b> Dupa ultima primesti plata, iar ruta noua porneste singura.</li>
</ul>

<h2>Singur sau in echipa</h2>
<div class="gz-modes">
<div class="gz-mode">
<h3>Singur</h3>
<p>Conduci, strangi si arunci tu. Ritm linistit, plata intreaga pentru tine.</p>
</div>
<div class="gz-mode team">
<h3>Cu un prieten</h3>
<p>Formeaza echipa din <b>Meniu echipa</b>. Liderul porneste tura, amandoi strangeti saci, iar <strong>fiecare primeste plata intreaga</strong>. Rutele se termina mai repede si castigi mai mult.</p>
</div>
</div>

<h2>Sfaturi</h2>
<ul class="gz-tips">
<li><b>Nu lasa camionul departe.</b> Sacii se arunca doar in camionul tau, de aproape.</li>
<li><b>Fii atent la tomberoane.</b> Uneori te musca un sobolan, iar alteori gasesti o sticla de apa in sac.</li>
<li><b>Ia opririle in ordine,</b> asa cum le arata GPS-ul, ca sa nu pierzi timp.</li>
<li><b>Daca renunti la job,</b> camionul dispare si tura se opreste.</li>
</ul>
</div>
