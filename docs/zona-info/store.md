---
outline: false
---

<style>
.egs {
  --ink: #0c0c0e;
  --panel: #18181b;
  --panel2: #202024;
  --line: #34343b;
  --text: #f4f4f5;
  --mute: #a1a1aa;
  --red: #cc2b2b;
  --red-deep: #b91c1c;
  --red-soft: rgba(204, 43, 43, 0.14);
  --coin: #f5b931;
  --silver: #c4c7cc;
  --gold: #f2cf3c;
  --plat: #4fe3e0;
  max-width: 960px;
  margin: 0 auto;
  color: var(--text);
  font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.egs *, .egs *::before, .egs *::after { box-sizing: border-box; }
.egs p, .egs li { line-height: 1.6; color: var(--text); margin: 0; }
.egs ul, .egs ol { list-style: none; padding: 0; margin: 0; }
.egs li + li { margin-top: 0; }
.egs b { color: #fff; font-weight: 650; }
.egs code { white-space: normal; overflow-wrap: anywhere; }
.egs a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.egs a:hover { color: #ffb4b4; }
.egs a:focus-visible { outline: 3px solid var(--red); outline-offset: 3px; border-radius: 6px; }
.egs kbd {
  font: inherit; font-size: 0.85em; font-weight: 700; color: #fff; background: var(--red-deep);
  border-radius: 6px; padding: 0.05rem 0.45rem;
}
/* hero */
.egs-hero {
  position: relative;
  background: radial-gradient(100% 130% at 100% 0%, rgba(245, 185, 49, 0.16), transparent 55%),
              radial-gradient(110% 120% at 0% 100%, rgba(185, 28, 28, 0.28), var(--ink) 65%);
  border: 1px solid var(--line);
  border-radius: 22px;
  padding: clamp(1.25rem, 4vw, 2.5rem);
  overflow: hidden;
}
.egs .egs-kicker {
  font-size: 0.78rem; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: var(--red);
  margin-bottom: 0.6rem;
}
.egs-hero h1 {
  margin: 0 0 0.8rem; border: 0; padding: 0;
  font-size: clamp(2rem, 6vw, 3.3rem); line-height: 1.05; font-weight: 800; letter-spacing: -0.03em; color: #fff;
}
.egs-hero h1 span { color: var(--coin); }
.egs .egs-lede { max-width: 56ch; color: var(--mute); font-size: 1.05rem; }
.egs .egs-cta { display: flex; flex-wrap: wrap; gap: 0.6rem; margin-top: 1.4rem; }
.egs .egs-cta a {
  display: inline-flex; align-items: center; gap: 0.4rem; text-decoration: none;
  border-radius: 999px; padding: 0.55rem 1.1rem; font-weight: 700; color: #fff;
  border: 1px solid var(--line); background: var(--panel);
}
.egs .egs-cta a.main { background: var(--red-deep); border-color: var(--red-deep); }
.egs .egs-cta a:hover { border-color: var(--red); color: #fff; }
/* section titles */
.egs h2 {
  margin: 3rem 0 1rem; border: 0; padding: 0;
  font-size: 1.5rem; font-weight: 750; letter-spacing: -0.015em; color: #fff;
}
.egs h2::before {
  content: ''; display: inline-block; width: 0.55rem; height: 0.55rem; margin-right: 0.6rem;
  border-radius: 2px; background: var(--red); vertical-align: middle; transform: translateY(-2px) rotate(45deg);
}
.egs .egs-sub { color: var(--mute); margin: -0.4rem 0 1rem; }
/* ways to open the store */
.egs .egs-open { display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 0.75rem; }
.egs .egs-open li { background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 1rem 1.1rem; }
.egs .egs-open b { display: block; margin-bottom: 0.25rem; }
.egs .egs-open span { color: var(--mute); font-size: 0.93rem; }
/* what coins buy */
.egs .egs-buy { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 0.75rem; }
.egs .egs-buy li {
  background: var(--panel2); border: 1px solid var(--line); border-left: 3px solid var(--coin);
  border-radius: 12px; padding: 0.85rem 1rem;
}
.egs .egs-buy b { display: block; }
.egs .egs-buy span { color: var(--mute); font-size: 0.92rem; }
/* earn coins */
.egs .egs-earn { counter-reset: egs; display: grid; gap: 0.75rem; }
.egs .egs-earn li {
  counter-increment: egs; position: relative; background: var(--panel); border: 1px solid var(--line);
  border-radius: 14px; padding: 1rem 1.1rem 1rem 3.6rem;
}
.egs .egs-earn li::before {
  content: counter(egs); position: absolute; left: 1rem; top: 1rem; display: grid; place-items: center;
  width: 1.9rem; height: 1.9rem; border-radius: 50%; background: var(--coin); color: var(--ink); font-weight: 800;
}
.egs .egs-earn p { color: var(--mute); }
.egs .egs-earn b { color: #fff; }
/* VIP tiers */
.egs .egs-tiers { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; align-items: stretch; }
.egs .egs-tier {
  --tier: var(--silver);
  display: flex; flex-direction: column;
  --tier-soft: rgba(196, 199, 204, 0.12);
  background: linear-gradient(180deg, var(--tier-soft), var(--panel) 40%);
  border: 1px solid var(--line); border-top: 3px solid var(--tier); border-radius: 18px; padding: 1.25rem 1.3rem;
}
.egs .egs-tier.gold { --tier: var(--gold); --tier-soft: rgba(242, 207, 60, 0.12); }
.egs .egs-tier.plat { --tier: var(--plat); --tier-soft: rgba(79, 227, 224, 0.12); border-color: rgba(79, 227, 224, 0.45); }
.egs .egs-tier h3 { margin: 0; border: 0; padding: 0; font-size: 1.35rem; font-weight: 800; color: #fff; }
.egs .egs-tier h3 span { color: var(--tier); }
.egs .egs-perks { margin-top: 0.9rem; }
.egs .egs-perks li {
  display: flex; justify-content: space-between; gap: 0.75rem; padding: 0.5rem 0;
  border-top: 1px solid var(--line); font-size: 0.95rem;
}
.egs .egs-perks li span:first-child { color: var(--mute); }
.egs .egs-perks li span:last-child { color: #fff; font-weight: 650; text-align: right; }
.egs .egs-cars-h { margin-top: 1rem; font-size: 0.78rem; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: var(--tier); }
.egs .egs-cars { margin-top: 0.4rem; }
.egs .egs-cars li { font-size: 0.95rem; padding: 0.15rem 0; }
.egs .egs-cars li.inc { color: var(--mute); font-style: italic; }
.egs .egs-cars small { color: var(--mute); }
.egs .egs-common { margin-top: 1rem; display: flex; flex-wrap: wrap; gap: 0.5rem; }
.egs .egs-common li {
  background: var(--panel2); border: 1px solid var(--line); border-radius: 999px; padding: 0.3rem 0.85rem; font-size: 0.9rem;
}
/* screenshot */
.egs .egs-shot { margin: 1.25rem 0 0; background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 0.5rem; }
.egs .egs-shot img { display: block; width: 100%; height: auto; border-radius: 11px; margin: 0; }
.egs .egs-shot figcaption { color: var(--mute); font-size: 0.9rem; padding: 0.6rem 0.4rem 0.2rem; }
/* sanctions */
.egs .egs-warn {
  background: var(--red-soft); border: 1px solid rgba(204, 43, 43, 0.5); border-radius: 16px; padding: 1.1rem 1.25rem;
}
.egs .egs-warn p + p { margin-top: 0.6rem; }
.egs .egs-steps { margin-top: 0.9rem; display: grid; gap: 0.5rem; }
.egs .egs-steps li { padding-left: 1.4rem; position: relative; }
.egs .egs-steps li::before { content: ''; position: absolute; left: 0.2rem; top: 0.65em; width: 0.45rem; height: 0.45rem; border-radius: 50%; background: var(--red); }
.egs .egs-sub.egs-after { margin: 1rem 0 0; }
.egs .egs-warn .egs-gap { margin-top: 0.9rem; }
.egs .egs-foot { margin-top: 2.5rem; color: var(--mute); text-align: center; }
</style>

<div class="egs">
<section class="egs-hero">
<p class="egs-kicker">Zona info</p>
<h1>Store si <span>EG Coins</span></h1>
<p class="egs-lede">EG Coins este moneda premium a serverului. Cu ea iei VIP, masini premium, bani in joc si alte pachete. Multumim ca sustii comunitatea EliteGamers!</p>
<div class="egs-cta">
<a class="main" href="https://elitegamers.tebex.io" target="_blank" rel="noopener">Magazin online (Tebex)</a>
<a href="https://discord.gg/elitegamers" target="_blank" rel="noopener">Intrebari pe Discord</a>
</div>
</section>
<h2>Unde cheltui EG Coins</h2>
<p class="egs-sub">Magazinul din joc se deschide in trei feluri:</p>
<ul class="egs-open">
<li><b>Tasta <kbd>K</kbd></b><span>Meniul radial, apoi <code>Magazin in joc</code></span></li>
<li><b>Tasta <kbd>ESC</kbd></b><span>Meniul de pauza, apoi <code>Magazin din joc</code></span></li>
<li><b>Comanda <code>/store</code></b><span>Scrisa in chat</span></li>
</ul>
<h2>Ce poti lua cu EG Coins</h2>
<ul class="egs-buy">
<li><b>VIP</b><span>Silver, Gold sau Platinum, pe 30 sau 90 de zile</span></li>
<li><b>Bani in joc</b><span>Pachete de bani, direct in banca</span></li>
<li><b>Ore jucate</b><span>Pachete de la 25 la 1000 de ore</span></li>
<li><b>Iteme premium</b><span>Jante premium, antilag, sistem audio, ghiozdan premium, licenta de operator drone</span></li>
<li><b>Sloturi de garaj</b><span>+1, +3, +5 sau +10 sloturi</span></li>
<li><b>Sala</b><span>Stamina si putere la maxim</span></li>
<li><b>Sanctiuni</b><span>Iesi din admin-jail sau stergi cel mai vechi avertisment</span></li>
<li><b>Masini premium</b><span>In dealership, la categoria premium</span></li>
<li><b>Case si skin-uri de arme</b><span>Case platite in EG Coins si <a href="/general/skin-uri-arme">skin-uri premium</a></span></li>
</ul>
<figure class="egs-shot">
<img src="../public/store/dealership.png" alt="Dealership-ul Premium Deluxe Motorsport din oras" loading="lazy">
<figcaption>Dealership-ul din oras (Premium Deluxe Motorsport): aici gasesti masinile premium si pe cele VIP.</figcaption>
</figure>
<h2>Cum obtii EG Coins</h2>
<ol class="egs-earn">
<li><p><b>Din magazinul online.</b> Cumperi de pe <a href="https://elitegamers.tebex.io" target="_blank" rel="noopener">elitegamers.tebex.io</a> si treci ID-ul tau din joc. Monedele intra automat in cont, chiar daca nu esti pe server in acel moment.</p></li>
<li><p><b>Din pachetul de inceput.</b> Un personaj nou primeste un EG Coin ca item. Il folosesti din inventar si intra in cont.</p></li>
</ol>
<h2>VIP</h2>
<p class="egs-sub">Trei niveluri. Un nivel mai mare are tot ce are cel de sub el, plus ceva in plus.</p>
<div class="egs-tiers">
<div class="egs-tier">
<h3>VIP <span>Silver</span></h3>
<ul class="egs-perks">
<li><span>Boost la joburi</span><span>+5%</span></li>
<li><span>Salariu VIP</span><span>2.000 € / ora</span></li>
<li><span>Bani la cumparare (30 zile)</span><span>75.000 €</span></li>
<li><span>Prioritate la coada</span><span>Nivel 1</span></li>
</ul>
<p class="egs-cars-h">Masini VIP</p>
<ul class="egs-cars">
<li>Ubermacht Oracle XS-LE</li>
<li>Ubermacht Sentinel 4CSL</li>
<li>Obey 9R</li>
</ul>
</div>
<div class="egs-tier gold">
<h3>VIP <span>Gold</span></h3>
<ul class="egs-perks">
<li><span>Boost la joburi</span><span>+10%</span></li>
<li><span>Salariu VIP</span><span>3.500 € / ora</span></li>
<li><span>Bani la cumparare (30 zile)</span><span>150.000 €</span></li>
<li><span>Prioritate la coada</span><span>Nivel 2</span></li>
</ul>
<p class="egs-cars-h">Masini VIP</p>
<ul class="egs-cars">
<li>Pegassi Reaper Custom</li>
<li>Grotti Turismo S</li>
<li>Gallivanter Baller ST-D Platinum</li>
<li>Pegassi Toros</li>
<li class="inc">+ toate masinile de la Silver</li>
</ul>
</div>
<div class="egs-tier plat">
<h3>VIP <span>Platinum</span></h3>
<ul class="egs-perks">
<li><span>Boost la joburi</span><span>+15%</span></li>
<li><span>Salariu VIP</span><span>5.000 € / ora</span></li>
<li><span>Bani la cumparare (30 zile)</span><span>250.000 €</span></li>
<li><span>Prioritate la coada</span><span>Nivel 3</span></li>
</ul>
<p class="egs-cars-h">Masini VIP</p>
<ul class="egs-cars">
<li>Invetero Coquette VR1</li>
<li>Benefactor Krieger</li>
<li>Pfister Comet GTS2</li>
<li>Annis Elegy RH8 FR-Works</li>
<li>Pegassi Severo Widebody</li>
<li>Pegassi Speeder <small>(barca)</small></li>
<li>Sparrow <small>(elicopter)</small></li>
<li class="inc">+ toate masinile de la Gold</li>
</ul>
</div>
</div>
<ul class="egs-common">
<li>Suport</li>
<li>Grad VIP pe Discord si in joc</li>
<li>Salariul VIP intra in banca, la fiecare ora</li>
<li>Pachetul de 90 de zile da mai multi bani la cumparare</li>
<li>Acelasi nivel cumparat din nou adauga zilele la cele ramase</li>
</ul>
<p class="egs-sub egs-after">Masinile VIP le iei gratis din dealership, cate una din fiecare model, cat timp ai VIP-ul. Barca o gasesti la dealership-ul de barci, elicopterul la cel de avioane. Daca VIP-ul expira, nu le mai poti scoate din garaj pana nu il reactivezi.</p>
<h2>Sanctiuni si unban</h2>
<div class="egs-warn">
<p>Ai primit ban temporar sau permanent si vrei sa platesti ridicarea lui? Pe Tebex gasesti <b>Unban temporar</b>, <b>Unban permanent</b> si <b>Clear warn</b>.</p>
<ul class="egs-steps">
<li><b>Inainte sa cumperi, deschide un ticket pe <a href="https://discord.gg/elitegamers" target="_blank" rel="noopener">Discord</a>.</b> Echipa iti spune daca sanctiunea ta se poate ridica.</li>
<li>Unban-ul nu se aplica automat: dupa plata, staff-ul ridica sanctiunea manual, pe ticketul tau.</li>
<li>Unban-ul temporar ridica doar un ban temporar. Pentru un ban permanent iei Unban permanent.</li>
<li>Clear warn sterge cel mai vechi avertisment activ.</li>
<li><b>Unban Discord:</b> dupa plata, deschide un ticket pe <a href="https://discord.gg/elitegamers" target="_blank" rel="noopener">Discord</a> si ataseaza dovada platii (emailul de confirmare).</li>
</ul>
<p class="egs-gap"><b>Atentie:</b> respectarea regulamentului FiveM e obligatorie. Daca primesti <b>ban fara drept de plata</b>, pachetele cumparate nu se mai pot folosi.</p>
</div>
<p class="egs-foot">Ai intrebari? Echipa te asteapta pe <a href="https://discord.gg/elitegamers" target="_blank" rel="noopener">Discord</a>.</p>
</div>
