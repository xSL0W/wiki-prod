---
outline: false
---

<style>
.bvd {
  --steel: #0b0e11;
  --plate: #141a1f;
  --rivet: #1f272e;
  --edge: #34404a;
  --text: #e8edf1;
  --mute: #9ba8b3;
  --brass: #d6a650;
  --brass-soft: rgba(214, 166, 80, 0.13);
  --alarm: #ff4b3e;
  --alarm-soft: rgba(255, 75, 62, 0.12);
  --cash: #5fd38d;
  max-width: 920px;
  margin: 0 auto;
  color: var(--text);
  font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.bvd *, .bvd *::before, .bvd *::after { box-sizing: border-box; }
.bvd p, .bvd li { line-height: 1.6; color: var(--text); margin: 0; }
.bvd ul, .bvd ol { list-style: none; padding: 0; margin: 0; }
.bvd li + li { margin-top: 0; }
.bvd b { color: #fff; font-weight: 650; }

/* hero: the vault door */
.bvd .bvd-hero {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: clamp(1rem, 4vw, 2rem);
  align-items: center;
  background:
    repeating-linear-gradient(90deg, rgba(255, 255, 255, 0.018) 0 2px, transparent 2px 6px),
    linear-gradient(160deg, #182029, var(--steel) 70%);
  border: 1px solid var(--edge);
  border-radius: 22px;
  padding: clamp(1.25rem, 4vw, 2.5rem);
  overflow: hidden;
}
.bvd .bvd-hero h1 {
  margin: 0 0 0.7rem;
  border: 0;
  padding: 0;
  font-size: clamp(2rem, 6.2vw, 3.4rem);
  line-height: 1.05;
  font-weight: 800;
  letter-spacing: -0.03em;
  color: #fff;
}
.bvd .bvd-hrs { display: inline-flex; gap: 0.3em; white-space: nowrap; color: var(--brass); }
.bvd .bvd-lead { color: var(--mute); font-size: 1.05rem; max-width: 46ch; }
.bvd-door { display: block; width: 100%; max-width: 340px; height: auto; margin: 0 auto; }
.bvd-door .frame { fill: #11161b; stroke: var(--edge); stroke-width: 3; }
.bvd-door .slab { fill: #1c242c; stroke: #46525d; stroke-width: 3; }
.bvd-door .ring { fill: none; stroke: #2c363f; stroke-width: 10; }
.bvd-door .bolt { fill: #4b5864; }
.bvd-door .hinge { fill: #2a333b; stroke: var(--edge); stroke-width: 2; }
.bvd-door .dial { fill: #0f1418; stroke: var(--brass); stroke-width: 4; }
.bvd-door .tick { stroke: var(--brass); stroke-width: 2.5; stroke-linecap: round; }
.bvd-door .spoke { stroke: #5b6976; stroke-width: 7; stroke-linecap: round; }
.bvd-door .hub { fill: var(--brass); }
.bvd-door .mark { fill: var(--alarm); }
.bvd-door .spin {
  transform-box: fill-box;
  transform-origin: center;
  animation: bvd-spin 9s cubic-bezier(.6, 0, .3, 1) infinite;
}
@keyframes bvd-spin {
  0% { transform: rotate(0deg); }
  30% { transform: rotate(140deg); }
  55% { transform: rotate(60deg); }
  85%, 100% { transform: rotate(250deg); }
}
.bvd .bvd-facts { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 0.6rem; margin-top: 1.2rem; }
.bvd .bvd-fact {
  margin: 0;
  background: var(--plate);
  border: 1px solid var(--edge);
  border-radius: 10px;
  padding: 0.6rem 0.8rem;
}
.bvd .bvd-fact span { display: block; font-size: 0.74rem; letter-spacing: 0.1em; text-transform: uppercase; color: var(--mute); }
.bvd .bvd-fact strong { display: block; font-size: 1.1rem; color: #fff; font-variant-numeric: tabular-nums; }

/* sections */
.bvd h2 {
  margin: 3rem 0 1rem;
  border: 0;
  padding: 0;
  font-size: 1.5rem;
  font-weight: 750;
  letter-spacing: -0.015em;
  color: #fff;
}
.bvd .bvd-p { color: var(--mute); max-width: 68ch; }
.bvd .bvd-p + .bvd-p { margin-top: 0.7rem; }

/* before you start */
.bvd .bvd-rules { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 0.8rem; }
.bvd .bvd-rule { margin: 0; background: var(--plate); border: 1px solid var(--edge); border-radius: 14px; padding: 1rem 1.15rem; }
.bvd .bvd-rule p { color: var(--mute); font-size: 0.96rem; }
.bvd .bvd-warn {
  margin-top: 1rem;
  background: linear-gradient(150deg, var(--alarm-soft), var(--plate) 60%);
  border: 1px solid rgba(255, 75, 62, 0.55);
  border-left-width: 5px;
  border-radius: 12px;
  padding: 1rem 1.2rem;
}
.bvd .bvd-warn p { color: var(--text); }

/* kit: safe deposit lockers */
.bvd .bvd-lockers { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 0.7rem; }
.bvd .bvd-locker {
  position: relative;
  margin: 0;
  background: linear-gradient(180deg, #1a2128, #12171c);
  border: 1px solid var(--edge);
  border-radius: 10px;
  padding: 1rem 1rem 1rem 1rem;
}
.bvd .bvd-locker::after {
  content: '';
  position: absolute; right: 12px; top: 50%;
  width: 6px; height: 26px; margin-top: -13px;
  border-radius: 3px;
  background: #3b4651;
}
.bvd .bvd-locker .bvd-no {
  display: inline-block;
  margin-bottom: 0.5rem;
  font-size: 0.72rem; font-weight: 700; letter-spacing: 0.12em;
  color: var(--steel); background: var(--brass);
  border-radius: 3px; padding: 0.05rem 0.4rem;
}
.bvd .bvd-locker h3 { margin: 0 0 0.25rem; border: 0; padding: 0; font-size: 1.02rem; color: #fff; }
.bvd .bvd-locker p { color: var(--mute); font-size: 0.92rem; padding-right: 1rem; }

/* the nine phases as a combination */
.bvd .bvd-step {
  position: relative;
  margin: 0;
  padding: 1rem 0 1rem 3.9rem;
  border-top: 1px solid var(--edge);
}
.bvd .bvd-step:last-child { border-bottom: 1px solid var(--edge); }
.bvd .bvd-step::before {
  content: attr(data-n);
  position: absolute; left: 0; top: 0.9rem;
  width: 42px; height: 42px;
  display: grid; place-items: center;
  border-radius: 50%;
  font-weight: 800; font-size: 1rem; color: var(--brass);
  background: radial-gradient(circle, #0f1418 55%, transparent 56%), repeating-conic-gradient(var(--brass) 0 3deg, transparent 3deg 30deg);
  border: 2px solid #46525d;
}
.bvd .bvd-step.alert::before { color: var(--alarm); border-color: var(--alarm); }
.bvd .bvd-step.final::before { color: var(--cash); border-color: var(--cash); }
.bvd .bvd-step h3 { margin: 0 0 0.25rem; border: 0; padding: 0; font-size: 1.08rem; color: #fff; }
.bvd .bvd-step p { color: var(--mute); }
.bvd .bvd-tag {
  display: inline-block; margin-left: 0.4rem; vertical-align: 0.1em;
  font-size: 0.72rem; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase;
  color: var(--alarm); border: 1px solid var(--alarm); border-radius: 999px; padding: 0 0.5rem;
}
.bvd kbd {
  font: inherit; font-size: 0.85em; font-weight: 800; color: var(--steel); background: var(--brass);
  border-radius: 6px; padding: 0.05rem 0.45rem;
}

/* loot */
.bvd .bvd-loot { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1rem; }
.bvd .bvd-box { background: var(--plate); border: 1px solid var(--edge); border-radius: 16px; padding: 1.2rem 1.3rem; }
.bvd .bvd-box.cash { background: linear-gradient(160deg, rgba(95, 211, 141, 0.12), var(--plate) 60%); border-color: rgba(95, 211, 141, 0.55); }
.bvd .bvd-box h3 { margin: 0 0 0.7rem; border: 0; padding: 0; font-size: 1.12rem; color: #fff; }
.bvd .bvd-chips { display: flex; flex-wrap: wrap; gap: 0.5rem; }
.bvd .bvd-chip {
  margin: 0;
  background: var(--steel);
  border: 1px solid var(--edge);
  border-radius: 6px;
  padding: 0.28rem 0.75rem;
  font-size: 0.93rem;
}
.bvd .bvd-box .bvd-note { margin-top: 0.8rem; color: var(--mute); font-size: 0.93rem; }
.bvd .bvd-after { margin-top: 1rem; }

/* police and risks */
.bvd .bvd-rows .bvd-row { margin: 0; padding: 0.85rem 0; border-top: 1px solid var(--edge); }
.bvd .bvd-rows .bvd-row:last-child { border-bottom: 1px solid var(--edge); }
.bvd .bvd-rows .bvd-row p { color: var(--mute); }

.bvd a:focus-visible { outline: 3px solid var(--brass); outline-offset: 2px; border-radius: 4px; }
@media (prefers-reduced-motion: reduce) {
  .bvd-door .spin { animation: none; }
}
</style>

<div class="bvd">

<section class="bvd-hero">
<div>
<h1>Jaf la banca <span class="bvd-hrs"><span>-</span> <span>500h</span></span></h1>
<p class="bvd-lead">Cel mai mare jaf din oras. O echipa numeroasa, noua etape la rand, o bomba pe usa seifului si toata politia pe urmele voastre.</p>
</div>
<svg class="bvd-door" viewBox="0 0 300 300" role="img" aria-label="Usa rotunda a unui seif de banca, cu bolturi pe margine si un disc de cod care se roteste">
<rect class="frame" x="10" y="10" width="280" height="280" rx="18"/>
<rect class="hinge" x="18" y="92" width="22" height="40" rx="5"/>
<rect class="hinge" x="18" y="168" width="22" height="40" rx="5"/>
<circle class="slab" cx="155" cy="150" r="122"/>
<circle class="ring" cx="155" cy="150" r="100"/>
<rect class="bolt" x="149" y="34" width="12" height="18" rx="3"/>
<rect class="bolt" x="149" y="248" width="12" height="18" rx="3"/>
<rect class="bolt" x="39" y="144" width="18" height="12" rx="3"/>
<rect class="bolt" x="253" y="144" width="18" height="12" rx="3"/>
<rect class="bolt" x="223" y="72" width="12" height="18" rx="3" transform="rotate(45 229 81)"/>
<rect class="bolt" x="75" y="72" width="12" height="18" rx="3" transform="rotate(-45 81 81)"/>
<rect class="bolt" x="223" y="210" width="12" height="18" rx="3" transform="rotate(-45 229 219)"/>
<rect class="bolt" x="75" y="210" width="12" height="18" rx="3" transform="rotate(45 81 219)"/>
<line class="spoke" x1="155" y1="150" x2="155" y2="78"/>
<line class="spoke" x1="155" y1="150" x2="217" y2="186"/>
<line class="spoke" x1="155" y1="150" x2="93" y2="186"/>
<polygon class="mark" points="149,92 161,92 155,103"/>
<g class="spin">
<circle class="dial" cx="155" cy="150" r="44"/>
<line class="tick" x1="155" y1="110" x2="155" y2="120"/>
<line class="tick" x1="155" y1="180" x2="155" y2="190"/>
<line class="tick" x1="115" y1="150" x2="125" y2="150"/>
<line class="tick" x1="185" y1="150" x2="195" y2="150"/>
<line class="tick" x1="127" y1="122" x2="133" y2="128"/>
<line class="tick" x1="177" y1="172" x2="183" y2="178"/>
<line class="tick" x1="183" y1="122" x2="177" y2="128"/>
<line class="tick" x1="133" y1="172" x2="127" y2="178"/>
<circle class="hub" cx="155" cy="150" r="10"/>
</g>
</svg>
<ul class="bvd-facts">
<li class="bvd-fact"><span>Ore jucate</span><strong>500h fiecare</strong></li>
<li class="bvd-fact"><span>Echipa</span><strong>15 - 20</strong></li>
<li class="bvd-fact"><span>Politie de serviciu</span><strong>minim 10</strong></li>
<li class="bvd-fact"><span>Banca</span><strong>Fleeca Legion Square</strong></li>
</ul>
</section>

<h2>Inainte sa pornesti</h2>
<ul class="bvd-rules">
<li class="bvd-rule"><b>De la Lester.</b><p>Locul lui il afli in joc. Din lista lui alegi <b>Jaf de banca</b>, apoi banca. Acolo ai <b>Informatii</b>, <b>Obiecte necesare</b> si <b>Meniu echipa</b>.</p></li>
<li class="bvd-rule"><b>Liderul porneste.</b><p>Doar liderul echipei porneste si opreste jaful. Fiecare membru trebuie sa fie online si sa aiba minim 500 de ore jucate.</p></li>
<li class="bvd-rule"><b>Doar seara.</b><p>Jaful merge doar intr-un interval orar fix, seara. Daca incerci in afara lui, notificarea iti spune orele.</p></li>
<li class="bvd-rule"><b>Unul singur pe server.</b><p>Merge un singur jaf de banca odata. Dupa fiecare jaf urmeaza o pauza pentru toate bancile. Cat timp ruleaza, nu porneste nici jaful la bijuterii.</p></li>
<li class="bvd-rule"><b>Nu pot intra</b><p>politistii si medicii (SMIR). Daca un singur membru nu se califica, echipa vede cine si de ce, iar jaful nu porneste.</p></li>
</ul>
<div class="bvd-warn">
<p><b>Rezervarea in Sentinel.</b> Inainte de jaf, liderul factiunii rezerva un interval in calendarul din Sentinel. La pornire confirmi ca echipa ta este cea programata. Daca pornesti jaful fara rezervare valida, primesti sanctiune.</p>
</div>

<h2>Ce iei in geanta</h2>
<p class="bvd-p">Lista exacta, cu cate bucati iti trebuie, o vezi in meniu la <b>Obiecte necesare</b>. Obiectele de hacking se consuma doar cand reusesti.</p>
<ul class="bvd-lockers bvd-after">
<li class="bvd-locker"><span class="bvd-no">CUTIA 01</span><h3>Telefon Hacking</h3><p>Pentru camere. Se face la <b>Hackeru' lui Peste</b>, langa Lester. Ia rezerve: politia poate lua camerele inapoi.</p></li>
<li class="bvd-locker"><span class="bvd-no">CUTIA 02</span><h3>Soricel</h3><p>Blocheaza usa de la intrare. Il cumperi de la Home Depot.</p></li>
<li class="bvd-locker"><span class="bvd-no">CUTIA 03</span><h3>C4</h3><p>Bomba pentru usa seifului. Se face la <b>Crafting Ilegale Sandy</b>.</p></li>
<li class="bvd-locker"><span class="bvd-no">CUTIA 04</span><h3>Topor</h3><p>Sparge usa din interior. Un topor tine cateva folosiri, apoi se rupe.</p></li>
<li class="bvd-locker"><span class="bvd-no">CUTIA 05</span><h3>Tableta Hacking</h3><p>Cate una pentru fiecare calculator. Se face la <b>Hackeru' lui Peste</b>.</p></li>
<li class="bvd-locker"><span class="bvd-no">CUTIA 06</span><h3>Laptop de hacking</h3><p>Sparge codul seifului final. Se face la <b>Crafting Ilegale Sandy</b>.</p></li>
<li class="bvd-locker"><span class="bvd-no">CUTIA 07</span><h3>Bormasina cu burghiu de diamant</h3><p>Gaureste cutiile cu valori si se uzeaza la fiecare cutie noua. Se face la <b>Crafting Ilegale Sandy</b>.</p></li>
</ul>

<h2>Combinatia: cele noua etape</h2>
<p class="bvd-p">Etapele merg strict in ordine. O etapa noua se deschide doar dupa ce o terminati pe cea de dinainte, iar lista apare in HUD la toata echipa.</p>
<ol class="bvd-combo bvd-after">
<li class="bvd-step" data-n="1"><h3>Sparge camerele</h3><p>La cutia electrica de langa banca apasa <kbd>H</kbd>. Ai nevoie de <b>Telefon Hacking</b>: gasesti cipurile ascunse cu lanterna. <kbd>ESC</kbd> te scoate din joc. Cand reusesti, camerele bancii sunt ale voastre.</p></li>
<li class="bvd-step alert" data-n="2"><h3>Blocheaza intrarea <span class="bvd-tag">alarma</span></h3><p>Foloseste <b>Soricel</b> din inventar langa usa de la intrare. Usa se incuie, porneste alarma si toti politistii de serviciu primesc alerta.</p></li>
<li class="bvd-step alert" data-n="3"><h3>Planteaza bomba</h3><p>Stai cu fata la usa seifului si foloseste <b>C4</b>. Bomba numara invers si piuie tot mai des. Nu sta langa ea cand explodeaza: te omoara. Cat timp numara, treceti la etapele urmatoare.</p></li>
<li class="bvd-step" data-n="4"><h3>Cauta prin hartiile rupte</h3><p>La rafturi apasa <kbd>H</kbd> si lipesti documentul la loc. Primesti o <b>Bucata de hartie</b> cu numarul unei cutii pline din seif. Daca gresesti, raftul se blocheaza pentru putin timp.</p></li>
<li class="bvd-step" data-n="5"><h3>Sparge usa cu toporul</h3><p>Langa usa apasa <kbd>H</kbd>, apoi apasa repetat <kbd>SPACE</kbd>. Daca tii tasta apasata, nu se intampla nimic. <kbd>BACKSPACE</kbd> anuleaza.</p></li>
<li class="bvd-step" data-n="6"><h3>Sparge calculatoarele</h3><p>La fiecare calculator apasa <kbd>H</kbd> si ghicesti parola terminalului. Fiecare calculator spart consuma o <b>Tableta Hacking</b> si iti da inca o hartie cu numarul unei cutii pline.</p></li>
<li class="bvd-step" data-n="7"><h3>Sparge codul seifului</h3><p>Merge doar dupa ce bomba a explodat. La tastatura apasa <kbd>H</kbd> si ghicesti codul din cateva incercari. Cand reusesti, <b>Laptop de hacking</b> se consuma si seiful se deschide.</p></li>
<li class="bvd-step" data-n="8"><h3>Deschide cutiile cu valori</h3><p>Langa un rand de cutii apasa <kbd>H</kbd> si alegi numarul. Gauresti cutia cu bormasina, apoi iei ce e in ea din inventar. Hartiile iti spun care sunt pline, dar nu le acopera pe toate: pe restul le cautati. Etapa se termina cand ati deschis toate cutiile pline.</p></li>
<li class="bvd-step final" data-n="9"><h3>Ia banii</h3><p>La caruciorul cu bani apasa <kbd>H</kbd>. Strangi banii intr-o animatie lunga, pe care o poti anula. Lucreaza un singur om. Cand termina, jaful e gata.</p></li>
</ol>

<h2>Ce iese din seif</h2>
<div class="bvd-loot">
<div class="bvd-box">
<h3>Cutiile pline</h3>
<ul class="bvd-chips">
<li class="bvd-chip">Bani murdari</li>
<li class="bvd-chip">Bara de aur</li>
<li class="bvd-chip">Diamant</li>
<li class="bvd-chip">Rubin</li>
<li class="bvd-chip">Safir</li>
<li class="bvd-chip">Smarald</li>
</ul>
<p class="bvd-note">O cutie deschisa ramane deschisa pana la final: oricine din echipa ia ce a ramas in ea, fara sa mai gaureasca. Cutiile goale nu au nimic.</p>
</div>
<div class="bvd-box cash">
<h3>Caruciorul</h3>
<ul class="bvd-chips">
<li class="bvd-chip">Bani murdari</li>
</ul>
<p class="bvd-note">Banii ajung la cel care i-a strans si se iau o singura data pe jaf. Fa-ti loc in inventar: daca nu ai loc, nu primesti banii si trebuie sa strangi din nou.</p>
</div>
</div>
<p class="bvd-p bvd-after">Pietrele pretioase si barele de aur le vinzi la <b>Punct de vanzare miner</b>. Barele de aur le cumpara si <b>Amanet Cris</b>. Plata depinde de ce vinzi.</p>

<h2>Politia si riscuri</h2>
<ul class="bvd-rows">
<li class="bvd-row"><b>Alerta vine la etapa 2.</b><p>Cand blochezi intrarea, politia primeste locatia, iar alarma suna in jurul bancii.</p></li>
<li class="bvd-row"><b>Lupta pe camere.</b><p>Politia poate securiza camerele din nou, de la aceeasi cutie electrica. Ca sa le iei inapoi, ai nevoie de alt <b>Telefon Hacking</b>.</p></li>
<li class="bvd-row"><b>Soricelul se taie.</b><p>Cu un <b>Cutter</b>, usa de la intrare se deblocheaza si politia intra.</p></li>
<li class="bvd-row"><b>Bomba se poate dezamorsa.</b><p>Politia o dezamorseaza cu <b>Kit dezamorsare</b>. Daca reuseste, plantati alta. Daca greseste, bomba explodeaza pe loc.</p></li>
<li class="bvd-row"><b>Fara zona sigura.</b><p>Cat timp ruleaza jaful, echipa nu mai e protejata in nicio zona sigura de pe harta.</p></li>
</ul>

<h2>Cand se termina jaful</h2>
<ul class="bvd-rows">
<li class="bvd-row"><b>Ati furat banii</b> din carucior: jaful e finalizat.</li>
<li class="bvd-row"><b>Expira timpul.</b> La pornire primesti cat timp aveti. Dupa aceea, jaful se opreste singur.</li>
<li class="bvd-row"><b>Liderul il opreste</b> din meniu, iese de pe server sau se delogheaza.</li>
<li class="bvd-row"><b>Echipa cade.</b> Toti membrii sunt morti sau au plecat din zona bancii. Cand mori sau pleci din zona, nu mai contezi ca prezent. Daca esti reanimat in zona sau te intorci in ea, contezi din nou.</li>
<li class="bvd-row"><b>Dupa final</b> usile, camerele si cutiile mai raman o vreme asa cum le-ati lasat, apoi banca revine la normal.</li>
</ul>

</div>
