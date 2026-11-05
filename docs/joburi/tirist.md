---
outline: false
---

<style>
.tr {
  --night: #0c0f14;
  --cab: #141922;
  --rail: #222a36;
  --line: #333d4b;
  --text: #e8ecf2;
  --mute: #9aa6b5;
  --diesel: #f4b400;
  --diesel-soft: rgba(244, 180, 0, 0.12);
  --stamp: #ff5a4e;
  --bay-bad: #ff5a4e;
  --bay-ok: #4c8dff;
  --bay-good: #2fd27a;
  --mono: ui-monospace, 'SFMono-Regular', 'Cascadia Mono', Consolas, monospace;
  max-width: 940px;
  margin: 0 auto;
  color: var(--text);
  font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.tr *, .tr *::before, .tr *::after { box-sizing: border-box; }
.tr p, .tr li { line-height: 1.6; color: var(--text); margin: 0; }
.tr ul, .tr ol { list-style: none; padding: 0; margin: 0; }
.tr h1, .tr h2, .tr h3 { border: 0; padding: 0; }
.tr a:focus-visible { outline: 3px solid var(--diesel); outline-offset: 2px; }
.tr code { font-family: var(--mono); }

/* hero: a waybill with the road on it */
.tr-bill {
  position: relative;
  background: var(--night);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: clamp(1.2rem, 4vw, 2.4rem);
  overflow: hidden;
}
.tr-bill::before {
  content: ''; position: absolute; inset: 0 0 auto 0; height: 6px;
  background: repeating-linear-gradient(90deg, var(--diesel) 0 22px, var(--night) 22px 44px);
}
.tr-doc {
  display: flex; flex-wrap: wrap; justify-content: space-between; gap: 0.5rem 1rem;
  font-family: var(--mono); font-size: 0.78rem; letter-spacing: 0.14em; text-transform: uppercase; color: var(--mute);
}
.tr-stamp {
  color: var(--stamp); border: 2px solid var(--stamp); border-radius: 6px; padding: 0.1rem 0.5rem;
  transform: rotate(-4deg); font-weight: 700;
}
.tr-bill h1 {
  margin: 1rem 0 0.6rem;
  font-size: clamp(2.1rem, 7vw, 3.6rem);
  line-height: 1.05;
  font-weight: 850;
  letter-spacing: -0.035em;
  color: #fff;
}
.tr-hours {
  display: inline-block; font-family: var(--mono); font-size: 0.55em; font-weight: 700; letter-spacing: 0;
  color: var(--night); background: var(--diesel); border-radius: 10px; padding: 0.12em 0.45em; vertical-align: 0.35em;
}
.tr-bill > p { max-width: 54ch; color: var(--mute); font-size: 1.05rem; }
.tr-road { display: block; width: 100%; height: auto; margin-top: 1.4rem; }
.tr-road .asphalt { fill: var(--cab); }
.tr-road .edge { stroke: var(--line); stroke-width: 2; }
.tr-road .lane {
  stroke: var(--diesel); stroke-width: 3; stroke-dasharray: 26 22;
  animation: tr-lane 1.1s linear infinite;
}
.tr-road .rig { animation: tr-bob 1.4s ease-in-out infinite; }
.tr-road .box { fill: #2a3442; stroke: var(--mute); stroke-width: 1.5; }
.tr-road .cab { fill: var(--diesel); }
.tr-road .glass { fill: var(--night); }
.tr-road .wheel { fill: var(--night); stroke: var(--mute); stroke-width: 2; }
.tr-road .pin { fill: var(--diesel); }
.tr-road .pin-end { fill: var(--bay-good); }
.tr-road text { fill: var(--mute); font-size: 12px; font-family: var(--mono); letter-spacing: 0.08em; }
@keyframes tr-lane { to { stroke-dashoffset: 48; } }
@keyframes tr-bob { 50% { transform: translateY(-1.5px); } }
@media (prefers-reduced-motion: reduce) {
  .tr-road .lane, .tr-road .rig { animation: none; }
}

/* manifest fields */
.tr-manifest {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
  border: 1px dashed var(--line); border-radius: 12px; margin-top: 1.4rem; overflow: hidden;
}
.tr-manifest div { padding: 0.75rem 1rem; border-right: 1px dashed var(--line); border-bottom: 1px dashed var(--line); margin: 0 -1px -1px 0; }
.tr-manifest dt {
  font-family: var(--mono); font-size: 0.72rem; letter-spacing: 0.12em; text-transform: uppercase; color: var(--diesel);
}
.tr-manifest dd { margin: 0.2rem 0 0; color: var(--text); font-size: 0.95rem; line-height: 1.45; }

/* sections */
.tr h2 {
  display: flex; align-items: baseline; gap: 0.7rem;
  margin: 3rem 0 1rem;
  font-size: 1.5rem; font-weight: 780; letter-spacing: -0.015em; color: #fff;
}
.tr h2 span { font-family: var(--mono); font-size: 0.8rem; font-weight: 600; color: var(--diesel); letter-spacing: 0.1em; }
.tr b { color: #fff; font-weight: 650; }
.tr kbd {
  font-family: var(--mono); font-size: 0.85em; font-weight: 700; color: var(--night); background: var(--diesel);
  border-radius: 5px; padding: 0.05rem 0.45rem; box-shadow: 0 2px 0 #9c7300;
}

/* progression as an odometer */
.tr-odo { display: grid; gap: 0.8rem; }
.tr-odo li {
  display: grid; grid-template-columns: auto 1fr; gap: 0.4rem 1.2rem; align-items: center;
  background: var(--cab); border: 1px solid var(--line); border-radius: 14px; padding: 1rem 1.2rem;
}
.tr-digits { display: flex; gap: 3px; font-family: var(--mono); font-weight: 700; font-size: clamp(1.1rem, 4vw, 1.5rem); }
.tr-digits i {
  font-style: normal; width: 1.35em; text-align: center; padding: 0.15em 0; border-radius: 4px;
  background: #05070a; color: #f5f5f5; border: 1px solid #2a3240;
}
.tr-digits i.on { color: var(--night); background: var(--diesel); border-color: var(--diesel); }
.tr-digits em { font-style: normal; color: var(--mute); align-self: center; margin-left: 0.35rem; font-size: 0.75em; }
.tr-odo strong { display: block; color: #fff; font-size: 1.1rem; }
.tr-odo p { color: var(--mute); font-size: 0.95rem; }
@media (max-width: 520px) { .tr-odo li { grid-template-columns: 1fr; } }
.tr .tr-note { margin-top: 0.8rem; color: var(--mute); font-size: 0.95rem; }

/* the run as a log sheet */
.tr-log { counter-reset: leg; border-top: 1px solid var(--line); }
.tr-log li {
  counter-increment: leg;
  display: grid; grid-template-columns: 3.2rem 1fr; gap: 1rem;
  padding: 1rem 0; border-bottom: 1px solid var(--line);
}
.tr-log li::before {
  content: counter(leg, decimal-leading-zero);
  font-family: var(--mono); font-weight: 700; font-size: 1.05rem; color: var(--diesel);
  border: 1px solid var(--line); border-radius: 8px; text-align: center; padding: 0.35rem 0; height: fit-content;
}

/* parking grades */
.tr-park { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 1rem; }
.tr-bay { background: var(--cab); border: 1px solid var(--line); border-radius: 14px; padding: 1rem 1.1rem 1.2rem; }
.tr-bay svg { display: block; width: 100%; max-width: 220px; height: auto; margin: 0 auto 0.8rem; }
.tr-bay .spot { fill: none; stroke: var(--line); stroke-width: 2; stroke-dasharray: 6 5; }
.tr-bay .trl { stroke-width: 3; fill-opacity: 0.18; }
.tr-bay.bad .trl { stroke: var(--bay-bad); fill: var(--bay-bad); }
.tr-bay.ok .trl { stroke: var(--bay-ok); fill: var(--bay-ok); }
.tr-bay.good .trl { stroke: var(--bay-good); fill: var(--bay-good); }
.tr-bay h3 { margin: 0 0 0.3rem; font-size: 1.05rem; display: flex; align-items: center; gap: 0.5rem; color: #fff; }
.tr-bay h3::before { content: ''; width: 12px; height: 12px; border-radius: 3px; background: currentColor; }
.tr-bay.bad h3 { color: var(--bay-bad); }
.tr-bay.ok h3 { color: var(--bay-ok); }
.tr-bay.good h3 { color: var(--bay-good); }
.tr-bay p { color: var(--mute); font-size: 0.95rem; }

/* tips */
.tr-tips { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 0.8rem; }
.tr-tips li {
  background: linear-gradient(160deg, var(--diesel-soft), var(--cab) 55%);
  border: 1px solid var(--line); border-left: 4px solid var(--diesel); border-radius: 12px; padding: 0.9rem 1.1rem;
}
</style>

<div class="tr">

<section class="tr-bill">
<div class="tr-doc"><span>Scrisoare de transport</span><span class="tr-stamp">Job legal</span></div>
<h1>Tirist - <span class="tr-hours">50h/200h</span></h1>
<p>Iei tirul firmei, cuplezi remorca si duci marfa dintr-un capat al hartii in altul. La destinatie parchezi remorca, iar cu cat o parchezi mai bine, cu atat castigi mai mult.</p>
<svg class="tr-road" viewBox="0 0 640 150" role="img" aria-label="Un tir cu remorca merge pe autostrada de la punctul de preluare spre destinatie">
<rect class="asphalt" x="0" y="62" width="640" height="56" rx="6"/>
<line class="edge" x1="0" y1="64" x2="640" y2="64"/>
<line class="edge" x1="0" y1="116" x2="640" y2="116"/>
<line class="lane" x1="0" y1="90" x2="640" y2="90"/>
<g class="rig">
<rect class="box" x="190" y="70" width="150" height="38" rx="3"/>
<rect class="cab" x="344" y="74" width="52" height="34" rx="6"/>
<rect class="glass" x="378" y="79" width="14" height="13" rx="2"/>
<circle class="wheel" cx="215" cy="112" r="7"/>
<circle class="wheel" cx="235" cy="112" r="7"/>
<circle class="wheel" cx="320" cy="112" r="7"/>
<circle class="wheel" cx="384" cy="112" r="7"/>
</g>
<path class="pin" d="M40 20 a12 12 0 0 1 24 0 c0 10 -12 22 -12 22 s-12 -12 -12 -22z"/>
<text x="20" y="140">PRELUARE</text>
<path class="pin-end" d="M580 20 a12 12 0 0 1 24 0 c0 10 -12 22 -12 22 s-12 -12 -12 -22z"/>
<text x="540" y="140">DESTINATIE</text>
</svg>
<dl class="tr-manifest">
<div><dt>Vehicul</dt><dd>Tir Hauler + remorca, ale firmei</dd></div>
<div><dt>Echipa</dt><dd>Fiecare cu tirul lui, convoiul e la alegere</dd></div>
<div><dt>Plata</dt><dd>In contul bancar, la fiecare livrare</dd></div>
<div><dt>Uniforma</dt><dd>Nu ai nevoie de uniforma</dd></div>
</dl>
</section>

<h2>Cum incep? <span>/ ANGAJARE</span></h2>
<p>Angajeaza-te ca <b>Tirist</b> la Primarie (<code>Telefon → Harti → Locatii importante → Primarie</code>) sau direct la seful tiristilor, cu <b>Angajeaza-te ca Tirist</b>. Ai nevoie de <b>50 de ore</b> jucate. Gasesti cate un sef la fiecare punct de preluare; cel marcat la Primarie sta in docurile din Los Santos.</p>

<h2>Grade <span>/ KILOMETRAJ</span></h2>
<ol class="tr-odo">
<li><span class="tr-digits"><i>0</i><i>0</i><i>0</i><i class="on">5</i><i class="on">0</i><em>h</em></span><div><strong>Sofer</strong><p>Curse de nivel 1: aprovizionare pentru magazine, depozite si fabrici.</p></div></li>
<li><span class="tr-digits"><i>0</i><i>0</i><i class="on">2</i><i class="on">0</i><i class="on">0</i><em>h</em></span><div><strong>Sofer avansat</strong><p>Deblocheaza cursele de nivel 2, cu remorci speciale, de exemplu platforma pentru masini.</p></div></li>
</ol>
<p class="tr-note">Promovarea e automata: cand ai strans orele, vorbesti cu seful tiristilor si urci in grad.</p>

<h2>O cursa, pe scurt <span>/ FOAIE DE PARCURS</span></h2>
<ol class="tr-log">
<li><p><b>Vorbeste cu seful tiristilor</b> cu <kbd>E</kbd> si alege <b>Incepe tura</b>.</p></li>
<li><p><b>Alege nivelul si cursa.</b> Lista iti arata distanta pana la fiecare destinatie. Cursele prea apropiate de tine nu apar.</p></li>
<li><p><b>Tirul si remorca apar langa tine</b>, deja cuplate, iar tu esti urcat direct la volan. Pana pleci din parcare treci prin celelalte vehicule, ca sa iesi usor.</p></li>
<li><p><b>Urmeaza traseul de pe GPS</b> pana la <b>Destinatie Tir</b>.</p></li>
<li><p><b>Parcheaza remorca pe marcaj</b> si apasa <kbd>H</kbd>. Culoarea marcajului iti spune cat de bine ai parcat.</p></li>
<li><p><b>Primesti plata</b> si cobori din tir. Pe harta apare <b>Preluare marfa tirist</b>, locul de unde iei urmatoarea cursa, aproape de unde ai livrat.</p></li>
</ol>

<h2>Parcarea conteaza <span>/ LIVRARE</span></h2>
<div class="tr-park">
<div class="tr-bay bad">
<svg viewBox="0 0 220 110" aria-hidden="true"><rect class="spot" x="60" y="20" width="100" height="70" rx="4"/><rect class="trl" x="150" y="8" width="62" height="40" rx="3" transform="rotate(14 181 28)"/></svg>
<h3>Rosu</h3>
<p>Remorca e departe de loc, nu e cuplata sau nu esti in tir. Poti livra, dar castigi cel mai putin.</p>
</div>
<div class="tr-bay ok">
<svg viewBox="0 0 220 110" aria-hidden="true"><rect class="spot" x="60" y="20" width="100" height="70" rx="4"/><rect class="trl" x="70" y="30" width="80" height="50" rx="3" transform="rotate(-22 110 55)"/></svg>
<h3>Albastru</h3>
<p>Remorca e pe loc, dar stramba. Plata e mai buna.</p>
</div>
<div class="tr-bay good">
<svg viewBox="0 0 220 110" aria-hidden="true"><rect class="spot" x="60" y="20" width="100" height="70" rx="4"/><rect class="trl" x="70" y="30" width="80" height="50" rx="3"/></svg>
<h3>Verde</h3>
<p>Remorca e pe loc si dreapta, in directia marcajului. Asta e parcarea care aduce cel mai mult.</p>
</div>
</div>
<p class="tr-note">Plata depinde de distanta cursei, de nivelul ei si de cum ai parcat. Tasta <kbd>H</kbd> merge doar cand remorca e aproape de marcaj.</p>

<h2>Sfaturi <span>/ DE RETINUT</span></h2>
<ul class="tr-tips">
<li><b>Nu pleca de langa tir.</b> Daca cobori, ai 10 minute sa te urci inapoi. Altfel cursa se anuleaza si tirul dispare.</li>
<li><b>Livreaza cu tirul si remorca primite.</b> Alt camion sau alta remorca nu se platesc.</li>
<li><b>Fa convoaie.</b> Prietenii pot lua aceeasi cursa de la acelasi sef, fiecare cu tirul lui.</li>
<li><b>Livrarile prea rapide nu se platesc.</b> Daca ajungi la destinatie mult mai repede decat se poate in mod normal, nu primesti bani pe cursa.</li>
<li><b>Daca renunti la job</b> sau iesi de pe server, cursa se opreste si tirul dispare.</li>
<li><b>Asteapta putin</b> daca seful iti spune ca tocmai a dat o cursa. Dupa cateva secunde poti lua alta.</li>
</ul>

</div>
