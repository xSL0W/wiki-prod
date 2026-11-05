---
outline: false
---

<style>
.cpr {
  --soil: #0e1410;
  --moss: #16211a;
  --bark: #223026;
  --edge: #33463a;
  --text: #edf1e8;
  --mute: #a3b0a0;
  --leaf: #7fcf72;
  --leaf-soft: rgba(127, 207, 114, 0.13);
  --cap: #e8774a;
  --spore: #b79bff;
  --spore-soft: rgba(183, 155, 255, 0.14);
  max-width: 920px;
  margin: 0 auto;
  color: var(--text);
  font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.cpr *, .cpr *::before, .cpr *::after { box-sizing: border-box; }
.cpr p, .cpr li { line-height: 1.6; color: var(--text); margin: 0; }
.cpr ul { list-style: none; padding: 0; margin: 0; }

/* hero: a hand-drawn field map */
.cpr-hero {
  background: radial-gradient(120% 90% at 85% 0%, rgba(127, 207, 114, 0.10), transparent 60%), var(--soil);
  border: 1px solid var(--edge);
  border-radius: 24px;
  padding: clamp(1.25rem, 4vw, 2.5rem);
  overflow: hidden;
}
.cpr-hero h1 {
  margin: 0 0 0.6rem;
  border: 0;
  padding: 0;
  font-family: Georgia, 'Times New Roman', serif;
  font-size: clamp(2rem, 6.5vw, 3.5rem);
  line-height: 1.05;
  font-weight: 700;
  letter-spacing: -0.01em;
  color: #fff;
}
.cpr-hero h1 .cpr-hrs {
  font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
  font-size: 0.55em;
  font-weight: 800;
  vertical-align: middle;
  color: var(--soil);
  background: var(--leaf);
  border-radius: 999px;
  padding: 0.1em 0.6em;
}
.cpr-hero > p { max-width: 54ch; color: var(--mute); font-size: 1.05rem; }
.cpr-field { display: block; width: 100%; height: auto; margin-top: 1.4rem; }
.cpr-field .z1 { fill: var(--leaf-soft); stroke: var(--leaf); stroke-width: 2.5; stroke-dasharray: 8 7; }
.cpr-field .z2 { fill: var(--spore-soft); stroke: var(--spore); stroke-width: 2.5; stroke-dasharray: 8 7; }
.cpr-field .path { fill: none; stroke: var(--bark); stroke-width: 5; stroke-linecap: round; stroke-dasharray: 2 10; }
.cpr-field .cap { fill: var(--cap); }
.cpr-field .cap2 { fill: var(--spore); }
.cpr-field .stem { fill: #efe6d2; }
.cpr-field .hut { fill: var(--leaf); }
.cpr-field text { fill: var(--mute); font-size: 13px; font-family: inherit; }
.cpr-field .lbl1 { fill: var(--leaf); font-weight: 700; }
.cpr-field .lbl2 { fill: var(--spore); font-weight: 700; }
.cpr-field .spore { fill: var(--spore); opacity: 0; animation: cpr-drift 4s ease-in-out infinite; }
.cpr-field .spore:nth-of-type(2n) { animation-delay: 1.3s; }
.cpr-field .spore:nth-of-type(3n) { animation-delay: 2.6s; }
@keyframes cpr-drift {
  0% { opacity: 0; transform: translateY(0); }
  40% { opacity: 0.9; }
  100% { opacity: 0; transform: translateY(-18px); }
}
@media (prefers-reduced-motion: reduce) {
  .cpr-field .spore { animation: none; opacity: 0.6; }
}

/* facts: little tags */
.cpr .cpr-facts { display: flex; flex-wrap: wrap; gap: 0.55rem; margin-top: 1.1rem; }
.cpr-facts li {
  background: var(--moss);
  border: 1px solid var(--edge);
  border-radius: 8px 18px 8px 18px;
  padding: 0.35rem 0.9rem;
  font-size: 0.92rem;
}

/* sections */
.cpr h2 {
  margin: 3rem 0 1rem;
  border: 0;
  padding: 0;
  font-family: Georgia, 'Times New Roman', serif;
  font-size: 1.6rem;
  font-weight: 700;
  color: #fff;
}
.cpr b { color: #fff; font-weight: 650; }
.cpr code { overflow-wrap: anywhere; }
.cpr kbd {
  font: inherit; font-size: 0.85em; font-weight: 700; color: var(--soil); background: var(--leaf);
  border-radius: 6px; padding: 0.05rem 0.45rem;
}

/* grades as two growth stages */
.cpr-grow { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; align-items: stretch; }
.cpr-stage {
  position: relative;
  background: var(--moss);
  border: 1px solid var(--edge);
  border-radius: 18px;
  padding: 1.2rem 1.35rem 1.25rem 4.6rem;
}
.cpr-stage svg { position: absolute; left: 1.1rem; top: 1.15rem; width: 2.6rem; height: 2.6rem; }
.cpr-stage .cap { fill: var(--cap); }
.cpr-stage .stem { fill: #efe6d2; }
.cpr-stage.expert { background: linear-gradient(160deg, var(--spore-soft), var(--moss) 65%); border-color: var(--spore); }
.cpr-stage.expert .cap { fill: var(--spore); }
.cpr-stage h3 { margin: 0; border: 0; padding: 0; font-size: 1.15rem; color: #fff; }
.cpr-stage .h { display: inline-block; margin: 0.2rem 0 0.5rem; font-weight: 800; color: var(--leaf); }
.cpr-stage.expert .h { color: var(--spore); }
.cpr-stage p { color: var(--mute); }
.cpr-note { margin-top: 0.9rem !important; color: var(--mute) !important; font-size: 0.95rem; }

/* the work loop: a basket of numbered caps */
.cpr-steps { counter-reset: cpr; display: grid; gap: 0.7rem; }
.cpr-steps li {
  counter-increment: cpr;
  position: relative;
  background: var(--moss);
  border: 1px solid var(--edge);
  border-radius: 14px;
  padding: 0.85rem 1rem 0.85rem 3.6rem;
}
.cpr-steps li::before {
  content: counter(cpr);
  position: absolute; left: 0.85rem; top: 0.8rem;
  width: 2rem; height: 1.45rem;
  border-radius: 1rem 1rem 0.3rem 0.3rem;
  background: var(--cap);
  color: var(--soil);
  font-weight: 800; font-size: 0.85rem;
  display: grid; place-items: center;
}

/* what grows where */
.cpr-zones { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1rem; }
.cpr-zone { border: 1px solid var(--edge); border-radius: 16px; padding: 1.1rem 1.25rem; background: var(--soil); }
.cpr-zone.two { border-color: var(--spore); }
.cpr-zone h3 { margin: 0 0 0.6rem; border: 0; padding: 0; font-size: 1.1rem; color: #fff; }
.cpr-chips { display: flex; flex-wrap: wrap; gap: 0.4rem; }
.cpr-chips li { font-size: 0.85rem; background: var(--bark); border-radius: 999px; padding: 0.15rem 0.65rem; color: var(--text); }
.cpr-chips li.new { background: var(--spore-soft); outline: 1px solid var(--spore); }

/* the illegal side */
.cpr-dark {
  border: 1px solid var(--spore);
  border-radius: 18px;
  padding: 1.2rem 1.35rem;
  background: repeating-linear-gradient(135deg, rgba(183, 155, 255, 0.05) 0 12px, transparent 12px 24px), var(--soil);
}
.cpr-dark p + p { margin-top: 0.7rem; }
.cpr-dark em { color: var(--spore); font-style: normal; font-weight: 650; }

/* tips */
.cpr-tips li { padding: 0.8rem 0 0.8rem 1.6rem; border-top: 1px solid var(--edge); position: relative; }
.cpr-tips li:last-child { border-bottom: 1px solid var(--edge); }
.cpr-tips li::before {
  content: ''; position: absolute; left: 0.2rem; top: 1.25rem; width: 0.65rem; height: 0.65rem;
  border-radius: 0 60% 0 60%; background: var(--leaf);
}

.cpr a:focus-visible { outline: 3px solid var(--leaf); outline-offset: 2px; }
</style>

<div class="cpr">

<section class="cpr-hero">
<h1>Ciupercar <span class="cpr-hrs">- 10h/40h</span></h1>
<p>Un cos, o padure si ochi buni. Intri in zona de cules, aduni ciupercile de pe jos si le vinzi in oras. Cu experienta ajungi intr-o zona noua, cu ciuperci mai rare.</p>
<svg class="cpr-field" viewBox="0 0 640 220" role="img" aria-label="Harta cu doua zone de cules: zona 1 pentru toti ciupercarii si zona 2 pentru culegatorii experti">
<path class="path" d="M300 200 C 260 170, 210 150, 170 120 M300 200 C 360 175, 420 150, 470 118"/>
<circle class="z1" cx="160" cy="100" r="88"/>
<circle class="z2" cx="480" cy="100" r="88"/>
<text class="lbl1" x="96" y="205">Zona 1 · 10h</text>
<text class="lbl2" x="418" y="205">Zona 2 · 40h</text>
<rect class="hut" x="288" y="186" width="24" height="18" rx="3"/>
<text x="270" y="180">sef</text>
<g transform="translate(120 70)"><path class="cap" d="M-12 0 Q0 -16 12 0 Z"/><rect class="stem" x="-3" y="0" width="6" height="9" rx="2"/></g>
<g transform="translate(180 60)"><path class="cap" d="M-9 0 Q0 -12 9 0 Z"/><rect class="stem" x="-2.5" y="0" width="5" height="7" rx="2"/></g>
<g transform="translate(205 115)"><path class="cap" d="M-12 0 Q0 -16 12 0 Z"/><rect class="stem" x="-3" y="0" width="6" height="9" rx="2"/></g>
<g transform="translate(140 135)"><path class="cap" d="M-9 0 Q0 -12 9 0 Z"/><rect class="stem" x="-2.5" y="0" width="5" height="7" rx="2"/></g>
<g transform="translate(100 112)"><path class="cap" d="M-7 0 Q0 -10 7 0 Z"/><rect class="stem" x="-2" y="0" width="4" height="6" rx="2"/></g>
<g transform="translate(440 65)"><path class="cap" d="M-12 0 Q0 -16 12 0 Z"/><rect class="stem" x="-3" y="0" width="6" height="9" rx="2"/></g>
<g transform="translate(505 55)"><path class="cap2" d="M-10 0 Q0 -14 10 0 Z"/><rect class="stem" x="-2.5" y="0" width="5" height="8" rx="2"/></g>
<g transform="translate(530 120)"><path class="cap" d="M-9 0 Q0 -12 9 0 Z"/><rect class="stem" x="-2.5" y="0" width="5" height="7" rx="2"/></g>
<g transform="translate(470 140)"><path class="cap2" d="M-12 0 Q0 -16 12 0 Z"/><rect class="stem" x="-3" y="0" width="6" height="9" rx="2"/></g>
<g transform="translate(420 115)"><path class="cap" d="M-7 0 Q0 -10 7 0 Z"/><rect class="stem" x="-2" y="0" width="4" height="6" rx="2"/></g>
<circle class="spore" cx="505" cy="40" r="2.5"/>
<circle class="spore" cx="498" cy="44" r="2"/>
<circle class="spore" cx="512" cy="46" r="2"/>
<circle class="spore" cx="470" cy="122" r="2.5"/>
<circle class="spore" cx="463" cy="127" r="2"/>
<circle class="spore" cx="478" cy="128" r="2"/>
</svg>
<ul class="cpr-facts">
<li>Lucrezi singur, in ritmul tau</li>
<li>Vii cu ce transport vrei</li>
<li>Plata depinde de ciupercile vandute</li>
</ul>
</section>

<h2>Cum ma angajez?</h2>
<p>Ai nevoie de <b>10 ore jucate</b>. Angajeaza-te ca <b>Culegator de ciuperci</b> la Primarie (<code>Telefon → Harti → Locatii importante → Primarie</code>) sau direct de la seful ciupercarilor, cu <kbd>E</kbd>. Dupa angajare, pe harta apar cercurile verzi cu zonele de cules in care ai voie sa intri.</p>

<h2>Grade</h2>
<div class="cpr-grow">
<div class="cpr-stage">
<svg viewBox="-20 -20 40 40" aria-hidden="true"><path class="cap" d="M-15 2 Q0 -20 15 2 Z"/><rect class="stem" x="-4" y="2" width="8" height="13" rx="3"/></svg>
<h3>Culegator</h3>
<span class="h">10 ore</span>
<p>Culegi in <b>Zona 1</b>, aproape de sef. Ciuperci obisnuite, bune pentru inceput.</p>
</div>
<div class="cpr-stage expert">
<svg viewBox="-20 -20 40 40" aria-hidden="true"><path class="cap" d="M-15 2 Q0 -20 15 2 Z"/><rect class="stem" x="-4" y="2" width="8" height="13" rx="3"/></svg>
<h3>Culegator expert</h3>
<span class="h">40 ore</span>
<p>Se deschide si <b>Zona 2</b>, mai departe, spre vest. Acolo cresc mai multe soiuri, printre care si ciuperci halucinogene.</p>
</div>
</div>
<p class="cpr-note">Promovarea tine doar de orele jucate: cand le ai, deschide meniul sefului si urci automat in grad. Progresul il vezi in meniul lui, la <b>Skill-uri si promovare</b>. Daca te angajezi cand ai deja 40 de ore, incepi direct ca expert.</p>

<h2>Cum culegi</h2>
<ul class="cpr-steps">
<li><b>Mergi intr-o zona de cules.</b> Cand intri in cerc, intri automat in tura.</li>
<li><b>Cauta ciupercile de pe jos.</b> Cand esti aproape, deasupra lor apare <b>Culege</b>.</li>
<li><b>Apasa <kbd>E</kbd></b> langa ciuperca. Trebuie sa fii pe jos, nu in masina.</li>
<li><b>Stai pe loc</b> pana se umple bara <b>Culegi ciuperca...</b> Daca anulezi, nu primesti nimic.</li>
<li><b>Ciuperca intra in inventar,</b> uneori mai multe bucati odata. Cand iesi din zona, iesi si din tura.</li>
<li><b>Vinde-le</b> la <b>Punctul de vanzare ciuperci</b>, marcat pe harta, in oras. Plata depinde de soiul ciupercii.</li>
</ul>

<h2>Ce gasesti</h2>
<div class="cpr-zones">
<div class="cpr-zone">
<h3>Zona 1</h3>
<ul class="cpr-chips">
<li>Stridie</li>
<li>Hrib</li>
<li>Muscarita</li>
<li>Mycena</li>
<li>Palaria sarpelui</li>
<li>Zbarciog</li>
<li>Regala</li>
</ul>
</div>
<div class="cpr-zone two">
<h3>Zona 2</h3>
<ul class="cpr-chips">
<li>Tot ce e in Zona 1</li>
<li class="new">Buretele viperei</li>
<li class="new">Soiuri noi de hrib, mycena si stridie</li>
<li class="new">Halucinogena</li>
</ul>
</div>
</div>

<h2>Partea ascunsa</h2>
<div class="cpr-dark">
<p>Ciupercile <em>halucinogene</em> din Zona 2 nu se vand la punctul obisnuit. Din ele se pot face substante interzise, la o ferma din Grapeseed. <b>Asta este o activitate ilegala</b>, cu tot riscul care vine cu ea.</p>
<p>Unde gasesti restul, afli din indicii. Unul te asteapta in zona de cules, altul il primesti uneori chiar cand culegi o ciuperca halucinogena.</p>
</div>

<h2>Sfaturi</h2>
<ul class="cpr-tips">
<li><b>Fa loc in inventar.</b> Cu inventarul plin nu poti culege nimic.</li>
<li><b>Ciupercile sunt ale tuturor.</b> Ce culege alt jucator dispare si pentru tine. Ciupercile cresc la loc dupa o vreme.</li>
<li><b>Prinde Happy Hour-ul.</b> In orele de Happy Hour primesti mai multe ciuperci la fiecare cules.</li>
<li><b>Uniforma o iei de la sef,</b> din garderoba jobului sau dintr-o tinuta salvata.</li>
<li><b>Daca renunti la job,</b> ciupercile dispar de pe jos si nu mai poti culege.</li>
</ul>
</div>
