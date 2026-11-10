---
outline: false
---

<style>
.tf {
  --ink: #050507;
  --line: rgba(255, 255, 255, 0.09);
  --line2: rgba(255, 255, 255, 0.16);
  --text: #f5f5f7;
  --mute: #a1a1aa;
  --dim: #71717a;
  --red: #ef4444;
  --red-deep: #b91c1c;
  max-width: 1040px;
  margin: 0 auto;
  color: var(--text);
  font-family: Inter, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.tf *, .tf *::before, .tf *::after { box-sizing: border-box; }
.tf p, .tf li { margin: 0; line-height: 1.6; color: var(--text); }
.tf ul, .tf ol { list-style: none; padding: 0; margin: 0; }
.tf li + li { margin-top: 0; }
.tf b { color: #fff; font-weight: 650; }
.tf a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.tf a:hover { color: #fecaca; }
.tf a:focus-visible { outline: 3px solid var(--red); outline-offset: 3px; border-radius: 6px; }
.tf kbd {
  font: inherit; font-size: 0.82em; font-weight: 700; color: #fff; white-space: nowrap;
  background: linear-gradient(180deg, #3f3f46, #27272a); border: 1px solid #52525b; border-bottom-width: 2px;
  border-radius: 7px; padding: 0.02rem 0.45rem;
}
.tf svg.tf-g { width: 100%; height: 100%; fill: none; stroke: currentColor; stroke-width: 1.9; stroke-linecap: round; stroke-linejoin: round; }
.tf .tf-defs { position: absolute; width: 0; height: 0; overflow: hidden; }
/* ---------- hero ---------- */
.tf .tf-hero {
  position: relative; overflow: hidden; isolation: isolate;
  display: grid; grid-template-columns: minmax(0, 1fr); justify-items: center; gap: 0.5rem; text-align: center;
  padding: clamp(1.4rem, 4.5vw, 3.2rem);
  border-radius: 30px; border: 1px solid var(--line);
  background:
    radial-gradient(60% 45% at 50% 72%, rgba(239, 68, 68, 0.24), transparent 70%),
    radial-gradient(50% 60% at 95% 100%, rgba(99, 102, 241, 0.16), transparent 70%),
    radial-gradient(70% 80% at 0% 0%, rgba(255, 255, 255, 0.05), transparent 60%),
    var(--ink);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.06), 0 30px 80px -40px rgba(0, 0, 0, 0.9);
}
.tf .tf-hero::after {
  content: ''; position: absolute; inset: 0; z-index: -1; pointer-events: none;
  background-image: radial-gradient(rgba(255, 255, 255, 0.07) 1px, transparent 1px);
  background-size: 26px 26px;
  -webkit-mask-image: radial-gradient(70% 60% at 50% 70%, #000, transparent 75%);
  mask-image: radial-gradient(70% 60% at 50% 70%, #000, transparent 75%);
}
.tf .tf-kicker {
  display: inline-flex; align-items: center; gap: 0.5rem;
  font-size: 0.78rem; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase; color: #fca5a5;
  margin-bottom: 1rem;
}
.tf .tf-kicker::before { content: ''; width: 8px; height: 8px; border-radius: 50%; background: var(--red); box-shadow: 0 0 0 4px rgba(239, 68, 68, 0.2); }
.tf .tf-hero h1 {
  margin: 0 0 1.1rem; border: 0; padding: 0;
  font-size: clamp(2.5rem, 5.4vw, 4.4rem); line-height: 0.98; font-weight: 800; letter-spacing: -0.045em; color: #fff;
}
.tf .tf-hero h1 span {
  display: block;
  background: linear-gradient(92deg, #fff 0%, #fecaca 35%, #ef4444 75%, #fb923c 100%);
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.tf .tf-lead { font-size: clamp(1.02rem, 2.2vw, 1.2rem); line-height: 1.55; color: #d4d4d8; max-width: 32rem; margin: 0 auto; }
.tf .tf-chips { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.5rem; margin-top: 1.5rem; }
.tf .tf-chips li {
  display: inline-flex; align-items: center; gap: 0.45rem;
  font-size: 0.86rem; font-weight: 600; color: #e4e4e7;
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.08), rgba(255, 255, 255, 0.025));
  border: 1px solid var(--line2); border-radius: 999px; padding: 0.35rem 0.85rem;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.08);
}
/* stage + phone */
.tf .tf-stage { position: relative; width: 100%; height: 520px; display: grid; place-items: center; margin-top: 0.5rem; }
.tf .tf-halo {
  position: absolute; width: 380px; height: 380px; border-radius: 50%;
  background: radial-gradient(circle, rgba(239, 68, 68, 0.35), rgba(239, 68, 68, 0) 65%);
  animation: tf-breathe 7s ease-in-out infinite;
}
.tf .tf-ring {
  position: absolute; width: 440px; height: 440px; border-radius: 50%;
  border: 1px dashed rgba(255, 255, 255, 0.08);
}
.tf .tf-orbit { position: absolute; width: 440px; height: 440px; animation: tf-spin 70s linear infinite; }
.tf .tf-ot { position: absolute; width: 52px; height: 52px; margin: -26px 0 0 -26px; }
.tf .tf-ot > div { width: 100%; height: 100%; animation: tf-spin 70s linear infinite reverse; }
.tf .tf-ot .tf-ico { width: 100%; height: 100%; padding: 13px; box-shadow: 0 14px 30px -10px rgba(0, 0, 0, 0.8); }
.tf .tf-ot:nth-child(1) { left: 50%; top: 0%; }
.tf .tf-ot:nth-child(2) { left: 93.3%; top: 25%; }
.tf .tf-ot:nth-child(3) { left: 93.3%; top: 75%; }
.tf .tf-ot:nth-child(4) { left: 50%; top: 100%; }
.tf .tf-ot:nth-child(5) { left: 6.7%; top: 75%; }
.tf .tf-ot:nth-child(6) { left: 6.7%; top: 25%; }
.tf .tf-phone {
  position: relative; width: 236px; height: 484px; border-radius: 46px; padding: 9px;
  background: linear-gradient(145deg, #d4d4d8 0%, #71717a 18%, #3f3f46 40%, #a1a1aa 62%, #52525b 82%, #e4e4e7 100%);
  box-shadow:
    0 0 0 1px rgba(0, 0, 0, 0.6),
    inset 0 0 0 1px rgba(255, 255, 255, 0.35),
    0 40px 80px -24px rgba(0, 0, 0, 0.95),
    0 0 60px -10px rgba(239, 68, 68, 0.35);
  animation: tf-hover 8s ease-in-out infinite;
}
.tf .tf-key { position: absolute; width: 4px; border-radius: 2px; background: linear-gradient(90deg, #52525b, #a1a1aa); }
.tf .tf-key.k1 { left: -3px; top: 96px; height: 26px; }
.tf .tf-key.k2 { left: -3px; top: 138px; height: 46px; }
.tf .tf-key.k3 { left: -3px; top: 194px; height: 46px; }
.tf .tf-key.k4 { right: -3px; top: 150px; height: 70px; }
.tf .tf-screen {
  position: relative; width: 100%; height: 100%; border-radius: 38px; overflow: hidden;
  background: #000; box-shadow: inset 0 0 0 2px #000;
}
.tf .tf-island {
  position: absolute; z-index: 5; top: 10px; left: 50%; width: 78px; height: 22px; margin-left: -39px;
  border-radius: 999px; background: #000; box-shadow: 0 0 0 1px rgba(255, 255, 255, 0.04);
}
.tf .tf-island::after { content: ''; position: absolute; right: 9px; top: 7px; width: 8px; height: 8px; border-radius: 50%; background: radial-gradient(circle at 35% 35%, #3b82f6, #0b1220 60%); }
.tf .tf-scr { position: absolute; inset: 0; opacity: 0; }
.tf .tf-scr.s1 { opacity: 1; }
.tf .tf-scr.s1 { animation: tf-show1 15s ease-in-out infinite; }
.tf .tf-scr.s2 { animation: tf-show2 15s ease-in-out infinite; }
.tf .tf-scr.s3 { animation: tf-show3 15s ease-in-out infinite; }
.tf .tf-glare {
  position: absolute; inset: -20% -60%; z-index: 6; pointer-events: none;
  background: linear-gradient(105deg, transparent 38%, rgba(255, 255, 255, 0.16) 48%, rgba(255, 255, 255, 0.04) 54%, transparent 62%);
  transform: translateX(-70%);
  animation: tf-glare 7.5s ease-in-out infinite;
}
/* lock screen */
.tf .tf-lock {
  background:
    radial-gradient(90% 60% at 50% 110%, rgba(239, 68, 68, 0.9), transparent 70%),
    radial-gradient(80% 50% at 0% 70%, rgba(124, 58, 237, 0.7), transparent 70%),
    linear-gradient(180deg, #0b0b12 0%, #1e1b4b 55%, #450a0a 100%);
  text-align: center; padding-top: 52px;
}
.tf .tf-lock .d { font-size: 0.78rem; font-weight: 600; color: rgba(255, 255, 255, 0.82); }
.tf .tf-lock .t { font-size: 4.1rem; line-height: 1; font-weight: 700; letter-spacing: -0.04em; color: #fff; margin-top: 0.1rem; }
.tf .tf-note {
  margin: 1.4rem 0.7rem 0; display: flex; gap: 0.55rem; align-items: center; text-align: left;
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.24), rgba(255, 255, 255, 0.13));
  border: 1px solid rgba(255, 255, 255, 0.18); border-radius: 18px; padding: 0.55rem 0.65rem;
}
.tf .tf-note + .tf-note { margin-top: 0.45rem; }
.tf .tf-note .tf-ico { width: 30px; height: 30px; border-radius: 8px; padding: 6px; flex: none; }
.tf .tf-note b { display: block; font-size: 0.72rem; line-height: 1.2; }
.tf .tf-note span { display: block; font-size: 0.7rem; line-height: 1.3; color: rgba(255, 255, 255, 0.85); }
.tf .tf-lockbar { position: absolute; left: 0; right: 0; bottom: 26px; display: flex; justify-content: space-between; padding: 0 1.4rem; }
.tf .tf-lockbar i { display: block; width: 38px; height: 38px; border-radius: 50%; background: rgba(0, 0, 0, 0.35); border: 1px solid rgba(255, 255, 255, 0.14); padding: 9px; color: #fff; }
.tf .tf-home-ind { position: absolute; left: 50%; bottom: 8px; width: 92px; height: 4px; margin-left: -46px; border-radius: 3px; background: rgba(255, 255, 255, 0.85); }
/* home screen */
.tf .tf-homes {
  background:
    radial-gradient(80% 50% at 100% 0%, rgba(239, 68, 68, 0.55), transparent 70%),
    radial-gradient(80% 60% at 0% 100%, rgba(14, 165, 233, 0.45), transparent 70%),
    linear-gradient(180deg, #111827, #0b0b12);
  padding: 46px 14px 0;
}
.tf .tf-grid4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 13px 11px; }
.tf .tf-grid4 .tf-ico { width: 100%; aspect-ratio: 1; padding: 10px; border-radius: 12px; }
.tf .tf-dock {
  position: absolute; left: 9px; right: 9px; bottom: 18px; display: grid; grid-template-columns: repeat(4, 1fr); gap: 11px;
  padding: 9px; border-radius: 24px; background: linear-gradient(180deg, rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.1));
  border: 1px solid rgba(255, 255, 255, 0.12);
}
.tf .tf-dock .tf-ico { width: 100%; aspect-ratio: 1; padding: 10px; border-radius: 12px; }
/* maps screen */
.tf .tf-maps { background: #0f172a; }
.tf .tf-maps svg { position: absolute; inset: 0; width: 100%; height: 100%; }
.tf .tf-pin { transform-box: fill-box; transform-origin: center; animation: tf-ping 2.2s ease-out infinite; }
.tf .tf-sheet {
  position: absolute; left: 8px; right: 8px; bottom: 18px; border-radius: 20px; padding: 0.7rem 0.8rem;
  background: linear-gradient(180deg, rgba(24, 24, 27, 0.96), rgba(9, 9, 11, 0.96)); border: 1px solid rgba(255, 255, 255, 0.1);
}
.tf .tf-sheet b { display: block; font-size: 0.8rem; }
.tf .tf-sheet span { display: block; font-size: 0.68rem; color: var(--mute); }
.tf .tf-sheet i { display: block; margin-top: 0.5rem; font-style: normal; text-align: center; font-size: 0.72rem; font-weight: 700; padding: 0.42rem; border-radius: 10px; background: #0a84ff; color: #fff; }
/* entrance */
.tf .tf-rise { animation: tf-rise 0.9s cubic-bezier(0.2, 0.7, 0.1, 1) both; }
.tf .tf-rise.r2 { animation-delay: 0.08s; }
.tf .tf-rise.r3 { animation-delay: 0.16s; }
.tf .tf-rise.r4 { animation-delay: 0.24s; }
.tf .tf-rise.r5 { animation-delay: 0.32s; }
@keyframes tf-rise { from { opacity: 0; transform: translateY(18px); } to { opacity: 1; transform: none; } }
@keyframes tf-spin { to { transform: rotate(360deg); } }
@keyframes tf-breathe { 0%, 100% { transform: scale(0.92); opacity: 0.75; } 50% { transform: scale(1.06); opacity: 1; } }
@keyframes tf-hover { 0%, 100% { transform: translateY(0) rotate(-1.5deg); } 50% { transform: translateY(-10px) rotate(-0.5deg); } }
@keyframes tf-glare { 0%, 35% { transform: translateX(-70%); } 75%, 100% { transform: translateX(70%); } }
@keyframes tf-show1 { 0%, 28% { opacity: 1; transform: none; } 34%, 94% { opacity: 0; transform: scale(1.04); } 100% { opacity: 1; transform: none; } }
@keyframes tf-show2 { 0%, 28% { opacity: 0; transform: scale(0.96); } 34%, 61% { opacity: 1; transform: none; } 67%, 100% { opacity: 0; transform: scale(1.04); } }
@keyframes tf-show3 { 0%, 61% { opacity: 0; transform: scale(0.96); } 67%, 94% { opacity: 1; transform: none; } 100% { opacity: 0; transform: scale(1.04); } }
@keyframes tf-ping { 0% { transform: scale(0.6); opacity: 0.9; } 100% { transform: scale(2.4); opacity: 0; } }
/* ---------- icon tiles ---------- */
.tf .tf-ico {
  display: block; position: relative; color: #fff; border-radius: 23%;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.35), inset 0 -1px 0 rgba(0, 0, 0, 0.25);
}
.tf .tf-ico::after {
  content: ''; position: absolute; inset: 0; border-radius: inherit; pointer-events: none;
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.22), rgba(255, 255, 255, 0) 48%);
}
.tf .c-green { background: linear-gradient(160deg, #6ee787, #22a046); }
.tf .c-blue { background: linear-gradient(160deg, #5ab0ff, #0a5fd8); }
.tf .c-sky { background: linear-gradient(160deg, #8be0ff, #2a9fd8); }
.tf .c-yellow { background: linear-gradient(160deg, #ffe27a, #e0a10e); color: #3b2a00; }
.tf .c-dark { background: linear-gradient(160deg, #3a3a40, #121214); }
.tf .c-white { background: linear-gradient(160deg, #ffffff, #d6d6dc); color: #1c1c1e; }
.tf .c-red { background: linear-gradient(160deg, #ff7a70, #e0241b); }
.tf .c-pink { background: linear-gradient(160deg, #ff7aa2, #e01e4f); }
.tf .c-gram { background: linear-gradient(45deg, #f9ce34 0%, #ee2a7b 50%, #6228d7 100%); }
.tf .c-violet { background: linear-gradient(160deg, #c084fc, #7c3aed); }
.tf .c-orange { background: linear-gradient(160deg, #ffb26b, #f2620f); }
.tf .c-teal { background: linear-gradient(160deg, #4fe0cf, #0f9488); }
.tf .c-emerald { background: linear-gradient(160deg, #5eead4, #059669); }
.tf .c-indigo { background: linear-gradient(160deg, #a5b4fc, #4f46e5); }
.tf .c-amber { background: linear-gradient(160deg, #fcd34d, #d97706); }
.tf .c-gold { background: linear-gradient(160deg, #fde68a, #eab308); color: #3b2a00; }
.tf .c-slate { background: linear-gradient(160deg, #64748b, #1e293b); }
.tf .c-gray { background: linear-gradient(160deg, #c7c7cc, #6e6e73); }
.tf .c-cyan { background: linear-gradient(160deg, #a5f3fc, #0891b2); }
.tf .c-cherry { background: linear-gradient(160deg, #ff8fae, #c8103e); }
/* ---------- stats strip ---------- */
.tf .tf-stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 140px), 1fr)); gap: 0.75rem; margin-top: 1rem; }
.tf .tf-stats li {
  padding: 1.1rem 1.2rem; border-radius: 22px; border: 1px solid var(--line);
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.06), rgba(255, 255, 255, 0.015)), #0b0b0e;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.06);
}
.tf .tf-stats b { display: block; font-size: clamp(1.7rem, 4vw, 2.3rem); line-height: 1; font-weight: 800; letter-spacing: -0.04em; color: #fff; }
.tf .tf-stats span { display: block; margin-top: 0.45rem; font-size: 0.85rem; line-height: 1.35; color: var(--mute); }
/* ---------- sections ---------- */
.tf .tf-sec { margin-top: clamp(3.2rem, 8vw, 5.2rem); }
.tf .tf-eyebrow { font-size: 0.78rem; font-weight: 700; letter-spacing: 0.16em; text-transform: uppercase; color: #fca5a5; margin-bottom: 0.5rem; }
.tf .tf-h2 {
  margin: 0 0 1.2rem; border: 0; padding: 0;
  font-size: clamp(1.9rem, 5vw, 2.9rem); line-height: 1.05; font-weight: 800; letter-spacing: -0.035em; color: #fff;
}
.tf .tf-h2 span { color: var(--dim); }
.tf .tf-sub { max-width: 40rem; font-size: 1.05rem; color: var(--mute); margin: -0.5rem 0 1.6rem; }
.tf .tf-card {
  position: relative; overflow: hidden; border-radius: 24px; border: 1px solid var(--line);
  padding: clamp(1.1rem, 3vw, 1.6rem);
  background:
    linear-gradient(180deg, rgba(255, 255, 255, 0.065), rgba(255, 255, 255, 0.015)),
    radial-gradient(120% 90% at 100% 0%, rgba(239, 68, 68, 0.08), transparent 60%),
    #0b0b0e;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.07), 0 20px 50px -30px rgba(0, 0, 0, 0.9);
}
.tf .tf-card h3 { margin: 0 0 0.45rem; border: 0; padding: 0; font-size: 1.15rem; font-weight: 750; letter-spacing: -0.015em; line-height: 1.3; color: #fff; }
.tf .tf-card p { color: #d4d4d8; font-size: 0.95rem; }
.tf .tf-card p + p { margin-top: 0.55rem; }
.tf .tf-card .tf-num {
  display: inline-grid; place-items: center; width: 34px; height: 34px; margin-bottom: 0.85rem; border-radius: 11px;
  font-weight: 800; font-size: 0.95rem; color: #fff; background: linear-gradient(160deg, #f87171, #b91c1c);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.3), 0 8px 20px -8px rgba(239, 68, 68, 0.7);
}
.tf .tf-steps { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr)); gap: 0.8rem; }
.tf .tf-two { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr)); gap: 0.8rem; }
.tf .tf-three { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 185px), 1fr)); gap: 0.8rem; }
/* ---------- app catalog ---------- */
.tf .tf-cat + .tf-cat { margin-top: 2rem; }
.tf .tf-cat-h { display: flex; align-items: baseline; gap: 0.7rem; margin-bottom: 0.85rem; padding-bottom: 0.55rem; border-bottom: 1px solid var(--line); }
.tf .tf-cat-h h3 { margin: 0; border: 0; padding: 0; font-size: 1.2rem; font-weight: 750; letter-spacing: -0.02em; color: #fff; }
.tf .tf-cat-h span { font-size: 0.85rem; color: var(--dim); }
.tf .tf-apps { display: grid; grid-template-columns: repeat(auto-fill, minmax(min(100%, 228px), 1fr)); gap: 0.7rem; }
.tf .tf-apps li {
  display: grid; grid-template-columns: 54px minmax(0, 1fr); gap: 0.85rem; align-items: start;
  padding: 0.85rem; border-radius: 20px; border: 1px solid var(--line);
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0.012)), #0a0a0d;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.05);
  transition: transform 0.25s ease, opacity 0.25s ease;
}
.tf .tf-apps li:hover { transform: translateY(-3px); }
.tf .tf-apps .tf-ico { width: 54px; height: 54px; padding: 13px; }
.tf .tf-apps b { display: flex; flex-direction: column; align-items: flex-start; gap: 0.25rem; font-size: 1rem; line-height: 1.3; letter-spacing: -0.01em; }
.tf .tf-apps p { margin-top: 0.2rem; font-size: 0.86rem; line-height: 1.45; color: var(--mute); }
.tf .tf-tag {
  font-size: 0.66rem; font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase;
  color: #93c5fd; background: rgba(59, 130, 246, 0.14); border: 1px solid rgba(59, 130, 246, 0.3);
  border-radius: 999px; padding: 0.05rem 0.45rem; white-space: nowrap;
}
/* ---------- lists in cards ---------- */
.tf .tf-list li { position: relative; padding-left: 1.15rem; color: #d4d4d8; font-size: 0.95rem; }
.tf .tf-list li + li { margin-top: 0.4rem; }
.tf .tf-list li::before { content: ''; position: absolute; left: 0; top: 0.62em; width: 6px; height: 6px; border-radius: 50%; background: var(--red); }
.tf .tf-keys { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr)); gap: 0.6rem; }
.tf .tf-keys li {
  display: grid; grid-template-columns: 5.2rem minmax(0, 1fr); align-items: center; gap: 0.8rem; padding: 0.75rem 0.9rem; border-radius: 16px;
  border: 1px solid var(--line); background: linear-gradient(180deg, rgba(255, 255, 255, 0.045), rgba(255, 255, 255, 0.01)), #0a0a0d;
  font-size: 0.92rem; color: #d4d4d8;
}
.tf .tf-keys kbd { justify-self: start; min-width: 2.2rem; text-align: center; }
/* accessories */
.tf .tf-acc { display: grid; grid-template-columns: 64px minmax(0, 1fr); gap: 1rem; align-items: start; }
.tf .tf-acc .tf-ico { width: 64px; height: 64px; padding: 15px; }
/* path */
.tf .tf-path { font-weight: 650; color: #fff; }
.tf .tf-note2 {
  margin-top: 1rem; padding: 0.85rem 1rem; border-radius: 16px; font-size: 0.92rem; color: #d4d4d8;
  border: 1px solid rgba(239, 68, 68, 0.3); background: linear-gradient(90deg, rgba(239, 68, 68, 0.12), rgba(239, 68, 68, 0.02));
}
/* ---------- responsive ---------- */
@media (max-width: 480px) {
  .tf .tf-hero { border-radius: 24px; padding: 1.4rem 1rem; }
  .tf .tf-stage { height: 470px; transform: scale(0.82); margin: -42px 0; }
  .tf .tf-orbit, .tf .tf-ring { width: 380px; height: 380px; }
  .tf .tf-halo { width: 320px; height: 320px; }
  .tf .tf-acc { grid-template-columns: minmax(0, 1fr); }
}
@media (prefers-reduced-motion: reduce) {
  .tf .tf-halo, .tf .tf-orbit, .tf .tf-ot > div, .tf .tf-phone, .tf .tf-glare, .tf .tf-scr,
  .tf .tf-pin, .tf .tf-rise { animation: none; }
  .tf .tf-glare { display: none; }
  .tf .tf-pin { opacity: 0; }
  .tf .tf-scr.s1 { opacity: 1; }
  .tf .tf-apps li { transition: none; }
  .tf .tf-apps li:hover { transform: none; }
}
</style>

<div class="tf">
<svg class="tf-defs" aria-hidden="true" focusable="false">
<symbol id="tf-phone" viewBox="0 0 24 24"><path d="M21.5 16.4v3a2 2 0 0 1-2.2 2 19.6 19.6 0 0 1-8.5-3 19.3 19.3 0 0 1-6-6A19.6 19.6 0 0 1 1.8 3.7 2 2 0 0 1 3.8 1.5h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.4 2.1L7.8 9.4a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.5 2z"/></symbol>
<symbol id="tf-msg" viewBox="0 0 24 24"><path d="M21 11.4c0 4.4-4 8-9 8-1.3 0-2.6-.2-3.7-.7L3 20.4l1.4-4.1A7.5 7.5 0 0 1 3 11.4c0-4.4 4-8 9-8s9 3.6 9 8z"/></symbol>
<symbol id="tf-mail" viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="m3.5 7 8.5 6 8.5-6"/></symbol>
<symbol id="tf-mask" viewBox="0 0 24 24"><path d="M5 21V10a7 7 0 0 1 14 0v11l-2.4-1.6L14.2 21 12 19.4 9.8 21l-2.4-1.6z"/><path d="M9.5 10h.01M14.5 10h.01"/></symbol>
<symbol id="tf-gram" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="5.5"/><circle cx="12" cy="12" r="4.2"/><path d="M17.4 6.6h.01"/></symbol>
<symbol id="tf-clout" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="16" rx="4.5"/><path d="m10 8.6 5.4 3.4-5.4 3.4z"/></symbol>
<symbol id="tf-cherry" viewBox="0 0 24 24"><circle cx="7.5" cy="16" r="4"/><circle cx="16.5" cy="17" r="3.5"/><path d="M7.5 12c.5-4 3.5-7.5 8-9.5M16.5 13.5C16.3 9 16 5.5 15.5 2.5"/></symbol>
<symbol id="tf-flame" viewBox="0 0 24 24"><path d="M12 22c4 0 7-2.8 7-6.8 0-3.6-2.4-5.9-3.8-8.1-.6 1.9-1.6 3-2.8 3.4C12.6 7 11 4 9 2c.2 4-4 6.6-4 12.6A7.1 7.1 0 0 0 12 22z"/></symbol>
<symbol id="tf-map" viewBox="0 0 24 24"><path d="M9 4 3 6.2v13.6L9 17.6l6 2.2 6-2.2V4l-6 2.2z"/><path d="M9 4v13.6M15 6.2v13.6"/></symbol>
<symbol id="tf-compass" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="m15.8 8.2-2.3 5.3-5.3 2.3 2.3-5.3z"/></symbol>
<symbol id="tf-car" viewBox="0 0 24 24"><path d="M3 16.5v-3.8L5.6 7.5h12.8l2.6 5.2v3.8z"/><path d="M3 12.7h18"/><circle cx="7.5" cy="16.8" r="1.8"/><circle cx="16.5" cy="16.8" r="1.8"/></symbol>
<symbol id="tf-cloud" viewBox="0 0 24 24"><path d="M7.5 19h10a4 4 0 0 0 .4-8A6 6 0 0 0 6.4 10.4 4.4 4.4 0 0 0 7.5 19z"/><path d="M16 3.5v1.6M20.6 5.4l-1.1 1.1M22.5 10h-1.6"/></symbol>
<symbol id="tf-cam" viewBox="0 0 24 24"><path d="M4 7.5h3.2l1.9-2.8h5.8l1.9 2.8H20a1.5 1.5 0 0 1 1.5 1.5v9A1.5 1.5 0 0 1 20 19.5H4A1.5 1.5 0 0 1 2.5 18V9A1.5 1.5 0 0 1 4 7.5z"/><circle cx="12" cy="13.2" r="3.6"/></symbol>
<symbol id="tf-photo" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="3.5"/><circle cx="9" cy="9" r="2"/><path d="m21 15.5-5.2-5.2L5 21"/></symbol>
<symbol id="tf-note-m" viewBox="0 0 24 24"><path d="M9 18V5.5l11-2V16"/><circle cx="6" cy="18" r="3"/><circle cx="17" cy="16" r="3"/></symbol>
<symbol id="tf-wave" viewBox="0 0 24 24"><path d="M3 12h1.5M7 8.5v7M11 5v14M15 8v8M19 6.5v11M21.5 12H21"/></symbol>
<symbol id="tf-bank" viewBox="0 0 24 24"><path d="M3 9.5 12 4l9 5.5"/><path d="M5.5 10.5v7M10 10.5v7M14 10.5v7M18.5 10.5v7M3 20h18"/></symbol>
<symbol id="tf-bars" viewBox="0 0 24 24"><path d="M4.5 20v-3M9.5 20v-6.5M14.5 20v-10M19.5 20V4"/></symbol>
<symbol id="tf-mega" viewBox="0 0 24 24"><path d="M3 10.5v3.5a1 1 0 0 0 1 1h2.2l5.3 4.2V5.3L6.2 9.5H4a1 1 0 0 0-1 1z"/><path d="M15.5 9a4.2 4.2 0 0 1 0 6.2M18.5 6.3a8 8 0 0 1 0 11.6"/></symbol>
<symbol id="tf-book" viewBox="0 0 24 24"><path d="M2.5 5H8a4 4 0 0 1 4 4v11a3 3 0 0 0-3-3H2.5zM21.5 5H16a4 4 0 0 0-4 4v11a3 3 0 0 1 3-3h6.5z"/></symbol>
<symbol id="tf-gavel" viewBox="0 0 24 24"><path d="m13.5 12.5-8 8a2 2 0 0 1-2.9-2.9l8-8"/><path d="m9.2 6.8 8 8M15.8 16.2l5.6-5.6M7.8 8.2l5.6-5.6M12.8 3.2l8 8"/></symbol>
<symbol id="tf-garage" viewBox="0 0 24 24"><path d="M3 20.5V9l9-5.5L21 9v11.5"/><path d="M7 20.5V12.5h10v8M7 16.5h10"/></symbol>
<symbol id="tf-house" viewBox="0 0 24 24"><path d="M3 11 12 3.8 21 11"/><path d="M5.2 9.5v10.7h13.6V9.5"/><path d="M10 20.2v-5.4h4v5.4"/></symbol>
<symbol id="tf-brief" viewBox="0 0 24 24"><rect x="3" y="7" width="18" height="13" rx="2.2"/><path d="M8.8 7V5.2A1.7 1.7 0 0 1 10.5 3.5h3a1.7 1.7 0 0 1 1.7 1.7V7M3 12.8h18"/></symbol>
<symbol id="tf-cctv" viewBox="0 0 24 24"><path d="M2.8 7.6 15.6 4.4l1.6 6.2L4.4 13.8z"/><path d="m8.6 12.4 1 4.6H3.5M3.5 14.5v5M17 9l3.8 1.2-.9 3.2-3.5-1.1"/></symbol>
<symbol id="tf-cal" viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="16" rx="2.5"/><path d="M3 10h18M8 3v4M16 3v4M8 14h.01M12 14h.01M16 14h.01M8 17.5h.01M12 17.5h.01"/></symbol>
<symbol id="tf-clock" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.2 2"/></symbol>
<symbol id="tf-notes" viewBox="0 0 24 24"><path d="M14 3H6.5A2 2 0 0 0 4.5 5v14a2 2 0 0 0 2 2h11a2 2 0 0 0 2-2V8.5z"/><path d="M14 3v5.5h5.5M8 13h8M8 17h5"/></symbol>
<symbol id="tf-folder" viewBox="0 0 24 24"><path d="M3 7a2 2 0 0 1 2-2h4.2l2 2.2H19a2 2 0 0 1 2 2V17a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></symbol>
<symbol id="tf-key" viewBox="0 0 24 24"><circle cx="7.5" cy="15.5" r="4.2"/><path d="m10.5 12.5 9-9M15.8 7.2l3 3M13.5 9.5l2 2"/></symbol>
<symbol id="tf-calc" viewBox="0 0 24 24"><rect x="5" y="2.5" width="14" height="19" rx="2.5"/><path d="M8.5 6.5h7M8.5 11h.01M12 11h.01M15.5 11h.01M8.5 14.5h.01M12 14.5h.01M15.5 14.5h.01M8.5 18h.01M12 18h3.5"/></symbol>
<symbol id="tf-heart" viewBox="0 0 24 24"><path d="M20.6 5.6a5.3 5.3 0 0 0-7.6 0L12 6.6l-1-1a5.3 5.3 0 1 0-7.6 7.6L12 21.6l8.6-8.4a5.3 5.3 0 0 0 0-7.6z"/><path d="M3.5 12h4l1.5-2.5 2.5 5 1.6-2.5h7.4"/></symbol>
<symbol id="tf-bird" viewBox="0 0 24 24"><path d="M3.5 13.5c0-4.4 3.6-7.5 8.4-7.5 4.4 0 8.1 2.6 8.1 6.2 0 3-2.3 5.3-6.3 5.3H9"/><path d="M15.2 10.2h.01M20 12.6h2.3M3.5 13.5l-1.8 3.2h5.6"/></symbol>
<symbol id="tf-blocks" viewBox="0 0 24 24"><path d="M3 13.5h6v6H3zM9 13.5h6v6H9zM9 7.5h6v6H9zM15 13.5h6v6h-6z"/></symbol>
<symbol id="tf-chess" viewBox="0 0 24 24"><path d="M6.5 21h11M8 21v-2.6h8V21M9 18.4c.3-3.6 1.6-5.4.7-7.8l-2.3 1-1.1-2.1L10.6 4h2.6c3.4.8 4.6 4.2 4.4 8.6l-.4 5.8"/></symbol>
<symbol id="tf-gear" viewBox="0 0 24 24"><circle cx="12" cy="12" r="3.2"/><path d="M12 2.5v3M12 18.5v3M2.5 12h3M18.5 12h3M5.3 5.3l2.1 2.1M16.6 16.6l2.1 2.1M5.3 18.7l2.1-2.1M16.6 7.4l2.1-2.1"/></symbol>
<symbol id="tf-store" viewBox="0 0 24 24"><path d="M6.5 18.5 12 7.5l5.5 11M8.6 14.5h6.8"/></symbol>
<symbol id="tf-watch" viewBox="0 0 24 24"><rect x="6" y="6" width="12" height="12" rx="3.2"/><path d="M9 6l.8-3.5h4.4L15 6M9 18l.8 3.5h4.4L15 18M12 9.5V12l1.6 1.2"/></symbol>
<symbol id="tf-speaker" viewBox="0 0 24 24"><rect x="5" y="2.5" width="14" height="19" rx="2.5"/><circle cx="12" cy="14.2" r="3.8"/><path d="M12 6.8h.01"/></symbol>
<symbol id="tf-torch" viewBox="0 0 24 24"><path d="M8 2.5h8v4l-2 3v12h-4v-12l-2-3z"/><path d="M8 6.5h8M12 13v2"/></symbol>
</svg>
<section class="tf-hero">
<div>
<div class="tf-kicker tf-rise">Telefon</div>
<h1 class="tf-rise r2">Tot orasul.<span>Intr-o mana.</span></h1>
<p class="tf-lead tf-rise r3">Apeluri, mesaje, banca, harti, muzica, masinile si casele tale. Scoti telefonul cu <kbd>M</kbd> si ai totul la indemana.</p>
<ul class="tf-chips tf-rise r4">
<li><kbd>M</kbd> deschide telefonul</li>
<li>Numar 07xx xxx xxx</li>
<li>Se cumpara de la DigitalDen</li>
</ul>
</div>
<div class="tf-stage" aria-hidden="true">
<div class="tf-halo"></div>
<div class="tf-ring"></div>
<div class="tf-orbit">
<div class="tf-ot"><div><i class="tf-ico c-gram"><svg class="tf-g"><use href="#tf-gram"/></svg></i></div></div>
<div class="tf-ot"><div><i class="tf-ico c-yellow"><svg class="tf-g"><use href="#tf-map"/></svg></i></div></div>
<div class="tf-ot"><div><i class="tf-ico c-emerald"><svg class="tf-g"><use href="#tf-bank"/></svg></i></div></div>
<div class="tf-ot"><div><i class="tf-ico c-red"><svg class="tf-g"><use href="#tf-note-m"/></svg></i></div></div>
<div class="tf-ot"><div><i class="tf-ico c-dark"><svg class="tf-g"><use href="#tf-car"/></svg></i></div></div>
<div class="tf-ot"><div><i class="tf-ico c-cherry"><svg class="tf-g"><use href="#tf-cherry"/></svg></i></div></div>
</div>
<div class="tf-phone">
<i class="tf-key k1"></i><i class="tf-key k2"></i><i class="tf-key k3"></i><i class="tf-key k4"></i>
<div class="tf-screen">
<div class="tf-island"></div>
<div class="tf-scr s1 tf-lock">
<div class="d">Joi, 6 noiembrie</div>
<div class="t">21:47</div>
<div class="tf-note"><i class="tf-ico c-green"><svg class="tf-g"><use href="#tf-msg"/></svg></i><div><b>Mesaje</b><span>Ne vedem la Legion Square?</span></div></div>
<div class="tf-note"><i class="tf-ico c-dark"><svg class="tf-g"><use href="#tf-car"/></svg></i><div><b>Ryde</b><span>Soferul tau a ajuns</span></div></div>
<div class="tf-lockbar"><i><svg class="tf-g"><use href="#tf-torch"/></svg></i><i><svg class="tf-g"><use href="#tf-cam"/></svg></i></div>
<div class="tf-home-ind"></div>
</div>
<div class="tf-scr s2 tf-homes">
<div class="tf-grid4">
<i class="tf-ico c-blue"><svg class="tf-g"><use href="#tf-mail"/></svg></i>
<i class="tf-ico c-yellow"><svg class="tf-g"><use href="#tf-map"/></svg></i>
<i class="tf-ico c-red"><svg class="tf-g"><use href="#tf-note-m"/></svg></i>
<i class="tf-ico c-sky"><svg class="tf-g"><use href="#tf-cloud"/></svg></i>
<i class="tf-ico c-emerald"><svg class="tf-g"><use href="#tf-bank"/></svg></i>
<i class="tf-ico c-gram"><svg class="tf-g"><use href="#tf-gram"/></svg></i>
<i class="tf-ico c-violet"><svg class="tf-g"><use href="#tf-clout"/></svg></i>
<i class="tf-ico c-cherry"><svg class="tf-g"><use href="#tf-cherry"/></svg></i>
<i class="tf-ico c-indigo"><svg class="tf-g"><use href="#tf-garage"/></svg></i>
<i class="tf-ico c-emerald"><svg class="tf-g"><use href="#tf-house"/></svg></i>
<i class="tf-ico c-dark"><svg class="tf-g"><use href="#tf-car"/></svg></i>
<i class="tf-ico c-teal"><svg class="tf-g"><use href="#tf-brief"/></svg></i>
<i class="tf-ico c-pink"><svg class="tf-g"><use href="#tf-heart"/></svg></i>
<i class="tf-ico c-blue"><svg class="tf-g"><use href="#tf-bars"/></svg></i>
<i class="tf-ico c-gray"><svg class="tf-g"><use href="#tf-gear"/></svg></i>
<i class="tf-ico c-blue"><svg class="tf-g"><use href="#tf-store"/></svg></i>
</div>
<div class="tf-dock">
<i class="tf-ico c-green"><svg class="tf-g"><use href="#tf-phone"/></svg></i>
<i class="tf-ico c-green"><svg class="tf-g"><use href="#tf-msg"/></svg></i>
<i class="tf-ico c-dark"><svg class="tf-g"><use href="#tf-cam"/></svg></i>
<i class="tf-ico c-white"><svg class="tf-g"><use href="#tf-photo"/></svg></i>
</div>
<div class="tf-home-ind"></div>
</div>
<div class="tf-scr s3 tf-maps">
<svg viewBox="0 0 218 466" preserveAspectRatio="xMidYMid slice">
<rect width="218" height="466" fill="#0f172a"/>
<path d="M0 300 C60 280 90 330 218 300 L218 466 L0 466Z" fill="#0c2340"/>
<g stroke="#1e293b" stroke-width="10" fill="none" stroke-linecap="round">
<path d="M-10 120 L230 160"/><path d="M40 -10 L80 480"/><path d="M150 -10 L130 480"/><path d="M-10 240 L230 220"/>
</g>
<g stroke="#334155" stroke-width="3" fill="none" stroke-linecap="round">
<path d="M-10 70 L230 90"/><path d="M110 -10 L100 480"/><path d="M-10 190 L230 196"/><path d="M190 -10 L180 300"/>
</g>
<rect x="88" y="128" width="34" height="26" rx="4" fill="#1f3b2a"/>
<path d="M62 330 L66 236 L104 232 L134 168 L168 148" stroke="#0a84ff" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<circle class="tf-pin" cx="168" cy="148" r="10" fill="#ef4444"/>
<circle cx="168" cy="148" r="6" fill="#ef4444" stroke="#fff" stroke-width="2"/>
<circle cx="62" cy="330" r="7" fill="#0a84ff" stroke="#fff" stroke-width="2.5"/>
</svg>
<div class="tf-sheet"><b>Destinatie setata</b><span>Pinul tau, pe GPS</span><i>Seteaza destinatia</i></div>
<div class="tf-home-ind"></div>
</div>
<div class="tf-glare"></div>
</div>
</div>
</div>
</section>
<ul class="tf-stats tf-rise r5">
<li><b>37</b><span>aplicatii pe server</span></li>
<li><b>13</b><span>se descarca din App Store</span></li>
<li><b>10</b><span>carcase la alegere, plus varianta pliabila</span></li>
<li><b>100%</b><span>baterie mereu: nu se descarca</span></li>
</ul>
<section class="tf-sec">
<div class="tf-eyebrow">Primii pasi</div>
<h2 class="tf-h2">Pornesti in patru miscari.</h2>
<p class="tf-sub">Fiecare personaj nou primeste un telefon din prima zi. Restul vine de la sine.</p>
<div class="tf-steps">
<div class="tf-card"><div class="tf-num">1</div><h3><img class="eg-item" src="/items/phone.webp" alt="">Ia un telefon</h3><p>Personajele noi il primesc in inventar. Daca l-ai pierdut, cumperi altul de la <b>DigitalDen</b>, magazinul marcat pe harta.</p></div>
<div class="tf-card"><div class="tf-num">2</div><h3>Deschide-l cu <kbd>M</kbd></h3><p>Sau folosesti telefonul din inventar. Tasta se schimba din <span class="tf-path">Setari FiveM → Key Bindings</span>, la <b>Deschide telefonul</b>.</p></div>
<div class="tf-card"><div class="tf-num">3</div><h3>Ai deja un numar</h3><p>Primul eSIM, <b>Principal</b>, e gratis si vine cu un numar de forma <b>07xx xxx xxx</b>.</p></div>
<div class="tf-card"><div class="tf-num">4</div><h3>Ai si internet</h3><p>Un telefon nou vine cu date mobile gratuite. Le vezi si le reincarci din <b>InetMax</b>.</p></div>
</div>
</section>
<section class="tf-sec">
<div class="tf-eyebrow">Aplicatii</div>
<h2 class="tf-h2">Tot ce iti trebuie. <span>Nimic in plus.</span></h2>
<p class="tf-sub">Majoritatea vin instalate. Cele marcate <span class="tf-tag">App Store</span> le descarci gratuit din App Store, iar descarcarea are nevoie de semnal.</p>
<div class="tf-cat">
<div class="tf-cat-h"><h3>Comunicare</h3><span>4 aplicatii</span></div>
<ul class="tf-apps">
<li><i class="tf-ico c-green"><svg class="tf-g"><use href="#tf-phone"/></svg></i><div><b>Telefon</b><p>Apeluri si apeluri video, Favorite, Recente, Contacte si mesagerie vocala. Poti bloca un numar.</p></div></li>
<li><i class="tf-ico c-green"><svg class="tf-g"><use href="#tf-msg"/></svg></i><div><b>Mesaje</b><p>Conversatii si grupuri de pana la 16 oameni. Trimiti locatia, locatia live, un contact, bani sau ceri bani.</p></div></li>
<li><i class="tf-ico c-blue"><svg class="tf-g"><use href="#tf-mail"/></svg></i><div><b>Email</b><p>Iti faci o adresa @lifeinvader.com cu parola si poti fi logat pe pana la 3 casute deodata.</p></div></li>
<li><i class="tf-ico c-dark"><svg class="tf-g"><use href="#tf-mask"/></svg></i><div><b>Dark Chat <span class="tf-tag">App Store</span></b><p>Vorbesti anonim, sub o porecla. Ai 5 camere publice si poti face camere private, cu cod.</p></div></li>
</ul>
</div>
<div class="tf-cat">
<div class="tf-cat-h"><h3>Social</h3><span>4 aplicatii</span></div>
<ul class="tf-apps">
<li><i class="tf-ico c-gram"><svg class="tf-g"><use href="#tf-gram"/></svg></i><div><b>Photogram <span class="tf-tag">App Store</span></b><p>Postari, povesti, mesaje private si Live din camera telefonului, 30 de minute pe zi.</p></div></li>
<li><i class="tf-ico c-violet"><svg class="tf-g"><use href="#tf-clout"/></svg></i><div><b>Clout <span class="tf-tag">App Store</span></b><p>Clipuri scurte, cu like-uri si comentarii. Poti pune peste clip o voce citita din textul tau.</p></div></li>
<li><i class="tf-ico c-cherry"><svg class="tf-g"><use href="#tf-cherry"/></svg></i><div><b>Cherry <span class="tf-tag">App Store</span></b><p>Dating: glisezi prin profiluri, faci potriviri si vorbesti cu ele.</p></div></li>
<li><i class="tf-ico c-orange"><svg class="tf-g"><use href="#tf-flame"/></svg></i><div><b>Streaks <span class="tf-tag">App Store</span></b><p>O poza noua in fiecare zi iti tine seria. Pozele tuturor intra intr-o galerie comuna, cu clasament.</p></div></li>
</ul>
</div>
<div class="tf-cat">
<div class="tf-cat-h"><h3>Prin oras</h3><span>4 aplicatii</span></div>
<ul class="tf-apps">
<li><i class="tf-ico c-yellow"><svg class="tf-g"><use href="#tf-map"/></svg></i><div><b>Harti</b><p>Harta orasului: pui pinuri, setezi destinatia pe GPS si iti vezi prietenii pe harta.</p></div></li>
<li><i class="tf-ico c-dark"><svg class="tf-g"><use href="#tf-compass"/></svg></i><div><b>Busola <span class="tf-tag">App Store</span></b><p>Iti arata directia in care te uiti.</p></div></li>
<li><i class="tf-ico c-dark"><svg class="tf-g"><use href="#tf-car"/></svg></i><div><b>Ryde</b><p>Comanzi o cursa sau conduci tu, cu masina ta. Soferii iti fac oferte de pret, tu alegi una, dai nota si bacsis.</p></div></li>
<li><i class="tf-ico c-sky"><svg class="tf-g"><use href="#tf-cloud"/></svg></i><div><b>Vreme</b><p>Vremea din oras, in timp real.</p></div></li>
</ul>
</div>
<div class="tf-cat">
<div class="tf-cat-h"><h3>Foto si muzica</h3><span>4 aplicatii</span></div>
<ul class="tf-apps">
<li><i class="tf-ico c-dark"><svg class="tf-g"><use href="#tf-cam"/></svg></i><div><b>Camera</b><p>Poze si clipuri, cu camera din fata sau din spate, filtre si mod peisaj. Te poti misca in timp ce filmezi.</p></div></li>
<li><i class="tf-ico c-white"><svg class="tf-g"><use href="#tf-photo"/></svg></i><div><b>Galerie</b><p>Pozele si clipurile tale, pe albume, inclusiv albume partajate. Copiezi link-ul sau o pui ca fundal.</p></div></li>
<li><i class="tf-ico c-red"><svg class="tf-g"><use href="#tf-note-m"/></svg></i><div><b>YouMusic</b><p>Cauti melodii pe YouTube, iti faci playlisturi si asculti pe telefon, pe EliteBox sau in masina.</p></div></li>
<li><i class="tf-ico c-red"><svg class="tf-g"><use href="#tf-wave"/></svg></i><div><b>Notite vocale</b><p>Inregistrezi rapid ce ai de zis si asculti mai tarziu.</p></div></li>
</ul>
</div>
<div class="tf-cat">
<div class="tf-cat-h"><h3>Bani si anunturi</h3><span>5 aplicatii</span></div>
<ul class="tf-apps">
<li><i class="tf-ico c-emerald"><svg class="tf-g"><use href="#tf-bank"/></svg></i><div><b>Banca</b><p>Soldul, istoricul si transferuri catre ID-ul sau numarul altui jucator. Iti alegi si cum arata cardul.</p></div></li>
<li><i class="tf-ico c-blue"><svg class="tf-g"><use href="#tf-bars"/></svg></i><div><b>InetMax</b><p>Datele mobile ramase, pachete de date de 5, 25 sau 100 GB si consumul pe fiecare aplicatie in ultimele 7 zile.</p></div></li>
<li><i class="tf-ico c-blue"><svg class="tf-g"><use href="#tf-mega"/></svg></i><div><b>Anunturi <span class="tf-tag">App Store</span></b><p>Anunturile din oras. Unul nou il publici la Agentia de Anunturi, apoi sta 24 de ore.</p></div></li>
<li><i class="tf-ico c-gold"><svg class="tf-g"><use href="#tf-book"/></svg></i><div><b>Pagini <span class="tf-tag">App Store</span></b><p>Panoul public al jucatorilor: oferte, servicii, cereri. Postezi direct din telefon.</p></div></li>
<li><i class="tf-ico c-amber"><svg class="tf-g"><use href="#tf-gavel"/></svg></i><div><b>Licitatii</b><p>Licitezi din banca sau din coins pe ce scot adminii la licitatie. Daca pierzi, iti iei banii inapoi din aplicatie.</p></div></li>
</ul>
</div>
<div class="tf-cat">
<div class="tf-cat-h"><h3>Masina, casa, serviciu</h3><span>4 aplicatii</span></div>
<ul class="tf-apps">
<li><i class="tf-ico c-indigo"><svg class="tf-g"><use href="#tf-garage"/></svg></i><div><b>Garaj <span class="tf-tag">App Store</span></b><p>Masinile tale: unde sunt, combustibil, motor si caroserie. Le incui sau descui cand esti langa ele.</p></div></li>
<li><i class="tf-ico c-emerald"><svg class="tf-g"><use href="#tf-house"/></svg></i><div><b>Case <span class="tf-tag">App Store</span></b><p>Casele si apartamentele tale, cumparate sau inchiriate. Incui usile si dai sau iei chei chiriasilor.</p></div></li>
<li><i class="tf-ico c-teal"><svg class="tf-g"><use href="#tf-brief"/></svg></i><div><b>Servicii</b><p>Scrii Politiei, Ambulantei si firmelor din oras. La job, intri sau iesi din tura de aici.</p></div></li>
<li><i class="tf-ico c-slate"><svg class="tf-g"><use href="#tf-cctv"/></svg></i><div><b>Supraveghere</b><p>Camerele de supraveghere la care ai acces, de exemplu cele din banci si magazine pentru Politie.</p></div></li>
</ul>
</div>
<div class="tf-cat">
<div class="tf-cat-h"><h3>Organizare</h3><span>7 aplicatii</span></div>
<ul class="tf-apps">
<li><i class="tf-ico c-white"><svg class="tf-g"><use href="#tf-cal"/></svg></i><div><b>Calendar</b><p>Evenimente, cu invitatii pe care ceilalti le accepta.</p></div></li>
<li><i class="tf-ico c-dark"><svg class="tf-g"><use href="#tf-clock"/></svg></i><div><b>Ceas</b><p>Alarme, cronometru, temporizatoare si ora pe glob.</p></div></li>
<li><i class="tf-ico c-gold"><svg class="tf-g"><use href="#tf-notes"/></svg></i><div><b>Notite</b><p>Notitele tale, cu schite desenate de mana.</p></div></li>
<li><i class="tf-ico c-blue"><svg class="tf-g"><use href="#tf-folder"/></svg></i><div><b>Fisiere</b><p>Documente in dosare. Ceri o semnatura si semnezi direct pe telefon.</p></div></li>
<li><i class="tf-ico c-dark"><svg class="tf-g"><use href="#tf-key"/></svg></i><div><b>Parole</b><p>Conturile salvate din aplicatii, intr-un singur loc.</p></div></li>
<li><i class="tf-ico c-dark"><svg class="tf-g"><use href="#tf-calc"/></svg></i><div><b>Calculator</b><p>Pentru socotelile de zi cu zi.</p></div></li>
<li><i class="tf-ico c-pink"><svg class="tf-g"><use href="#tf-heart"/></svg></i><div><b>Sanatate</b><p>Pasi si distanta pe zi, clasament de pasi si fisa ta medicala, citita de medici la nevoie.</p></div></li>
</ul>
</div>
<div class="tf-cat">
<div class="tf-cat-h"><h3>Jocuri si sistem</h3><span>5 aplicatii</span></div>
<ul class="tf-apps">
<li><i class="tf-ico c-cyan"><svg class="tf-g"><use href="#tf-bird"/></svg></i><div><b>Flappy <span class="tf-tag">App Store</span></b><p>Atingi ca sa zbori printre obstacole. Ai clasament.</p></div></li>
<li><i class="tf-ico c-violet"><svg class="tf-g"><use href="#tf-blocks"/></svg></i><div><b>Blocks <span class="tf-tag">App Store</span></b><p>Asezi piesele si stergi linii. Ai clasament.</p></div></li>
<li><i class="tf-ico c-dark"><svg class="tf-g"><use href="#tf-chess"/></svg></i><div><b>Sah <span class="tf-tag">App Store</span></b><p>Joci cu calculatorul sau online cu alt jucator, si pe miza din banca.</p></div></li>
<li><i class="tf-ico c-gray"><svg class="tf-g"><use href="#tf-gear"/></svg></i><div><b>Setari</b><p>Aspect, sunete, eSIM, Bluetooth, securitate si notificari.</p></div></li>
<li><i class="tf-ico c-blue"><svg class="tf-g"><use href="#tf-store"/></svg></i><div><b>App Store</b><p>Descarci aplicatiile care nu vin instalate si le stergi cand nu le mai vrei.</p></div></li>
</ul>
</div>
</section>
<section class="tf-sec">
<div class="tf-eyebrow">Apeluri si mesaje</div>
<h2 class="tf-h2">Vorbesti cum vrei.</h2>
<p class="tf-sub">Telefonul suna si pentru cei din jur, deci un apel se aude pe strada. In <b>Concentrare</b> sau pe silentios, ramane linistit.</p>
<div class="tf-three">
<div class="tf-card"><h3>Apeluri</h3><ul class="tf-list"><li>Apel normal sau apel video.</li><li>Cine nu raspunde poate primi un mesaj vocal.</li><li>Favorite pentru apel dintr-o atingere.</li><li>Blochezi un numar din fisa contactului.</li></ul></div>
<div class="tf-card"><h3>Mesaje</h3><ul class="tf-list"><li>Grupuri cu nume, pana la 16 oameni.</li><li>Locatia ta, o data sau live.</li><li>Trimiti sau ceri bani direct in conversatie.</li><li>Un contact trimis in chat se salveaza dintr-o atingere.</li></ul></div>
<div class="tf-card"><h3>Contacte</h3><ul class="tf-list"><li>Le adaugi cu nume, numar si poza.</li><li>Trimiti un contact unui jucator de langa tine.</li></ul></div>
</div>
</section>
<section class="tf-sec">
<div class="tf-eyebrow">Numarul tau</div>
<h2 class="tf-h2">eSIM. <span>Unul activ, oricand altul.</span></h2>
<div class="tf-two">
<div class="tf-card"><h3>Cum functioneaza</h3><p>Numarul tau sta pe un eSIM. Primul, <b>Principal</b>, il ai gratis. Poti cumpara si alte eSIM-uri, fiecare cu numar nou, din <span class="tf-path">Setari → eSIM</span>.</p><p>Doar unul e activ odata. Apelurile, mesajele, contactele si conturile tin de eSIM-ul activ, iar schimbarea reporneste telefonul.</p></div>
<div class="tf-card"><h3>Stergerea</h3><p>Cand stergi un eSIM, pierzi definitiv conversatiile, apelurile si numarul de pe el. Dupa o stergere astepti o perioada pana poti cumpara altul.</p><p>Pretul si cate eSIM-uri poti avea se vad in aplicatie, inainte sa cumperi.</p></div>
</div>
</section>
<section class="tf-sec">
<div class="tf-eyebrow">Date mobile</div>
<h2 class="tf-h2">InetMax. <span>Internetul din buzunar.</span></h2>
<div class="tf-two">
<div class="tf-card"><h3>Ce consuma date</h3><ul class="tf-list"><li>Mesaje, emailuri, Dark Chat, Cherry si mesajele din Photogram.</li><li>Postarile din Photogram si Clout, plus pornirea unui Live.</li><li>Anunturile si postarile din Pagini.</li><li>Transferurile din Banca.</li><li>Cautarile si link-urile din YouMusic.</li></ul></div>
<div class="tf-card"><h3>Cand se termina</h3><p>Fara date nu mai trimiti, nu mai postezi si nu mai poti suna. Apelurile cer date ca sa porneasca, dar nu consuma din ele.</p><p>Reincarci din <b>InetMax</b> cu pachete de 5, 25 sau 100 GB. Platesti cash, iar daca nu ajunge, din banca.</p></div>
</div>
</section>
<section class="tf-sec">
<div class="tf-eyebrow">Harti</div>
<h2 class="tf-h2">Nu te mai pierzi.</h2>
<div class="tf-three">
<div class="tf-card"><h3>Pinuri si GPS</h3><p>Apesi <b>+</b> si pui un pin pe harta. <b>Seteaza destinatia</b> il trimite in GPS-ul jocului.</p></div>
<div class="tf-card"><h3>Coduri de destinatie</h3><p>Copiezi codul unei destinatii si il trimiti. Cine il primeste il lipeste la <b>Importa destinatie</b>.</p></div>
<div class="tf-card"><h3>Prieteni pe harta</h3><p>Adaugi prieteni din Contacte sau dupa numar. Daca accepta, va vedeti unul pe altul pana opriti partajarea.</p></div>
</div>
<p class="tf-note2">Pe jos, minimapa apare doar cat ai telefonul deschis sau un <b><img class="eg-item" src="/items/smartwatch.webp" alt="">SmartWatch</b> la tine. In masina o ai mereu.</p>
</section>
<section class="tf-sec">
<div class="tf-eyebrow">Accesorii</div>
<h2 class="tf-h2">Merg mana in mana.</h2>
<p class="tf-sub">Le gasesti la DigitalDen, langa telefon.</p>
<div class="tf-two">
<div class="tf-card tf-acc"><i class="tf-ico c-dark"><svg class="tf-g"><use href="#tf-watch"/></svg></i><div><h3><img class="eg-item" src="/items/smartwatch.webp" alt="">SmartWatch (GPS)</h3><p>Cat il ai in inventar, vezi minimapa si pe jos, fara sa scoti telefonul.</p></div></div>
<div class="tf-card tf-acc"><i class="tf-ico c-red"><svg class="tf-g"><use href="#tf-speaker"/></svg></i><div><h3><img class="eg-item" src="/items/elitebox.webp" alt="">EliteBox</h3><p>Folosesti boxa din inventar si o asezi pe jos. Te conectezi din YouMusic sau din <span class="tf-path">Setari → Bluetooth</span>, iar muzica se aude din boxa pentru toti cei din jur.</p><p>O iei inapoi cu <b>Ridica boxa</b>. Tot asa te conectezi si la sistemul audio al masinii.</p></div></div>
</div>
</section>
<section class="tf-sec">
<div class="tf-eyebrow">Personalizare</div>
<h2 class="tf-h2">Al tau. <span>Pana la ultimul pixel.</span></h2>
<div class="tf-three">
<div class="tf-card"><h3>Corp si ecran</h3><ul class="tf-list"><li>10 carcase, din <span class="tf-path">Setari → Afisaj si luminozitate</span>.</li><li>Telefon pliabil: deschizi balamaua si ai ecran dublu, cu doua aplicatii una langa alta.</li><li>Mod intunecat, fundal, tema iconitelor.</li><li>Un animalut pe Dynamic Island.</li></ul></div>
<div class="tf-card"><h3>Ecran principal</h3><ul class="tf-list"><li>Muti aplicatiile unde vrei.</li><li>Alegi cat de mari sunt iconitele.</li><li>Redenumesti aplicatiile.</li></ul></div>
<div class="tf-card"><h3>Liniste si siguranta</h3><ul class="tf-list"><li>Mod avion, Concentrare, Mod streamer.</li><li>Cod de acces si scanare fata.</li><li>Ton de apel la alegere, chiar si o melodie de pe YouTube.</li><li>Pe ecranul de blocare ai lanterna si fisa medicala.</li></ul></div>
</div>
</section>
<section class="tf-sec">
<div class="tf-eyebrow">Taste</div>
<h2 class="tf-h2">Scurtaturi.</h2>
<p class="tf-sub">Cu telefonul deschis poti merge in continuare. Mouse-ul controleaza ecranul, nu camera jocului. Toate tastele se schimba din Key Bindings.</p>
<ul class="tf-keys">
<li><kbd>M</kbd><span>Deschide sau inchide telefonul</span></li>
<li><kbd>Mouse 4</kbd><span>Tii apasat ca sa te uiti in jur cu telefonul deschis</span></li>
<li><kbd>Alt</kbd><span>In camera: preda mouse-ul ca sa tintesti, apoi il iei inapoi</span></li>
<li><kbd>↓</kbd><span>Selfie: misti camera in jurul tau, nu personajul</span></li>
<li><kbd>Shift</kbd><span>Selfie (Shift dreapta): personajul se uita in camera</span></li>
<li><kbd>Backspace</kbd><span>Iesi dintr-o camera de supraveghere (rotita face zoom)</span></li>
</ul>
</section>
<section class="tf-sec">
<div class="tf-eyebrow">Bine de stiut</div>
<h2 class="tf-h2">Cand telefonul tace.</h2>
<div class="tf-three">
<div class="tf-card"><h3>Nu se deschide</h3><ul class="tf-list"><li>Nu ai telefon in inventar.</li><li>Esti mort, la pamant sau incatusat.</li><li>Inoti.</li><li>Ai o arma in mana.</li></ul></div>
<div class="tf-card"><h3>Fara semnal</h3><p>Pe varful Muntelui Chiliad, in mine si in cateva zone izolate nu ai semnal: nu suni, nu trimiti mesaje, nu folosesti internetul. In Sandy Shores semnalul e slab si apelurile se aud intrerupt.</p><p>Langa un bruiaj (jammer) pornit, telefonul ramane fara semnal.</p></div>
<div class="tf-card"><h3>Bateria</h3><p>Nu se descarca si nu ai nevoie de incarcator. Telefonul merge cat timp il ai la tine.</p></div>
</div>
</section>
</div>
