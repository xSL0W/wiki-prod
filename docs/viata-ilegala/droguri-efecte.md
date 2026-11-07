---
outline: false
---

<style>
.vdr {
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
  --weed: #4ade80;
  --meth: #22d3ee;
  --coke: #e4e4e7;
  --lsd: #c084fc;
  --hero: #f87171;
  max-width: 960px;
  margin: 0 auto;
  color: var(--text);
  font-family: Inter, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.vdr *, .vdr *::before, .vdr *::after { box-sizing: border-box; }
.vdr p, .vdr li { margin: 0; line-height: 1.6; color: var(--text); }
.vdr ul, .vdr ol { list-style: none; padding: 0; margin: 0; }
.vdr li + li { margin-top: 0; }
.vdr b { color: #fff; font-weight: 650; }
.vdr a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.vdr a:hover { color: #fecaca; }
.vdr a:focus-visible { outline: 3px solid var(--red); outline-offset: 3px; border-radius: 8px; }
.vdr kbd { font: inherit; font-size: 0.85em; font-weight: 700; color: #fff; background: var(--blood); border-radius: 6px; padding: 0.05rem 0.45rem; }
/* ---------- hero ---------- */
.vdr .vdr-hero {
  position: relative; overflow: hidden; isolation: isolate;
  display: grid; grid-template-columns: minmax(0, 1fr); gap: 1.4rem; align-items: center;
  background: radial-gradient(90% 110% at 100% 0%, rgba(192, 132, 252, 0.1), transparent 55%), radial-gradient(120% 90% at 0% 120%, rgba(185, 28, 28, 0.3), transparent 60%), var(--ink);
  border: 1px solid var(--line); border-radius: 22px;
  padding: clamp(1.15rem, 4vw, 2.4rem);
}
.vdr .vdr-hero::after {
  content: ''; position: absolute; inset: 0; z-index: -1; pointer-events: none;
  background: repeating-linear-gradient(0deg, rgba(255, 255, 255, 0.018) 0 1px, transparent 1px 4px);
}
.vdr .vdr-kicker {
  display: inline-flex; align-items: center; gap: 0.5rem; margin-bottom: 0.7rem;
  font: 700 0.74rem/1.2 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace;
  letter-spacing: 0.18em; text-transform: uppercase; color: var(--red);
}
.vdr .vdr-kicker::before { content: ''; width: 8px; height: 8px; border-radius: 50%; background: var(--red); box-shadow: 0 0 0 4px var(--ember); animation: vdr-rec 1.6s steps(1, end) infinite; }
@keyframes vdr-rec { 0%, 60% { opacity: 1; } 61%, 100% { opacity: 0.25; } }
.vdr .vdr-hero h1 {
  margin: 0 0 0.8rem; padding: 0; border: 0; color: #fff;
  font-size: clamp(2.1rem, 7vw, 3.6rem); line-height: 1.02; font-weight: 850; letter-spacing: -0.035em;
}
.vdr .vdr-hero h1 span { color: var(--red); }
.vdr .vdr-lede { max-width: 56ch; color: var(--mute); font-size: 1.05rem; }
.vdr .vdr-chips { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1.1rem; }
.vdr .vdr-chips li {
  display: inline-flex; align-items: baseline; gap: 0.4rem;
  background: rgba(15, 15, 17, 0.9); border: 1px solid var(--line2); border-radius: 999px; padding: 0.3rem 0.8rem;
  font-size: 0.85rem; color: var(--mute);
}
.vdr .vdr-chips b { font-size: 1rem; font-variant-numeric: tabular-nums; }
/* element tiles */
.vdr .vdr-table { display: grid; grid-template-columns: repeat(auto-fit, minmax(6.2rem, 1fr)); gap: 0.5rem; }
.vdr .vdr-table li { position: relative; min-height: 6.2rem; border-radius: 14px; padding: 0.55rem 0.65rem; background: rgba(15, 15, 17, 0.92); border: 1px solid var(--line2); border-top: 3px solid var(--c); display: flex; flex-direction: column; justify-content: space-between; }
.vdr .vdr-table li a { position: absolute; inset: 0; border-radius: 14px; }
.vdr .vdr-table li:hover { border-color: var(--c); }
.vdr .vdr-table .n { font: 700 0.66rem/1 ui-monospace, Menlo, Consolas, monospace; color: var(--dim); }
.vdr .vdr-table .s { font: 850 1.7rem/1 Inter, system-ui, sans-serif; color: var(--c); letter-spacing: -0.02em; }
.vdr .vdr-table .l { font-size: 0.74rem; color: var(--mute); line-height: 1.2; }
.vdr .vdr-table li.na { border-top-color: var(--line2); border-style: dashed; justify-content: center; align-items: center; text-align: center; }
.vdr .vdr-table li.na .l { color: var(--dim); }
@media (prefers-reduced-motion: reduce) { .vdr .vdr-kicker::before { animation: none; } }
/* ---------- sections ---------- */
.vdr .vdr-h2 {
  display: flex; align-items: baseline; gap: 0.7rem;
  margin: 3rem 0 0.6rem; padding: 0; border: 0;
  font-size: 1.5rem; line-height: 1.25; font-weight: 750; letter-spacing: -0.015em; color: #fff;
}
.vdr .vdr-h2 span { font: 700 0.8rem/1 ui-monospace, Menlo, Consolas, monospace; color: var(--red); letter-spacing: 0.1em; }
.vdr .vdr-sub { color: var(--mute); max-width: 68ch; margin-bottom: 1.1rem; }
.vdr .vdr-h3 { margin: 0 0 0.35rem; padding: 0; border: 0; font-size: 1.06rem; line-height: 1.3; font-weight: 700; color: #fff; }
.vdr .vdr-card { background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 1.1rem 1.2rem; }
.vdr .vdr-card > p { color: var(--mute); font-size: 0.95rem; }
.vdr .vdr-card > p + p { margin-top: 0.5rem; }
.vdr .vdr-note { margin-top: 0.85rem; color: var(--mute); font-size: 0.92rem; }
.vdr .vdr-ticks { display: grid; gap: 0.45rem; margin-top: 0.6rem; }
.vdr .vdr-ticks li { position: relative; padding-left: 1.2rem; color: var(--mute); font-size: 0.94rem; line-height: 1.5; }
.vdr .vdr-ticks li::before { content: ''; position: absolute; left: 0; top: 0.55em; width: 7px; height: 7px; transform: rotate(45deg); background: var(--red); }
/* overview matrix */
.vdr .vdr-matrix { border: 1px solid var(--line); border-radius: 16px; overflow: hidden; background: var(--panel); }
.vdr .vdr-matrix li { display: grid; grid-template-columns: minmax(0, 1.05fr) minmax(0, 1.5fr) 5.5rem 7rem; gap: 0.7rem; align-items: center; padding: 0.7rem 1rem; border-top: 1px solid var(--line); font-size: 0.93rem; color: var(--mute); }
.vdr .vdr-matrix li:first-child { border-top: 0; background: var(--panel2); font: 700 0.7rem/1.2 ui-monospace, Menlo, Consolas, monospace; letter-spacing: 0.1em; text-transform: uppercase; color: var(--dim); }
.vdr .vdr-matrix .d { display: flex; align-items: center; gap: 0.55rem; font-weight: 700; color: #fff; }
.vdr .vdr-matrix .d::before { content: ''; flex: none; width: 0.65rem; height: 0.65rem; border-radius: 50%; background: var(--c); }
.vdr .vdr-matrix .t { font: 700 0.85rem/1.2 ui-monospace, Menlo, Consolas, monospace; color: #fff; }
.vdr .vdr-risk { display: inline-flex; gap: 3px; vertical-align: middle; }
.vdr .vdr-risk i { width: 0.9rem; height: 0.45rem; border-radius: 2px; background: #2a2a30; font-style: normal; }
.vdr .vdr-risk i.f { background: var(--red); }
@media (max-width: 640px) {
  .vdr .vdr-matrix li { grid-template-columns: minmax(0, 1fr) auto; gap: 0.25rem 0.8rem; }
  .vdr .vdr-matrix li:first-child { display: none; }
  .vdr .vdr-matrix .e { grid-column: 1 / -1; order: 3; }
  .vdr .vdr-matrix .t { text-align: right; }
  .vdr .vdr-matrix .r { grid-column: 1 / -1; order: 4; }
  .vdr .vdr-matrix .r::before { content: 'Risc bad trip '; font-size: 0.8rem; color: var(--dim); margin-right: 0.4rem; }
}
/* drug sheets */
.vdr .vdr-sheets { display: grid; gap: 0.9rem; }
.vdr .vdr-sheet { position: relative; display: grid; grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr); gap: 0; border: 1px solid var(--line); border-radius: 18px; overflow: hidden; background: var(--panel); scroll-margin-top: 80px; }
@media (max-width: 760px) { .vdr .vdr-sheet { grid-template-columns: minmax(0, 1fr); } }
.vdr .vdr-sheet .fx { padding: 1.1rem 1.2rem 1.15rem; background: linear-gradient(160deg, color-mix(in srgb, var(--c) 12%, transparent), transparent 60%); border-right: 1px solid var(--line); }
@media (max-width: 760px) { .vdr .vdr-sheet .fx { border-right: 0; border-bottom: 1px solid var(--line); } }
.vdr .vdr-sheet .it { font: 700 0.7rem/1.2 ui-monospace, Menlo, Consolas, monospace; letter-spacing: 0.14em; text-transform: uppercase; color: var(--c); }
.vdr .vdr-sheet h3 { margin: 0.2rem 0 0.7rem; padding: 0; border: 0; font-size: 1.45rem; font-weight: 820; letter-spacing: -0.02em; color: #fff; line-height: 1.15; }
.vdr .vdr-sheet .big { display: block; font: 850 clamp(1.6rem, 5vw, 2.1rem)/1.05 Inter, system-ui, sans-serif; color: #fff; letter-spacing: -0.02em; }
.vdr .vdr-sheet .bigl { display: block; margin-top: 0.2rem; color: var(--mute); font-size: 0.92rem; }
.vdr .vdr-sheet .dur { display: inline-flex; align-items: center; gap: 0.4rem; margin-top: 0.8rem; padding: 0.3rem 0.65rem; border-radius: 999px; border: 1px solid var(--line2); background: rgba(6, 6, 7, 0.6); font: 700 0.8rem/1.2 ui-monospace, Menlo, Consolas, monospace; color: #fff; }
.vdr .vdr-sheet .dur::before { content: ''; width: 0.5rem; height: 0.5rem; border-radius: 50%; background: var(--c); }
.vdr .vdr-sheet .vis { margin-top: 0.85rem; color: var(--mute); font-size: 0.92rem; line-height: 1.5; }
.vdr .vdr-sheet .how { padding: 1.1rem 1.2rem 1.15rem; }
.vdr .vdr-sheet .how .k { display: block; margin-bottom: 0.55rem; font: 700 0.7rem/1.2 ui-monospace, Menlo, Consolas, monospace; letter-spacing: 0.14em; text-transform: uppercase; color: var(--dim); }
.vdr .vdr-chain { display: grid; gap: 0.4rem; counter-reset: vdr-c; }
.vdr .vdr-chain li { position: relative; counter-increment: vdr-c; padding: 0.5rem 0.75rem 0.5rem 2.4rem; border-radius: 10px; background: var(--panel2); border: 1px solid var(--line); color: var(--mute); font-size: 0.92rem; line-height: 1.45; }
.vdr .vdr-chain li::before { content: counter(vdr-c); position: absolute; left: 0.65rem; top: 0.55rem; width: 1.2rem; height: 1.2rem; border-radius: 50%; display: grid; place-items: center; font-size: 0.7rem; font-weight: 800; color: #111; background: var(--c); }
.vdr .vdr-chain li.use { background: rgba(6, 6, 7, 0.6); border-style: dashed; border-color: var(--c); color: #fff; }
.vdr .vdr-sheet .bad { margin-top: 0.75rem; padding: 0.6rem 0.75rem; border-radius: 10px; background: #140707; border: 1px solid #3f1212; color: #fecaca; font-size: 0.9rem; line-height: 1.5; }
.vdr .vdr-sheet .bad b { color: #fca5a5; }
/* risks */
.vdr .vdr-two { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr)); gap: 0.8rem; }
.vdr .vdr-od { border: 1px solid #4c1414; border-radius: 18px; overflow: hidden; background: linear-gradient(160deg, #1a0808, var(--panel) 55%); }
.vdr .vdr-od .hd { padding: 1.05rem 1.2rem 0.4rem; }
.vdr .vdr-od .hd p { color: var(--mute); font-size: 0.95rem; }
.vdr .vdr-od ol { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 0; margin-top: 0.7rem; border-top: 1px solid #3f1212; }
.vdr .vdr-od ol li { position: relative; padding: 0.9rem 1rem 1rem; border-right: 1px solid #3f1212; color: var(--mute); font-size: 0.9rem; line-height: 1.5; }
.vdr .vdr-od ol li:last-child { border-right: 0; background: rgba(239, 68, 68, 0.08); }
.vdr .vdr-od ol .t { display: block; margin-bottom: 0.3rem; font: 700 0.7rem/1.2 ui-monospace, Menlo, Consolas, monospace; letter-spacing: 0.12em; text-transform: uppercase; color: var(--red); }
@media (max-width: 760px) {
  .vdr .vdr-od ol { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); }
  .vdr .vdr-od ol li:nth-child(2) { border-right: 0; }
  .vdr .vdr-od ol li:nth-child(-n+2) { border-bottom: 1px solid #3f1212; }
}
@media (max-width: 420px) { .vdr .vdr-od ol { grid-template-columns: minmax(0, 1fr); } .vdr .vdr-od ol li { border-right: 0; border-bottom: 1px solid #3f1212; } }
.vdr .vdr-weights { display: grid; gap: 0.45rem; margin-top: 0.75rem; }
.vdr .vdr-weights li { display: grid; grid-template-columns: 7rem minmax(0, 1fr); align-items: center; gap: 0.7rem; font-size: 0.9rem; color: var(--mute); }
.vdr .vdr-weights .bar { height: 0.55rem; border-radius: 999px; background: #1f1f24; overflow: hidden; }
.vdr .vdr-weights .bar i { display: block; height: 100%; border-radius: 999px; background: var(--c); font-style: normal; }
/* deliveries */
.vdr .vdr-route { display: flex; flex-wrap: wrap; align-items: center; gap: 0.4rem; margin: 0.2rem 0 1rem; }
.vdr .vdr-route span { display: inline-flex; align-items: center; padding: 0.35rem 0.7rem; border-radius: 10px; background: var(--panel2); border: 1px solid var(--line2); font-weight: 650; font-size: 0.9rem; color: #fff; }
.vdr .vdr-route > span + span { position: relative; margin-left: 1rem; }
/* the slash belongs to the next step, so a wrapped line never starts on a lone slash */
.vdr .vdr-route > span + span::before { content: '/'; position: absolute; left: -0.95rem; color: var(--dim); font-weight: 400; }
.vdr .vdr-drops { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 270px), 1fr)); gap: 0.6rem; }
.vdr .vdr-drops li { display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: 0.1rem 0.8rem; align-items: baseline; padding: 0.75rem 0.9rem; border-radius: 14px; background: var(--panel); border: 1px solid var(--line); border-left: 3px solid var(--c); }
.vdr .vdr-drops .p { font-weight: 700; color: #fff; }
.vdr .vdr-drops .h { font: 800 1rem/1 ui-monospace, Menlo, Consolas, monospace; color: #fff; white-space: nowrap; }
.vdr .vdr-drops .h small { font-size: 0.7rem; color: var(--dim); margin-left: 0.15rem; }
.vdr .vdr-drops .z { color: var(--mute); font-size: 0.86rem; }
.vdr .vdr-drops .zl { color: var(--dim); font-size: 0.78rem; text-align: right; }
/* other substances */
.vdr .vdr-other { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr)); gap: 0.8rem; }
.vdr .vdr-other > li { background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 1rem 1.15rem 1.1rem; }
.vdr .vdr-other .tag { display: inline-block; margin-bottom: 0.3rem; font: 700 0.68rem/1.2 ui-monospace, Menlo, Consolas, monospace; letter-spacing: 0.14em; text-transform: uppercase; color: var(--brass); }
.vdr .vdr-other p { color: var(--mute); font-size: 0.93rem; line-height: 1.5; }
.vdr .vdr-promil { display: grid; gap: 0.3rem; margin-top: 0.6rem; }
.vdr .vdr-promil li { display: grid; grid-template-columns: 3.2rem minmax(0, 1fr); gap: 0.6rem; font-size: 0.88rem; color: var(--mute); line-height: 1.4; }
.vdr .vdr-promil b { font: 700 0.85rem/1.4 ui-monospace, Menlo, Consolas, monospace; color: var(--brass); }
</style>

<div class="vdr">
<section class="vdr-hero">
<div>
<p class="vdr-kicker">Viata ilegala / Droguri</p>
<h1>Droguri &amp; <span>Efecte</span></h1>
<p class="vdr-lede">Fiecare drog iti da un avantaj real cat timp esti sub efect: mai multa viata, sprint, greutate in inventar sau un recul mai mic. Platesti cu riscul: bad trip, dureri in piept si supradoza. Aici vezi ce face fiecare si cum ajungi la el.</p>
<ul class="vdr-chips">
<li><b>5</b> droguri</li>
<li><b>10-30</b> minute de efect</li>
<li><b>5</b> minute de supradoza</li>
</ul>
</div>
<ul class="vdr-table" aria-label="Drogurile de pe server">
<li style="--c: var(--weed)"><a href="#iarba" aria-label="Iarba"></a><span class="n">01</span><span class="s">Ia</span><span class="l">Iarba</span></li>
<li style="--c: var(--meth)"><a href="#metamfetamina" aria-label="Metamfetamina"></a><span class="n">02</span><span class="s">Me</span><span class="l">Metamfetamina</span></li>
<li style="--c: var(--coke)"><a href="#cocaina" aria-label="Cocaina"></a><span class="n">03</span><span class="s">Co</span><span class="l">Cocaina</span></li>
<li style="--c: var(--hero)"><a href="#heroina" aria-label="Heroina"></a><span class="n">04</span><span class="s">He</span><span class="l">Heroina</span></li>
<li style="--c: var(--lsd)"><a href="#lsd" aria-label="LSD"></a><span class="n">05</span><span class="s">Ls</span><span class="l">LSD</span></li>
<li class="na"><span class="l">Efectul activ apare pe HUD si scade pe masura ce trece</span></li>
</ul>
</section>
<h2 class="vdr-h2" id="pe-scurt"><span>01</span>Pe scurt</h2>
<ul class="vdr-matrix">
<li><span>Drog</span><span class="e">Ce iti da</span><span class="t">Durata</span><span class="r">Risc bad trip</span></li>
<li><span class="d" style="--c: var(--weed)">Iarba (joint)</span><span class="e">+1 viata la fiecare 15 secunde</span><span class="t">10 min</span><span class="r"><span class="vdr-risk"><i class="f"></i><i></i><i></i><i></i></span></span></li>
<li><span class="d" style="--c: var(--meth)">Metamfetamina</span><span class="e">Sprint mai rapid cu 10% si rezistenta</span><span class="t">15 min</span><span class="r"><span class="vdr-risk"><i class="f"></i><i class="f"></i><i class="f"></i><i></i></span></span></li>
<li><span class="d" style="--c: var(--coke)">Cocaina</span><span class="e">+10 kg in inventar</span><span class="t">30 min</span><span class="r"><span class="vdr-risk"><i class="f"></i><i class="f"></i><i></i><i></i></span></span></li>
<li><span class="d" style="--c: var(--hero)">Heroina</span><span class="e">Recul mai mic cu 15% la arme</span><span class="t">10 min</span><span class="r"><span class="vdr-risk"><i class="f"></i><i class="f"></i><i class="f"></i><i></i></span></span></li>
<li><span class="d" style="--c: var(--lsd)">LSD (timbru)</span><span class="e">Lucrezi mai repede la unele mese ilegale</span><span class="t">10 min</span><span class="r"><span class="vdr-risk"><i class="f"></i><i class="f"></i><i class="f"></i><i class="f"></i></span></span></li>
</ul>
<p class="vdr-note">O noua doza luata cat inca esti sub efect reporneste cronometrul, nu dubleaza bonusul. In schimb, substanta se aduna in corp si creste riscurile.</p>
<h2 class="vdr-h2" id="fisele-drogurilor"><span>02</span>Fisele drogurilor</h2>
<p class="vdr-sub">Semintele le cumperi de la un magazin de seminte: unde e, afli in joc. Plicurile goale, hartia, foitele si substantele pentru metamfetamina sunt la <a href="/proprietati/homedepot">Home Depot</a>, iar kerosenul la magazinul aeronautic. Ca sa plantezi si sa culegi ai nevoie de un minim de ore jucate. Politistii si medicii nu pot lucra la mesele ilegale.</p>
<div class="vdr-sheets">
<article class="vdr-sheet" id="iarba" style="--c: var(--weed)">
<div class="fx"><span class="it">Joint</span><h3>Iarba</h3><span class="big">+40 viata</span><span class="bigl">cate 1 la fiecare 15 secunde, dupa ce termini jointul</span><span class="dur">2 min fumat + 10 min efect</span><p class="vis">Culori mai vii, putin blur. La doze mari camera se misca si apar halucinatii.</p></div>
<div class="how"><span class="k">Cum il obtii</span><ol class="vdr-chain"><li>Plantezi <b>Seminte iarba</b> pe Cayo Perico si culegi <b>Mugure de iarba</b>.</li><li>In laboratorul de iarba de pe insula maruntesti mugurii in <b>Iarba</b>.</li><li>Rulezi jointul din <b>Iarba</b> si <b>Foite tigari</b>.</li><li class="use">Il fumezi din inventar.</li></ol><p class="bad"><b>Bad trip:</b> cel mai mic risc dintre droguri. Creste cu cat ai mai multa iarba in corp.</p></div>
</article>
<article class="vdr-sheet" id="metamfetamina" style="--c: var(--meth)">
<div class="fx"><span class="it">Plic metamfetamina</span><h3>Metamfetamina</h3><span class="big">+10% sprint</span><span class="bigl">si rezistenta care se reface singura cat alergi</span><span class="dur">15 min</span><p class="vis">Filtru pe imagine si camera care tremura. La doze mari se zguduie tot mai tare.</p></div>
<div class="how"><span class="k">Cum o obtii</span><ol class="vdr-chain"><li>Iei <b>Propilen glicol</b> si <b>Benzoat de sodiu</b>.</li><li>In laboratorul de metamfetamina de pe Cayo Perico le amesteci la <b>Mixer</b>.</li><li>La <b>Solidificator</b> scoti o <b>Tava cu metamfetamina</b>.</li><li>La masa de distributie o imparti in <b>Plic metamfetamina</b>, cu plicuri goale.</li><li class="use">Consumi plicul din inventar.</li></ol><p class="bad"><b>Bad trip:</b> risc mediu. Ai halucinatii cu clovni.</p></div>
</article>
<article class="vdr-sheet" id="cocaina" style="--c: var(--coke)">
<div class="fx"><span class="it">Plic coca</span><h3>Cocaina</h3><span class="big">+10 kg</span><span class="bigl">in plus la cat poti cara in inventar</span><span class="dur">30 min</span><p class="vis">Imagine mai luminoasa si mana care tremura usor.</p></div>
<div class="how"><span class="k">Cum o obtii</span><ol class="vdr-chain"><li>Plantezi <b>Seminte coca</b> pe Cayo Perico si culegi <b>Frunze de coca</b>.</li><li>In laboratorul de cocaina de pe insula faci <b>Plic coca</b> din frunze, kerosen si plicuri goale.</li><li class="use">Consumi plicul din inventar.</li></ol><p class="bad"><b>Atentie:</b> cand efectul trece, pierzi cele 10 kg. Daca atunci ai in inventar mai mult decat limita normala, nu mai poti lua nimic pana nu scapi de greutate.</p></div>
</article>
<article class="vdr-sheet" id="heroina" style="--c: var(--hero)">
<div class="fx"><span class="it">Plic heroina</span><h3>Heroina</h3><span class="big">-15% recul</span><span class="bigl">la toate armele: tinta mai stabila in lupta</span><span class="dur">10 min</span><p class="vis">O senzatie de plutire, imagine ca prin vis.</p></div>
<div class="how"><span class="k">Cum o obtii</span><ol class="vdr-chain"><li>Plantezi <b>Seminte mac</b> la plantatia de mac. E un No Man's Land: acolo oricine te poate ataca si jefui.</li><li>Culegi <b>Pastaie de mac</b>.</li><li>La masa de procesare de langa plantatie faci <b>Plic heroina</b> din pastai, kerosen si plicuri goale.</li><li class="use">Consumi plicul din inventar.</li></ol><p class="bad"><b>Bad trip:</b> prima doza are risc mic, dar fiecare doza luata cat inca esti sub efect il creste.</p></div>
</article>
<article class="vdr-sheet" id="lsd" style="--c: var(--lsd)">
<div class="fx"><span class="it">Timbru LSD</span><h3>LSD</h3><span class="big">Lucrezi mai repede</span><span class="bigl">la mesele de iarba, de metamfetamina, de tigari si de LSD</span><span class="dur">10 min</span><p class="vis">Cele mai puternice halucinatii din joc: culori distorsionate, imagine care respira.</p></div>
<div class="how"><span class="k">Cum il obtii</span><ol class="vdr-chain"><li>Strangi <b>ciuperci halucinogene</b> cu <a href="/joburi/ciupercar">jobul de ciupercar</a>.</li><li>La o ferma din Grapeseed le faci <b>Plic halucinogene</b>.</li><li>Din plicuri, <b>Hartie</b> si <b>Bicarbonat de sodiu</b> scoti <b>Timbru LSD</b>.</li><li class="use">Consumi timbrul din inventar.</li></ol><p class="bad"><b>Bad trip:</b> cel mai mare risc. Uneori intri in panica: in jurul tau apar siluete care alearga spre tine si tipa, iar tu te ghemuiesti.</p></div>
</article>
</div>
<h2 class="vdr-h2" id="riscuri"><span>03</span>Riscuri</h2>
<div class="vdr-two">
<div class="vdr-card">
<h3 class="vdr-h3">Bad trip</h3>
<p>Imediat dupa doza poti avea un bad trip: un mesaj ca te simti ciudat, apoi cateva secunde de halucinatii. Riscul creste cu cat ai mai mult din acel drog in corp.</p>
</div>
<div class="vdr-card">
<h3 class="vdr-h3">Durere in piept</h3>
<p>Dupa fiecare doza de metamfetamina, cocaina, heroina sau LSD, uneori simti o durere in piept si pierzi putina viata.</p>
</div>
</div>
<div class="vdr-od" style="margin-top: 0.8rem">
<div class="hd">
<h3 class="vdr-h3">Supradoza</h3>
<p>Metamfetamina, cocaina, heroina si LSD se aduna in corp. Peste un prag, fiecare doza noua poate declansa o supradoza. Iarba si alcoolul nu intra in calcul.</p>
<ul class="vdr-weights" aria-label="Cat de mult impinge fiecare drog spre supradoza">
<li style="--c: var(--hero)"><span>Heroina</span><span class="bar"><i style="width: 100%"></i></span></li>
<li style="--c: var(--coke)"><span>Cocaina</span><span class="bar"><i style="width: 92%"></i></span></li>
<li style="--c: var(--meth)"><span>Metamfetamina</span><span class="bar"><i style="width: 77%"></i></span></li>
<li style="--c: var(--lsd)"><span>LSD</span><span class="bar"><i style="width: 62%"></i></span></li>
</ul>
</div>
<ol>
<li><span class="t">Declansare</span>Primesti mesajul ca ai luat supradoza si cazi la pamant.</li>
<li><span class="t">5 minute</span>Nu te poti ridica, viata iti scade si ecranul se inchide din cand in cand.</li>
<li><span class="t">NARCAN</span>Doar un medic iti poate da NARCAN, de langa tine. Supradoza se opreste pe loc si te ridici.</li>
<li><span class="t">Fara ajutor</span>Daca trec cele 5 minute si nu te-a tratat nimeni, mori.</li>
</ol>
</div>
<div class="vdr-two" style="margin-top: 0.8rem">
<div class="vdr-card">
<h3 class="vdr-h3">Ce vede politia</h3>
<p>Politistii au un test de droguri. Testul arata fiecare substanta din corpul tau, chiar daca bonusul s-a terminat, pana cand se elimina de tot. Si medicii pot vedea ce substante ai.</p>
</div>
<div class="vdr-card">
<h3 class="vdr-h3">Cum scazi riscul</h3>
<p>Lasa efectul unui drog sa treaca inainte de urmatoarea doza si nu amesteca drogurile. Daca tot exagerezi, ai grija sa fie un medic prin preajma.</p>
</div>
</div>
<h2 class="vdr-h2" id="livrari"><span>04</span>Livrari</h2>
<p class="vdr-sub">Drogurile se vand prin livrari la clienti. Pornesti din meniul rapid, iar fiecare marfa are cartierul ei si un minim de ore jucate.</p>
<div class="vdr-route"><span><kbd>K</kbd>&nbsp;Meniu rapid</span><span>Job</span><span>Livrari ilegale</span><span>Incepe livrari ...</span></div>
<ul class="vdr-drops">
<li style="--c: var(--lsd)"><span class="p">Timbru LSD</span><span class="h">50<small>ore</small></span><span class="z">Mirror Park &amp; Amarillo</span></li>
<li style="--c: var(--brass)"><span class="p">Pachet tigari</span><span class="h">75<small>ore</small></span><span class="z">Mirror Park &amp; Amarillo</span></li>
<li style="--c: var(--weed)"><span class="p">Plic de iarba</span><span class="h">150<small>ore</small></span><span class="z">Vinewood</span></li>
<li style="--c: var(--meth)"><span class="p">Plic metamfetamina</span><span class="h">300<small>ore</small></span><span class="z">Vespucci</span></li>
<li style="--c: var(--hero)"><span class="p">Plic heroina</span><span class="h">350<small>ore</small></span><span class="z">Sandy Shores</span></li>
<li style="--c: var(--coke)"><span class="p">Plic coca</span><span class="h">500<small>ore</small></span><span class="z">Grove Street</span></li>
</ul>
<ul class="vdr-ticks" style="margin-top: 0.9rem">
<li>Primesti o comanda cu o destinatie. Mergi acolo si predai marfa clientului. Plata vine in <b>bani murdari</b>.</li>
<li>Nu poti preda din masina.</li>
<li>Cand pornesti, afli daca la ora aceea livrarile au bonus sau penalizare.</li>
<li>Daca familia ta tine teritoriul cartierului, primesti in plus. Vezi <a href="/viata-ilegala/sistem-teritorial#cele-8-teritorii">Teritorii &amp; Razboaie</a>.</li>
<li>Politistii si medicii nu pot face livrari. Te opresti din meniul <b>Job</b>, cu <b>Opreste livrari</b>.</li>
</ul>
<h2 class="vdr-h2" id="alte-substante"><span>05</span>Alte substante</h2>
<ul class="vdr-other">
<li><span class="tag">Farmacie</span><h3 class="vdr-h3">Adrenalina</h3><p>Nu e un drog, e un kit de lupta. Timp de 10 minute:</p><ul class="vdr-ticks"><li>iti reface treptat <b>75 de viata</b>;</li><li>alergi mai repede;</li><li>nu simti ranile: piciorul rupt, tusea, voma, sangerarea, vederea incetosata si mainile ranite.</li></ul></li>
<li><span class="tag">Bautura</span><h3 class="vdr-h3">Alcool</h3><p>Berea, whisky-ul si vodca urca alcoolemia in promile. Scade singura in timp.</p><ul class="vdr-promil"><li><b>0.2</b><span>Ametit usor, imagine putin incetosata.</span></li><li><b>0.8</b><span>Camera se clatina.</span></li><li><b>1.0</b><span>Poti vomita.</span></li><li><b>1.5</b><span>Mers de om beat, cazi din picioare, masina trage singura de volan.</span></li><li><b>2.0</b><span>Pierzi viata.</span></li><li><b>2.5</b><span>Lesini: ecranul se face negru.</span></li></ul></li>
<li><span class="tag">Sala</span><h3 class="vdr-h3">Steroizi si dependenta</h3><p>Steroizii de la <a href="/general/sala">sala</a> sunt singurul produs care da dependenta. Dupa 5 folosiri incepi sa devii dependent.</p><ul class="vdr-ticks"><li>Cat esti dependent si nu esti sub efect: ecran care tremura, oboseala, filtru rosu.</li><li>La dependenta mare pierzi viata in fiecare ora.</li><li>Scapi doar daca nu mai iei: dependenta scade singura in timp.</li></ul></li>
</ul>
</div>
