---
outline: false
---

<style>
.egs {
  --ink: #0c0c0e;
  --panel: #18181b;
  --panel2: #202024;
  --line: #34343b;
  --text: #f4f4f5;
  --mute: #a1a1aa;
  --red: #cc2b2b;
  --red-deep: #b91c1c;
  --red-soft: rgba(204, 43, 43, 0.14);
  --coin: #f5b931;
  --silver: #c4c7cc;
  --gold: #f2cf3c;
  --plat: #4fe3e0;
  max-width: 960px;
  margin: 0 auto;
  color: var(--text);
  font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.egs *, .egs *::before, .egs *::after { box-sizing: border-box; }
.egs p, .egs li { line-height: 1.6; color: var(--text); margin: 0; }
.egs ul, .egs ol { list-style: none; padding: 0; margin: 0; }
.egs li + li { margin-top: 0; }
.egs b { color: #fff; font-weight: 650; }
.egs code { white-space: nowrap; }
.egs a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.egs a:hover { color: #ffb4b4; }
.egs a:focus-visible { outline: 3px solid var(--red); outline-offset: 3px; border-radius: 6px; }
.egs kbd {
  font: inherit; font-size: 0.85em; font-weight: 700; color: #fff; background: var(--red-deep);
  border-radius: 6px; padding: 0.05rem 0.45rem;
}
/* hero: black velvet, champagne gold, slowly turning EG Coin */
.egs-hero {
  --cs: 150px;
  position: relative;
  display: grid; grid-template-columns: minmax(0, 1fr) auto; grid-template-areas: "head art" "body art";
  align-items: center; gap: 0.4rem 1.5rem;
  background:
    radial-gradient(40% 62% at 82% 44%, rgba(226, 176, 72, 0.17), rgba(226, 176, 72, 0) 72%),
    radial-gradient(70% 90% at 0% 110%, rgba(185, 28, 28, 0.2), rgba(185, 28, 28, 0) 62%),
    radial-gradient(130% 110% at 50% 0%, #16130f, #0a0908 55%, #050404);
  border: 1px solid rgba(214, 178, 104, 0.24);
  border-radius: 22px;
  box-shadow: inset 0 0 90px rgba(0, 0, 0, 0.65), inset 0 1px 0 rgba(255, 232, 178, 0.08);
  padding: clamp(1.4rem, 4vw, 2.6rem);
  overflow: hidden;
}
.egs-bg { position: absolute; inset: 0; z-index: 0; pointer-events: none; overflow: hidden; }
.egs-shine {
  position: absolute; top: -60%; left: -45%; width: 38%; height: 220%; opacity: 0;
  background: linear-gradient(90deg, rgba(255, 228, 165, 0), rgba(255, 228, 165, 0.05) 35%, rgba(255, 240, 210, 0.1) 50%, rgba(255, 228, 165, 0.05) 65%, rgba(255, 228, 165, 0));
  transform: rotate(20deg) translateX(0);
  animation: egs-shine 12s cubic-bezier(0.45, 0, 0.35, 1) 1.6s infinite;
}
.egs-dust i {
  position: absolute; bottom: -6px; left: var(--x); width: var(--s, 3px); height: var(--s, 3px); border-radius: 50%;
  background: radial-gradient(circle, #fff6d6 0%, rgba(240, 200, 105, 0.95) 40%, rgba(240, 200, 105, 0) 72%);
  opacity: 0;
  animation: egs-rise var(--d, 12s) linear var(--l, 0s) infinite;
}
.egs-frame {
  position: absolute; top: 9px; left: 9px; width: calc(100% - 18px); height: calc(100% - 18px);
  z-index: 1; overflow: visible; pointer-events: none;
}
.egs-frame rect {
  fill: none; stroke-width: 1; stroke-dasharray: 3200; stroke-dashoffset: 0;
  animation: egs-draw 3s cubic-bezier(0.65, 0, 0.25, 1) 0.25s both;
}
.egs-head, .egs-body { position: relative; z-index: 2; min-width: 0; }
.egs-head { grid-area: head; }
.egs-body { grid-area: body; }
.egs .egs-kicker {
  font-size: 0.78rem; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: var(--red);
  margin-bottom: 0.6rem;
}
.egs-hero h1 {
  margin: 0 0 0.8rem; border: 0; padding: 0;
  font-size: clamp(2rem, 6vw, 3.3rem); line-height: 1.05; font-weight: 800; letter-spacing: -0.03em; color: #fff;
}
.egs-hero h1 span {
  color: var(--coin); white-space: nowrap;
  background: linear-gradient(180deg, #fff4d0 0%, #f1cd6f 48%, #c08a2b 100%);
  -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent;
}
.egs .egs-lede { max-width: 56ch; color: #bdb6a8; font-size: 1.05rem; }
.egs .egs-cta { display: flex; flex-wrap: wrap; gap: 0.6rem; margin-top: 1.4rem; }
.egs .egs-cta a {
  display: inline-flex; align-items: center; gap: 0.4rem; text-decoration: none;
  border-radius: 999px; padding: 0.55rem 1.1rem; font-weight: 700; color: #fff;
  border: 1px solid rgba(214, 178, 104, 0.32); background: rgba(255, 255, 255, 0.04);
}
.egs .egs-cta a.main { background: var(--red-deep); border-color: var(--red-deep); }
.egs .egs-cta a:hover { border-color: #e8c77a; color: #fff; }
/* hero art: the coin */
.egs-art { grid-area: art; position: relative; z-index: 2; padding: 0 calc(var(--cs) * 0.16) 0 0.5rem; }
.egs-stage { position: relative; width: var(--cs); height: var(--cs); margin: calc(var(--cs) * 0.16) 0 calc(var(--cs) * 0.22); }
.egs-halo {
  position: absolute; top: -30%; left: -30%; width: 160%; height: 160%; border-radius: 50%;
  background: radial-gradient(circle, rgba(240, 196, 96, 0.22) 0%, rgba(240, 196, 96, 0.07) 38%, rgba(240, 196, 96, 0) 64%);
  animation: egs-breathe 7s ease-in-out infinite;
}
.egs-orbit { position: absolute; top: -12%; left: -12%; width: 124%; height: 124%; overflow: visible; animation: egs-turn 120s linear infinite; }
.egs-orbit circle { fill: none; stroke: #e8c77a; }
.egs-orbit .tick { stroke-width: 0.9; stroke-dasharray: 0.35 2.1; stroke-opacity: 0.45; }
.egs-orbit .line { stroke-width: 0.25; stroke-opacity: 0.22; }
.egs-floor {
  position: absolute; left: 14%; width: 72%; bottom: -16%; height: 12%; border-radius: 50%;
  background: radial-gradient(ellipse at center, rgba(0, 0, 0, 0.75) 0%, rgba(0, 0, 0, 0) 70%);
  animation: egs-shadow 6s ease-in-out infinite;
}
.egs-float { position: absolute; inset: 0; perspective: 900px; animation: egs-bob 6s ease-in-out infinite; }
.egs-coin {
  position: relative; width: 100%; height: 100%;
  transform-style: preserve-3d; transform: rotateY(-16deg);
  animation: egs-spin 15s infinite;
}
.egs-edge {
  position: absolute; inset: 0; border-radius: 50%;
  background: linear-gradient(180deg, #f2d27f 0%, #b07c22 45%, #5c3d0c 100%);
  transform: translateZ(var(--z));
}
.egs-face {
  position: absolute; inset: 0; border-radius: 50%; overflow: hidden;
  -webkit-backface-visibility: hidden; backface-visibility: hidden;
  transform: translateZ(4px);
}
.egs-face.back { transform: rotateY(180deg) translateZ(4px); }
.egs-face svg { display: block; width: 100%; height: 100%; }
.egs-glint {
  position: absolute; top: -10%; left: 0; width: 36%; height: 120%; opacity: 0;
  background: linear-gradient(90deg, rgba(255, 250, 232, 0), rgba(255, 250, 232, 0.6) 50%, rgba(255, 250, 232, 0));
  transform: translateX(-140%) skewX(-18deg);
  animation: egs-glint 15s ease-in-out infinite;
}
/* hero: VIP marks */
.egs-vip {
  display: flex; flex-wrap: wrap; align-items: center; gap: 0.6rem 1rem;
  margin-top: 1.5rem; padding-top: 1.1rem; border-top: 1px solid rgba(214, 178, 104, 0.16);
}
.egs .egs-cap {
  font-size: 0.66rem; font-weight: 700; letter-spacing: 0.32em; text-transform: uppercase; color: #8f8573;
  animation: egs-in 0.9s ease-out 1.1s both;
}
.egs-chips { display: flex; flex-wrap: wrap; gap: 0.45rem; }
.egs-chip {
  --c1: #f4f5f7; --c2: #9aa0a8; --rim: rgba(196, 199, 204, 0.42);
  display: inline-flex; align-items: center; gap: 0.45rem;
  padding: 0.34rem 0.75rem 0.34rem 0.6rem; border-radius: 999px;
  background: linear-gradient(180deg, #1a1712, #0b0a08);
  border: 1px solid var(--rim);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.07), inset 0 -1px 0 rgba(0, 0, 0, 0.7), 0 2px 8px rgba(0, 0, 0, 0.45);
  font-size: 0.68rem; font-weight: 750; letter-spacing: 0.2em; text-transform: uppercase; line-height: 1.2;
  animation: egs-in 0.9s cubic-bezier(0.2, 0.7, 0.2, 1) 1.3s both;
}
.egs .egs-chip b {
  font-weight: 750; color: var(--c1);
  background: linear-gradient(180deg, var(--c1), var(--c2));
  -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent;
}
.egs-chip i {
  width: 6px; height: 6px; flex: none; transform: rotate(45deg);
  background: linear-gradient(135deg, var(--c1), var(--c2));
  box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.6);
}
.egs-chip.gold { --c1: #fff0bf; --c2: #d4a03a; --rim: rgba(232, 190, 90, 0.5); animation-delay: 1.5s; }
.egs-chip.plat { --c1: #effcfc; --c2: #7fd8d6; --rim: rgba(127, 216, 214, 0.45); animation-delay: 1.7s; }
@keyframes egs-draw { from { stroke-dashoffset: 3200; } to { stroke-dashoffset: 0; } }
@keyframes egs-in { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }
@keyframes egs-turn { to { transform: rotate(360deg); } }
@keyframes egs-breathe { 0%, 100% { opacity: 0.75; } 50% { opacity: 1; } }
@keyframes egs-bob { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-7px); } }
@keyframes egs-shadow { 0%, 100% { transform: scale(1); opacity: 1; } 50% { transform: scale(0.88); opacity: 0.75; } }
@keyframes egs-spin {
  0% { transform: rotateY(-22deg); animation-timing-function: cubic-bezier(0.45, 0, 0.55, 1); }
  48% { transform: rotateY(22deg); animation-timing-function: cubic-bezier(0.55, 0, 0.3, 1); }
  100% { transform: rotateY(338deg); }
}
@keyframes egs-glint {
  0%, 8% { transform: translateX(-140%) skewX(-18deg); opacity: 0; }
  13% { opacity: 1; }
  32%, 100% { transform: translateX(330%) skewX(-18deg); opacity: 0; }
}
@keyframes egs-shine {
  0% { transform: rotate(20deg) translateX(0); opacity: 0; }
  8% { opacity: 1; }
  46% { opacity: 1; }
  55%, 100% { transform: rotate(20deg) translateX(520%); opacity: 0; }
}
@keyframes egs-rise {
  0% { transform: translate3d(0, 0, 0) scale(0.6); opacity: 0; }
  18% { opacity: var(--o, 0.8); }
  75% { opacity: var(--o, 0.8); }
  100% { transform: translate3d(var(--dx, 0px), -320px, 0) scale(1); opacity: 0; }
}
@media (max-width: 640px) {
  .egs-hero {
    --cs: 124px;
    grid-template-columns: minmax(0, 1fr); grid-template-areas: "art" "head" "body"; gap: 0.5rem;
    background:
      radial-gradient(70% 34% at 50% 20%, rgba(226, 176, 72, 0.17), rgba(226, 176, 72, 0) 72%),
      radial-gradient(90% 60% at 0% 110%, rgba(185, 28, 28, 0.2), rgba(185, 28, 28, 0) 62%),
      radial-gradient(130% 110% at 50% 0%, #16130f, #0a0908 55%, #050404);
  }
  .egs-art { justify-self: center; padding: 0; }
  .egs-frame { top: 7px; left: 7px; width: calc(100% - 14px); height: calc(100% - 14px); }
  .egs-chip { font-size: 0.62rem; letter-spacing: 0.16em; padding: 0.3rem 0.6rem 0.3rem 0.5rem; }
}
@media (prefers-reduced-motion: reduce) {
  .egs-hero *, .egs-hero *::before, .egs-hero *::after { animation: none !important; }
  .egs-shine, .egs-dust { display: none; }
}
/* section titles */
.egs h2 {
  margin: 3rem 0 1rem; border: 0; padding: 0;
  font-size: 1.5rem; font-weight: 750; letter-spacing: -0.015em; color: #fff;
}
.egs h2::before {
  content: ''; display: inline-block; width: 0.55rem; height: 0.55rem; margin-right: 0.6rem;
  border-radius: 2px; background: var(--red); vertical-align: middle; transform: translateY(-2px) rotate(45deg);
}
.egs .egs-sub { color: var(--mute); margin: -0.4rem 0 1rem; }
/* ways to open the shop */
.egs .egs-open { display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 0.75rem; }
.egs .egs-open li { background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 1rem 1.1rem; }
.egs .egs-open b { display: block; margin-bottom: 0.25rem; }
.egs .egs-open span { color: var(--mute); font-size: 0.93rem; }
/* what coins buy */
.egs .egs-buy { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 0.75rem; }
.egs .egs-buy li {
  background: var(--panel2); border: 1px solid var(--line); border-left: 3px solid var(--coin);
  border-radius: 12px; padding: 0.85rem 1rem;
}
.egs .egs-buy b { display: block; }
.egs .egs-buy span { color: var(--mute); font-size: 0.92rem; }
/* earn coins */
.egs .egs-earn { counter-reset: egs; display: grid; gap: 0.75rem; }
.egs .egs-earn li {
  counter-increment: egs; position: relative; background: var(--panel); border: 1px solid var(--line);
  border-radius: 14px; padding: 1rem 1.1rem 1rem 3.6rem;
}
.egs .egs-earn li::before {
  content: counter(egs); position: absolute; left: 1rem; top: 1rem; display: grid; place-items: center;
  width: 1.9rem; height: 1.9rem; border-radius: 50%; background: var(--coin); color: var(--ink); font-weight: 800;
}
.egs .egs-earn p { color: var(--mute); }
.egs .egs-earn b { color: #fff; }
/* VIP tiers */
.egs .egs-tiers { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; align-items: stretch; }
.egs .egs-tier {
  --tier: var(--silver);
  display: flex; flex-direction: column;
  --tier-soft: rgba(196, 199, 204, 0.12);
  background: linear-gradient(180deg, var(--tier-soft), var(--panel) 40%);
  border: 1px solid var(--line); border-top: 3px solid var(--tier); border-radius: 18px; padding: 1.25rem 1.3rem;
}
.egs .egs-tier.gold { --tier: var(--gold); --tier-soft: rgba(242, 207, 60, 0.12); }
.egs .egs-tier.plat { --tier: var(--plat); --tier-soft: rgba(79, 227, 224, 0.12); border-color: rgba(79, 227, 224, 0.45); }
.egs .egs-tier h3 { margin: 0; border: 0; padding: 0; font-size: 1.35rem; font-weight: 800; color: #fff; }
.egs .egs-tier h3 span { color: var(--tier); }
.egs .egs-perks { margin-top: 0.9rem; }
.egs .egs-perks li {
  display: flex; justify-content: space-between; gap: 0.75rem; padding: 0.5rem 0;
  border-top: 1px solid var(--line); font-size: 0.95rem;
}
.egs .egs-perks li span:first-child { color: var(--mute); }
.egs .egs-perks li span:last-child { color: #fff; font-weight: 650; text-align: right; white-space: nowrap; }
.egs .egs-cars-h { margin-top: 1rem; font-size: 0.78rem; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: var(--tier); }
.egs .egs-cars { margin-top: 0.4rem; }
.egs .egs-cars li { font-size: 0.95rem; padding: 0.15rem 0; }
.egs .egs-cars li.inc { color: var(--mute); font-style: italic; }
.egs .egs-cars small { color: var(--mute); }
.egs .egs-common { margin-top: 1rem; display: flex; flex-wrap: wrap; gap: 0.5rem; }
.egs .egs-common li {
  background: var(--panel2); border: 1px solid var(--line); border-radius: 1.1rem; padding: 0.3rem 0.85rem; font-size: 0.9rem; /* pill on one line, rounded box when it wraps */
}
/* screenshot */
.egs .egs-shot { margin: 1.25rem 0 0; background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 0.5rem; }
.egs .egs-shot img { display: block; width: 100%; height: auto; border-radius: 11px; margin: 0; }
.egs .egs-shot figcaption { color: var(--mute); font-size: 0.9rem; padding: 0.6rem 0.4rem 0.2rem; }
/* sanctions */
.egs .egs-warn {
  background: var(--red-soft); border: 1px solid rgba(204, 43, 43, 0.5); border-radius: 16px; padding: 1.1rem 1.25rem;
}
.egs .egs-warn p + p { margin-top: 0.6rem; }
.egs .egs-steps { margin-top: 0.9rem; display: grid; gap: 0.5rem; }
.egs .egs-steps li { padding-left: 1.4rem; position: relative; }
.egs .egs-steps li::before { content: ''; position: absolute; left: 0.2rem; top: 0.65em; width: 0.45rem; height: 0.45rem; border-radius: 50%; background: var(--red); }
.egs .egs-sub.egs-after { margin: 1rem 0 0; }
.egs .egs-warn .egs-gap { margin-top: 0.9rem; }
.egs .egs-foot { margin-top: 2.5rem; color: var(--mute); text-align: center; }
</style>

<div class="egs">
<section class="egs-hero">
<div class="egs-bg" aria-hidden="true"><span class="egs-shine"></span><span class="egs-dust"><i style="--x:58%;--d:13s;--l:-2s;--dx:-12px;--s:3px;--o:0.8"></i><i style="--x:66%;--d:11s;--l:-7s;--dx:10px;--s:2px;--o:0.7"></i><i style="--x:72%;--d:15s;--l:-4s;--dx:-6px;--s:3px;--o:0.9"></i><i style="--x:80%;--d:12s;--l:-10s;--dx:14px;--s:2px;--o:0.6"></i><i style="--x:86%;--d:14s;--l:-1s;--dx:-10px;--s:3px;--o:0.75"></i><i style="--x:91%;--d:10s;--l:-6s;--dx:6px;--s:2px;--o:0.6"></i><i style="--x:63%;--d:16s;--l:-12s;--dx:8px;--s:2px;--o:0.5"></i><i style="--x:76%;--d:13s;--l:-8s;--dx:-16px;--s:2px;--o:0.7"></i><i style="--x:14%;--d:17s;--l:-5s;--dx:10px;--s:2px;--o:0.35"></i><i style="--x:30%;--d:19s;--l:-13s;--dx:-8px;--s:2px;--o:0.3"></i><i style="--x:44%;--d:18s;--l:-9s;--dx:6px;--s:2px;--o:0.35"></i><i style="--x:95%;--d:15s;--l:-3s;--dx:-8px;--s:2px;--o:0.5"></i></span></div>
<svg class="egs-frame" aria-hidden="true" focusable="false"><defs><linearGradient id="egs-fg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f3d58c" stop-opacity="0.8"/><stop offset="0.5" stop-color="#a47b35" stop-opacity="0.22"/><stop offset="1" stop-color="#f3d58c" stop-opacity="0.65"/></linearGradient></defs><rect width="100%" height="100%" rx="14" ry="14" stroke="url(#egs-fg)"/></svg>
<div class="egs-head">
<p class="egs-kicker">Zona info</p>
<h1>Magazin si <span>EG Coins</span></h1>
</div>
<div class="egs-body">
<p class="egs-lede">EG Coins este moneda premium a serverului. Cu ea iei VIP, masini premium, bani in joc si alte pachete. Multumim ca sustii comunitatea EliteGamers!</p>
<div class="egs-cta">
<a class="main" href="https://elitegamers.tebex.io" target="_blank" rel="noopener">Magazin online (Tebex)</a>
<a href="https://discord.gg/elitegamers" target="_blank" rel="noopener">Intrebari pe Discord</a>
</div>
<div class="egs-vip" aria-hidden="true"><p class="egs-cap">Niveluri VIP</p><div class="egs-chips"><span class="egs-chip"><i></i><b>Silver</b></span><span class="egs-chip gold"><i></i><b>Gold</b></span><span class="egs-chip plat"><i></i><b>Platinum</b></span></div></div>
</div>
<div class="egs-art" aria-hidden="true">
<div class="egs-stage">
<span class="egs-halo"></span>
<svg class="egs-orbit" viewBox="0 0 100 100" focusable="false"><circle class="tick" cx="50" cy="50" r="48"/><circle class="line" cx="50" cy="50" r="45.5"/></svg>
<span class="egs-floor"></span>
<div class="egs-float"><div class="egs-coin"><span class="egs-edge" style="--z:-3.5px"></span><span class="egs-edge" style="--z:-2.5px"></span><span class="egs-edge" style="--z:-1.5px"></span><span class="egs-edge" style="--z:-0.5px"></span><span class="egs-edge" style="--z:0.5px"></span><span class="egs-edge" style="--z:1.5px"></span><span class="egs-edge" style="--z:2.5px"></span><span class="egs-edge" style="--z:3.5px"></span><div class="egs-face front"><svg viewBox="0 0 200 200" focusable="false"><defs><linearGradient id="egs-cg1" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff4c8"/><stop offset="0.22" stop-color="#f0cc6a"/><stop offset="0.5" stop-color="#c38e2a"/><stop offset="0.72" stop-color="#f5da88"/><stop offset="1" stop-color="#8f6118"/></linearGradient><radialGradient id="egs-cg2" cx="0.38" cy="0.32" r="0.8"><stop offset="0" stop-color="#fbe8ad"/><stop offset="0.5" stop-color="#dcaa46"/><stop offset="1" stop-color="#9c6a1a"/></radialGradient><linearGradient id="egs-cg3" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff2c6"/><stop offset="0.55" stop-color="#e2b04c"/><stop offset="1" stop-color="#a87420"/></linearGradient><path id="egs-ring" d="M100 30 a70 70 0 1 1 -0.01 0"/><symbol id="egs-face" viewBox="0 0 200 200"><circle cx="100" cy="100" r="100" fill="url(#egs-cg1)"/><circle cx="100" cy="100" r="95" fill="none" stroke="#6e4810" stroke-opacity="0.55" stroke-width="6" stroke-dasharray="1.3 1.7"/><circle cx="100" cy="100" r="88" fill="url(#egs-cg2)" stroke="#fff1c0" stroke-opacity="0.6" stroke-width="1"/><circle cx="100" cy="100" r="80" fill="none" stroke="#6e4810" stroke-opacity="0.45" stroke-width="0.8"/><circle cx="100" cy="100" r="58" fill="none" stroke="#6e4810" stroke-opacity="0.35" stroke-width="0.6"/><text font-family="Georgia, 'Times New Roman', serif" font-size="8.5" letter-spacing="3.2" fill="#6e4810" fill-opacity="0.75"><textPath href="#egs-ring">ELITEGAMERS &#183; EG COINS &#183; ELITEGAMERS &#183; EG COINS &#183;</textPath></text><g font-family="Georgia, 'Times New Roman', serif" font-size="52" font-weight="700" text-anchor="middle"><text x="100" y="119.5" fill="#5a3a0a" fill-opacity="0.7">EG</text><text x="100" y="117" fill="#fff8e0" fill-opacity="0.75">EG</text><text x="100" y="118" fill="url(#egs-cg3)">EG</text></g><path d="M86 134 L100 130 L114 134 L100 138 Z" fill="#6e4810" fill-opacity="0.5"/></symbol></defs><use href="#egs-face"/></svg><span class="egs-glint"></span></div><div class="egs-face back"><svg viewBox="0 0 200 200" focusable="false"><use href="#egs-face"/></svg></div></div></div>
</div>
</div>
</section>
<h2>Unde cheltui EG Coins</h2>
<p class="egs-sub">Magazinul din joc se deschide in trei feluri:</p>
<ul class="egs-open">
<li><b>Tasta <kbd>K</kbd></b><span>Meniul radial, apoi <code>Magazin in joc</code></span></li>
<li><b>Tasta <kbd>ESC</kbd></b><span>Meniul de pauza, apoi <code>Magazin din joc</code></span></li>
<li><b>Comanda <code>/store</code></b><span>Scrisa in chat</span></li>
</ul>
<h2>Ce poti lua cu EG Coins</h2>
<ul class="egs-buy">
<li><b>VIP</b><span>Silver, Gold sau Platinum, pe 30 sau 90 de zile</span></li>
<li><b>Bani in joc</b><span>Pachete de bani, direct in banca</span></li>
<li><b>Ore jucate</b><span>Pachete de la 25 la 1000 de ore</span></li>
<li><b>Iteme premium</b><span>Jante premium, antilag, sistem audio, ghiozdan premium, licenta de operator drone</span></li>
<li><b>Sloturi de garaj</b><span>+1, +3, +5 sau +10 sloturi</span></li>
<li><b>Sala</b><span>Stamina si putere la maxim</span></li>
<li><b>Sanctiuni</b><span>Iesi din admin-jail sau stergi cel mai vechi avertisment</span></li>
<li><b>Masini premium</b><span>In dealership, la categoria premium</span></li>
<li><b>Case si skin-uri de arme</b><span>Case platite in EG Coins si <a href="/general/skin-uri-arme">skin-uri premium</a></span></li>
</ul>
<figure class="egs-shot">
<img src="../public/store/dealership.png" alt="Dealership-ul Premium Deluxe Motorsport din oras" loading="lazy">
<figcaption>Dealership-ul din oras (Premium Deluxe Motorsport): aici gasesti masinile premium si pe cele VIP.</figcaption>
</figure>
<h2>Cum obtii EG Coins</h2>
<ol class="egs-earn">
<li><p><b>Din magazinul online.</b> Cumperi de pe <a href="https://elitegamers.tebex.io" target="_blank" rel="noopener">elitegamers.tebex.io</a> si treci ID-ul tau din joc. Monedele intra automat in cont, chiar daca nu esti pe server in acel moment.</p></li>
<li><p><b>Din pachetul de inceput.</b> Un personaj nou primeste un EG Coin ca item. Il folosesti din inventar si intra in cont.</p></li>
</ol>
<h2>VIP</h2>
<p class="egs-sub">Trei niveluri. Un nivel mai mare are tot ce are cel de sub el, plus ceva in plus.</p>
<div class="egs-tiers">
<div class="egs-tier">
<h3>VIP <span>Silver</span></h3>
<ul class="egs-perks">
<li><span>Boost la joburi</span><span>+5%</span></li>
<li><span>Salariu VIP</span><span>2.000 € / ora</span></li>
<li><span>Bani la cumparare (30 zile)</span><span>75.000 €</span></li>
</ul>
<p class="egs-cars-h">Masini VIP</p>
<ul class="egs-cars">
<li>Ubermacht Oracle XS-LE</li>
<li>Ubermacht Sentinel 4CSL</li>
<li>Obey 9R</li>
</ul>
</div>
<div class="egs-tier gold">
<h3>VIP <span>Gold</span></h3>
<ul class="egs-perks">
<li><span>Boost la joburi</span><span>+10%</span></li>
<li><span>Salariu VIP</span><span>3.500 € / ora</span></li>
<li><span>Bani la cumparare (30 zile)</span><span>150.000 €</span></li>
</ul>
<p class="egs-cars-h">Masini VIP</p>
<ul class="egs-cars">
<li>Pegassi Reaper Custom</li>
<li>Grotti Turismo S</li>
<li>Gallivanter Baller ST-D Platinum</li>
<li>Pegassi Toros</li>
<li class="inc">+ toate masinile de la Silver</li>
</ul>
</div>
<div class="egs-tier plat">
<h3>VIP <span>Platinum</span></h3>
<ul class="egs-perks">
<li><span>Boost la joburi</span><span>+15%</span></li>
<li><span>Salariu VIP</span><span>5.000 € / ora</span></li>
<li><span>Bani la cumparare (30 zile)</span><span>250.000 €</span></li>
</ul>
<p class="egs-cars-h">Masini VIP</p>
<ul class="egs-cars">
<li>Invetero Coquette VR1</li>
<li>Benefactor Krieger</li>
<li>Pfister Comet GTS2</li>
<li>Annis Elegy RH8 FR-Works</li>
<li>Pegassi Severo Widebody</li>
<li>Pegassi Speeder <small>(barca)</small></li>
<li>Sparrow <small>(elicopter)</small></li>
<li class="inc">+ toate masinile de la Gold</li>
</ul>
</div>
</div>
<ul class="egs-common">
<li>Suport</li>
<li>Grad VIP pe Discord si in joc</li>
<li>Salariul VIP intra in banca, la fiecare ora</li>
<li>Pachetul de 90 de zile da mai multi bani la cumparare</li>
<li>Acelasi nivel cumparat din nou adauga zilele la cele ramase</li>
</ul>
<p class="egs-sub egs-after">Masinile VIP le iei gratis din dealership, cate una din fiecare model, cat timp ai VIP-ul. Barca o gasesti la dealership-ul de barci, elicopterul la cel de avioane. Daca VIP-ul expira, nu le mai poti scoate din garaj pana nu il reactivezi.</p>
<h2>Sanctiuni si unban</h2>
<div class="egs-warn">
<p>Ai primit ban temporar sau permanent si vrei sa platesti ridicarea lui? Pe Tebex gasesti <b>Unban temporar</b>, <b>Unban permanent</b> si <b>Clear warn</b>.</p>
<ul class="egs-steps">
<li><b>Inainte sa cumperi, deschide un ticket pe <a href="https://discord.gg/elitegamers" target="_blank" rel="noopener">Discord</a>.</b> Echipa iti spune daca sanctiunea ta se poate ridica.</li>
<li>Unban-ul nu se scoate automat, este nevoie sa deschizi un ticket inainte de a cumpara.</li>
<li>Unban-ul temporar ridica doar un ban temporar. Pentru un ban permanent iei Unban permanent.</li>
</ul>
<p class="egs-gap"><b>Atentie:</b> respectarea regulamentului FiveM e obligatorie. Daca primesti <b>ban fara drept de plata</b>, pachetele cumparate nu se mai pot folosi.</p>
</div>
<p class="egs-foot">Ai intrebari? Echipa te asteapta pe <a href="https://discord.gg/elitegamers" target="_blank" rel="noopener">Discord</a>.</p>
</div>
