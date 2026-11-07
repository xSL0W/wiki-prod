---
outline: false
---

<style>
.el {
  --board: #0b1117;
  --trace: #121c25;
  --pad: #1a2833;
  --grid: #22394a;
  --text: #e6eef3;
  --mute: #8fa6b4;
  --volt: #ffd84a;
  --volt-soft: rgba(255, 216, 74, 0.12);
  --arc: #5ee3ff;
  --copper: #d98b4a;
  max-width: 920px;
  margin: 0 auto;
  color: var(--text);
  font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.el *, .el *::before, .el *::after { box-sizing: border-box; }
.el p, .el li { line-height: 1.6; color: var(--text); margin: 0; }
.el ul, .el ol { list-style: none; padding: 0; margin: 0; }
.el code { white-space: normal; overflow-wrap: anywhere; }
.el b { color: #fff; font-weight: 650; }
.el kbd {
  font: inherit; font-size: 0.85em; font-weight: 800; color: var(--board); background: var(--volt);
  border-radius: 4px; padding: 0.05rem 0.45rem; box-shadow: 0 0 0 2px rgba(255, 216, 74, 0.25);
}
/* hero: a schematic, current running from the depot to the pole */
.el-hero {
  background-color: var(--board);
  background-image: linear-gradient(var(--trace) 1px, transparent 1px), linear-gradient(90deg, var(--trace) 1px, transparent 1px);
  background-size: 24px 24px;
  border: 1px solid var(--grid);
  border-radius: 18px;
  padding: clamp(1.25rem, 4vw, 2.5rem);
  overflow: hidden;
}
.el-hero h1 {
  display: flex; flex-wrap: wrap; align-items: center; gap: 0.2em 0.35em;
  margin: 0 0 0.6rem; border: 0; padding: 0;
  font-size: clamp(2rem, 6vw, 3.4rem); line-height: 1.05; font-weight: 800; letter-spacing: -0.03em; color: #fff;
}
.el-hero h1 .el-dash { color: var(--mute); font-weight: 500; }
.el-hero h1 .el-hours {
  font-family: ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; font-size: 0.55em; letter-spacing: 0.02em;
  color: var(--volt); border: 2px solid var(--volt); border-radius: 8px; padding: 0.1em 0.5em;
}
.el-hero p { max-width: 52ch; color: var(--mute); font-size: 1.05rem; }
.el-sch { display: block; width: 100%; height: auto; margin-top: 1.5rem; }
.el-sch .wire { fill: none; stroke: var(--copper); stroke-width: 4; stroke-linejoin: round; stroke-linecap: round; }
.el-sch .flow {
  fill: none; stroke: var(--volt); stroke-width: 4; stroke-linecap: round; stroke-linejoin: round;
  stroke-dasharray: 0.04 0.16; animation: el-flow 2.4s linear infinite;
}
.el-sch .part { fill: var(--board); stroke: var(--arc); stroke-width: 3; stroke-linejoin: round; }
.el-sch .node { fill: var(--volt); }
.el-sch .lamp { fill: var(--volt); opacity: 0.25; animation: el-glow 2.4s ease-in-out infinite; }
.el-sch .lbl { fill: var(--text); font-size: 18px; font-weight: 700; font-family: inherit; }
.el-sch .sub { fill: var(--mute); font-size: 15px; font-family: ui-monospace, Menlo, Consolas, monospace; }
@keyframes el-flow { to { stroke-dashoffset: -0.2; } }
@keyframes el-glow { 0%, 60% { opacity: 0.2; } 75%, 100% { opacity: 0.95; } }
@media (prefers-reduced-motion: reduce) {
  .el-sch .flow { animation: none; }
  .el-sch .lamp { animation: none; opacity: 0.9; }
}
.el .el-chips { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1.1rem; }
.el-chips li {
  font-family: ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; font-size: 0.85rem;
  border: 1px solid var(--grid); background: var(--pad); border-radius: 6px; padding: 0.3rem 0.7rem;
}
.el-chips li::before { content: '\25CF'; color: var(--arc); margin-right: 0.45rem; font-size: 0.7em; vertical-align: 0.15em; }
/* sections */
.el h2 {
  display: flex; align-items: center; gap: 0.7rem;
  margin: 3rem 0 1rem; border: 0; padding: 0;
  font-size: 1.5rem; font-weight: 750; letter-spacing: -0.015em; color: #fff;
}
.el h2::before {
  content: ''; flex: none; width: 22px; height: 22px;
  background: var(--volt);
  clip-path: polygon(55% 0, 10% 58%, 45% 58%, 35% 100%, 90% 40%, 54% 40%);
}
.el h3 { margin: 0 0 0.45rem; border: 0; padding: 0; color: #fff; font-size: 1.12rem; }
.el-lead { max-width: 66ch; }
.el-lead + .el-lead { margin-top: 0.8rem; }
/* the shift as a circuit trace with solder points */
.el-trace { position: relative; counter-reset: el-step; }
.el-trace::before {
  content: ''; position: absolute; left: 15px; top: 14px; bottom: 14px; width: 4px; border-radius: 2px;
  background: linear-gradient(var(--copper), var(--volt));
}
.el-trace li { position: relative; padding: 0 0 1.3rem 3.2rem; counter-increment: el-step; }
.el-trace li:last-child { padding-bottom: 0; }
.el-trace li::before {
  content: counter(el-step); position: absolute; left: 0; top: 0;
  width: 34px; height: 34px; border-radius: 50%; display: grid; place-items: center;
  font-family: ui-monospace, Menlo, Consolas, monospace; font-size: 0.85rem; font-weight: 800;
  color: var(--volt); background: var(--board); border: 3px solid var(--volt);
}
.el-trace li p { color: var(--mute); }
.el-trace li p b { color: #fff; }
.el-trace .t { display: block; color: #fff; font-weight: 700; margin-bottom: 0.15rem; padding-top: 0.25rem; }
/* solo vs team: one lamp or two lamps in parallel */
.el-modes { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1rem; }
.el-mode { background: var(--pad); border: 1px solid var(--grid); border-radius: 16px; padding: 1.2rem 1.35rem; }
.el-mode.team { background: linear-gradient(160deg, var(--volt-soft), var(--pad) 60%); border-color: var(--volt); }
.el-mode p { color: var(--mute); }
.el-mini { display: block; width: 100%; max-width: 220px; height: auto; margin: 0 0 0.8rem; }
.el-mini .w { fill: none; stroke: var(--copper); stroke-width: 3; }
.el-mini .l { fill: var(--volt); }
.el-mini .r { fill: none; stroke: var(--volt); stroke-width: 2; opacity: 0.5; }
/* tips as fuses */
.el-tips { display: grid; gap: 0.6rem; }
.el-tips li {
  display: grid; grid-template-columns: 14px minmax(0, 1fr); gap: 0.9rem; align-items: start;
  background: var(--trace); border: 1px solid var(--grid); border-radius: 12px; padding: 0.85rem 1rem;
}
.el-tips li::before {
  content: ''; width: 14px; height: 24px; margin-top: 0.15rem; border-radius: 4px;
  border: 2px solid var(--arc); background: linear-gradient(var(--board) 40%, var(--volt) 40% 60%, var(--board) 60%);
}
.el a { color: var(--arc); }
.el a:focus-visible { outline: 3px solid var(--volt); outline-offset: 2px; border-radius: 4px; }
/* block list: keeps the 8px row spacing the theme no longer adds to classed lists */
.el .el-trace > li + li { margin-top: 8px; }
</style>

<div class="el">

<section class="el-hero">
<h1><span>Electrician</span> <span class="el-dash">-</span> <span class="el-hours">35h</span></h1>
<p>Duba de serviciu, o scara si un stalp care nu mai merge. Ajungi la locatie, urci si repari circuitul. Singur sau impreuna cu un coleg.</p>
<svg class="el-sch" viewBox="0 0 640 210" role="img" aria-label="Schema electrica: curentul pleaca de la sef, trece prin duba, scara si reparatie si aprinde becul de pe stalp">
<path class="wire" d="M60 150 V60 H220 M260 60 H400 M440 60 H560 V150 M560 190 V200 H60 V190"/>
<path class="flow" pathLength="1" d="M60 150 V60 H560 V150"/>
<rect class="part" x="40" y="150" width="40" height="40" rx="4"/>
<path class="part" d="M50 162 h20 M54 174 h12" fill="none"/>
<rect class="part" x="220" y="44" width="40" height="32" rx="6"/>
<path class="part" d="M400 60 l6 -12 l8 24 l8 -24 l8 24 l6 -12" fill="none"/>
<circle class="lamp" cx="560" cy="170" r="28"/>
<circle class="part" cx="560" cy="170" r="20"/>
<path class="part" d="M546 156 l28 28 M574 156 l-28 28" fill="none"/>
<circle class="node" cx="60" cy="60" r="6"/>
<circle class="node" cx="560" cy="60" r="6"/>
<text class="lbl" x="92" y="168">Sef</text>
<text class="sub" x="92" y="186">tura</text>
<text class="lbl" x="214" y="112">Duba</text>
<text class="sub" x="214" y="132">scara</text>
<text class="lbl" x="386" y="112">Stalp</text>
<text class="sub" x="386" y="132">repara</text>
<text class="lbl" x="470" y="176">Plata</text>
</svg>
<ul class="el-chips">
<li>Grad unic: Angajat</li>
<li>Singur sau in echipa</li>
<li>Duba si uniforma de la job</li>
</ul>
</section>

<h2>Cum incep?</h2>
<p class="el-lead">Angajeaza-te ca <b>Electrician</b> la Primarie (<code>Telefon → Harti → Locatii importante → Primarie</code>) sau direct de la <b>seful electrician</b>. Ai nevoie de minim <b>35 de ore</b> jucate pe server.</p>
<p class="el-lead">Seful te asteapta la sediul electricienilor (<code>Telefon → Harti → Locatii job-uri → Job electrician</code>). De la el pornesti si opresti tura si tot de acolo faci echipa.</p>

<h2>O tura, pe circuit</h2>
<ol class="el-trace">
<li><span class="t">Porneste tura</span><p>Alege <b>Incepe tura</b> din meniul sefului. Primesti uniforma, iar liderul primeste duba de serviciu, cu scara in ea. GPS-ul iti arata prima <b>Locatie job electrician</b>.</p></li>
<li><span class="t">Parcheaza langa stalp</span><p>Lasa duba in afara cercului rosu de langa stalp. Daca parchezi in cerc, nu poti scoate scara.</p></li>
<li><span class="t">Ia scara</span><p>Langa duba, apasa <kbd>E</kbd> pe <b>Ia scara din masina</b>. Cat o cari, nu poti alerga, sari sau urca in masini.</p></li>
<li><span class="t">Pune scara</span><p>Du-o la punctul marcat si apasa <kbd>E</kbd> pe <b>Pune scara</b>.</p></li>
<li><span class="t">Urca si repara</span><p>Sus, la marcajul <b>[E] - Repara</b>, apasa <kbd>E</kbd> si rezolva minijocul cu circuitul electric.</p></li>
<li><span class="t">Primeste plata</span><p>Banii intra in contul din banca, iar GPS-ul iti da imediat o locatie noua.</p></li>
<li><span class="t">Strange scara</span><p>Apasa <kbd>E</kbd> pe <b>Ia scara</b>, du-te la duba si alege <b>Pune scara in masina</b>. Apoi pleci la urmatorul stalp.</p></li>
</ol>

<h2>Singur sau in echipa</h2>
<div class="el-modes">
<div class="el-mode">
<svg class="el-mini" viewBox="0 0 220 70" aria-hidden="true"><path class="w" d="M10 35 H90 M130 35 H210"/><circle class="r" cx="110" cy="35" r="26"/><circle class="l" cx="110" cy="35" r="14"/></svg>
<h3>Singur</h3>
<p>Conduci, cari scara si repari tu. Ritm linistit, toata plata e a ta.</p>
</div>
<div class="el-mode team">
<svg class="el-mini" viewBox="0 0 220 70" aria-hidden="true"><path class="w" d="M10 35 H50 V15 H90 M130 15 H170 V35 H210 M50 35 V55 H90 M130 55 H170 V35"/><circle class="l" cx="110" cy="15" r="11"/><circle class="l" cx="110" cy="55" r="11"/></svg>
<h3>Cu un coleg</h3>
<p>Formeaza echipa din <b>Meniu echipa</b>, la sef. Liderul porneste tura si primeste duba, iar amandoi trebuie sa fiti electricieni. La fiecare reparatie, <b>fiecare primeste plata intreaga</b>.</p>
</div>
</div>

<h2>Cum termin?</h2>
<p class="el-lead">Alege <b>Termina tura</b> de la sef sau deschide meniul cu <kbd>K</kbd> si alege <b>Job → Opreste job</b>. Duba dispare si iti primesti hainele inapoi.</p>

<h2>Sfaturi</h2>
<ul class="el-tips">
<li><span><b>Nu uita scara.</b> Daca urci in duba fara ea, primesti <b>Nu uita scara!</b>. Scara ramane unde ai lasat-o si trebuie sa te intorci dupa ea.</span></li>
<li><span><b>Nu pune scara langa duba.</b> Scara se pune doar la punctul marcat, departe de masina.</span></li>
<li><span><b>Ramaneti impreuna.</b> Daca un coleg iese din joc sau renunta la job, tura se opreste pentru toata echipa.</span></li>
<li><span><b>Repara de aproape.</b> Reparatia se plateste doar daca esti sus, langa marcaj.</span></li>
</ul>

</div>
