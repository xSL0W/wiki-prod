---
outline: false
---

<style>
.tng {
  --ink: #0b0b0d;
  --panel: #151517;
  --panel2: #1d1d20;
  --line: #2f2f35;
  --text: #f4f4f5;
  --mute: #a1a1aa;
  --red: #dc2626;
  --red2: #ef4444;
  --amber: #f59e0b;
  --carbon: repeating-linear-gradient(45deg, rgba(255, 255, 255, 0.022) 0 2px, transparent 2px 6px), repeating-linear-gradient(-45deg, rgba(0, 0, 0, 0.28) 0 2px, transparent 2px 6px), #111113;
  max-width: 980px;
  margin: 0 auto;
  color: var(--text);
}
.tng *, .tng *::before, .tng *::after { box-sizing: border-box; }
.tng p, .tng li { margin: 0; line-height: 1.6; color: var(--text); }
.tng ul, .tng ol { list-style: none; padding: 0; margin: 0; }
.tng li + li { margin-top: 0; }
.tng b { color: #fff; font-weight: 650; }
.tng kbd {
  display: inline-block; min-width: 1.6em; padding: 0.05rem 0.45rem; border-radius: 6px; text-align: center;
  font: 700 0.82em ui-monospace, Menlo, Consolas, monospace; color: #fff;
  background: var(--panel2); border: 1px solid var(--line); border-bottom-width: 3px;
}
.tng a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.tng a:hover { color: #fecaca; }
.tng a:focus-visible { outline: 3px solid var(--amber); outline-offset: 3px; border-radius: 6px; }
/* group nav (shared by the Tuning pages) */
.tng .tng-group { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1rem; }
.tng .tng-group a {
  display: inline-flex; align-items: center; gap: 0.55rem; text-decoration: none; color: var(--mute);
  background: var(--panel); border: 1px solid var(--line); border-radius: 10px; padding: 0.35rem 0.85rem 0.35rem 0.4rem;
  font-weight: 700; font-size: 0.9rem;
}
.tng .tng-group a span { font: 800 0.75rem ui-monospace, Menlo, Consolas, monospace; color: var(--ink); background: var(--mute); border-radius: 6px; padding: 0.1rem 0.35rem; }
.tng .tng-group a:hover { color: #fff; border-color: var(--red); }
.tng .tng-group a[aria-current="page"] { color: #fff; border-color: var(--red); background: rgba(220, 38, 38, 0.12); }
.tng .tng-group a[aria-current="page"] span { background: var(--red); color: #fff; }
/* hero */
.tng .tng-hero {
  position: relative; overflow: hidden; border: 1px solid var(--line); border-radius: 22px;
  background: radial-gradient(80% 110% at 100% 0%, rgba(220, 38, 38, 0.22), transparent 60%), var(--carbon);
  padding: clamp(1.25rem, 4vw, 2.4rem); padding-top: calc(clamp(1.25rem, 4vw, 2.4rem) + 12px);
}
.tng .tng-hero::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 12px;
  background: conic-gradient(#e4e4e7 0 25%, #0b0b0d 0 50%, #e4e4e7 0 75%, #0b0b0d 0) 0 0 / 12px 12px; opacity: 0.85;
}
.tng .tng-hero-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 300px), 1fr)); gap: 1.5rem; align-items: center; }
.tng .tng-kicker { font: 800 0.75rem ui-monospace, Menlo, Consolas, monospace; letter-spacing: 0.16em; text-transform: uppercase; color: var(--amber); margin-bottom: 0.6rem; }
.tng .tng-hero h1 {
  margin: 0 0 0.8rem; border: 0; padding: 0; font-style: italic;
  font-size: clamp(2.4rem, 8vw, 3.6rem); line-height: 1; font-weight: 900; letter-spacing: -0.035em; color: #fff;
}
.tng .tng-hero h1 em { font-style: italic; color: var(--red2); }
.tng .tng-lede { color: var(--mute); font-size: 1.05rem; max-width: 46ch; }
.tng .tng-cta { display: flex; flex-wrap: wrap; gap: 0.55rem; margin-top: 1.2rem; }
.tng .tng-cta a { text-decoration: none; border-radius: 8px; padding: 0.45rem 0.95rem; font-weight: 800; color: #fff; background: var(--red); transform: skewX(-8deg); }
.tng .tng-cta a:hover { background: var(--red2); color: #fff; }
.tng .tng-cta a.alt { background: transparent; border: 1px solid var(--line); }
.tng .tng-cta a.alt:hover { border-color: var(--amber); }
.tng .tng-art { display: block; width: 100%; max-width: 420px; height: auto; margin: 0 auto; }
.tng-art .body { fill: #1c1c20; stroke: #e4e4e7; stroke-width: 2.2; stroke-linejoin: round; }
.tng-art .glass { fill: rgba(161, 161, 170, 0.18); stroke: #a1a1aa; stroke-width: 1.4; }
.tng-art .stripe { fill: none; stroke: var(--red); stroke-width: 5; stroke-linecap: round; stroke-dasharray: 260; stroke-dashoffset: 260; animation: tng-draw 0.9s ease-out 1.5s forwards; }
.tng-art .part { fill: var(--red); stroke: #fca5a5; stroke-width: 1; opacity: 0; }
.tng-art .wing { animation: tng-drop 0.5s cubic-bezier(0.3, 1.6, 0.5, 1) 0.4s forwards; }
.tng-art .split { animation: tng-slide 0.5s cubic-bezier(0.3, 1.6, 0.5, 1) 0.8s forwards; }
.tng-art .skirt { animation: tng-rise 0.5s cubic-bezier(0.3, 1.6, 0.5, 1) 1.1s forwards; }
.tng-art .tyre { fill: #0b0b0d; stroke: #3f3f46; stroke-width: 5; }
.tng-art .rim { fill: none; stroke: var(--amber); stroke-width: 2.5; }
.tng-art .spokes { stroke: var(--amber); stroke-width: 3; stroke-linecap: round; transform-box: fill-box; transform-origin: center; animation: tng-spin 0.55s linear infinite; }
.tng-art .roller { fill: #27272a; stroke: #3f3f46; stroke-width: 1.5; }
.tng-art .floor { stroke: #3f3f46; stroke-width: 2; stroke-dasharray: 10 8; animation: tng-floor 0.5s linear infinite; }
.tng-art .arc { fill: none; stroke: #3f3f46; stroke-width: 9; stroke-linecap: round; }
.tng-art .arc.hot { stroke: var(--red); stroke-dasharray: 34 300; stroke-dashoffset: -112; }
.tng-art .needle { stroke: #fff; stroke-width: 3.5; stroke-linecap: round; transform-origin: 340px 40px; animation: tng-rev 2.4s ease-in-out infinite; }
.tng-art .hub { fill: var(--red); }
.tng-art .lbl { fill: var(--mute); font: 700 10px ui-monospace, Menlo, Consolas, monospace; letter-spacing: 0.08em; }
@keyframes tng-draw { to { stroke-dashoffset: 0; } }
@keyframes tng-drop { from { opacity: 0; transform: translateY(-34px); } to { opacity: 1; transform: none; } }
@keyframes tng-slide { from { opacity: 0; transform: translateX(34px); } to { opacity: 1; transform: none; } }
@keyframes tng-rise { from { opacity: 0; transform: translateY(18px); } to { opacity: 1; transform: none; } }
@keyframes tng-spin { to { transform: rotate(360deg); } }
@keyframes tng-floor { to { stroke-dashoffset: 18; } }
@keyframes tng-rev { 0%, 100% { transform: rotate(-60deg); } 40% { transform: rotate(55deg); } 55% { transform: rotate(40deg); } 75% { transform: rotate(62deg); } }
.tng .tng-facts { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 130px), 1fr)); gap: 0.6rem; margin-top: 1.4rem; }
.tng .tng-facts li { background: rgba(11, 11, 13, 0.7); border: 1px solid var(--line); border-left: 3px solid var(--red); border-radius: 10px; padding: 0.7rem 0.9rem; }
.tng .tng-facts b { display: block; font: 900 1.55rem/1.1 ui-monospace, Menlo, Consolas, monospace; color: #fff; font-style: italic; }
.tng .tng-facts span { color: var(--mute); font-size: 0.9rem; }
/* section heads */
.tng .tng-h2 {
  display: flex; align-items: flex-start; gap: 0.7rem; margin: 3rem 0 0.9rem; line-height: 32px; border: 0; padding: 0;
  font-size: 1.45rem; font-weight: 850; letter-spacing: -0.015em; color: #fff; font-style: italic;
}
.tng .tng-h2 span { flex: none; font: 800 0.8rem ui-monospace, Menlo, Consolas, monospace; font-style: normal; color: #fff; background: var(--red); border-radius: 6px; padding: 0.15rem 0.45rem; transform: skewX(-10deg); margin-top: 6px; }
.tng .tng-sub { color: var(--mute); margin: -0.3rem 0 1rem; max-width: 66ch; }
.tng .tng-card { background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 1rem 1.15rem; }
.tng .tng-card h3 { margin: 0 0 0.45rem; border: 0; padding: 0; font-size: 1.02rem; font-weight: 800; color: #fff; }
.tng .tng-card p { color: var(--mute); font-size: 0.95rem; }
.tng .tng-card p + p { margin-top: 0.5rem; }
/* where */
.tng .tng-shops { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 150px), 1fr)); gap: 0.55rem; }
.tng .tng-shops li { background: var(--panel); border: 1px solid var(--line); border-radius: 10px; padding: 0.6rem 0.8rem; font-weight: 700; }
.tng .tng-shops li small { display: block; font-weight: 500; color: var(--mute); font-size: 0.8rem; }
.tng .tng-shops li.dyno { border-color: rgba(245, 158, 11, 0.55); }
.tng .tng-shops li.dyno small { color: var(--amber); }
.tng .tng-how { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 240px), 1fr)); gap: 0.7rem; margin-top: 0.8rem; }
/* who */
.tng .tng-who { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 230px), 1fr)); gap: 0.7rem; }
.tng .tng-who .tng-card { border-top: 3px solid var(--red); }
.tng .tng-who .tng-card.amber { border-top-color: var(--amber); }
.tng .tng-who .tng-card.grey { border-top-color: #71717a; }
/* menu tree */
.tng .tng-menu { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 250px), 1fr)); gap: 0.7rem; }
.tng .tng-menu .tng-card h3 { display: flex; justify-content: space-between; gap: 0.5rem; align-items: baseline; }
.tng .tng-menu .tng-card h3 small { font: 700 0.72rem ui-monospace, Menlo, Consolas, monospace; color: var(--mute); text-transform: uppercase; letter-spacing: 0.1em; }
.tng .tng-chips { display: flex; flex-wrap: wrap; gap: 0.35rem; margin-top: 0.4rem; }
.tng .tng-chips li { background: var(--panel2); border: 1px solid var(--line); border-radius: 7px; padding: 0.12rem 0.55rem; font-size: 0.86rem; color: var(--text); }
.tng .tng-keys { display: flex; flex-wrap: wrap; gap: 0.5rem 1.1rem; margin-top: 0.9rem; padding: 0.8rem 1rem; border: 1px dashed var(--line); border-radius: 12px; color: var(--mute); font-size: 0.92rem; }
/* dyno chart */
.tng .tng-dyno { background: var(--carbon); border: 1px solid var(--line); border-radius: 16px; padding: 1.1rem 1.2rem; }
.tng .tng-bars li { display: grid; grid-template-columns: minmax(7.5rem, 11rem) 1fr 4.2rem; gap: 0.6rem; align-items: center; padding: 0.35rem 0; }
.tng .tng-bars li + li { border-top: 1px solid rgba(63, 63, 70, 0.45); }
.tng .tng-bars .name { font-weight: 700; font-size: 0.93rem; }
.tng .tng-bars .name small { display: block; font-weight: 500; color: var(--mute); font-size: 0.78rem; }
.tng .tng-bars .track { height: 12px; border-radius: 3px; background: repeating-linear-gradient(90deg, #27272a 0 10px, #1d1d20 10px 12px); overflow: hidden; }
.tng .tng-bars .fill { display: block; height: 100%; width: var(--w); background: linear-gradient(90deg, var(--amber), var(--red)); transform-origin: left; animation: tng-fill 1.1s cubic-bezier(0.2, 0.8, 0.2, 1) both; }
.tng .tng-bars .val { font: 800 0.95rem ui-monospace, Menlo, Consolas, monospace; text-align: right; color: #fff; }
@keyframes tng-fill { from { transform: scaleX(0); } to { transform: scaleX(1); } }
.tng .tng-turbo { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 200px), 1fr)); gap: 0.6rem; margin-top: 0.9rem; }
.tng .tng-turbo li { background: var(--panel); border: 1px solid var(--line); border-radius: 12px; padding: 0.7rem 0.9rem; color: var(--mute); font-size: 0.88rem; }
.tng .tng-turbo li b { display: flex; justify-content: space-between; align-items: baseline; gap: 0.5rem; color: #fff; font-size: 0.98rem; }
.tng .tng-turbo li b i { font: 800 0.9rem ui-monospace, Menlo, Consolas, monospace; font-style: normal; color: var(--amber); }
.tng .tng-note { margin-top: 0.8rem; color: var(--mute); font-size: 0.92rem; }
/* two col */
.tng .tng-two { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr)); gap: 0.7rem; }
.tng .tng-list li { position: relative; padding: 0.45rem 0 0.45rem 1.2rem; color: var(--mute); }
.tng .tng-list li + li { border-top: 1px solid var(--line); }
.tng .tng-list li::before { content: ''; position: absolute; left: 0; top: 0.95rem; width: 8px; height: 8px; background: var(--red); transform: skewX(-15deg); }
.tng .tng-list li b { color: #fff; }
.tng .tng-steps { counter-reset: tng; display: grid; gap: 0.5rem; }
.tng .tng-steps li { counter-increment: tng; position: relative; padding: 0.6rem 0.9rem 0.6rem 3rem; background: var(--panel); border: 1px solid var(--line); border-radius: 12px; color: var(--mute); }
.tng .tng-steps li::before { content: counter(tng); position: absolute; left: 0.75rem; top: 0.55rem; width: 1.6rem; height: 1.6rem; display: grid; place-items: center; font: 900 0.85rem ui-monospace, Menlo, Consolas, monospace; color: #fff; background: var(--red); border-radius: 6px; transform: skewX(-10deg); }
.tng .tng-steps li b { color: #fff; }
.tng .tng-sliders { display: flex; flex-wrap: wrap; gap: 0.35rem; margin: 0.6rem 0; }
.tng .tng-sliders li { font: 600 0.8rem ui-monospace, Menlo, Consolas, monospace; color: var(--amber); border: 1px solid rgba(245, 158, 11, 0.4); border-radius: 999px; padding: 0.1rem 0.6rem; }
.tng .tng-warn { border-left: 4px solid var(--amber); }
.tng .tng-foot { margin-top: 2.5rem; padding: 1rem 1.2rem; border: 1px dashed var(--line); border-radius: 14px; color: var(--mute); }
@media (max-width: 520px) {
  .tng .tng-bars li { grid-template-columns: 1fr 3.8rem; }
  .tng .tng-bars .track { grid-column: 1 / -1; grid-row: 2; }
}
@media (prefers-reduced-motion: reduce) {
  .tng-art .stripe, .tng-art .part, .tng-art .spokes, .tng-art .floor, .tng-art .needle, .tng .tng-bars .fill { animation: none; }
  .tng-art .stripe { stroke-dashoffset: 0; }
  .tng-art .part { opacity: 1; }
  .tng-art .needle { transform: rotate(40deg); }
}
</style>
<div class="tng">
<nav class="tng-group" aria-label="Pagini tuning">
<a href="/general/tuning" aria-current="page"><span>01</span>Tuning</a>
<a href="/general/antilag"><span>02</span>Antilag</a>
<a href="/general/offroad"><span>03</span>Offroad</a>
</nav>
<section class="tng-hero">
<div class="tng-hero-grid">
<div>
<p class="tng-kicker">Garaj · Piese · Dyno</p>
<h1>Tuning <em>la service</em></h1>
<p class="tng-lede">Duci masina la un atelier de tuning, te urci la volan si alegi piesele din meniu. Vezi fiecare piesa pe masina inainte s-o cumperi, iar tot ce cumperi ramane salvat pe masina.</p>
<div class="tng-cta">
<a href="#tng-unde">Unde tunezi</a>
<a class="alt" href="#tng-perf">Performanta</a>
<a class="alt" href="#tng-stancer">Stancer</a>
</div>
</div>
<svg class="tng-art" viewBox="0 0 420 190" role="img" aria-label="Masina pe dyno: piesele se monteaza pe rand, rotile se invart, acul turometrului urca">
<g>
<path class="arc" d="M 312 52 A 32 32 0 1 1 368 52"/>
<path class="arc hot" d="M 312 52 A 32 32 0 1 1 368 52"/>
<line class="needle" x1="340" y1="40" x2="340" y2="16"/>
<circle class="hub" cx="340" cy="40" r="4.5"/>
<text class="lbl" x="322" y="72">RPM</text>
</g>
<line class="floor" x1="0" y1="174" x2="420" y2="174"/>
<ellipse class="roller" cx="110" cy="166" rx="34" ry="7"/>
<ellipse class="roller" cx="300" cy="166" rx="34" ry="7"/>
<path class="body" d="M30 132 L40 114 Q60 106 110 102 L150 80 Q170 70 210 69 L250 70 Q280 72 305 96 L350 104 Q372 108 374 122 L374 134 Q374 138 368 138 L330 138 A30 30 0 0 0 270 138 L140 138 A30 30 0 0 0 80 138 L36 138 Q30 138 30 132 Z"/>
<path class="glass" d="M160 84 Q172 76 208 75 L246 76 Q266 78 284 96 L160 98 Z"/>
<line x1="222" y1="76" x2="222" y2="98" stroke="#a1a1aa" stroke-width="1.4"/>
<path class="stripe" d="M44 118 Q120 108 160 104 L300 102 Q345 106 368 116"/>
<g class="part wing"><rect x="34" y="88" width="58" height="6" rx="2"/><rect x="56" y="94" width="5" height="13"/></g>
<rect class="part split" x="330" y="137" width="48" height="5" rx="2"/>
<rect class="part skirt" x="142" y="136" width="126" height="5" rx="2"/>
<g><circle class="tyre" cx="110" cy="138" r="23"/><circle class="rim" cx="110" cy="138" r="14"/><g class="spokes"><line x1="110" y1="125" x2="110" y2="151"/><line x1="97" y1="138" x2="123" y2="138"/><line x1="101" y1="129" x2="119" y2="147"/><line x1="119" y1="129" x2="101" y2="147"/></g></g>
<g><circle class="tyre" cx="300" cy="138" r="23"/><circle class="rim" cx="300" cy="138" r="14"/><g class="spokes"><line x1="300" y1="125" x2="300" y2="151"/><line x1="287" y1="138" x2="313" y2="138"/><line x1="291" y1="129" x2="309" y2="147"/><line x1="309" y1="129" x2="291" y2="147"/></g></g>
</svg>
</div>
<ul class="tng-facts">
<li><b>6</b><span>service-uri cu atelier de tuning</span></li>
<li><b>3</b><span>sectiuni in meniu: Reparatii, Aspect, Performanta</span></li>
<li><b>4</b><span>trepte de turbina</span></li>
<li><b>82</b><span>culori chameleon</span></li>
</ul>
</section>
<h2 class="tng-h2" id="tng-unde"><span>01</span>Unde tunezi</h2>
<p class="tng-sub">Atelierele de tuning apar pe harta cu numele <b>Tuning</b>. Service-urile le gasesti si in <b>Telefon → Harti → Service-uri auto</b>. Fiecare service e o firma de mecanici: <a href="/afaceri/service">Service auto</a>.</p>
<ul class="tng-shops">
<li class="dyno">Strawberry<small>tuning + dyno</small></li>
<li class="dyno">Burton<small>tuning + dyno</small></li>
<li class="dyno">East Vinewood<small>tuning + dyno</small></li>
<li class="dyno">Murrieta Heights<small>tuning + dyno</small></li>
<li>Cypress Flats<small>tuning</small></li>
<li>Grapeseed<small>tuning</small></li>
</ul>
<div class="tng-how">
<div class="tng-card">
<h3>Ateliere fara firma</h3>
<p>Barcile se tuneaza in port, avioanele la aeroportul din Los Santos. Pe Cayo Perico ai un atelier pentru masini si unul pentru avioane. Mai e un atelier langa sectia de politie din Vespucci.</p>
</div>
<div class="tng-card">
<h3>Cum intri in meniu</h3>
<p>Intra cu masina pe marcajul rosu, la volan. Cand apare <b>Tuneaza masina</b>, apasa <kbd>E</kbd>. Masina se opreste pe loc si camera trece in jurul ei.</p>
</div>
</div>
<h2 class="tng-h2"><span>02</span>Cine poate tuna</h2>
<div class="tng-who">
<div class="tng-card">
<h3>Proprietarul</h3>
<p>Iti tunezi singur masina ta, fara mecanic. Masina altcuiva nu o poti tuna.</p>
</div>
<div class="tng-card amber">
<h3>Mecanicul</h3>
<p>Un mecanic tuneaza orice masina. Doar el poate folosi stancerul si dyno-ul. Despre job: <a href="/joburi/mecanic">Mecanic</a>.</p>
</div>
<div class="tng-card grey">
<h3>Masini de job</h3>
<p>Masinile de politie le tuneaza doar politistii, iar pe cele de ambulanta doar medicii. Primesc doar piese de aspect. Alte masini de job nu se tuneaza.</p>
</div>
</div>
<h2 class="tng-h2"><span>03</span>Meniul de tuning</h2>
<p class="tng-sub">Cand alegi o piesa, o vezi direct pe masina. O platesti doar cand o cumperi.</p>
<div class="tng-menu">
<div class="tng-card">
<h3>Reparatii <small>self-service</small></h3>
<ul class="tng-chips"><li>Motor</li><li>Caroserie</li><li>Parti principale</li><li>Parti de service</li></ul>
<p style="margin-top:0.6rem">O reparatie dureaza 30 de secunde. Merge doar cand sunt putini mecanici de serviciu. Pe Cayo Perico merge oricand.</p>
</div>
<div class="tng-card">
<h3>Aspect exterior <small>vizual</small></h3>
<ul class="tng-chips"><li>Caroserie</li><li>Interior</li><li>Vopsea</li><li>Jante</li><li>Numar de inmatriculare</li><li>Lumini</li><li>Grafica</li><li>Accesorii extra</li><li>Folie geamuri</li></ul>
</div>
<div class="tng-card">
<h3>Performanta <small>viteza</small></h3>
<ul class="tng-chips"><li>Motor</li><li>Frane</li><li>Transmisie</li><li>Suspensii</li><li>Blindaj</li><li>Turbo</li><li>Engine Swap</li></ul>
</div>
</div>
<div class="tng-keys">
<span><kbd>↑</kbd> <kbd>↓</kbd> navighezi</span>
<span><kbd>Enter</kbd> alegi</span>
<span><kbd>Backspace</kbd> inapoi</span>
<span><kbd>Esc</kbd> inchizi</span>
<span><kbd>C</kbd> camera libera</span>
<span><kbd>V</kbd> schimbi camera</span>
<span><kbd>G</kbd> statistici</span>
</div>
<h2 class="tng-h2" id="tng-perf"><span>04</span>Performanta: viteza maxima</h2>
<p class="tng-sub">Fiecare masina are o viteza maxima. Motorul, transmisia, suspensiile, turbina si engine swap-ul o ridica. Franele si blindajul nu schimba viteza maxima.</p>
<div class="tng-dyno">
<ul class="tng-bars">
<li><span class="name">Engine Swap<small>orice motor nou</small></span><span class="track"><span class="fill" style="--w:100%"></span></span><span class="val">+20</span></li>
<li><span class="name">Turbina<small>treapta Ultimate</small></span><span class="track"><span class="fill" style="--w:85%"></span></span><span class="val">+17</span></li>
<li><span class="name">Motor<small>nivelul maxim</small></span><span class="track"><span class="fill" style="--w:75%"></span></span><span class="val">+15</span></li>
<li><span class="name">Transmisie<small>nivelul maxim</small></span><span class="track"><span class="fill" style="--w:70%"></span></span><span class="val">+14</span></li>
<li><span class="name">Suspensii<small>nivelul maxim</small></span><span class="track"><span class="fill" style="--w:70%"></span></span><span class="val">+14</span></li>
</ul>
<p class="tng-note">Valorile sunt in km/h, adaugate la viteza maxima a masinii. Daca o masina nu are loc pentru o piesa, primeste din start bonusul maxim pentru ea.</p>
</div>
<ul class="tng-turbo">
<li><b>Street <i>+5</i></b>O singura turbina, rulmenti standard.</li>
<li><b>Sports <i>+8</i></b>Rulmenti ceramici, intercooler frontal, blow-off.</li>
<li><b>Racing <i>+13</i></b>Twin-scroll, wastegate extern, intercooler mare.</li>
<li><b>Ultimate <i>+17</i></b>Bi-turbo secvential si boost controller.</li>
</ul>
<div class="tng-two" style="margin-top:0.8rem">
<div class="tng-card">
<h3>Turbina</h3>
<p>Turbina iti da putere in plus cand prinde presiune. Supapa de blow-off se aude si de cei din jur. Pe motociclete nu se monteaza turbina. Cu turbina montata poti pune si <a href="/general/antilag">Antilag</a>.</p>
</div>
<div class="tng-card">
<h3>Engine Swap</h3>
<p>Schimbi motorul cu unul din lista clasei masinii tale. Masina capata alt sunet si mai multa putere. Asculti fiecare motor in meniu inainte sa-l cumperi.</p>
<p>Motocicletele primesc din start bonusul de engine swap si de turbina Ultimate.</p>
</div>
</div>
<h2 class="tng-h2"><span>05</span>Aspect</h2>
<div class="tng-two">
<div class="tng-card">
<h3>Vopsea si lumini</h3>
<ul class="tng-list">
<li><b>Vopsea</b> principala, secundara, perlata si tipul vopselei.</li>
<li><b>Chameleon</b>: 82 de culori care isi schimba nuanta dupa unghi, pe principala sau pe secundara.</li>
<li><b>Xenon</b> si <b>neon</b> in orice culoare. Neonul il aprinzi din meniul vehiculului, tasta <kbd>O</kbd>, la Neoane.</li>
<li><b>Folie geamuri</b> si <b>grafica</b>. Unele grafici sunt rezervate anumitor jucatori.</li>
</ul>
</div>
<div class="tng-card">
<h3>Jante si cauciucuri</h3>
<ul class="tng-list">
<li><b>8 tipuri de jante</b>: Sport, Muscle, Lowrider, SUV, Offroad, Tuner, Motocicleta, High End.</li>
<li>Pe motociclete merg doar jantele de tip <b>Motocicleta</b>.</li>
<li><b>Culoare jante</b>, <b>fum cauciucuri</b> si <b>cauciucuri drift</b>.</li>
<li>Jantele <b>Offroad</b> conteaza ca anvelope de teren: <a href="/general/offroad">Offroad</a>.</li>
</ul>
</div>
</div>
<h2 class="tng-h2"><span>06</span>Piese premium</h2>
<p class="tng-sub">Le iei din <a href="/zona-info/store">Magazin</a>, cu EG Coins. Nu le poti da altcuiva, arunca sau vinde in Piata.</p>
<div class="tng-two">
<div class="tng-card">
<h3><img class="eg-item" src="/items/jante_premium_a.webp" alt="">Jante Premium A si <img class="eg-item" src="/items/jante_premium_b.webp" alt="">B</h3>
<ol class="tng-steps" style="margin-top:0.5rem">
<li>Urca-te in <b>masina ta</b> si foloseste item-ul din inventar.</li>
<li>Pachetul se deblocheaza pe acea masina, pentru totdeauna. Item-ul se consuma.</li>
<li>La tuning, in <b>Jante → Model jante</b>, cumperi orice janta din pachet.</li>
</ol>
</div>
<div class="tng-card">
<h3><img class="eg-item" src="/items/antilag.webp" alt="">Antilag</h3>
<p>Pops & bangs si flacari colorate pe evacuare. Ai nevoie de turbina montata. Tot ce trebuie sa stii e pe pagina <a href="/general/antilag">Antilag</a>.</p>
</div>
</div>
<h2 class="tng-h2" id="tng-stancer"><span>07</span>Stancer si dyno</h2>
<div class="tng-two">
<div class="tng-card">
<h3>Stancer</h3>
<p>Doar un mecanic, la volan, cu <b><img class="eg-item" src="/items/stancerkit.webp" alt="">Kit stancer</b> in inventar. Kitul il comanda angajatii service-ului din Tableta firmei, la Furnizor. Il folosesti oriunde, nu doar la atelier.</p>
<ul class="tng-sliders"><li>Inaltime suspensie</li><li>Offset roti fata</li><li>Offset roti spate</li><li>Camber fata</li><li>Camber spate</li><li>Latime roti</li><li>Dimensiune roti</li></ul>
<p>Latimea si dimensiunea rotilor se schimba doar pe jante montate la tuning. Setarile raman salvate pe masina si le vad toti jucatorii. Nu merge pe motociclete, biciclete, barci si aeronave.</p>
</div>
<div class="tng-card">
<h3>Dyno</h3>
<p>Standul dyno e la service-urile din Strawberry, Burton, East Vinewood si Murrieta Heights. Il folosesc doar mecanicii angajati la acel service.</p>
<p>Urca masina pe stand si apasa <kbd>E</kbd> pe <b>Test dyno</b>. Testul dureaza 15 secunde, iar televizorul din atelier arata puterea si cuplul masinii.</p>
</div>
</div>
<h2 class="tng-h2"><span>08</span>Plata si salvare</h2>
<div class="tng-two">
<div class="tng-card">
<h3>Cine plateste</h3>
<ul class="tng-list">
<li>Platesti cand cumperi piesa, intai din cash, apoi din banca.</li>
<li>Pretul depinde de valoarea masinii si de piesa aleasa.</li>
<li>Cand un mecanic iti tuneaza masina, el plateste piesele. Ti le poate cere apoi printr-o factura pe Terminalul POS.</li>
<li>Service-ul primeste o parte din fiecare piesa vanduta in atelierul lui.</li>
</ul>
</div>
<div class="tng-card">
<h3>Salvare si proba</h3>
<ul class="tng-list">
<li>Piesele cumparate se salveaza pe masina cand inchizi meniul, chiar daca iesi de pe server in timp ce tunezi.</li>
<li>La dealer, butonul <b>Tuning</b> iti arata cum arata masina tunata, inainte s-o cumperi. Acolo nu platesti si nu se salveaza nimic.</li>
</ul>
</div>
</div>
<h2 class="tng-h2"><span>09</span>Limite</h2>
<div class="tng-card tng-warn">
<ul class="tng-list">
<li>Barcile, elicopterele, avioanele, bicicletele si masinile de Cayo primesc doar piese de aspect.</li>
<li>Masinile de job primesc doar piese de aspect.</li>
<li>Tunezi doar stand la volan.</li>
<li>Armele de pe masini, minele, lamele, tepii si placile de blindaj nu se vand.</li>
<li>Pe aeronave nu ai acces la Accesorii extra.</li>
</ul>
</div>
<p class="tng-foot">Mai departe: <a href="/general/antilag">Antilag</a> pentru pops & bangs, <a href="/general/offroad">Offroad</a> pentru condusul pe teren, <a href="/afaceri/service">Service auto</a> pentru firmele de mecanici.</p>
</div>
