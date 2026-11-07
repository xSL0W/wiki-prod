---
outline: false
---

<style>
.pdd {
  --ink: #0c0c0e;
  --panel: #18181b;
  --panel2: #202024;
  --line: #34343b;
  --text: #f4f4f5;
  --mute: #a1a1aa;
  --red: #dc2626;
  --acc: #60a5fa;
  width: 960px;
  max-width: 100%;
  margin: 0 auto;
  color: var(--text);
}
.pdd *, .pdd *::before, .pdd *::after { box-sizing: border-box; }
.pdd p, .pdd li { margin: 0; line-height: 1.6; color: var(--text); }
.pdd ul, .pdd ol { list-style: none; padding: 0; margin: 0; }
.pdd li + li { margin-top: 0; }
.pdd b { color: #fff; font-weight: 650; }
.pdd code { white-space: normal; overflow-wrap: anywhere; }
.pdd a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.pdd a:hover { color: #fecaca; }
.pdd a:focus-visible { outline: 3px solid var(--acc); outline-offset: 3px; border-radius: 6px; }
.pdd .pdd-head {
  background: var(--ink); border: 1px solid var(--line); border-left: 4px solid var(--acc);
  border-radius: 18px; padding: clamp(1.2rem, 4vw, 2rem);
}
.pdd .pdd-kicker { font-size: 0.78rem; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: var(--acc); margin-bottom: 0.5rem; }
.pdd .pdd-head h1 {
  margin: 0 0 0.7rem; border: 0; padding: 0;
  font-size: clamp(2rem, 7vw, 3rem); line-height: 1.05; font-weight: 800; letter-spacing: -0.03em; color: #fff;
}
.pdd .pdd-lede { color: var(--mute); font-size: 1.05rem; max-width: 60ch; }
.pdd .pdd-facts { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 180px), 1fr)); gap: 0.7rem; margin-top: 1rem; }
.pdd .pdd-facts li { background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 0.9rem 1rem; }
.pdd .pdd-facts b { display: block; font-size: 1.5rem; line-height: 1.1; color: var(--acc); font-variant-numeric: tabular-nums; }
.pdd .pdd-facts span { color: var(--mute); font-size: 0.92rem; }
.pdd h2 {
  margin: 2.6rem 0 1rem; border: 0; padding: 0 0 0 0.8rem; border-left: 4px solid var(--acc);
  font-size: 1.4rem; font-weight: 750; letter-spacing: -0.015em; color: #fff;
}
.pdd .pdd-sub { color: var(--mute); margin: -0.4rem 0 1rem; max-width: 64ch; }
.pdd kbd { display: inline-block; min-width: 1.6em; padding: 0 0.4em; border: 1px solid var(--line); border-bottom-width: 3px; border-radius: 6px; background: var(--panel2); color: #fff; font: 700 0.85em/1.6 Inter, system-ui, sans-serif; text-align: center; }
.pdd .pdd-cat { background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 0.4rem 1.1rem; }
.pdd .pdd-cat + .pdd-cat { margin-top: 0.9rem; }
.pdd .pdd-cat h3 { margin: 0.8rem 0 0.2rem; border: 0; padding: 0; font-size: 1.1rem; font-weight: 750; color: #fff; }
.pdd .pdd-items li { display: grid; grid-template-columns: minmax(0, 13rem) minmax(0, 1fr); gap: 0.3rem 1rem; padding: 0.7rem 0; border-top: 1px solid var(--line); }
.pdd .pdd-items li:first-child { border-top: 0; }
.pdd .pdd-items span { color: var(--mute); font-size: 0.95rem; }
.pdd .pdd-notes { display: grid; gap: 0.5rem; }
.pdd .pdd-end { margin-top: 1rem; }
.pdd .pdd-notes li { position: relative; padding-left: 1.3rem; color: var(--mute); }
.pdd .pdd-notes li::before { content: ''; position: absolute; left: 0.2rem; top: 0.62em; width: 0.45rem; height: 0.45rem; border-radius: 50%; background: var(--acc); }
@media (max-width: 560px) {
  .pdd .pdd-items li { grid-template-columns: minmax(0, 1fr); }
}
</style>

<div class="pdd">
<section class="pdd-head">
<p class="pdd-kicker">Proprietati · Magazin</p>
<h1>DigitalDen</h1>
<p class="pdd-lede">Magazinul de electronice din Vespucci. Aici iei telefon, radio, smartwatch, tableta si terminalul POS pentru firma, boxa EliteBox si drone. Oricine poate cumpara.</p>
</section>
<ul class="pdd-facts">
<li><b>1</b><span>magazin, in Vespucci</span></li>
<li><b>726</b><span>codul postal al magazinului</span></li>
<li><b>11</b><span>produse, in 2 categorii</span></li>
</ul>
<h2>Unde il gasesti</h2>
<ul class="pdd-notes">
<li>Pe harta apare ca DigitalDen, cu un blip albastru, la codul postal <code>726</code>.</li>
<li>Mergi langa vanzator si apasa <kbd>E</kbd> la Acceseaza magazinul. Banii se iau intai cash, iar ce lipseste se ia din banca.</li>
<li>Magazinul e al unei firme. Banii din vanzari ajung la ea, iar firma isi poate pune propriile preturi. Stocul nu se termina niciodata.</li>
</ul>
<h2>Ce gasesti</h2>
<p class="pdd-sub">Preturile se schimba in timp, le vezi direct in magazin.</p>
<div class="pdd-cat">
<h3>Diverse</h3>
<ul class="pdd-items">
<li><b>Telefon</b><span>Apeluri, mesaje si aplicatii. Cat il ai deschis, vezi GPS-ul pe minimapa. Detalii pe pagina <a href="/general/telefon">Telefon</a>.</span></li>
<li><b>SmartWatch (GPS)</b><span>Cat il ai in inventar, minimapa cu GPS ramane pe ecran si fara sa deschizi telefonul.</span></li>
<li><b>Radio</b><span>Statie radio: vorbesti cu ceilalti pe aceeasi frecventa.</span></li>
<li><b>EliteBox</b><span>Boxa portabila. O pui jos si dai muzica pe ea din telefon. O poti ridica inapoi oricand.</span></li>
<li><b>Body Camera</b><span>Cat o ai in inventar, pe HUD apare indicatorul REC.</span></li>
<li><b>Tableta firma</b><span>Gestionezi firma ta din ea.</span></li>
<li><b>Terminal POS</b><span>Faci facturi clientilor firmei tale.</span></li>
<li><b>Acumulator</b><span>Sursa de curent. Intra in reteta de C4, la crafting.</span></li>
</ul>
</div>
<div class="pdd-cat">
<h3>Drone</h3>
<ul class="pdd-items">
<li><b>Drona</b><span>Drona de baza, pentru recunoastere din aer.</span></li>
<li><b>Drona NightVision</b><span>Are vedere de noapte.</span></li>
<li><b>Drona FPV</b><span>Drona de curse: rapida, dar fragila, cu baterie care tine putin.</span></li>
</ul>
</div>
<ul class="pdd-notes pdd-end">
<li>Cum zbori cu dronele afli pe pagina <a href="/general/sistem-drone">Sistem drone</a>.</li>
</ul>
</div>
