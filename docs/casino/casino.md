---
outline: deep
---

<style>
.csn {
  --ink: #0a0a0c;
  --panel: #17171a;
  --panel2: #1f1f23;
  --line: #2f2f36;
  --text: #f4f4f5;
  --mute: #a1a1aa;
  --red: #ef4444;
  --red-deep: #b91c1c;
  --red-soft: rgba(239, 68, 68, 0.14);
  --gold: #f5b931;
  --gold-soft: rgba(245, 185, 49, 0.13);
  --green: #4ade80;
  max-width: 960px;
  margin: 0 auto;
  color: var(--text);
  font-family: Inter, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.csn *, .csn *::before, .csn *::after { box-sizing: border-box; }
.csn p, .csn li { line-height: 1.6; color: var(--text); margin: 0; }
.csn ul, .csn ol { list-style: none; padding: 0; margin: 0; }
.csn li + li { margin-top: 0; }
.csn b { color: #fff; font-weight: 650; }
.csn a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.csn a:hover { color: #fecaca; }
.csn a:focus-visible { outline: 3px solid var(--red); outline-offset: 3px; border-radius: 6px; }
.csn kbd {
  font: inherit; font-size: 0.85em; font-weight: 700; color: #fff; background: var(--red-deep);
  border-radius: 6px; padding: 0.05rem 0.45rem; white-space: nowrap;
}
/* ---------- hero ---------- */
.csn .csn-hero {
  position: relative; overflow: hidden; isolation: isolate;
  background: radial-gradient(80% 110% at 85% 10%, rgba(245, 185, 49, 0.12), transparent 55%),
              radial-gradient(110% 120% at 0% 100%, rgba(185, 28, 28, 0.32), var(--ink) 62%);
  border: 1px solid var(--line); border-radius: 22px;
  padding: clamp(1.15rem, 4vw, 2.4rem);
}
.csn .csn-kicker {
  font-size: 0.78rem; font-weight: 700; letter-spacing: 0.16em; text-transform: uppercase; color: var(--gold);
  margin-bottom: 0.55rem;
}
.csn .csn-hero h1 {
  margin: 0 0 0.75rem; border: 0; padding: 0;
  font-size: clamp(2.1rem, 7vw, 3.6rem); line-height: 1.02; font-weight: 800; letter-spacing: -0.03em; color: #fff;
}
.csn .csn-hero h1 span { color: var(--red); }
.csn .csn-lede { max-width: 60ch; color: var(--mute); font-size: 1.05rem; }
.csn .csn-stage { display: block; width: 100%; height: auto; margin-top: 1.3rem; border-radius: 16px; }
.csn-stage .bg { fill: #0d0b0e; }
.csn-stage .ray { fill: #fff; opacity: 0.025; }
.csn-stage .floor { fill: #120d0f; }
.csn-stage .floor-line { stroke: #2a1d20; stroke-width: 1; }
/* neon sign */
.csn-stage .neon-box { fill: none; stroke: var(--red); stroke-width: 2.5; }
.csn-stage .neon-glow { fill: none; stroke: var(--red); stroke-width: 9; opacity: 0.16; }
.csn-stage .neon-t { font: 800 30px Inter, system-ui, sans-serif; letter-spacing: 0.32em; }
.csn-stage .neon-t.glow { fill: none; stroke: var(--gold); stroke-width: 7; opacity: 0.16; }
.csn-stage .neon-t.core { fill: #ffe7a8; stroke: var(--gold); stroke-width: 1; }
.csn-stage .neon-sign { animation: csn-flicker 9s linear infinite; }
.csn-stage .bulb { fill: var(--gold); opacity: 0.35; }
.csn-stage .bulbs-a .bulb { animation: csn-bulb 1.2s steps(1, end) infinite; }
.csn-stage .bulbs-b .bulb { animation: csn-bulb 1.2s steps(1, end) -0.6s infinite; }
@keyframes csn-flicker {
  0%, 41%, 44%, 47%, 100% { opacity: 1; }
  42%, 46% { opacity: 0.35; }
}
@keyframes csn-bulb { 0% { opacity: 1; } 50% { opacity: 0.25; } }
/* slot machine */
.csn-stage .cab { fill: #1a1418; stroke: #3a2a30; stroke-width: 2; }
.csn-stage .cab-top { fill: var(--red-deep); }
.csn-stage .cab-trim { fill: none; stroke: var(--gold); stroke-width: 2; opacity: 0.85; }
.csn-stage .window { fill: #f6f1e7; }
.csn-stage .reel-sep { stroke: #c9bfae; stroke-width: 2; }
.csn-stage .payline { stroke: var(--red); stroke-width: 2; opacity: 0.7; }
.csn-stage .shade { fill: url(#csn-shade); }
.csn-stage .strip { animation-duration: 7s; animation-iteration-count: infinite; animation-timing-function: cubic-bezier(.35, .05, .2, 1); }
.csn-stage .strip.r1 { animation-name: csn-reel1; }
.csn-stage .strip.r2 { animation-name: csn-reel2; }
.csn-stage .strip.r3 { animation-name: csn-reel3; }
@keyframes csn-reel1 { 0%, 9% { transform: translateY(0); } 38%, 100% { transform: translateY(-480px); } }
@keyframes csn-reel2 { 0%, 9% { transform: translateY(0); } 47%, 100% { transform: translateY(-480px); } }
@keyframes csn-reel3 { 0%, 9% { transform: translateY(0); } 56%, 100% { transform: translateY(-480px); } }
.csn-stage .win-lamp { fill: #2a1a1d; }
.csn-stage .win-t { font: 800 15px Inter, system-ui, sans-serif; letter-spacing: 0.3em; fill: #5a3a40; }
.csn-stage .win-on { opacity: 0; animation: csn-win 7s linear infinite; }
.csn-stage .win-on rect { fill: var(--red); }
.csn-stage .win-on text { font: 800 15px Inter, system-ui, sans-serif; letter-spacing: 0.3em; fill: #fff; }
@keyframes csn-win {
  0%, 58% { opacity: 0; }
  60%, 66%, 72%, 78%, 84% { opacity: 1; }
  63%, 69%, 75%, 81% { opacity: 0.2; }
  92%, 100% { opacity: 0; }
}
.csn-stage .lever { transform-origin: 468px 222px; animation: csn-lever 7s ease-in-out infinite; }
.csn-stage .lever-rod { stroke: #9ca3af; stroke-width: 5; stroke-linecap: round; }
.csn-stage .lever-ball { fill: var(--red); }
@keyframes csn-lever { 0%, 1% { transform: rotate(0); } 5% { transform: rotate(38deg); } 10%, 100% { transform: rotate(0); } }
.csn-stage .sym-7 { font: 900 44px Inter, system-ui, sans-serif; fill: #dc2626; }
.csn-stage .sym-bar { fill: #18181b; }
.csn-stage .sym-bar-t { font: 800 11px Inter, system-ui, sans-serif; fill: #fff; letter-spacing: 0.08em; }
.csn-stage .sym-cherry { fill: #dc2626; }
.csn-stage .sym-stem { fill: none; stroke: #15803d; stroke-width: 2.5; stroke-linecap: round; }
.csn-stage .sym-dia { fill: #38bdf8; stroke: #0369a1; stroke-width: 1.5; }
.csn-stage .sym-bell { fill: var(--gold); stroke: #a16207; stroke-width: 1.5; }
/* chips and cards */
.csn-stage .chip-base { fill: var(--red-deep); }
.csn-stage .chip-base.k { fill: #18181b; }
.csn-stage .chip-base.g { fill: #166534; }
.csn-stage .chip-edge { fill: none; stroke: #fff; stroke-width: 4; stroke-dasharray: 6 6.56; }
.csn-stage .chip-in { fill: none; stroke: rgba(255, 255, 255, 0.55); stroke-width: 1.5; }
.csn-stage .chip-side { fill: #7f1d1d; }
.csn-stage .chip-side.k { fill: #09090b; }
.csn-stage .chip-side.g { fill: #14532d; }
.csn-stage .chip-ring { transform-box: fill-box; transform-origin: center; animation: csn-spin 6s linear infinite; }
.csn-stage .chip-ring.rev { animation-direction: reverse; animation-duration: 8s; }
.csn-stage .float-a { animation: csn-float 5s ease-in-out infinite; }
.csn-stage .float-b { animation: csn-float 6s ease-in-out -2s infinite; }
.csn-stage .float-c { animation: csn-float 7s ease-in-out -4s infinite; }
@keyframes csn-spin { to { transform: rotate(360deg); } }
@keyframes csn-float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-9px); } }
.csn-stage .card { fill: #fafafa; stroke: #d4d4d8; stroke-width: 1; }
.csn-stage .card-red { fill: #dc2626; font: 800 15px Inter, system-ui, sans-serif; }
.csn-stage .card-blk { fill: #18181b; font: 800 15px Inter, system-ui, sans-serif; }
.csn-stage .die { fill: #fafafa; stroke: #d4d4d8; stroke-width: 1; }
.csn-stage .pip { fill: #18181b; }
.csn-stage .pip.r { fill: #dc2626; }
/* hero stats */
.csn .csn-stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(118px, 1fr)); gap: 0.6rem; margin-top: 1.2rem; }
.csn .csn-stats li { background: rgba(23, 23, 26, 0.85); border: 1px solid var(--line); border-radius: 14px; padding: 0.7rem 0.9rem; }
.csn .csn-stats b { display: block; font-size: clamp(1.35rem, 4vw, 1.8rem); line-height: 1.1; font-weight: 800; color: var(--gold); font-variant-numeric: tabular-nums; }
.csn .csn-stats span { display: block; color: var(--mute); font-size: 0.84rem; line-height: 1.35; margin-top: 0.2rem; }
@media (prefers-reduced-motion: reduce) {
  .csn .csn-stage .neon-sign, .csn .csn-stage .bulb, .csn .csn-stage .strip, .csn .csn-stage .win-on,
  .csn .csn-stage .lever, .csn .csn-stage .chip-ring, .csn .csn-stage .float-a, .csn .csn-stage .float-b,
  .csn .csn-stage .float-c { animation: none; }
  .csn .csn-stage .win-on { opacity: 1; }
}
/* ---------- sections ---------- */
.csn .csn-h2 {
  display: flex; align-items: flex-start; gap: 0.65rem;
  margin: 3rem 0 0.9rem; border: 0; padding: 0;
  font-size: 1.5rem; font-weight: 750; letter-spacing: -0.015em; line-height: 1.25; color: #fff;
}
.csn .csn-h2::before { margin-top: calc(0.5lh - 0.9rem / 2);
  content: ''; flex: none; width: 0.9rem; height: 0.9rem; border-radius: 50%;
  background: var(--red-deep); border: 3px dashed #fff; box-shadow: 0 0 0 3px var(--red-soft);
}
.csn .csn-h3 { margin: 0 0 0.35rem; border: 0; padding: 0; font-size: 1.05rem; font-weight: 700; color: #fff; line-height: 1.3; }
.csn .csn-sub { color: var(--mute); max-width: 66ch; margin-bottom: 1rem; }
.csn .csn-card { background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 1.1rem 1.25rem; }
.csn .csn-card p { color: var(--mute); font-size: 0.97rem; }
.csn .csn-card p + p { margin-top: 0.5rem; }
.csn .csn-tag {
  display: inline-block; font-size: 0.72rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase;
  color: var(--gold); margin-bottom: 0.4rem;
}
/* where */
.csn .csn-where { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 0.75rem; }
.csn .csn-where .csn-card:first-child { background: linear-gradient(160deg, var(--gold-soft), var(--panel) 60%); border-color: #4a3d1c; }
.csn .csn-path {
  display: inline-flex; flex-wrap: wrap; align-items: center; gap: 0.3rem; margin-top: 0.5rem;
  font-size: 0.9rem; font-weight: 650; color: #fff;
}
.csn .csn-path span { position: relative; background: var(--panel2); border: 1px solid var(--line); border-radius: 8px; padding: 0.1rem 0.5rem; }
/* the arrow belongs to the next chip, so a wrapped line never starts or ends on a lone arrow */
.csn .csn-path > span + span { margin-left: 1.2rem; }
.csn .csn-path > span + span::before { content: '\2192'; position: absolute; left: -1.05rem; color: var(--red); }
/* money flow */
.csn .csn-flow { border: 1px solid var(--line); border-radius: 16px; overflow: hidden; background: var(--panel); }
.csn .csn-flow li {
  display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1.2fr) minmax(0, 1.2fr); gap: 0.75rem; align-items: center;
  padding: 0.7rem 1rem; border-top: 1px solid var(--line); font-size: 0.93rem; color: var(--mute);
}
.csn .csn-flow li:first-child {
  border-top: 0; background: var(--panel2); font-size: 0.74rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase;
}
.csn .csn-flow li > span:first-child { color: #fff; font-weight: 700; }
.csn .csn-flow li:first-child > span:first-child { color: var(--mute); }
@media (max-width: 560px) {
  .csn .csn-flow li { grid-template-columns: minmax(0, 1fr); gap: 0.15rem; }
  .csn .csn-flow li:first-child { display: none; }
  .csn .csn-flow li > span:nth-child(2)::before { content: 'Platesti: '; color: var(--gold); font-weight: 650; }
  .csn .csn-flow li > span:nth-child(3)::before { content: 'Castigul: '; color: var(--gold); font-weight: 650; }
}
/* chips counter */
.csn .csn-counter { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 0.75rem; margin-top: 0.75rem; }
.csn .csn-counter .csn-card { border-color: #3d2a2e; }
/* games */
.csn .csn-games { display: grid; grid-template-columns: minmax(0, 1fr); gap: 1rem; }
.csn .csn-game {
  position: relative; background: var(--panel); border: 1px solid var(--line); border-radius: 18px;
  padding: 1.2rem 1.3rem 1.25rem; overflow: hidden;
}
.csn .csn-game::before {
  content: ''; position: absolute; inset: 0 auto 0 0; width: 4px; background: var(--red);
}
.csn .csn-game.gold::before { background: var(--gold); }
.csn .csn-game.green::before { background: var(--green); }
.csn .csn-game-head { display: flex; flex-wrap: wrap; align-items: center; gap: 0.5rem 0.85rem; margin-bottom: 0.65rem; }
.csn .csn-game-head svg { flex: none; width: 2.6rem; height: 2.6rem; }
.csn .csn-game-head .csn-h3 { margin: 0; font-size: 1.2rem; }
.csn .csn-game-head .csn-where-pill {
  font-size: 0.78rem; font-weight: 650; color: var(--mute); background: var(--panel2);
  border: 1px solid var(--line); border-radius: 999px; padding: 0.15rem 0.65rem;
}
@media (max-width: 560px) {
  /* phone: the pill always goes under the title, next to the icon */
  .csn .csn-game-head { display: grid; grid-template-columns: auto minmax(0, 1fr); gap: 0.3rem 0.85rem; }
  .csn .csn-game-head svg { grid-row: span 2; align-self: center; }
  .csn .csn-game-head .csn-where-pill { justify-self: start; }
}
.csn .csn-game > p:not(.csn-mini) { color: var(--mute); font-size: 0.97rem; max-width: 70ch; }
.csn .csn-cols { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 0.9rem 1.4rem; margin-top: 0.9rem; }
.csn .csn-steps { counter-reset: csn-step; }
.csn .csn-steps li {
  position: relative; counter-increment: csn-step; padding-left: 2rem; color: var(--text); font-size: 0.95rem;
}
.csn .csn-steps li + li { margin-top: 0.45rem; }
.csn .csn-steps li::before {
  content: counter(csn-step); position: absolute; left: 0; top: 0.1rem;
  width: 1.35rem; height: 1.35rem; border-radius: 50%; display: grid; place-items: center;
  font-size: 0.75rem; font-weight: 800; color: #fff; background: var(--red-deep);
}
.csn .csn-facts li { position: relative; padding-left: 1.2rem; color: var(--mute); font-size: 0.94rem; }
.csn .csn-facts li + li { margin-top: 0.4rem; }
.csn .csn-facts li::before {
  content: ''; position: absolute; left: 0.1rem; top: 0.55rem; width: 0.45rem; height: 0.45rem;
  background: var(--gold); transform: rotate(45deg);
}
.csn .csn-mini {
  font-size: 0.72rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: var(--gold);
  margin: 0 0 0.45rem;
}
.csn .csn-gap { margin-top: 1rem; }
.csn .csn-prizes { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-top: 0.3rem; }
.csn .csn-prizes li {
  font-size: 0.84rem; font-weight: 650; color: var(--text); background: var(--panel2);
  border: 1px solid var(--line); border-radius: 999px; padding: 0.2rem 0.65rem;
}
.csn .csn-prizes li.top { border-color: #6b5320; background: var(--gold-soft); color: #fde68a; }
.csn .csn-symbols { display: flex; flex-wrap: wrap; gap: 0.35rem; margin-top: 0.3rem; }
.csn .csn-symbols li {
  font-size: 0.82rem; font-weight: 650; color: #18181b; background: #f6f1e7; border-radius: 8px; padding: 0.15rem 0.55rem;
}
.csn .csn-note {
  margin-top: 1rem; padding: 0.85rem 1rem; border-radius: 14px; border: 1px dashed #3f3f46;
  color: var(--mute); font-size: 0.93rem;
}
.csn .csn-note b { color: var(--gold); }
</style>

<div class="csn">

<section class="csn-hero" aria-labelledby="csn-title">
<p class="csn-kicker">Diamond Casino &middot; East Vinewood</p>
<h1 id="csn-title">Casino<span>.</span></h1>
<p class="csn-lede">Roata norocului cu masina pe podium, pacanele, coinflip si barbut cu alti jucatori. Joci cu bani, castigurile vin direct la tine. Nu ai nevoie de un minim de ore jucate.</p>
<svg class="csn-stage" viewBox="0 0 640 300" role="img" aria-label="Firma luminoasa CASINO deasupra unui aparat de pacanele care se opreste pe 7-7-7, cu jetoane, carti si zaruri pe masa">
<defs>
<linearGradient id="csn-shade" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#000" stop-opacity="0.45"/>
<stop offset="0.28" stop-color="#000" stop-opacity="0"/>
<stop offset="0.72" stop-color="#000" stop-opacity="0"/>
<stop offset="1" stop-color="#000" stop-opacity="0.45"/>
</linearGradient>
<clipPath id="csn-win-clip"><rect x="238" y="128" width="174" height="60" rx="4"/></clipPath>
</defs>
<rect class="bg" x="0" y="0" width="640" height="300"/>
<polygon class="ray" points="320,0 250,300 290,300"/>
<polygon class="ray" points="320,0 350,300 400,300"/>
<polygon class="ray" points="320,0 120,300 180,300"/>
<polygon class="ray" points="320,0 480,300 540,300"/>
<rect class="floor" x="0" y="252" width="640" height="48"/>
<line class="floor-line" x1="0" y1="252" x2="640" y2="252"/>
<g class="neon-sign">
<rect class="neon-glow" x="196" y="14" width="248" height="52" rx="12"/>
<rect class="neon-box" x="196" y="14" width="248" height="52" rx="12"/>
<text class="neon-t glow" x="324" y="51" text-anchor="middle">CASINO</text>
<text class="neon-t core" x="324" y="51" text-anchor="middle">CASINO</text>
</g>
<rect class="cab" x="222" y="76" width="206" height="176" rx="14"/>
<path class="cab-top" d="M222 104 V90 Q222 76 236 76 H414 Q428 76 428 90 V104 Z"/>
<g class="bulbs-a"><circle class="bulb" cx="240" cy="90" r="3.5"/><circle class="bulb" cx="280" cy="90" r="3.5"/><circle class="bulb" cx="320" cy="90" r="3.5"/><circle class="bulb" cx="360" cy="90" r="3.5"/><circle class="bulb" cx="400" cy="90" r="3.5"/></g>
<g class="bulbs-b"><circle class="bulb" cx="260" cy="90" r="3.5"/><circle class="bulb" cx="300" cy="90" r="3.5"/><circle class="bulb" cx="340" cy="90" r="3.5"/><circle class="bulb" cx="380" cy="90" r="3.5"/><circle class="bulb" cx="410" cy="90" r="3.5"/></g>
<rect class="cab-trim" x="232" y="120" width="186" height="76" rx="8"/>
<rect class="window" x="238" y="128" width="174" height="60" rx="4"/>
<g clip-path="url(#csn-win-clip)">
<g transform="translate(239 128)"><g class="strip r1">
<g transform="translate(0 0)"><text class="sym-7" x="26" y="46" text-anchor="middle">7</text></g><g transform="translate(0 60)"><path class="sym-stem" d="M20 34 Q24 18 34 14 M33 36 Q32 22 34 14"/><circle class="sym-cherry" cx="19" cy="38" r="8"/><circle class="sym-cherry" cx="33" cy="40" r="8"/></g><g transform="translate(0 120)"><rect class="sym-bar" x="6" y="21" width="40" height="18" rx="3"/><text class="sym-bar-t" x="26" y="34" text-anchor="middle">BAR</text></g><g transform="translate(0 180)"><polygon class="sym-dia" points="14,24 20,16 32,16 38,24 26,44"/></g><g transform="translate(0 240)"><path class="sym-bell" d="M26 14 C17 14 16 24 15 32 L12 38 H40 L37 32 C36 24 35 14 26 14 Z"/><circle class="sym-bell" cx="26" cy="41" r="3.5"/></g><g transform="translate(0 300)"><path class="sym-stem" d="M20 34 Q24 18 34 14 M33 36 Q32 22 34 14"/><circle class="sym-cherry" cx="19" cy="38" r="8"/><circle class="sym-cherry" cx="33" cy="40" r="8"/></g><g transform="translate(0 360)"><rect class="sym-bar" x="6" y="21" width="40" height="18" rx="3"/><text class="sym-bar-t" x="26" y="34" text-anchor="middle">BAR</text></g><g transform="translate(0 420)"><polygon class="sym-dia" points="14,24 20,16 32,16 38,24 26,44"/></g><g transform="translate(0 480)"><text class="sym-7" x="26" y="46" text-anchor="middle">7</text></g>
</g></g>
<g transform="translate(299 128)"><g class="strip r2">
<g transform="translate(0 0)"><text class="sym-7" x="26" y="46" text-anchor="middle">7</text></g><g transform="translate(0 60)"><path class="sym-bell" d="M26 14 C17 14 16 24 15 32 L12 38 H40 L37 32 C36 24 35 14 26 14 Z"/><circle class="sym-bell" cx="26" cy="41" r="3.5"/></g><g transform="translate(0 120)"><polygon class="sym-dia" points="14,24 20,16 32,16 38,24 26,44"/></g><g transform="translate(0 180)"><path class="sym-stem" d="M20 34 Q24 18 34 14 M33 36 Q32 22 34 14"/><circle class="sym-cherry" cx="19" cy="38" r="8"/><circle class="sym-cherry" cx="33" cy="40" r="8"/></g><g transform="translate(0 240)"><rect class="sym-bar" x="6" y="21" width="40" height="18" rx="3"/><text class="sym-bar-t" x="26" y="34" text-anchor="middle">BAR</text></g><g transform="translate(0 300)"><path class="sym-bell" d="M26 14 C17 14 16 24 15 32 L12 38 H40 L37 32 C36 24 35 14 26 14 Z"/><circle class="sym-bell" cx="26" cy="41" r="3.5"/></g><g transform="translate(0 360)"><path class="sym-stem" d="M20 34 Q24 18 34 14 M33 36 Q32 22 34 14"/><circle class="sym-cherry" cx="19" cy="38" r="8"/><circle class="sym-cherry" cx="33" cy="40" r="8"/></g><g transform="translate(0 420)"><rect class="sym-bar" x="6" y="21" width="40" height="18" rx="3"/><text class="sym-bar-t" x="26" y="34" text-anchor="middle">BAR</text></g><g transform="translate(0 480)"><text class="sym-7" x="26" y="46" text-anchor="middle">7</text></g>
</g></g>
<g transform="translate(359 128)"><g class="strip r3">
<g transform="translate(0 0)"><text class="sym-7" x="26" y="46" text-anchor="middle">7</text></g><g transform="translate(0 60)"><polygon class="sym-dia" points="14,24 20,16 32,16 38,24 26,44"/></g><g transform="translate(0 120)"><path class="sym-stem" d="M20 34 Q24 18 34 14 M33 36 Q32 22 34 14"/><circle class="sym-cherry" cx="19" cy="38" r="8"/><circle class="sym-cherry" cx="33" cy="40" r="8"/></g><g transform="translate(0 180)"><path class="sym-bell" d="M26 14 C17 14 16 24 15 32 L12 38 H40 L37 32 C36 24 35 14 26 14 Z"/><circle class="sym-bell" cx="26" cy="41" r="3.5"/></g><g transform="translate(0 240)"><rect class="sym-bar" x="6" y="21" width="40" height="18" rx="3"/><text class="sym-bar-t" x="26" y="34" text-anchor="middle">BAR</text></g><g transform="translate(0 300)"><polygon class="sym-dia" points="14,24 20,16 32,16 38,24 26,44"/></g><g transform="translate(0 360)"><path class="sym-bell" d="M26 14 C17 14 16 24 15 32 L12 38 H40 L37 32 C36 24 35 14 26 14 Z"/><circle class="sym-bell" cx="26" cy="41" r="3.5"/></g><g transform="translate(0 420)"><path class="sym-stem" d="M20 34 Q24 18 34 14 M33 36 Q32 22 34 14"/><circle class="sym-cherry" cx="19" cy="38" r="8"/><circle class="sym-cherry" cx="33" cy="40" r="8"/></g><g transform="translate(0 480)"><text class="sym-7" x="26" y="46" text-anchor="middle">7</text></g>
</g></g>
<rect class="shade" x="238" y="128" width="174" height="60"/>
</g>
<line class="reel-sep" x1="296" y1="128" x2="296" y2="188"/>
<line class="reel-sep" x1="354" y1="128" x2="354" y2="188"/>
<line class="payline" x1="232" y1="158" x2="418" y2="158"/>
<rect class="win-lamp" x="270" y="206" width="110" height="26" rx="13"/>
<text class="win-t" x="327" y="224" text-anchor="middle">CASTIG</text>
<g class="win-on"><rect x="270" y="206" width="110" height="26" rx="13"/><text x="327" y="224" text-anchor="middle">CASTIG</text></g>
<rect class="cab" x="428" y="196" width="18" height="34" rx="4"/>
<g class="lever"><line class="lever-rod" x1="468" y1="222" x2="468" y2="150"/><circle class="lever-ball" cx="468" cy="146" r="9"/></g>
<line class="lever-rod" x1="446" y1="222" x2="468" y2="222"/>
<g transform="translate(70 196) rotate(-14)"><rect class="card" x="0" y="0" width="40" height="56" rx="5"/><text class="card-blk" x="7" y="20">A</text><text class="card-blk" x="20" y="44" text-anchor="middle">&#9824;</text></g>
<g transform="translate(96 190) rotate(9)"><rect class="card" x="0" y="0" width="40" height="56" rx="5"/><text class="card-red" x="7" y="20">K</text><text class="card-red" x="20" y="44" text-anchor="middle">&#9829;</text></g>
<g transform="translate(156 236)"><ellipse class="chip-side" cx="0" cy="12" rx="18" ry="6"/><ellipse class="chip-side" cx="0" cy="6" rx="18" ry="6"/><ellipse class="chip-side" cx="0" cy="0" rx="18" ry="6"/><ellipse class="chip-base" cx="0" cy="-4" rx="18" ry="6"/></g>
<g transform="translate(186 242)"><ellipse class="chip-side k" cx="0" cy="6" rx="18" ry="6"/><ellipse class="chip-side k" cx="0" cy="0" rx="18" ry="6"/><ellipse class="chip-base k" cx="0" cy="-4" rx="18" ry="6"/></g>
<g transform="translate(500 226)"><rect class="die" x="0" y="0" width="30" height="30" rx="6"/><circle class="pip" cx="8" cy="8" r="3"/><circle class="pip" cx="22" cy="8" r="3"/><circle class="pip" cx="8" cy="22" r="3"/><circle class="pip" cx="22" cy="22" r="3"/><circle class="pip" cx="15" cy="15" r="3"/></g>
<g transform="translate(540 236) rotate(16)"><rect class="die" x="0" y="0" width="26" height="26" rx="5"/><circle class="pip r" cx="13" cy="13" r="3.5"/></g>
<g class="float-a"><g transform="translate(96 110)"><circle class="chip-base" r="18"/><g class="chip-ring"><circle class="chip-edge" r="16"/></g><circle class="chip-in" r="10.5"/></g></g>
<g class="float-b"><g transform="translate(548 96)"><circle class="chip-base k" r="18"/><g class="chip-ring rev"><circle class="chip-edge" r="16"/></g><circle class="chip-in" r="10.5"/></g></g>
<g class="float-c"><g transform="translate(590 170)"><circle class="chip-base g" r="18"/><g class="chip-ring"><circle class="chip-edge" r="16"/></g><circle class="chip-in" r="10.5"/></g></g>
<g class="float-b"><g transform="translate(44 168)"><circle class="chip-base" r="18"/><g class="chip-ring"><circle class="chip-edge" r="16"/></g><circle class="chip-in" r="10.5"/></g></g>
<g class="float-c"><g transform="translate(150 62)"><circle class="chip-base g" r="18"/><g class="chip-ring"><circle class="chip-edge" r="16"/></g><circle class="chip-in" r="10.5"/></g></g>
<g class="float-a"><g transform="translate(506 44)"><circle class="chip-base" r="18"/><g class="chip-ring"><circle class="chip-edge" r="16"/></g><circle class="chip-in" r="10.5"/></g></g>
</svg>
<ul class="csn-stats">
<li><b>35</b><span>aparate de pacanele</span></li>
<li><b>3</b><span>mese de coinflip</span></li>
<li><b>20</b><span>felii pe roata norocului</span></li>
<li><b>4</b><span>jocuri diferite</span></li>
</ul>
</section>

<h2 id="unde-este" class="csn-h2">Unde este si cum intri</h2>
<div class="csn-where">
<div class="csn-card">
<p class="csn-tag">Locatie</p>
<h3 class="csn-h3">Diamond Casino, East Vinewood</h3>
<p>Cauta pe harta iconita <b>Casino</b> si mergi la intrarea principala. Intri pe jos, pe usa din fata, nu ai nevoie de bilet sau de invitatie.</p>
<p class="csn-path"><span>Telefon</span><span>Harti</span></p>
</div>
<div class="csn-card">
<p class="csn-tag">Fara masina</p>
<h3 class="csn-h3">Vii cu Ryde</h3>
<p>In aplicatia Ryde, <b>Diamond Casino</b> apare direct in lista de destinatii rapide.</p>
<p class="csn-path"><span>Telefon</span><span>Ryde</span><span>Diamond Casino</span></p>
</div>
<div class="csn-card">
<p class="csn-tag">Zona sigura</p>
<h3 class="csn-h3">Fara arme, fara batai</h3>
<p>Casino-ul si imprejurimile lui sunt zona sigura: armele nu merg si jucatorii nu se pot rani intre ei.</p>
</div>
</div>

<h2 id="bani-si-jetoane" class="csn-h2">Bani si jetoane</h2>
<p class="csn-sub">Toate jocurile din casino merg pe euro, nu pe jetoane. Miza se ia mai intai din banii cash si, daca nu ajung, restul din banca. La barbut conteaza doar banii cash.</p>
<ul class="csn-flow">
<li><span>Joc</span><span>Platesti din</span><span>Castigul intra in</span></li>
<li><span>Roata norocului</span><span>cash, apoi banca</span><span>banca (premiile in bani), inventar (obiectele)</span></li>
<li><span>Pacanele</span><span>cash, apoi banca</span><span>cash</span></li>
<li><span>Coinflip</span><span>cash, apoi banca</span><span>cash</span></li>
<li><span>Barbut</span><span>doar cash, amandoi jucatorii</span><span>cash</span></li>
</ul>
<div class="csn-counter">
<div class="csn-card">
<p class="csn-tag">Magazin casino</p>
<h3 class="csn-h3">Ghiseul de langa casierita</h3>
<p>La ghiseu apesi <kbd>E</kbd> pe <b>Magazin casino</b>. Aici schimbi jetoanele pe bani (si invers), in pachete fixe, si cumperi <b>Zaruri</b> pentru barbut.</p>
</div>
<div class="csn-card">
<p class="csn-tag">Casino Chips</p>
<h3 class="csn-h3">De unde ai jetoane</h3>
<p>Jetoanele sunt unul din premiile de la roata norocului. Nu joci cu ele la niciun aparat: le duci la ghiseu si le schimbi pe bani.</p>
</div>
</div>

<h2 id="jocuri" class="csn-h2">Jocurile</h2>
<div class="csn-games">

<article class="csn-game gold" aria-labelledby="csn-g-roata">
<div class="csn-game-head">
<svg viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="24" r="21" fill="#1f1f23" stroke="#f5b931" stroke-width="2.5"/><path d="M24 24 L24 3 A21 21 0 0 1 42.2 13.5 Z" fill="#b91c1c"/><path d="M24 24 L42.2 34.5 A21 21 0 0 1 24 45 Z" fill="#b91c1c"/><path d="M24 24 L5.8 34.5 A21 21 0 0 1 5.8 13.5 Z" fill="#b91c1c"/><circle cx="24" cy="24" r="5" fill="#f5b931"/></svg>
<h3 id="csn-g-roata" class="csn-h3">Roata norocului</h3>
<span class="csn-where-pill">langa podiumul cu masina</span>
</div>
<p>Marea atractie a casino-ului. Pe podiumul de langa roata se invarte masina pe care o poti castiga: <b>Truffade Apex</b>.</p>
<div class="csn-cols">
<div>
<p class="csn-mini">Cum joci</p>
<ol class="csn-steps">
<li>Mergi la roata. Bula iti arata pretul unei invartiri.</li>
<li>Apasi <kbd>E</kbd>. Platesti si personajul trage de roata.</li>
<li>Roata se opreste pe una din cele 20 de felii si primesti premiul pe loc.</li>
</ol>
</div>
<div>
<p class="csn-mini">Bine de stiut</p>
<ul class="csn-facts">
<li>Roata o invarte un singur jucator odata. Cat timp se misca, ceilalti asteapta.</li>
<li>Masina castigata intra pe numele tau si primesti cheia ei.</li>
<li>Banii castigati intra in banca. Obiectele ajung in inventar.</li>
</ul>
</div>
</div>
<p class="csn-mini csn-gap">Premii pe roata</p>
<ul class="csn-prizes">
<li class="top">Truffade Apex</li>
<li>Bani</li>
<li>Casino Chips</li>
<li>SNS Pistol</li>
<li>SmartWatch (GPS)</li>
<li>Drona</li>
<li>EliteBox</li>
<li>Lockpick avansat</li>
<li>Whiskey</li>
</ul>
</article>

<article class="csn-game" aria-labelledby="csn-g-pacanele">
<div class="csn-game-head">
<svg viewBox="0 0 48 48" aria-hidden="true"><rect x="5" y="6" width="38" height="36" rx="6" fill="#1f1f23" stroke="#ef4444" stroke-width="2.5"/><rect x="10" y="15" width="28" height="16" rx="2" fill="#f6f1e7"/><text x="15" y="28" font-size="12" font-weight="900" fill="#dc2626" font-family="Inter, sans-serif">777</text><rect x="16" y="34" width="16" height="4" rx="2" fill="#ef4444"/></svg>
<h3 id="csn-g-pacanele" class="csn-h3">Pacanele</h3>
<span class="csn-where-pill">35 de aparate in sala</span>
</div>
<p>Joc clasic cu 3 role si o singura linie. Te asezi la orice aparat cu bula <b>Joaca la pacanele</b>.</p>
<div class="csn-cols">
<div>
<p class="csn-mini">Cum joci</p>
<ol class="csn-steps">
<li>Apasi <kbd>E</kbd> langa aparat si se deschide ecranul de joc.</li>
<li>Alegi miza, intre minimul si maximul afisate, in pasii pe care ii accepta aparatul.</li>
<li>Apesi <kbd>SPACE</kbd> sau butonul de invartire. <kbd>ESC</kbd> inchide aparatul.</li>
</ol>
</div>
<div>
<p class="csn-mini">Cum castigi</p>
<ul class="csn-facts">
<li><b>3 simboluri la fel</b>: castigul mare al simbolului.</li>
<li><b>2 simboluri la fel</b>: un castig mai mic.</li>
<li>Castigul creste odata cu miza si intra in banii cash.</li>
<li>Castigurile mari apar in chat, pentru tot serverul.</li>
</ul>
</div>
</div>
<p class="csn-mini csn-gap">Simboluri</p>
<ul class="csn-symbols">
<li>Cirese</li><li>Lamaie</li><li>Portocala</li><li>Pruna</li><li>Clopot</li><li>Bani</li><li>Diamant</li><li>Sapte</li>
</ul>
<ul class="csn-facts csn-gap">
<li><b>Auto Spin</b>: alegi 5, 10, 25, 50 sau 100 de rotiri si aparatul joaca singur, cu aceeasi miza. Il opresti oricand.</li>
<li>Intre doua rotiri ai o pauza scurta, cat se invart rolele.</li>
<li>Daca inchizi aparatul cat se invart rolele, castigul tot il primesti.</li>
<li>Tasta de invartire o poti schimba din setarile jocului: <b>Roteste pacanelele</b>.</li>
</ul>
</article>

<article class="csn-game green" aria-labelledby="csn-g-coinflip">
<div class="csn-game-head">
<svg viewBox="0 0 48 48" aria-hidden="true"><ellipse cx="24" cy="26" rx="19" ry="19" fill="#a16207"/><circle cx="24" cy="23" r="19" fill="#f5b931" stroke="#a16207" stroke-width="2"/><circle cx="24" cy="23" r="13" fill="none" stroke="#a16207" stroke-width="1.5"/><text x="24" y="28" text-anchor="middle" font-size="13" font-weight="900" fill="#713f12" font-family="Inter, sans-serif">C</text></svg>
<h3 id="csn-g-coinflip" class="csn-h3">Coinflip</h3>
<span class="csn-where-pill">3 mese cu marcaj rosu</span>
</div>
<p>Cap sau pajura: alegi o fata a monedei si o arunci. Daca pica pe fata ta, castigi.</p>
<div class="csn-cols">
<div>
<p class="csn-mini">Cum joci</p>
<ol class="csn-steps">
<li>Mergi la o masa cu bula <b>Joaca Coinflip</b> si apasi <kbd>E</kbd>.</li>
<li>Alegi miza, intre minimul si maximul afisate in meniu.</li>
<li>Alegi <b>Cap</b> sau <b>Pajura</b> si astepti sa cada moneda. <kbd>ESC</kbd> inchide meniul.</li>
</ol>
</div>
<div>
<p class="csn-mini">Bine de stiut</p>
<ul class="csn-facts">
<li>Daca ghicesti, primesti miza inapoi plus castigul, din care casa opreste un comision.</li>
<li>Castigul intra in banii cash.</li>
<li>Intre doua aruncari astepti cateva secunde. Meniul iti arata cat mai ai.</li>
<li>Panoul <b>Statistici</b> tine socoteala sesiunii: total mize, castiguri, pierderi, profit net si rata de castig.</li>
</ul>
</div>
</div>
</article>

<article class="csn-game" aria-labelledby="csn-g-barbut">
<div class="csn-game-head">
<svg viewBox="0 0 48 48" aria-hidden="true"><rect x="4" y="12" width="24" height="24" rx="5" fill="#fafafa" transform="rotate(-10 16 24)"/><circle cx="11" cy="20" r="2.4" fill="#18181b"/><circle cx="20" cy="28" r="2.4" fill="#18181b"/><circle cx="15.5" cy="24" r="2.4" fill="#18181b"/><rect x="22" y="16" width="22" height="22" rx="5" fill="#fafafa" stroke="#ef4444" stroke-width="2"/><circle cx="33" cy="27" r="3" fill="#dc2626"/></svg>
<h3 id="csn-g-barbut" class="csn-h3">Barbut (zaruri)</h3>
<span class="csn-where-pill">jucator contra jucator</span>
</div>
<p>Joci cu un alt jucator, pe bani cash. Ai nevoie de <b>Zaruri</b> din inventar, le cumperi de la Magazin casino. Barbutul merge oriunde in oras, nu doar in casino.</p>
<div class="csn-cols">
<div>
<p class="csn-mini">Cum joci</p>
<ol class="csn-steps">
<li>Stai langa jucatorul cu care vrei sa joci, la cel mult 5 metri.</li>
<li>Folosesti <b>Zaruri</b> din inventar si scrii suma pusa in joc.</li>
<li>Celalalt primeste <b>Cerere barbut</b> cu suma si accepta sau refuza.</li>
<li>Fiecare arunca doua zaruri. Zarurile aruncate apar langa voi.</li>
</ol>
</div>
<div>
<p class="csn-mini">Cine castiga</p>
<ul class="csn-facts">
<li>Suma mai mare a zarurilor ia ambele mize.</li>
<li>La egalitate, fiecare isi primeste miza inapoi.</li>
<li>Amandoi trebuie sa aveti suma in cash. Banca nu conteaza.</li>
<li>Nu merge daca unul din voi e incatusat sau daca celalalt e mort ori in masina.</li>
<li>Zarurile nu se consuma, le poti folosi de cate ori vrei.</li>
</ul>
</div>
</div>
</article>

</div>

<p class="csn-note"><b>Mesele cu dealer</b> din sala (ruleta, blackjack, poker) sunt doar decor momentan: nu poti juca la ele.</p>

</div>
