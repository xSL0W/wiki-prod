---
outline: false
---

<style>
.xmag {
  --dark: #0f0a12;
  --shelf: #1a1220;
  --aisle: #241a2c;
  --edge: #3a2c45;
  --text: #f1e9f4;
  --mute: #ab9cb3;
  --neon: #ff3da5;
  --neon-soft: rgba(255, 61, 165, 0.14);
  --amber: #ffb547;
  --paper: #eee8db;
  --ink: #2b2620;
  --ink-mute: #6f675b;
  --mono: ui-monospace, 'SFMono-Regular', 'Cascadia Mono', Consolas, monospace;
  max-width: 920px;
  margin: 0 auto;
  color: var(--text);
  font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.xmag *, .xmag *::before, .xmag *::after { box-sizing: border-box; }
.xmag p, .xmag li { line-height: 1.6; color: var(--text); margin: 0; }
.xmag ul, .xmag ol { list-style: none; padding: 0; margin: 0; }
.xmag li + li { margin-top: 0; }
.xmag b { color: #fff; font-weight: 650; }

/* hero: a neon 24/7 sign over a shop front */
.xmag-hero {
  position: relative;
  background:
    radial-gradient(90% 70% at 50% 0%, var(--neon-soft), transparent 70%),
    repeating-linear-gradient(90deg, transparent 0 46px, rgba(255, 255, 255, 0.025) 46px 48px),
    var(--dark);
  border: 1px solid var(--edge);
  border-radius: 22px;
  padding: clamp(1.25rem, 4vw, 2.5rem);
  text-align: center;
  overflow: hidden;
}
.xmag-sign { display: block; width: min(100%, 420px); height: auto; margin: 0 auto 1.2rem; }
.xmag-sign .frame { fill: none; stroke: var(--neon); stroke-width: 4; filter: url(#xmag-glow); }
.xmag-sign .num { fill: none; stroke: var(--neon); stroke-width: 5; stroke-linecap: round; stroke-linejoin: round; filter: url(#xmag-glow); }
.xmag-sign .num.amb { stroke: var(--amber); }
.xmag-sign .open { fill: var(--amber); font: 700 15px ui-monospace, Consolas, monospace; letter-spacing: 6px; }
.xmag-sign .flick { animation: xmag-flicker 5s infinite; }
@keyframes xmag-flicker {
  0%, 18%, 22%, 62%, 64%, 100% { opacity: 1; }
  20%, 63% { opacity: 0.25; }
}
.xmag .xmag-hero h1 {
  margin: 0 0 0.7rem;
  border: 0;
  padding: 0;
  font-size: clamp(2rem, 6.5vw, 3.4rem);
  line-height: 1.05;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: #fff;
}
.xmag-hrs {
  display: inline-flex;
  gap: 0.3em;
  white-space: nowrap;
  color: var(--neon);
  text-shadow: 0 0 22px rgba(255, 61, 165, 0.55);
}
.xmag .xmag-lead { max-width: 54ch; margin: 0 auto; color: var(--mute); font-size: 1.05rem; }
.xmag .xmag-chips { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.5rem; margin-top: 1.2rem; }
.xmag .xmag-chips li {
  margin: 0;
  font-size: 0.88rem;
  border: 1px solid var(--edge);
  background: var(--shelf);
  border-radius: 999px;
  padding: 0.3rem 0.85rem;
}
.xmag .xmag-chips li.xmag-hot { border-color: var(--neon); color: var(--neon); }

.xmag h2 {
  margin: 3rem 0 1rem;
  border: 0;
  padding: 0;
  font-size: 1.45rem;
  font-weight: 750;
  letter-spacing: -0.01em;
  color: #fff;
}

/* requirements: a till receipt next to the weapons card */
.xmag-duo { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr)); gap: 1.2rem; align-items: start; }
.xmag-receipt {
  position: relative;
  background: var(--paper);
  color: var(--ink);
  font-family: var(--mono);
  padding: 1.4rem 1.3rem 1.6rem;
  border-radius: 6px 6px 0 0;
  transform: rotate(-0.6deg);
  box-shadow: 0 18px 40px rgba(0, 0, 0, 0.45);
  margin-bottom: 14px;
}
.xmag-receipt::after {
  content: '';
  position: absolute;
  left: 0;
  right: 0;
  bottom: -14px;
  height: 14px;
  background:
    linear-gradient(135deg, var(--paper) 50%, transparent 50%) 0 0 / 14px 14px repeat-x,
    linear-gradient(225deg, var(--paper) 50%, transparent 50%) 0 0 / 14px 14px repeat-x;
}
.xmag .xmag-receipt p { color: var(--ink); font-size: 0.85rem; text-align: center; }
.xmag .xmag-receipt .xmag-shop { font-weight: 800; font-size: 1.05rem; letter-spacing: 0.12em; }
.xmag .xmag-receipt .xmag-small { color: var(--ink-mute); font-size: 0.75rem; }
.xmag .xmag-rule { border: 0; border-top: 1px dashed var(--ink-mute); margin: 0.8rem 0; }
.xmag .xmag-rows li {
  margin: 0;
  display: flex;
  align-items: baseline;
  gap: 0.4rem;
  color: var(--ink);
  font-size: 0.86rem;
  padding: 0.18rem 0;
}
.xmag .xmag-rows .xmag-dots { flex: 1; border-bottom: 1px dotted var(--ink-mute); transform: translateY(-0.25em); min-width: 1rem; }
.xmag .xmag-rows b { color: var(--ink); font-weight: 800; white-space: nowrap; }
.xmag .xmag-rows .xmag-x { color: #b3261e; }
.xmag .xmag-receipt .xmag-total { display: flex; justify-content: space-between; gap: 0.5rem; font-weight: 800; font-size: 0.95rem; color: var(--ink); text-align: left; }
.xmag-bars { display: block; width: 70%; height: 28px; margin: 0.9rem auto 0; }
.xmag-bars rect { fill: var(--ink); }

.xmag-arms { background: var(--shelf); border: 1px solid var(--edge); border-radius: 16px; padding: 1.2rem 1.3rem; }
.xmag .xmag-arms h3 { margin: 0 0 0.4rem; border: 0; padding: 0; font-size: 1.1rem; color: #fff; }
.xmag .xmag-arms > p { color: var(--mute); font-size: 0.95rem; }
.xmag .xmag-tags { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-top: 0.6rem; }
.xmag .xmag-tags li {
  margin: 0;
  font-size: 0.85rem;
  background: var(--aisle);
  border: 1px solid var(--edge);
  border-radius: 6px;
  padding: 0.15rem 0.55rem;
}
.xmag .xmag-tags.xmag-melee li { border-color: rgba(255, 181, 71, 0.45); color: var(--amber); }
.xmag .xmag-arms .xmag-group { margin-top: 1rem; font-size: 0.78rem; letter-spacing: 0.12em; text-transform: uppercase; color: var(--mute); }

/* flow: price-tag cards */
.xmag-steps { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 250px), 1fr)); gap: 0.9rem; counter-reset: xmag-step; }
.xmag .xmag-steps li {
  counter-increment: xmag-step;
  position: relative;
  margin: 0;
  background: var(--shelf);
  border: 1px solid var(--edge);
  border-radius: 14px;
  padding: 2.9rem 1.15rem 1.1rem;
}
.xmag .xmag-steps li::before {
  content: counter(xmag-step, decimal-leading-zero);
  position: absolute;
  top: 0.75rem;
  left: 1.15rem;
  font-family: var(--mono);
  font-weight: 800;
  font-size: 1.35rem;
  color: var(--neon);
  text-shadow: 0 0 14px rgba(255, 61, 165, 0.5);
}
.xmag .xmag-steps li.xmag-alarm { border-color: var(--neon); background: linear-gradient(160deg, var(--neon-soft), var(--shelf) 65%); }
.xmag .xmag-steps p { color: var(--mute); font-size: 0.95rem; }
.xmag .xmag-steps .xmag-t { display: block; color: #fff; margin-bottom: 0.25rem; font-size: 1.02rem; }
.xmag kbd {
  font-family: var(--mono);
  font-size: 0.85em;
  font-weight: 800;
  color: var(--dark);
  background: var(--amber);
  border: 0;
  border-radius: 5px;
  padding: 0.05rem 0.45rem;
}

/* risks: a CCTV frame */
.xmag-cctv {
  position: relative;
  background: #0b0b0d;
  border: 1px solid var(--edge);
  border-radius: 16px;
  padding: 2.6rem clamp(1rem, 3vw, 1.6rem) 1.3rem;
  overflow: hidden;
}
.xmag-cctv::before {
  content: '';
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(0deg, rgba(255, 255, 255, 0.025) 0 1px, transparent 1px 3px);
  pointer-events: none;
}
.xmag-cam {
  position: absolute;
  top: 0.8rem;
  left: 1rem;
  right: 1rem;
  display: flex;
  justify-content: space-between;
  font-family: var(--mono);
  font-size: 0.75rem;
  letter-spacing: 0.1em;
  color: var(--mute);
}
.xmag-rec { color: #ff4646; }
.xmag-rec::before {
  content: '';
  display: inline-block;
  width: 0.55rem;
  height: 0.55rem;
  margin-right: 0.4rem;
  border-radius: 50%;
  background: #ff4646;
  animation: xmag-rec 1.4s steps(1) infinite;
}
@keyframes xmag-rec { 50% { opacity: 0; } }
.xmag .xmag-risks li {
  position: relative;
  margin: 0;
  padding: 0.65rem 0 0.65rem 1.4rem;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
}
.xmag .xmag-risks li:first-child { border-top: 0; }
.xmag .xmag-risks li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 1.15rem;
  width: 0.55rem;
  height: 0.55rem;
  border: 2px solid var(--neon);
  transform: rotate(45deg);
}

.xmag-extra { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr)); gap: 1rem; }
.xmag-card { background: var(--shelf); border: 1px solid var(--edge); border-radius: 16px; padding: 1.2rem 1.3rem; }
.xmag .xmag-card h3 { margin: 0 0 0.45rem; border: 0; padding: 0; font-size: 1.08rem; color: #fff; }
.xmag .xmag-card p { color: var(--mute); }

.xmag a:focus-visible { outline: 3px solid var(--neon); outline-offset: 2px; border-radius: 4px; }
@media (prefers-reduced-motion: reduce) {
  .xmag-sign .flick, .xmag-rec::before { animation: none; }
}
</style>

<div class="xmag">

<section class="xmag-hero">
<svg class="xmag-sign" viewBox="0 0 420 150" role="img" aria-label="Firma luminoasa de neon 24/7 deschis non-stop">
<defs>
<filter id="xmag-glow" x="-20%" y="-40%" width="140%" height="180%">
<feGaussianBlur stdDeviation="3" result="b"/>
<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
</filter>
</defs>
<rect class="frame" x="10" y="10" width="400" height="130" rx="22"/>
<path class="num" d="M70 45 Q 70 30 88 30 Q 106 30 106 46 Q 106 58 70 92 L 108 92"/>
<path class="num" d="M150 30 L 126 72 L 162 72 M 152 52 L 152 96"/>
<path class="num amb flick" d="M200 100 L 232 26"/>
<path class="num" d="M262 32 L 298 32 L 274 96"/>
<text class="open" x="210" y="126" text-anchor="middle">DESCHIS NON-STOP</text>
</svg>
<h1>Jaf la magazin <span class="xmag-hrs"><span>-</span> <span>20h</span></span></h1>
<p class="xmag-lead">Intri intr-un magazin 24/7 cu arma in mana si il ameninti pe vanzator. El goleste casa de marcat, iar tu astepti sa se termine jaful cu politia deja pe drum.</p>
<ul class="xmag-chips">
<li>Singur</li>
<li>Minim 3 politisti in serviciu</li>
<li class="xmag-hot">Plata in bani murdari</li>
</ul>
</section>

<h2>Ce iti trebuie</h2>
<div class="xmag-duo">
<div class="xmag-receipt">
<p class="xmag-shop">24/7 MARKET</p>
<p class="xmag-small">BON DE JAF - NU ESTE DOCUMENT FISCAL</p>
<hr class="xmag-rule">
<ul class="xmag-rows">
<li>ORE JUCATE<span class="xmag-dots"></span><b>MIN. 20h</b></li>
<li>POLITISTI IN SERVICIU<span class="xmag-dots"></span><b>MIN. 3</b></li>
<li>JUCATORI<span class="xmag-dots"></span><b>1 (SINGUR)</b></li>
<li>ARMA IN MANA<span class="xmag-dots"></span><b>DA</b></li>
<li>POLITIST SAU MEDIC<span class="xmag-dots"></span><b class="xmag-x">NU</b></li>
<li>IN ZONA PROTEJATA<span class="xmag-dots"></span><b class="xmag-x">NU</b></li>
</ul>
<hr class="xmag-rule">
<p class="xmag-total"><span>TOTAL</span><span>BANI MURDARI</span></p>
<svg class="xmag-bars" viewBox="0 0 200 28" aria-hidden="true">
<rect x="0" y="0" width="3" height="28"/><rect x="6" y="0" width="1" height="28"/><rect x="10" y="0" width="4" height="28"/><rect x="17" y="0" width="2" height="28"/><rect x="22" y="0" width="1" height="28"/><rect x="26" y="0" width="5" height="28"/><rect x="34" y="0" width="2" height="28"/><rect x="39" y="0" width="1" height="28"/><rect x="43" y="0" width="3" height="28"/><rect x="49" y="0" width="1" height="28"/><rect x="53" y="0" width="4" height="28"/><rect x="60" y="0" width="2" height="28"/><rect x="65" y="0" width="1" height="28"/><rect x="69" y="0" width="3" height="28"/><rect x="75" y="0" width="5" height="28"/><rect x="83" y="0" width="1" height="28"/><rect x="87" y="0" width="2" height="28"/><rect x="92" y="0" width="3" height="28"/><rect x="98" y="0" width="1" height="28"/><rect x="102" y="0" width="4" height="28"/><rect x="109" y="0" width="2" height="28"/><rect x="114" y="0" width="1" height="28"/><rect x="118" y="0" width="5" height="28"/><rect x="126" y="0" width="2" height="28"/><rect x="131" y="0" width="1" height="28"/><rect x="135" y="0" width="3" height="28"/><rect x="141" y="0" width="1" height="28"/><rect x="145" y="0" width="4" height="28"/><rect x="152" y="0" width="2" height="28"/><rect x="157" y="0" width="3" height="28"/><rect x="163" y="0" width="1" height="28"/><rect x="167" y="0" width="5" height="28"/><rect x="175" y="0" width="2" height="28"/><rect x="180" y="0" width="1" height="28"/><rect x="184" y="0" width="4" height="28"/><rect x="191" y="0" width="2" height="28"/><rect x="196" y="0" width="4" height="28"/>
</svg>
</div>
<div class="xmag-arms">
<h3>Cu ce poti ameninta</h3>
<p>Vanzatorul se sperie doar daca ai arma in mana in clipa in care apesi <kbd>H</kbd>. Merg aproape toate armele de foc si cateva arme albe.</p>
<p class="xmag-group">Arme de foc</p>
<ul class="xmag-tags">
<li>Pistoale</li>
<li>Revolvere</li>
<li>SMG-uri</li>
<li>Pusti de asalt</li>
<li>Shotgun-uri</li>
<li>Pusti cu luneta</li>
<li>Mitraliere</li>
</ul>
<p class="xmag-group">Arme albe</p>
<ul class="xmag-tags xmag-melee">
<li><img class="eg-item" src="/items/WEAPON_KNIFE.webp" alt="">Cutit</li>
<li><img class="eg-item" src="/items/WEAPON_DAGGER.webp" alt="">Pumnal</li>
<li><img class="eg-item" src="/items/WEAPON_SWITCHBLADE.webp" alt="">Briceag</li>
<li><img class="eg-item" src="/items/WEAPON_MACHETE.webp" alt="">Maceta</li>
<li><img class="eg-item" src="/items/WEAPON_BAT.webp" alt="">Bata</li>
<li><img class="eg-item" src="/items/WEAPON_KNUCKLE.webp" alt="">Box</li>
<li><img class="eg-item" src="/items/WEAPON_HAMMER.webp" alt="">Ciocan</li>
<li><img class="eg-item" src="/items/WEAPON_HATCHET.webp" alt="">Topor</li>
<li><img class="eg-item" src="/items/WEAPON_BATTLEAXE.webp" alt="">Secure</li>
</ul>
</div>
</div>

<h2>Pas cu pas</h2>
<ol class="xmag-steps">
<li><p><b class="xmag-t">Intra intr-un magazin 24/7</b> Oricare din oras, cat timp vanzatorul e la tejghea si magazinul nu a fost jefuit de curand.</p></li>
<li><p><b class="xmag-t">Scoate arma si du-te la vanzator</b> Cand esti aproape de el, apare bula <b>Jefuieste</b>. Apasa <kbd>H</kbd>.</p></li>
<li class="xmag-alarm"><p><b class="xmag-t">Politia afla pe loc</b> Alerta pleaca in secunda in care incepe jaful, cu locul magazinului pe harta lor.</p></li>
<li><p><b class="xmag-t">Vanzatorul goleste casa</b> Ridica mainile, scoate banii si apoi se ghemuieste speriat dupa tejghea.</p></li>
<li><p><b class="xmag-t">Ramai in magazin</b> Asteapta pana se umple bara. Te poti misca prin magazin, dar nu poti alerga si nu poti urca in masina.</p></li>
<li><p><b class="xmag-t">Ia banii si fugi</b> Primesti <b><img class="eg-item" src="/items/dirtymoney.webp" alt="">Bani murdari</b> direct in inventar. Pleaca repede din zona.</p></li>
</ol>

<h2>Ce strica jaful</h2>
<div class="xmag-cctv">
<div class="xmag-cam"><span class="xmag-rec">REC</span><span>CAM 02 - CASA</span></div>
<ul class="xmag-risks">
<li><p><b>Iesi din magazin</b> inainte sa se umple bara. Jaful se anuleaza si nu primesti nimic.</p></li>
<li><p><b>Anulezi bara</b> sau iesi de pe server in timpul jafului. Jaful se termina fara bani.</p></li>
<li><p><b>Magazinul a fost jefuit de curand</b> sau il jefuieste deja altcineva. Alege alt magazin.</p></li>
<li><p><b>Ai dat deja un jaf la magazin.</b> Dupa fiecare jaf, reusit sau nu, astepti o pauza pana la urmatorul. Pauza porneste cand incepi jaful.</p></li>
<li><p><b>Sunt prea putini politisti in serviciu.</b> Sub 3, nu poti incepe.</p></li>
</ul>
</div>

<h2>In plus</h2>
<div class="xmag-extra">
<div class="xmag-card">
<h3>Happy Hour</h3>
<p>Cand Happy Hour e activ pentru jafurile la magazin, primesti mai multi bani murdari pe acelasi jaf.</p>
</div>
<div class="xmag-card">
<h3>Puncte pentru familie</h3>
<p>Daca faci parte dintr-o familie care aduna puncte, fiecare jaf reusit ii aduce puncte.</p>
</div>
</div>

</div>
