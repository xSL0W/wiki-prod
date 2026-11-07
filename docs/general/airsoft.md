---
title: Airsoft
outline: false
---

<style>
.as {
  --ink: #09090b;
  --panel: #151518;
  --panel2: #1c1c20;
  --line: #2c2c33;
  --text: #f4f4f5;
  --mute: #a1a1aa;
  --red: #ef4444;
  --red-deep: #b91c1c;
  --red-soft: rgba(239, 68, 68, 0.14);
  --blue: #3b82f6;
  --blue-soft: rgba(59, 130, 246, 0.14);
  --hud: #a3e635;
  --hud-soft: rgba(163, 230, 53, 0.12);
  max-width: 940px;
  margin: 0 auto;
  color: var(--text);
  font-family: Inter, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.as *, .as *::before, .as *::after { box-sizing: border-box; }
.as p, .as li { line-height: 1.6; color: var(--text); margin: 0; }
.as ul, .as ol { list-style: none; padding: 0; margin: 0; }
.as li + li { margin-top: 0; }
.as b { color: #fff; font-weight: 650; }
.as code { white-space: normal; overflow-wrap: anywhere; }
.as a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.as a:focus-visible { outline: 3px solid var(--red); outline-offset: 3px; border-radius: 6px; }
.as kbd {
  font: inherit; font-size: 0.85em; font-weight: 700; color: var(--ink); background: var(--hud);
  border-radius: 6px; padding: 0.05rem 0.45rem;
}
/* ---------- hero: a scope over the arena ---------- */
.as .as-hero {
  position: relative; overflow: hidden; isolation: isolate;
  display: grid; grid-template-columns: minmax(0, 1.15fr) minmax(0, 1fr); gap: 1.2rem 2rem; align-items: center;
  background: radial-gradient(80% 110% at 100% 0%, rgba(59, 130, 246, 0.14), transparent 60%),
              radial-gradient(90% 120% at 0% 100%, rgba(185, 28, 28, 0.28), var(--ink) 65%);
  border: 1px solid var(--line); border-radius: 22px;
  padding: clamp(1.15rem, 4vw, 2.3rem);
}
.as .as-kicker {
  font: 700 0.75rem/1.2 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace;
  letter-spacing: 0.18em; text-transform: uppercase; color: var(--hud); margin-bottom: 0.6rem;
}
.as .as-hero h1 {
  margin: 0 0 0.75rem; border: 0; padding: 0;
  font-size: clamp(2.3rem, 7vw, 3.8rem); line-height: 1; font-weight: 850; letter-spacing: -0.035em; color: #fff;
}
.as .as-hero h1 span { color: var(--red); }
.as .as-lede { color: var(--mute); font-size: 1.04rem; max-width: 52ch; }
.as .as-chips { display: flex; flex-wrap: wrap; gap: 0.45rem; margin-top: 1rem; }
.as .as-chips li {
  font: 700 0.75rem/1 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; letter-spacing: 0.06em;
  border: 1px solid var(--line); background: rgba(9, 9, 11, 0.6); border-radius: 999px; padding: 0.45rem 0.7rem; color: var(--text);
}
.as .as-chips li i { font-style: normal; color: var(--hud); }
.as .as-scope { display: block; width: 100%; max-width: 360px; height: auto; margin: 0 auto; }
.as-scope .ring { fill: none; stroke: #3f3f46; stroke-width: 1.5; }
.as-scope .ring.outer { stroke: var(--hud); stroke-width: 2; opacity: 0.7; }
.as-scope .tick { stroke: var(--hud); stroke-width: 2; opacity: 0.8; }
.as-scope .hair { stroke: var(--hud); stroke-width: 1; opacity: 0.45; }
.as-scope .lens { fill: #0c0f0a; }
.as-scope .sweep { fill: url(#as-sweep-grad); transform-origin: 160px 160px; animation: as-spin 6s linear infinite; }
.as-scope .dot { transform-box: fill-box; transform-origin: center; animation: as-ping 6s ease-out infinite; opacity: 0.25; }
.as-scope .dot.r { fill: var(--red); }
.as-scope .dot.b { fill: var(--blue); }
.as-scope .dot.d1 { animation-delay: 0.6s; }
.as-scope .dot.d2 { animation-delay: 1.9s; }
.as-scope .dot.d3 { animation-delay: 2.7s; }
.as-scope .dot.d4 { animation-delay: 3.8s; }
.as-scope .dot.d5 { animation-delay: 4.6s; }
.as-scope .dot.d6 { animation-delay: 5.3s; }
.as-scope .center { fill: var(--red); }
@keyframes as-spin { to { transform: rotate(360deg); } }
@keyframes as-ping { 0% { opacity: 1; transform: scale(1.5); } 30% { opacity: 0.7; transform: scale(1); } 100% { opacity: 0.2; transform: scale(1); } }
/* kill feed ticker under the scope */
.as .as-feed { grid-column: 1 / -1; display: grid; gap: 0.35rem; justify-items: end; }
.as .as-feed li {
  grid-area: 1 / 1; display: flex; align-items: center; gap: 0.5rem; flex-wrap: wrap; justify-content: flex-end;
  font: 600 0.82rem/1.2 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace;
  background: rgba(9, 9, 11, 0.75); border: 1px solid var(--line); border-radius: 8px; padding: 0.35rem 0.65rem;
  opacity: 0; animation: as-feed 9s ease-in-out infinite;
}
.as .as-feed li:nth-child(2) { animation-delay: 3s; }
.as .as-feed li:nth-child(3) { animation-delay: 6s; }
.as .as-feed .r { color: #fca5a5; }
.as .as-feed .b { color: #93c5fd; }
.as .as-feed .w { color: var(--mute); }
@keyframes as-feed { 0% { opacity: 0; transform: translateX(14px); } 6%, 30% { opacity: 1; transform: none; } 38%, 100% { opacity: 0; transform: none; } }
@media (max-width: 720px) {
  .as .as-hero { grid-template-columns: minmax(0, 1fr); }
  .as .as-feed { justify-items: stretch; }
}
@media (prefers-reduced-motion: reduce) {
  .as-scope .sweep, .as-scope .dot, .as .as-feed li { animation: none; }
  .as-scope .dot, .as .as-feed li:first-child { opacity: 1; }
}
/* ---------- sections ---------- */
.as h2 {
  display: flex; align-items: center; gap: 0.65rem;
  margin: 3rem 0 1rem; border: 0; padding: 0;
  font-size: 1.5rem; font-weight: 750; letter-spacing: -0.015em; color: #fff;
}
.as h2::before {
  content: ''; flex: none; width: 16px; height: 16px; border-radius: 50%;
  border: 2px solid var(--hud); box-shadow: inset 0 0 0 4px var(--ink), inset 0 0 0 8px var(--hud);
}
.as h3 { margin: 0; border: 0; padding: 0; color: #fff; }
.as .as-lead { max-width: 66ch; color: var(--text); }
.as .as-lead + .as-lead { margin-top: 0.8rem; }
/* steps: how you get into a match */
.as .as-steps { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 200px), 1fr)); gap: 0.8rem; counter-reset: as-step; }
.as .as-steps li {
  position: relative; background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 1rem 1.05rem 1.05rem;
  counter-increment: as-step;
}
.as .as-steps li::before {
  content: counter(as-step, decimal-leading-zero);
  display: block; margin-bottom: 0.4rem;
  font: 800 1.5rem/1 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; color: var(--hud);
}
.as .as-steps h3 { font-size: 1.02rem; margin-bottom: 0.3rem; }
.as .as-steps p { color: var(--mute); font-size: 0.93rem; }
/* lobby cards */
.as .as-lobby { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr)); gap: 0.9rem; }
.as .as-card { background: var(--panel); border: 1px solid var(--line); border-radius: 18px; padding: 1.15rem 1.25rem; }
.as .as-card h3 { font-size: 1.1rem; margin-bottom: 0.15rem; }
.as .as-card .as-tag { display: block; font: 700 0.72rem/1.3 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; letter-spacing: 0.1em; text-transform: uppercase; color: var(--mute); margin-bottom: 0.65rem; min-height: 2.6em; }
.as .as-card .as-list li { position: relative; padding: 0.3rem 0 0.3rem 1.1rem; color: var(--text); font-size: 0.94rem; line-height: 1.45; }
.as .as-card .as-list li + li { border-top: 1px solid var(--line); }
.as .as-card .as-list li::before { content: ''; position: absolute; left: 0; top: 0.78rem; width: 6px; height: 6px; background: var(--hud); }
.as .as-card.pub { border-top: 3px solid var(--hud); }
.as .as-card.priv { border-top: 3px solid var(--red); }
/* modes */
.as .as-modes { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 250px), 1fr)); gap: 0.9rem; }
.as .as-mode { position: relative; overflow: hidden; background: var(--panel); border: 1px solid var(--line); border-radius: 18px; padding: 1.2rem 1.25rem; }
.as .as-mode svg { width: 40px; height: 40px; display: block; margin-bottom: 0.6rem; }
.as .as-mode h3 { font-size: 1.15rem; }
.as .as-mode .as-sub { font: 700 0.72rem/1.3 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; letter-spacing: 0.1em; text-transform: uppercase; color: var(--hud); margin: 0.15rem 0 0.6rem; }
.as .as-mode p { color: var(--mute); font-size: 0.94rem; }
.as .as-mode p + p { margin-top: 0.5rem; }
.as .as-mode.tdm { background: linear-gradient(115deg, rgba(239, 68, 68, 0.12), var(--panel) 45%, var(--panel) 55%, rgba(59, 130, 246, 0.12)); }
.as .as-mode .as-win { margin-top: 0.8rem; padding-top: 0.7rem; border-top: 1px dashed var(--line); color: var(--text); font-size: 0.92rem; }
.as .as-mode .as-win b { color: var(--hud); }
/* vote */
.as .as-vote { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 200px), 1fr)); gap: 0.7rem; }
.as .as-vote li { background: var(--panel2); border: 1px solid var(--line); border-radius: 14px; padding: 0.85rem 1rem; }
.as .as-vote h3 { font-size: 1rem; margin-bottom: 0.25rem; }
.as .as-vote p { color: var(--mute); font-size: 0.9rem; }
/* maps */
.as .as-maps { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 200px), 1fr)); gap: 0.7rem; }
.as .as-maps li {
  background:
    linear-gradient(var(--panel), var(--panel)) padding-box,
    linear-gradient(135deg, #3f3f46, var(--line)) border-box;
  border: 1px solid transparent; border-radius: 14px; padding: 0.9rem 1rem;
}
.as .as-maps .nm { display: block; font: 750 1rem/1.2 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; color: #fff; }
.as .as-maps .ds { display: block; margin-top: 0.3rem; color: var(--mute); font-size: 0.88rem; line-height: 1.45; }
.as .as-maps .sz { display: flex; align-items: center; gap: 0.4rem; margin-top: 0.6rem; font-size: 0.75rem; color: var(--mute); text-transform: uppercase; letter-spacing: 0.08em; }
.as .as-maps .bar { display: inline-flex; gap: 3px; }
.as .as-maps .bar i { width: 14px; height: 6px; border-radius: 2px; background: #2f2f36; }
.as .as-maps .s1 .bar i:nth-child(-n+1),
.as .as-maps .s2 .bar i:nth-child(-n+2),
.as .as-maps .s3 .bar i:nth-child(-n+3) { background: var(--hud); }
/* rules as HUD readouts */
.as .as-hud { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 170px), 1fr)); gap: 0.7rem; }
.as .as-hud li { background: #0d0f0b; border: 1px solid #27301b; border-radius: 14px; padding: 0.9rem 1rem; }
.as .as-hud .v { display: block; font: 800 1.7rem/1 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; color: var(--hud); }
.as .as-hud .k { display: block; margin-top: 0.45rem; font-size: 0.9rem; line-height: 1.4; color: var(--text); }
.as .as-rules { margin-top: 0.9rem; display: grid; gap: 0.5rem; }
.as .as-rules li { position: relative; padding: 0.7rem 0.9rem 0.7rem 2.4rem; background: var(--panel); border: 1px solid var(--line); border-radius: 12px; font-size: 0.95rem; }
.as .as-rules li::before {
  content: ''; position: absolute; left: 0.9rem; top: 1.05rem; width: 10px; height: 10px; border-radius: 50%;
  border: 2px solid var(--hud);
}
.as .as-rules li.warn::before { border-color: var(--red); background: var(--red-soft); }
/* keys */
.as .as-keys { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 240px), 1fr)); gap: 0.7rem; }
.as .as-keys li { display: flex; gap: 0.8rem; align-items: flex-start; background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 0.85rem 1rem; }
.as .as-keys kbd { flex: none; min-width: 2.1rem; text-align: center; font-size: 1rem; padding: 0.3rem 0.5rem; }
.as .as-keys p { font-size: 0.93rem; color: var(--mute); }
.as .as-keys p b { color: #fff; }
.as .as-keys p b:first-child { display: block; }
/* reward */
.as .as-reward {
  border: 1px solid #3a2a12; border-radius: 18px; padding: 1.2rem 1.3rem;
  background: radial-gradient(90% 140% at 0% 0%, rgba(245, 185, 49, 0.12), var(--panel) 60%);
}
.as .as-reward .as-list li { position: relative; padding: 0.45rem 0 0.45rem 1.4rem; font-size: 0.95rem; line-height: 1.5; }
.as .as-reward .as-list li + li { border-top: 1px solid var(--line); }
.as .as-reward .as-list li::before { content: ''; position: absolute; left: 0; top: 0.95rem; width: 9px; height: 9px; border-radius: 2px; background: #f5b931; transform: rotate(45deg); }
.as .as-reward .as-list li.no::before { background: var(--red); transform: none; border-radius: 50%; }
.as .as-reward h3 { font-size: 1.05rem; margin-bottom: 0.4rem; }
.as .as-reward h3 + .as-list { margin-bottom: 0.9rem; }
</style>

<div class="as">

<section class="as-hero">
<div>
<div class="as-kicker">Locatii / arena</div>
<h1>Air<span>soft</span></h1>
<p class="as-lede">Meciuri de tras cu prietenii sau cu oricine e pe server, intr-o arena separata de oras. Iti faci lobby-ul, votati harta si modul de joc, iar castigatorul ia recompensa in banca.</p>
<ul class="as-chips">
<li><i>3</i> moduri</li>
<li><i>7</i> harti</li>
<li><i>15</i> min / meci</li>
<li>pana la <i>32</i> jucatori</li>
</ul>
</div>
<svg class="as-scope" viewBox="0 0 320 320" role="img" aria-label="Luneta peste arena, cu jucatori din echipa rosie si echipa albastra">
<defs>
<radialGradient id="as-lens-grad" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#141a10"/><stop offset="100%" stop-color="#07080a"/></radialGradient>
<linearGradient id="as-sweep-grad" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#a3e635" stop-opacity="0"/><stop offset="100%" stop-color="#a3e635" stop-opacity="0.32"/></linearGradient>
</defs>
<circle cx="160" cy="160" r="150" fill="url(#as-lens-grad)"/>
<path class="sweep" d="M160 160 L160 12 A148 148 0 0 1 264.6 55.4 Z"/>
<circle class="ring" cx="160" cy="160" r="110"/>
<circle class="ring" cx="160" cy="160" r="70"/>
<circle class="ring" cx="160" cy="160" r="30"/>
<line class="hair" x1="10" y1="160" x2="310" y2="160"/>
<line class="hair" x1="160" y1="10" x2="160" y2="310"/>
<line class="tick" x1="10" y1="160" x2="40" y2="160"/>
<line class="tick" x1="280" y1="160" x2="310" y2="160"/>
<line class="tick" x1="160" y1="10" x2="160" y2="40"/>
<line class="tick" x1="160" y1="280" x2="160" y2="310"/>
<circle class="dot r d1" cx="214" cy="86" r="6"/>
<circle class="dot b d2" cx="246" cy="196" r="6"/>
<circle class="dot r d3" cx="118" cy="232" r="6"/>
<circle class="dot b d4" cx="78" cy="122" r="6"/>
<circle class="dot r d5" cx="190" cy="250" r="6"/>
<circle class="dot b d6" cx="120" cy="70" r="6"/>
<circle class="center" cx="160" cy="160" r="3"/>
<circle class="ring outer" cx="160" cy="160" r="150"/>
</svg>
<ul class="as-feed" aria-hidden="true">
<li><span class="r">Andrei</span><span class="w">M4A4</span><span class="b">Vlad</span></li>
<li><span class="b">Ioana</span><span class="w">Deagle</span><span class="r">Mihai</span></li>
<li><span class="r">Radu</span><span class="w">AK-47</span><span class="b">Cristi</span></li>
</ul>
</section>

<h2>Unde gasesti arena</h2>
<p class="as-lead">Cauta pe harta blipul <b>Airsoft</b>. Acolo te asteapta <b>instructorul de airsoft</b>. Apropie-te de el si apasa <kbd>E</kbd>: din meniul lui iti faci un lobby sau intri in unul existent.</p>
<p class="as-lead">Nu poti intra cat timp esti ranit, incatusat sau inchis. Esti intr-un singur lobby o data.</p>

<h2>De la lobby la meci</h2>
<ol class="as-steps">
<li><h3>Lobby</h3><p>Creezi un lobby sau intri in unul. Cel care il creeaza e liderul si porneste meciul cand sunt minim 2 jucatori.</p></li>
<li><h3>Vot de 15 secunde</h3><p>Toti din lobby voteaza harta, modul de joc si daca jucati cu armura sau fara.</p></li>
<li><h3>Echipe</h3><p>Doar la Team Deathmatch: echipele se fac automat sau le aranjeaza liderul (la lobby privat).</p></li>
<li><h3>Meci de 15 minute</h3><p>Esti dus in arena cu armele meciului. La final te intorci langa instructor.</p></li>
</ol>

<h2>Lobby public sau privat</h2>
<div class="as-lobby">
<div class="as-card pub">
<h3>Lobby public</h3>
<span class="as-tag">Instructor → Alatura-te unui lobby → Lobby-uri publice</span>
<ul class="as-list">
<li>Apare in lista oricui vorbeste cu instructorul.</li>
<li>Poti intra si dupa ce meciul a inceput: esti bagat direct in arena (la Team Deathmatch, in echipa cu mai putini jucatori).</li>
</ul>
</div>
<div class="as-card priv">
<h3>Lobby privat</h3>
<span class="as-tag">Instructor → Alatura-te unui lobby → Intra cu PIN</span>
<ul class="as-list">
<li>Il faci cu un PIN de 4 cifre, pe care il dai doar prietenilor.</li>
<li>Se poate intra doar inainte de start.</li>
<li>La Team Deathmatch, liderul alege cine joaca in fiecare echipa.</li>
<li>Liderul poate incheia meciul oricand, pentru toti (fara recompensa).</li>
</ul>
</div>
</div>
<ul class="as-rules">
<li>Un lobby are cel mult <b>32 de jucatori</b>, iar pe server pot exista cel mult <b>20 de lobby-uri</b> in acelasi timp.</li>
<li>Inainte de start, liderul poate da afara un jucator din lobby. Daca liderul pleaca, cel mai vechi membru ramas devine lider.</li>
</ul>

<h2>Votul</h2>
<ul class="as-vote">
<li><h3>Harta</h3><p>Castiga harta cu cele mai multe voturi. Daca nu voteaza nimeni, harta se alege la intamplare.</p></li>
<li><h3>Mod de joc</h3><p>Poti vota doar modurile pentru care sunt destui jucatori. Fara voturi, modul se alege la intamplare.</p></li>
<li><h3>Armura</h3><p>Cu armura, primesti armura plina la fiecare spawn. La egalitate (sau fara voturi) decide norocul.</p></li>
</ul>

<h2>Moduri de joc</h2>
<div class="as-modes">
<div class="as-mode">
<svg viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="20" r="15" fill="none" stroke="#a3e635" stroke-width="2.5"/><circle cx="20" cy="20" r="3" fill="#ef4444"/><path d="M20 2v9M20 29v9M2 20h9M29 20h9" stroke="#a3e635" stroke-width="2.5"/></svg>
<h3>Free For All</h3>
<div class="as-sub">Minim 2 jucatori</div>
<p>Toti contra tuturor. Fiecare joaca pe cont propriu.</p>
<p class="as-win"><b>Castiga:</b> jucatorul cu cele mai multe ucideri la final.</p>
</div>
<div class="as-mode tdm">
<svg viewBox="0 0 40 40" aria-hidden="true"><circle cx="13" cy="13" r="6" fill="#ef4444"/><path d="M3 34c0-6 4.5-10 10-10s10 4 10 10z" fill="#ef4444"/><circle cx="27" cy="13" r="6" fill="#3b82f6"/><path d="M17 34c0-6 4.5-10 10-10s10 4 10 10z" fill="#3b82f6"/></svg>
<h3>Team Deathmatch</h3>
<div class="as-sub">Minim 4 jucatori</div>
<p>Echipa Rosie contra Echipa Albastra, fiecare cu uniforma ei. In lobby-ul public echipele se impart la intamplare, jumatate-jumatate. In lobby-ul privat liderul le aranjeaza in 2 minute, altfel se impart la intamplare.</p>
<p>Daca ucizi un coechipier pierzi o ucidere. La al treilea coechipier ucis esti scos din meci.</p>
<p class="as-win"><b>Castiga:</b> echipa cu cele mai multe ucideri. Toti membrii ei primesc recompensa.</p>
</div>
<div class="as-mode">
<svg viewBox="0 0 40 40" aria-hidden="true"><path d="M4 26h8v8H4zM16 18h8v16h-8zM28 8h8v26h-8z" fill="#a3e635"/><path d="M6 18 18 8l4 4 10-9" fill="none" stroke="#ef4444" stroke-width="2.5"/></svg>
<h3>Gun Game</h3>
<div class="as-sub">Minim 2 jucatori</div>
<p>Toti incep cu aceeasi arma. Dupa 3 ucideri treci la urmatoarea, prin 16 arme: de la pusti de asalt, la SMG-uri si pistoale.</p>
<p class="as-win"><b>Castiga:</b> primul care face 3 ucideri cu ultima arma. Meciul se termina pe loc.</p>
</div>
</div>

<h2>Hartile</h2>
<ul class="as-maps">
<li class="s1"><span class="nm">de_sandy</span><span class="ds">Sandy Shores: cladiri mici si strazi inguste, lupte rapide.</span><span class="sz">Mica <span class="bar"><i></i><i></i><i></i></span></span></li>
<li class="s2"><span class="nm">de_grove</span><span class="ds">Grove Street din GTA: San Andreas, strazi inguste si cladiri.</span><span class="sz">Medie <span class="bar"><i></i><i></i><i></i></span></span></li>
<li class="s2"><span class="nm">de_vista</span><span class="ds">Strada Amarillo Vista, cu case mici si o strada ingusta.</span><span class="sz">Medie <span class="bar"><i></i><i></i><i></i></span></span></li>
<li class="s2"><span class="nm">de_dust2</span><span class="ds">Clasica: doua baze fata in fata si un drum prin mijloc.</span><span class="sz">Medie <span class="bar"><i></i><i></i><i></i></span></span></li>
<li class="s2"><span class="nm">de_poppy</span><span class="ds">Plantatia de mac.</span><span class="sz">Mica / medie <span class="bar"><i></i><i></i><i></i></span></span></li>
<li class="s3"><span class="nm">de_humanelabs</span><span class="ds">Humane Labs, una dintre cele mai cerute zone de bataie.</span><span class="sz">Mare <span class="bar"><i></i><i></i><i></i></span></span></li>
<li class="s3"><span class="nm">de_petrol_refinery</span><span class="ds">Rafinaria de petrol.</span><span class="sz">Mare <span class="bar"><i></i><i></i><i></i></span></span></li>
</ul>

<h2>In meci</h2>
<ul class="as-hud">
<li><span class="v">15:00</span><span class="k">dureaza un meci</span></li>
<li><span class="v">5s</span><span class="k">pana reapari dupa ce mori</span></li>
<li><span class="v">5s</span><span class="k">de protectie dupa fiecare spawn</span></li>
<li><span class="v">10s</span><span class="k">ca sa te intorci daca iesi din zona hartii</span></li>
</ul>
<ul class="as-rules">
<li>Armele sunt ale meciului: la fiecare meci se alege un set nou de pusti, SMG-uri, pistoale si o grenada sau un molotov, cu accesorii. Le primesti din nou la fiecare spawn.</li>
<li>Uciderea o primeste ultimul jucator care te-a lovit inainte sa mori.</li>
<li>Inventarul tau e blocat cat timp esti in meci: nu poti scoate nimic din el.</li>
<li class="warn">Daca iesi din zona hartii ai 10 secunde sa te intorci, altfel reapari in alt loc.</li>
<li class="warn">Cu 5 secunde inainte de final ti se iau armele. Dupa meci te intorci langa instructor, cu armura pe care o aveai inainte.</li>
<li>La final primesti in notificare uciderile, mortile si K/D-ul tau.</li>
</ul>

<h2>Taste</h2>
<ul class="as-keys">
<li><kbd>E</kbd><p><b>Instructorul</b>Deschide meniul de airsoft.</p></li>
<li><kbd>F</kbd><p><b>Clasament</b>Tine apasat ca sa vezi uciderile, mortile si K/D-ul fiecaruia.</p></li>
<li><kbd>L</kbd><p><b>Clasament fixat</b>Ramane deschis cu mouse-ul: de aici apesi <b>Paraseste meciul</b>.</p></li>
</ul>

<h2>Recompensa</h2>
<div class="as-reward">
<h3>Cine primeste bani in banca</h3>
<ul class="as-list">
<li><b>Free For All:</b> jucatorul cu cele mai multe ucideri. Trebuie sa aiba minimul de ucideri cerut, altfel nu castiga nimeni.</li>
<li><b>Team Deathmatch:</b> fiecare membru al echipei castigatoare. Un meci fara ucideri nu are castigator.</li>
<li><b>Gun Game:</b> cel care termina ultima arma.</li>
</ul>
<h3>Cand nu se plateste nimic</h3>
<ul class="as-list">
<li class="no">Daca raman prea putini jucatori in arena, meciul se opreste fara recompensa.</li>
<li class="no">Daca liderul unui lobby privat incheie meciul.</li>
<li class="no">Daca parasesti meciul inainte de final.</li>
</ul>
</div>

</div>
