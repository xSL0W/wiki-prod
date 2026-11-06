---
outline: false
---

<style>
.ofr {
  --ink: #0b0b0d;
  --panel: #151517;
  --panel2: #1d1d20;
  --line: #2f2f35;
  --text: #f4f4f5;
  --mute: #a1a1aa;
  --red: #dc2626;
  --red2: #ef4444;
  --amber: #f59e0b;
  --mud: #a16207;
  --carbon: repeating-linear-gradient(45deg, rgba(255, 255, 255, 0.022) 0 2px, transparent 2px 6px), repeating-linear-gradient(-45deg, rgba(0, 0, 0, 0.28) 0 2px, transparent 2px 6px), #111113;
  max-width: 980px;
  margin: 0 auto;
  color: var(--text);
}
.ofr *, .ofr *::before, .ofr *::after { box-sizing: border-box; }
.ofr p, .ofr li { margin: 0; line-height: 1.6; color: var(--text); }
.ofr ul, .ofr ol { list-style: none; padding: 0; margin: 0; }
.ofr li + li { margin-top: 0; }
.ofr b { color: #fff; font-weight: 650; }
.ofr a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.ofr a:hover { color: #fde68a; }
.ofr a:focus-visible { outline: 3px solid var(--amber); outline-offset: 3px; border-radius: 6px; }
/* group nav (shared by the Tuning pages) */
.ofr .ofr-group { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1rem; }
.ofr .ofr-group a {
  display: inline-flex; align-items: center; gap: 0.55rem; text-decoration: none; color: var(--mute);
  background: var(--panel); border: 1px solid var(--line); border-radius: 10px; padding: 0.35rem 0.85rem 0.35rem 0.4rem;
  font-weight: 700; font-size: 0.9rem;
}
.ofr .ofr-group a span { font: 800 0.75rem ui-monospace, Menlo, Consolas, monospace; color: var(--ink); background: var(--mute); border-radius: 6px; padding: 0.1rem 0.35rem; }
.ofr .ofr-group a:hover { color: #fff; border-color: var(--red); }
.ofr .ofr-group a[aria-current="page"] { color: #fff; border-color: var(--red); background: rgba(220, 38, 38, 0.12); }
.ofr .ofr-group a[aria-current="page"] span { background: var(--red); color: #fff; }
/* hero */
.ofr .ofr-hero {
  position: relative; overflow: hidden; border: 1px solid var(--line); border-radius: 22px;
  background: radial-gradient(90% 90% at 50% 120%, rgba(161, 98, 7, 0.28), transparent 65%), var(--carbon);
  padding: clamp(1.25rem, 4vw, 2.4rem); padding-top: calc(clamp(1.25rem, 4vw, 2.4rem) + 12px);
}
.ofr .ofr-hero::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 12px;
  background: conic-gradient(#e4e4e7 0 25%, #0b0b0d 0 50%, #e4e4e7 0 75%, #0b0b0d 0) 0 0 / 12px 12px; opacity: 0.85;
}
.ofr .ofr-kicker { font: 800 0.75rem ui-monospace, Menlo, Consolas, monospace; letter-spacing: 0.16em; text-transform: uppercase; color: var(--amber); margin-bottom: 0.6rem; }
.ofr .ofr-hero h1 {
  margin: 0 0 0.8rem; border: 0; padding: 0; font-style: italic;
  font-size: clamp(2.4rem, 8vw, 3.6rem); line-height: 1; font-weight: 900; letter-spacing: -0.035em; color: #fff;
}
.ofr .ofr-lede { color: var(--mute); font-size: 1.05rem; max-width: 60ch; }
.ofr .ofr-art { display: block; width: 100%; height: auto; margin-top: 1.2rem; border-radius: 14px; background: rgba(11, 11, 13, 0.55); border: 1px solid var(--line); }
.ofr-art .hill { fill: #18181b; }
.ofr-art .ground { fill: #3b2a12; stroke: var(--mud); stroke-width: 3; }
.ofr-art .scroll { animation: ofr-scroll 2.4s linear infinite; }
.ofr-art .far { animation: ofr-scroll-far 9s linear infinite; }
.ofr-art .body { fill: #1c1c20; stroke: #e4e4e7; stroke-width: 2.2; stroke-linejoin: round; }
.ofr-art .glass { fill: rgba(161, 161, 170, 0.18); stroke: #a1a1aa; stroke-width: 1.4; }
.ofr-art .bar { fill: var(--red); }
.ofr-art .chassis { animation: ofr-body 1.2s ease-in-out infinite; }
.ofr-art .wheel { animation: ofr-wheel 1.2s ease-in-out infinite; }
.ofr-art .wheel.rear { animation-delay: -0.6s; }
.ofr-art .tyre { fill: #0b0b0d; stroke: #52525b; stroke-width: 6; stroke-dasharray: 5 4; }
.ofr-art .rim { fill: none; stroke: var(--amber); stroke-width: 2.5; }
.ofr-art .spring { fill: none; stroke: var(--amber); stroke-width: 2; stroke-linejoin: round; }
.ofr-art .mud { fill: var(--mud); opacity: 0; animation: ofr-mud 1.2s ease-out infinite; }
.ofr-art .mud.m2 { animation-delay: 0.3s; }
.ofr-art .mud.m3 { animation-delay: 0.65s; }
@keyframes ofr-scroll { to { transform: translateX(-120px); } }
@keyframes ofr-scroll-far { to { transform: translateX(-300px); } }
@keyframes ofr-body { 0%, 100% { transform: translateY(0) rotate(0deg); } 50% { transform: translateY(-4px) rotate(-0.8deg); } }
@keyframes ofr-wheel { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-11px); } }
@keyframes ofr-mud { 0% { opacity: 0; transform: translate(0, 0); } 15% { opacity: 1; } 70%, 100% { opacity: 0; transform: translate(-46px, -22px); } }
.ofr .ofr-facts { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 150px), 1fr)); gap: 0.6rem; margin-top: 1rem; }
.ofr .ofr-facts li { background: rgba(11, 11, 13, 0.7); border: 1px solid var(--line); border-left: 3px solid var(--mud); border-radius: 10px; padding: 0.7rem 0.9rem; }
.ofr .ofr-facts b { display: block; font: 900 1.45rem/1.1 ui-monospace, Menlo, Consolas, monospace; color: #fff; font-style: italic; }
.ofr .ofr-facts span { color: var(--mute); font-size: 0.9rem; }
/* section heads */
.ofr .ofr-h2 {
  display: flex; align-items: center; gap: 0.7rem; margin: 3rem 0 0.9rem; border: 0; padding: 0;
  font-size: 1.45rem; font-weight: 850; letter-spacing: -0.015em; color: #fff; font-style: italic;
}
.ofr .ofr-h2 span { flex: none; font: 800 0.8rem ui-monospace, Menlo, Consolas, monospace; font-style: normal; color: #fff; background: var(--red); border-radius: 6px; padding: 0.15rem 0.45rem; transform: skewX(-10deg); }
.ofr .ofr-sub { color: var(--mute); margin: -0.3rem 0 1rem; max-width: 66ch; }
.ofr .ofr-card { background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 1rem 1.15rem; }
.ofr .ofr-card h3 { margin: 0 0 0.45rem; border: 0; padding: 0; font-size: 1.02rem; font-weight: 800; color: #fff; }
.ofr .ofr-card p { color: var(--mute); font-size: 0.95rem; }
/* surfaces strip */
.ofr .ofr-strata { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 180px), 1fr)); gap: 0; border: 1px solid var(--line); border-radius: 14px; overflow: hidden; }
.ofr .ofr-strata li { padding: 1rem 1.1rem; color: var(--mute); font-size: 0.93rem; border-right: 1px solid var(--line); }
.ofr .ofr-strata li:last-child { border-right: 0; }
.ofr .ofr-strata li b { display: block; color: #fff; font-size: 1rem; margin-bottom: 0.2rem; }
.ofr .ofr-strata .hard { background: linear-gradient(180deg, #27272a, var(--panel)); }
.ofr .ofr-strata .soft { background: linear-gradient(180deg, #3b2a12, var(--panel)); }
.ofr .ofr-strata .deep { background: linear-gradient(180deg, #4a2c0a, var(--panel)); }
.ofr .ofr-effects { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 180px), 1fr)); gap: 0.7rem; margin-top: 0.8rem; }
.ofr .ofr-effects .ofr-card { border-top: 3px solid var(--mud); }
/* speed bars */
.ofr .ofr-speed { background: var(--carbon); border: 1px solid var(--line); border-radius: 16px; padding: 1.1rem 1.2rem; }
.ofr .ofr-legend { display: flex; flex-wrap: wrap; gap: 1rem; margin-bottom: 0.7rem; font-size: 0.85rem; color: var(--mute); }
.ofr .ofr-legend i { display: inline-block; width: 0.9rem; height: 0.6rem; border-radius: 2px; margin-right: 0.35rem; vertical-align: middle; }
.ofr .ofr-legend .a { background: #52525b; }
.ofr .ofr-legend .b { background: linear-gradient(90deg, var(--amber), var(--red)); }
.ofr .ofr-rows li { display: grid; grid-template-columns: minmax(7rem, 10rem) 1fr; gap: 0.3rem 0.9rem; align-items: center; padding: 0.55rem 0; }
.ofr .ofr-rows li + li { border-top: 1px solid rgba(63, 63, 70, 0.45); }
.ofr .ofr-rows .name { font-weight: 750; grid-row: span 2; }
.ofr .ofr-rows .name small { display: block; color: var(--mute); font-weight: 500; font-size: 0.78rem; }
.ofr .ofr-rows .bar { display: flex; align-items: center; gap: 0.5rem; font: 800 0.85rem ui-monospace, Menlo, Consolas, monospace; color: #fff; }
.ofr .ofr-rows .bar i { display: block; height: 10px; border-radius: 2px; width: var(--w); flex: none; max-width: calc(100% - 4.5rem); }
.ofr .ofr-rows .bar.a i { background: #52525b; }
.ofr .ofr-rows .bar.b i { background: linear-gradient(90deg, var(--amber), var(--red)); }
.ofr .ofr-mods { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 180px), 1fr)); gap: 0.6rem; margin-top: 0.9rem; }
.ofr .ofr-mods li { background: var(--panel); border: 1px solid var(--line); border-radius: 12px; padding: 0.7rem 0.9rem; color: var(--mute); font-size: 0.9rem; }
.ofr .ofr-mods li b { display: block; font: 900 1.25rem/1.15 ui-monospace, Menlo, Consolas, monospace; font-style: italic; color: var(--amber); }
/* tyres path */
.ofr .ofr-path { display: flex; flex-wrap: wrap; align-items: center; gap: 0.35rem; margin: 0.2rem 0 0.9rem; }
.ofr .ofr-path li { font-weight: 700; font-size: 0.9rem; background: var(--panel2); border: 1px solid var(--line); border-radius: 8px; padding: 0.2rem 0.65rem; }
.ofr .ofr-path li.sep { background: none; border: 0; padding: 0; color: var(--mute); }
.ofr .ofr-path li.end { border-color: var(--amber); color: var(--amber); }
.ofr .ofr-two { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr)); gap: 0.7rem; }
.ofr .ofr-list li { position: relative; padding: 0.45rem 0 0.45rem 1.2rem; color: var(--mute); }
.ofr .ofr-list li + li { border-top: 1px solid var(--line); }
.ofr .ofr-list li::before { content: ''; position: absolute; left: 0; top: 0.95rem; width: 8px; height: 8px; background: var(--amber); transform: skewX(-15deg); }
.ofr .ofr-list li.minus::before { background: var(--red); }
.ofr .ofr-list li b { color: #fff; }
/* weather table */
.ofr .ofr-table { width: 100%; border-collapse: collapse; display: table; margin: 0; font-size: 0.93rem; }
.ofr .ofr-wrap { border: 1px solid var(--line); border-radius: 14px; overflow-x: auto; }
.ofr .ofr-table th, .ofr .ofr-table td { border: 0; border-bottom: 1px solid var(--line); padding: 0.6rem 0.8rem; text-align: left; background: var(--panel); }
.ofr .ofr-table tr:last-child td { border-bottom: 0; }
.ofr .ofr-table th { background: var(--panel2); color: var(--mute); font: 700 0.72rem ui-monospace, Menlo, Consolas, monospace; text-transform: uppercase; letter-spacing: 0.08em; }
.ofr .ofr-table td.num { font: 800 0.9rem ui-monospace, Menlo, Consolas, monospace; color: #fff; white-space: nowrap; }
.ofr .ofr-table td.num.up { color: #86efac; }
.ofr .ofr-warn { border-left: 4px solid var(--red); }
.ofr .ofr-foot { margin-top: 2.5rem; padding: 1rem 1.2rem; border: 1px dashed var(--line); border-radius: 14px; color: var(--mute); }
@media (max-width: 520px) {
  .ofr .ofr-rows li { grid-template-columns: 1fr; }
  .ofr .ofr-rows .name { grid-row: auto; }
}
@media (prefers-reduced-motion: reduce) {
  .ofr-art .scroll, .ofr-art .far, .ofr-art .chassis, .ofr-art .wheel, .ofr-art .mud { animation: none; }
  .ofr-art .mud { opacity: 0; }
}
</style>
<div class="ofr">
<nav class="ofr-group" aria-label="Pagini tuning">
<a href="/general/tuning"><span>01</span>Tuning</a>
<a href="/general/antilag"><span>02</span>Antilag</a>
<a href="/general/offroad" aria-current="page"><span>03</span>Offroad</a>
</nav>
<section class="ofr-hero">
<p class="ofr-kicker">Teren · Noroi · Vreme</p>
<h1>Offroad</h1>
<p class="ofr-lede">Cand iesi de pe asfalt, masina simte terenul. In nisip si noroi rotile se afunda, pe pamant moale aluneci, iar viteza maxima scade dupa tipul masinii. Anvelopele de teren si tractiunea 4x4 te ajuta.</p>
<svg class="ofr-art" viewBox="0 0 600 190" role="img" aria-label="Un SUV merge peste teren denivelat: rotile urca si coboara pe suspensie, din spate sare noroi">
<g class="far"><path class="hill" d="M0 120 Q75 60 150 110 Q225 70 300 112 Q375 62 450 110 Q525 72 600 112 Q675 60 750 110 Q825 70 900 112 L900 190 L0 190 Z"/></g>
<g class="scroll"><path class="ground" d="M0 160 Q30 148 60 160 T120 160 T180 160 T240 160 T300 160 T360 160 T420 160 T480 160 T540 160 T600 160 T660 160 T720 160 L720 190 L0 190 Z"/></g>
<circle class="mud" cx="196" cy="150" r="4"/>
<circle class="mud m2" cx="200" cy="146" r="3"/>
<circle class="mud m3" cx="192" cy="152" r="3.5"/>
<g class="wheel rear"><path class="spring" d="M238 120 l6 4 l-12 4 l12 4 l-12 4 l6 3"/><circle class="tyre" cx="238" cy="142" r="20"/><circle class="rim" cx="238" cy="142" r="10"/></g>
<g class="wheel"><path class="spring" d="M392 120 l6 4 l-12 4 l12 4 l-12 4 l6 3"/><circle class="tyre" cx="392" cy="142" r="20"/><circle class="rim" cx="392" cy="142" r="10"/></g>
<g class="chassis">
<path class="body" d="M200 120 L204 92 Q206 84 216 84 L262 82 L284 56 Q290 50 300 50 L370 50 Q380 50 386 58 L404 84 L426 88 Q436 90 436 100 L436 120 Q436 124 430 124 L206 124 Q200 124 200 120 Z"/>
<path class="glass" d="M292 58 L330 58 L330 82 L274 82 Z"/>
<path class="glass" d="M338 58 L372 58 Q378 58 382 64 L394 82 L338 82 Z"/>
<rect class="bar" x="288" y="42" width="96" height="5" rx="2"/>
<rect x="206" y="104" width="226" height="4" fill="#3f3f46"/>
</g>
</svg>
<ul class="ofr-facts">
<li><b>4</b><span>tipuri de vehicule, cu limite diferite</span></li>
<li><b>+10 km/h</b><span>pe teren, pentru masinile 4x4</span></li>
<li><b>30 km/h</b><span>limita cand mergi pe janta</span></li>
</ul>
</section>
<h2 class="ofr-h2"><span>01</span>Ce simti pe teren</h2>
<ul class="ofr-strata">
<li class="hard"><b>Asfalt si beton</b>Sosea, beton, metal, piatra cubica si stanca. Masina merge normal.</li>
<li class="soft"><b>Teren tare</b>Drumuri de pietris, pamant uscat, iarba scurta, marginea nisipoasa a soselei. Te afunzi putin.</li>
<li class="deep"><b>Teren adanc</b>Nisip, pamant, camp arat, nisip ud si mlastina. Rotile se afunda mult.</li>
</ul>
<div class="ofr-effects">
<div class="ofr-card"><h3>Te afunzi</h3><p>Rotile intra in pamant si masina incetineste. Cu cat terenul e mai adanc, cu atat iesi mai greu. Cand accelerezi in noroi, masina se murdareste.</p></div>
<div class="ofr-card"><h3>Aluneci</h3><p>Pe teren moale masina are mai putina aderenta si derapeaza mai usor.</p></div>
<div class="ofr-card"><h3>Viteza scade</h3><p>Cand iesi de pe asfalt, viteza maxima coboara treptat. Cand revii pe sosea, creste la loc.</p></div>
</div>
<h2 class="ofr-h2"><span>02</span>Viteza maxima pe teren</h2>
<p class="ofr-sub">Limita depinde de tipul masinii si de anvelope. Masinile din categoria Offroad si SUV-urile merg cel mai repede.</p>
<div class="ofr-speed">
<div class="ofr-legend"><span><i class="a"></i>Anvelope normale</span><span><i class="b"></i>Anvelope offroad</span></div>
<ul class="ofr-rows">
<li><span class="name">Offroad<small>masini de teren</small></span><span class="bar a"><i style="--w:66%"></i>110</span><span class="bar b"><i style="--w:78%"></i>130</span></li>
<li><span class="name">Motociclete de cros<small>Sanchez, BF400, Manchez...</small></span><span class="bar a"><i style="--w:60%"></i>100</span><span class="bar b"><i style="--w:78%"></i>130</span></li>
<li><span class="name">SUV</span><span class="bar a"><i style="--w:48%"></i>80</span><span class="bar b"><i style="--w:66%"></i>110</span></li>
<li><span class="name">Restul masinilor</span><span class="bar a"><i style="--w:12%"></i>20</span><span class="bar b"><i style="--w:24%"></i>40</span></li>
</ul>
</div>
<ul class="ofr-mods">
<li><b>+10 km/h</b>daca masina are tractiune 4x4</li>
<li><b>60%</b>din limita, pe munte: Chiliad, Gordo, Josiah si Palomino Highlands</li>
<li><b>50%</b>din limita, in mlastina Zancudo</li>
</ul>
<h2 class="ofr-h2"><span>03</span>Anvelope offroad</h2>
<p class="ofr-sub">Nu e un item separat. Montezi orice janta din categoria Offroad, la un atelier de <a href="/general/tuning">Tuning</a>:</p>
<ol class="ofr-path"><li>Aspect Exterior</li><li class="sep">→</li><li>Jante</li><li class="sep">→</li><li>Model jante</li><li class="sep">→</li><li class="end">Offroad</li></ol>
<div class="ofr-two">
<div class="ofr-card">
<h3>Ce primesti</h3>
<ul class="ofr-list">
<li>Limita de viteza mai mare pe teren.</li>
<li>Te afunzi mai putin in nisip si noroi.</li>
<li>Mai multa aderenta pe teren moale.</li>
<li>Mai multa aderenta pe ploaie si pe zapada.</li>
<li class="minus">Putin mai putina aderenta pe asfalt.</li>
</ul>
</div>
<div class="ofr-card">
<h3>Motocicletele</h3>
<p>Pe motociclete merg doar jantele de tip Motocicleta. De aceea, orice motocicleta are din start bonusul anvelopelor offroad.</p>
</div>
</div>
<h2 class="ofr-h2"><span>04</span>Ce te mai ajuta</h2>
<div class="ofr-two">
<div class="ofr-card">
<ul class="ofr-list">
<li><b>Tractiunea 4x4</b>: te afunzi mai putin si ai aderenta mai buna pe ploaie si zapada.</li>
<li><b>Tipul masinii</b>: masinile de teren si SUV-urile ies cel mai usor din noroi. Motocicletele ies cel mai greu.</li>
</ul>
</div>
<div class="ofr-card">
<ul class="ofr-list">
<li><b>Aproape de sosea</b>: pamantul de langa drumurile mari e mai putin adanc.</li>
<li><b>In oras</b>: parcurile si zonele verzi din oras te trag mult mai putin in jos decat terenul de la tara.</li>
</ul>
</div>
</div>
<h2 class="ofr-h2"><span>05</span>Ploaie si zapada</h2>
<p class="ofr-sub">Vremea iti ia din aderenta, pe asfalt si pe teren. Pe ploaie si zapada, terenul devine si mai adanc.</p>
<div class="ofr-wrap">
<table class="ofr-table">
<thead><tr><th>Vreme</th><th>Pe asfalt</th><th>Pe teren</th></tr></thead>
<tbody>
<tr><td>Ploaie</td><td class="num">-15%</td><td class="num">-25%</td></tr>
<tr><td>Ploaie puternica</td><td class="num">-30%</td><td class="num">-40%</td></tr>
<tr><td>Zapada</td><td class="num">-15%</td><td class="num">-25%</td></tr>
<tr><td>Viscol</td><td class="num">-30%</td><td class="num">-40%</td></tr>
</tbody>
</table>
</div>
<div class="ofr-wrap" style="margin-top:0.7rem">
<table class="ofr-table">
<thead><tr><th>Iti recupereaza aderenta</th><th>Ploaie</th><th>Zapada</th></tr></thead>
<tbody>
<tr><td>Anvelope offroad</td><td class="num up">+10%</td><td class="num up">+20%</td></tr>
<tr><td>Tractiune 4x4</td><td class="num up">+5%</td><td class="num up">+15%</td></tr>
<tr><td>Masini premium</td><td class="num up">+5%</td><td class="num up">+10%</td></tr>
</tbody>
</table>
</div>
<h2 class="ofr-h2"><span>06</span>Pe janta si exceptii</h2>
<div class="ofr-two">
<div class="ofr-card ofr-warn">
<h3>Anvelope distruse</h3>
<p>Cand cel putin jumatate din roti merg pe janta, mai ai 100 de metri. Dupa ei, masina nu mai trece de 30 km/h pana repari anvelopele. Pe teren se aplica limita mai mica dintre cele doua.</p>
</div>
<div class="ofr-card">
<h3>Unde nu se aplica</h3>
<ul class="ofr-list">
<li>Barci, avioane si elicoptere. Elicopterele cu roti se afunda totusi cand aterizeaza pe teren moale. Daca se afunda de tot, nu mai decoleaza si trebuie remorcate pe teren tare.</li>
<li>Platformele si masinile de tractari ale mecanicilor.</li>
<li>Pe Cayo Perico nu te afunzi, dar aderenta scade la fel.</li>
<li>In cateva locuri fixe: Legion Square, spitalul Pillbox, sectiile de politie din Mission Row, Sandy Shores si Paleto, dealer-ul Premium Deluxe Motorsport.</li>
</ul>
</div>
</div>
<p class="ofr-foot">Jante si restul pieselor: <a href="/general/tuning">Tuning</a>. Pops & bangs pe evacuare: <a href="/general/antilag">Antilag</a>.</p>
</div>
