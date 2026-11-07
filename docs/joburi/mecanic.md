---
outline: false
---

<style>
.mc {
  --mc-bezel: #121417;
  --mc-shell: #1a1d21;
  --mc-screen: #0b1310;
  --mc-line: #2c3238;
  --mc-text: #e4e8ea;
  --mc-mute: #98a3aa;
  --mc-ok: #3ddc84;
  --mc-amber: #ffb340;
  --mc-red: #ef4b4b;
  --mc-mono: ui-monospace, 'SFMono-Regular', Menlo, Consolas, 'Liberation Mono', monospace;
  max-width: 920px;
  margin: 0 auto;
  color: var(--mc-text);
  font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.mc *, .mc *::before, .mc *::after { box-sizing: border-box; }
.mc p, .mc li { line-height: 1.6; color: var(--mc-text); margin: 0; }
.mc ul, .mc ol { list-style: none; padding: 0; margin: 0; }
.mc b { color: #fff; font-weight: 650; }
.mc code { white-space: normal; }

/* hero: a rugged OBD tablet */
.mc-tablet {
  padding: clamp(0.6rem, 2vw, 1rem);
  border-radius: 26px;
  background: linear-gradient(150deg, #23272c, var(--mc-bezel) 60%);
  border: 1px solid var(--mc-line);
  box-shadow: inset 0 0 0 3px #0c0e10;
}
.mc-screen {
  border-radius: 16px;
  background:
    repeating-linear-gradient(0deg, rgba(255, 255, 255, 0.018) 0 2px, transparent 2px 4px),
    radial-gradient(120% 100% at 80% 0%, rgba(61, 220, 132, 0.1), transparent 55%),
    var(--mc-screen);
  border: 1px solid #1d2a23;
  padding: clamp(1rem, 4vw, 2rem);
  overflow: hidden;
}
.mc-bar {
  display: flex; flex-wrap: wrap; justify-content: space-between; gap: 0.5rem 1rem;
  padding-bottom: 0.8rem;
  margin-bottom: 1.2rem;
  border-bottom: 1px solid #1f2d26;
  font: 600 0.75rem/1.3 var(--mc-mono);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--mc-mute);
}
.mc-leds { display: flex; flex-wrap: wrap; gap: 0.9rem; }
.mc-leds span::before {
  content: '';
  display: inline-block;
  width: 8px; height: 8px;
  margin-right: 0.4rem;
  border-radius: 50%;
  background: var(--mc-ok);
  box-shadow: 0 0 8px var(--mc-ok);
  vertical-align: 1px;
}
.mc-leds span.amber::before { background: var(--mc-amber); box-shadow: 0 0 8px var(--mc-amber); }
.mc-hero-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.3fr) minmax(0, 1fr);
  gap: clamp(1rem, 4vw, 2rem);
  align-items: center;
}
@media (max-width: 640px) { .mc-hero-grid { grid-template-columns: 1fr; } }
.mc-hero h1 {
  margin: 0 0 0.6rem;
  border: 0;
  padding: 0;
  font-size: clamp(2rem, 6.5vw, 3.3rem);
  line-height: 1.05;
  font-weight: 800;
  letter-spacing: -0.03em;
  color: #fff;
}
.mc-hrs {
  font-family: var(--mc-mono);
  font-size: 0.6em;
  color: var(--mc-ok);
  letter-spacing: 0;
}
.mc-hero p { color: var(--mc-mute); font-size: 1.05rem; max-width: 46ch; }
.mc-gauge { display: block; width: 100%; max-width: 260px; height: auto; margin: 0 auto; }
.mc-gauge .ring { fill: none; stroke: #1f2d26; stroke-width: 14; stroke-linecap: round; }
.mc-gauge .load {
  fill: none; stroke: var(--mc-ok); stroke-width: 14; stroke-linecap: round;
  stroke-dasharray: 1; stroke-dashoffset: 1;
  animation: mc-load 2.4s cubic-bezier(.4, 0, .2, 1) 0.2s forwards;
}
.mc-gauge .red { fill: none; stroke: var(--mc-red); stroke-width: 14; }
.mc-gauge .tick { stroke: #4a5a52; stroke-width: 2; }
.mc-gauge .needle { stroke: #fff; stroke-width: 3; stroke-linecap: round; transform-origin: 120px 120px; transform: rotate(-120deg); animation: mc-needle 2.4s cubic-bezier(.4, 0, .2, 1) 0.2s forwards; }
.mc-gauge .hub { fill: #fff; }
.mc-gauge text { fill: var(--mc-mute); font: 600 12px var(--mc-mono); letter-spacing: 0.1em; }
.mc-gauge .big { fill: #fff; font-size: 26px; letter-spacing: 0; }
@keyframes mc-load { to { stroke-dashoffset: 0.32; } }
@keyframes mc-needle { to { transform: rotate(42deg); } }
@media (prefers-reduced-motion: reduce) {
  .mc-gauge .load { animation: none; stroke-dashoffset: 0.32; }
  .mc-gauge .needle { animation: none; transform: rotate(42deg); }
}

/* sections */
.mc h2 {
  margin: 3rem 0 1rem;
  border: 0;
  padding: 0;
  font-size: 1.5rem;
  font-weight: 750;
  letter-spacing: -0.015em;
  color: #fff;
}
.mc h2 small {
  display: block;
  margin-bottom: 0.25rem;
  font: 600 0.72rem/1 var(--mc-mono);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--mc-ok);
}
.mc .mc-lead { max-width: 64ch; color: var(--mc-mute); }
.mc kbd {
  font: 700 0.82em/1 var(--mc-mono); color: #0b1310; background: var(--mc-ok);
  border-radius: 5px; padding: 0.12rem 0.4rem;
}

/* hiring as a boot sequence */
.mc-boot {
  background: var(--mc-screen);
  border: 1px solid #1f2d26;
  border-radius: 14px;
  padding: 1rem 1.1rem;
  font-family: var(--mc-mono);
  font-size: 0.92rem;
}
.mc-boot li {
  display: grid;
  grid-template-columns: 3.4rem 1fr;
  gap: 0.6rem;
  padding: 0.45rem 0;
  border-bottom: 1px dashed #1f2d26;
}
/* .mc ol resets padding/margin with higher specificity: restore the screen's padding and its gap under the lead */
.mc .mc-boot { padding: 1rem 1.1rem; margin-top: 1rem; }
.mc-boot li:last-child { border-bottom: 0; }
.mc-boot li > span { color: var(--mc-ok); font-weight: 700; }
.mc-boot li.wait > span { color: var(--mc-amber); }
.mc-boot p { color: var(--mc-text); font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif; font-size: 0.98rem; }

/* tools as tablet tiles */
.mc-tiles { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); grid-auto-flow: dense; gap: 0.9rem; }
.mc-tile {
  background: var(--mc-shell);
  border: 1px solid var(--mc-line);
  border-radius: 14px;
  padding: 1.05rem 1.15rem 1.15rem;
}
.mc-tile h3 {
  display: flex; align-items: center; gap: 0.6rem;
  margin: 0 0 0.45rem;
  border: 0;
  padding: 0;
  font-size: 1.08rem;
  color: #fff;
}
.mc-tile h3 span {
  font: 700 0.68rem/1 var(--mc-mono);
  letter-spacing: 0.08em;
  padding: 0.25rem 0.4rem;
  border-radius: 5px;
  color: var(--mc-ok);
  border: 1px solid rgba(61, 220, 132, 0.4);
}
.mc-tile p { color: var(--mc-mute); font-size: 0.95rem; }
.mc-tile.wide { grid-column: 1 / -1; }
.mc-parts { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 0.4rem 1.2rem; margin-top: 0.6rem; }
.mc-parts p b { color: var(--mc-amber); }

/* pay sources */
.mc-pay { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 0.6rem; }
.mc-pay li {
  padding: 0.8rem 1rem;
  border-radius: 12px;
  background: linear-gradient(160deg, rgba(61, 220, 132, 0.09), transparent 70%), var(--mc-shell);
  border: 1px solid var(--mc-line);
  color: var(--mc-mute);
  font-size: 0.95rem;
}

/* tips as fault codes */
.mc-codes li {
  display: grid;
  grid-template-columns: 5.5rem 1fr;
  gap: 0.9rem;
  align-items: start;
  padding: 0.85rem 0;
  border-top: 1px solid var(--mc-line);
}
.mc-codes li:last-child { border-bottom: 1px solid var(--mc-line); }
.mc-sev {
  font: 700 0.72rem/1 var(--mc-mono);
  letter-spacing: 0.1em;
  text-align: center;
  padding: 0.4rem 0;
  border-radius: 6px;
  color: #0b1310;
  background: var(--mc-mute);
}
.mc-sev.crit { background: var(--mc-red); color: #fff; }
.mc-sev.urg { background: var(--mc-amber); }
.mc-codes p { color: var(--mc-mute); }
@media (max-width: 420px) { .mc-codes li { grid-template-columns: 1fr; gap: 0.4rem; } .mc-sev { justify-self: start; padding: 0.35rem 0.6rem; } }

.mc a:focus-visible { outline: 3px solid var(--mc-ok); outline-offset: 2px; }
/* block list: keeps the 8px row spacing the theme no longer adds to classed lists */
.mc .mc-boot > li + li, .mc .mc-codes > li + li { margin-top: 8px; }
</style>

<div class="mc">

<section class="mc-hero mc-tablet">
<div class="mc-screen">
<div class="mc-bar"><span>Diagnoza vehicul</span><div class="mc-leds"><span>Conectat</span><span>In tura</span><span class="amber">Service</span></div></div>
<div class="mc-hero-grid">
<div>
<h1>Mecanic <span class="mc-hrs">- 0h</span></h1>
<p>Lucrezi intr-un service condus de jucatori. Diagnostichezi masini, schimbi piese, repari caroserii, tractezi si raspunzi la apeluri din tot orasul.</p>
</div>
<svg class="mc-gauge" viewBox="0 0 240 200" role="img" aria-label="Un indicator de turatie care urca pana aproape de zona rosie">
<path class="ring" pathLength="1" d="M 46.8 162.3 A 85 85 0 1 1 193.2 162.3"/>
<path class="load" pathLength="1" d="M 46.8 162.3 A 85 85 0 1 1 193.2 162.3"/>
<path class="red" d="M 186.3 77.5 A 85 85 0 0 1 193.2 162.3"/>
<line class="tick" x1="120" y1="22" x2="120" y2="34"/>
<line class="tick" x1="35" y1="71" x2="45" y2="77"/>
<line class="tick" x1="205" y1="71" x2="195" y2="77"/>
<line class="needle" x1="120" y1="120" x2="120" y2="52"/>
<circle class="hub" cx="120" cy="120" r="7"/>
<text class="big" x="120" y="166" text-anchor="middle">OBD</text>
<text x="120" y="186" text-anchor="middle">SCAN OK</text>
</svg>
</div>
</div>
</section>

<h2><small>Pornire</small>Cum devii mecanic?</h2>
<p class="mc-lead">Mecanicul nu se ia de la Primarie. Esti angajat de un <b>service</b>, o firma condusa de jucatori, iar jobul il primesti la prima tura.</p>
<ol class="mc-boot">
<li><span>[01]</span><p>Gaseste un service si vorbeste cu conducerea. Te angajeaza cand esti langa ei, dupa nume si ID.</p></li>
<li><span>[02]</span><p>Ia-ti o <b>Tableta firma</b> din magazinele de electronice. De aici vezi firma, pontajul si furnizorul.</p></li>
<li><span>[03]</span><p>Din tableta, la <b>Pontaj</b>, alege <b>Incepe tura</b>. Trebuie sa fii langa service sau langa o masina de lucru a mecanicilor.</p></li>
<li class="wait"><span>[OK]</span><p>Primesti jobul de <b>Mecanic</b> si intri in tura. Masinile de lucru le iei din garajul mecanicilor de la service.</p></li>
</ol>

<h2><small>Module</small>Ce face un mecanic</h2>
<div class="mc-tiles">
<div class="mc-tile">
<h3><span>OBD</span>Diagnoza</h3>
<p>Foloseste <b>Tester Auto</b> la capota sau de pe scaunul soferului. Se deschide tableta cu paginile Defecte, Date live, Revizii, Istoric si Fisa de lucru. Cu <kbd>ALT</kbd> folosesti cursorul.</p>
</div>
<div class="mc-tile">
<h3><span>LST</span>Agenda de lucru</h3>
<p>Din Fisa de lucru creezi o lista cu tot ce are de schimbat masina. O bifezi pe masura ce lucrezi. Cu <kbd>J</kbd> o redeschizi sau iei cursorul.</p>
</div>
<div class="mc-tile wide">
<h3><span>PRT</span>Piese</h3>
<p>Fiecare masina are doua feluri de piese. Le schimbi cu piesa din inventar, la masina, printr-un mic test de indemanare.</p>
<div class="mc-parts">
<p><b>Principale:</b> alternator, frane, injector, radiator, transmisie, pompa servo, motor si baterie la electrice. Se uzeaza la condus si in accidente.</p>
<p><b>De revizie:</b> ulei si filtru, bujii, curea de distributie, placute, anvelope, lichide si filtre. Se termina dupa un numar de kilometri.</p>
</div>
</div>
<div class="mc-tile">
<h3><span>CAR</span>Caroserie</h3>
<p>Inspecteaza masina ca sa vezi ce e stricat, apoi pune usi, capota, portbagaj, geamuri si roti noi.</p>
</div>
<div class="mc-tile">
<h3><span>LFT</span>Elevator si cric</h3>
<p>Elevatoarele din service le urci si le cobori tinand apasat <kbd>G</kbd> pe ele. <b>Cricul Auto</b> il asezi sub roata cu <kbd>E</kbd> si il pui inapoi cu <kbd>F5</kbd>.</p>
</div>
<div class="mc-tile">
<h3><span>TOW</span>Platforma</h3>
<p>Tine apasat <kbd>G</kbd> pe platforma si alege <b>Tracteaza vehicul</b>. Apoi, in spatele platformei, apasa <kbd>G</kbd> ca sa urci sau sa cobori masina.</p>
</div>
<div class="mc-tile">
<h3><span>CALL</span>Apeluri</h3>
<p>Cand cineva cheama un mecanic, apelul apare in aplicatia de apeluri, pe <kbd>F7</kbd>. Acolo il accepti.</p>
</div>
<div class="mc-tile">
<h3><span>IMP</span>Impound</h3>
<p>Politia cere ridicarea unor masini. Accepti apelul, gasesti masina, o duci la parcarea Impound si alegi <b>Livreaza vehiculul</b>.</p>
</div>
<div class="mc-tile">
<h3><span>RD</span>Ajutor pe drum</h3>
<p>Poti impinge orice masina, tinand apasat <kbd>ALT</kbd> langa ea. O masina goala rasturnata o pui pe roti tinand apasat <kbd>G</kbd> pe ea.</p>
</div>
<div class="mc-tile">
<h3><span>TUN</span>Tuning</h3>
<p>Doar mecanicii monteaza <b>Kitul stancer</b>, cu care reglezi rotile din meniul lui. <b>Antilag</b>-ul se pune doar pe masini cu turbo.</p>
</div>
</div>

<h2><small>Venit</small>De unde vin banii</h2>
<ul class="mc-pay">
<li><b>Salariu</b>, cat timp esti in tura.</li>
<li><b>Facturi</b> date clientilor cu <b>Terminalul POS</b>. Primesti o parte din fiecare.</li>
<li><b>Livrari la Impound</b>, platite dupa masina adusa.</li>
</ul>

<h2><small>Piese si materiale</small>De unde iau piese?</h2>
<p class="mc-lead">Din tableta firmei comanzi piese si unelte de la <b>furnizor</b>, cu banii tai. Ele ajung in depozitul firmei, la comun pentru toti colegii. Cand schimbi o piesa primesti inapoi materiale, mai multe daca piesa veche era intr-o stare buna. Le transformi la bancul <b>Reciclare piese</b> din service.</p>

<h2><small>Coduri memorate</small>Sfaturi</h2>
<ul class="mc-codes">
<li><span class="mc-sev crit">CRITIC</span><p><b>Nu pleca departe de service fara o masina de lucru.</b> Prezenta se verifica in fiecare minut. Daca nu esti langa service si nici langa o masina a mecanicilor, iesi din tura.</p></li>
<li><span class="mc-sev urg">URGENT</span><p><b>Jobul tine de firma.</b> Daca pleci din service sau esti concediat, pierzi jobul de mecanic.</p></li>
<li><span class="mc-sev">INFO</span><p><b>Programul firmei conteaza.</b> Daca firma are program de lucru, pontajul merge doar in orele stabilite de conducere.</p></li>
<li><span class="mc-sev">INFO</span><p><b>Spune-le clientilor de revizii.</b> O piesa de revizie expirata uzeaza mai repede piesele principale ale masinii.</p></li>
</ul>

</div>
