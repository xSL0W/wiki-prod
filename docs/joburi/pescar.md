---
outline: false
---

<style>
.pf {
  --abyss: #04121c;
  --deep: #072033;
  --water: #0b2c44;
  --shelf: #123a56;
  --rule: #1d4a68;
  --text: #e3f1f7;
  --mute: #93b3c3;
  --sonar: #3ef2b0;
  --sonar-soft: rgba(62, 242, 176, 0.13);
  --coral: #ff8a6b;
  max-width: 920px;
  margin: 0 auto;
  color: var(--text);
  font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.pf *, .pf *::before, .pf *::after { box-sizing: border-box; }
.pf p, .pf li { line-height: 1.6; color: var(--text); margin: 0; }
.pf ul, .pf ol { list-style: none; padding: 0; margin: 0; }
.pf code { white-space: normal; overflow-wrap: anywhere; }
/* hero: a sonar cross-section of the three depths */
.pf-hero {
  position: relative;
  background: radial-gradient(120% 90% at 85% 0%, var(--water), var(--abyss) 70%);
  border: 1px solid var(--rule);
  border-radius: 22px;
  padding: clamp(1.25rem, 4vw, 2.5rem);
  overflow: hidden;
}
.pf-hero h1 {
  display: flex; flex-wrap: wrap; align-items: center; gap: 0.2em 0.35em;
  margin: 0 0 0.6rem; border: 0; padding: 0;
  font-size: clamp(2rem, 6vw, 3.4rem); line-height: 1.05; font-weight: 800; letter-spacing: -0.03em; color: #fff;
}
.pf-hero h1 .pf-tail { display: inline-flex; align-items: center; gap: 0.35em; white-space: nowrap; }
.pf-hero h1 .pf-dash { color: var(--mute); font-weight: 500; }
.pf-hero h1 .pf-hours {
  font-family: ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace;
  font-size: 0.55em; letter-spacing: 0; color: var(--abyss); background: var(--sonar);
  border-radius: 999px; padding: 0.15em 0.6em;
}
.pf-hero p { max-width: 54ch; color: var(--mute); font-size: 1.05rem; }
.pf-sonar { display: block; width: 100%; height: auto; margin-top: 1.4rem; }
.pf-sonar .band1 { fill: #0d3550; }
.pf-sonar .band2 { fill: #0a2a41; }
.pf-sonar .band3 { fill: #061b2b; }
.pf-sonar .floor { fill: #03101a; }
.pf-sonar .surface { fill: none; stroke: var(--mute); stroke-width: 2; opacity: 0.6; }
.pf-sonar .grid { stroke: var(--rule); stroke-width: 1; stroke-dasharray: 3 7; }
.pf-sonar .line { stroke: var(--text); stroke-width: 1.5; opacity: 0.75; }
.pf-sonar .boat { fill: var(--text); }
.pf-sonar .hook { fill: none; stroke: var(--sonar); stroke-width: 3; stroke-linecap: round; }
.pf-sonar .blip { fill: var(--sonar); }
.pf-sonar .blip.rare { fill: var(--coral); }
.pf-sonar .ping { fill: none; stroke: var(--sonar); stroke-width: 2; opacity: 0; transform-box: fill-box; transform-origin: center; }
.pf-sonar .lbl { fill: var(--text); font-size: 17px; font-weight: 700; font-family: inherit; }
.pf-sonar .sub { fill: var(--mute); font-size: 15px; font-family: ui-monospace, Menlo, Consolas, monospace; }
.pf-sonar .drop { animation: pf-drop 5s ease-in-out infinite alternate; }
.pf-sonar .ping { animation: pf-ping 3s ease-out infinite; }
.pf-sonar .ping.d2 { animation-delay: 1s; }
.pf-sonar .ping.d3 { animation-delay: 2s; }
.pf-sonar .blip { animation: pf-blink 3s ease-in-out infinite; }
.pf-sonar .blip:nth-of-type(2n) { animation-delay: 1.4s; }
@keyframes pf-drop { from { transform: translateY(0); } to { transform: translateY(150px); } }
@keyframes pf-ping { 0% { opacity: 0.9; transform: scale(0.2); } 100% { opacity: 0; transform: scale(1.6); } }
@keyframes pf-blink { 0%, 100% { opacity: 0.35; } 50% { opacity: 1; } }
@media (prefers-reduced-motion: reduce) {
  .pf-sonar .drop, .pf-sonar .ping, .pf-sonar .blip { animation: none; }
  .pf-sonar .ping { opacity: 0.35; transform: none; }
}
/* sections */
.pf h2 {
  display: flex; align-items: center; gap: 0.6rem;
  margin: 3rem 0 1rem; border: 0; padding: 0;
  font-size: 1.5rem; font-weight: 750; letter-spacing: -0.015em; color: #fff;
}
.pf h2::before {
  content: ''; width: 12px; height: 12px; border-radius: 50%; flex: none;
  background: var(--sonar); box-shadow: 0 0 0 5px var(--sonar-soft);
}
.pf h3 { margin: 0; border: 0; padding: 0; color: #fff; }
.pf b { color: #fff; font-weight: 650; }
.pf kbd {
  font: inherit; font-size: 0.85em; font-weight: 700; color: var(--abyss); background: var(--sonar);
  border-radius: 6px; padding: 0.05rem 0.45rem;
}
.pf-lead { max-width: 64ch; }
.pf-lead + .pf-lead { margin-top: 0.8rem; }
/* depth levels = the grades */
.pf-depths { display: grid; gap: 0.9rem; }
.pf-depth {
  display: grid; grid-template-columns: minmax(0, 9.5rem) minmax(0, 1fr); gap: 1rem 1.4rem;
  border: 1px solid var(--rule); border-radius: 18px; padding: 1.2rem 1.4rem;
}
.pf-depth.l1 { background: linear-gradient(100deg, #0f3b58, var(--deep) 70%); }
.pf-depth.l2 { background: linear-gradient(100deg, #0b2d45, var(--deep) 70%); }
.pf-depth.l3 { background: linear-gradient(100deg, #061a29, #04121c 70%); border-color: #2a5f80; }
.pf-gauge { font-family: ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; }
.pf-gauge .h { display: block; font-size: 2rem; font-weight: 800; line-height: 1; color: var(--sonar); }
.pf-gauge .n { display: block; margin-top: 0.4rem; font-size: 0.8rem; letter-spacing: 0.08em; text-transform: uppercase; color: var(--mute); }
.pf-depth h3 { font-size: 1.15rem; margin-bottom: 0.35rem; }
.pf-depth p { color: var(--mute); }
/* inside each depth: what you need / what you catch / the special catch */
.pf-kit { grid-column: 1 / -1; display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1.3fr) minmax(0, 1fr); gap: 0.7rem; }
.pf-box { background: rgba(4, 18, 28, 0.55); border: 1px solid var(--rule); border-radius: 12px; padding: 0.75rem 0.9rem; }
.pf .pf-box h4 {
  margin: 0 0 0.5rem; padding: 0; border: 0; font: 700 0.72rem/1.2 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace;
  letter-spacing: 0.1em; text-transform: uppercase; color: var(--mute);
}
.pf .pf-need li { margin: 0; padding: 0.25rem 0; color: var(--text); font-size: 0.92rem; line-height: 1.3; }
.pf .pf-need li + li { border-top: 1px solid var(--rule); }
.pf .pf-need li small { display: block; color: var(--mute); font-size: 0.78rem; }
.pf .pf-need li.bait span { color: var(--sonar); }
.pf .pf-fish { display: flex; flex-wrap: wrap; gap: 0.35rem; }
.pf .pf-fish li { margin: 0; font-size: 0.85rem; border: 1px solid var(--rule); border-radius: 999px; padding: 0.1rem 0.6rem; color: var(--text); }
@media (max-width: 760px) { .pf-kit { grid-template-columns: minmax(0, 1fr); } }
.pf .pf-box.special { border-color: var(--coral); background: linear-gradient(150deg, rgba(255, 138, 107, 0.16), rgba(4, 18, 28, 0.55) 70%); }
.pf .pf-box.special h4 { color: var(--coral); }
.pf .pf-box.special strong { display: block; color: #fff; font-size: 1.05rem; margin-bottom: 0.2rem; }
.pf .pf-box.special p { color: var(--mute); font-size: 0.9rem; }
@media (max-width: 560px) {
  .pf-depth { grid-template-columns: minmax(0, 1fr); }
  .pf-gauge .h { display: inline; font-size: 1.6rem; }
  .pf-gauge .n { display: inline; margin: 0 0 0 0.5rem; }
}
.pf .pf-note { margin-top: 0.9rem; color: var(--mute); font-size: 0.95rem; }
/* the cast, as a line going down */
.pf .pf-cast { position: relative; padding-left: 2.4rem; }
.pf-cast li:not(:last-child)::after {
  content: ''; position: absolute; left: calc(-2.4rem + 0.725rem - 1px); top: 1.5rem; bottom: 0.05rem; width: 2px;
  background: linear-gradient(var(--mute), var(--sonar));
}
.pf .pf-cast li { position: relative; margin: 0; padding-bottom: 1.2rem; counter-increment: pf-step; }
.pf-cast li:last-child { padding-bottom: 0; }
.pf-cast li::before {
  content: counter(pf-step); position: absolute; left: -2.4rem; top: 0.05rem;
  width: 1.45rem; height: 1.45rem; border-radius: 50%; display: grid; place-items: center;
  font-size: 0.78rem; font-weight: 800; color: var(--abyss); background: var(--sonar);
}
.pf-cast { counter-reset: pf-step; }
/* gear & spots */
.pf-spots { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 0.9rem; }
.pf-spot { background: var(--deep); border: 1px solid var(--rule); border-radius: 16px; padding: 1.1rem 1.25rem; }
.pf-spot h3 { font-size: 1.05rem; margin-bottom: 0.4rem; }
.pf-spot p { color: var(--mute); font-size: 0.97rem; }
.pf-pearls { display: flex; gap: 0.35rem; margin-top: 0.7rem; }
.pf-pearls span { width: 14px; height: 14px; border-radius: 50%; box-shadow: inset -3px -3px 5px rgba(0,0,0,0.35); }
/* tips */
.pf-tips li { display: grid; grid-template-columns: 1.4rem minmax(0, 1fr); gap: 0.6rem; padding: 0.8rem 0; border-top: 1px solid var(--rule); }
.pf-tips li:last-child { border-bottom: 1px solid var(--rule); }
.pf-tips li::before { content: ''; width: 9px; height: 9px; margin-top: 0.55rem; border-radius: 50%; background: var(--coral); }
.pf a { color: var(--sonar); }
.pf a:focus-visible { outline: 3px solid var(--sonar); outline-offset: 2px; border-radius: 4px; }
/* block list: keeps the 8px row spacing the theme no longer adds to classed lists */
.pf .pf-tips > li + li { margin-top: 8px; }
</style>

<div class="pf">

<section class="pf-hero">
<h1><span>Pescar</span> <span class="pf-tail"><span class="pf-dash">-</span> <span class="pf-hours">25h/200h/500h</span></span></h1>
<p>Undita, momeala si rabdare. Incepi pe pontonul de la plaja, iar cu orele jucate cobori tot mai adanc: pe Lacul Alamo si apoi in largul oceanului, dupa pesti mai mari.</p>
<svg class="pf-sonar" viewBox="0 0 640 300" role="img" aria-label="Sectiune prin apa, cu trei adancimi: ponton la 25 de ore, Lacul Alamo la 200 de ore si ocean la 500 de ore">
<rect class="band1" x="0" y="44" width="640" height="70"/>
<rect class="band2" x="0" y="114" width="640" height="80"/>
<rect class="band3" x="0" y="194" width="640" height="80"/>
<path class="floor" d="M0 300 L0 282 C 90 268, 170 292, 260 280 S 430 264, 520 284 S 610 276, 640 270 L640 300 Z"/>
<path class="surface" d="M0 44 C 40 36, 80 52, 120 44 S 200 36, 240 44 S 320 52, 360 44 S 440 36, 480 44 S 560 52, 640 44"/>
<line class="grid" x1="0" y1="114" x2="640" y2="114"/>
<line class="grid" x1="0" y1="194" x2="640" y2="194"/>
<path class="boat" d="M418 40 L494 40 L482 52 L430 52 Z"/>
<rect class="boat" x="446" y="28" width="22" height="12" rx="2"/>
<clipPath id="pf-below-boat"><rect x="0" y="40" width="640" height="260"/></clipPath>
<g clip-path="url(#pf-below-boat)">
<g class="drop">
<line class="line" x1="470" y1="-120" x2="470" y2="92"/>
<path class="hook" d="M470 92 v10 a6 6 0 0 1 -12 0"/>
</g>
</g>
<circle class="ping" cx="470" cy="160" r="26"/>
<circle class="ping d2" cx="470" cy="160" r="26"/>
<circle class="ping d3" cx="470" cy="160" r="26"/>
<ellipse class="blip" cx="300" cy="82" rx="9" ry="4"/>
<ellipse class="blip" cx="352" cy="96" rx="7" ry="3"/>
<ellipse class="blip rare" cx="560" cy="78" rx="6" ry="3"/>
<ellipse class="blip" cx="250" cy="150" rx="12" ry="5"/>
<ellipse class="blip" cx="590" cy="170" rx="11" ry="5"/>
<ellipse class="blip rare" cx="370" cy="164" rx="8" ry="4"/>
<ellipse class="blip" cx="300" cy="236" rx="18" ry="7"/>
<ellipse class="blip" cx="560" cy="246" rx="15" ry="6"/>
<ellipse class="blip rare" cx="380" cy="252" rx="7" ry="4"/>
<text class="lbl" x="16" y="78">Ponton</text>
<text class="sub" x="16" y="100">25h</text>
<text class="lbl" x="16" y="152">Lacul Alamo</text>
<text class="sub" x="16" y="174">200h</text>
<text class="lbl" x="16" y="232">Ocean</text>
<text class="sub" x="16" y="254">500h</text>
</svg>
</section>

<h2>Cum incep?</h2>
<p class="pf-lead">Angajeaza-te ca <b>Pescar</b> la Primarie (<code>Telefon → Harti → Locatii importante → Primarie</code>) sau direct de la <b>seful pescar</b>. Ai nevoie de minim <b>25 de ore</b> jucate pe server.</p>
<p class="pf-lead">Seful pescar sta pe pontonul de la plaja din Los Santos (<code>Telefon → Harti → Locatii job-uri → Job pescar nivel 1</code>). Mai e unul si in Sandy Shores, langa Lacul Alamo. Langa seful de la plaja gasesti si magazinul pescaresc si masa de momeala.</p>

<h2>Trei adancimi, trei grade</h2>
<div class="pf-depths">
<div class="pf-depth l1">
<div class="pf-gauge"><span class="h">25h</span><span class="n">Pescar</span></div>
<div>
<h3>Pontonul de la plaja</h3>
<p>Locul de inceput, chiar sub seful pescar. Pescuiesti de pe ponton, la mal.</p>
</div>
<div class="pf-kit">
<div class="pf-box">
<h4>Ai nevoie de</h4>
<ul class="pf-need">
<li><span><img class="eg-item" src="/items/pescar_undita.webp" alt="">Undita</span><small>magazin pescaresc</small></li>
<li class="bait"><span><img class="eg-item" src="/items/pescar_rame_premium.webp" alt="">Rame premium</span><small>zona de rame, gratis</small></li>
<li class="bait"><span>sau <img class="eg-item" src="/items/pescar_rame.webp" alt="">Rame</span><small>magazin pescaresc</small></li>
</ul>
</div>
<div class="pf-box">
<h4>Poti prinde</h4>
<ul class="pf-fish">
<li><img class="eg-item" src="/items/pescar_caras.webp" alt="">Caras mic</li>
<li><img class="eg-item" src="/items/pescar_platica.webp" alt="">Platica mica</li>
<li><img class="eg-item" src="/items/pescar_hamsii.webp" alt="">Hamsii mici</li>
<li><img class="eg-item" src="/items/pescar_morunas.webp" alt="">Morunas mic</li>
<li><img class="eg-item" src="/items/pescar_sprot.webp" alt="">Sprot mic</li>
<li><img class="eg-item" src="/items/pescar_guvid.webp" alt="">Guvid mic</li>
<li><img class="eg-item" src="/items/pescar_rosioara.webp" alt="">Rosioara mica</li>
</ul>
</div>
<div class="pf-box special">
<h4>Captura speciala</h4>
<strong><img class="eg-item" src="/items/pescar_homar.webp" alt="">Homar mic</strong>
<p>Il prinzi doar cu <b>Rame premium</b>. Cu rame obisnuite nu musca, iar uneori scoti gunoi.</p>
</div>
</div>
</div>
<div class="pf-depth l2">
<div class="pf-gauge"><span class="h">200h</span><span class="n">Pescar profesionist</span></div>
<div>
<h3>Lacul Alamo</h3>
<p>Zona e pe lac, langa Sandy Shores.</p>
</div>
<div class="pf-kit">
<div class="pf-box">
<h4>Ai nevoie de</h4>
<ul class="pf-need">
<li><span><img class="eg-item" src="/items/pescar_undita.webp" alt="">Undita</span><small>magazin pescaresc</small></li>
<li class="bait"><span><img class="eg-item" src="/items/pescar_nada2.webp" alt="">Nada medie</span><small>masa de momeala</small></li>
<li class="bait"><span>sau <img class="eg-item" src="/items/pescar_naluca2.webp" alt="">Naluca medie</span><small>magazin pescaresc</small></li>
<li><span>Barca</span><small>obligatorie</small></li>
</ul>
</div>
<div class="pf-box">
<h4>Poti prinde</h4>
<ul class="pf-fish">
<li><img class="eg-item" src="/items/pescar_somn.webp" alt="">Somn mediu</li>
<li><img class="eg-item" src="/items/pescar_salau.webp" alt="">Salau mediu</li>
<li><img class="eg-item" src="/items/pescar_biban.webp" alt="">Biban mediu</li>
<li><img class="eg-item" src="/items/pescar_avat.webp" alt="">Avat mediu</li>
<li><img class="eg-item" src="/items/pescar_pastrav.webp" alt="">Pastrav mediu</li>
<li><img class="eg-item" src="/items/pescar_stiuca.webp" alt="">Stiuca medie</li>
<li><img class="eg-item" src="/items/pescar_clean.webp" alt="">Clean mediu</li>
</ul>
</div>
<div class="pf-box special">
<h4>Captura speciala</h4>
<strong><img class="eg-item" src="/items/pescar_mandarin.webp" alt="">Mandarin mediu</strong>
<p>Il prinzi doar cu <b>Nada medie</b>. Cu naluca nu musca, iar uneori scoti gunoi.</p>
</div>
</div>
</div>
<div class="pf-depth l3">
<div class="pf-gauge"><span class="h">500h</span><span class="n">Pescar expert</span></div>
<div>
<h3>Largul oceanului</h3>
<p>Zona e in larg, in sudul hartii.</p>
</div>
<div class="pf-kit">
<div class="pf-box">
<h4>Ai nevoie de</h4>
<ul class="pf-need">
<li><span><img class="eg-item" src="/items/pescar_undita.webp" alt="">Undita</span><small>magazin pescaresc</small></li>
<li class="bait"><span><img class="eg-item" src="/items/pescar_nada3.webp" alt="">Nada mare</span><small>masa de momeala</small></li>
<li class="bait"><span>sau <img class="eg-item" src="/items/pescar_naluca3.webp" alt="">Naluca mare</span><small>magazin pescaresc</small></li>
<li><span>Barca</span><small>obligatorie</small></li>
</ul>
</div>
<div class="pf-box">
<h4>Poti prinde</h4>
<ul class="pf-fish">
<li><img class="eg-item" src="/items/pescar_ton.webp" alt="">Ton mare</li>
<li><img class="eg-item" src="/items/pescar_sturion.webp" alt="">Sturion mare</li>
<li><img class="eg-item" src="/items/pescar_cega.webp" alt="">Cega mare</li>
<li><img class="eg-item" src="/items/pescar_pastruga.webp" alt="">Pastruga mare</li>
<li><img class="eg-item" src="/items/pescar_morun.webp" alt="">Morun mare</li>
<li><img class="eg-item" src="/items/pescar_spada.webp" alt="">Peste spada mare</li>
<li><img class="eg-item" src="/items/pescar_tipar.webp" alt="">Tipar mare</li>
</ul>
</div>
<div class="pf-box special">
<h4>Captura speciala</h4>
<strong><img class="eg-item" src="/items/pescar_scoica.webp" alt="">Scoica</strong>
<p>O prinzi doar cu <b>Nada mare</b>. Cu naluca n-o prinzi, iar uneori scoti gunoi. Scoica o deschizi din inventar: poate avea o perla sau doar gunoi.</p>
</div>
</div>
</div>
</div>
<p class="pf-note">Promovarea e automata: cand ai orele necesare, treci pe la seful pescar si primesti gradul urmator. Daca te angajezi cand ai deja orele, incepi direct la gradul potrivit. Poti pescui in zona gradului tau si in toate zonele de sub el; pe harta vezi doar zonele in care ai voie. Fiecare zona primeste doar momeala ei.</p>

<h2>O aruncare, pas cu pas</h2>
<ol class="pf-cast">
<li><b>Intra in zona de pescuit.</b> Pe ecran apare <b>Esti in zona de pescuit</b>.</li>
<li><b>Foloseste <img class="eg-item" src="/items/pescar_undita.webp" alt="">Undita</b> din inventar. Fiecare aruncare consuma o momeala potrivita zonei.</li>
<li><b>Asteapta sa muste.</b> Stai pe loc pana se umple bara. Cu cat zona e mai grea, cu atat astepti mai mult. Te opresti oricand cu <kbd>Backspace</kbd>.</li>
<li><b>Pestele musca si il scoti singur.</b> Apare <b>Ai prins ceva!</b>, iar captura intra in inventar. Arunca din nou si continua.</li>
</ol>

<h2>Momeala, vanzare si perle</h2>
<div class="pf-spots">
<div class="pf-spot">
<h3>Magazin pescaresc</h3>
<p>Langa seful de la plaja, doar pentru pescari. Aici iei <b><img class="eg-item" src="/items/pescar_undita.webp" alt="">Undita</b>, <b><img class="eg-item" src="/items/pescar_rame.webp" alt="">Rame</b>, <b><img class="eg-item" src="/items/pescar_naluca2.webp" alt="">Naluca medie</b> si <b><img class="eg-item" src="/items/pescar_naluca3.webp" alt="">Naluca mare</b>.</p>
</div>
<div class="pf-spot">
<h3>Masa de momeala</h3>
<p>Tot langa sef. Faci <b><img class="eg-item" src="/items/pescar_nada2.webp" alt="">Nada medie</b> din pestii de la ponton si <b><img class="eg-item" src="/items/pescar_nada3.webp" alt="">Nada mare</b> din pestii de pe Lacul Alamo.</p>
</div>
<div class="pf-spot">
<h3>Zona de rame</h3>
<p>Marcata pe harta. Mergi la locul aratat si apasa <kbd>E</kbd> pe <b>Ia rame</b> ca sa culegi <b><img class="eg-item" src="/items/pescar_rame_premium.webp" alt="">Rame premium</b>, gratis. Dupa fiecare cules, locul se muta.</p>
</div>
<div class="pf-spot">
<h3>Punct de vanzare peste</h3>
<p>Pe coasta de vest (<code>Telefon → Harti → Puncte de vanzare/cumparare pentru joburi</code>). Primeste pestele de la toate cele trei adancimi, doar de la pescari. Plata depinde de ce prinzi.</p>
</div>
<div class="pf-spot">
<h3>Scoica si perlele</h3>
<p>Foloseste <b><img class="eg-item" src="/items/pescar_scoica.webp" alt="">Scoica</b> din inventar ca s-o deschizi. Poate avea o perla sau doar gunoi. Perlele le vinzi la <b>Punctul de vanzare perle</b>, din Rockford Hills.</p>
<div class="pf-pearls" aria-hidden="true"><span style="background:#f4f1ea"></span><span style="background:#4fc98a"></span><span style="background:#4d8ff0"></span><span style="background:#e0505a"></span><span style="background:#f2c14e"></span></div>
</div>
</div>

<h2>Sfaturi</h2>
<ul class="pf-tips">
<li><span><b>Ai grija la greutate.</b> Pestele prins intra in inventar chiar daca te supraincarca, dar cat timp esti supraincarcat nu mai poti arunca. Vinde sau lasa din peste.</span></li>
<li><span><b>Pastreaza un slot liber.</b> Fara loc in inventar, pestele scapa.</span></li>
<li><span><b>Nu inota si nu iesi din zona.</b> Daca pestele musca in timp ce esti in apa sau in afara zonei, pescuitul se opreste.</span></li>
<li><span><b>Nu pescui de la volan.</b> Din vehicul nu merge. Pe barca, opreste si ridica-te de la carma.</span></li>
<li><span><b>Fii atent la Happy Hour.</b> Cand e activ pentru pescari, prinzi mai mult peste la fiecare captura.</span></li>
</ul>

</div>
