---
outline: false
---

<style>
.drn {
  --ink: #0b0b0d;
  --panel: #17171a;
  --panel2: #1f1f23;
  --line: #2f2f36;
  --text: #f4f4f5;
  --mute: #a1a1aa;
  --red: #ef4444;
  --red-deep: #b91c1c;
  --red-soft: rgba(239, 68, 68, 0.14);
  --cyan: #67e8f9;
  --cyan-soft: rgba(103, 232, 249, 0.12);
  --green: #4ade80;
  max-width: 960px;
  margin: 0 auto;
  color: var(--text);
  font-family: Inter, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.drn *, .drn *::before, .drn *::after { box-sizing: border-box; }
.drn p, .drn li { line-height: 1.6; color: var(--text); margin: 0; }
.drn ul, .drn ol { list-style: none; padding: 0; margin: 0; }
.drn li + li { margin-top: 0; }
.drn b { color: #fff; font-weight: 650; }
.drn a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.drn a:hover { color: #fecaca; }
.drn a:focus-visible { outline: 3px solid var(--red); outline-offset: 3px; border-radius: 6px; }
.drn kbd {
  display: inline-block; min-width: 1.7em; text-align: center;
  font: inherit; font-size: 0.82em; font-weight: 700; color: #fff; background: var(--red-deep);
  border-radius: 6px; padding: 0.08rem 0.45rem; box-shadow: inset 0 -2px 0 rgba(0, 0, 0, 0.35);
}
/* ---------- hero ---------- */
.drn .drn-hero {
  position: relative; overflow: hidden; isolation: isolate;
  background: radial-gradient(80% 110% at 85% 0%, rgba(103, 232, 249, 0.1), transparent 55%),
              radial-gradient(110% 120% at 0% 100%, rgba(185, 28, 28, 0.28), var(--ink) 62%);
  border: 1px solid var(--line);
  border-radius: 22px;
  padding: clamp(1.15rem, 4vw, 2.4rem);
}
.drn .drn-kicker {
  font-size: 0.78rem; font-weight: 700; letter-spacing: 0.16em; text-transform: uppercase; color: var(--red);
  margin-bottom: 0.55rem;
}
.drn .drn-hero h1 {
  margin: 0 0 0.75rem; border: 0; padding: 0;
  font-size: clamp(2rem, 6.4vw, 3.4rem); line-height: 1.04; font-weight: 800; letter-spacing: -0.03em; color: #fff;
}
.drn .drn-hero h1 span { color: var(--cyan); }
.drn .drn-lede { max-width: 60ch; color: var(--mute); font-size: 1.05rem; }
/* drone scene */
.drn .drn-scene { display: block; width: 100%; height: auto; margin-top: 1.3rem; border-radius: 14px; background: #08080a; }
.drn-scene .sky { fill: url(#drn-sky); }
.drn-scene .bld { fill: #101014; stroke: #222229; stroke-width: 1; }
.drn-scene .lit { fill: #f5b931; opacity: 0.55; }
.drn-scene .grid line { stroke: #1f2a2e; stroke-width: 1; }
.drn-scene .cone { fill: url(#drn-cone); }
.drn-scene .scanline { stroke: var(--cyan); stroke-width: 1.5; opacity: 0.55; }
.drn-scene .spot { fill: none; stroke: var(--cyan); stroke-width: 1.5; stroke-dasharray: 4 4; opacity: 0.7; }
.drn-scene .body { fill: #2a2a31; stroke: #44444d; stroke-width: 1.2; }
.drn-scene .arm { stroke: #3a3a42; stroke-width: 5; stroke-linecap: round; }
.drn-scene .motor { fill: #1a1a1f; stroke: #4a4a54; stroke-width: 1; }
.drn-scene .disc { fill: rgba(220, 220, 230, 0.08); stroke: rgba(220, 220, 230, 0.18); stroke-width: 1; }
.drn-scene .blade { fill: #c9c9d1; opacity: 0.75; }
.drn-scene .lens { fill: #0b0b0d; stroke: var(--cyan); stroke-width: 1.5; }
.drn-scene .led { fill: var(--red); }
.drn-scene .hud { fill: none; stroke: rgba(255, 255, 255, 0.55); stroke-width: 2; }
.drn-scene .reticle { fill: none; stroke: var(--cyan); stroke-width: 1.2; opacity: 0.75; }
.drn-scene .hud-t { fill: #e4e4e7; font: 700 11px ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; letter-spacing: 0.06em; }
.drn-scene .hud-m { fill: #a1a1aa; }
.drn-scene .rec { fill: var(--red); }
.drn-scene .drift { animation: drn-drift 9s ease-in-out infinite; }
.drn-scene .blade { transform-box: fill-box; transform-origin: center; animation: drn-spin 0.16s linear infinite; }
.drn-scene .blade.b2 { animation-delay: -0.04s; }
.drn-scene .blade.b3 { animation-delay: -0.08s; }
.drn-scene .blade.b4 { animation-delay: -0.12s; }
.drn-scene .sweep { transform-box: view-box; transform-origin: 320px 112px; animation: drn-sweep 6s ease-in-out infinite; }
.drn-scene .scanline { animation: drn-scan 2.4s linear infinite; }
.drn-scene .led, .drn-scene .rec { animation: drn-blink 1.4s steps(1, end) infinite; }
.drn-scene .reticle { transform-box: fill-box; transform-origin: center; animation: drn-lock 6s ease-in-out infinite; }
@keyframes drn-drift {
  0%, 100% { transform: translate(0, 0); }
  30% { transform: translate(14px, -7px); }
  65% { transform: translate(-12px, 5px); }
}
@keyframes drn-spin { 0% { transform: scaleX(1); } 50% { transform: scaleX(0.08); } 100% { transform: scaleX(1); } }
@keyframes drn-sweep { 0%, 100% { transform: rotate(-9deg); } 50% { transform: rotate(9deg); } }
@keyframes drn-scan { 0% { transform: translateY(0); opacity: 0; } 15% { opacity: 0.6; } 100% { transform: translateY(110px); opacity: 0; } }
@keyframes drn-blink { 0% { opacity: 1; } 50% { opacity: 0.15; } }
@keyframes drn-lock { 0%, 100% { transform: scale(1); } 45% { transform: scale(1.18); } 55% { transform: scale(0.94); } }
/* hero stats */
.drn .drn-stats { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 0.6rem; margin-top: 1.2rem; }
.drn .drn-stats li { background: rgba(23, 23, 26, 0.85); border: 1px solid var(--line); border-radius: 14px; padding: 0.7rem 0.9rem; }
.drn .drn-stats b { display: block; font-size: clamp(1.35rem, 4vw, 1.8rem); line-height: 1.1; font-weight: 800; color: #fff; font-variant-numeric: tabular-nums; }
.drn .drn-stats span { display: block; color: var(--mute); font-size: 0.82rem; line-height: 1.35; margin-top: 0.2rem; }
@media (max-width: 480px) { .drn .drn-stats { grid-template-columns: minmax(0, 1fr); } }
@media (prefers-reduced-motion: reduce) {
  .drn .drn-scene .drift, .drn .drn-scene .blade, .drn .drn-scene .sweep, .drn .drn-scene .scanline,
  .drn .drn-scene .led, .drn .drn-scene .rec, .drn .drn-scene .reticle { animation: none; }
  .drn .drn-scene .scanline { opacity: 0; }
}
/* ---------- sections ---------- */
.drn .drn-h2 {
  display: flex; align-items: center; gap: 0.65rem;
  margin: 3rem 0 0.9rem; border: 0; padding: 0;
  font-size: 1.5rem; font-weight: 750; letter-spacing: -0.015em; line-height: 1.25; color: #fff;
}
.drn .drn-h2::before {
  content: ''; flex: none; width: 0.6rem; height: 0.6rem; border-radius: 2px; background: var(--red);
  transform: rotate(45deg); box-shadow: 0 0 0 4px var(--red-soft);
}
.drn .drn-h3 { margin: 0 0 0.35rem; border: 0; padding: 0; font-size: 1.05rem; font-weight: 700; color: #fff; line-height: 1.3; }
.drn .drn-sub { color: var(--mute); max-width: 66ch; margin-bottom: 1rem; }
.drn .drn-card { background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 1.1rem 1.25rem; }
.drn .drn-card p { color: var(--mute); font-size: 0.97rem; }
.drn .drn-card p + p { margin-top: 0.5rem; }
.drn .drn-grid2 { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 0.8rem; }
.drn .drn-grid3 { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 0.8rem; }
/* need: numbered cards */
.drn .drn-need { counter-reset: drn-step; }
.drn .drn-need > li { position: relative; counter-increment: drn-step; padding-top: 2.6rem; }
.drn .drn-need > li::before {
  content: counter(drn-step); position: absolute; top: 0.9rem; left: 1.25rem;
  width: 1.5rem; height: 1.5rem; border-radius: 50%; display: grid; place-items: center;
  font-size: 0.8rem; font-weight: 800; color: #fff; background: var(--red-deep);
}
.drn .drn-path {
  display: inline-block; margin-top: 0.6rem; font-size: 0.86rem; font-weight: 650; color: var(--cyan);
  background: var(--cyan-soft); border: 1px solid rgba(103, 232, 249, 0.25); border-radius: 999px; padding: 0.2rem 0.7rem;
}
@media (max-width: 480px) { .drn .drn-path { border-radius: 10px; } }
/* models */
.drn .drn-model { display: flex; flex-direction: column; gap: 0.75rem; }
.drn .drn-model.nv { background: linear-gradient(160deg, rgba(74, 222, 128, 0.08), var(--panel) 55%); }
.drn .drn-model.fpv { background: linear-gradient(160deg, var(--red-soft), var(--panel) 55%); }
.drn .drn-tag {
  align-self: flex-start; font-size: 0.7rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase;
  color: var(--mute); border: 1px solid var(--line); border-radius: 999px; padding: 0.12rem 0.55rem;
}
.drn .drn-model.nv .drn-tag { color: var(--green); border-color: rgba(74, 222, 128, 0.35); }
.drn .drn-model.fpv .drn-tag { color: var(--red); border-color: rgba(239, 68, 68, 0.4); }
.drn .drn-spec { margin-top: auto; }
.drn .drn-spec li {
  display: flex; justify-content: space-between; gap: 1rem; padding: 0.42rem 0; border-top: 1px dashed var(--line);
  font-size: 0.92rem; color: var(--mute);
}
.drn .drn-spec li b { color: #fff; text-align: right; }
.drn .drn-pips { display: inline-flex; gap: 3px; vertical-align: middle; }
.drn .drn-pips i { width: 9px; height: 9px; border-radius: 2px; background: #3f3f46; }
.drn .drn-pips i.on { background: var(--red); }
/* launch steps */
.drn .drn-steps { display: grid; gap: 0.55rem; }
.drn .drn-steps li {
  display: grid; grid-template-columns: 2rem minmax(0, 1fr); gap: 0.75rem; align-items: start;
  background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 0.8rem 1rem;
}
.drn .drn-steps .n {
  width: 2rem; height: 2rem; border-radius: 10px; display: grid; place-items: center;
  font-weight: 800; color: #fff; background: var(--panel2); border: 1px solid var(--line);
}
.drn .drn-steps p { color: var(--mute); font-size: 0.95rem; }
.drn .drn-warn {
  margin-top: 0.8rem; border-left: 3px solid var(--red); background: var(--red-soft);
  border-radius: 0 12px 12px 0; padding: 0.7rem 1rem; color: var(--text); font-size: 0.95rem;
}
/* controls */
.drn .drn-keys { display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 0.55rem; }
.drn .drn-keys li {
  display: flex; align-items: center; gap: 0.7rem;
  background: var(--panel); border: 1px solid var(--line); border-radius: 12px; padding: 0.6rem 0.85rem;
}
.drn .drn-keys .k { display: flex; gap: 0.25rem; flex: none; min-width: 4.6rem; }
.drn .drn-keys span:last-child { color: var(--mute); font-size: 0.93rem; line-height: 1.35; }
.drn .drn-keys .nw { white-space: nowrap; }
.drn .drn-note { margin-top: 0.85rem; color: var(--mute); font-size: 0.93rem; }
/* hud readouts */
.drn .drn-hud { display: grid; grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: 0.55rem; }
.drn .drn-hud li {
  background: #0d0f10; border: 1px solid #1f2a2e; border-radius: 12px; padding: 0.7rem 0.85rem;
}
.drn .drn-hud .l {
  display: block; font: 700 0.7rem/1.2 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace;
  letter-spacing: 0.14em; text-transform: uppercase; color: var(--cyan);
}
.drn .drn-hud .d { display: block; margin-top: 0.3rem; color: var(--mute); font-size: 0.9rem; line-height: 1.45; }
/* recover */
.drn .drn-rec li { display: grid; grid-template-columns: 1.6rem minmax(0, 1fr); gap: 0.6rem; padding: 0.55rem 0; border-top: 1px solid var(--line); }
.drn .drn-rec li:first-child { border-top: 0; padding-top: 0; }
.drn .drn-rec .ic {
  width: 1.4rem; height: 1.4rem; border-radius: 50%; display: grid; place-items: center; font-size: 0.78rem; font-weight: 800;
}
.drn .drn-rec .ok .ic { background: rgba(74, 222, 128, 0.15); color: var(--green); }
.drn .drn-rec .bad .ic { background: var(--red-soft); color: var(--red); }
.drn .drn-rec p { color: var(--mute); font-size: 0.95rem; }
.drn .drn-list li { position: relative; padding-left: 1.1rem; color: var(--mute); font-size: 0.95rem; }
.drn .drn-list li + li { margin-top: 0.4rem; }
.drn .drn-list li::before { content: ''; position: absolute; left: 0; top: 0.62em; width: 6px; height: 6px; border-radius: 50%; background: var(--red); }
</style>

<div class="drn">
<header class="drn-hero">
<div class="drn-kicker">Sisteme generale</div>
<h1>Sistem <span>Drone</span></h1>
<p class="drn-lede">Ridici o drona in aer si vezi orasul prin camera ei. Personajul tau ramane pe loc cu telecomanda in mana, iar tu pilotezi din ochii dronei: recunoastere, filmari, poze din aer.</p>
<svg class="drn-scene" viewBox="0 0 640 260" role="img" aria-label="Drona care pluteste deasupra orasului si scaneaza solul cu camera">
<defs>
<linearGradient id="drn-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0c1114"/><stop offset="1" stop-color="#140a0b"/></linearGradient>
<linearGradient id="drn-cone" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#67e8f9" stop-opacity="0.32"/><stop offset="1" stop-color="#67e8f9" stop-opacity="0.02"/></linearGradient>
</defs>
<rect class="sky" x="0" y="0" width="640" height="260"/>
<g class="grid"><line x1="0" y1="226" x2="640" y2="226"/><line x1="0" y1="240" x2="640" y2="240"/><line x1="0" y1="256" x2="640" y2="256"/><line x1="320" y1="214" x2="320" y2="260"/><line x1="250" y1="214" x2="200" y2="260"/><line x1="390" y1="214" x2="440" y2="260"/><line x1="180" y1="214" x2="80" y2="260"/><line x1="460" y1="214" x2="560" y2="260"/></g>
<rect class="bld" x="14" y="150" width="46" height="66"/><rect class="bld" x="64" y="120" width="34" height="96"/><rect class="bld" x="102" y="168" width="52" height="48"/><rect class="bld" x="486" y="140" width="40" height="76"/><rect class="bld" x="530" y="112" width="30" height="104"/><rect class="bld" x="564" y="160" width="62" height="56"/>
<rect class="lit" x="72" y="132" width="5" height="5"/><rect class="lit" x="86" y="150" width="5" height="5"/><rect class="lit" x="538" y="126" width="5" height="5"/><rect class="lit" x="548" y="158" width="5" height="5"/><rect class="lit" x="574" y="174" width="5" height="5"/><rect class="lit" x="24" y="166" width="5" height="5"/>
<g class="drift">
<g class="sweep">
<polygon class="cone" points="320,112 250,222 390,222"/>
<line class="scanline" x1="296" y1="112" x2="344" y2="112"/>
<ellipse class="spot" cx="320" cy="222" rx="70" ry="9"/>
</g>
<line class="arm" x1="320" y1="96" x2="256" y2="80"/><line class="arm" x1="320" y1="96" x2="384" y2="80"/><line class="arm" x1="320" y1="96" x2="276" y2="104"/><line class="arm" x1="320" y1="96" x2="364" y2="104"/>
<ellipse class="disc" cx="256" cy="74" rx="34" ry="6"/><ellipse class="disc" cx="384" cy="74" rx="34" ry="6"/><ellipse class="disc" cx="276" cy="98" rx="30" ry="5"/><ellipse class="disc" cx="364" cy="98" rx="30" ry="5"/>
<rect class="blade" x="224" y="72.5" width="64" height="3" rx="1.5"/><rect class="blade b2" x="352" y="72.5" width="64" height="3" rx="1.5"/><rect class="blade b3" x="248" y="96.6" width="56" height="2.8" rx="1.4"/><rect class="blade b4" x="336" y="96.6" width="56" height="2.8" rx="1.4"/>
<rect class="motor" x="251" y="74" width="10" height="9" rx="2"/><rect class="motor" x="379" y="74" width="10" height="9" rx="2"/><rect class="motor" x="271" y="98" width="10" height="9" rx="2"/><rect class="motor" x="359" y="98" width="10" height="9" rx="2"/>
<rect class="body" x="296" y="84" width="48" height="22" rx="9"/>
<circle class="lens" cx="320" cy="110" r="6"/>
<circle class="led" cx="337" cy="90" r="2.2"/>
</g>
<path class="hud" d="M18 34 V18 H34 M606 18 H622 V34 M18 226 V242 H34 M606 242 H622 V226"/>
<g class="reticle"><circle cx="320" cy="222" r="10"/><path d="M304 222 H312 M328 222 H336 M320 206 V214 M320 230 V238"/></g>
<text class="hud-t" x="34" y="48"><tspan class="hud-m">ALTITUDINE </tspan>42 m</text>
<text class="hud-t" x="34" y="66"><tspan class="hud-m">DISTANTA </tspan>180 m</text>
<text class="hud-t" x="508" y="48"><tspan class="hud-m">BATERIE </tspan>86%</text>
<text class="hud-t" x="508" y="66"><tspan class="hud-m">SEMNAL </tspan>92%</text>
</svg>
<ul class="drn-stats">
<li><b>3</b><span>modele de drona</span></li>
<li><b>450 m</b><span>raza maxima fata de tine</span></li>
<li><b>60 min</b><span>baterie maxima (FPV: 20 min)</span></li>
</ul>
</header>
<h2 class="drn-h2">Ce iti trebuie</h2>
<p class="drn-sub">Ai nevoie de doua lucruri in inventar: licenta de zbor si drona.</p>
<ol class="drn-grid2 drn-need">
<li class="drn-card">
<h3 class="drn-h3"><img class="eg-item" src="/items/document.webp" alt="">Licenta operator drone</h3>
<p>O cumperi din <a href="../zona-info/store">Magazinul EG</a>, cu EG Coins, pentru <b>30</b> sau <b>90 de zile</b>. Primesti un document legat de CNP-ul tau.</p>
<p>Documentul trebuie sa fie in inventarul tau si sa nu fie expirat. Licenta cumparata de alt jucator nu te lasa sa zbori.</p>
<span class="drn-path">Magazin EG → Iteme → Licenta operator drone</span>
</li>
<li class="drn-card">
<h3 class="drn-h3"><img class="eg-item" src="/items/drone.webp" alt="">O drona</h3>
<p>Dronele se vand la magazinul <b>DigitalDen</b> din Little Seoul, cu bani din joc. Il gasesti pe harta dupa iconita DigitalDen.</p>
<p>Fara licenta valida drona nu porneste, chiar daca o ai in inventar.</p>
<span class="drn-path">DigitalDen → Drone</span>
</li>
</ol>
<h2 class="drn-h2">Cele trei modele</h2>
<p class="drn-sub">Toate zboara pana la 450 m de tine, fac poze si au busola. Difera prin rezistenta, baterie si viteza.</p>
<div class="drn-grid3">
<div class="drn-card drn-model">
<span class="drn-tag">Standard</span>
<h3 class="drn-h3"><img class="eg-item" src="/items/drone.webp" alt="">Drona</h3>
<p>Drona de baza, echilibrata. Buna pentru recunoastere si filmari ziua.</p>
<ul class="drn-spec">
<li>Rezistenta <b><span class="drn-pips" aria-label="3 lovituri"><i class="on"></i><i class="on"></i><i class="on"></i><i></i></span></b></li>
<li>Baterie <b>60 min</b></li>
<li>Viteza <b>normala</b></li>
<li>Greutate <b>0,5 kg</b></li>
</ul>
</div>
<div class="drn-card drn-model nv">
<span class="drn-tag">Vedere nocturna</span>
<h3 class="drn-h3"><img class="eg-item" src="/items/nvdrone.webp" alt="">Drona NightVision</h3>
<p>Are butonul <b>Vedere nocturna</b> pe ecranul dronei. Cea mai rezistenta dintre cele trei.</p>
<ul class="drn-spec">
<li>Rezistenta <b><span class="drn-pips" aria-label="4 lovituri"><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i></span></b></li>
<li>Baterie <b>60 min</b></li>
<li>Viteza <b>normala</b></li>
<li>Greutate <b>0,5 kg</b></li>
</ul>
</div>
<div class="drn-card drn-model fpv">
<span class="drn-tag">De curse</span>
<h3 class="drn-h3"><img class="eg-item" src="/items/fpvdrone.webp" alt="">Drona FPV</h3>
<p>Mult mai rapida si mai usoara, dar fragila si cu baterie mica. Piloteaz-o cu grija.</p>
<ul class="drn-spec">
<li>Rezistenta <b><span class="drn-pips" aria-label="2 lovituri"><i class="on"></i><i class="on"></i><i></i><i></i></span></b></li>
<li>Baterie <b>20 min</b></li>
<li>Viteza <b>mult mai mare</b></li>
<li>Greutate <b>0,35 kg</b></li>
</ul>
</div>
</div>
<p class="drn-note">Rezistenta = cate izbituri duce drona. La ultima izbitura se prabuseste.</p>
<h2 class="drn-h2">Cum o lansezi</h2>
<ol class="drn-steps">
<li><span class="n">1</span><p><b>Iesi afara.</b> Drona nu porneste din vehicul sau dintr-un interior.</p></li>
<li><span class="n">2</span><p><b>Foloseste drona din inventar.</b> Personajul o ridica si o lanseaza in fata ta. Drona iese din inventar cat timp zbori.</p></li>
<li><span class="n">3</span><p><b>Pilotezi din camera dronei.</b> Personajul ramane pe loc cu telecomanda, iar pe ecran apare interfata de zbor.</p></li>
</ol>
<p class="drn-warn">Poti zbura cu o singura drona odata. Daca ai mai multe drone de acelasi tip, pleaca in zbor cea cu bateria cea mai plina.</p>
<h2 class="drn-h2">Controale de zbor</h2>
<ul class="drn-keys">
<li><span class="k"><kbd>W</kbd><kbd>S</kbd></span><span>Inainte / inapoi</span></li>
<li><span class="k"><kbd>A</kbd><kbd>D</kbd></span><span>Stanga / dreapta</span></li>
<li><span class="k"><kbd>Q</kbd><kbd>E</kbd></span><span>Rotesti drona <span class="nw">(merg si <kbd>←</kbd> <kbd>→</kbd>)</span></span></li>
<li><span class="k"><kbd>Shift</kbd></span><span>Urci</span></li>
<li><span class="k"><kbd>Ctrl</kbd></span><span>Cobori</span></li>
<li><span class="k"><kbd>↑</kbd><kbd>↓</kbd></span><span>Inclini camera in sus / in jos</span></li>
<li><span class="k"><kbd>Scroll</kbd></span><span>Zoom pe camera, 3 trepte</span></li>
<li><span class="k"><kbd>H</kbd></span><span>Ascunzi / arati interfata</span></li>
</ul>
<p class="drn-note">Cu zoom, drona raspunde mai lent la comenzi, ca sa poti filma precis. Merge si cu controller. Lista completa o vezi oricand in joc, din butonul <b>Instructiuni</b>.</p>
<h2 class="drn-h2">Ecranul dronei</h2>
<ul class="drn-hud">
<li><span class="l">Altitudine</span><span class="d">Cat de sus esti fata de sol, in metri.</span></li>
<li><span class="l">Distanta</span><span class="d">Cati metri a zburat drona de la lansare.</span></li>
<li><span class="l">Orizontal / Vertical</span><span class="d">Viteza dronei, in km/h.</span></li>
<li><span class="l">Busola</span><span class="d">Directia in care priveste drona.</span></li>
<li><span class="l">Baterie</span><span class="d">Cat mai poti zbura, in procente.</span></li>
<li><span class="l">Semnal</span><span class="d">Cat mai ai pana la marginea razei de 450 m.</span></li>
<li><span class="l">Coordonate</span><span class="d">Pozitia exacta a dronei pe harta.</span></li>
<li><span class="l">Fa o poza</span><span class="d">Poza ajunge in galeria telefonului. Poti face o poza la fiecare 15 secunde.</span></li>
<li><span class="l">Vedere nocturna</span><span class="d">Doar pe Drona NightVision.</span></li>
<li><span class="l">Opreste</span><span class="d">Opresti drona. Vezi mai jos cum o recuperezi.</span></li>
</ul>
<h2 class="drn-h2">Baterie, semnal si avarii</h2>
<div class="drn-grid3">
<div class="drn-card">
<h3 class="drn-h3">Baterie</h3>
<p>Fiecare drona isi tine bateria ramasa pe item. O vezi in inventar, la <b>Baterie (minute)</b>.</p>
<p>Bateria <b>nu se reincarca</b>. Sub 15% primesti avertisment. La 0% drona se opreste, iar o drona descarcata nu mai porneste.</p>
</div>
<div class="drn-card">
<h3 class="drn-h3">Semnal</h3>
<p>Drona zboara pana la 450 m de tine. Cand semnalul scade sub 25% primesti avertisment si imaginea incepe sa se strice.</p>
<p>Daca treci de 450 m, <b>pierzi drona</b>.</p>
</div>
<div class="drn-card">
<h3 class="drn-h3">Avarii</h3>
<p>Fiecare izbitura iti scade din rezistenta. Dupa o izbitura ai 2 secunde in care nu mai iei avarii.</p>
<p>Drona se prabuseste pe loc daca o impusca cineva sau daca atinge apa. Jucatorii din jur vad si aud explozia.</p>
</div>
</div>
<h2 class="drn-h2">Cum recuperezi drona</h2>
<div class="drn-card">
<ul class="drn-rec">
<li class="ok"><span class="ic">✓</span><p><b>Adu drona la cel mult 5 m de tine</b>, apoi apasa <b>Opreste</b>. Personajul o ridica si itemul revine in inventar cu bateria ramasa.</p></li>
<li class="bad"><span class="ic">✕</span><p><b>Opresti drona departe de tine:</b> primesti o confirmare, iar daca accepti drona se distruge si pierzi itemul.</p></li>
<li class="bad"><span class="ic">✕</span><p><b>Drona se prabuseste</b> (izbituri, gloante, apa) sau <b>iese din raza</b>: pierzi itemul.</p></li>
<li class="bad"><span class="ic">✕</span><p><b>Mori in timp ce pilotezi:</b> drona se opreste. O primesti inapoi doar daca era langa tine.</p></li>
</ul>
</div>
<h2 class="drn-h2">De retinut</h2>
<ul class="drn-list">
<li>Cat timp pilotezi nu poti deschide inventarul, telefonul sau meniul de pauza (<kbd>ESC</kbd>). Iesi din drona cu butonul <b>Opreste</b>.</li>
<li>Chat-ul si HUD-ul se ascund cat timp zbori si revin cand opresti drona.</li>
<li>Ceilalti jucatori iti vad drona si o aud zburand.</li>
</ul>
</div>
