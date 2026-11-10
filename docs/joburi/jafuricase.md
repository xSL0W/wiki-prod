---
outline: false
---

<style>
.jc {
  --night: #070c16;
  --paper: #0c1526;
  --panel: #111d33;
  --grid: rgba(110, 160, 255, 0.07);
  --wall: #7fa6e6;
  --rule: #22324f;
  --text: #e3eaf6;
  --mute: #93a3c0;
  --blue: #6ea8ff;
  --blue-soft: rgba(110, 168, 255, 0.12);
  --alarm: #ff3d4f;
  --alarm-soft: rgba(255, 61, 79, 0.14);
  --gold: #f2c14e;
  --gold-soft: rgba(242, 193, 78, 0.13);
  max-width: 940px;
  margin: 0 auto;
  color: var(--text);
  font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.jc *, .jc *::before, .jc *::after { box-sizing: border-box; }
.jc p, .jc li { line-height: 1.6; color: var(--text); margin: 0; }
.jc ul, .jc ol { list-style: none; padding: 0; margin: 0; }
.jc b { color: #fff; font-weight: 650; }
.jc code { font-size: 0.88em; }
.jc kbd {
  font: inherit; font-size: 0.82em; font-weight: 800; color: var(--night); background: var(--blue);
  border-radius: 6px; padding: 0.05rem 0.45rem; box-shadow: 0 2px 0 #3c6fbf;
}
.jc a:focus-visible { outline: 3px solid var(--blue); outline-offset: 2px; border-radius: 4px; }
/* hero: the blueprint of the house */
.jc-hero {
  position: relative;
  background:
    linear-gradient(var(--grid) 1px, transparent 1px) 0 0 / 22px 22px,
    linear-gradient(90deg, var(--grid) 1px, transparent 1px) 0 0 / 22px 22px,
    var(--paper);
  border: 1px solid var(--rule);
  border-radius: 20px;
  padding: clamp(1.25rem, 4vw, 2.5rem);
  overflow: hidden;
}
.jc-hero::before {
  content: 'PLAN CASA  /  SCARA 1:100'; position: absolute; top: 0.9rem; right: 1.1rem;
  font: 700 0.68rem/1 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; letter-spacing: 0.14em; color: var(--mute);
}
.jc .jc-hero h1 {
  margin: 0.8rem 0 0.7rem; border: 0; padding: 0;
  font-size: clamp(2rem, 6.5vw, 3.5rem); line-height: 1.05; font-weight: 850; letter-spacing: -0.03em; color: #fff;
}
.jc-hrs { display: inline-flex; gap: 0.3em; white-space: nowrap; color: var(--blue); }
.jc-hrs .lux { color: var(--gold); }
.jc .jc-hero p { max-width: 56ch; color: var(--mute); font-size: 1.05rem; }
.jc-plan { display: block; width: 100%; height: auto; margin-top: 1.4rem; }
.jc-plan .wall { fill: none; stroke: var(--wall); stroke-width: 4; stroke-linejoin: round; }
.jc-plan .inner { fill: none; stroke: var(--wall); stroke-width: 2; opacity: 0.7; }
.jc-plan .room { fill: rgba(110, 168, 255, 0.04); }
.jc-plan .door { fill: none; stroke: var(--blue); stroke-width: 1.5; stroke-dasharray: 3 3; }
.jc-plan .route {
  fill: none; stroke: #fff; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; opacity: 0.85;
  stroke-dasharray: 1; stroke-dashoffset: 1; animation: jc-walk 4s cubic-bezier(.45, 0, .2, 1) 0.4s forwards;
}
.jc-plan .loot { fill: var(--alarm); }
.jc-plan .ring { fill: none; stroke: var(--alarm); stroke-width: 2; transform-box: fill-box; transform-origin: center; animation: jc-ping 2.4s ease-out infinite; }
.jc-plan .panel { fill: var(--night); stroke: var(--alarm); stroke-width: 2; }
.jc-plan .led { fill: var(--alarm); animation: jc-blink 1s steps(2, start) infinite; }
.jc-plan .safe { fill: var(--gold-soft); stroke: var(--gold); stroke-width: 2; }
.jc-plan .dial { fill: none; stroke: var(--gold); stroke-width: 1.5; }
.jc-plan text { fill: var(--mute); font: 600 11px ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; letter-spacing: 0.08em; }
.jc-plan .t-alarm { fill: var(--alarm); }
.jc-plan .t-safe { fill: var(--gold); }
.jc-plan .t-door { fill: var(--blue); }
@keyframes jc-walk { to { stroke-dashoffset: 0; } }
@keyframes jc-ping { 0% { transform: scale(0.6); opacity: 0.9; } 100% { transform: scale(2.2); opacity: 0; } }
@keyframes jc-blink { to { visibility: hidden; } }
@media (prefers-reduced-motion: reduce) {
  .jc-plan .route { animation: none; stroke-dashoffset: 0; }
  .jc-plan .ring, .jc-plan .led { animation: none; }
}
.jc .jc-facts { display: flex; flex-wrap: wrap; gap: 0.55rem; margin-top: 1.2rem; }
.jc .jc-facts li {
  margin: 0; font-size: 0.9rem; padding: 0.3rem 0.85rem; border-radius: 6px;
  border: 1px solid var(--rule); background: rgba(7, 12, 22, 0.7); color: var(--text);
}
.jc .jc-facts li.warn { border-color: var(--alarm); color: #ffd0d5; background: var(--alarm-soft); }
/* section headings: a dimension line */
.jc h2 {
  display: flex; align-items: center; gap: 0.8rem;
  margin: 3rem 0 1.1rem; border: 0; padding: 0;
  font-size: 1.5rem; font-weight: 780; letter-spacing: -0.015em; color: #fff;
}
.jc h2::after { content: ''; flex: 1; height: 1px; background: linear-gradient(90deg, var(--rule), transparent); }
.jc .jc-lead { max-width: 66ch; color: var(--mute); }
.jc .jc-lead + .jc-lead { margin-top: 0.7rem; }
.jc .jc-lead b { color: var(--text); }
/* the two house types */
.jc-types { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 270px), 1fr)); gap: 1rem; }
.jc-type { border: 1px solid var(--rule); border-radius: 16px; padding: 1.25rem 1.35rem; background: var(--panel); }
.jc-type.lux { border-color: rgba(242, 193, 78, 0.55); background: linear-gradient(160deg, var(--gold-soft), var(--panel) 55%); }
.jc .jc-type h3 { margin: 0; border: 0; padding: 0; font-size: 1.2rem; color: #fff; }
.jc .jc-type .tag {
  display: inline-block; margin: 0.35rem 0 0.9rem; font: 700 0.75rem/1 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace;
  letter-spacing: 0.1em; color: var(--blue); text-transform: uppercase;
}
.jc .jc-type.lux .tag { color: var(--gold); }
.jc .jc-spec li { margin: 0; display: flex; justify-content: space-between; gap: 1rem; padding: 0.45rem 0; border-top: 1px dashed var(--rule); font-size: 0.94rem; }
.jc .jc-spec li span { color: var(--mute); }
.jc .jc-spec li strong { color: #fff; text-align: right; }
.jc .jc-type p.jc-note { margin-top: 0.8rem; color: var(--mute); font-size: 0.9rem; }
/* the kit: three tool cards */
.jc-kit { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 250px), 1fr)); gap: 1rem; }
.jc-tool { border: 1px solid var(--rule); border-radius: 16px; padding: 1.1rem 1.2rem; background: var(--panel); }
.jc-tool svg { display: block; width: 46px; height: 46px; margin-bottom: 0.7rem; }
.jc-tool svg .s { fill: none; stroke: var(--blue); stroke-width: 2.2; stroke-linecap: round; stroke-linejoin: round; }
.jc .jc-tool h3 { margin: 0 0 0.35rem; border: 0; padding: 0; font-size: 1.08rem; color: #fff; }
.jc .jc-tool p { color: var(--mute); font-size: 0.93rem; }
.jc .jc-tool p + p { margin-top: 0.5rem; }
.jc .jc-tool p b { color: var(--text); }
/* the robbery: numbered rooms on the plan */
.jc-steps { display: grid; gap: 0.75rem; counter-reset: jc-step; }
.jc .jc-steps li {
  position: relative; margin: 0; counter-increment: jc-step;
  display: grid; grid-template-columns: 3.2rem minmax(0, 1fr); gap: 0.2rem 1rem;
  padding: 1rem 1.2rem; border: 1px solid var(--rule); border-left: 3px solid var(--blue); border-radius: 12px; background: var(--panel);
}
.jc .jc-steps li::before {
  content: counter(jc-step, decimal-leading-zero); grid-row: 1 / span 2;
  font: 800 1.6rem/1 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; color: var(--blue);
}
.jc .jc-steps li.alarm { border-left-color: var(--alarm); }
.jc .jc-steps li.alarm::before { color: var(--alarm); }
.jc .jc-steps li.safe { border-left-color: var(--gold); }
.jc .jc-steps li.safe::before { color: var(--gold); }
.jc .jc-steps li strong { color: #fff; font-size: 1.04rem; }
.jc .jc-steps li p { color: var(--mute); font-size: 0.95rem; }
.jc .jc-steps li p b { color: var(--text); }
@media (max-width: 480px) {
  .jc .jc-steps li { grid-template-columns: minmax(0, 1fr); }
  .jc .jc-steps li::before { grid-row: auto; font-size: 1.2rem; }
}
/* alarm box */
.jc-alert {
  display: grid; grid-template-columns: auto minmax(0, 1fr); gap: 1rem 1.2rem; align-items: start;
  border: 1px solid var(--alarm); border-radius: 16px; padding: 1.2rem 1.35rem;
  background: linear-gradient(150deg, var(--alarm-soft), var(--panel) 60%);
}
.jc-siren { width: 52px; height: 52px; }
.jc-siren .body { fill: var(--alarm); }
.jc-siren .wave { fill: none; stroke: var(--alarm); stroke-width: 2.5; stroke-linecap: round; animation: jc-blink 1.2s steps(2, start) infinite; }
@media (prefers-reduced-motion: reduce) { .jc-siren .wave { animation: none; } }
.jc .jc-alert h3 { margin: 0 0 0.4rem; border: 0; padding: 0; font-size: 1.12rem; color: #fff; }
.jc .jc-alert p { color: var(--mute); }
.jc .jc-alert p + p { margin-top: 0.5rem; }
.jc .jc-alert p b { color: #fff; }
@media (max-width: 480px) { .jc-alert { grid-template-columns: minmax(0, 1fr); } }
/* team */
.jc .jc-rows li { margin: 0; padding: 0.85rem 0 0.85rem 1.6rem; border-top: 1px solid var(--rule); position: relative; color: var(--mute); }
.jc .jc-rows li:last-child { border-bottom: 1px solid var(--rule); }
.jc .jc-rows li::before {
  content: ''; position: absolute; left: 0.2rem; top: 1.35rem; width: 8px; height: 8px; border: 2px solid var(--blue); transform: rotate(45deg);
}
.jc .jc-rows li b { color: #fff; }
/* loot drawers */
.jc-loot { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr)); gap: 1rem; }
.jc-drawer { border: 1px solid var(--rule); border-radius: 16px; padding: 1.1rem 1.2rem; background: var(--panel); }
.jc-drawer.safe { border-color: rgba(242, 193, 78, 0.55); background: linear-gradient(160deg, var(--gold-soft), var(--panel) 60%); }
.jc .jc-drawer h3 {
  margin: 0 0 0.75rem; border: 0; padding: 0; font: 700 0.78rem/1.2 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace;
  letter-spacing: 0.12em; text-transform: uppercase; color: var(--blue);
}
.jc .jc-drawer.safe h3 { color: var(--gold); }
.jc .jc-items { display: flex; flex-wrap: wrap; gap: 0.4rem; }
.jc .jc-items li { margin: 0; font-size: 0.88rem; padding: 0.15rem 0.65rem; border-radius: 999px; border: 1px solid var(--rule); color: var(--text); background: rgba(7, 12, 22, 0.6); }
.jc .jc-items li.sell { border-color: rgba(242, 193, 78, 0.6); }
.jc .jc-items li em { font-style: normal; color: var(--mute); font-size: 0.8rem; }
.jc .jc-drawer p { margin-top: 0.75rem; color: var(--mute); font-size: 0.9rem; }
.jc-pawn {
  margin-top: 1rem; display: flex; flex-wrap: wrap; align-items: center; gap: 0.6rem 1rem;
  padding: 0.9rem 1.2rem; border: 1px dashed rgba(242, 193, 78, 0.6); border-radius: 12px;
}
.jc .jc-pawn p { color: var(--mute); flex: 1 1 260px; }
.jc .jc-pawn p b { color: var(--gold); }
/* risks */
.jc-risks { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr)); gap: 0.75rem; }
.jc .jc-risks li { margin: 0; padding: 0.9rem 1rem; border-radius: 12px; border: 1px solid var(--rule); background: var(--panel); color: var(--mute); font-size: 0.94rem; }
.jc .jc-risks li b { display: block; color: #fff; margin-bottom: 0.2rem; }
</style>

<div class="jc">
<section class="jc-hero">
<h1>Jaf la case <span class="jc-hrs"><span>-</span> <span>50h/<span class="lux">100h</span></span></span></h1>
<p>Lester te trimite la o casa. Tu spargi usa, opresti alarma inainte sa sune si golesti casa camera cu camera, singur sau cu echipa ta.</p>
<svg class="jc-plan" viewBox="0 0 640 300" role="img" aria-label="Planul unei case: usa de la intrare, panoul de alarma langa usa, puncte de cautat in fiecare camera si seiful in birou">
<rect class="room" x="40" y="30" width="560" height="240"/>
<path class="wall" d="M40 30 H600 V270 H160 M100 270 H40 V30"/>
<path class="inner" d="M260 30 V120 M260 160 V270 M260 150 H330 M370 150 H480 M520 150 H600 M440 30 V110"/>
<path class="door" d="M100 270 A60 60 0 0 1 160 210"/>
<line class="door" x1="100" y1="270" x2="160" y2="270"/>
<text class="t-door" x="74" y="292">USA</text>
<rect class="panel" x="52" y="200" width="20" height="28" rx="3"/>
<circle class="led" cx="62" cy="211" r="4"/>
<text class="t-alarm" x="50" y="190">ALARMA</text>
<path class="route" pathLength="1" d="M130 262 L130 225 L78 214 L150 170 L200 90 L240 140 L285 140 L300 120 L360 70 L360 205 L470 210 L500 180 L500 120 L540 80"/>
<circle class="loot" cx="200" cy="90" r="6"/><circle class="ring" cx="200" cy="90" r="6"/>
<circle class="loot" cx="300" cy="120" r="6"/><circle class="ring" cx="300" cy="120" r="6" style="animation-delay: .6s"/>
<circle class="loot" cx="360" cy="70" r="6"/><circle class="ring" cx="360" cy="70" r="6" style="animation-delay: 1.2s"/>
<circle class="loot" cx="360" cy="205" r="6"/><circle class="ring" cx="360" cy="205" r="6" style="animation-delay: .3s"/>
<circle class="loot" cx="470" cy="210" r="6"/><circle class="ring" cx="470" cy="210" r="6" style="animation-delay: .9s"/>
<rect class="safe" x="520" y="58" width="44" height="44" rx="4"/>
<circle class="dial" cx="542" cy="80" r="10"/>
<line class="dial" x1="542" y1="80" x2="542" y2="72"/>
<text x="80" y="50">LIVING</text>
<text x="280" y="50">DORMITOR</text>
<text x="280" y="262">BUCATARIE</text>
<text x="460" y="50">BIROU</text>
<text class="t-safe" x="486" y="124">SEIF (LUX)</text>
</svg>
<ul class="jc-facts">
<li class="warn">Minim 3 politisti la datorie</li>
<li>Casa normala: echipa de 1-4</li>
<li>Casa de lux: echipa de 1-6</li>
<li>Pornesti de la Lester</li>
</ul>
</section>
<h2>Doua tipuri de case</h2>
<div class="jc-types">
<div class="jc-type">
<h3>Case obisnuite</h3>
<span class="tag">Jaf case obisnuite</span>
<ul class="jc-spec">
<li><span>Ore jucate</span><strong>50h</strong></li>
<li><span>Echipa</span><strong>1-4 jucatori</strong></li>
<li><span>Opresti alarma cu</span><strong><img class="eg-item" src="/items/telefon_hacking.webp" alt="">Telefon Hacking</strong></li>
<li><span>Seif</span><strong>Nu</strong></li>
</ul>
<p class="jc-note">Casa poate fi jefuita chiar daca are proprietar.</p>
</div>
<div class="jc-type lux">
<h3>Case de lux</h3>
<span class="tag">Jaf case de lux</span>
<ul class="jc-spec">
<li><span>Ore jucate</span><strong>100h</strong></li>
<li><span>Echipa</span><strong>1-6 jucatori</strong></li>
<li><span>Opresti alarma cu</span><strong><img class="eg-item" src="/items/tableta_hacking.webp" alt="">Tableta Hacking</strong></li>
<li><span>Seif</span><strong>Da</strong></li>
</ul>
<p class="jc-note">O casa de lux care are proprietar nu iese niciodata la jaf.</p>
</div>
</div>
<h2>Cine poate intra</h2>
<p class="jc-lead">Politistii si medicii nu pot da jaful si nici nu pot fi in echipa. Cand liderul porneste jaful, fiecare membru este verificat: trebuie sa aiba orele jucate pentru tipul de casa ales si sa nu fie inca in pauza dupa un jaf la case. Daca pica cineva, toata echipa vede cine si de ce.</p>
<p class="jc-lead">Pe server trebuie sa fie cel putin <b>3 politisti la datorie</b>, altfel jaful nu porneste.</p>
<h2>Ce iti trebuie</h2>
<div class="jc-kit">
<div class="jc-tool">
<svg viewBox="0 0 48 48" aria-hidden="true"><path class="s" d="M8 30 L30 8 M26 12 L32 18 M22 16 L26 20"/><circle class="s" cx="34" cy="34" r="8"/><path class="s" d="M28 28 L14 42"/></svg>
<h3><img class="eg-item" src="/items/advancedlockpick.webp" alt="">Lockpick avansat</h3>
<p>Cu el spargi usa. <b>Fiecare incercare il consuma</b>, fie ca reusesti, fie ca nu, asa ca ia mai multe.</p>
<p>Il cumperi de la <b>Home depot</b>. Mai pica uneori din jafurile de masini sau din tomberoane.</p>
</div>
<div class="jc-tool">
<svg viewBox="0 0 48 48" aria-hidden="true"><path class="s" d="M12 40 L36 10 Q40 6 42 10 L40 14"/><path class="s" d="M12 40 Q8 42 6 38 L10 34"/></svg>
<h3><img class="eg-item" src="/items/WEAPON_CROWBAR.webp" alt="">Ranga</h3>
<p>Fara ranga nu poti cauta prin casa. <b>Se poate rupe</b> la orice punct, asa ca ia cateva.</p>
<p>O gasesti pe un santier, cu optiunea <b>Obtine ranga</b> de la Lester. Detaliile sunt mai jos.</p>
</div>
<div class="jc-tool">
<svg viewBox="0 0 48 48" aria-hidden="true"><rect class="s" x="14" y="6" width="20" height="36" rx="4"/><path class="s" d="M20 36 H28 M20 14 L24 18 L20 22 M26 22 H30"/></svg>
<h3>Telefon / Tableta Hacking</h3>
<p>Opreste alarma: <b><img class="eg-item" src="/items/telefon_hacking.webp" alt="">Telefon Hacking</b> la casele obisnuite, <b><img class="eg-item" src="/items/tableta_hacking.webp" alt="">Tableta Hacking</b> la cele de lux. Se consuma la fiecare incercare.</p>
<p>Le craftezi la <b>Hackeru lui Peste</b>, langa Lester, dintr-un <img class="eg-item" src="/items/phone.webp" alt="">Telefon (de la DigitalDen) sau o <img class="eg-item" src="/items/tableta.webp" alt="">Tableta (o gasesti la jafurile la case obisnuite) plus un <b><img class="eg-item" src="/items/sim_hacking.webp" alt="">Sim hacking</b> (din jafurile de masini).</p>
</div>
</div>
<h2>Ranga de pe santier</h2>
<ul class="jc-rows">
<li>Alege <b>Obtine ranga</b> din meniul lui Lester. Primesti GPS spre un santier, in centrul orasului sau in Mirror Park. Cauti singur, fara echipa.</li>
<li>Pe santier apar puncte de cautat. Apasa <kbd>E</kbd> langa unul si asteapta sa se umple bara. Fiecare punct il cauti o singura data si nu de fiecare data gasesti ranga.</li>
<li>Daca pleci din zona santierului si nu te intorci repede, cautarea se opreste. Fa-ti loc in inventar inainte, altfel ranga nu ti se da.</li>
</ul>
<h2>Jaful, pas cu pas</h2>
<ol class="jc-steps">
<li><strong>Vorbeste cu Lester</strong><p>Alege <b>Jaf case obisnuite</b> sau <b>Jaf case de lux</b>. Daca joci in echipa, formeaz-o din <b>Meniu echipa</b>. Doar liderul apasa <b>Incepe jaf</b>. Singur poti porni direct.</p></li>
<li><strong>Mergi la adresa</strong><p>Toata echipa primeste GPS spre o casa aleasa la intamplare si numarul ei in notificare. Ai un timp limitat pentru tot jaful. Pasii apar si pe ecran, in lista jafului.</p></li>
<li><strong>Sparge usa</strong><p>Stai langa usa si foloseste <b><img class="eg-item" src="/items/advancedlockpick.webp" alt="">Lockpick avansat</b> din inventar. Treci minijocul si usa ramane deschisa pentru toata echipa.</p></li>
<li class="alarm"><strong>Opreste alarma</strong><p>Cand se deschide usa porneste numaratoarea, iar notificarea iti spune cate secunde ai. Du-te la panoul de alarma, tine <kbd>H</kbd> si treci minijocul cu luminile. Cat timp lucrezi la panou, numaratoarea sta pe loc. O greseala porneste alarma pe loc, iar dupa cateva incercari ratate panoul se blocheaza.</p></li>
<li><strong>Cauta prin casa</strong><p>Cu o <img class="eg-item" src="/items/WEAPON_CROWBAR.webp" alt="">ranga in inventar, apasa <kbd>E</kbd> la fiecare punct marcat si asteapta bara. Fiecare membru cauta separat si ce gaseste ajunge direct in inventarul lui. Daca nu ai loc, punctul ramane pentru alta incercare. Uneori nu gasesti nimic.</p></li>
<li class="safe"><strong>Seiful (doar la lux)</strong><p>Tine <kbd>G</kbd> pe seif si alege <b>Jefuieste seiful</b>. Dupa ce il spargi, se deschide ca un depozit pe care orice membru al echipei il poate goli cat timp jaful merge.</p></li>
<li><strong>Final</strong><p>Jaful se termina singur cand expira timpul. Liderul il poate opri mai devreme din meniul lui Lester, cu <b>Opreste/finalizeaza jaf</b>, dar numai dupa o vreme de la pornire.</p></li>
</ol>
<h2>Alarma si politia</h2>
<div class="jc-alert">
<svg class="jc-siren" viewBox="0 0 52 52" aria-hidden="true"><path class="body" d="M16 40 V26 a10 10 0 0 1 20 0 V40 Z"/><rect class="body" x="12" y="40" width="28" height="5" rx="2"/><path class="wave" d="M8 18 L4 15 M44 18 L48 15 M26 9 V4 M14 11 L11 7 M38 11 L41 7"/></svg>
<div>
<h3>Daca alarma porneste, vine politia</h3>
<p>Alarma porneste cand expira numaratoarea sau cand gresesti la panou. Politistii de la datorie primesc pe harta <b>Jaf la casa normala in curs</b> sau <b>Jaf la casa de lux in curs</b>, iar sirena se aude in jurul casei.</p>
<p>Daca opresti alarma la timp, politia nu este anuntata.</p>
</div>
</div>
<h2>Echipa si zona</h2>
<ul class="jc-rows">
<li><b>Echipa e optionala.</b> Poti merge singur sau cu maxim 3 colegi la casele obisnuite si maxim 5 la cele de lux. Toata casa are aceleasi puncte, oricati ati fi: mai multi oameni golesc casa mai repede, dar fiecare ia doar ce cauta el.</li>
<li><b>Pauza dupa jaf.</b> Cand porneste jaful, fiecare membru intra intr-o pauza comuna pentru ambele tipuri de case. Nu poti da alt jaf la case pana nu trece.</li>
<li><b>Nu plecati toti din zona.</b> Dupa ce s-a deschis usa, daca toti membrii se departeaza de casa, primiti un avertisment. Daca nu se intoarce nimeni la timp, jaful se anuleaza.</li>
<li><b>Daca iesi de pe server, iesi si din jaf.</b> Cand nu mai ramane nimeni din echipa, jaful se opreste.</li>
<li><b>Familia ta castiga puncte</b> cand casa e golita complet: toate punctele cautate si, la lux, seiful spart.</li>
</ul>
<h2>Ce gasesti</h2>
<div class="jc-loot">
<div class="jc-drawer">
<h3>Punctele din casa</h3>
<ul class="jc-items">
<li><img class="eg-item" src="/items/money.webp" alt="">Bani cash</li>
<li class="sell"><img class="eg-item" src="/items/inel_diamant.webp" alt="">Inel cu diamant</li>
<li class="sell"><img class="eg-item" src="/items/bratara_aur.webp" alt="">Bratara de aur</li>
<li class="sell"><img class="eg-item" src="/items/cercei_diamant.webp" alt="">Cercei cu diamant</li>
<li><img class="eg-item" src="/items/axe.webp" alt="">Topor</li>
<li><img class="eg-item" src="/items/tableta.webp" alt="">Tableta <em>(case obisnuite)</em></li>
<li><img class="eg-item" src="/items/metal_detector.webp" alt="">Detector de electronice <em>(lux)</em></li>
</ul>
<p>In happy hour ai sanse sa gasesti mai mult la fiecare punct.</p>
</div>
<div class="jc-drawer safe">
<h3>Seiful (lux)</h3>
<ul class="jc-items">
<li class="sell"><img class="eg-item" src="/items/bara_aur.webp" alt="">Bara de aur</li>
<li><img class="eg-item" src="/items/laptop.webp" alt="">Laptop</li>
<li><img class="eg-item" src="/items/WEAPON_PISTOL.webp" alt="">Pistol</li>
<li><img class="eg-item" src="/items/ammo-9.webp" alt="">Munitie</li>
<li><img class="eg-item" src="/items/plic_iarba.webp" alt="">Plic de iarba</li>
<li><img class="eg-item" src="/items/metal_detector.webp" alt="">Detector de electronice</li>
</ul>
<p>Seiful il deschide oricine din echipa, deci impartiti-va ce e inauntru.</p>
</div>
</div>
<div class="jc-pawn">
<p>Bijuteriile si barele de aur le vinzi la <b>Amanet Cris</b>, care apare pe harta. Plata depinde de ce aduci.</p>
</div>
<h2>Ce strica jaful</h2>
<ul class="jc-risks">
<li><b>Alarma nu e oprita la timp</b>Politia primeste locatia casei.</li>
<li><b>Ramai fara lockpick</b>Fiecare incercare la usa consuma unul.</li>
<li><b>Ramai fara ranga</b>Se poate rupe la orice punct si fara ea nu mai cauti.</li>
<li><b>Plecati toti din zona</b>Jaful se anuleaza daca nu va intoarceti la timp.</li>
<li><b>Expira timpul</b>Jaful se opreste si usile se incuie la loc.</li>
<li><b>Inventar plin</b>Ce nu incape nu primesti, iar punctul ramane necautat.</li>
</ul>
</div>
