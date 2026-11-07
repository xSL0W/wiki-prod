---
outline: false
---

<style>
.mt {
  --tunnel: #080b14;
  --wall: #10162a;
  --tile: #1a2240;
  --line: #2c365a;
  --text: #e6ebf7;
  --mute: #98a3c2;
  --signal: #2bd4f0;
  --signal-soft: rgba(43, 212, 240, 0.12);
  --edge: #ffd23f;
  --q-normal: #94a3b8;
  --q-good: #f59e0b;
  --q-perfect: #22c55e;
  max-width: 940px;
  margin: 0 auto;
  color: var(--text);
  font-family: 'DIN Alternate', 'Bahnschrift', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.mt *, .mt *::before, .mt *::after { box-sizing: border-box; }
.mt p, .mt li { line-height: 1.6; color: var(--text); margin: 0; }
.mt ul, .mt ol { list-style: none; padding: 0; margin: 0; }
.mt h1, .mt h2, .mt h3 { border: 0; padding: 0; }
.mt a:focus-visible { outline: 3px solid var(--signal); outline-offset: 2px; }
.mt b { color: #fff; font-weight: 650; }
.mt kbd {
  font: inherit; font-size: 0.85em; font-weight: 700; color: var(--tunnel); background: var(--signal);
  border-radius: 6px; padding: 0.05rem 0.45rem; white-space: nowrap;
}

/* hero: the line map */
.mt-hero {
  background: radial-gradient(120% 90% at 85% 0%, var(--signal-soft), transparent 60%), var(--tunnel);
  border: 1px solid var(--line);
  border-radius: 20px;
  padding: clamp(1.2rem, 4vw, 2.4rem);
  overflow: hidden;
  position: relative;
}
.mt-hero::after {
  content: ''; position: absolute; left: 0; right: 0; bottom: 0; height: 8px;
  background: repeating-linear-gradient(90deg, var(--edge) 0 18px, #000 18px 36px);
}
.mt-tag { display: flex; align-items: center; gap: 0.6rem; color: var(--mute); font-size: 0.85rem; letter-spacing: 0.16em; text-transform: uppercase; }
.mt-m {
  display: inline-grid; place-items: center; width: 2rem; height: 2rem; border-radius: 50%;
  background: var(--signal); color: var(--tunnel); font-weight: 900; letter-spacing: 0; font-size: 1.05rem;
}
.mt-hero h1 {
  margin: 0.9rem 0 0.6rem;
  font-size: clamp(2rem, 6.5vw, 3.4rem);
  line-height: 1.05;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: #fff;
}
.mt-tail { white-space: nowrap; }
.mt-hours {
  display: inline-block; font-size: 0.6em; vertical-align: 0.25em; color: var(--tunnel); background: var(--edge);
  border-radius: 8px; padding: 0.1em 0.45em; font-weight: 800;
}
.mt-hero > p { max-width: 54ch; color: var(--mute); font-size: 1.05rem; }
.mt-map { display: block; width: 100%; height: auto; margin: 1.4rem 0 1.6rem; }
.mt-map .track { fill: none; stroke: var(--signal); stroke-width: 8; stroke-linejoin: round; opacity: 0.35; }
.mt-map .train {
  fill: none; stroke: var(--signal); stroke-width: 10; stroke-linecap: round;
  stroke-dasharray: 0.05 0.95; animation: mt-run 14s linear infinite;
}
.mt-map .st { fill: var(--tunnel); stroke: #fff; stroke-width: 3; }
.mt-map .start { fill: var(--edge); stroke: var(--edge); }
.mt-map text { fill: var(--mute); font-size: 14px; font-family: inherit; letter-spacing: 0.05em; }
.mt-map .lbl-start { fill: var(--edge); font-weight: 700; }
@keyframes mt-run { to { stroke-dashoffset: -1; } }
@media (prefers-reduced-motion: reduce) {
  .mt-map .train { animation: none; }
}

/* the station strip */
.mt-line { display: flex; flex-wrap: wrap; gap: 0.5rem 0; position: relative; }
.mt-line li {
  position: relative; padding: 0 0.9rem 0 1.25rem; font-size: 0.92rem; color: var(--text);
}
.mt-line li::before {
  content: ''; position: absolute; left: 0; top: 0.42em; width: 10px; height: 10px; border-radius: 50%;
  background: var(--tunnel); border: 2px solid var(--signal);
}
.mt-line li.here::before { background: var(--edge); border-color: var(--edge); }
.mt-line li.here { color: var(--edge); font-weight: 700; }

/* sections */
.mt h2 {
  margin: 3rem 0 1rem;
  font-size: 1.5rem; font-weight: 780; letter-spacing: -0.01em; color: #fff;
  display: flex; align-items: center; gap: 0.6rem;
}
.mt h2::before { content: ''; width: 14px; height: 14px; border-radius: 50%; background: var(--signal); flex: none; }

/* the shift: platform signs */
.mt-run { display: grid; gap: 0.7rem; counter-reset: st; }
.mt-run li {
  counter-increment: st;
  display: grid; grid-template-columns: 2.6rem 1fr; gap: 1rem; align-items: start;
  background: var(--wall); border: 1px solid var(--line); border-radius: 12px; padding: 0.9rem 1.1rem;
}
.mt-run li::before {
  content: counter(st); display: grid; place-items: center; width: 2.6rem; height: 2.6rem; border-radius: 50%;
  background: var(--tile); border: 2px solid var(--signal); color: #fff; font-weight: 800;
}
/* first text line centred on the number circle; longer steps keep reading down from there */
.mt-run li > p { padding-top: calc((2.6rem - 1.6em) / 2); }

/* driver console */
.mt-console {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 0.7rem;
  background: var(--wall); border: 1px solid var(--line); border-radius: 16px; padding: 1rem;
}
.mt-console li { background: var(--tunnel); border: 1px solid var(--line); border-radius: 10px; padding: 0.8rem 0.9rem; }
.mt .mt-console { padding: 1rem; }
.mt-console .keys { display: flex; gap: 0.3rem; flex-wrap: wrap; margin-bottom: 0.35rem; }
.mt-console p { color: var(--mute); font-size: 0.93rem; }

/* stop target */
.mt-stop { display: grid; grid-template-columns: minmax(0, 220px) 1fr; gap: 1.5rem; align-items: center; }
.mt-stop svg { display: block; width: 100%; height: auto; }
.mt-stop .z-normal { fill: var(--q-normal); fill-opacity: 0.25; stroke: var(--q-normal); stroke-width: 2; }
.mt-stop .z-good { fill: var(--q-good); fill-opacity: 0.3; stroke: var(--q-good); stroke-width: 2; }
.mt-stop .z-perfect { fill: var(--q-perfect); fill-opacity: 0.45; stroke: var(--q-perfect); stroke-width: 2; }
.mt-stop .arrow { fill: #fff; }
.mt-q li { display: flex; gap: 0.7rem; padding: 0.55rem 0; border-bottom: 1px solid var(--line); }
.mt-q li:last-child { border-bottom: 0; }
.mt-q i { flex: none; width: 14px; height: 14px; border-radius: 50%; margin-top: 0.35em; }
.mt-q .n { background: var(--q-normal); }
.mt-q .g { background: var(--q-good); }
.mt-q .p { background: var(--q-perfect); }
.mt-q .x { background: transparent; border: 2px solid #ef4444; }
@media (max-width: 560px) { .mt-stop { grid-template-columns: 1fr; } .mt-stop svg { max-width: 220px; margin: 0 auto; } }

.mt .mt-after { margin-top: 1rem; color: var(--mute); }

/* tips */
.mt-tips li { padding: 0.8rem 0 0.8rem 1rem; border-left: 3px solid var(--edge); margin-bottom: 0.6rem; background: linear-gradient(90deg, rgba(255, 210, 63, 0.07), transparent 70%); border-radius: 0 10px 10px 0; }
/* block list: keeps the 8px row spacing the theme no longer adds to classed lists */
.mt .mt-q > li + li, .mt .mt-tips > li + li { margin-top: 8px; }
</style>

<div class="mt">

<section class="mt-hero">
<div class="mt-tag"><span class="mt-m">M</span>Linia de metrou Los Santos</div>
<h1>Mecanic metrou <span class="mt-tail">- <span class="mt-hours">400h</span></span></h1>
<p>Conduci metroul orasului pe toata linia, opresti in fiecare statie si deschizi usile pentru pasageri. Cu cat opresti mai precis, cu atat tura iese mai bine.</p>
<svg class="mt-map" viewBox="0 0 680 230" role="img" aria-label="Schema liniei de metrou: zece statii pe dus si zece pe intors, cu startul in statia Burton">
<path class="track" d="M90 70 H590 A50 50 0 0 1 590 170 H90 A50 50 0 0 1 90 70 Z"/>
<path class="train" pathLength="1" d="M90 70 H590 A50 50 0 0 1 590 170 H90 A50 50 0 0 1 90 70 Z"/>
<circle class="st" cx="90" cy="70" r="7"/>
<circle class="st" cx="146" cy="70" r="7"/>
<circle class="st" cx="201" cy="70" r="7"/>
<circle class="st" cx="257" cy="70" r="7"/>
<circle class="st" cx="312" cy="70" r="7"/>
<circle class="st" cx="368" cy="70" r="7"/>
<circle class="st" cx="423" cy="70" r="7"/>
<circle class="st" cx="479" cy="70" r="7"/>
<circle class="st" cx="534" cy="70" r="7"/>
<circle class="st" cx="590" cy="70" r="7"/>
<circle class="st" cx="590" cy="170" r="7"/>
<circle class="st" cx="534" cy="170" r="7"/>
<circle class="st" cx="479" cy="170" r="7"/>
<circle class="st" cx="423" cy="170" r="7"/>
<circle class="st" cx="368" cy="170" r="7"/>
<circle class="st start" cx="312" cy="170" r="9"/>
<circle class="st" cx="257" cy="170" r="7"/>
<circle class="st" cx="201" cy="170" r="7"/>
<circle class="st" cx="146" cy="170" r="7"/>
<circle class="st" cx="90" cy="170" r="7"/>
<text x="20" y="40">LSIA TERMINAL 4</text>
<text x="600" y="40" text-anchor="end">DAVIS</text>
<text class="lbl-start" x="312" y="210" text-anchor="middle">BURTON - START</text>
</svg>
<ol class="mt-line" aria-label="Statiile liniei, in ordine">
<li>LSIA Terminal 4</li>
<li>LSIA Parking</li>
<li>Puerto Del Sol</li>
<li>Strawberry</li>
<li class="here">Burton</li>
<li>Portola Drive</li>
<li>Del Perro</li>
<li>Little Seoul</li>
<li>Pillbox South</li>
<li>Davis</li>
</ol>
</section>

<h2>Cum incep?</h2>
<p>Angajeaza-te ca <b>Mecanic metrou</b> la Primarie (<code>Telefon → Harti → Locatii importante → Primarie</code>) sau direct la seful de pe peron, cu <b>Angajeaza-te ca Mecanic metrou</b>. Ai nevoie de <b>400 de ore</b> jucate. Dupa angajare, pe harta apare <b>Intrare subterana metrou</b>: coboara pe peronul statiei Burton, unde te asteapta seful.</p>

<h2>O tura, statie cu statie</h2>
<ol class="mt-run">
<li><p><b>Vorbeste cu seful</b> cu <kbd>E</kbd> si alege <b>Incepe tura</b>. In fereastra care se deschide vezi bonusurile turei, apoi apesi <b>Incepe</b>.</p></li>
<li><p><b>Metroul apare in statie</b> si esti pus direct in cabina. Pe ecran ai vitezometrul, statia urmatoare si progresul turei.</p></li>
<li><p><b>Pleaca spre statia urmatoare.</b> Pe unele portiuni apare o viteza recomandata. E doar un sfat, nu te penalizeaza.</p></li>
<li><p><b>Opreste in tinta din statie</b>, apoi deschide usile cu <kbd>E</kbd>. Pasagerii urca si coboara.</p></li>
<li><p><b>Inchide usile tot cu <kbd>E</kbd>.</b> Se aude semnalul de avertizare, iar dupa ce usile s-au inchis poti pleca.</p></li>
<li><p><b>O tura are 20 de opriri</b>, adica toata linia dus-intors. La final primesti plata in cont, iar tura urmatoare porneste singura.</p></li>
</ol>

<h2>Pupitrul de comanda</h2>
<ul class="mt-console">
<li><div class="keys"><kbd>W</kbd></div><p>Accelerezi cu o treapta.</p></li>
<li><div class="keys"><kbd>S</kbd></div><p>Incetinesti cu o treapta.</p></li>
<li><div class="keys"><kbd>Shift</kbd><kbd>W</kbd></div><p>Sari direct la viteza recomandata sau la viteza maxima.</p></li>
<li><div class="keys"><kbd>Shift</kbd><kbd>S</kbd></div><p>Opresti metroul de tot.</p></li>
<li><div class="keys"><kbd>E</kbd></div><p>Deschizi sau inchizi usile. Merge doar cu metroul oprit, in statie.</p></li>
<li><div class="keys"><kbd>F</kbd></div><p>Cobori din metrou, doar cu usile deschise. Tura se incheie.</p></li>
</ul>

<h2>Cum se puncteaza o oprire</h2>
<div class="mt-stop">
<svg viewBox="0 0 220 220" role="img" aria-label="Tinta din statie: cercul exterior gri, cel din mijloc portocaliu, centrul verde">
<circle class="z-normal" cx="110" cy="110" r="100"/>
<circle class="z-good" cx="110" cy="110" r="50"/>
<circle class="z-perfect" cx="110" cy="110" r="25"/>
<path class="arrow" d="M110 98 l-12 -22 h24 z"/>
</svg>
<ul class="mt-q">
<li><i class="p"></i><p><b>Perfect</b> - ai oprit in centrul verde.</p></li>
<li><i class="g"></i><p><b>Bun</b> - ai oprit in cercul portocaliu.</p></li>
<li><i class="n"></i><p><b>Normal</b> - ai oprit in cercul gri, in raza statiei.</p></li>
<li><i class="x"></i><p><b>Ratat</b> - ai trecut de statie fara sa deschizi usile. Statia conteaza la tura, dar iti scade plata.</p></li>
</ul>
</div>
<p class="mt-after">Sageata alba arata exact punctul care se masoara, putin in fata cabinei. Cu destule opriri perfecte sau bune intr-o tura primesti un bonus. Pragurile le vezi in fereastra de start. Plata mai depinde si de statiile ratate, iar VIP-ul iti aduce un bonus in plus.</p>

<h2>Sfaturi</h2>
<ul class="mt-tips">
<li><b>Termina tura inainte sa cobori.</b> Daca iesi din metrou, trenul dispare, iar opririle din tura neterminata nu se platesc.</li>
<li><b>Opreste complet inainte de usi.</b> Usile nu se deschid cat timp metroul inca merge, iar cu usile deschise nu poti porni.</li>
<li><b>Franeaza din timp.</b> Tinta apare cand te apropii de statie. Daca o depasesti, statia e pierduta.</li>
<li><b>Daca primesti mesajul ca exista deja un metrou aici,</b> asteapta sa plece si incearca din nou.</li>
</ul>

</div>
