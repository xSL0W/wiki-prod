---
outline: false
---

<style>
.ebc {
  --ink: #0b0b0d;
  --panel: #17171a;
  --panel2: #1f1f23;
  --line: #2f2f36;
  --text: #f4f4f5;
  --mute: #a1a1aa;
  --red: #ef4444;
  --red-deep: #b91c1c;
  --red-soft: rgba(239, 68, 68, 0.14);
  --gold: #f5b931;
  --gold-soft: rgba(245, 185, 49, 0.14);
  --green: #4ade80;
  max-width: 960px;
  margin: 0 auto;
  color: var(--text);
  font-family: Inter, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.ebc *, .ebc *::before, .ebc *::after { box-sizing: border-box; }
.ebc p, .ebc li { line-height: 1.6; color: var(--text); margin: 0; }
.ebc ul, .ebc ol { list-style: none; padding: 0; margin: 0; }
.ebc li + li { margin-top: 0; }
.ebc b { color: #fff; font-weight: 650; }
.ebc a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.ebc a:hover { color: #fecaca; }
.ebc a:focus-visible { outline: 3px solid var(--red); outline-offset: 3px; border-radius: 6px; }
.ebc kbd {
  font: inherit; font-size: 0.85em; font-weight: 700; color: #fff; background: var(--red-deep);
  border-radius: 6px; padding: 0.05rem 0.45rem;
}
/* ---------- hero ---------- */
.ebc .ebc-hero {
  position: relative; overflow: hidden; isolation: isolate;
  background: radial-gradient(90% 120% at 100% 0%, rgba(245, 185, 49, 0.12), transparent 55%),
              radial-gradient(110% 120% at 0% 100%, rgba(185, 28, 28, 0.3), var(--ink) 62%);
  border: 1px solid var(--line);
  border-radius: 22px;
  padding: clamp(1.15rem, 4vw, 2.4rem);
}
.ebc .ebc-hero::before {
  content: ''; position: absolute; inset: 0 auto 0 0; width: 60%; z-index: -1; pointer-events: none;
  background: linear-gradient(100deg, transparent 0%, rgba(255, 255, 255, 0.055) 50%, transparent 100%);
  transform: translateX(-110%);
  animation: ebc-sweep 11s ease-in-out infinite;
}
@keyframes ebc-sweep { 0%, 20% { transform: translateX(-110%); } 60%, 100% { transform: translateX(240%); } }
.ebc .ebc-kicker {
  font-size: 0.78rem; font-weight: 700; letter-spacing: 0.16em; text-transform: uppercase; color: var(--red);
  margin-bottom: 0.55rem;
}
.ebc .ebc-hero h1 {
  margin: 0 0 0.75rem; border: 0; padding: 0;
  font-size: clamp(2rem, 6.4vw, 3.4rem); line-height: 1.04; font-weight: 800; letter-spacing: -0.03em; color: #fff;
}
.ebc .ebc-hero h1 span { color: var(--gold); }
.ebc .ebc-lede { max-width: 58ch; color: var(--mute); font-size: 1.05rem; }
/* skyline */
.ebc .ebc-city { display: block; width: 100%; height: auto; margin-top: 1.3rem; border-radius: 14px; }
.ebc-city .far { fill: #1d1d24; }
.ebc-city .bld { fill: #0e0e11; stroke: #26262d; stroke-width: 1; }
.ebc-city .ground { fill: #08080a; }
.ebc-city .sign { fill: var(--red); }
.ebc-city .sign-t { fill: #fff; font: 800 9px Inter, system-ui, sans-serif; letter-spacing: 0.08em; }
.ebc-city .star { fill: #fff; opacity: 0.5; }
.ebc-city .win rect { fill: var(--gold); opacity: 0.16; }
.ebc-city .win rect.on { opacity: 0.85; }
.ebc-city .win .a { animation: ebc-lamp 7s steps(1, end) infinite; }
.ebc-city .win .b { animation: ebc-lamp 9s steps(1, end) -3s infinite; }
.ebc-city .win .c { animation: ebc-lamp 11s steps(1, end) -6s infinite; }
.ebc-city .win .d { animation: ebc-lamp2 8s steps(1, end) -2s infinite; }
.ebc-city .win .e { animation: ebc-lamp2 13s steps(1, end) -9s infinite; }
.ebc-city .win .f { animation: ebc-lamp 15s steps(1, end) -11s infinite; }
@keyframes ebc-lamp { 0% { opacity: 0.16; } 35% { opacity: 0.9; } 80% { opacity: 0.16; } }
@keyframes ebc-lamp2 { 0% { opacity: 0.9; } 50% { opacity: 0.16; } 70% { opacity: 0.9; } }
.ebc-city .star { animation: ebc-twinkle 4s ease-in-out infinite; }
.ebc-city .star:nth-of-type(2n) { animation-delay: -1.5s; }
.ebc-city .star:nth-of-type(3n) { animation-delay: -2.7s; }
@keyframes ebc-twinkle { 0%, 100% { opacity: 0.15; } 50% { opacity: 0.7; } }
/* revenue line: revealed by a clip rect that only scales */
.ebc-city .area { fill: url(#ebc-area); }
.ebc-city .rev { fill: none; stroke: var(--red); stroke-width: 3.5; stroke-linejoin: round; stroke-linecap: round; }
.ebc-city .rev-under { fill: none; stroke: #0b0b0d; stroke-width: 8; stroke-linejoin: round; stroke-linecap: round; opacity: 0.8; }
.ebc-city .wipe { transform-box: fill-box; transform-origin: left center; animation: ebc-wipe 10s cubic-bezier(.45, .05, .25, 1) infinite; }
.ebc-city .chart { animation: ebc-chart 10s linear infinite; }
.ebc-city .tip { fill: #fff; }
.ebc-city .pulse { fill: none; stroke: var(--red); stroke-width: 2; transform-box: fill-box; transform-origin: center; opacity: 0; }
.ebc-city .tipgrp { opacity: 0; animation: ebc-tip 10s linear infinite; }
.ebc-city .pulse { animation: ebc-pulse 2s ease-out infinite; }
@keyframes ebc-wipe { 0% { transform: scaleX(0); } 45%, 100% { transform: scaleX(1); } }
@keyframes ebc-chart { 0%, 88% { opacity: 1; } 96%, 100% { opacity: 0; } }
@keyframes ebc-tip { 0%, 42% { opacity: 0; } 47%, 88% { opacity: 1; } 96%, 100% { opacity: 0; } }
@keyframes ebc-pulse { 0% { opacity: 0.9; transform: scale(0.4); } 100% { opacity: 0; transform: scale(2.4); } }
/* floating firm-type badges */
.ebc .ebc-badges { display: flex; flex-wrap: wrap; gap: 0.45rem; margin-top: 1.1rem; }
.ebc .ebc-badges li {
  display: inline-flex; align-items: center; gap: 0.4rem;
  font-size: 0.82rem; font-weight: 650; color: var(--text);
  background: rgba(23, 23, 26, 0.85); border: 1px solid var(--line); border-radius: 999px; padding: 0.25rem 0.7rem;
  animation: ebc-float 6s ease-in-out infinite;
}
.ebc .ebc-badges li::before { content: ''; width: 7px; height: 7px; border-radius: 50%; background: var(--gold); }
.ebc .ebc-badges li:nth-child(3n)::before { background: var(--red); }
.ebc .ebc-badges li:nth-child(4n)::before { background: var(--green); }
.ebc .ebc-badges li:nth-child(2) { animation-delay: -1s; }
.ebc .ebc-badges li:nth-child(3) { animation-delay: -2.2s; }
.ebc .ebc-badges li:nth-child(4) { animation-delay: -3.1s; }
.ebc .ebc-badges li:nth-child(5) { animation-delay: -4s; }
.ebc .ebc-badges li:nth-child(6) { animation-delay: -0.6s; }
.ebc .ebc-badges li:nth-child(7) { animation-delay: -2.7s; }
.ebc .ebc-badges li:nth-child(8) { animation-delay: -4.6s; }
.ebc .ebc-badges li:nth-child(9) { animation-delay: -1.7s; }
@keyframes ebc-float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-5px); } }
/* hero stats */
.ebc .ebc-stats { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 0.6rem; margin-top: 1.2rem; }
.ebc .ebc-stats li { background: rgba(23, 23, 26, 0.85); border: 1px solid var(--line); border-radius: 14px; padding: 0.7rem 0.9rem; }
.ebc .ebc-stats b { display: block; font-size: clamp(1.35rem, 4vw, 1.8rem); line-height: 1.1; font-weight: 800; color: #fff; font-variant-numeric: tabular-nums; }
.ebc .ebc-stats span { display: block; color: var(--mute); font-size: 0.82rem; line-height: 1.35; margin-top: 0.2rem; }
@media (prefers-reduced-motion: reduce) {
  .ebc .ebc-hero::before { animation: none; display: none; }
  .ebc .ebc-city .win rect, .ebc .ebc-city .star, .ebc .ebc-city .wipe, .ebc .ebc-city .chart, .ebc .ebc-city .tipgrp,
  .ebc .ebc-city .pulse, .ebc .ebc-badges li { animation: none; }
  .ebc .ebc-city .wipe { transform: none; }
  .ebc .ebc-city .tipgrp { opacity: 1; }
  .ebc .ebc-city .pulse { opacity: 0; }
}
/* ---------- sections ---------- */
.ebc .ebc-h2 {
  display: flex; align-items: flex-start; gap: 0.65rem;
  margin: 3rem 0 0.9rem; border: 0; padding: 0;
  font-size: 1.5rem; font-weight: 750; letter-spacing: -0.015em; line-height: 1.25; color: #fff;
}
.ebc .ebc-h2::before { margin-top: calc(0.5lh - 0.6rem / 2);
  content: ''; flex: none; width: 0.6rem; height: 0.6rem; border-radius: 2px; background: var(--red);
  transform: rotate(45deg); box-shadow: 0 0 0 4px var(--red-soft);
}
.ebc .ebc-h3 { margin: 0 0 0.35rem; border: 0; padding: 0; font-size: 1.05rem; font-weight: 700; color: #fff; line-height: 1.3; }
.ebc .ebc-sub { color: var(--mute); max-width: 66ch; margin-bottom: 1rem; }
.ebc .ebc-card { background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 1.1rem 1.25rem; }
.ebc .ebc-card p { color: var(--mute); font-size: 0.97rem; }
.ebc .ebc-card p + p { margin-top: 0.5rem; }
/* about: text + where */
.ebc .ebc-about { display: grid; grid-template-columns: minmax(0, 1.5fr) minmax(0, 1fr); gap: 0.9rem; }
.ebc .ebc-about .ebc-where { background: linear-gradient(160deg, var(--gold-soft), var(--panel) 60%); border-color: #4a3d1c; }
.ebc .ebc-where .ebc-tag {
  display: inline-block; font-size: 0.72rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase;
  color: var(--gold); margin-bottom: 0.4rem;
}
@media (max-width: 720px) { .ebc .ebc-about { grid-template-columns: minmax(0, 1fr); } }
/* road to owner */
.ebc .ebc-road { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 0.75rem; counter-reset: ebc-step; }
.ebc .ebc-road li {
  position: relative; counter-increment: ebc-step;
  background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 2.6rem 1.15rem 1.05rem;
}
.ebc .ebc-road li::before {
  content: counter(ebc-step); position: absolute; top: 0.9rem; left: 1.15rem;
  width: 1.5rem; height: 1.5rem; border-radius: 50%; display: grid; place-items: center;
  font-size: 0.8rem; font-weight: 800; color: #fff; background: var(--red-deep);
}
.ebc .ebc-road p { color: var(--mute); font-size: 0.95rem; }
.ebc .ebc-note { margin-top: 0.85rem; color: var(--mute); font-size: 0.93rem; }
/* lobby directory board = the firm types */
.ebc .ebc-board {
  background: #0d0d0f; border: 1px solid #3a3222; border-radius: 16px; padding: 0.6rem clamp(0.75rem, 3vw, 1.4rem);
  box-shadow: inset 0 0 0 4px #141210;
}
.ebc .ebc-board-head {
  display: flex; justify-content: space-between; gap: 1rem; padding: 0.55rem 0 0.6rem; border-bottom: 1px solid #3a3222;
  font: 700 0.72rem/1.2 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; letter-spacing: 0.14em; text-transform: uppercase; color: var(--gold);
}
.ebc .ebc-board li {
  display: grid; grid-template-columns: minmax(0, 1fr) auto; align-items: baseline; gap: 0.2rem 1rem;
  padding: 0.65rem 0; border-bottom: 1px dashed #2c2820;
}
.ebc .ebc-board li:last-child { border-bottom: 0; }
.ebc .ebc-board .t { font-weight: 700; color: #fff; }
.ebc .ebc-board .t a { color: #fff; }
.ebc .ebc-board .n {
  font: 800 1.05rem/1 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; color: var(--gold); font-variant-numeric: tabular-nums;
}
.ebc .ebc-board .d { grid-column: 1 / -1; color: var(--mute); font-size: 0.9rem; line-height: 1.45; }
/* roles matrix */
.ebc .ebc-matrix { border: 1px solid var(--line); border-radius: 16px; overflow: hidden; background: var(--panel); }
.ebc .ebc-matrix li {
  display: grid; grid-template-columns: minmax(0, 1fr) repeat(3, 4.2rem); align-items: center;
  padding: 0.6rem 0.9rem; border-top: 1px solid var(--line); font-size: 0.93rem;
}
.ebc .ebc-matrix li:first-child { border-top: 0; background: var(--panel2); font-size: 0.75rem; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; color: var(--mute); }
.ebc .ebc-matrix li > span:not(:first-child) { text-align: center; }
.ebc .ebc-matrix .y, .ebc .ebc-matrix .x {
  display: inline-grid; place-items: center; width: 1.4rem; height: 1.4rem; border-radius: 50%; font-size: 0.8rem; font-weight: 800;
}
.ebc .ebc-matrix .y { background: rgba(74, 222, 128, 0.15); color: var(--green); }
.ebc .ebc-matrix .x { color: #52525b; }
@media (max-width: 480px) {
  .ebc .ebc-matrix li { grid-template-columns: minmax(0, 1fr) repeat(3, 3.2rem); padding: 0.55rem 0.6rem; font-size: 0.88rem; }
  .ebc .ebc-matrix li:first-child { font-size: 0.62rem; letter-spacing: 0; }
}
/* tablet mock */
.ebc .ebc-tablet-wrap { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 1rem; align-items: start; }
.ebc .ebc-tablet {
  background: #050506; border: 10px solid #26262b; border-radius: 22px; padding: 0.8rem;
  box-shadow: 0 0 0 1px #3a3a42;
}
.ebc .ebc-tablet-top { display: flex; justify-content: space-between; align-items: center; gap: 0.5rem; margin-bottom: 0.65rem; }
.ebc .ebc-tablet-top b { font-size: 0.9rem; }
.ebc .ebc-shift { font-size: 0.72rem; font-weight: 700; color: #fff; background: #15803d; border-radius: 6px; padding: 0.2rem 0.5rem; white-space: nowrap; }
.ebc .ebc-tabs { display: flex; flex-wrap: wrap; gap: 0.35rem; }
.ebc .ebc-tabs li { font-size: 0.75rem; font-weight: 600; color: var(--mute); background: var(--panel2); border: 1px solid var(--line); border-radius: 7px; padding: 0.2rem 0.5rem; }
.ebc .ebc-tabs li.cur { color: #fff; background: var(--red-deep); border-color: var(--red-deep); }
.ebc .ebc-tiles { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0.45rem; margin-top: 0.7rem; }
.ebc .ebc-tiles li { background: var(--panel); border: 1px solid var(--line); border-radius: 10px; padding: 0.5rem 0.6rem; font-size: 0.72rem; color: var(--mute); line-height: 1.3; }
.ebc .ebc-tiles li i { display: block; height: 0.55rem; margin-top: 0.35rem; border-radius: 4px; background: #2d2d33; font-style: normal; }
.ebc .ebc-tiles li i.g { width: 70%; background: var(--gold); opacity: 0.7; }
.ebc .ebc-tiles li i.r { width: 45%; background: var(--red); opacity: 0.7; }
.ebc .ebc-tabdesc li { padding: 0.55rem 0; border-top: 1px solid var(--line); font-size: 0.94rem; color: var(--mute); }
.ebc .ebc-tabdesc li:first-child { border-top: 0; padding-top: 0; }
.ebc .ebc-tabdesc b { color: #fff; }
@media (max-width: 760px) { .ebc .ebc-tablet-wrap { grid-template-columns: minmax(0, 1fr); } }
/* steps (pontaj, POS) */
.ebc .ebc-steps { counter-reset: ebc-s; display: grid; gap: 0.6rem; }
.ebc .ebc-steps li {
  position: relative; counter-increment: ebc-s; padding: 0.85rem 1rem 0.85rem 3.1rem;
  background: var(--panel); border: 1px solid var(--line); border-radius: 14px; color: var(--mute); font-size: 0.96rem;
}
.ebc .ebc-steps li::before {
  content: counter(ebc-s); position: absolute; left: 0.95rem; top: 0.9rem;
  width: 1.45rem; height: 1.45rem; border-radius: 50%; display: grid; place-items: center;
  font-size: 0.78rem; font-weight: 800; color: #111; background: var(--gold);
}
.ebc .ebc-two { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 0.9rem; }
/* money flow */
.ebc .ebc-flow { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 0.8fr) minmax(0, 1fr); gap: 0.75rem; align-items: stretch; }
.ebc .ebc-flow .col { background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 1rem 1.1rem; }
.ebc .ebc-flow .col h3 { margin: 0 0 0.6rem; border: 0; padding: 0; font: 700 0.75rem/1.2 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; letter-spacing: 0.12em; text-transform: uppercase; }
.ebc .ebc-flow .in h3 { color: var(--green); }
.ebc .ebc-flow .out h3 { color: var(--red); }
.ebc .ebc-flow .col li { padding: 0.45rem 0; border-top: 1px solid var(--line); font-size: 0.92rem; color: var(--mute); line-height: 1.45; }
.ebc .ebc-flow .col li:first-child { border-top: 0; padding-top: 0; }
.ebc .ebc-flow .col li b { display: block; color: #fff; font-size: 0.95rem; }
.ebc .ebc-flow .vault {
  display: grid; place-items: center; text-align: center; gap: 0.4rem;
  background: radial-gradient(circle at 50% 35%, var(--gold-soft), var(--panel) 70%); border-color: #4a3d1c;
}
.ebc .ebc-flow .vault svg { width: 64px; height: 64px; }
.ebc .ebc-flow .vault b { display: block; font-size: 1.1rem; }
.ebc .ebc-flow .vault span { display: block; color: var(--mute); font-size: 0.85rem; line-height: 1.4; }
@media (max-width: 760px) { .ebc .ebc-flow { grid-template-columns: minmax(0, 1fr); } }
/* receipt */
.ebc .ebc-receipt {
  background: #f4f1ea; color: #1c1917; border-radius: 6px 6px 0 0; padding: 1rem 1.1rem 1.4rem;
  font: 500 0.86rem/1.5 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace;
  -webkit-mask: radial-gradient(circle 7px at 50% 100%, transparent 98%, #000) 0 0 / 18px 100% repeat-x;
          mask: radial-gradient(circle 7px at 50% 100%, transparent 98%, #000) 0 0 / 18px 100% repeat-x;
}
.ebc .ebc-receipt p, .ebc .ebc-receipt li { color: #1c1917; line-height: 1.5; }
.ebc .ebc-receipt .rh { text-align: center; font-weight: 800; letter-spacing: 0.14em; border-bottom: 1px dashed #a8a29e; padding-bottom: 0.45rem; margin-bottom: 0.45rem; }
.ebc .ebc-receipt li { display: flex; justify-content: space-between; gap: 0.6rem; }
.ebc .ebc-receipt li span:last-child { text-align: right; }
.ebc .ebc-receipt .rf { border-top: 1px dashed #a8a29e; margin-top: 0.45rem; padding-top: 0.45rem; text-align: center; font-weight: 700; }
/* warn meter */
.ebc .ebc-meter { display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 4px; margin: 0.8rem 0 0.4rem; }
.ebc .ebc-meter span { height: 0.7rem; border-radius: 3px; background: #2d2d33; }
.ebc .ebc-meter span.f { background: var(--red); }
.ebc .ebc-meter-l { display: flex; justify-content: space-between; color: var(--mute); font-size: 0.78rem; font-family: ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; }
.ebc .ebc-card ul.ebc-dots li { position: relative; padding-left: 1.1rem; color: var(--mute); font-size: 0.95rem; margin-top: 0.35rem; }
.ebc .ebc-card ul.ebc-dots li::before { content: ''; position: absolute; left: 0; top: 0.62em; width: 6px; height: 6px; border-radius: 50%; background: var(--red); }
/* closing */
.ebc .ebc-end {
  margin-top: 3rem; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 0.8rem;
  background: linear-gradient(110deg, rgba(185, 28, 28, 0.22), var(--panel) 60%); border: 1px solid var(--line); border-radius: 16px; padding: 1.1rem 1.25rem;
}
.ebc .ebc-end p { color: var(--mute); max-width: 52ch; }
.ebc .ebc-end a.btn {
  display: inline-flex; align-items: center; text-decoration: none; font-weight: 700; color: #fff;
  background: var(--red-deep); border-radius: 999px; padding: 0.55rem 1.1rem;
}
.ebc .ebc-end a.btn:hover { background: #991b1b; color: #fff; }
@media (max-width: 420px) {
  .ebc .ebc-stats { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); }
  .ebc .ebc-stats li:last-child { grid-column: 1 / -1; }
}
</style>

<div class="ebc">
<section class="ebc-hero">
<p class="ebc-kicker">Afaceri si locatii</p>
<h1>Elite Business <span>Center</span></h1>
<p class="ebc-lede">Elite Business Center se ocupa de afacerile din oras: service-uri, magazine, frizerii, club. Castigi o firma la licitatie, iti faci echipa si o conduci dintr-o tableta: angajati, pontaj, stoc, preturi, facturi si contul firmei.</p>
<svg class="ebc-city" viewBox="0 0 640 240" role="img" aria-label="Siluetele unor cladiri de birouri noaptea, cu ferestre care se aprind si se sting, si o linie de venit care urca peste oras">
<defs>
<linearGradient id="ebc-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1a0d10"/><stop offset="1" stop-color="#0b0b0d"/></linearGradient>
<linearGradient id="ebc-area" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ef4444" stop-opacity="0.28"/><stop offset="1" stop-color="#ef4444" stop-opacity="0"/></linearGradient>
<clipPath id="ebc-reveal"><rect class="wipe" x="0" y="0" width="640" height="240"/></clipPath>
</defs>
<rect x="0" y="0" width="640" height="240" fill="url(#ebc-sky)"/>
<g><circle class="star" cx="40" cy="22" r="1.2"/><circle class="star" cx="112" cy="48" r="1"/><circle class="star" cx="198" cy="18" r="1.3"/><circle class="star" cx="246" cy="60" r="0.9"/><circle class="star" cx="408" cy="26" r="1.2"/><circle class="star" cx="452" cy="56" r="1"/><circle class="star" cx="530" cy="20" r="1.1"/><circle class="star" cx="618" cy="64" r="1"/><circle class="star" cx="160" cy="76" r="0.8"/></g>
<g class="far"><rect x="0" y="153" width="32" height="79"/><rect x="34" y="163" width="23" height="69"/><rect x="61" y="126" width="25" height="106"/><rect x="91" y="108" width="23" height="124"/><rect x="113" y="161" width="23" height="71"/><rect x="138" y="164" width="35" height="68"/><rect x="172" y="102" width="24" height="130"/><rect x="198" y="100" width="23" height="132"/><rect x="218" y="92" width="29" height="140"/><rect x="253" y="165" width="40" height="67"/><rect x="298" y="122" width="40" height="110"/><rect x="334" y="167" width="29" height="65"/><rect x="367" y="135" width="26" height="97"/><rect x="395" y="103" width="26" height="129"/><rect x="418" y="133" width="40" height="99"/><rect x="462" y="159" width="27" height="73"/><rect x="494" y="91" width="40" height="141"/><rect x="533" y="160" width="33" height="72"/><rect x="570" y="100" width="24" height="132"/><rect x="590" y="109" width="28" height="123"/><rect x="624" y="118" width="39" height="114"/></g>
<g class="chart"><path class="area" clip-path="url(#ebc-reveal)" d="M16 200 L70 182 L120 188 L170 152 L222 162 L272 124 L330 132 L382 96 L432 108 L482 72 L540 82 L600 40 L600 232 L16 232 Z"/></g>
<g class="bld"><rect x="8" y="150" width="44" height="82"/><rect x="58" y="118" width="38" height="114"/><rect x="102" y="165" width="52" height="67"/><rect x="160" y="96" width="46" height="136"/><rect x="212" y="140" width="50" height="92"/><rect x="350" y="110" width="44" height="122"/><rect x="400" y="150" width="56" height="82"/><rect x="462" y="88" width="40" height="144"/><rect x="508" y="132" width="52" height="100"/><rect x="566" y="160" width="36" height="72"/><rect x="608" y="124" width="32" height="108"/><path d="M276 232 V58 L340 32 V232 Z"/></g>
<g class="win"><rect class="on" x="16" y="160" width="6" height="7"/><rect class="b" x="27" y="173" width="6" height="7"/><rect class="on" x="38" y="173" width="6" height="7"/><rect class="on" x="16" y="186" width="6" height="7"/><rect class="b" x="38" y="186" width="6" height="7"/><rect class="c" x="16" y="199" width="6" height="7"/><rect class="c" x="27" y="199" width="6" height="7"/><rect class="on" x="38" y="199" width="6" height="7"/><rect class="f" x="27" y="212" width="6" height="7"/><rect class="on" x="80" y="128" width="6" height="7"/><rect class="b" x="80" y="154" width="6" height="7"/><rect class="on" x="80" y="167" width="6" height="7"/><rect class="a" x="68" y="193" width="6" height="7"/><rect class="f" x="80" y="193" width="6" height="7"/><rect class="c" x="120" y="175" width="6" height="7"/><rect class="on" x="130" y="175" width="6" height="7"/><rect class="b" x="108" y="188" width="6" height="7"/><rect class="e" x="120" y="201" width="6" height="7"/><rect class="f" x="130" y="201" width="6" height="7"/><rect class="on" x="142" y="201" width="6" height="7"/><rect class="c" x="108" y="214" width="6" height="7"/><rect class="a" x="142" y="214" width="6" height="7"/><rect class="c" x="169" y="106" width="6" height="7"/><rect class="c" x="191" y="119" width="6" height="7"/><rect class="a" x="169" y="132" width="6" height="7"/><rect class="on" x="180" y="132" width="6" height="7"/><rect class="on" x="180" y="145" width="6" height="7"/><rect class="on" x="180" y="197" width="6" height="7"/><rect class="on" x="234" y="150" width="6" height="7"/><rect class="e" x="245" y="150" width="6" height="7"/><rect class="c" x="234" y="176" width="6" height="7"/><rect class="d" x="245" y="176" width="6" height="7"/><rect class="f" x="223" y="189" width="6" height="7"/><rect class="a" x="245" y="189" width="6" height="7"/><rect class="e" x="223" y="202" width="6" height="7"/><rect class="b" x="234" y="202" width="6" height="7"/><rect class="e" x="245" y="202" width="6" height="7"/><rect class="c" x="223" y="215" width="6" height="7"/><rect class="f" x="358" y="120" width="6" height="7"/><rect class="d" x="369" y="120" width="6" height="7"/><rect class="on" x="380" y="120" width="6" height="7"/><rect class="d" x="358" y="133" width="6" height="7"/><rect class="a" x="380" y="133" width="6" height="7"/><rect class="e" x="358" y="146" width="6" height="7"/><rect class="d" x="369" y="146" width="6" height="7"/><rect class="f" x="380" y="146" width="6" height="7"/><rect class="f" x="358" y="159" width="6" height="7"/><rect class="f" x="369" y="159" width="6" height="7"/><rect class="f" x="369" y="172" width="6" height="7"/><rect class="a" x="358" y="185" width="6" height="7"/><rect class="f" x="369" y="185" width="6" height="7"/><rect class="b" x="380" y="185" width="6" height="7"/><rect class="b" x="358" y="198" width="6" height="7"/><rect class="d" x="369" y="198" width="6" height="7"/><rect class="c" x="380" y="198" width="6" height="7"/><rect class="f" x="358" y="211" width="6" height="7"/><rect class="on" x="380" y="211" width="6" height="7"/><rect class="b" x="408" y="160" width="6" height="7"/><rect class="c" x="420" y="160" width="6" height="7"/><rect class="a" x="430" y="160" width="6" height="7"/><rect class="c" x="408" y="173" width="6" height="7"/><rect class="on" x="420" y="173" width="6" height="7"/><rect class="f" x="430" y="173" width="6" height="7"/><rect class="a" x="408" y="186" width="6" height="7"/><rect class="b" x="430" y="186" width="6" height="7"/><rect class="c" x="442" y="186" width="6" height="7"/><rect class="d" x="408" y="199" width="6" height="7"/><rect class="d" x="420" y="199" width="6" height="7"/><rect class="f" x="408" y="212" width="6" height="7"/><rect class="f" x="474" y="98" width="6" height="7"/><rect class="on" x="484" y="98" width="6" height="7"/><rect class="c" x="474" y="111" width="6" height="7"/><rect class="a" x="484" y="111" width="6" height="7"/><rect class="c" x="474" y="124" width="6" height="7"/><rect class="c" x="484" y="124" width="6" height="7"/><rect class="b" x="484" y="137" width="6" height="7"/><rect class="f" x="474" y="150" width="6" height="7"/><rect class="on" x="484" y="150" width="6" height="7"/><rect class="b" x="474" y="163" width="6" height="7"/><rect class="a" x="484" y="163" width="6" height="7"/><rect class="on" x="474" y="189" width="6" height="7"/><rect class="b" x="484" y="189" width="6" height="7"/><rect class="d" x="474" y="202" width="6" height="7"/><rect class="on" x="484" y="202" width="6" height="7"/><rect class="on" x="474" y="215" width="6" height="7"/><rect class="d" x="484" y="215" width="6" height="7"/><rect class="e" x="514" y="142" width="6" height="7"/><rect class="d" x="526" y="142" width="6" height="7"/><rect class="c" x="536" y="142" width="6" height="7"/><rect class="on" x="536" y="155" width="6" height="7"/><rect class="b" x="514" y="168" width="6" height="7"/><rect class="c" x="526" y="168" width="6" height="7"/><rect class="f" x="536" y="168" width="6" height="7"/><rect class="on" x="514" y="181" width="6" height="7"/><rect class="on" x="536" y="181" width="6" height="7"/><rect class="c" x="548" y="181" width="6" height="7"/><rect class="d" x="514" y="194" width="6" height="7"/><rect class="on" x="536" y="194" width="6" height="7"/><rect class="a" x="536" y="207" width="6" height="7"/><rect class="a" x="576" y="170" width="6" height="7"/><rect class="e" x="576" y="183" width="6" height="7"/><rect class="b" x="586" y="183" width="6" height="7"/><rect class="d" x="586" y="196" width="6" height="7"/><rect class="b" x="576" y="209" width="6" height="7"/><rect class="c" x="626" y="134" width="6" height="7"/><rect class="e" x="616" y="160" width="6" height="7"/><rect class="on" x="616" y="173" width="6" height="7"/><rect class="b" x="626" y="173" width="6" height="7"/><rect class="c" x="626" y="186" width="6" height="7"/><rect class="b" x="616" y="199" width="6" height="7"/><rect class="d" x="294" y="80" width="6" height="7"/><rect class="on" x="316" y="80" width="6" height="7"/><rect class="on" x="283" y="93" width="6" height="7"/><rect class="e" x="294" y="93" width="6" height="7"/><rect class="a" x="305" y="93" width="6" height="7"/><rect class="d" x="316" y="93" width="6" height="7"/><rect class="c" x="327" y="93" width="6" height="7"/><rect class="e" x="305" y="106" width="6" height="7"/><rect class="d" x="316" y="106" width="6" height="7"/><rect class="c" x="283" y="119" width="6" height="7"/><rect class="e" x="305" y="119" width="6" height="7"/><rect class="d" x="283" y="132" width="6" height="7"/><rect class="d" x="294" y="132" width="6" height="7"/><rect class="b" x="305" y="132" width="6" height="7"/><rect class="on" x="316" y="132" width="6" height="7"/><rect class="on" x="327" y="132" width="6" height="7"/><rect class="e" x="283" y="145" width="6" height="7"/><rect class="d" x="294" y="145" width="6" height="7"/><rect class="c" x="316" y="145" width="6" height="7"/><rect class="e" x="327" y="158" width="6" height="7"/><rect class="a" x="283" y="171" width="6" height="7"/><rect class="e" x="305" y="171" width="6" height="7"/><rect class="e" x="316" y="171" width="6" height="7"/><rect class="f" x="283" y="197" width="6" height="7"/><rect class="e" x="305" y="197" width="6" height="7"/><rect class="d" x="316" y="210" width="6" height="7"/><rect class="a" x="327" y="210" width="6" height="7"/></g>
<rect x="290" y="74" width="36" height="13" rx="2" class="sign"/><text class="sign-t" x="308" y="84" text-anchor="middle">EBC</text>
<rect class="ground" x="0" y="232" width="640" height="8"/>
<g class="chart" clip-path="url(#ebc-reveal)"><path class="rev-under" d="M16 200 L70 182 L120 188 L170 152 L222 162 L272 124 L330 132 L382 96 L432 108 L482 72 L540 82 L600 40"/><path class="rev" d="M16 200 L70 182 L120 188 L170 152 L222 162 L272 124 L330 132 L382 96 L432 108 L482 72 L540 82 L600 40"/></g>
<g class="tipgrp"><circle class="pulse" cx="600" cy="40" r="7"/><circle class="tip" cx="600" cy="40" r="5"/></g>
</svg>
<ul class="ebc-badges" aria-label="Tipuri de afaceri">
<li>Service auto</li><li>Magazin 24/7</li><li>Haine</li><li>Arme</li><li>Frizerie</li><li>Tatuaje</li><li>Club</li><li>Salon</li>
</ul>
<ul class="ebc-stats">
<li><b>31</b><span>afaceri in oras</span></li>
<li><b>8</b><span>tipuri diferite</span></li>
<li><b>max. 2</b><span>afaceri pe numele tau</span></li>
</ul>
</section>
<h2 class="ebc-h2">Ce este Elite Business Center</h2>
<div class="ebc-about">
<div class="ebc-card">
<p><b>Elite Business Center (EBC)</b> tine evidenta afacerilor din oras. Prin EBC primeste fiecare firma un proprietar, tot aici se intoarce o firma la care patronul renunta, si tot EBC poate lua inapoi o afacere care nu functioneaza.</p>
<p>Nu cumperi o firma de la un NPC si nici nu o inchiriezi: afacerile se castiga la <b>licitatie</b>. Proprietarul o tine cat timp o face sa mearga: stoc, angajati, program.</p>
</div>
<div class="ebc-card ebc-where">
<span class="ebc-tag">Unde ii gasesti</span>
<p><b>Maze Bank Tower</b>, in centrul orasului. Intri in hol si urci cu liftul la birourile EBC, in varful turnului.</p>
<p>E cel mai inalt turn din centru, il vezi din tot orasul.</p>
</div>
</div>
<h2 class="ebc-h2">De la licitatie la firma ta</h2>
<ol class="ebc-road">
<li><h3 class="ebc-h3">Castigi licitatia</h3><p>Afacerile libere se scot la licitatie. Cine castiga devine proprietarul de drept al firmei.</p></li>
<li><h3 class="ebc-h3">Primesti firma</h3><p>Firma e trecuta pe numele tau. Iti iei o <b>tableta de firma</b> de la Digital Den si de acolo o conduci.</p></li>
<li><h3 class="ebc-h3">Iti faci echipa</h3><p>Angajezi oameni, le dai functie si salariu si numesti sefi care sa te ajute la conducere.</p></li>
</ol>
<p class="ebc-note">Poti detine cel mult <b>doua afaceri</b>. O afacere castigata la licitatie nu se vinde si nu se trece pe altcineva. Daca renunti la ea, o cedezi catre EBC si nu primesti banii inapoi. Toate regulile sunt in <a href="/zona-info/regulament#_9-firme-afaceri">Regulament, sectiunea 9</a>.</p>
<h2 class="ebc-h2">Ce afaceri exista</h2>
<p class="ebc-sub">Numarul de locatii pentru fiecare tip. Fiecare tip de afacere are pagina lui cu detaliile meseriei.</p>
<div class="ebc-board">
<div class="ebc-board-head"><span>Tip afacere</span><span>Locatii</span></div>
<ul>
<li><span class="t"><a href="/afaceri/service">Service auto</a></span><span class="n">6</span><span class="d">Mecanici pe tura, piese de la furnizor, facturi pentru reparatii.</span></li>
<li><span class="t"><a href="/afaceri/shop">Magazin 24/7</a></span><span class="n">5</span><span class="d">Marfa din depozitul firmei, preturi puse de sef, vanzarile apar in tableta.</span></li>
<li><span class="t"><a href="/afaceri/clothing">Magazin de haine</a></span><span class="n">7</span><span class="d">Stoc pe fiecare categorie de haine, plus ghiozdane.</span></li>
<li><span class="t"><a href="/afaceri/gunshop">Magazin de arme</a></span><span class="n">6</span><span class="d">Armele se vand din stocul firmei, la preturile puse de sef.</span></li>
<li><span class="t"><a href="/afaceri/frizerie">Frizerie</a></span><span class="n">2</span><span class="d">Fiecare tunsoare consuma din stocul de consumabile al frizeriei.</span></li>
<li><span class="t"><a href="/afaceri/tattoo">Salon de tatuaje</a></span><span class="n">3</span><span class="d">Fiecare tatuaj consuma din stocul de consumabile al salonului.</span></li>
<li><span class="t"><a href="/afaceri/club">Club</a></span><span class="n">1</span><span class="d">Bar cu stoc propriu, bilete la intrare si cabina de DJ.</span></li>
<li><span class="t">Salon de infrumusetare</span><span class="n">1</span><span class="d">Lucreaza cu creme si consumabile luate de la furnizorul de salon.</span></li>
</ul>
</div>
<h2 class="ebc-h2">Proprietar, sef, angajat</h2>
<p class="ebc-sub">Nu exista grade fixe. Fiecare om din firma are o <b>functie</b> scrisa de sef (orice text: Mecanic, Manager, Casier), un <b>salariu</b> si, optional, bifa de <b>sef</b>. Poti lucra la mai multe firme in acelasi timp.</p>
<ul class="ebc-matrix">
<li><span>Ce poti face</span><span>Patron</span><span>Sef</span><span>Angajat</span></li>
<li><span>Intri in tura (pontaj) din tableta</span><span><i class="y">&#10003;</i></span><span><i class="y">&#10003;</i></span><span><i class="y">&#10003;</i></span></li>
<li><span>Dai facturi cu terminalul POS</span><span><i class="y">&#10003;</i></span><span><i class="y">&#10003;</i></span><span><i class="y">&#10003;</i></span></li>
<li><span>Vezi stocul si avertismentele firmei</span><span><i class="y">&#10003;</i></span><span><i class="y">&#10003;</i></span><span><i class="y">&#10003;</i></span></li>
<li><span>Angajezi, concediezi, schimbi functia si salariul</span><span><i class="y">&#10003;</i></span><span><i class="y">&#10003;</i></span><span><i class="x">&ndash;</i></span></li>
<li><span>Pui preturile si programul firmei</span><span><i class="y">&#10003;</i></span><span><i class="y">&#10003;</i></span><span><i class="x">&ndash;</i></span></li>
<li><span>Depui bani in contul firmei</span><span><i class="y">&#10003;</i></span><span><i class="y">&#10003;</i></span><span><i class="x">&ndash;</i></span></li>
<li><span>Deschizi seiful sefului</span><span><i class="y">&#10003;</i></span><span><i class="y">&#10003;</i></span><span><i class="x">&ndash;</i></span></li>
<li><span>Numesti sau scoti sefi</span><span><i class="y">&#10003;</i></span><span><i class="x">&ndash;</i></span><span><i class="x">&ndash;</i></span></li>
<li><span>Scoti bani din contul firmei</span><span><i class="y">&#10003;</i></span><span><i class="x">&ndash;</i></span><span><i class="x">&ndash;</i></span></li>
<li><span>Platesti intretinerea firmei</span><span><i class="y">&#10003;</i></span><span><i class="x">&ndash;</i></span><span><i class="x">&ndash;</i></span></li>
</ul>
<p class="ebc-note">Cand angajezi pe cineva, stai langa el si il cauti in tableta dupa nume si ID (campul se numeste CNP). Omul angajat primeste pe loc un <b>contract de munca</b>. Un angajat poate pleca singur din firma, din tableta.</p>
<h2 class="ebc-h2">Tableta firmei</h2>
<p class="ebc-sub">Firma se conduce dintr-un singur obiect: <b>tableta de firma</b>, de cumparat de la <a href="/proprietati/digitalden">Digital Den</a>. O folosesti din inventar. Daca lucrezi la mai multe firme, alegi intai firma.</p>
<div class="ebc-tablet-wrap">
<div class="ebc-tablet" aria-hidden="true">
<div class="ebc-tablet-top"><b>Firma ta</b><span class="ebc-shift">Incheie tura</span></div>
<ul class="ebc-tabs"><li class="cur">Dashboard</li><li>Bani</li><li>Angajati</li><li>Angajeaza</li><li>Preturi</li><li>Furnizor</li><li>Stoc</li><li>Avertismente</li><li>Vanzari</li><li>Loguri</li><li>Setari</li></ul>
<ul class="ebc-tiles"><li>Sold curent<i class="g"></i></li><li>Venit saptamana<i class="r"></i></li><li>Venit luna<i class="g"></i></li><li>Angajati<i></i></li></ul>
</div>
<ul class="ebc-tabdesc">
<li><b>Dashboard</b>: soldul firmei, venitul pe saptamana si pe luna, intretinerea si scadenta ei.</li>
<li><b>Bani</b>: depui sau scoti bani din contul firmei.</li>
<li><b>Angajati</b>: functie, salariu, orele de pontaj si cati bani a adus fiecare om, pe saptamana si pe luna.</li>
<li><b>Preturi</b>: pretul fiecarui produs, pana la un maxim stabilit de server (magazine, haine, arme, frizerie, tatuaje, club).</li>
<li><b>Furnizor</b> (service): comanzi piese si kituri direct in depozitul firmei.</li>
<li><b>Stoc</b>: cat mai ai din fiecare produs sau consumabil.</li>
<li><b>Vanzari</b>: apare doar la club si la magazine.</li>
<li><b>Loguri</b> si <b>Setari</b>: tot ce s-a intamplat in firma, programul de lucru si controlul manual al turei.</li>
</ul>
</div>
<p class="ebc-note">Un angajat simplu vede in tableta doar ce ii trebuie pe tura: butonul de pontaj, stocul, avertismentele si, la service, furnizorul.</p>
<h2 class="ebc-h2">Pontaj si salariu</h2>
<div class="ebc-two">
<ol class="ebc-steps">
<li><b>Intri in tura</b> din tableta, cu butonul <b>Incepe tura</b>. Nu poti cat timp esti AFK sau dormi.</li>
<li>Daca firma are <b>program de lucru</b>, intri in tura doar in orele lui. Cand se termina programul, iesi automat din tura.</li>
<li>Seful poate <b>deschide tura manual</b> in afara programului sau o poate <b>incheia</b> pentru toti pana la miezul noptii.</li>
<li>La fiecare <b>payday</b> (o data pe ora) primesti in banca salariul tau, platit din contul firmei. Doar daca esti in tura la firma aceea.</li>
</ol>
<div class="ebc-card">
<h3 class="ebc-h3">La service e mai strict</h3>
<p>Ca mecanic intri in tura doar daca esti langa service sau langa o masina de lucru. Serverul verifica asta in fiecare minut: daca pleci departe de amandoua, iesi din tura.</p>
<p>Cand intri in tura la un service devii automat mecanic la datorie.</p>
<h3 class="ebc-h3" style="margin-top:0.9rem">Fara bani in cont, fara salariu</h3>
<p>Daca firma nu are destui bani, nu primesti salariul si iti apare un mesaj. Tine contul firmei plin.</p>
</div>
</div>
<h2 class="ebc-h2">Banii firmei</h2>
<p class="ebc-sub">Firma are contul ei, separat de banii tai. Uite de unde intra banii si unde pleaca.</p>
<div class="ebc-flow">
<div class="col in">
<h3>Intra</h3>
<ul>
<li><b>Partea din vanzari</b>Firma ia un procent din fiecare vanzare (produse, haine, tuning). Procentul creste cu fiecare angajat aflat in tura langa firma, pana la o limita.</li>
<li><b>Facturi POS</b>Facturile date de angajati intra in contul firmei.</li>
<li><b>Depuneri</b>Patronul si sefii pot pune bani de-ai lor, din cash sau din banca.</li>
</ul>
</div>
<div class="col vault">
<svg viewBox="0 0 64 64" aria-hidden="true"><rect x="6" y="10" width="52" height="44" rx="6" fill="#1f1f23" stroke="#f5b931" stroke-width="2.5"/><circle cx="32" cy="32" r="11" fill="none" stroke="#f5b931" stroke-width="2.5"/><path d="M32 21v6M32 37v6M21 32h6M37 32h6" stroke="#f5b931" stroke-width="2.5" stroke-linecap="round"/><rect x="12" y="54" width="8" height="4" rx="1" fill="#f5b931"/><rect x="44" y="54" width="8" height="4" rx="1" fill="#f5b931"/></svg>
<b>Contul firmei</b>
<span>Soldul si venitul il vezi in Dashboard, fiecare miscare in Loguri.</span>
</div>
<div class="col out">
<h3>Iese</h3>
<ul>
<li><b>Salarii</b>La fiecare payday, pentru angajatii aflati in tura.</li>
<li><b>Retrageri</b>Doar patronul scoate bani, direct in contul lui din banca.</li>
</ul>
</div>
</div>
<h2 class="ebc-h2">Stoc, depozit si furnizori</h2>
<div class="ebc-two">
<div class="ebc-card">
<h3 class="ebc-h3">Furnizorii de pe harta</h3>
<p>Magazinele, magazinele de haine, frizeriile, saloanele de tatuaje, salonul de infrumusetare si barul clubului isi iau marfa de la furnizori NPC, marcati pe harta (<b>Furnizor Magazin</b>, <b>Furnizor Magazin Haine</b>, <b>Furnizor Frizer</b>, <b>Furnizor Tatuaje</b>, <b>Furnizor Salon</b>, <b>Furnizor Bar</b>).</p>
<p>Doar angajatii firmei pot cumpara. Primesti o cutie cu marfa. La haine, frizerie si tatuaje, cand o deschizi langa firma, marfa intra direct in stoc. La magazin, club si salon, marfa iti intra in inventar si o pui tu in depozitul firmei. Fiecare produs are o limita de stoc.</p>
</div>
<div class="ebc-card">
<h3 class="ebc-h3">Furnizorul din tableta (service)</h3>
<p>Mecanicii comanda din tab-ul <b>Furnizor</b>: parti de caroserie, parti principale, parti de service, kit-uri si obiecte de atelier. Platesti din banii tai, iar piesele ajung direct in depozitul service-ului, daca e loc in el.</p>
<h3 class="ebc-h3" style="margin-top:0.9rem">Depozit si seif</h3>
<p>Multe firme au un <b>depozit</b> la sediu, deschis pentru angajati, si un <b>seif al sefului</b>, doar pentru sefi si patron.</p>
</div>
</div>
<p class="ebc-note">Regula EBC: patronul trebuie sa tina un stoc constant. O firma fara stoc poate fi luata inapoi si scoasa din nou la licitatie.</p>
<h2 class="ebc-h2">Facturi cu terminalul POS</h2>
<div class="ebc-two">
<ol class="ebc-steps">
<li>Cumpara un <b>Terminal POS</b> de la <a href="/proprietati/digitalden">Digital Den</a> si foloseste-l din inventar.</li>
<li>Daca lucrezi la mai multe firme, alegi firma care incaseaza. Apoi scrii numele clientului: trebuie sa fie langa tine.</li>
<li>Alegi o factura libera (suma si motivul le scrii tu, pana la o limita) sau un serviciu din lista. Mecanicii au gata facute: reparatii complete, reparatii motor, pana.</li>
<li>Clientul vede factura si o accepta sau o refuza. Daca accepta, banii se iau intai din cash, apoi din banca.</li>
</ol>
<div>
<div class="ebc-receipt" aria-hidden="true">
<p class="rh">CHITANTA</p>
<ul><li><span>Emitent</span><span>Andrei Popescu</span></li><li><span>Client</span><span>Mihai Ionescu</span></li><li><span>Motiv</span><span>Reparatii motor</span></li><li><span>Suma</span><span>800 €</span></li></ul>
<p class="rf">08-11-2026 14:30</p>
</div>
<div class="ebc-card" style="margin-top:0.9rem">
<ul class="ebc-dots">
<li>Banii intra in contul firmei. La service, angajatul care a dat factura primeste si el o parte.</li>
<li>Daca nu esti angajat nicaieri, banii facturii raman la tine.</li>
<li>Un politist sau un medic SMIR aflat la datorie nu plateste factura de la service: o plateste statul, pana la o limita.</li>
<li>Amandoi primiti chitanta, iar factura apare in statistica angajatului.</li>
</ul>
</div>
</div>
</div>
<h2 class="ebc-h2">Avertismente si intretinere</h2>
<div class="ebc-two">
<div class="ebc-card">
<h3 class="ebc-h3">Avertismente</h3>
<p>Sindicatul si staff-ul pot da avertismente unei firme, de cate <b>0.5</b> sau <b>1</b>. O firma poate avea cel mult <b>3</b> active in acelasi timp, iar fiecare expira dupa <b>30 de zile</b>. Toata firma le vede in tab-ul Avertismente.</p>
<div class="ebc-meter" aria-hidden="true"><span class="f"></span><span class="f"></span><span class="f"></span><span></span><span></span><span></span></div>
<div class="ebc-meter-l" aria-hidden="true"><span>0</span><span>1.5 / 3</span><span>3</span></div>
</div>
<div class="ebc-card">
<h3 class="ebc-h3">Intretinere</h3>
<p>Unele firme au o <b>intretinere lunara</b>, platita in coins de patron, din Dashboard. O plata tine firma activa inca 30 de zile.</p>
<p>Dashboard-ul iti arata scadenta si te avertizeaza cand mai ai sub 7 zile. Dupa 3 zile de intarziere, staff-ul primeste o alerta.</p>
</div>
</div>
<div class="ebc-end">
<p>O firma poate fi inchisa daca nu are activitate, nu are stoc sau daca patronul paraseste serverul. Citeste regulile inainte sa intri la licitatie.</p>
<a class="btn" href="/zona-info/regulament#_9-firme-afaceri">Regulament: Firme / Afaceri</a>
</div>
</div>
