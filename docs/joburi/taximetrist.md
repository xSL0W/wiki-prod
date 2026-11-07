---
outline: false
---

<style>
.tx {
  --night: #0f0f10;
  --cab: #1a1a1c;
  --panel: #232326;
  --edge: #3a3a3f;
  --text: #f2f0e9;
  --mute: #a7a49a;
  --yellow: #ffc61a;
  --yellow-soft: rgba(255, 198, 26, 0.12);
  --lcd: #9dff5a;
  --lcd-bg: #0c1608;
  --red: #ff5b4f;
  --paper: #f6f1e3;
  --ink: #2a2620;
  max-width: 920px;
  margin: 0 auto;
  color: var(--text);
  font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.tx *, .tx *::before, .tx *::after { box-sizing: border-box; }
.tx p, .tx li { line-height: 1.6; color: var(--text); margin: 0; }
.tx ul, .tx ol { list-style: none; padding: 0; margin: 0; }
.tx code { white-space: normal; overflow-wrap: anywhere; }
.tx b { color: #fff; font-weight: 650; }
.tx kbd {
  font: inherit; font-size: 0.85em; font-weight: 800; color: var(--night); background: var(--yellow);
  border-radius: 6px; padding: 0.05rem 0.45rem;
}
/* hero: the cab roof sign + the meter */
.tx-hero {
  position: relative;
  background: var(--cab);
  border: 1px solid var(--edge);
  border-radius: 20px;
  padding: clamp(1.25rem, 4vw, 2.5rem);
  padding-top: calc(clamp(1.25rem, 4vw, 2.5rem) + 18px);
  overflow: hidden;
}
.tx-hero::before {
  content: ''; position: absolute; left: 0; right: 0; top: 0; height: 18px;
  background: repeating-conic-gradient(var(--yellow) 0 25%, var(--night) 0 50%) 0 0 / 18px 18px;
}
.tx-head { display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: 1.5rem; align-items: center; }
@media (max-width: 640px) { .tx-head { grid-template-columns: minmax(0, 1fr); } }
.tx-hero h1 {
  display: flex; flex-wrap: wrap; align-items: baseline; gap: 0.15em 0.35em;
  margin: 0 0 0.6rem; border: 0; padding: 0;
  font-size: clamp(2rem, 6vw, 3.4rem); line-height: 1.05; font-weight: 850; letter-spacing: -0.03em; color: #fff;
}
.tx-hero h1 .tx-dash { color: var(--mute); font-weight: 500; }
.tx-hero h1 .tx-hours { color: var(--yellow); }
.tx-hero p { max-width: 48ch; color: var(--mute); font-size: 1.05rem; }
.tx-meter {
  width: min(100%, 300px);
  background: linear-gradient(#2c2c30, #18181a);
  border: 1px solid var(--edge); border-radius: 14px; padding: 0.8rem;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.45);
  font-family: ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace;
}
.tx-sign {
  display: flex; justify-content: space-between; align-items: center;
  font-size: 0.72rem; letter-spacing: 0.14em; text-transform: uppercase; color: var(--mute); margin-bottom: 0.55rem;
}
.tx-status { position: relative; display: inline-block; width: 6.5em; height: 1.5em; border-radius: 5px; overflow: hidden; background: #111; }
.tx-status span {
  position: absolute; inset: 0; display: grid; place-items: center; font-weight: 800; letter-spacing: 0.1em;
  animation: tx-flip 6s steps(1) infinite;
}
.tx-status .free { color: var(--lcd); }
.tx-status .busy { color: var(--red); animation-delay: -3s; }
@keyframes tx-flip { 0% { opacity: 1; } 50% { opacity: 0; } }
.tx-lcd {
  display: grid; grid-template-columns: auto minmax(0, 1fr); gap: 0.35rem 0.8rem; align-items: center;
  background: var(--lcd-bg); border-radius: 8px; padding: 0.7rem 0.85rem;
  color: var(--lcd); text-shadow: 0 0 8px rgba(157, 255, 90, 0.45);
}
.tx-lcd .k { font-size: 0.72rem; letter-spacing: 0.12em; opacity: 0.75; }
.tx-lcd .v { justify-self: end; font-size: 1.6rem; font-weight: 700; line-height: 1; display: flex; }
.tx-roll { display: inline-block; height: 1em; overflow: hidden; }
.tx-roll i { display: block; font-style: normal; line-height: 1; animation: tx-roll 10s steps(10) infinite; }
.tx-roll.fast i { animation-duration: 1s; }
@keyframes tx-roll { to { transform: translateY(-10em); } }
.tx-lcd .dim { opacity: 0.5; }
@media (prefers-reduced-motion: reduce) {
  .tx-status span, .tx-roll i { animation: none; }
  .tx-status .busy { opacity: 0; }
}
.tx .tx-facts { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1.25rem; }
.tx-facts li {
  border: 1px solid var(--edge); background: var(--panel); border-radius: 8px;
  padding: 0.3rem 0.75rem; font-size: 0.92rem;
}
.tx-facts li b { color: var(--yellow); }
/* sections */
.tx h2 {
  margin: 3rem 0 1rem; border: 0; padding: 0 0 0 0.85rem;
  border-left: 5px solid var(--yellow);
  font-size: 1.5rem; font-weight: 800; letter-spacing: -0.015em; color: #fff; line-height: 1.2;
}
.tx h3 { margin: 0 0 0.5rem; border: 0; padding: 0; color: #fff; font-size: 1.15rem; }
.tx-lead { max-width: 66ch; }
.tx-lead + .tx-lead { margin-top: 0.8rem; }
/* the shift as a printed receipt */
.tx-receipt {
  max-width: 640px; margin: 0 auto;
  background: var(--paper); color: var(--ink);
  font-family: ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; font-size: 0.95rem;
  padding: 1.6rem clamp(1rem, 4vw, 2rem);
  -webkit-mask: radial-gradient(circle at 8px 0, transparent 6px, #000 6.5px) top / 16px 51% repeat-x, radial-gradient(circle at 8px 100%, transparent 6px, #000 6.5px) bottom / 16px 51% repeat-x;
  mask: radial-gradient(circle at 8px 0, transparent 6px, #000 6.5px) top / 16px 51% repeat-x, radial-gradient(circle at 8px 100%, transparent 6px, #000 6.5px) bottom / 16px 51% repeat-x;
}
.tx-receipt p, .tx-receipt li { color: var(--ink); }
.tx-receipt b { color: #000; }
.tx-receipt .title { text-align: center; font-weight: 800; letter-spacing: 0.2em; text-transform: uppercase; }
.tx-receipt .sub { text-align: center; font-size: 0.82rem; opacity: 0.7; margin-top: 0.2rem; }
.tx-receipt hr { border: 0; border-top: 2px dashed rgba(42, 38, 32, 0.4); margin: 1rem 0; }
.tx-receipt ol { counter-reset: tx-line; }
.tx-receipt li { display: grid; grid-template-columns: 2.4rem minmax(0, 1fr); gap: 0.4rem; padding: 0.35rem 0; counter-increment: tx-line; }
.tx-receipt li::before { content: counter(tx-line, decimal-leading-zero); font-weight: 800; }
.tx-receipt kbd { color: var(--paper); background: var(--ink); }
.tx-receipt .total { display: flex; justify-content: space-between; gap: 1rem; flex-wrap: wrap; font-weight: 800; text-transform: uppercase; letter-spacing: 0.08em; }
/* two kinds of fares */
.tx-fares { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1rem; }
.tx-fare { background: var(--panel); border: 1px solid var(--edge); border-radius: 16px; padding: 1.25rem 1.4rem; }
.tx-fare.players { border-top: 4px solid var(--yellow); }
.tx-fare.npc { border-top: 4px solid var(--lcd); }
.tx-fare p { color: var(--mute); }
.tx-fare p + p { margin-top: 0.6rem; }
.tx-tag {
  display: inline-block; margin-bottom: 0.6rem; font-size: 0.72rem; font-weight: 800; letter-spacing: 0.14em; text-transform: uppercase;
  color: var(--night); background: var(--yellow); border-radius: 4px; padding: 0.1rem 0.5rem;
}
.tx-fare.npc .tx-tag { background: var(--lcd); }
/* monkey */
.tx-monkey {
  display: grid; grid-template-columns: auto minmax(0, 1fr); gap: 1rem 1.25rem; align-items: center;
  background: linear-gradient(120deg, var(--yellow-soft), var(--panel) 65%);
  border: 1px dashed var(--yellow); border-radius: 16px; padding: 1.2rem 1.4rem;
}
.tx-monkey svg { width: 64px; height: 64px; }
.tx-monkey p { color: var(--mute); }
@media (max-width: 480px) { .tx-monkey { grid-template-columns: minmax(0, 1fr); } }
/* tips */
.tx-tips li { padding: 0.8rem 0 0.8rem 1.6rem; border-top: 1px solid var(--edge); position: relative; }
.tx-tips li:last-child { border-bottom: 1px solid var(--edge); }
.tx-tips li::before {
  content: ''; position: absolute; left: 0; top: 1.15rem; width: 0.8rem; height: 0.8rem;
  background: repeating-conic-gradient(var(--yellow) 0 25%, var(--night) 0 50%) 0 0 / 0.4rem 0.4rem;
}
.tx a { color: var(--yellow); }
.tx a:focus-visible { outline: 3px solid var(--yellow); outline-offset: 2px; border-radius: 4px; }
/* block list: keeps the 8px row spacing the theme no longer adds to classed lists */
.tx .tx-tips > li + li { margin-top: 8px; }
</style>

<div class="tx">

<section class="tx-hero">
<div class="tx-head">
<div>
<h1><span>Taximetrist</span> <span class="tx-dash">-</span> <span class="tx-hours">30h</span></h1>
<p>Urci la volanul unui taxi, pornesti aparatul si duci oamenii prin oras. Pasageri jucatori sau clienti NPC, plata vine din kilometri.</p>
</div>
<div class="tx-meter" role="img" aria-label="Aparat de taxat care alterneaza intre liber si ocupat si numara kilometrii">
<div class="tx-sign"><span>Taxi</span><span class="tx-status"><span class="free">LIBER</span><span class="busy">OCUPAT</span></span></div>
<div class="tx-lcd">
<span class="k">KM</span>
<span class="v"><span class="dim">0</span><span class="tx-roll"><i>0<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9</i></span>.<span class="tx-roll fast"><i>0<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9</i></span></span>
<span class="k">TARIF</span>
<span class="v">/ KM</span>
</div>
</div>
</div>
<ul class="tx-facts">
<li>Un singur grad: <b>Sofer</b></li>
<li>Taxiul este al jobului</li>
<li>Curse cu jucatori si cu NPC</li>
</ul>
</section>

<h2>Cum incep?</h2>
<p class="tx-lead">Angajeaza-te ca <b>Taxi</b> la Primarie (<code>Telefon → Harti → Locatii importante → Primarie</code>) sau direct de la <b>seful taximetristilor</b>. Ai nevoie de minim <b>30 de ore</b> jucate pe server.</p>
<p class="tx-lead">Seful te asteapta la dispeceratul de taxi (<code>Telefon → Harti → Locatii job-uri → Job taximetrist</code>). Chiar langa el e <b>Garajul job Taxi</b>, de unde iei masina de serviciu, un <b>Rhinehart Taxi</b>.</p>

<h2>O tura, pe bon</h2>
<div class="tx-receipt">
<p class="title">Bon de tura</p>
<p class="sub">Taxi - Sofer</p>
<hr>
<ol>
<li><span><b>Ia taxiul</b> din garajul jobului, de langa sef.</span></li>
<li><span><b>Urca la volan.</b> Tura incepe singura si primesti <b>Ai inceput tura!</b>.</span></li>
<li><span><b>Gaseste un client:</b> un jucator care se urca in taxi sau un apel din aplicatia <b>Servicii</b>, deschisa cu <kbd>F7</kbd>.</span></li>
<li><span><b>Du-l la destinatie.</b> Aparatul porneste pentru amandoi si arata kilometrii si suma.</span></li>
<li><span><b>Incaseaza.</b> Cand clientul coboara, cursa se inchide si primesti banii.</span></li>
<li><span><b>Coboara din taxi</b> cand vrei sa termini. Tura se opreste: <b>Ai terminat tura!</b>.</span></li>
</ol>
<hr>
<p class="total"><span>Total</span><span>dupa kilometri</span></p>
</div>

<h2>Doua feluri de curse</h2>
<div class="tx-fares">
<div class="tx-fare players">
<span class="tx-tag">Jucatori</span>
<h3>Pasager real</h3>
<p>Un jucator se urca in taxiul tau si aparatul porneste singur. Suma creste cu fiecare kilometru parcurs.</p>
<p>La coborare, pasagerul plateste exact cat arata aparatul, iar banii intra in contul tau din banca. Pasagerul trebuie sa aiba o suma minima la el ca sa poata urca.</p>
<p>Jucatorii te pot chema si din telefon, din aplicatia <b>Servicii</b>. Duci un singur pasager odata.</p>
</div>
<div class="tx-fare npc">
<span class="tx-tag">NPC</span>
<h3>Client din oras</h3>
<p>Cat esti in tura, primesti apeluri de la NPC in aplicatia <b>Servicii</b> (<kbd>F7</kbd>). Accepta unul si urmeaza GPS-ul pana la <b>Client taxi</b>.</p>
<p>Opreste langa marcaj si clientul urca singur. Du-l la <b>Destinatie taxi</b>, opreste langa marcaj si clientul coboara. Primesti banii cash.</p>
<p>Pretul e fix inca de la urcare si depinde de distanta pana la destinatie. Iei o singura cursa NPC odata.</p>
</div>
</div>

<h2>Maimuta</h2>
<div class="tx-monkey">
<svg viewBox="0 0 64 64" aria-hidden="true"><circle cx="14" cy="26" r="9" fill="#8a5a2b"/><circle cx="50" cy="26" r="9" fill="#8a5a2b"/><circle cx="32" cy="32" r="20" fill="#8a5a2b"/><ellipse cx="32" cy="38" rx="13" ry="11" fill="#e3b98a"/><circle cx="25" cy="29" r="3" fill="#1a1a1c"/><circle cx="39" cy="29" r="3" fill="#1a1a1c"/><path d="M26 42 q6 5 12 0" stroke="#1a1a1c" stroke-width="2.5" fill="none" stroke-linecap="round"/></svg>
<div>
<h3>Trucul aparatului</h3>
<p>Cu un pasager jucator in masina, deschide meniul cu <kbd>K</kbd>, apoi <b>Job → Maimuta</b>. La suma cursei se adauga un bonus. Exista insa o sansa ca pasagerul sa vada, iar atunci primeste mesajul <b>Soferul a folosit maimuta!</b>. La cursele NPC maimuta nu merge.</p>
</div>
</div>

<h2>Sfaturi</h2>
<ul class="tx-tips">
<li><b>Nu cobori din taxi intre curse.</b> Cand iesi de la volan, tura se termina si trebuie sa urci din nou ca s-o reiei.</li>
<li><b>Pasagerul care coboara mai devreme</b> plateste cat arata aparatul pana in acel moment.</li>
<li><b>Daca pasagerul nu are bani,</b> cursa se inchide si nu primesti nimic. Aparatul nu porneste deloc daca nu are suma minima la urcare.</li>
<li><b>La NPC, opreste aproape de marcaj.</b> Clientul urca doar cand esti langa el, iar plata vine doar daca l-ai luat si l-ai lasat la destinatie.</li>
<li><b>In Happy Hour</b> tariful pe kilometru creste, deci si castigul tau.</li>
<li><b>Vrei sa renunti la o cursa NPC?</b> Foloseste <kbd>K</kbd> → <b>Job → Opreste job</b>. Cursa se anuleaza si tura se opreste.</li>
</ul>

</div>
