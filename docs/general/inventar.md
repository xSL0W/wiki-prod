---
outline: false
---

<style>
.inv {
  --panel: #17171a;
  --panel2: #1f1f23;
  --line: #2f2f36;
  --text: #f4f4f5;
  --mute: #a1a1aa;
  --red: #ef4444;
  --red-deep: #b91c1c;
  --red-soft: rgba(239, 68, 68, 0.14);
  max-width: 960px;
  margin: 0 auto;
  color: var(--text);
  font-family: Inter, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.inv *, .inv *::before, .inv *::after { box-sizing: border-box; }
.inv p, .inv li { line-height: 1.6; color: var(--text); margin: 0; }
.inv ul, .inv ol { list-style: none; padding: 0; margin: 0; }
.inv li + li { margin-top: 0; }
.inv b { color: #fff; font-weight: 650; }
.inv a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.inv a:hover { color: #fecaca; }
.inv a:focus-visible { outline: 3px solid var(--red); outline-offset: 3px; border-radius: 6px; }
.inv kbd {
  font: inherit; font-size: 0.85em; font-weight: 700; color: #fff; background: var(--red-deep);
  border-radius: 6px; padding: 0.05rem 0.45rem; white-space: nowrap;
}
.inv .inv-head { border-bottom: 1px solid var(--line); padding-bottom: 1.2rem; }
.inv .inv-kicker { font-size: 0.78rem; font-weight: 700; letter-spacing: 0.16em; text-transform: uppercase; color: var(--red); margin-bottom: 0.4rem; }
.inv .inv-head h1 { margin: 0 0 0.6rem; border: 0; padding: 0; font-size: clamp(2rem, 6vw, 3rem); line-height: 1.05; font-weight: 800; letter-spacing: -0.03em; color: #fff; }
.inv .inv-lede { color: var(--mute); max-width: 62ch; font-size: 1.05rem; }
.inv .inv-h2 {
  display: flex; align-items: center; gap: 0.65rem;
  margin: 2.6rem 0 0.9rem; border: 0; padding: 0;
  font-size: 1.4rem; font-weight: 750; letter-spacing: -0.015em; line-height: 1.25; color: #fff;
}
.inv .inv-h2::before {
  content: ''; flex: none; width: 0.6rem; height: 0.6rem; border-radius: 2px; background: var(--red);
  transform: rotate(45deg); box-shadow: 0 0 0 4px var(--red-soft);
}
.inv .inv-h3 { margin: 0 0 0.35rem; border: 0; padding: 0; font-size: 1.02rem; font-weight: 700; color: #fff; line-height: 1.3; }
.inv .inv-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 250px), 1fr)); gap: 0.75rem; }
.inv .inv-card { background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 1.05rem 1.2rem; }
.inv .inv-card p { color: var(--mute); font-size: 0.96rem; }
.inv .inv-card p + p { margin-top: 0.5rem; }
/* keys */
.inv .inv-keys { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 210px), 1fr)); gap: 0.6rem; }
.inv .inv-keys li { display: flex; gap: 0.75rem; align-items: flex-start; background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 0.75rem 0.9rem; }
.inv .inv-keys kbd { flex: none; min-width: 2.6rem; text-align: center; font-size: 0.9rem; padding: 0.2rem 0.5rem; }
.inv .inv-keys span { color: var(--mute); font-size: 0.93rem; line-height: 1.45; }
.inv .inv-keys b { display: block; color: #fff; }
/* stats */
.inv .inv-stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 150px), 1fr)); gap: 0.6rem; margin-top: 1.1rem; }
.inv .inv-stats li { background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 0.7rem 0.9rem; }
.inv .inv-stats b { display: block; font-size: 1.6rem; line-height: 1.1; font-weight: 800; color: #fff; }
.inv .inv-stats span { display: block; color: var(--mute); font-size: 0.82rem; margin-top: 0.15rem; }
/* bullets */
.inv .inv-list li { position: relative; padding-left: 1.2rem; color: var(--mute); font-size: 0.96rem; }
.inv .inv-list li + li { margin-top: 0.45rem; }
.inv .inv-list li::before { content: ''; position: absolute; left: 0.1rem; top: 0.62em; width: 0.42rem; height: 0.42rem; border-radius: 50%; background: var(--red); }
.inv .inv-list b { color: var(--text); }
/* backpacks table */
.inv .inv-bags { border: 1px solid var(--line); border-radius: 14px; overflow: hidden; margin-top: 0.7rem; }
.inv .inv-bags li { display: flex; justify-content: space-between; gap: 1rem; padding: 0.5rem 0.9rem; border-top: 1px solid var(--line); font-size: 0.94rem; color: var(--mute); }
.inv .inv-bags li:first-child { border-top: 0; }
.inv .inv-bags li b { color: #fff; font-variant-numeric: tabular-nums; }
.inv .inv-tags { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-top: 0.6rem; }
.inv .inv-tags li { font-size: 0.82rem; font-weight: 650; color: var(--text); background: var(--panel2); border: 1px solid var(--line); border-radius: 999px; padding: 0.2rem 0.7rem; }
</style>

<div class="inv">
<header class="inv-head">
<p class="inv-kicker">Sisteme generale</p>
<h1>Inventar</h1>
<p class="inv-lede">Tot ce cari asupra ta: bani, arme, documente, mancare. Fiecare obiect are greutate, asa ca nu poti duce orice.</p>
<ul class="inv-stats">
<li><b>50</b><span>sloturi</span></li>
<li><b>20 kg</b><span>greutate de baza</span></li>
<li><b>5</b><span>sloturi rapide (hotbar)</span></li>
</ul>
</header>

<h2 class="inv-h2" id="taste">Taste</h2>
<ul class="inv-keys">
<li><kbd>TAB</kbd><span><b>Inventarul tau</b>In masina deschide si torpedoul.</span></li>
<li><kbd>I</kbd><span><b>Portbagaj sau depozit</b>Langa spatele unei masini descuiate sau la un depozit.</span></li>
<li><kbd>1-5</kbd><span><b>Folosesti slotul</b>Primele 5 sloturi din inventar sunt hotbar-ul.</span></li>
<li><kbd>J</kbd><span><b>Arata hotbar-ul</b>Vezi ce ai pe tastele 1-5.</span></li>
<li><kbd>R</kbd><span><b>Reincarci arma</b>Cu munitia potrivita din inventar.</span></li>
<li><kbd>G</kbd><span><b>Interactiuni</b>Pe jucatori (perchezitie, furt) si pe masini (portbagaj).</span></li>
</ul>

<h2 class="inv-h2" id="greutate">Greutate si ghiozdane</h2>
<div class="inv-grid">
<div class="inv-card">
<h3 class="inv-h3">Ghiozdane</h3>
<p>Un ghiozdan in inventar iti mareste greutatea pe care o duci. Daca ai mai multe, conteaza doar cel mai mare.</p>
<ul class="inv-bags">
<li>Ghiozdan mic <b>+20 kg</b></li>
<li>Ghiozdan mediu <b>+35 kg</b></li>
<li>Ghiozdan mare <b>+50 kg</b></li>
<li>Ghiozdan premium <b>+80 kg</b></li>
</ul>
<p style="margin-top:0.6rem">Ghiozdanul premium expira dupa o perioada si primesti avertisment inainte.</p>
</div>
<div class="inv-card">
<h3 class="inv-h3">Arme</h3>
<ul class="inv-list">
<li>Armele si munitia sunt iteme ca oricare altele.</li>
<li>O arma mai grea de <b>3 kg</b> nu o poti folosi fara ghiozdan. Medicii si canistra de benzina sunt exceptie.</li>
<li>Armele se uzeaza. O arma fara durabilitate nu se mai reincarca.</li>
</ul>
<h3 class="inv-h3" style="margin-top:1rem">Sala</h3>
<p>Forta castigata la <a href="/general/sala">sala</a> iti adauga si ea greutate.</p>
</div>
</div>

<h2 class="inv-h2" id="ofera-arunca">Oferi si arunci</h2>
<div class="inv-grid">
<div class="inv-card"><h3 class="inv-h3">Ofera</h3><p>Trage itemul pe <b>Ofera</b> si alege jucatorul din lista celor de langa tine.</p></div>
<div class="inv-card"><h3 class="inv-h3">Arunca</h3><p>Trage itemul pe <b>Arunca</b>. Pe jos apare o punga pe care o poate lua oricine.</p></div>
<div class="inv-card"><h3 class="inv-h3">Bani</h3><p>Banii cash sunt itemul <b>Euro</b> si sunt mereu egali cu numerarul tau. Daca ai inventarul plin, banii raman in cont si apar ca item cand faci loc. <b>Bani murdari</b> sunt un item separat.</p></div>
</div>

<h2 class="inv-h2" id="containere">Masini si depozite</h2>
<div class="inv-grid">
<div class="inv-card"><h3 class="inv-h3">Portbagaj</h3><p>Mergi la spatele masinii si apasa <kbd>I</kbd> cand vezi bula <b>Portbagaj</b>. Masina trebuie sa fie descuiata. Fiecare tip de masina are alt spatiu.</p></div>
<div class="inv-card"><h3 class="inv-h3">Torpedou</h3><p>Apasa <kbd>TAB</kbd> cand esti in masina.</p></div>
<div class="inv-card"><h3 class="inv-h3">In safezone</h3><p>Nimeni nu iti deschide portbagajul sau torpedoul fara acordul tau: primesti o cerere pe care o accepti sau o refuzi. Politia in serviciu nu are nevoie de acord.</p></div>
<div class="inv-card"><h3 class="inv-h3">Depozite</h3><p>Pentru lucrurile pe care nu vrei sa le cari dupa tine, vezi <a href="/general/depozit">Depozit</a>.</p></div>
</div>

<h2 class="inv-h2" id="reguli">Ce nu poti pierde</h2>
<div class="inv-grid">
<div class="inv-card">
<h3 class="inv-h3">Nu se arunca si nu se dau</h3>
<p>Le poti muta doar in inventarul tau:</p>
<ul class="inv-tags">
<li>Moneda oficiala EG</li><li>Sistem Audio</li><li>Antilag</li><li>Jante Premium A</li><li>Jante Premium B</li><li>Ghiozdan premium</li><li>Starter Pack</li>
</ul>
</div>
<div class="inv-card">
<h3 class="inv-h3">Nu ti se pot fura</h3>
<ul class="inv-tags">
<li>Buletin</li><li>Permis de conducere</li><li>Talon de inmatriculare</li><li>Mapa documente</li><li>Documente</li><li>Vehicle Keys</li><li>Key Bag</li>
</ul>
</div>
</div>

<h2 class="inv-h2" id="jaf">Perchezitie si furt</h2>
<div class="inv-card">
<ul class="inv-list">
<li><b>Perchezitioneaza</b> (<kbd>G</kbd> pe jucator): vezi ce are in inventar, fara sa iei ceva. El primeste notificare.</li>
<li><b>Fura din buzunar</b> merge doar daca jucatorul e incatusat sau sta cu mainile sus. Daca e doar mort, nu il poti jefui.</li>
<li>In zonele de jaf (in jurul unui airdrop, in cercul unui razboi activ) poti fura de la oricine. Cine poarta loot proaspat de la airdrop poate fi jefuit oriunde.</li>
<li>Medicii in serviciu nu pot fura de la nimeni.</li>
</ul>
</div>
</div>
