---
outline: false
---

<style>
.vtr {
  --ink: #060607;
  --panel: #0f0f11;
  --panel2: #151518;
  --line: #232327;
  --line2: #303036;
  --text: #f4f4f5;
  --mute: #a1a1aa;
  --dim: #71717a;
  --red: #ef4444;
  --blood: #b91c1c;
  --wine: #3b0a0a;
  --ember: rgba(239, 68, 68, 0.14);
  --brass: #d6a54a;
  --green: #4ade80;
  max-width: 960px;
  margin: 0 auto;
  color: var(--text);
  font-family: Inter, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.vtr *, .vtr *::before, .vtr *::after { box-sizing: border-box; }
.vtr p, .vtr li { margin: 0; line-height: 1.6; color: var(--text); }
.vtr ul, .vtr ol { list-style: none; padding: 0; margin: 0; }
.vtr li + li { margin-top: 0; }
.vtr b { color: #fff; font-weight: 650; }
.vtr a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.vtr a:hover { color: #fecaca; }
.vtr a:focus-visible { outline: 3px solid var(--red); outline-offset: 3px; border-radius: 8px; }
.vtr .mono { font-family: ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; }
/* ---------- hero ---------- */
.vtr .vtr-hero {
  position: relative; overflow: hidden; isolation: isolate;
  background: radial-gradient(120% 90% at 50% 120%, rgba(185, 28, 28, 0.32), transparent 60%), var(--ink);
  border: 1px solid var(--line); border-radius: 22px;
  padding: clamp(1.15rem, 4vw, 2.4rem);
}
.vtr .vtr-hero::after {
  content: ''; position: absolute; inset: 0; z-index: -1; pointer-events: none;
  background: repeating-linear-gradient(0deg, rgba(255, 255, 255, 0.018) 0 1px, transparent 1px 4px);
}
.vtr .vtr-kicker {
  display: inline-flex; align-items: center; gap: 0.5rem; margin-bottom: 0.7rem;
  font: 700 0.74rem/1.2 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace;
  letter-spacing: 0.18em; text-transform: uppercase; color: var(--red);
}
.vtr .vtr-kicker::before { content: ''; width: 8px; height: 8px; border-radius: 50%; background: var(--red); box-shadow: 0 0 0 4px var(--ember); animation: vtr-rec 1.6s steps(1, end) infinite; }
@keyframes vtr-rec { 0%, 60% { opacity: 1; } 61%, 100% { opacity: 0.25; } }
.vtr .vtr-hero h1 {
  margin: 0 0 0.8rem; padding: 0; border: 0; color: #fff;
  font-size: clamp(2.1rem, 7vw, 3.6rem); line-height: 1.02; font-weight: 850; letter-spacing: -0.035em;
}
.vtr .vtr-hero h1 span { color: var(--red); }
.vtr .vtr-lede { max-width: 62ch; color: var(--mute); font-size: 1.05rem; }
.vtr .vtr-chips { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1.1rem; }
.vtr .vtr-chips li {
  display: inline-flex; align-items: baseline; gap: 0.4rem;
  background: rgba(15, 15, 17, 0.9); border: 1px solid var(--line2); border-radius: 999px; padding: 0.3rem 0.8rem;
  font-size: 0.85rem; color: var(--mute);
}
.vtr .vtr-chips b { font-size: 1rem; font-variant-numeric: tabular-nums; }
/* map */
.vtr .vtr-mapbox { margin-top: 1.3rem; border: 1px solid var(--line2); border-radius: 16px; overflow: hidden; background: #060a10; }
.vtr .vtr-map { display: block; width: 100%; height: auto; }
.vtr-map .sea { fill: #060a10; }
.vtr-map .wave { fill: none; stroke: #13202c; stroke-width: 1; }
.vtr-map .land { fill: #16161a; stroke: #2e2e35; stroke-width: 1.2; }
.vtr-map .street { stroke: #1b1b20; stroke-width: 1; }
.vtr-map .water { fill: none; stroke: #060a10; stroke-linecap: round; }
.vtr-map .frame { fill: #0a0a0c; stroke: #26262c; stroke-width: 1; }
.vtr-map .ttl { font: 700 9px ui-monospace, Menlo, Consolas, monospace; letter-spacing: 0.16em; fill: #52525b; }
.vtr-map .lbl { font: 700 10.5px Inter, system-ui, sans-serif; fill: #e4e4e7; paint-order: stroke; stroke: #060607; stroke-width: 3px; }
.vtr-map .pts { font: 700 9px ui-monospace, Menlo, Consolas, monospace; fill: #a1a1aa; paint-order: stroke; stroke: #060607; stroke-width: 3px; }
.vtr-map .z { stroke-width: 1.6; fill-opacity: 0.3; animation: vtr-zone 6s ease-in-out infinite; }
.vtr-map .z.d2 { animation-delay: -1.5s; }
.vtr-map .z.d3 { animation-delay: -3s; }
.vtr-map .z.d4 { animation-delay: -4.5s; }
@keyframes vtr-zone { 0%, 100% { fill-opacity: 0.22; } 50% { fill-opacity: 0.46; } }
.vtr-map .c-violet { fill: #8b53cf; stroke: #a78bfa; }
.vtr-map .c-cyan { fill: #33aaaa; stroke: #5eead4; }
.vtr-map .c-green { fill: #2c7d50; stroke: #4ade80; }
.vtr-map .c-orange { fill: #ff7f33; stroke: #fdba74; }
.vtr-map .c-red { fill: #c0382b; stroke: #f87171; }
.vtr-map .c-gold { fill: #fcd54a; stroke: #fde68a; }
.vtr-map .c-free { fill: #a8a8a8; stroke: #d4d4d8; stroke-dasharray: 4 3; }
.vtr-map .war-ring { fill: none; stroke: var(--red); stroke-width: 2; stroke-dasharray: 6 4; transform-box: fill-box; transform-origin: center; animation: vtr-spin 14s linear infinite; }
.vtr-map .war-fill { fill: rgba(239, 68, 68, 0.12); }
.vtr-map .sweep { fill: url(#vtr-sweep); transform-box: view-box; transform-origin: 185.4px 297.2px; animation: vtr-spin 3.2s linear infinite; }
.vtr-map .pulse { fill: none; stroke: var(--red); stroke-width: 1.5; transform-box: fill-box; transform-origin: center; animation: vtr-pulse 2.6s ease-out infinite; }
.vtr-map .camp { font: 800 7px ui-monospace, Menlo, Consolas, monospace; text-anchor: middle; fill: #fff; }
.vtr-map .campA { fill: #1d4ed8; }
.vtr-map .campB { fill: var(--blood); }
.vtr-map .fx { fill: #fff; animation: vtr-blip 2.4s steps(1, end) infinite; }
.vtr-map .fx:nth-of-type(2n) { animation-delay: -0.8s; }
.vtr-map .fx:nth-of-type(3n) { animation-delay: -1.6s; }
@keyframes vtr-spin { to { transform: rotate(360deg); } }
@keyframes vtr-pulse { 0% { opacity: 0.9; transform: scale(0.35); } 100% { opacity: 0; transform: scale(1.25); } }
@keyframes vtr-blip { 0%, 55% { opacity: 0.95; } 56%, 100% { opacity: 0.15; } }
.vtr .vtr-legend { display: flex; flex-wrap: wrap; gap: 0.4rem 1.1rem; padding: 0.7rem 0.95rem; border-top: 1px solid var(--line); background: var(--panel); }
.vtr .vtr-legend li { display: inline-flex; align-items: center; gap: 0.45rem; font-size: 0.82rem; color: var(--mute); }
.vtr .vtr-legend i { flex: none; width: 0.85rem; height: 0.85rem; border-radius: 3px; font-style: normal; }
.vtr .vtr-legend .own { background: linear-gradient(135deg, #8b53cf, #33aaaa 50%, #ff7f33); }
.vtr .vtr-legend .free { background: #a8a8a8; opacity: 0.6; outline: 1px dashed #d4d4d8; outline-offset: -1px; }
.vtr .vtr-legend .war { border-radius: 50%; border: 2px dashed var(--red); }
@media (prefers-reduced-motion: reduce) {
  .vtr .vtr-kicker::before, .vtr-map .z, .vtr-map .war-ring, .vtr-map .sweep, .vtr-map .pulse, .vtr-map .fx { animation: none; }
  .vtr-map .pulse, .vtr-map .sweep { opacity: 0; }
}
/* ---------- sections ---------- */
.vtr .vtr-h2 {
  display: flex; align-items: baseline; gap: 0.7rem;
  margin: 3rem 0 0.6rem; padding: 0; border: 0;
  font-size: 1.5rem; line-height: 1.25; font-weight: 750; letter-spacing: -0.015em; color: #fff;
}
.vtr .vtr-h2 span { font: 700 0.8rem/1 ui-monospace, Menlo, Consolas, monospace; color: var(--red); letter-spacing: 0.1em; }
.vtr .vtr-sub { color: var(--mute); max-width: 68ch; margin-bottom: 1.1rem; }
.vtr .vtr-h3 { margin: 0 0 0.35rem; padding: 0; border: 0; font-size: 1.06rem; line-height: 1.3; font-weight: 700; color: #fff; }
.vtr .vtr-card { background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 1.1rem 1.2rem; }
.vtr .vtr-card > p { color: var(--mute); font-size: 0.96rem; }
.vtr .vtr-card > p + p { margin-top: 0.5rem; }
.vtr .vtr-note { margin-top: 0.85rem; color: var(--mute); font-size: 0.92rem; }
.vtr .vtr-ticks { display: grid; gap: 0.5rem; }
.vtr .vtr-ticks li { position: relative; padding-left: 1.2rem; color: var(--mute); font-size: 0.95rem; line-height: 1.5; }
.vtr .vtr-ticks li::before { content: ''; position: absolute; left: 0; top: 0.55em; width: 7px; height: 7px; transform: rotate(45deg); background: var(--red); }
.vtr .vtr-card .vtr-ticks { margin-top: 0.7rem; }
/* routes to a territory */
.vtr .vtr-routes { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 230px), 1fr)); gap: 0.8rem; }
.vtr .vtr-routes li { background: linear-gradient(180deg, var(--panel2), var(--panel)); border: 1px solid var(--line); border-radius: 16px; padding: 1rem 1.15rem 1.1rem; }
.vtr .vtr-routes .ico { display: grid; place-items: center; width: 2.3rem; height: 2.3rem; margin-bottom: 0.7rem; border-radius: 12px; background: var(--wine); color: var(--red); border: 1px solid #5b1414; }
.vtr .vtr-routes .ico svg { width: 1.2rem; height: 1.2rem; }
.vtr .vtr-routes li.gold .ico { background: #141005; color: var(--brass); border-color: #4a3a17; }
.vtr .vtr-routes p { color: var(--mute); font-size: 0.94rem; }
/* territory dossiers */
.vtr .vtr-dossier { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 270px), 1fr)); gap: 0.8rem; }
.vtr .vtr-dossier > li {
  position: relative; background: var(--panel); border: 1px solid var(--line); border-radius: 16px;
  padding: 1rem 1.15rem 1.05rem; border-left: 3px solid var(--sw, var(--blood));
}
.vtr .vtr-dossier .hd { display: flex; justify-content: space-between; align-items: baseline; gap: 0.6rem; }
.vtr .vtr-dossier .rg { font: 700 0.68rem/1.2 ui-monospace, Menlo, Consolas, monospace; letter-spacing: 0.14em; text-transform: uppercase; color: var(--dim); }
.vtr .vtr-dossier .nm { display: block; margin-top: 0.15rem; font-size: 1.12rem; font-weight: 780; color: #fff; line-height: 1.25; }
.vtr .vtr-dossier .pt { font: 800 1.35rem/1 ui-monospace, Menlo, Consolas, monospace; color: #fff; font-variant-numeric: tabular-nums; white-space: nowrap; }
.vtr .vtr-dossier .pt small { font-size: 0.68rem; color: var(--dim); margin-left: 0.15rem; }
.vtr .vtr-dossier .bar { height: 5px; margin: 0.65rem 0 0.75rem; border-radius: 999px; background: #1f1f24; overflow: hidden; }
.vtr .vtr-dossier .bar i { display: block; height: 100%; border-radius: 999px; background: linear-gradient(90deg, var(--blood), var(--red)); font-style: normal; }
.vtr .vtr-dossier .pk { display: inline-block; margin-bottom: 0.3rem; font: 700 0.66rem/1.2 ui-monospace, Menlo, Consolas, monospace; letter-spacing: 0.12em; text-transform: uppercase; color: var(--brass); }
.vtr .vtr-dossier .ds { color: var(--mute); font-size: 0.93rem; line-height: 1.5; }
.vtr .vtr-dossier .tx { margin-top: 0.55rem; font-size: 0.8rem; color: var(--dim); }
/* protection tax ledger */
.vtr .vtr-duo { display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(0, 1fr); gap: 0.8rem; align-items: start; }
@media (max-width: 760px) { .vtr .vtr-duo { grid-template-columns: minmax(0, 1fr); } }
.vtr .vtr-ledger { background: #0b0b0d; border: 1px solid #3a3222; border-radius: 16px; padding: 0.7rem clamp(0.75rem, 3vw, 1.1rem) 0.9rem; box-shadow: inset 0 0 0 4px #121008; }
.vtr .vtr-ledger .lh { display: flex; justify-content: space-between; gap: 0.6rem; padding: 0.35rem 0 0.55rem; border-bottom: 1px solid #3a3222; font: 700 0.7rem/1.2 ui-monospace, Menlo, Consolas, monospace; letter-spacing: 0.14em; text-transform: uppercase; color: var(--brass); }
.vtr .vtr-ledger .row { display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: 0.15rem 0.8rem; padding: 0.55rem 0; border-bottom: 1px dashed #2c2820; }
.vtr .vtr-ledger .row:last-of-type { border-bottom: 0; }
.vtr .vtr-ledger .who { font-weight: 650; color: #fff; font-size: 0.92rem; }
.vtr .vtr-ledger .d { font: 700 0.8rem/1.4 ui-monospace, Menlo, Consolas, monospace; color: var(--brass); }
.vtr .vtr-ledger .w { grid-column: 1 / -1; color: var(--dim); font-size: 0.8rem; }
.vtr .vtr-pills { display: flex; flex-wrap: wrap; gap: 0.35rem; margin-top: 0.8rem; }
.vtr .vtr-pills li { font: 700 0.78rem/1 ui-monospace, Menlo, Consolas, monospace; color: var(--mute); background: var(--panel2); border: 1px solid var(--line2); border-radius: 8px; padding: 0.4rem 0.55rem; }
.vtr .vtr-pills li.on { color: #fff; background: var(--blood); border-color: var(--blood); }
/* war timeline */
.vtr .vtr-line { position: relative; display: grid; gap: 0.75rem; padding-left: 2.6rem; }
.vtr .vtr-line::before { content: ''; position: absolute; left: 0.95rem; top: 0.6rem; bottom: 0.6rem; width: 2px; background: linear-gradient(180deg, var(--line2), var(--blood) 55%, var(--line2)); }
.vtr .vtr-line > li { position: relative; background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 0.95rem 1.15rem 1rem; }
.vtr .vtr-line > li::before {
  content: attr(data-n); position: absolute; left: -2.6rem; top: 0.9rem; width: 1.95rem; height: 1.95rem; border-radius: 50%;
  display: grid; place-items: center; font: 800 0.8rem/1 ui-monospace, Menlo, Consolas, monospace; color: #fff;
  background: var(--ink); border: 2px solid var(--blood);
}
.vtr .vtr-line > li.hot { border-color: #5b1414; background: linear-gradient(110deg, #1a0808, var(--panel) 60%); }
.vtr .vtr-line > li.hot::before { background: var(--blood); }
.vtr .vtr-line .tm { display: inline-block; margin-bottom: 0.25rem; font: 700 0.7rem/1.2 ui-monospace, Menlo, Consolas, monospace; letter-spacing: 0.14em; text-transform: uppercase; color: var(--red); }
.vtr .vtr-line > li > p { color: var(--mute); font-size: 0.95rem; }
.vtr .vtr-line > li > p + p { margin-top: 0.45rem; }
.vtr .vtr-line .vtr-ticks { margin-top: 0.55rem; }
/* out / in */
.vtr .vtr-split { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr)); gap: 0.8rem; }
.vtr .vtr-split .out { border-color: #5b1414; background: linear-gradient(160deg, #1a0808, var(--panel) 55%); }
.vtr .vtr-split .in { border-color: #14532d; background: linear-gradient(160deg, #07160d, var(--panel) 55%); }
.vtr .vtr-split .in .vtr-ticks li::before { background: var(--green); }
.vtr .vtr-split .tag { display: inline-block; margin-bottom: 0.45rem; font: 700 0.7rem/1.2 ui-monospace, Menlo, Consolas, monospace; letter-spacing: 0.14em; text-transform: uppercase; }
.vtr .vtr-split .out .tag { color: var(--red); }
.vtr .vtr-split .in .tag { color: var(--green); }
.vtr .vtr-win { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 0.6rem; margin-top: 0.8rem; }
.vtr .vtr-win li { background: var(--panel2); border: 1px solid var(--line); border-radius: 14px; padding: 0.8rem 0.9rem; }
.vtr .vtr-win .k { display: block; font: 700 0.68rem/1.2 ui-monospace, Menlo, Consolas, monospace; letter-spacing: 0.12em; text-transform: uppercase; color: var(--dim); margin-bottom: 0.3rem; }
.vtr .vtr-win .v { display: block; font-weight: 700; color: #fff; font-size: 0.95rem; line-height: 1.4; }
@media (max-width: 640px) { .vtr .vtr-win { grid-template-columns: minmax(0, 1fr); } }
/* overlord */
.vtr .vtr-over { display: grid; grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr); gap: 0.8rem; align-items: stretch; }
@media (max-width: 760px) { .vtr .vtr-over { grid-template-columns: minmax(0, 1fr); } }
.vtr .vtr-vs { display: grid; place-items: center; background: radial-gradient(circle at 50% 40%, rgba(214, 165, 74, 0.12), var(--panel) 70%); border-color: #3d3217; }
.vtr .vtr-vs svg { width: 100%; max-width: 300px; height: auto; }
.vtr-vs .side { font: 700 9px ui-monospace, Menlo, Consolas, monospace; letter-spacing: 0.12em; fill: #a1a1aa; text-anchor: middle; }
.vtr-vs .big { font: 900 22px Inter, system-ui, sans-serif; fill: var(--brass); text-anchor: middle; }
/* closing */
.vtr .vtr-end {
  margin-top: 2.6rem; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 0.8rem;
  padding: 1.1rem 1.25rem; border-radius: 16px; border: 1px solid #4c1414; background: linear-gradient(110deg, #1d0808, var(--panel) 70%);
}
.vtr .vtr-end p { color: var(--mute); max-width: 56ch; }
.vtr .vtr-end a.btn { display: inline-flex; align-items: center; text-decoration: none; font-weight: 700; color: #fff; background: var(--blood); border-radius: 999px; padding: 0.55rem 1.1rem; }
.vtr .vtr-end a.btn:hover { background: #991b1b; color: #fff; }
</style>

<div class="vtr">
<section class="vtr-hero">
<p class="vtr-kicker">Viata ilegala / Teritorii</p>
<h1>Teritorii &amp; <span>Razboaie</span></h1>
<p class="vtr-lede">Los Santos, Sandy Shores si insula Cayo Perico sunt impartite in 8 teritorii. Familia care tine un teritoriu primeste puncte in clasament si un bonus pentru fiecare membru. Cine il vrea il ia cu arma, intr-un razboi programat din Tableta Sentinel.</p>
<ul class="vtr-chips">
<li><b>8</b> teritorii</li>
<li><b>3.600</b> puncte pe harta</li>
<li><b>60</b> minute de lupta maxim</li>
<li><b>5</b> zile de protectie dupa razboi</li>
</ul>
<div class="vtr-mapbox">
<svg class="vtr-map" viewBox="0 0 640 480" role="img" aria-label="Harta schematica a celor 8 teritorii, colorate dupa familia care le tine. Pe Grove Street pulseaza un cerc de razboi cu cele doua zone de asteptare.">
<defs>
<radialGradient id="vtr-sweep" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(185.4 297.2) scale(25)"><stop offset="0" stop-color="#ef4444" stop-opacity="0.55"/><stop offset="1" stop-color="#ef4444" stop-opacity="0"/></radialGradient>
<clipPath id="vtr-land"><path d="M44 20 H345 V470 H232 L226 448 L196 448 L190 470 H96 L92 452 L22 452 L22 352 L60 340 L70 324 C58 300 48 280 44 262 C40 240 30 222 26 200 C30 160 40 110 44 70 Z"/></clipPath>
</defs>
<rect class="sea" x="0" y="0" width="640" height="480"/>
<path class="wave" d="M6 120 q6 -4 12 0 t12 0 M4 260 q6 -4 12 0 t12 0 M30 300 q6 -4 12 0 M8 470 q6 -4 12 0 t12 0 t12 0 M120 474 q6 -4 12 0 t12 0"/>
<path class="land" d="M44 20 H345 V470 H232 L226 448 L196 448 L190 470 H96 L92 452 L22 452 L22 352 L60 340 L70 324 C58 300 48 280 44 262 C40 240 30 222 26 200 C30 160 40 110 44 70 Z"/>
<g clip-path="url(#vtr-land)">
<path class="street" d="M0 60 H345 M0 100 H345 M0 140 H345 M0 180 H345 M0 220 H345 M0 260 H345 M0 300 H345 M0 340 H345 M0 380 H345 M0 420 H345 M60 0 V480 M100 0 V480 M140 0 V480 M180 0 V480 M220 0 V480 M260 0 V480 M300 0 V480 M40 150 L330 40 M60 400 L300 230"/>
<path class="water" stroke-width="5" d="M266 110 C258 190 252 260 249 330 C247 372 240 398 234 410"/>
<path class="water" stroke-width="7" d="M92 406 C150 398 220 412 345 400"/>
</g>
<text class="ttl" x="338" y="438" text-anchor="end">LOS SANTOS</text>
<rect class="z c-violet" x="20.8" y="28.6" width="210" height="70" rx="3"/>
<text class="lbl" x="125.8" y="62" text-anchor="middle">Vinewood</text>
<text class="pts" x="125.8" y="76" text-anchor="middle">300 p</text>
<rect class="z c-cyan d2" x="45.9" y="212.1" width="60" height="90" rx="3"/>
<text class="lbl" x="75.9" y="252" text-anchor="middle">Vespucci</text>
<text class="pts" x="75.9" y="266" text-anchor="middle">400 p</text>
<rect class="z c-green d3" x="161.2" y="266.3" width="90" height="70" rx="3"/>
<rect class="z c-orange d4" x="259.3" y="161.1" width="70" height="50" rx="3"/>
<rect class="z c-orange d4" x="292.6" y="276.3" width="48" height="38" rx="3"/>
<text class="lbl" x="294.3" y="154" text-anchor="middle">Mirror Park</text>
<text class="lbl" x="316.6" y="328" text-anchor="middle">Amarillo</text>
<text class="pts" x="294.3" y="190" text-anchor="middle">200 p</text>
<rect class="z c-red d2" x="197.9" y="404.7" width="17" height="60" rx="2"/>
<text class="lbl" x="192" y="430" text-anchor="end">Spalatorie</text>
<text class="pts" x="192" y="443" text-anchor="end">750 p</text>
<circle class="war-fill" cx="185.4" cy="297.2" r="25"/>
<path class="sweep" d="M185.4 297.2 L210.4 297.2 A25 25 0 0 0 203.1 279.5 Z"/>
<circle class="war-ring" cx="185.4" cy="297.2" r="25"/>
<circle class="pulse" cx="185.4" cy="297.2" r="25"/>
<circle class="fx" cx="178" cy="306" r="1.6"/><circle class="fx" cx="190" cy="289" r="1.6"/><circle class="fx" cx="194" cy="303" r="1.6"/><circle class="fx" cx="181" cy="292" r="1.6"/>
<circle class="campA" cx="174.4" cy="313.7" r="5"/><text class="camp" x="174.4" y="316.2">A</text>
<circle class="campB" cx="179.7" cy="281.3" r="5"/><text class="camp" x="179.7" y="283.8">B</text>
<text class="lbl" x="232" y="352" text-anchor="middle">Grove Street</text>
<text class="pts" x="232" y="364" text-anchor="middle">500 p</text>
<rect class="frame" x="360" y="20" width="268" height="200" rx="12"/>
<path class="land" d="M372 32 H616 V208 H372 Z"/>
<ellipse cx="420" cy="62" rx="44" ry="20" fill="#060a10"/>
<path class="street" d="M372 120 H616 M372 160 H616 M440 32 V208 M520 32 V208 M580 32 V208 M380 200 L610 90"/>
<rect class="z c-free" x="430" y="96.5" width="140" height="77" rx="3"/>
<text class="lbl" x="500" y="134" text-anchor="middle">Sandy Shores</text>
<text class="pts" x="500" y="148" text-anchor="middle">450 p / liber</text>
<text class="ttl" x="616" y="202" text-anchor="end">BLAINE COUNTY</text>
<rect class="frame" x="360" y="236" width="268" height="234" rx="12"/>
<path class="land" d="M416 268 C450 258 490 252 524 256 C552 268 572 284 578 304 C586 330 588 350 584 364 C574 396 562 414 548 424 C530 440 508 448 488 448 C462 446 440 432 428 412 C412 392 398 366 392 340 C390 316 398 288 416 268 Z"/>
<path class="street" d="M400 320 H580 M410 380 H570 M470 260 V445 M530 262 V440"/>
<rect class="z c-violet d3" x="492.9" y="325" width="38.4" height="60" rx="3"/>
<rect class="z c-violet d3" x="514.2" y="273.8" width="24" height="24" rx="3"/>
<rect class="z c-gold" x="534.9" y="326.1" width="44.4" height="60" rx="3"/>
<text class="lbl" x="512" y="402" text-anchor="middle">Cayo Crafting</text>
<text class="pts" x="512" y="414" text-anchor="middle">500 p</text>
<text class="lbl" x="560" y="308" text-anchor="middle">Cayo Plantatii</text>
<text class="pts" x="560" y="320" text-anchor="middle">500 p</text>
<text class="ttl" x="372" y="462">CAYO PERICO</text>
</svg>
<ul class="vtr-legend">
<li><i class="own"></i>Zona colorata: are stapan, in culoarea familiei</li>
<li><i class="free"></i>Argintiu: teritoriu liber</li>
<li><i class="war"></i>Cerc rosu: razboi in desfasurare</li>
</ul>
</div>
</section>
<h2 class="vtr-h2" id="cum-iei-un-teritoriu"><span>01</span>Cum ajunge un teritoriu la tine</h2>
<p class="vtr-sub">Teritoriile sunt un sistem real in joc, nu doar o intelegere intre familii. Le vezi pe harta mare, in culoarea familiei care le tine, si in Tableta Sentinel, la <b>Teritorii</b>.</p>
<ul class="vtr-routes">
<li class="gold"><span class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2 3 6v6c0 5 4 9 9 10 5-1 9-5 9-10V6z"/><path d="m9 12 2 2 4-4"/></svg></span><h3 class="vtr-h3">De la Sindicat</h3><p>Un teritoriu liber nu se ataca. Sindicatul il da direct unei familii, fara razboi. Tot Sindicatul poate lua inapoi un teritoriu.</p></li>
<li><span class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14.5 17.5 3 6V3h3l11.5 11.5"/><path d="m13 19 6-6"/><path d="m16 16 4 4"/><path d="m19 21 2-2"/></svg></span><h3 class="vtr-h3">Prin razboi</h3><p>Seful familiei declara razboi din tableta pe un teritoriu care are deja stapan. Daca atacatorii castiga, teritoriul trece la ei pe loc.</p></li>
<li><span class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m11 17 2 2a1 1 0 1 0 3-3"/><path d="m14 14 2.5 2.5a1 1 0 1 0 3-3l-3.88-3.88a3 3 0 0 0-4.24 0l-.88.88a1 1 0 1 1-3-3l2.81-2.81a5.79 5.79 0 0 1 7.06-.87l.47.28a2 2 0 0 0 1.42.25L21 4"/><path d="m21 3 1 11h-2"/><path d="M3 3 2 14l6.5 6.5a1 1 0 1 0 3-3"/><path d="M3 4h8"/></svg></span><h3 class="vtr-h3">Prin intelegere</h3><p>Doua mafii pot schimba sau vinde un teritoriu intre ele. Anuntati Sindicatul, altfel intelegerea nu e recunoscuta. Sindicatul muta apoi teritoriul la noul stapan.</p></li>
</ul>
<h2 class="vtr-h2" id="cele-8-teritorii"><span>02</span>Cele 8 teritorii</h2>
<p class="vtr-sub">Cat timp tii un teritoriu, punctele lui intra in scorul familiei. Bonusul merge la fiecare membru al familiei, oriunde s-ar afla, nu doar pe teritoriu. Doua teritorii cu bonus pe acelasi produs se aduna. Cat valoreaza acum fiecare bonus vezi in tableta, la <b>Teritorii</b>.</p>
<ul class="vtr-dossier">
<li style="--sw: #c0382b"><div class="hd"><div><span class="rg">Los Santos / port</span><span class="nm">Spalatorie</span></div><span class="pt">750<small>p</small></span></div><div class="bar"><i style="width: 100%"></i></div><span class="pk">Spalare de bani</span><p class="ds">Cand speli bani murdari, familia ta pierde un procent mai mic decat restul orasului.</p><p class="tx">Fara taxa de protectie.</p></li>
<li style="--sw: #2c7d50"><div class="hd"><div><span class="rg">Los Santos / sud</span><span class="nm">Grove Street</span></div><span class="pt">500<small>p</small></span></div><div class="bar"><i style="width: 66.7%"></i></div><span class="pk">Bonus livrari</span><p class="ds">Livrarile de cocaina iti aduc mai multi bani murdari.</p><p class="tx">Cu taxa de protectie.</p></li>
<li style="--sw: #fcd54a"><div class="hd"><div><span class="rg">Cayo Perico</span><span class="nm">Cayo Plantatii</span></div><span class="pt">500<small>p</small></span></div><div class="bar"><i style="width: 66.7%"></i></div><span class="pk">Recolta dubla</span><p class="ds">Ai o sansa ca recolta de tutun, frunze de coca sau muguri de iarba sa iasa dubla.</p><p class="tx">Cu taxa de protectie.</p></li>
<li style="--sw: #8b53cf"><div class="hd"><div><span class="rg">Cayo Perico</span><span class="nm">Cayo Crafting</span></div><span class="pt">500<small>p</small></span></div><div class="bar"><i style="width: 66.7%"></i></div><span class="pk">Productie dubla</span><p class="ds">Ai o sansa sa iti iasa dublu plicul de cocaina, iarba sau metamfetamina, ori pachetul de tigari.</p><p class="tx">Cu taxa de protectie.</p></li>
<li style="--sw: #a8a8a8"><div class="hd"><div><span class="rg">Blaine County</span><span class="nm">Sandy Shores</span></div><span class="pt">450<small>p</small></span></div><div class="bar"><i style="width: 60%"></i></div><span class="pk">Bonus livrari</span><p class="ds">Livrarile de heroina iti aduc mai multi bani murdari.</p><p class="tx">Cu taxa de protectie.</p></li>
<li style="--sw: #33aaaa"><div class="hd"><div><span class="rg">Los Santos / vest</span><span class="nm">Vespucci</span></div><span class="pt">400<small>p</small></span></div><div class="bar"><i style="width: 53.3%"></i></div><span class="pk">Bonus livrari</span><p class="ds">Livrarile de metamfetamina iti aduc mai multi bani murdari.</p><p class="tx">Cu taxa de protectie.</p></li>
<li style="--sw: #8b53cf"><div class="hd"><div><span class="rg">Los Santos / nord</span><span class="nm">Vinewood</span></div><span class="pt">300<small>p</small></span></div><div class="bar"><i style="width: 40%"></i></div><span class="pk">Bonus livrari</span><p class="ds">Livrarile de iarba iti aduc mai multi bani murdari.</p><p class="tx">Cu taxa de protectie.</p></li>
<li style="--sw: #ff7f33"><div class="hd"><div><span class="rg">Los Santos / est</span><span class="nm">Mirror Park &amp; Amarillo</span></div><span class="pt">200<small>p</small></span></div><div class="bar"><i style="width: 26.7%"></i></div><span class="pk">Bonus livrari</span><p class="ds">Livrarile de timbre LSD si de pachete de tigari iti aduc mai multi bani murdari.</p><p class="tx">Cu taxa de protectie. Pe harta are doua zone.</p></li>
</ul>
<p class="vtr-note">Despre livrari, plantatii si laboratoare afli mai multe pe pagina <a href="/viata-ilegala/droguri-efecte">Droguri &amp; Efecte</a>. Culorile de pe harta de mai sus sunt doar un exemplu: in joc, fiecare familie are culoarea aleasa de Sindicat.</p>
<h2 class="vtr-h2" id="taxa-de-protectie"><span>03</span>Taxa de protectie</h2>
<div class="vtr-duo">
<div class="vtr-card">
<p>Fiecare teritoriu, in afara de Spalatorie, are o taxa de protectie pe zi. Banii se dau in RP, de la om la om. Tableta doar tine evidenta: cine a platit, pentru ce teritoriu si pe cate zile.</p>
<ul class="vtr-ticks">
<li>Orice membru al familiei care tine teritoriul poate trece o plata, nu doar seful.</li>
<li>Alegi perioada, iar suma se calculeaza singura, dupa taxa zilnica a teritoriului.</li>
<li>Vezi doar platile familiei tale. Sindicatul le vede pe toate si e singurul care poate sterge o plata.</li>
<li>Ai statistici pe 24 de ore, 3, 7, 14, 21 si 30 de zile, un grafic pe ultimele 30 de zile si topul celor mai buni 10 colectori.</li>
</ul>
<p class="vtr-note">Regulamentul iti cere sa pazesti livratorii de pe teritoriile tale si sa strangi taxele: intre <b>20:00 si 02:00</b> in Los Santos si intre <b>18:00 si 00:00</b> pe Cayo Perico.</p>
</div>
<div class="vtr-ledger" aria-label="Exemplu de registru de taxe">
<div class="lh"><span>Registru taxe</span><span>Teritoriu</span></div>
<div class="row"><span class="who">Atelier auto din zona</span><span class="d">7 zile</span><span class="w">Grove Street / trecut de un membru</span></div>
<div class="row"><span class="who">Barul de pe colt</span><span class="d">3 zile</span><span class="w">Vespucci / trecut de un membru</span></div>
<div class="row"><span class="who">Vanzatorul ambulant</span><span class="d">1 zi</span><span class="w">Vinewood / trecut de sef</span></div>
<ul class="vtr-pills" aria-label="Perioade de plata">
<li>1 zi</li><li>2 zile</li><li class="on">3 zile</li><li>5 zile</li><li>7 zile</li>
</ul>
</div>
</div>
<h2 class="vtr-h2" id="razboiul-pas-cu-pas"><span>04</span>Razboiul, pas cu pas</h2>
<p class="vtr-sub">Serverul face totul singur: programarea, lista de luptatori, eliminarile, castigatorul si plata. Regulile complete sunt in <a href="/zona-info/regulament-mafii">Regulamentul Mafiilor</a>, capitolul 4.</p>
<ol class="vtr-line">
<li data-n="1"><span class="tm">Declararea</span><h3 class="vtr-h3">Seful alege tinta</h3><p>Doar seful familiei declara razboi, din tableta, si doar pe un teritoriu care are stapan. La declarare se retine o <b>garantie in bani murdari</b>: intai din seiful familiei, iar daca nu ajunge, din inventarul sefului.</p><ul class="vtr-ticks"><li>Nu poti ataca un teritoriu aflat in protectie.</li><li>Nu poti declara daca tu sau adversarul sunteti deja intr-un razboi.</li><li>Familiile care au terminat un razboi in ultima ora nu pot declara si nu pot fi atacate.</li></ul></li>
<li data-n="2"><span class="tm">Alegerea datei / 12 ore</span><h3 class="vtr-h3">Aparatorul alege ziua</h3><p>Sistemul propune 3 zile la rand, incepand de a doua zi. Nu se lupta niciodata in ziua declararii. Seful familiei atacate are <b>12 ore</b> sa aleaga ziua si ora de start, intre <b>19:00 si 22:00</b>.</p><p>Daca nu alege la timp, razboiul se pune singur in prima zi propusa, la <b>21:00</b>. Pana se alege data, tableta familiei atacate se deschide direct la Teritorii.</p></li>
<li data-n="3"><span class="tm">Pregatirea / 10 minute</span><h3 class="vtr-h3">Va strangeti in zona de asteptare</h3><p>Fiecare tabara primeste pe harta zona ei de asteptare: A pentru atacatori, B pentru aparatori. Intra in zona si ramai acolo. La finalul pregatirii, doar cine e in zona intra in lupta.</p><ul class="vtr-ticks"><li>Nu exista limita de luptatori.</li><li>O tabara fara niciun om in zona pierde prin neprezentare.</li></ul></li>
<li data-n="4" class="hot"><span class="tm">Lupta / maxim 60 de minute</span><h3 class="vtr-h3">Cercul de razboi</h3><p>Zonele de asteptare sunt in interiorul cercului, asa ca lupta incepe pe loc. La marginea cercului esti tras inapoi, pe jos sau cu masina: nu poti fugi din lupta.</p><ul class="vtr-ticks"><li>In cerc, furtul e legal cat tine lupta.</li><li>Nimeni din afara cercului nu poate trage inauntru.</li><li>Pe ecran vezi echipele, cati luptatori mai sunt in viata de fiecare parte si timpul ramas.</li><li>Cine nu lupta si intra in cerc primeste avertisment sa plece.</li></ul></li>
<li data-n="5"><span class="tm">Finalul</span><h3 class="vtr-h3">Plata si protectia</h3><p>Castigatorul ia garantia, in bani murdari, direct in inventarul membrului cu cel mai mare grad aflat online. Daca acela nu are loc, suma trece la urmatorul. Daca nu e nimeni online, suma se pierde.</p><ul class="vtr-ticks"><li>Teritoriul intra <b>5 zile</b> in protectie: nimeni nu il poate ataca.</li><li>Familiile care au luptat au o pauza de <b>o ora</b>: nu declara si nu pot fi atacate.</li></ul></li>
</ol>
<h2 class="vtr-h2" id="cine-ramane-in-picioare"><span>05</span>Cine ramane in picioare</h2>
<div class="vtr-split">
<div class="vtr-card out"><span class="tag">Esti eliminat cand</span><ul class="vtr-ticks"><li>primesti o <b>lovitura fatala</b>, la cap sau la gat;</li><li>te <b>deconectezi</b>: la reconectare esti scos din zona si nu mai revii in razboi;</li><li>ajungi totusi in afara cercului (de exemplu dupa un respawn) si nu te intorci in <b>10 secunde</b>.</li></ul></div>
<div class="vtr-card in"><span class="tag">Ramai in lupta cand</span><ul class="vtr-ticks"><li>cazi fara lovitura fatala: primesti un mesaj ca nu ai fost eliminat;</li><li>un coleg sau un medic iti da revive: te intorci in lupta.</li></ul></div>
</div>
<ul class="vtr-win">
<li><span class="k">Toti adversarii eliminati</span><span class="v">Tabara ramasa castiga pe loc.</span></li>
<li><span class="k">Timpul expira</span><span class="v">Castiga tabara cu mai multi luptatori in viata.</span></li>
<li><span class="k">Egalitate</span><span class="v">Aparatorul pastreaza teritoriul.</span></li>
</ul>
<h2 class="vtr-h2" id="suzeranul-hartii"><span>06</span>Suzeranul hartii</h2>
<div class="vtr-over">
<div class="vtr-card vtr-vs">
<svg viewBox="0 0 300 150" role="img" aria-label="Doua familii impotriva suzeranului hartii">
<g fill="none" stroke-width="2.5"><path d="M60 40 l22 8 v18 c0 14 -10 24 -22 28 c-12 -4 -22 -14 -22 -28 v-18 z" stroke="#ef4444" fill="#1a0808"/><path d="M60 92 l22 8 v14 c0 10 -10 18 -22 21 c-12 -3 -22 -11 -22 -21 v-14 z" stroke="#71717a" fill="#151518"/><path d="M240 54 l32 11 v24 c0 20 -14 34 -32 40 c-18 -6 -32 -20 -32 -40 v-24 z" stroke="#d6a54a" fill="#141005"/></g>
<text class="big" x="150" y="96">2 vs 1</text>
<text class="side" x="60" y="20">RIVAL + ALIAT</text>
<text class="side" x="240" y="34">SUZERAN</text>
</svg>
</div>
<div class="vtr-card">
<p>Familia care tine <b>cel putin 4 din cele 8</b> teritorii devine suzeranul hartii. Cand suzeranul intra intr-un razboi, seful taberei adverse poate chema <b>o familie aliata</b> ca sa lupte 2 contra 1.</p>
<ul class="vtr-ticks">
<li>Daca suzeranul apara, atacatorul alege aliatul cand declara razboiul.</li>
<li>Daca suzeranul ataca, aparatorul alege aliatul odata cu data bataliei.</li>
<li>Aliatul nu poate fi deja intr-un razboi sau in pauza de dupa unul. Nu poate fi Sindicatul si nici suzeranul.</li>
<li>Aliatul nu primeste nicio recompensa. Lupta doar ca sa echilibreze harta.</li>
</ul>
</div>
</div>
<h2 class="vtr-h2" id="sindicatul"><span>07</span>Ce poate face Sindicatul</h2>
<div class="vtr-card">
<ul class="vtr-ticks">
<li><b>Anuleaza</b> orice razboi, oricand. Garantia se intoarce la membrul cu cel mai mare grad online din familia atacatoare.</li>
<li><b>Muta data</b> unui razboi si schimba aliatii unui razboi cu suzeranul hartii.</li>
<li><b>Da si ia</b> teritorii direct, fara razboi.</li>
<li>Alege <b>culoarea</b> fiecarei familii pe harta.</li>
</ul>
<p class="vtr-note">Un razboi aflat in pregatire sau in lupta cand serverul da restart se anuleaza singur, iar garantia se intoarce la atacator.</p>
</div>
<h2 class="vtr-h2" id="rezervari-si-statistici"><span>08</span>Rezervari si statistici</h2>
<div class="vtr-split">
<div class="vtr-card">
<h3 class="vtr-h3">Rezervari</h3>
<p>Sindicatul pune in calendar activitati pe care familiile le rezerva pe intervale fixe, de exemplu un jaf la banca. Calendarul il gasesti in tableta, la <b>Rezervari</b>.</p>
<ul class="vtr-ticks">
<li>Doar seful familiei face sau anuleaza o rezervare.</li>
<li>Poti rezerva pentru azi si urmatoarele 2 zile.</li>
<li>O familie are cel mult o rezervare activa pe acelasi tip de activitate.</li>
<li>Unele activitati se rezerva cu cateva ore inainte. Tableta iti spune cate.</li>
<li>O rezervare se anuleaza doar inainte sa inceapa.</li>
</ul>
</div>
<div class="vtr-card">
<h3 class="vtr-h3">Statistici</h3>
<p>Dupa fiecare razboi, tableta pastreaza fisa fiecarui luptator: cati adversari a eliminat, de cate ori a cazut, foc pe propriii colegi, cat a rezistat si daca a ramas in picioare pana la final.</p>
<p>Le gasesti la <b>Statistici</b>, impreuna cu rezultatul razboiului.</p>
</div>
</div>
<div class="vtr-end">
<p>Inainte de primul razboi, citeste capitolul 4 din regulament: filmarea e obligatorie, iar jucatorii care nu fac parte din razboi nu se implica.</p>
<a class="btn" href="/zona-info/regulament-mafii">Regulamentul Mafiilor</a>
</div>
</div>
