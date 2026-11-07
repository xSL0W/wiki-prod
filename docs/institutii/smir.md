---
outline: false
---

<style>
.smr {
  --ink: #0a0607;
  --panel: #161012;
  --panel2: #1e1618;
  --line: #34262a;
  --text: #f6eff0;
  --mute: #b0a2a5;
  --red: #ef4444;
  --red-deep: #b91c1c;
  --red-soft: rgba(239, 68, 68, 0.14);
  --ecg: #4ade80;
  --ecg-soft: rgba(74, 222, 128, 0.14);
  max-width: 960px;
  margin: 0 auto;
  color: var(--text);
  font-family: Inter, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.smr *, .smr *::before, .smr *::after { box-sizing: border-box; }
.smr p, .smr li { line-height: 1.6; color: var(--text); margin: 0; }
.smr ul, .smr ol { list-style: none; padding: 0; margin: 0; }
.smr li + li { margin-top: 0; }
.smr b { color: #fff; font-weight: 650; }
.smr code { white-space: normal; overflow-wrap: anywhere; }
.smr a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.smr a:hover { color: #fecaca; }
.smr a:focus-visible { outline: 3px solid var(--red); outline-offset: 3px; border-radius: 6px; }
.smr kbd {
  font: inherit; font-size: 0.85em; font-weight: 700; color: #fff; background: var(--red-deep);
  border-radius: 6px; padding: 0.05rem 0.45rem; white-space: nowrap;
}
/* ---------- hero: patient monitor with a live ECG trace, ambulance lights on top ---------- */
.smr .smr-hero {
  position: relative; overflow: hidden; isolation: isolate;
  background: radial-gradient(110% 130% at 0% 100%, rgba(185, 28, 28, 0.28), var(--ink) 62%);
  border: 1px solid var(--line); border-radius: 22px;
  padding: clamp(1.15rem, 4vw, 2.4rem);
}
.smr .smr-lights { position: absolute; top: 0; left: 0; right: 0; height: 4px; display: grid; grid-template-columns: 1fr 1fr; }
.smr .smr-lights span:first-child { background: var(--red); animation: smr-flash 1.2s steps(1, end) infinite; }
.smr .smr-lights span:last-child { background: #fff; animation: smr-flash 1.2s steps(1, end) -0.6s infinite; }
@keyframes smr-flash { 0%, 16%, 32% { opacity: 1; } 8%, 24%, 40%, 100% { opacity: 0.12; } }
.smr .smr-top { display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: 1.2rem; align-items: center; }
.smr .smr-kicker { font-size: 0.78rem; font-weight: 700; letter-spacing: 0.16em; text-transform: uppercase; color: var(--red); margin-bottom: 0.55rem; }
.smr .smr-hero h1 {
  margin: 0 0 0.75rem; border: 0; padding: 0;
  font-size: clamp(2rem, 6.4vw, 3.4rem); line-height: 1.04; font-weight: 800; letter-spacing: -0.03em; color: #fff;
}
.smr .smr-hero h1 span { color: var(--red); }
.smr .smr-lede { max-width: 56ch; color: var(--mute); font-size: 1.05rem; }
.smr .smr-cross { width: clamp(84px, 16vw, 128px); height: auto; display: block; }
.smr-cross .bg { fill: #1c1113; stroke: var(--line); stroke-width: 2; }
.smr-cross .plus { fill: var(--red); transform-box: fill-box; transform-origin: center; animation: smr-beat 1.6s ease-in-out infinite; }
.smr-cross .ring { fill: none; stroke: var(--red); stroke-width: 2; opacity: 0; transform-box: fill-box; transform-origin: center; animation: smr-ring 1.6s ease-out infinite; }
@keyframes smr-beat { 0%, 30%, 100% { transform: scale(1); } 10% { transform: scale(1.1); } 20% { transform: scale(0.97); } }
@keyframes smr-ring { 0% { opacity: 0.8; transform: scale(0.75); } 60%, 100% { opacity: 0; transform: scale(1.25); } }
.smr .smr-monitor { display: block; width: 100%; height: auto; margin-top: 1.3rem; border-radius: 14px; background: #070b08; border: 1px solid #1d2a20; }
.smr-monitor .grid { stroke: #12241a; stroke-width: 1; }
.smr-monitor .trace { fill: none; stroke: var(--ecg); stroke-width: 2.5; stroke-linejoin: round; stroke-linecap: round; }
.smr-monitor .wipe { transform-box: fill-box; transform-origin: left center; animation: smr-wipe 3.2s linear infinite; }
.smr-monitor .head { fill: #d9ffe6; animation: smr-head 3.2s linear infinite; }
.smr-monitor .lbl { fill: var(--ecg); font: 700 11px ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; letter-spacing: 0.1em; }
.smr-monitor .lbl.dim { fill: #4b7a5b; }
@keyframes smr-wipe { 0% { transform: scaleX(0); } 92%, 100% { transform: scaleX(1); } }
@keyframes smr-head { 0% { transform: translateX(0); } 92%, 100% { transform: translateX(640px); } }
.smr .smr-stats { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 0.6rem; margin-top: 1.2rem; }
.smr .smr-stats li { background: rgba(22, 16, 18, 0.88); border: 1px solid var(--line); border-radius: 14px; padding: 0.7rem 0.9rem; }
.smr .smr-stats b { display: block; font-size: clamp(1.35rem, 4vw, 1.8rem); line-height: 1.1; font-weight: 800; color: #fff; font-variant-numeric: tabular-nums; }
.smr .smr-stats span { display: block; color: var(--mute); font-size: 0.82rem; line-height: 1.35; margin-top: 0.2rem; }
@media (max-width: 560px) {
  .smr .smr-top { grid-template-columns: minmax(0, 1fr); }
  .smr .smr-cross { display: none; }
  .smr .smr-stats { grid-template-columns: minmax(0, 1fr); }
}
@media (prefers-reduced-motion: reduce) {
  .smr .smr-lights span, .smr-cross .plus, .smr-cross .ring, .smr-monitor .wipe, .smr-monitor .head { animation: none; }
  .smr .smr-lights span { opacity: 1; }
  .smr-monitor .wipe { transform: none; }
  .smr-monitor .head { display: none; }
}
/* ---------- sections ---------- */
.smr .smr-h2 {
  display: flex; align-items: flex-start; gap: 0.65rem;
  margin: 3rem 0 0.9rem; border: 0; padding: 0;
  font-size: 1.5rem; font-weight: 750; letter-spacing: -0.015em; line-height: 1.25; color: #fff;
}
.smr .smr-h2::before { margin-top: calc(0.5lh - 0.8rem / 2);
  content: ''; flex: none; width: 0.8rem; height: 0.8rem;
  background: linear-gradient(var(--red), var(--red)) center / 100% 34% no-repeat, linear-gradient(var(--red), var(--red)) center / 34% 100% no-repeat;
}
.smr .smr-h3 { margin: 0 0 0.35rem; border: 0; padding: 0; font-size: 1.05rem; font-weight: 700; color: #fff; line-height: 1.3; }
.smr .smr-sub { color: var(--mute); max-width: 68ch; margin-bottom: 1rem; }
.smr .smr-card { background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 1.1rem 1.25rem; }
.smr .smr-card p { color: var(--mute); font-size: 0.96rem; }
.smr .smr-card p + p { margin-top: 0.5rem; }
.smr .smr-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr)); gap: 0.75rem; }
.smr .smr-list li { position: relative; padding-left: 1.1rem; color: var(--mute); font-size: 0.95rem; }
.smr .smr-list li + li { margin-top: 0.4rem; }
.smr .smr-list li::before { content: ''; position: absolute; left: 0; top: 0.62em; width: 6px; height: 6px; border-radius: 50%; background: var(--red); }
/* steps */
.smr .smr-road { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 210px), 1fr)); gap: 0.75rem; counter-reset: smr-step; }
.smr .smr-road li {
  position: relative; counter-increment: smr-step;
  background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 2.6rem 1.15rem 1.05rem;
}
.smr .smr-road li::before {
  content: counter(smr-step); position: absolute; top: 0.9rem; left: 1.15rem;
  width: 1.5rem; height: 1.5rem; border-radius: 50%; display: grid; place-items: center;
  font-size: 0.8rem; font-weight: 800; color: #fff; background: var(--red-deep);
}
.smr .smr-road p { color: var(--mute); font-size: 0.95rem; }
.smr .smr-check { margin-top: 0.75rem; border-left: 3px solid var(--ecg); background: linear-gradient(90deg, var(--ecg-soft), var(--panel) 40%); }
/* grade ladder */
.smr .smr-ladder { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 200px), 1fr)); gap: 0.5rem; counter-reset: smr-grade; }
.smr .smr-ladder li {
  counter-increment: smr-grade; display: flex; align-items: center; gap: 0.7rem;
  background: var(--panel); border: 1px solid var(--line); border-radius: 12px; padding: 0.6rem 0.8rem; font-weight: 650; color: #fff;
}
.smr .smr-ladder li::before {
  content: counter(smr-grade); flex: none; display: grid; place-items: center; width: 1.9rem; height: 1.9rem; border-radius: 8px;
  font: 800 0.9rem/1 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; color: #fca5a5; background: var(--red-soft);
}
.smr .smr-ladder li.boss { border-color: #5a2a2f; }
.smr .smr-ladder li.boss::before { color: #fff; background: var(--red-deep); }
.smr .smr-ladder li span { margin-left: auto; font-size: 0.68rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; color: var(--red); }
/* body map of injuries */
.smr .smr-body { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 210px), 1fr)); gap: 0.75rem; }
.smr .smr-body li { background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 1rem 1.1rem; }
.smr .smr-body li.fatal { border-color: #7f1d1d; background: linear-gradient(160deg, rgba(185, 28, 28, 0.22), var(--panel) 60%); }
.smr .smr-zone { display: inline-block; font-size: 0.72rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: #fca5a5; margin-bottom: 0.3rem; }
.smr .smr-body p { color: var(--mute); font-size: 0.93rem; }
/* treatment table */
.smr .smr-treat { border: 1px solid var(--line); border-radius: 16px; overflow: hidden; background: var(--panel); }
.smr .smr-treat li { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 0.3rem 1rem; padding: 0.7rem 1rem; border-top: 1px solid var(--line); font-size: 0.94rem; }
.smr .smr-treat li:first-child { border-top: 0; background: var(--panel2); font-size: 0.75rem; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; color: var(--mute); }
.smr .smr-treat li span:first-child { color: var(--mute); }
.smr .smr-treat li b { color: #fff; }
.smr .smr-treat li.fatal b { color: #fca5a5; }
/* death timeline */
.smr .smr-time { position: relative; display: grid; gap: 0.75rem; padding-left: 1.6rem; }
.smr .smr-time::before { content: ''; position: absolute; left: 0.45rem; top: 0.6rem; bottom: 0.6rem; width: 2px; background: linear-gradient(var(--red), var(--ecg)); }
.smr .smr-time li { position: relative; background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 0.85rem 1rem; }
.smr .smr-time li::before {
  content: ''; position: absolute; left: -1.45rem; top: 1.05rem; width: 0.8rem; height: 0.8rem; border-radius: 50%;
  background: var(--ink); border: 2px solid var(--red);
}
.smr .smr-time li:last-child::before { border-color: var(--ecg); }
.smr .smr-time p { color: var(--mute); font-size: 0.94rem; }
/* gear */
.smr .smr-gear { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 200px), 1fr)); gap: 0.6rem; }
/* subgrid: titles of one row share a height, so their descriptions line up */
.smr .smr-gear li { display: grid; grid-row: span 2; grid-template-rows: subgrid; row-gap: 0; align-content: start; background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 0.8rem 0.95rem; }
.smr .smr-gear b { display: block; font-size: 0.97rem; }
.smr .smr-gear span { display: block; color: var(--mute); font-size: 0.88rem; line-height: 1.45; margin-top: 0.2rem; }
/* keys */
.smr .smr-keys { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 230px), 1fr)); gap: 0.45rem 1rem; }
.smr .smr-keys li { display: flex; gap: 0.6rem; align-items: baseline; color: var(--mute); font-size: 0.93rem; }
.smr .smr-keys li kbd, .smr .smr-keys li code { flex: none; }
.smr .smr-note { margin-top: 0.85rem; color: var(--mute); font-size: 0.92rem; }
.smr .smr-rules {
  margin-top: 3rem; display: flex; flex-wrap: wrap; gap: 0.8rem 1.2rem; align-items: center; justify-content: space-between;
  background: linear-gradient(120deg, var(--red-soft), var(--panel) 55%); border: 1px solid #5a2a2f; border-radius: 16px; padding: 1.1rem 1.25rem;
}
.smr .smr-rules p { color: var(--mute); max-width: 60ch; }
.smr .smr-btn { display: inline-block; font-weight: 700; color: #fff; text-decoration: none; background: var(--red-deep); border-radius: 10px; padding: 0.55rem 1rem; }
.smr .smr-btn:hover { background: var(--red); color: #fff; }
</style>

<div class="smr">
<section class="smr-hero">
<div class="smr-lights" aria-hidden="true"><span></span><span></span></div>
<div class="smr-top">
<div>
<p class="smr-kicker">Institutii · SMIR</p>
<h1>Ambulanta <span>SMIR</span></h1>
<p class="smr-lede">Ajungi la ranitii din oras, ii stabilizezi pe loc sau ii duci la spital. Tratezi fiecare rana in parte si readuci la viata pe cei cazuti.</p>
</div>
<svg class="smr-cross" viewBox="0 0 120 120" role="img" aria-label="Crucea SMIR">
<rect class="bg" x="6" y="6" width="108" height="108" rx="26"/>
<circle class="ring" cx="60" cy="60" r="40"/>
<path class="plus" d="M48 26 H72 V48 H94 V72 H72 V94 H48 V72 H26 V48 H48 Z"/>
</svg>
</div>
<svg class="smr-monitor" viewBox="0 0 640 120" role="img" aria-label="Monitor cu ritmul inimii">
<g class="grid"><path d="M0 30 H640 M0 60 H640 M0 90 H640"/><path d="M80 0 V120 M160 0 V120 M240 0 V120 M320 0 V120 M400 0 V120 M480 0 V120 M560 0 V120"/></g>
<g class="wipe"><path class="trace" d="M0 70 H60 L70 64 L80 70 H96 L104 78 L114 20 L124 96 L132 70 H150 L166 60 L182 70 H220 L230 64 L240 70 H256 L264 78 L274 20 L284 96 L292 70 H310 L326 60 L342 70 H380 L390 64 L400 70 H416 L424 78 L434 20 L444 96 L452 70 H470 L486 60 L502 70 H540 L550 64 L560 70 H576 L584 78 L594 20 L604 96 L612 70 H640"/></g>
<circle class="head" cx="0" cy="70" r="3.5"/>
<text class="lbl" x="12" y="20">ECG II</text>
<text class="lbl dim" x="560" y="112">SMIR</text>
</svg>
<ul class="smr-stats">
<li><b>8 grade</b><span>de la Debutant la Director</span></li>
<li><b>3 spitale</b><span>Pillbox, Sandy Shores si Paleto Bay</span></li>
<li><b>20 minute</b><span>pana cand un pacient cazut poate da respawn</span></li>
</ul>
</section>
<h2 class="smr-h2" id="cum-intri">Cum intri in SMIR</h2>
<p class="smr-sub">SMIR este o factiune. Nu te angajezi singur: treci de interviu si te angajeaza conducerea, in joc, fata in fata.</p>
<ol class="smr-road">
<li><h3 class="smr-h3">Pregateste-te</h3><p>Ai minim 14 ani, stii regulile de roleplay si regulamentul SMIR. Ai cazierul curat, esti calm si lucrezi bine in echipa.</p></li>
<li><h3 class="smr-h3">Interviul</h3><p>Conducerea spitalului te testeaza la interviu. Vino pregatit: prima impresie conteaza.</p></li>
<li><h3 class="smr-h3">Angajarea</h3><p>Managerul sau Directorul te angajeaza din biroul sefului de la spitalul Pillbox, cu tine langa el (cel mult 10 m). Incepi ca <b>Debutant</b>.</p></li>
</ol>
<div class="smr-card smr-check">
<h3 class="smr-h3">Ce verifica jocul cand esti angajat</h3>
<ul class="smr-list">
<li>Daca ai peste <b>25 de caziere in ultimele 3 luni</b>, nu poti fi angajat. Se numara si cazierele platite sau sterse.</li>
<li>Daca ai plecat de curand dintr-o factiune sau din politie, astepti <b>7 zile</b> (daca ai stat acolo cel putin 30 de zile) sau <b>14 zile</b>.</li>
<li>Cat timp esti in politie, nu poti intra in SMIR.</li>
<li>Conducerea tine o lista neagra: cine e pe ea nu poate fi angajat.</li>
</ul>
</div>
<h2 class="smr-h2" id="grade">Grade</h2>
<p class="smr-sub">Masinile din garajul medicilor se deblocheaza pe grade. Managerul si Directorul conduc spitalul: angajeaza, promoveaza si concediaza.</p>
<ol class="smr-ladder">
<li>Debutant</li>
<li>Asistent</li>
<li>Asistent Sef</li>
<li>Medic Generalist</li>
<li>Medic Specialist</li>
<li>Medic Primar</li>
<li class="boss">Manager<span>conducere</span></li>
<li class="boss">Director<span>conducere</span></li>
</ol>
<h2 class="smr-h2" id="tura">Tura</h2>
<div class="smr-grid">
<div class="smr-card">
<h3 class="smr-h3">Unde intri in tura</h3>
<ul class="smr-list">
<li>La seful de la spitalul Pillbox sau din Sandy Shores: <b>Incepe tura</b> iti pune si uniforma, <b>Termina tura</b> iti da hainele inapoi.</li>
<li>Oriunde, din meniul radial: <kbd>K</kbd> → <b>Ambulanta</b> → <b>Tura (intra/iesi)</b>.</li>
<li>La fiecare logare intri in joc in afara turei.</li>
</ul>
</div>
<div class="smr-card">
<h3 class="smr-h3">Ce ai doar in tura</h3>
<ul class="smr-list">
<li>Salariul: in afara turei nu esti platit.</li>
<li>Frecventele de statie SMIR si cele comune cu politia.</li>
<li>Targa din ambulanta si apelurile de la NPC.</li>
<li>Puncte in pontaj: 2 pentru o reanimare cu defibrilatorul, 1 pentru o rana tratata, 1 pentru o misiune NPC.</li>
</ul>
</div>
<div class="smr-card">
<h3 class="smr-h3">Spitalul are nevoie de tine</h3>
<p>Daca sunt cel putin 2 medici conectati si mai putin de jumatate sunt in tura, nu poti incepe alte joburi pana nu se acopera spitalul.</p>
<p>In tura vezi pe harta toti medicii si politistii din tura, fara tracker.</p>
</div>
</div>
<h2 class="smr-h2" id="cand-cazi">Cand cazi la pamant</h2>
<p class="smr-sub">Asta e valabil pentru orice jucator. Esti in coma si vezi doar de sus, deasupra corpului.</p>
<ol class="smr-time">
<li><h3 class="smr-h3">Chemi ambulanta</h3><p>Apesi <kbd>H</kbd> si apelul pleaca la SMIR. Merge doar daca nu e nimeni in viata la mai putin de 25 m de tine.</p></li>
<li><h3 class="smr-h3">Astepti un medic</h3><p>Un medic te poate reanima pe loc cu defibrilatorul sau te poate duce la spital.</p></li>
<li><h3 class="smr-h3">La medicul de garda</h3><p>Daca esti adus la Pillbox, Sandy Shores sau Paleto Bay, medicul de garda te trateaza contra cost (un minut). Te ridici si iti pastrezi tot inventarul.</p></li>
<li><h3 class="smr-h3">Respawn</h3><p>Dupa 20 de minute apesi <kbd>G</kbd>. Daca nu e nimeni la mai putin de 100 m de tine, astepti doar jumatate. Pierzi inventarul, in afara de acte, chei si cateva obiecte premium sau de eveniment, si te trezesti la cel mai apropiat spital (politistii la sectie, medicii la spital, detinutii la penitenciar).</p></li>
</ol>
<h2 class="smr-h2" id="rani">Ranile</h2>
<p class="smr-sub">Fiecare lovitura de la 5 HP in sus iti lasa o rana pe zona lovita, cu o gravitate care creste la fiecare lovitura (mai putin la pumni, mai mult la arme). Ranile raman si dupa reconectare, pana te trateaza un medic sau medicul de garda. Cat timp porti vesta anti-glont, nu primesti rani.</p>
<ul class="smr-body">
<li><span class="smr-zone">Picioare</span><h3 class="smr-h3">Schiopatezi</h3><p>Mergi mai incet si mai cazi din cand in cand, cu atat mai des cu cat rana e mai grava.</p></li>
<li><span class="smr-zone">Brate si maini</span><h3 class="smr-h3">Scapi arma</h3><p>Din cand in cand nu mai poti tine arma pentru cateva secunde.</p></li>
<li><span class="smr-zone">Torace si spate</span><h3 class="smr-h3">Tusesti</h3><p>Tusesti, vezi incetosat si pierzi viata incet. La o rana grava mai si vomiti.</p></li>
<li><span class="smr-zone">Picioare, brate, torace</span><h3 class="smr-h3">Sangerezi</h3><p>Pierzi viata la intervale fixe; cu cat rana e mai grava, cu atat mai des si mai mult.</p></li>
<li class="fatal"><span class="smr-zone">Cap si gat</span><h3 class="smr-h3">Rana fatala</h3><p>Nu mai poti fi reanimat cu defibrilatorul. Te trateaza doar un medic SMIR, cu bisturiul, in spital, sau medicul de garda. Un glont in cap sau gat cand esti deja jos face si el rana fatala.</p></li>
</ul>
<h2 class="smr-h2" id="interventie">Interventia, pas cu pas</h2>
<div class="smr-grid">
<div class="smr-card">
<h3 class="smr-h3">1. Verifici pacientul</h3>
<p>Tintesti pacientul → <b>Verifica pacientul</b>. Se deschide fisa pacientului: starea lui, ranile in ordinea gravitatii, substantele din sange si supradoza, daca are.</p>
</div>
<div class="smr-card">
<h3 class="smr-h3">2. Tratezi ranile</h3>
<p>Alegi rana din fisa si faci un mic joc de indemanare cu obiectul potrivit. La 3 greseli tratamentul se opreste, obiectul se consuma, iar fiecare greseala agraveaza putin rana.</p>
</div>
<div class="smr-card">
<h3 class="smr-h3">3. Il readuci la viata</h3>
<p>Daca pacientul e in coma si nu are rana fatala, il reanimezi cu <b>Defibrilatorul</b>. In supradoza ii dai <b>NARCAN</b>.</p>
</div>
</div>
<h3 class="smr-h3" style="margin-top:1.2rem">Ce folosesti pentru fiecare rana</h3>
<ul class="smr-treat">
<li><span>Cauza</span><span>Obiect</span></li>
<li><span>Lovituri</span><b>Gheata</b></li>
<li><span>Injunghiere</span><b>Kit de cusut</b></li>
<li><span>Impuscatura</span><b>Penseta</b></li>
<li><span>Arsura</span><b>Crema pentru arsuri</b></li>
<li><span>Alte rani</span><b>Bandaj</b></li>
<li class="fatal"><span>Rana fatala (cap, gat), doar in spital</span><b>Bisturiu</b></li>
</ul>
<p class="smr-note">Fiecare folosire scade 10% din durabilitatea obiectului. Doar medicii SMIR trateaza rani. Politistii, Sindicatul si membrii bandelor pot verifica un pacient si il pot reanima cu un defibrilator.</p>
<h2 class="smr-h2" id="transport">Transportul pacientului</h2>
<div class="smr-grid">
<div class="smr-card">
<h3 class="smr-h3">Targa</h3>
<p>Din ambulanta iei targa (<b>Ia targa</b>; fiecare ambulanta are 2). Pui pacientul pe ea, o impingi si il incarci pe bancheta din spate. Targa o folosesti doar in tura.</p>
</div>
<div class="smr-card">
<h3 class="smr-h3">In brate si pe pat</h3>
<p>Il iei in brate (<b>Ia in brate</b>) si, langa un pat de spital, apesi <kbd>E</kbd> ca sa-l asezi. Pe pat sta cel mult 5 minute. Il poti si reanima direct pe pat.</p>
</div>
<div class="smr-card">
<h3 class="smr-h3">Geanta medicala si haine</h3>
<p>Asezi <b>Geanta medicala</b> pe jos si o folosesti ca depozit (30 de sloturi) langa pacient.</p>
<p>Cu <b>Dezbraca pacientul</b> ii scoti palaria, ochelarii, masca si celelalte accesorii.</p>
</div>
</div>
<h2 class="smr-h2" id="apeluri">Apeluri si statie</h2>
<div class="smr-grid">
<div class="smr-card">
<h3 class="smr-h3">Apelurile</h3>
<ul class="smr-list">
<li>Apelurile cetatenilor (din Telefon → Servicii sau din coma) le deschizi cu <kbd>F7</kbd>.</li>
<li>In tura primesti si apeluri de la NPC: fie il tratezi pe loc, fie il duci la intrarea spitalului Pillbox.</li>
<li>Primesti alertele <b>Cod 3</b> de la politie (un politist are nevoie de ingrijiri).</li>
</ul>
</div>
<div class="smr-card">
<h3 class="smr-h3">Urgenta ta: Cod 5</h3>
<p>Cand echipajul tau are o problema, scrii <code>/cod5</code>, in tura. Alerta ajunge la politistii si medicii din tura, cu locatia ta.</p>
</div>
<div class="smr-card">
<h3 class="smr-h3">Statia</h3>
<p>Frecventele <b>11 - 20</b> sunt doar ale SMIR, iar <b>30 - 34</b> sunt comune cu politia. Intri pe ele doar in tura.</p>
</div>
</div>
<h2 class="smr-h2" id="echipament">Echipament si vehicule</h2>
<p class="smr-sub">Echipamentul il iei de la <b>Farmacie</b>, in spitalul Pillbox.</p>
<ul class="smr-gear">
<li><b>Defibrilator</b><span>Reanimezi un pacient in coma, fara rana fatala.</span></li>
<li><b>NARCAN (Naloxona)</b><span>Opresti o supradoza.</span></li>
<li><b>Gheata, Kit de cusut, Penseta</b><span>Pentru lovituri, injunghieri si impuscaturi.</span></li>
<li><b>Crema pentru arsuri, Bandaj</b><span>Pentru arsuri si celelalte rani.</span></li>
<li><b>Bisturiu</b><span>Pentru ranile fatale, doar in spital.</span></li>
<li><b>Kit test antidrog</b><span>Arata ce substante are pacientul in sange.</span></li>
<li><b>Geanta medicala</b><span>Depozitul pe care il asezi langa pacient.</span></li>
<li><b>Legitimatie Medic</b><span>O arati cand ajungi la un apel, daca ti se cere.</span></li>
</ul>
<div class="smr-grid" style="margin-top:0.75rem">
<div class="smr-card">
<h3 class="smr-h3">Garajele medicilor</h3>
<p>Ai garaje de masini la Pillbox, Sandy Shores si Paleto Bay, heliporturi si garaje de barci. Masina scoasa vine cu blindaj maxim, iar piesele nu i se uzeaza cat timp e scoasa.</p>
</div>
<div class="smr-card">
<h3 class="smr-h3">Girofar si sirena</h3>
<p><kbd>[</kbd> porneste sau opreste girofarul, <kbd>]</kbd> sirena, iar <kbd>R</kbd> schimba tonul.</p>
<p><kbd>K</kbd> → Ambulanta → <b>Obiecte</b>: conuri, bariere, lumini, cort si birou pentru interventii.</p>
</div>
</div>
<h2 class="smr-h2" id="taste">Taste si comenzi</h2>
<div class="smr-card">
<ul class="smr-keys">
<li><kbd>K</kbd> meniul radial → Ambulanta</li>
<li><kbd>F7</kbd> apelurile cetatenilor</li>
<li><kbd>[</kbd> / <kbd>]</kbd> girofar / sirena</li>
<li><code>/cod5</code> urgenta echipajului</li>
<li><kbd>H</kbd> in coma: chemi ambulanta</li>
<li><kbd>G</kbd> in coma: respawn</li>
</ul>
</div>
<div class="smr-rules">
<p>Uniforma, statia, elicopterul, jafurile si orele minime in tura sunt in regulamentul SMIR. Il citesti inainte de interviu.</p>
<a class="smr-btn" href="/zona-info/regulament-smir">Regulament SMIR</a>
</div>
</div>
