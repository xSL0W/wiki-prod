---
outline: false
---

<style>
.abz {
  --night: #0b1020;
  --panel: #121a30;
  --rail: #1d2742;
  --edge: #2c3858;
  --text: #e8ecf6;
  --mute: #9ba6c2;
  --led: #ffb21e;
  --led-dim: rgba(255, 178, 30, 0.16);
  --line: #23c4a8;
  --line-soft: rgba(35, 196, 168, 0.14);
  max-width: 920px;
  margin: 0 auto;
  color: var(--text);
  font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.abz *, .abz *::before, .abz *::after { box-sizing: border-box; }
.abz p, .abz li { line-height: 1.6; color: var(--text); margin: 0; }
.abz ul { list-style: none; padding: 0; margin: 0; }

/* hero: the destination sign on the front of the bus */
.abz-hero {
  background: var(--night);
  border: 1px solid var(--edge);
  border-radius: 20px;
  padding: clamp(1.1rem, 4vw, 2.2rem);
  overflow: hidden;
}
.abz-sign {
  background-color: #07090f;
  background-image: radial-gradient(rgba(255, 178, 30, 0.10) 1px, transparent 1.4px);
  background-size: 6px 6px;
  border: 3px solid #252b3a;
  border-radius: 12px;
  padding: clamp(0.9rem, 3vw, 1.4rem) clamp(1rem, 3vw, 1.6rem);
  box-shadow: inset 0 0 24px rgba(0, 0, 0, 0.8);
}
.abz-sign small {
  display: block;
  font-family: ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace;
  font-size: 0.8rem;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  color: var(--led);
  opacity: 0.75;
  margin-bottom: 0.35rem;
}
.abz-hero h1 {
  margin: 0;
  border: 0;
  padding: 0;
  font-family: ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace;
  font-size: clamp(1.6rem, 6vw, 3rem);
  line-height: 1.1;
  font-weight: 800;
  letter-spacing: 0.02em;
  text-transform: uppercase;
  color: var(--led);
  text-shadow: 0 0 6px rgba(255, 178, 30, 0.55), 0 0 18px rgba(255, 178, 30, 0.25);
  overflow-wrap: anywhere;
}
.abz-hero h1 .abz-hrs {
  display: inline-block;
  color: var(--night);
  background: var(--led);
  text-shadow: none;
  border-radius: 8px;
  padding: 0 0.4em;
  margin-left: 0.15em;
  text-transform: none;
}
.abz .abz-intro { max-width: 56ch; color: var(--mute); font-size: 1.05rem; margin-top: 1.2rem !important; }

/* the line map */
.abz-map { display: block; width: 100%; height: auto; margin-top: 1.4rem; }
.abz-map .track { fill: none; stroke: var(--line); stroke-width: 8; stroke-linecap: round; stroke-linejoin: round; }
.abz-map .ghost { fill: none; stroke: var(--rail); stroke-width: 18; stroke-linecap: round; stroke-linejoin: round; }
.abz-map .st { fill: #fff; stroke: var(--night); stroke-width: 4; }
.abz-map .pass { fill: var(--line); stroke: var(--night); stroke-width: 3; }
.abz-map .term { fill: var(--led); stroke: var(--night); stroke-width: 4; }
.abz-map text { fill: var(--mute); font-size: 13px; font-family: inherit; }
.abz-map .bus rect { fill: var(--led); }
.abz-map .bus .win { fill: var(--night); }
.abz-map .bus-still { display: none; }
@media (prefers-reduced-motion: reduce) {
  .abz-map .bus-moving { display: none; }
  .abz-map .bus-still { display: inline; }
}

.abz-legend { display: flex; flex-wrap: wrap; gap: 0.5rem 1.2rem; margin-top: 0.8rem; color: var(--mute); font-size: 0.9rem; }
.abz-legend span { display: inline-flex; align-items: center; gap: 0.45rem; }
.abz-legend i { display: inline-block; width: 14px; height: 14px; border-radius: 50%; border: 3px solid var(--night); outline: 2px solid var(--edge); }
.abz-legend .k-st { background: #fff; }
.abz-legend .k-pass { background: var(--line); }
.abz-legend .k-term { background: var(--led); }

/* facts strip, like tickets */
.abz .abz-facts { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 0.6rem; margin-top: 1.2rem; }
.abz-facts li {
  background: var(--panel);
  border: 1px dashed var(--edge);
  border-radius: 10px;
  padding: 0.6rem 0.9rem;
  font-size: 0.93rem;
}
.abz .abz-facts b { display: block; color: var(--led); font-size: 0.75rem; letter-spacing: 0.12em; text-transform: uppercase; }

/* sections */
.abz h2 {
  margin: 3rem 0 1rem;
  border: 0;
  padding: 0;
  font-size: 1.5rem;
  font-weight: 750;
  letter-spacing: -0.015em;
  color: #fff;
  display: flex;
  align-items: center;
  gap: 0.6rem;
}
.abz h2::before {
  content: attr(data-line);
  flex: none;
  font-size: 0.85rem;
  font-weight: 800;
  color: var(--night);
  background: var(--line);
  border-radius: 6px;
  padding: 0.1rem 0.45rem;
}
.abz b { color: #fff; font-weight: 650; }
.abz code { overflow-wrap: anywhere; }
.abz kbd {
  font: inherit; font-size: 0.85em; font-weight: 700; color: var(--night); background: var(--led);
  border-radius: 6px; padding: 0.05rem 0.45rem;
}

/* a shift as a line timetable */
.abz-line { position: relative; }
.abz-line::before {
  content: ''; position: absolute; left: 13px; top: 10px; bottom: 10px; width: 6px; border-radius: 3px;
  background: var(--line);
}
.abz-line li { position: relative; padding: 0 0 1.4rem 3.2rem; }
.abz-line li:last-child { padding-bottom: 0; }
.abz-line li::before {
  content: ''; position: absolute; left: 4px; top: 2px; width: 24px; height: 24px;
  border-radius: 50%; background: #fff; border: 5px solid var(--night); outline: 2px solid var(--line);
}
.abz-line li:last-child::before { background: var(--led); }
.abz-line small {
  display: block; font-size: 0.75rem; letter-spacing: 0.14em; text-transform: uppercase; color: var(--line); margin-bottom: 0.1rem;
}

/* two kinds of points */
.abz-kinds { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1rem; }
.abz-kind { background: var(--panel); border: 1px solid var(--edge); border-radius: 16px; padding: 1.2rem 1.35rem; }
.abz-kind.stop { background: linear-gradient(160deg, var(--line-soft), var(--panel) 60%); border-color: var(--line); }
.abz-kind h3 { margin: 0 0 0.45rem; border: 0; padding: 0; font-size: 1.1rem; color: #fff; }
.abz-kind p { color: var(--mute); }

/* tips */
.abz .abz-tips li {
  padding: 0.85rem 1rem;
  border-left: 4px solid var(--led);
  background: var(--panel);
  border-radius: 0 10px 10px 0;
  margin-bottom: 0.6rem;
}
.abz-tips li:last-child { margin-bottom: 0; }

.abz a:focus-visible { outline: 3px solid var(--led); outline-offset: 2px; }
/* block list: keeps the 8px row spacing the theme no longer adds to classed lists */
.abz .abz-line > li + li, .abz .abz-tips > li + li { margin-top: 8px; }
</style>

<div class="abz">

<section class="abz-hero">
<div class="abz-sign">
<small>Linia de serviciu</small>
<h1>Sofer de autobuz <span class="abz-hrs">- 0h</span></h1>
</div>
<p class="abz-intro">Primul job pentru orice jucator nou. Iei autobuzul de la depou, mergi pe o ruta prin oras, opresti in statii si iei plata la capatul liniei.</p>
<svg class="abz-map" viewBox="0 0 640 160" role="img" aria-label="Schema unei rute de autobuz: pleaca de la depou, trece prin statii si puncte de trecere si se intoarce la depou">
<path class="ghost" d="M40 120 L160 120 Q190 120 200 92 L220 50 Q232 30 260 30 L420 30 Q450 30 462 54 L478 92 Q490 120 520 120 L600 120"/>
<path class="track" d="M40 120 L160 120 Q190 120 200 92 L220 50 Q232 30 260 30 L420 30 Q450 30 462 54 L478 92 Q490 120 520 120 L600 120"/>
<circle class="term" cx="40" cy="120" r="11"/>
<circle class="st" cx="110" cy="120" r="9"/>
<circle class="pass" cx="210" cy="70" r="7"/>
<circle class="st" cx="290" cy="30" r="9"/>
<circle class="st" cx="360" cy="30" r="9"/>
<circle class="pass" cx="470" cy="72" r="7"/>
<circle class="st" cx="545" cy="120" r="9"/>
<circle class="term" cx="600" cy="120" r="11"/>
<g class="bus bus-moving">
<rect x="-17" y="-8" width="34" height="16" rx="4"/>
<rect class="win" x="-12" y="-4" width="7" height="5" rx="1"/>
<rect class="win" x="-2" y="-4" width="7" height="5" rx="1"/>
<rect class="win" x="8" y="-4" width="6" height="5" rx="1"/>
<animateMotion dur="9s" repeatCount="indefinite" rotate="auto" path="M40 120 L160 120 Q190 120 200 92 L220 50 Q232 30 260 30 L420 30 Q450 30 462 54 L478 92 Q490 120 520 120 L600 120"/>
</g>
<g class="bus bus-still" transform="translate(150 120)">
<rect x="-17" y="-8" width="34" height="16" rx="4"/>
<rect class="win" x="-12" y="-4" width="7" height="5" rx="1"/>
<rect class="win" x="-2" y="-4" width="7" height="5" rx="1"/>
<rect class="win" x="8" y="-4" width="6" height="5" rx="1"/>
</g>
<text x="22" y="152">depou</text>
<text x="572" y="152">depou</text>
</svg>
<div class="abz-legend">
<span><i class="k-st"></i>statie (opresti)</span>
<span><i class="k-pass"></i>punct de trecere</span>
<span><i class="k-term"></i>capat de linie</span>
</div>
<ul class="abz-facts">
<li><b>Ore necesare</b>0 ore, din prima zi</li>
<li><b>Vehicul</b>Autobuz de serviciu</li>
<li><b>Ruta</b>Aleasa la intamplare</li>
<li><b>Plata</b>La capatul fiecarei rute</li>
</ul>
</section>

<h2 data-line="L1">Cum ma angajez?</h2>
<p>Angajeaza-te ca <b>Sofer de autobuz</b> la Primarie (<code>Telefon → Harti → Locatii importante → Primarie</code>). Nu ai nevoie de ore jucate. Dupa angajare, pe harta apare depoul, cu numele <b>Inceput cursa autobuz</b>. Acolo te asteapta seful: apropie-te si apasa <kbd>E</kbd> ca sa vorbesti cu el.</p>

<h2 data-line="L2">O tura, statie cu statie</h2>
<ul class="abz-line">
<li><small>Depou</small><b>Alege Incepe tura</b> din meniul sefului. Primesti uniforma si o ruta, iar autobuzul apare intr-un loc liber din parcare, cu tine la volan.</li>
<li><small>Pe drum</small><b>Urmeaza GPS-ul</b> pana la urmatorul punct. Il recunosti dupa coloana rosie de lumina de pe sosea.</li>
<li><small>Statie</small><b>Intra cu autobuzul in punct.</b> In statii autobuzul se opreste singur cateva secunde, cat astepti pasagerii. Pe punctele de trecere doar treci prin ele.</li>
<li><small>Mai departe</small><b>Punctul s-a bifat,</b> iar GPS-ul iti arata urmatorul. Fiecare ruta are intre 7 si 11 puncte.</li>
<li><small>Capat de linie</small><b>Ultimul punct e inapoi langa depou.</b> Aici primesti plata in contul din banca. Primesti imediat o ruta noua, cu rezervorul plin, si poti continua.</li>
</ul>

<h2 data-line="L3">Statii si puncte de trecere</h2>
<div class="abz-kinds">
<div class="abz-kind stop">
<h3>Statie</h3>
<p>Autobuzul se opreste si apare cercul <b>Astepti in statie</b>. Stai pe loc pana se umple cercul, apoi statia se bifeaza.</p>
</div>
<div class="abz-kind">
<h3>Punct de trecere</h3>
<p>Doar un reper pe traseu, ca sa mergi pe drumul corect. Treci prin el si GPS-ul te duce mai departe.</p>
</div>
</div>

<h2 data-line="L4">Sfaturi</h2>
<ul class="abz-tips">
<li><b>Tu trebuie sa fii la volan.</b> Punctele se bifeaza doar cand intri in ele conducand autobuzul tau de serviciu. Cu alta masina nu se intampla nimic.</li>
<li><b>Nu lasa autobuzul.</b> Daca iesi din el, ai 10 minute sa te intorci. Dupa aceea autobuzul dispare si tura se termina.</li>
<li><b>Un punct nu s-a bifat?</b> Iesi din cerc si intra din nou cu autobuzul. Puncte luate prea repede unul dupa altul nu sunt acceptate.</li>
<li><b>Plata vine doar la capatul rutei.</b> Daca renunti la jumatatea drumului, nu primesti nimic pentru ruta inceputa.</li>
<li><b>Cand vrei sa te opresti,</b> alege <b>Termina tura</b> de la sef. Autobuzul dispare si primesti hainele inapoi. Si daca schimbi jobul sau iesi de pe server, autobuzul dispare si tura se opreste.</li>
<li><b>Vrei alta uniforma?</b> Din meniul sefului poti deschide garderoba jobului sau poti alege o tinuta salvata.</li>
</ul>
</div>
