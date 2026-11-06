---
outline: false
---

<style>
.phd {
  --ink: #0c0c0e;
  --panel: #18181b;
  --panel2: #202024;
  --line: #34343b;
  --text: #f4f4f5;
  --mute: #a1a1aa;
  --red: #dc2626;
  --acc: #facc15;
  max-width: 960px;
  margin: 0 auto;
  color: var(--text);
}
.phd *, .phd *::before, .phd *::after { box-sizing: border-box; }
.phd p, .phd li { margin: 0; line-height: 1.6; color: var(--text); }
.phd ul, .phd ol { list-style: none; padding: 0; margin: 0; }
.phd li + li { margin-top: 0; }
.phd b { color: #fff; font-weight: 650; }
.phd code { white-space: normal; overflow-wrap: anywhere; }
.phd a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.phd a:hover { color: #fecaca; }
.phd a:focus-visible { outline: 3px solid var(--acc); outline-offset: 3px; border-radius: 6px; }
.phd .phd-head {
  background: var(--ink); border: 1px solid var(--line); border-left: 4px solid var(--acc);
  border-radius: 18px; padding: clamp(1.2rem, 4vw, 2rem);
}
.phd .phd-kicker { font-size: 0.78rem; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: var(--acc); margin-bottom: 0.5rem; }
.phd .phd-head h1 {
  margin: 0 0 0.7rem; border: 0; padding: 0;
  font-size: clamp(2rem, 7vw, 3rem); line-height: 1.05; font-weight: 800; letter-spacing: -0.03em; color: #fff;
}
.phd .phd-lede { color: var(--mute); font-size: 1.05rem; max-width: 60ch; }
.phd .phd-facts { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 180px), 1fr)); gap: 0.7rem; margin-top: 1rem; }
.phd .phd-facts li { background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 0.9rem 1rem; }
.phd .phd-facts b { display: block; font-size: 1.5rem; line-height: 1.1; color: var(--acc); font-variant-numeric: tabular-nums; }
.phd .phd-facts span { color: var(--mute); font-size: 0.92rem; }
.phd h2 {
  margin: 2.6rem 0 1rem; border: 0; padding: 0 0 0 0.8rem; border-left: 4px solid var(--acc);
  font-size: 1.4rem; font-weight: 750; letter-spacing: -0.015em; color: #fff;
}
.phd .phd-sub { color: var(--mute); margin: -0.4rem 0 1rem; max-width: 64ch; }
.phd .phd-steps { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 200px), 1fr)); gap: 0.7rem; counter-reset: phd; }
.phd .phd-steps li { counter-increment: phd; background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 1rem 1.05rem; }
.phd .phd-steps li::before { content: counter(phd); display: inline-grid; place-items: center; width: 1.6rem; height: 1.6rem; margin-bottom: 0.5rem; border-radius: 50%; background: var(--acc); color: #18181b; font-weight: 800; font-size: 0.85rem; }
.phd .phd-steps b { display: block; }
.phd .phd-steps span { color: var(--mute); font-size: 0.93rem; }
.phd kbd { display: inline-block; min-width: 1.6em; padding: 0 0.4em; border: 1px solid var(--line); border-bottom-width: 3px; border-radius: 6px; background: var(--panel2); color: #fff; font: 700 0.85em/1.6 Inter, system-ui, sans-serif; text-align: center; }
.phd .phd-cat { background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 0.4rem 1.1rem; }
.phd .phd-cat + .phd-cat { margin-top: 0.9rem; }
.phd .phd-cat h3 { margin: 0.8rem 0 0.2rem; border: 0; padding: 0; font-size: 1.1rem; font-weight: 750; color: #fff; }
.phd .phd-items li { display: grid; grid-template-columns: minmax(0, 13rem) minmax(0, 1fr); gap: 0.3rem 1rem; padding: 0.7rem 0; border-top: 1px solid var(--line); }
.phd .phd-items li:first-child { border-top: 0; }
.phd .phd-items b { color: #fff; }
.phd .phd-items span { color: var(--mute); font-size: 0.95rem; }
.phd .phd-notes { display: grid; gap: 0.5rem; margin-top: 1rem; }
.phd .phd-notes li { position: relative; padding-left: 1.3rem; color: var(--mute); }
.phd .phd-notes li::before { content: ''; position: absolute; left: 0.2rem; top: 0.62em; width: 0.45rem; height: 0.45rem; border-radius: 50%; background: var(--acc); }
@media (max-width: 560px) {
  .phd .phd-items li { grid-template-columns: minmax(0, 1fr); }
}
</style>

<div class="phd">
<section class="phd-head">
<p class="phd-kicker">Proprietati · Magazin</p>
<h1>Home Depot</h1>
<p class="phd-lede">Magazinul de unelte si materiale de langa Sandy Shores. Aici iei lockpick-uri, bormasina, substante pentru droguri si materiale pentru crafting. Oricine poate cumpara: nu ai nevoie de job, licenta sau ore jucate.</p>
</section>
<ul class="phd-facts">
<li><b>313</b><span>codul postal al magazinului</span></li>
<li><b>24</b><span>produse, in 3 categorii</span></li>
<li><b>500</b><span>bucati maxim dintr-un produs pe cumparatura</span></li>
</ul>
<h2>Cum cumperi</h2>
<ol class="phd-steps">
<li><b>Gaseste blipul galben</b><span>Pe harta apare ca Home depot, la codul postal <code>313</code>.</span></li>
<li><b>Vorbeste cu vanzatorul</b><span>Mergi langa el si apasa <kbd>E</kbd> la Acceseaza magazinul.</span></li>
<li><b>Pune in cos si plateste</b><span>Banii se iau intai cash, iar ce lipseste se ia din banca. Trebuie sa ai loc in inventar.</span></li>
</ol>
<h2>Ce gasesti</h2>
<p class="phd-sub">Preturile se schimba in timp, le vezi direct in magazin.</p>
<div class="phd-cat">
<h3>Unelte</h3>
<ul class="phd-items">
<li><b>Lockpick simplu</b><span>Deschizi o masina incuiata, din afara ei. Se poate rupe la o incercare.</span></li>
<li><b>Lockpick avansat</b><span>Spargi usile la <a href="/joburi/jafuricase">jaful de case</a> si scoti catusele altui jucator. Se consuma la fiecare incercare, reusita sau nu.</span></li>
<li><b>Bormasina</b><span>Pentru <a href="/joburi/jafuriatm">jaful de bancomat</a>. Din ea se face si Bormasina cu burghiu de diamant, la crafting.</span></li>
<li><b>Soricel</b><span>Blochezi usile la <a href="/joburi/jafuribanca">jaful de banca</a> si la <a href="/joburi/jafuribijuterii">jaful de bijuterii</a>.</span></li>
<li><b>Cutter</b><span>Tai soricelul de pe o usa blocata.</span></li>
<li><b>Binoclu</b><span>Vezi departe, cu zoom.</span></li>
<li><b>Kit Scuba Diving</b><span>Iti da oxigen sub apa: pana la 10 minute cu kitul intreg.</span></li>
</ul>
</div>
<div class="phd-cat">
<h3>Substante</h3>
<ul class="phd-items">
<li><b>Bicarbonat de sodiu</b><span>Intra in Timbru LSD, impreuna cu Hartie.</span></li>
<li><b>Propilen glicol</b><span>Intra in <a href="/joburi/meta">Metamfetamina</a>, impreuna cu Benzoat de sodiu.</span></li>
<li><b>Benzoat de sodiu</b><span>Intra in <a href="/joburi/meta">Metamfetamina</a>, impreuna cu Propilen glicol.</span></li>
</ul>
</div>
<div class="phd-cat">
<h3>Altele</h3>
<ul class="phd-items">
<li><b>Plic gol</b><span>In el ambalezi <a href="/joburi/droguri">drogurile</a>: Plic de iarba, Plic coca, Plic heroina, Plic metamfetamina.</span></li>
<li><b>Hartie</b><span>Intra in Timbru LSD.</span></li>
<li><b>Foite tigari</b><span>Pentru Joint si Pachet tigari.</span></li>
<li><b>Filtre tigari, Folie transparenta</b><span>Pentru Pachet tigari.</span></li>
<li><b>Lemn</b><span>La crafting de arme albe (ciocan, cutit, topor si altele), muscheta si paturi de arme.</span></li>
<li><b>Baterie de masina</b><span>Intra in Bruiatorul mobil, la crafting.</span></li>
<li><b>Extinctor</b><span>Stingi focul.</span></li>
<li><b>Flare Gun si Flare round</b><span>Pistolul de semnalizare si munitia lui.</span></li>
<li><b>Parachute</b><span>Parasuta. O echipezi din inventar inainte sa sari.</span></li>
<li><b>Staniol, Banda adeziva, Carton</b><span>Se vand aici, dar acum nu intra in nicio reteta.</span></li>
</ul>
</div>
<ul class="phd-notes">
<li>Retetele de crafting se pot schimba. Ce iti trebuie exact vezi la masa de crafting.</li>
</ul>
</div>
