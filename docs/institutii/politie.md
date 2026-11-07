---
outline: false
---

<style>
.pol {
  --ink: #05070d;
  --panel: #10131b;
  --panel2: #171b26;
  --line: #262c3b;
  --text: #eef1f7;
  --mute: #9aa3b5;
  --blue: #3b82f6;
  --blue-soft: rgba(59, 130, 246, 0.16);
  --red: #ef4444;
  --red-deep: #b91c1c;
  --red-soft: rgba(239, 68, 68, 0.14);
  --gold: #f5c542;
  max-width: 960px;
  margin: 0 auto;
  color: var(--text);
  font-family: Inter, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.pol *, .pol *::before, .pol *::after { box-sizing: border-box; }
.pol p, .pol li { line-height: 1.6; color: var(--text); margin: 0; }
.pol ul, .pol ol { list-style: none; padding: 0; margin: 0; }
.pol li + li { margin-top: 0; }
.pol b { color: #fff; font-weight: 650; }
.pol code { white-space: normal; overflow-wrap: anywhere; }
.pol a { color: #fff; text-decoration: underline; text-decoration-color: var(--blue); text-underline-offset: 3px; }
.pol a:hover { color: #bfdbfe; }
.pol a:focus-visible { outline: 3px solid var(--blue); outline-offset: 3px; border-radius: 6px; }
.pol kbd {
  font: inherit; font-size: 0.85em; font-weight: 700; color: #fff; background: #1e3a8a;
  border: 1px solid #2f4fae; border-radius: 6px; padding: 0.05rem 0.45rem; white-space: nowrap;
}
/* ---------- hero: night patrol, lightbar on top, badge on the right ---------- */
.pol .pol-hero {
  position: relative; overflow: hidden; isolation: isolate;
  background: radial-gradient(120% 140% at 100% 0%, #0d1730, var(--ink) 62%);
  border: 1px solid var(--line); border-radius: 22px;
  padding: clamp(1.15rem, 4vw, 2.4rem); padding-top: clamp(2.2rem, 6vw, 3.2rem);
}
.pol .pol-wash { position: absolute; inset: 0; z-index: -1; pointer-events: none; }
.pol .pol-wash::before, .pol .pol-wash::after {
  content: ''; position: absolute; top: -40%; width: 70%; height: 120%; border-radius: 50%; opacity: 0;
}
.pol .pol-wash::before { left: -15%; background: radial-gradient(closest-side, rgba(239, 68, 68, 0.32), transparent); animation: pol-wash-r 1.6s steps(1, end) infinite; }
.pol .pol-wash::after { right: -15%; background: radial-gradient(closest-side, rgba(59, 130, 246, 0.36), transparent); animation: pol-wash-b 1.6s steps(1, end) infinite; }
@keyframes pol-wash-r { 0%, 12%, 24% { opacity: 1; } 6%, 18%, 30%, 100% { opacity: 0; } }
@keyframes pol-wash-b { 0%, 50% { opacity: 0; } 50%, 62%, 74% { opacity: 1; } 56%, 68%, 80%, 100% { opacity: 0; } }
.pol .pol-bar {
  position: absolute; top: 0.9rem; left: 50%; transform: translateX(-50%);
  display: grid; grid-template-columns: repeat(6, 1fr); gap: 3px; width: min(320px, 70%); height: 12px;
  padding: 2px; border-radius: 8px; background: #0b0d12; border: 1px solid #2a2f3c;
}
.pol .pol-bar span { border-radius: 3px; background: #1a1f2b; }
.pol .pol-bar span:nth-child(-n+3) { animation: pol-led-r 1.6s steps(1, end) infinite; }
.pol .pol-bar span:nth-child(n+4) { animation: pol-led-b 1.6s steps(1, end) infinite; }
@keyframes pol-led-r { 0%, 12%, 24% { background: var(--red); box-shadow: 0 0 12px var(--red); } 6%, 18%, 30%, 100% { background: #2a1416; box-shadow: none; } }
@keyframes pol-led-b { 0%, 50% { background: #121a2e; box-shadow: none; } 50%, 62%, 74% { background: var(--blue); box-shadow: 0 0 12px var(--blue); } 56%, 68%, 80%, 100% { background: #121a2e; box-shadow: none; } }
.pol .pol-top { display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: 1.2rem; align-items: center; }
.pol .pol-kicker { font-size: 0.78rem; font-weight: 700; letter-spacing: 0.16em; text-transform: uppercase; color: #93c5fd; margin-bottom: 0.55rem; }
.pol .pol-hero h1 {
  margin: 0 0 0.75rem; border: 0; padding: 0;
  font-size: clamp(2rem, 6.4vw, 3.4rem); line-height: 1.04; font-weight: 800; letter-spacing: -0.03em; color: #fff;
}
.pol .pol-hero h1 span { color: #93c5fd; }
.pol .pol-lede { max-width: 56ch; color: var(--mute); font-size: 1.05rem; }
.pol .pol-badge { width: clamp(92px, 18vw, 150px); height: auto; display: block; }
.pol-badge .shield { fill: #0f1a33; stroke: var(--gold); stroke-width: 4; }
.pol-badge .inner { fill: none; stroke: rgba(245, 197, 66, 0.45); stroke-width: 2; }
.pol-badge .star { fill: var(--gold); }
.pol-badge .txt { fill: var(--gold); font: 800 11px Inter, system-ui, sans-serif; letter-spacing: 0.12em; }
.pol-badge .glint { fill: url(#pol-glint); transform: translateX(-140px); animation: pol-glint 6s ease-in-out infinite; }
@keyframes pol-glint { 0%, 55% { transform: translateX(-140px); } 85%, 100% { transform: translateX(160px); } }
.pol .pol-stats { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 0.6rem; margin-top: 1.3rem; }
.pol .pol-stats li { background: rgba(16, 19, 27, 0.88); border: 1px solid var(--line); border-radius: 14px; padding: 0.7rem 0.9rem; }
.pol .pol-stats b { display: block; font-size: clamp(1.35rem, 4vw, 1.8rem); line-height: 1.1; font-weight: 800; color: #fff; font-variant-numeric: tabular-nums; }
.pol .pol-stats span { display: block; color: var(--mute); font-size: 0.82rem; line-height: 1.35; margin-top: 0.2rem; }
@media (max-width: 560px) {
  .pol .pol-top { grid-template-columns: minmax(0, 1fr); }
  .pol .pol-badge { display: none; }
  .pol .pol-stats { grid-template-columns: minmax(0, 1fr); }
}
@media (prefers-reduced-motion: reduce) {
  .pol .pol-wash::before, .pol .pol-wash::after, .pol .pol-bar span, .pol-badge .glint { animation: none; }
  .pol .pol-wash::before, .pol .pol-wash::after { opacity: 0.35; }
  .pol .pol-bar span:nth-child(-n+3) { background: var(--red); }
  .pol .pol-bar span:nth-child(n+4) { background: var(--blue); }
  .pol-badge .glint { display: none; }
}
/* ---------- sections ---------- */
.pol .pol-h2 {
  display: flex; align-items: flex-start; gap: 0.65rem;
  margin: 3rem 0 0.9rem; border: 0; padding: 0;
  font-size: 1.5rem; font-weight: 750; letter-spacing: -0.015em; line-height: 1.25; color: #fff;
}
.pol .pol-h2::before { margin-top: calc(0.5lh - 0.55rem / 2);
  content: ''; flex: none; width: 0.85rem; height: 0.55rem; border-radius: 3px;
  background: linear-gradient(90deg, var(--red) 50%, var(--blue) 50%);
}
.pol .pol-h3 { margin: 0 0 0.35rem; border: 0; padding: 0; font-size: 1.05rem; font-weight: 700; color: #fff; line-height: 1.3; }
.pol .pol-sub { color: var(--mute); max-width: 68ch; margin-bottom: 1rem; }
.pol .pol-card { background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 1.1rem 1.25rem; }
.pol .pol-card p { color: var(--mute); font-size: 0.96rem; }
.pol .pol-card p + p { margin-top: 0.5rem; }
.pol .pol-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr)); gap: 0.75rem; }
/* bullet list inside cards */
.pol .pol-list li { position: relative; padding-left: 1.1rem; color: var(--mute); font-size: 0.95rem; }
.pol .pol-list li + li { margin-top: 0.4rem; }
.pol .pol-list li::before { content: ''; position: absolute; left: 0; top: 0.62em; width: 6px; height: 6px; border-radius: 50%; background: var(--blue); }
/* road to the badge */
.pol .pol-road { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 210px), 1fr)); gap: 0.75rem; counter-reset: pol-step; }
.pol .pol-road li {
  position: relative; counter-increment: pol-step;
  background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 2.6rem 1.15rem 1.05rem;
}
.pol .pol-road li::before {
  content: counter(pol-step); position: absolute; top: 0.9rem; left: 1.15rem;
  width: 1.5rem; height: 1.5rem; border-radius: 50%; display: grid; place-items: center;
  font-size: 0.8rem; font-weight: 800; color: #fff; background: #1d4ed8;
}
.pol .pol-road p { color: var(--mute); font-size: 0.95rem; }
.pol .pol-check { margin-top: 0.75rem; border-left: 3px solid var(--gold); background: linear-gradient(90deg, rgba(245, 197, 66, 0.08), var(--panel) 40%); }
/* grade ladder */
.pol .pol-ladder { border: 1px solid var(--line); border-radius: 16px; overflow: hidden; background: var(--panel); }
.pol .pol-ladder li {
  display: grid; grid-template-columns: 2.4rem minmax(0, 11rem) minmax(0, 1fr); gap: 0.4rem 0.9rem; align-items: baseline;
  padding: 0.7rem 1rem; border-top: 1px solid var(--line);
}
.pol .pol-ladder li:first-child { border-top: 0; }
.pol .pol-ladder .n {
  font: 800 0.95rem/1 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; color: #93c5fd;
  display: inline-grid; place-items: center; width: 2rem; height: 2rem; border-radius: 8px; background: var(--blue-soft);
}
.pol .pol-ladder .t { font-weight: 700; color: #fff; }
.pol .pol-ladder .d { color: var(--mute); font-size: 0.92rem; line-height: 1.45; }
.pol .pol-ladder li.boss .n { color: var(--gold); background: rgba(245, 197, 66, 0.14); }
.pol .pol-ladder .tag {
  display: block; width: fit-content; margin-top: 0.3rem; font-size: 0.68rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase;
  color: var(--gold); border: 1px solid rgba(245, 197, 66, 0.4); border-radius: 999px; padding: 0 0.45rem;
}
@media (max-width: 560px) {
  .pol .pol-ladder li { grid-template-columns: 2.4rem minmax(0, 1fr); }
  .pol .pol-ladder .d { grid-column: 2; }
}
/* equipment chips */
.pol .pol-gear { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 200px), 1fr)); gap: 0.6rem; }
.pol .pol-gear li { background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 0.8rem 0.95rem; }
.pol .pol-gear b { display: block; font-size: 0.97rem; }
.pol .pol-gear span { display: block; color: var(--mute); font-size: 0.88rem; line-height: 1.45; margin-top: 0.2rem; }
/* field actions */
.pol .pol-acts { border: 1px solid var(--line); border-radius: 16px; overflow: hidden; background: var(--panel); }
.pol .pol-acts li { display: grid; grid-template-columns: minmax(0, 10rem) minmax(0, 1fr); gap: 0.3rem 1rem; padding: 0.8rem 1rem; border-top: 1px solid var(--line); }
.pol .pol-acts li:first-child { border-top: 0; }
.pol .pol-acts .a { font-weight: 700; color: #fff; }
.pol .pol-acts .h { color: var(--mute); font-size: 0.93rem; line-height: 1.5; }
@media (max-width: 560px) { .pol .pol-acts li { grid-template-columns: minmax(0, 1fr); } }
/* radio codes */
.pol .pol-codes { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 190px), 1fr)); gap: 0.45rem; }
.pol .pol-codes li {
  display: flex; gap: 0.6rem; align-items: baseline; background: #0b0e15; border: 1px solid var(--line); border-radius: 10px; padding: 0.5rem 0.7rem;
  font-size: 0.9rem; color: var(--mute);
}
.pol .pol-codes li b { font: 800 0.9rem/1 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; color: #93c5fd; flex: none; }
.pol .pol-codes li.em b { color: #fca5a5; }
/* keys */
.pol .pol-keys { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 230px), 1fr)); gap: 0.45rem 1rem; }
.pol .pol-keys li { display: flex; gap: 0.6rem; align-items: baseline; color: var(--mute); font-size: 0.93rem; }
.pol .pol-keys li kbd, .pol .pol-keys li code { flex: none; }
.pol .pol-note { margin-top: 0.85rem; color: var(--mute); font-size: 0.92rem; }
.pol .pol-rules {
  margin-top: 3rem; display: flex; flex-wrap: wrap; gap: 0.8rem 1.2rem; align-items: center; justify-content: space-between;
  background: linear-gradient(120deg, var(--blue-soft), var(--panel) 55%); border: 1px solid #2b4a8a; border-radius: 16px; padding: 1.1rem 1.25rem;
}
.pol .pol-rules p { color: var(--mute); max-width: 60ch; }
.pol .pol-btn {
  display: inline-block; font-weight: 700; color: #fff; text-decoration: none; background: #1d4ed8; border-radius: 10px; padding: 0.55rem 1rem;
}
.pol .pol-btn:hover { background: #2563eb; color: #fff; }
</style>

<div class="pol">
<section class="pol-hero">
<div class="pol-wash" aria-hidden="true"></div>
<div class="pol-bar" aria-hidden="true"><span></span><span></span><span></span><span></span><span></span><span></span></div>
<div class="pol-top">
<div>
<p class="pol-kicker">Institutii · Politia</p>
<h1>Politia <span>Los Santos</span></h1>
<p class="pol-lede">Patrulezi, raspunzi la apeluri, opresti masini si duci suspectii la inchisoare. Lucrezi in tura, cu statia pe frecventa politiei si tableta MDT la tine.</p>
</div>
<svg class="pol-badge" viewBox="0 0 120 140" role="img" aria-label="Insigna politiei">
<defs>
<linearGradient id="pol-glint" x1="0" x2="1" y1="0" y2="0">
<stop offset="0" stop-color="#fff" stop-opacity="0"/>
<stop offset="0.5" stop-color="#fff" stop-opacity="0.35"/>
<stop offset="1" stop-color="#fff" stop-opacity="0"/>
</linearGradient>
<clipPath id="pol-clip"><path d="M60 6 L108 22 V64 C108 98 86 122 60 134 C34 122 12 98 12 64 V22 Z"/></clipPath>
</defs>
<path class="shield" d="M60 6 L108 22 V64 C108 98 86 122 60 134 C34 122 12 98 12 64 V22 Z"/>
<path class="inner" d="M60 16 L99 29 V64 C99 92 81 112 60 123 C39 112 21 92 21 64 V29 Z"/>
<path class="star" d="M60 40 L66.5 56 L83 57 L70 67.5 L74.5 84 L60 74.8 L45.5 84 L50 67.5 L37 57 L53.5 56 Z"/>
<text class="txt" x="60" y="104" text-anchor="middle">POLITIA</text>
<g clip-path="url(#pol-clip)"><rect class="glint" x="0" y="0" width="60" height="140"/></g>
</svg>
</div>
<ul class="pol-stats">
<li><b>8 grade</b><span>de la Cadet la Chestor General</span></li>
<li><b>120 luni</b><span>pedeapsa maxima; o luna trece intr-un minut real</span></li>
<li><b>10 frecvente</b><span>de statie doar pentru politie, plus 5 comune cu SMIR</span></li>
</ul>
</section>
<h2 class="pol-h2" id="cum-intri">Cum intri in politie</h2>
<p class="pol-sub">Politia nu are angajare la ghiseu. Treci printr-un interviu si te angajeaza conducerea, in joc, fata in fata.</p>
<ol class="pol-road">
<li><h3 class="pol-h3">Pregateste-te</h3><p>Ai minim 17 ani, stii regulile de roleplay si regulamentul politiei. Ai cazierul curat, iti asumi greselile si stii sa lucrezi in echipa.</p></li>
<li><h3 class="pol-h3">Interviul</h3><p>Conducerea te testeaza la interviu. Prima impresie conteaza: vino pregatit si calm, ca la un post adevarat.</p></li>
<li><h3 class="pol-h3">Angajarea</h3><p>Chestorul General te angajeaza de la computerul din sediu, cu tine langa el (cel mult 10 m). Incepi ca <b>Cadet</b>.</p></li>
</ol>
<div class="pol-card pol-check">
<h3 class="pol-h3">Ce verifica jocul cand esti angajat</h3>
<ul class="pol-list">
<li>Daca ai peste <b>25 de caziere in ultimele 3 luni</b>, nu poti fi angajat. Se numara si cazierele platite sau sterse.</li>
<li>Daca ai plecat de curand din politie sau dintr-o factiune, astepti <b>7 zile</b> (daca ai stat acolo cel putin 30 de zile) sau <b>14 zile</b>.</li>
<li>Cat timp esti membru intr-o factiune (in afara de SIS), nu poti intra in politie.</li>
<li>Conducerea tine o lista neagra: cine e pe ea nu poate fi angajat.</li>
</ul>
</div>
<h2 class="pol-h2" id="grade">Grade</h2>
<p class="pol-sub">Fiecare grad iti deblocheaza ceva in plus. Masinile din garaj se deblocheaza tot pe grade.</p>
<ol class="pol-ladder">
<li><span class="n">1</span><span class="t">Cadet</span><span class="d">Primesti tableta MDT. In incidente poti trece doar contraventii.</span></li>
<li><span class="n">2</span><span class="t">Agent</span><span class="d">Poti trece si infractiuni in MDT.</span></li>
<li><span class="n">3</span><span class="t">Agent Principal</span><span class="d">Acelasi acces ca Agentul, cu mai multa experienta pe teren.</span></li>
<li><span class="n">4</span><span class="t">Agent Sef</span><span class="d">Publici anunturi in MDT si setezi indicativele colegilor.</span></li>
<li><span class="n">5</span><span class="t">Inspector</span><span class="d">Scoti obiecte din evidenta, trimiti coduri radio fara pauza, trimiti notificari colegilor si planifici transporturi de persoane.</span></li>
<li class="boss"><span class="n">6</span><span class="t">Comisar<span class="tag">conducere</span></span><span class="d">Creezi unitati in dispecerat, planifici transporturi de armament si trimiti SMS-uri publice.</span></li>
<li class="boss"><span class="n">7</span><span class="t">Comisar Sef<span class="tag">conducere</span></span><span class="d">Deschizi computerul din sediu: vezi personalul, pontajul si cheltuielile si schimbi gradul colegilor sub tine.</span></li>
<li class="boss"><span class="n">8</span><span class="t">Chestor General<span class="tag">conducere</span></span><span class="d">Angajezi, promovezi si concediezi, administrezi flota, armuraria, codul penal si mandatele.</span></li>
</ol>
<h2 class="pol-h2" id="tura">Tura</h2>
<div class="pol-grid">
<div class="pol-card">
<h3 class="pol-h3">Unde intri in tura</h3>
<ul class="pol-list">
<li>La punctul de tura din sectia din Vespucci, cu <kbd>E</kbd>.</li>
<li>La seful de la sectie (Vespucci, Penitenciar, Sandy Shores): <b>Incepe tura</b> iti pune si uniforma, <b>Termina tura</b> iti da hainele inapoi.</li>
<li>Tot la sef iti alegi uniforma sau o tinuta salvata.</li>
<li>La fiecare logare intri in joc in afara turei.</li>
</ul>
</div>
<div class="pol-card">
<h3 class="pol-h3">Ce ai doar in tura</h3>
<ul class="pol-list">
<li>Salariul: in afara turei nu esti platit.</li>
<li>Frecventele de statie ale politiei si cele comune cu SMIR.</li>
<li>Catusele din comanda, inchisoarea, placajul si codurile radio.</li>
<li>Apelurile cetatenilor si alertele din dispecerat.</li>
<li>Puncte in pontaj: 3 pentru o trimitere la inchisoare, 1 pentru un incident sau un raport in MDT.</li>
</ul>
</div>
<div class="pol-card">
<h3 class="pol-h3">Indicativul si harta</h3>
<p>Iti setezi numarul matricol cu <code>/callsign numar</code> (0 - 9999). Colegii il vad pe harta, langa punctul tau.</p>
<p>Pe harta apari si ii vezi pe colegi (si pe medicii SMIR din tura) doar daca ai la tine un <b>Tracker GPS</b> care nu e bruiat.</p>
</div>
</div>
<h2 class="pol-h2" id="echipament">Echipament</h2>
<p class="pol-sub">Iti iei echipamentul de la <b>Armurarie Politie</b>, in sectia din Vespucci, la Penitenciar si in Sandy Shores. Gasesti acolo armele, munitia, atasamentele, vestele si obiectele de mai jos.</p>
<ul class="pol-gear">
<li><b>Tableta MDT</b><span>Cazierele, incidentele, amenzile, mandatele si dispeceratul.</span></li>
<li><b>Catuse</b><span>Necesare ca sa incatusezi pe cineva.</span></li>
<li><b>Berbec</b><span>Sparge o usa incuiata. Se uzeaza la fiecare usa si se strica in timp.</span></li>
<li><b>Benzi cu cuie</b><span>Le asezi pe drum si sparg rotile. Maxim 5 puse odata; le ridici tinand apasat <kbd>H</kbd>.</span></li>
<li><b>Scut balistic</b><span>Il tii in mana sau il asezi pe sol cu <kbd>H</kbd>; il strangi cu <kbd>F5</kbd>.</span></li>
<li><b>Etilotest</b><span>Masoara alcoolul si scoate bonul tiparit. Foloseste piese bucale.</span></li>
<li><b>Kit test antidrog</b><span>Arata ce substante are in sange cel mai apropiat jucator.</span></li>
<li><b>Scanner amprente</b><span>Identifica persoana dupa amprenta.</span></li>
<li><b>Buton de panica</b><span>Fara el nu poti trimite codurile radio.</span></li>
<li><b>Tracker GPS</b><span>Te arata pe harta colegilor si ti-i arata pe ei.</span></li>
<li><b>Body Camera</b><span>Cat o ai la tine, pe HUD apare indicatorul REC.</span></li>
<li><b>Radio si legitimatie</b><span>Statia pentru frecvente si Legitimatia de politie.</span></li>
</ul>
<p class="pol-note">Cine are un detector de electronice iti poate lua camera, trackerul si butonul de panica. Fara ele dispari de pe harta colegilor si nu mai poti trimite coduri.</p>
<h2 class="pol-h2" id="interventii">Interventii pe teren</h2>
<p class="pol-sub">Majoritatea actiunilor le faci tintind jucatorul (ox_target) sau din meniul radial, cu <kbd>K</kbd> → <b>Politie</b>.</p>
<ul class="pol-acts">
<li><span class="a">Incatusare</span><span class="h">Tintesti jucatorul → <b>Pune catusele</b> (ai nevoie de catuse in inventar), sau <code>/cuff</code> pe cel mai apropiat. <code>/sc</code> pune catuse usoare. Cineva cu un advanced lockpick ii poate scoate catusele.</span></li>
<li><span class="a">Escorta</span><span class="h">Tintesti un jucator incatusat → <b>Escorteaza</b> (sau <code>/escort</code>). Suspectul poate incerca de 2 ori sa scape, cu un test de reflexe.</span></li>
<li><span class="a">In masina</span><span class="h">Cu suspectul escortat, te duci la o usa a masinii si tii apasat <kbd>H</kbd>: <b>Pune in masina</b>. La fel il scoti.</span></li>
<li><span class="a">Placaj</span><span class="h"><kbd>Shift</kbd> + <kbd>G</kbd> langa un jucator, doar in tura. El se poate opune.</span></li>
<li><span class="a">Punga pe cap</span><span class="h">Tintesti jucatorul → <b>Pune punga</b>, cu o Punga de pus in cap in inventar. Il lasa fara vedere pana i-o scoti.</span></li>
<li><span class="a">Inchisoare</span><span class="h">Din zona inchisorii (celulele din Vespucci sau Penitenciarul): <code>/jail</code> sau <kbd>K</kbd> → Politie → <b>Sentinta inchisoare</b>. Alegi 1 - 120 de luni pentru cel mai apropiat jucator. <code>/unjail ID</code> il elibereaza.</span></li>
<li><span class="a">Amenda</span><span class="h">Din MDT, pe incident. Poti da reducere (25 - 90%) si puncte pe permis. Punctele se aduna pana la 15 si se sterg toate la 6 zile dupa prima amenda cu puncte.</span></li>
<li><span class="a">Retinere acte</span><span class="h"><kbd>K</kbd> → Politie → <b>Retine permis</b> sau <b>Retine talon</b>: alegi jucatorul si durata, intre 1 si 720 de ore.</span></li>
<li><span class="a">Ridicare masina</span><span class="h">Din MDT marchezi masina pentru ridicare, stand la cel mult 10 m de ea. Un mecanic preia comanda si o duce la parcare.</span></li>
<li><span class="a">Berbec</span><span class="h">Folosesti berbecul langa o usa incuiata; dupa lovituri, usa se descuie.</span></li>
<li><span class="a">Supraveghere</span><span class="h"><kbd>K</kbd> → Politie → <b>Camere de supraveghere</b> (sau Telefon → Supraveghere): camerele din banci, magazine si bijuterii.</span></li>
<li><span class="a">Obiecte pe drum</span><span class="h"><kbd>K</kbd> → Politie → <b>Obiecte</b>: conuri, bariere, semn de stop, lumini.</span></li>
</ul>
<p class="pol-note">In inchisoare, cine loveste de 10 ori alti detinuti primeste inca 5 luni. Cine iese din zona e adus inapoi de gardieni.</p>
<h2 class="pol-h2" id="mdt">Tableta MDT si dispeceratul</h2>
<div class="pol-grid">
<div class="pol-card">
<h3 class="pol-h3">Ce gasesti in MDT</h3>
<p><b>Bord</b> (colegi in tura, anunturi, persoane si masini cautate), <b>Profiluri</b>, <b>Incidente</b>, <b>Rapoarte</b>, <b>Plangeri</b>, <b>Vehicule</b>, <b>Dispecerat</b>, <b>Mandate</b>, <b>Transporturi</b>, <b>Top caziere</b>, <b>Lista</b> efectivului si <b>Acuzatii</b> (codul penal).</p>
<p>De pe incident poti tipari un <b>Proces verbal</b> pe hartie si i-l dai persoanei de langa tine.</p>
</div>
<div class="pol-card">
<h3 class="pol-h3">Apeluri si alerte</h3>
<ul class="pol-list">
<li>Codurile de urgenta ale colegilor si ale medicilor apar ca alerte pe ecran si pe harta. Tii apasat <kbd>Enter</kbd> ca sa raspunzi; <kbd>↑</kbd> / <kbd>↓</kbd> schimba alerta selectata.</li>
<li>Apelurile cetatenilor din Telefon → Servicii le deschizi cu <kbd>F7</kbd>.</li>
<li>In dispecerat va grupati pe unitati.</li>
</ul>
</div>
</div>
<h3 class="pol-h3" style="margin-top:1.2rem">Coduri de urgenta</h3>
<p class="pol-sub">Le trimiti cu <code>/cod0</code> ... <code>/cod4</code>, in tura si cu butonul de panica la tine. Sub gradul de Inspector ai 5 secunde pauza intre doua coduri.</p>
<ul class="pol-codes">
<li class="em"><b>Cod 0</b>Urgenta majora, cu sirena si girofar</li>
<li class="em"><b>Cod 1</b>Interventie urgenta, cu sirena si girofar</li>
<li><b>Cod 2</b>Asistenta standard, doar girofar</li>
<li><b>Cod 3</b>E nevoie de ingrijiri medicale (ajunge si la SMIR)</li>
<li><b>Cod 4</b>Zona libera</li>
<li><b>Cod 5</b>Echipajul SMIR are o urgenta (trimis de medici)</li>
</ul>
<h3 class="pol-h3" style="margin-top:1.2rem">Coduri de statie</h3>
<p class="pol-sub"><code>/coduripolitie</code> iti arata lista pe ecran (o mai scrii o data ca s-o inchizi).</p>
<ul class="pol-codes">
<li><b>10-0</b>Suspect pierdut</li>
<li><b>10-1</b>Schimbare frecventa radio</li>
<li><b>10-2</b>Cerere permisiune depasire</li>
<li><b>10-4</b>Receptionat</li>
<li><b>10-8</b>Patrula</li>
<li><b>10-9</b>Repeta</li>
<li><b>10-11</b>Focuri de arma</li>
<li><b>10-16</b>Vehicul fara numar de inmatriculare</li>
<li><b>10-20</b>Locatia curenta</li>
<li><b>10-23</b>Ajuns la destinatie</li>
<li><b>10-28</b>Numar de inmatriculare</li>
<li><b>10-38</b>Oprire in trafic</li>
<li><b>10-50</b>Accident</li>
<li><b>10-60</b>Livrare in progres</li>
<li><b>10-76</b>In drum spre</li>
<li><b>10-77</b>Necesit echipaje aditionale</li>
<li><b>10-80</b>Urmarire in desfasurare</li>
<li><b>10-95</b>Suspect in custodie</li>
</ul>
<h2 class="pol-h2" id="vehicule">Vehicule</h2>
<div class="pol-grid">
<div class="pol-card">
<h3 class="pol-h3">Garajele politiei</h3>
<p>Ai garaje de masini la sectii, heliporturi, garaje de avioane si de barci. Ce modele scoti depinde de grad; flota o stabileste Chestorul General.</p>
<p>Masina scoasa din garaj vine cu blindaj maxim, iar piesele nu i se uzeaza cat timp e scoasa.</p>
</div>
<div class="pol-card">
<h3 class="pol-h3">Girofar si sirena</h3>
<ul class="pol-list">
<li><kbd>[</kbd> porneste sau opreste girofarul.</li>
<li><kbd>]</kbd> porneste sau opreste sirena; <kbd>R</kbd> schimba tonul.</li>
<li><kbd>Y</kbd> deschide telecomanda radarului din masina (viteza si numerele masinilor din fata si din spate).</li>
</ul>
</div>
<div class="pol-card">
<h3 class="pol-h3">Elicopterul</h3>
<p>In elicopterul politiei: <kbd>E</kbd> camera, <kbd>X</kbd> cobori pe franghie, <kbd>H</kbd> reflectorul. In camera, click dreapta schimba vederea (noapte, termic).</p>
</div>
</div>
<h2 class="pol-h2" id="sediu">La sectia din Vespucci</h2>
<div class="pol-grid">
<div class="pol-card">
<h3 class="pol-h3">Evidenta</h3>
<p>Dulapurile de evidenta sunt la Vespucci, la Penitenciar si in Sandy Shores. Orice politist pune obiecte in ele; doar de la Inspector in sus le poate scoate. Fiecare miscare se inregistreaza.</p>
</div>
<div class="pol-card">
<h3 class="pol-h3">Pentru cetateni</h3>
<p>Functionarul de la <b>Licente arme</b> iti da sau iti reinnoieste licenta de port arma si iti trece arma pe ea.</p>
<p><b>Ofiterul de serviciu</b> iti arata cazierele si iti sterge un incident, contra cost.</p>
</div>
</div>
<h2 class="pol-h2" id="taste">Taste si comenzi</h2>
<div class="pol-card">
<ul class="pol-keys">
<li><kbd>K</kbd> meniul radial → Politie</li>
<li><kbd>Shift</kbd> + <kbd>G</kbd> placaj</li>
<li><kbd>F7</kbd> apelurile cetatenilor</li>
<li><kbd>Enter</kbd> (tinut) raspunzi la alerta</li>
<li><kbd>[</kbd> / <kbd>]</kbd> girofar / sirena</li>
<li><kbd>Y</kbd> radarul din masina</li>
<li><code>/cuff</code> <code>/sc</code> catuse</li>
<li><code>/escort</code> escorta</li>
<li><code>/jail</code> <code>/unjail ID</code> inchisoare</li>
<li><code>/callsign</code> numarul matricol</li>
<li><code>/cod0</code> - <code>/cod4</code> coduri</li>
<li><code>/coduripolitie</code> codurile de statie</li>
</ul>
</div>
<div class="pol-rules">
<p>Regulile de patrula, razii, urmariri si folosirea fortei sunt in regulamentul politiei. Il citesti inainte de interviu.</p>
<a class="pol-btn" href="/zona-info/regulament-politie">Regulament Politie</a>
</div>
</div>
