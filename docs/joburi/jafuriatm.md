---
outline: false
---

<style>
.xatm {
  --night: #070b10;
  --panel: #0d141c;
  --bezel: #16212c;
  --edge: #263646;
  --text: #e4edf3;
  --mute: #8fa2b0;
  --screen: #38f2c8;
  --screen-soft: rgba(56, 242, 200, 0.12);
  --screen-dim: #1d6b5a;
  --alarm: #ff4d5e;
  --alarm-soft: rgba(255, 77, 94, 0.12);
  --mono: ui-monospace, 'SFMono-Regular', 'Cascadia Mono', Consolas, monospace;
  max-width: 920px;
  margin: 0 auto;
  color: var(--text);
  font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.xatm *, .xatm *::before, .xatm *::after { box-sizing: border-box; }
.xatm p, .xatm li { line-height: 1.6; color: var(--text); margin: 0; }
.xatm ul, .xatm ol { list-style: none; padding: 0; margin: 0; }
.xatm li + li { margin-top: 0; }
.xatm b { color: #fff; font-weight: 650; }

/* hero: the front of an ATM */
.xatm-hero {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 300px), 1fr));
  gap: clamp(1rem, 3vw, 2rem);
  align-items: center;
  background: radial-gradient(120% 90% at 85% 10%, var(--screen-soft), transparent 60%), var(--night);
  border: 1px solid var(--edge);
  border-radius: 22px;
  padding: clamp(1.25rem, 4vw, 2.5rem);
  overflow: hidden;
}
.xatm .xatm-hero h1 {
  margin: 0 0 0.7rem;
  border: 0;
  padding: 0;
  font-size: clamp(2rem, 6.5vw, 3.4rem);
  line-height: 1.05;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: #fff;
}
.xatm-hrs {
  display: inline-flex;
  gap: 0.3em;
  white-space: nowrap;
  font-family: var(--mono);
  font-weight: 700;
  color: var(--screen);
  text-shadow: 0 0 18px rgba(56, 242, 200, 0.45);
}
.xatm .xatm-lead { max-width: 46ch; color: var(--mute); font-size: 1.05rem; }
.xatm .xatm-chips { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1.1rem; }
.xatm .xatm-chips li {
  margin: 0;
  font-family: var(--mono);
  font-size: 0.82rem;
  letter-spacing: 0.02em;
  color: var(--screen);
  border: 1px solid var(--screen-dim);
  border-radius: 6px;
  padding: 0.25rem 0.6rem;
  background: rgba(56, 242, 200, 0.05);
}
.xatm .xatm-chips li.xatm-red { color: var(--alarm); border-color: rgba(255, 77, 94, 0.45); background: var(--alarm-soft); }
.xatm-machine { display: block; width: 100%; max-width: 360px; height: auto; margin: 0 auto; }
.xatm-machine .case { fill: var(--bezel); stroke: var(--edge); stroke-width: 2; }
.xatm-machine .glass { fill: #04120f; stroke: var(--screen-dim); stroke-width: 2; }
.xatm-machine .txt { fill: var(--screen); font-family: var(--mono); font-size: 13px; letter-spacing: 1px; }
.xatm-machine .txt.dim { fill: var(--screen-dim); }
.xatm-machine .key { fill: #1f2d3a; stroke: var(--edge); }
.xatm-machine .key.ok { fill: #1c4a33; }
.xatm-machine .key.no { fill: #5a1f27; }
.xatm-machine .slot { fill: #020405; }
.xatm-machine .slotlight { fill: var(--screen); }
.xatm-machine .bolt { fill: #9aa7b2; stroke: #2a3440; stroke-width: 2; }
.xatm-machine .bolt.out { fill: var(--night); stroke: var(--alarm); stroke-dasharray: 3 3; }
.xatm-machine .bit { fill: #c9d3db; }
.xatm-machine .spark { fill: #ffd27a; }
.xatm-machine .cursor { fill: var(--screen); animation: xatm-blink 1.1s steps(1) infinite; }
.xatm-machine .spark { animation: xatm-spark 0.9s ease-in-out infinite; transform-origin: 251px 176px; }
@keyframes xatm-blink { 50% { opacity: 0; } }
@keyframes xatm-spark { 0%, 100% { opacity: 0.2; transform: scale(0.7); } 50% { opacity: 1; transform: scale(1.15); } }

/* section titles look like screen headers */
.xatm h2 {
  margin: 3rem 0 1rem;
  border: 0;
  padding: 0;
  font-size: 1.45rem;
  font-weight: 750;
  letter-spacing: -0.01em;
  color: #fff;
}
.xatm h2::before {
  content: '> ';
  font-family: var(--mono);
  color: var(--screen);
}
.xatm .xatm-intro { color: var(--mute); max-width: 60ch; margin-bottom: 1rem; }

/* requirements: keypad tiles */
.xatm .xatm-pad {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 200px), 1fr));
  gap: 0.75rem;
}
.xatm .xatm-pad li {
  margin: 0;
  background: linear-gradient(180deg, var(--bezel), var(--panel));
  border: 1px solid var(--edge);
  border-bottom-width: 4px;
  border-radius: 12px;
  padding: 1rem 1.1rem;
}
.xatm .xatm-pad .xatm-k {
  display: block;
  font-family: var(--mono);
  font-size: 1.6rem;
  font-weight: 700;
  line-height: 1.1;
  color: var(--screen);
  margin-bottom: 0.35rem;
}
.xatm .xatm-pad .xatm-k.xatm-no { color: var(--alarm); }
.xatm .xatm-pad p { color: var(--mute); font-size: 0.95rem; }

/* the flow: a screen menu with side keys */
.xatm-screen {
  background: #04120f;
  border: 2px solid var(--screen-dim);
  border-radius: 16px;
  padding: clamp(0.9rem, 3vw, 1.5rem);
  box-shadow: inset 0 0 40px rgba(56, 242, 200, 0.06);
}
.xatm .xatm-steps { counter-reset: xatm-step; }
.xatm .xatm-steps li {
  counter-increment: xatm-step;
  position: relative;
  margin: 0;
  padding: 0.85rem 0 0.85rem 3.3rem;
  border-top: 1px dashed rgba(56, 242, 200, 0.18);
}
.xatm .xatm-steps li:first-child { border-top: 0; }
.xatm .xatm-steps li::before {
  content: counter(xatm-step);
  position: absolute;
  left: 0;
  top: 0.8rem;
  width: 2.3rem;
  height: 1.8rem;
  display: grid;
  place-items: center;
  font-family: var(--mono);
  font-weight: 700;
  color: var(--night);
  background: var(--screen);
  border-radius: 5px;
  box-shadow: 0 3px 0 var(--screen-dim);
}
.xatm .xatm-steps b { color: var(--screen); font-family: var(--mono); font-weight: 700; letter-spacing: 0.02em; }
.xatm .xatm-steps p { color: #cfe7df; }
.xatm .xatm-steps .xatm-sub { display: block; margin-top: 0.3rem; color: var(--mute); font-size: 0.93rem; }
.xatm kbd {
  font-family: var(--mono);
  font-size: 0.82em;
  font-weight: 700;
  color: var(--night);
  background: var(--screen);
  border: 0;
  border-radius: 5px;
  box-shadow: 0 2px 0 var(--screen-dim);
  padding: 0.05rem 0.45rem;
}

/* distance gauge */
.xatm-gauge {
  background: var(--panel);
  border: 1px solid var(--edge);
  border-radius: 16px;
  padding: clamp(1rem, 3vw, 1.4rem);
}
.xatm-gauge svg { display: block; width: 100%; height: auto; }
.xatm-gauge .fill { fill: url(#xatm-grad); }
.xatm .xatm-ends { display: flex; justify-content: space-between; gap: 1rem; margin-bottom: 0.6rem; font-size: 0.88rem; color: var(--mute); }
.xatm .xatm-ends span:last-child { text-align: right; }
.xatm .xatm-ends b { display: block; color: #fff; }
.xatm-gauge .pin { fill: var(--screen); }
.xatm-gauge .pin.far { fill: var(--alarm); }
.xatm .xatm-gauge p { color: var(--mute); margin-top: 0.8rem; font-size: 0.95rem; }

/* failure list: an error screen */
.xatm-err {
  border: 1px solid rgba(255, 77, 94, 0.4);
  border-radius: 16px;
  background: linear-gradient(180deg, var(--alarm-soft), transparent 70%), var(--panel);
  padding: clamp(1rem, 3vw, 1.5rem);
}
.xatm .xatm-err li {
  margin: 0;
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 0.8rem;
  padding: 0.7rem 0;
  border-top: 1px solid rgba(255, 77, 94, 0.18);
}
.xatm .xatm-err li:first-child { border-top: 0; padding-top: 0; }
.xatm .xatm-err .xatm-code {
  font-family: var(--mono);
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--alarm);
  border: 1px solid rgba(255, 77, 94, 0.5);
  border-radius: 5px;
  padding: 0.1rem 0.4rem;
  height: fit-content;
  margin-top: 0.2rem;
}

/* extras */
.xatm-extra { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr)); gap: 1rem; }
.xatm-card { background: var(--panel); border: 1px solid var(--edge); border-radius: 16px; padding: 1.2rem 1.3rem; }
.xatm .xatm-card h3 { margin: 0 0 0.45rem; border: 0; padding: 0; font-size: 1.08rem; color: #fff; }
.xatm .xatm-card p { color: var(--mute); }

.xatm a:focus-visible { outline: 3px solid var(--screen); outline-offset: 2px; border-radius: 4px; }
@media (prefers-reduced-motion: reduce) {
  .xatm-machine .cursor, .xatm-machine .spark { animation: none; }
}
</style>

<div class="xatm">

<section class="xatm-hero">
<div>
<h1>Jaf la ATM <span class="xatm-hrs"><span>-</span> <span>10h</span></span></h1>
<p class="xatm-lead">Iei o bormasina, gauresti panoul unui bancomat si strangi banii din el. Lucrezi singur si repede, apoi dispari inainte sa ajunga politia.</p>
<ul class="xatm-chips">
<li>SINGUR</li>
<li>MIN. 2 POLITISTI IN SERVICIU</li>
<li class="xatm-red">PLATA: BANI MURDARI</li>
</ul>
</div>
<svg class="xatm-machine" viewBox="0 0 320 300" role="img" aria-label="Fata unui bancomat: pe ecran scrie jaf in curs, un surub e scos din panou si burghiul lucreaza la al doilea">
<rect class="case" x="20" y="10" width="280" height="280" rx="18"/>
<rect class="glass" x="48" y="34" width="224" height="104" rx="8"/>
<text class="txt" x="64" y="62">BANCOMAT 24/7</text>
<text class="txt dim" x="64" y="86">CARD: ----</text>
<text class="txt" x="64" y="110">JAF IN CURS</text>
<rect class="cursor" x="166" y="99" width="9" height="14"/>
<rect class="slot" x="200" y="154" width="72" height="8" rx="3"/>
<rect class="slotlight" x="214" y="166" width="44" height="3" rx="1.5"/>
<rect class="key" x="48" y="152" width="34" height="22" rx="4"/>
<rect class="key" x="88" y="152" width="34" height="22" rx="4"/>
<rect class="key" x="128" y="152" width="34" height="22" rx="4"/>
<rect class="key" x="48" y="180" width="34" height="22" rx="4"/>
<rect class="key" x="88" y="180" width="34" height="22" rx="4"/>
<rect class="key" x="128" y="180" width="34" height="22" rx="4"/>
<rect class="key" x="48" y="208" width="34" height="22" rx="4"/>
<rect class="key" x="88" y="208" width="34" height="22" rx="4"/>
<rect class="key" x="128" y="208" width="34" height="22" rx="4"/>
<rect class="key no" x="48" y="236" width="34" height="22" rx="4"/>
<rect class="key" x="88" y="236" width="34" height="22" rx="4"/>
<rect class="key ok" x="128" y="236" width="34" height="22" rx="4"/>
<circle class="bolt out" cx="214" cy="212" r="9"/>
<circle class="bolt" cx="251" cy="212" r="9"/>
<circle class="bolt" cx="232" cy="248" r="9"/>
<rect class="bit" x="244" y="150" width="14" height="5" rx="2" transform="rotate(90 251 176)"/>
<circle class="spark" cx="251" cy="176" r="5"/>
</svg>
</section>

<h2>Ce iti trebuie</h2>
<ul class="xatm-pad">
<li><span class="xatm-k">10h</span><p>jucate pe server. Sub 10 ore, bormasina nu porneste jaful.</p></li>
<li><span class="xatm-k">2+</span><p>politisti in serviciu in oras. Cu mai putini, nu poti incepe.</p></li>
<li><span class="xatm-k"><img class="eg-item" src="/items/drill.webp" alt="">Bormasina</span><p>in inventar. O gasesti la <b>Home depot</b>, la Unelte. Se consuma la fiecare incercare.</p></li>
<li><span class="xatm-k xatm-no">Nu</span><p>poti fi politist sau medic. Nici in zonele protejate nu poti sparge un bancomat.</p></li>
</ul>

<h2>Pas cu pas</h2>
<div class="xatm-screen">
<ol class="xatm-steps">
<li><p><b>Stai lipit de bancomat.</b> Trebuie sa fii chiar in fata lui, nu la cativa pasi.</p></li>
<li><p><b>Foloseste <img class="eg-item" src="/items/drill.webp" alt="">Bormasina</b> din inventar. Jaful porneste, iar bancomatul iese din functiune.</p></li>
<li><p><b>Gaureste suruburile panoului.</b> Tine apasat <kbd>Space</kbd> ca sa gauresti si da drumul ca sa se raceasca burghiul. <kbd>Esc</kbd> abandoneaza jaful.<span class="xatm-sub">Urmareste bara CALDURA. Daca ajunge sus, burghiul se supraincalzeste: pierzi din adancime si astepti pana se raceste. Scoate toate suruburile inainte sa expire timpul.</span></p></li>
<li><p><b>Politia primeste alerta</b> in clipa in care ai scos ultimul surub. Locul jafului apare pe harta lor.</p></li>
<li><p><b>Strange banii.</b> Stai pe loc pana se umple bara. Nu poti merge, alerga, trage sau urca in masina cat timp strangi.<span class="xatm-sub">Daca anulezi bara, jaful esueaza si pleci fara nimic.</span></p></li>
<li><p><b>Primesti <img class="eg-item" src="/items/dirtymoney.webp" alt="">Bani murdari</b> direct in inventar. Acum pleaca repede din zona.</p></li>
</ol>
</div>

<h2>Unde spargi conteaza</h2>
<div class="xatm-gauge">
<div class="xatm-ends"><span><b>Langa sectia VSPD</b>strangi repede</span><span><b>Departe de politie</b>strangi mai mult timp</span></div>
<svg viewBox="0 0 600 40" role="img" aria-label="Langa sectia de politie strangi banii repede, departe de ea dureaza mai mult">
<defs>
<linearGradient id="xatm-grad" x1="0" x2="1" y1="0" y2="0">
<stop offset="0" stop-color="#38f2c8"/>
<stop offset="1" stop-color="#ff4d5e"/>
</linearGradient>
</defs>
<rect class="fill" x="20" y="12" width="560" height="16" rx="8"/>
<rect class="pin" x="14" y="0" width="12" height="40" rx="3"/>
<rect class="pin far" x="574" y="0" width="12" height="40" rx="3"/>
</svg>
<p>Cat timp strangi banii depinde de distanta pana la sectia de politie din Vespucci (VSPD). Langa sectie termini repede, dar politia ajunge imediat. Departe de ea ai mai mult de stat langa bancomat, insa patrulele au de mers mai mult pana la tine.</p>
</div>

<h2>Ce te poate opri</h2>
<div class="xatm-err">
<ul>
<li><span class="xatm-code">ERR 01</span><p><b>Pierzi la bormasina.</b> Daca expira timpul sau apesi <kbd>Esc</kbd>, jaful esueaza. Bormasina e deja consumata.</p></li>
<li><span class="xatm-code">ERR 02</span><p><b>Anulezi stransul banilor.</b> Jaful se termina si nu primesti nimic.</p></li>
<li><span class="xatm-code">ERR 03</span><p><b>Iesi de pe server</b> in timpul jafului. Jaful se anuleaza.</p></li>
<li><span class="xatm-code">ERR 04</span><p><b>Ai dat deja un jaf la ATM.</b> Dupa fiecare jaf, reusit sau nu, astepti o pauza pana la urmatorul. Pauza porneste cand incepi jaful.</p></li>
<li><span class="xatm-code">ERR 05</span><p><b>Bancomatul a fost spart de curand.</b> Ramane dezactivat o vreme. Nu il mai poate jefui nimeni si nici nu mai poti scoate bani din el pana isi revine.</p></li>
</ul>
</div>

<h2>In plus</h2>
<div class="xatm-extra">
<div class="xatm-card">
<h3>Happy Hour</h3>
<p>Cand Happy Hour e activ pentru jafurile la ATM, primesti mai multi bani murdari pe acelasi jaf.</p>
</div>
<div class="xatm-card">
<h3>Puncte pentru familie</h3>
<p>Daca faci parte dintr-o familie care aduna puncte, fiecare jaf reusit ii aduce puncte.</p>
</div>
</div>

</div>
