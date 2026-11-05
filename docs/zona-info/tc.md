---
outline: false
---

<style>
.egt {
  --ink: #0c0c0e;
  --panel: #18181b;
  --panel2: #202024;
  --line: #34343b;
  --text: #f4f4f5;
  --mute: #a1a1aa;
  --red: #cc2b2b;
  --red-deep: #b91c1c;
  --red-soft: rgba(204, 43, 43, 0.14);
  max-width: 860px;
  margin: 0 auto;
  color: var(--text);
  font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.egt *, .egt *::before, .egt *::after { box-sizing: border-box; }
.egt p, .egt li { line-height: 1.6; color: var(--text); margin: 0; }
.egt ul, .egt ol { list-style: none; padding: 0; margin: 0; }
.egt li + li { margin-top: 0; }
.egt b { color: #fff; font-weight: 650; }
.egt a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.egt a:hover { color: #ffb4b4; }
.egt a:focus-visible { outline: 3px solid var(--red); outline-offset: 3px; border-radius: 6px; }
/* hero */
.egt-hero {
  background: radial-gradient(110% 120% at 100% 0%, rgba(185, 28, 28, 0.3), var(--ink) 62%);
  border: 1px solid var(--line);
  border-radius: 22px;
  padding: clamp(1.25rem, 4vw, 2.5rem);
}
.egt .egt-kicker {
  font-size: 0.78rem; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: var(--red);
  margin-bottom: 0.6rem;
}
.egt-hero h1 {
  margin: 0 0 0.8rem; border: 0; padding: 0;
  font-size: clamp(2rem, 6vw, 3.1rem); line-height: 1.05; font-weight: 800; letter-spacing: -0.03em; color: #fff;
}
.egt .egt-lede { max-width: 58ch; color: var(--mute); font-size: 1.05rem; }
/* table of contents */
.egt .egt-toc {
  counter-reset: egt-toc; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 0.5rem; margin-top: 1.4rem;
}
.egt .egt-toc li { counter-increment: egt-toc; }
.egt .egt-toc a {
  display: flex; align-items: center; gap: 0.6rem; height: 100%; text-decoration: none; color: #fff;
  font-weight: 650; font-size: 0.93rem; background: var(--panel); border: 1px solid var(--line);
  border-radius: 12px; padding: 0.55rem 0.8rem;
}
.egt .egt-toc a::before {
  content: counter(egt-toc); flex: none; display: grid; place-items: center; width: 1.6rem; height: 1.6rem;
  border-radius: 8px; background: var(--red-soft); color: #ffb4b4; font-weight: 800; font-size: 0.85rem;
}
.egt .egt-toc a:hover { border-color: var(--red); color: #fff; }
/* clauses */
.egt .egt-clauses { display: grid; gap: 1rem; margin-top: 2rem; }
.egt .egt-clause {
  position: relative; background: var(--panel); border: 1px solid var(--line); border-radius: 18px;
  padding: clamp(1.1rem, 3vw, 1.5rem) clamp(1.1rem, 3vw, 1.6rem); scroll-margin-top: 80px;
}
.egt .egt-clause:target { border-color: rgba(204, 43, 43, 0.7); background: var(--panel2); }
.egt .egt-clause.strong { border-left: 3px solid var(--red); }
.egt h2 {
  display: flex; align-items: center; gap: 0.75rem;
  margin: 0 0 0.8rem; border: 0; padding: 0;
  font-size: 1.3rem; font-weight: 750; letter-spacing: -0.015em; line-height: 1.25; color: #fff;
}
.egt h2 .egt-num {
  flex: none; display: grid; place-items: center; width: 2.1rem; height: 2.1rem; border-radius: 10px;
  background: var(--red-deep); color: #fff; font-size: 1rem; font-weight: 800;
}
.egt .egt-clause p { color: #d4d4d8; }
.egt .egt-clause p + p, .egt .egt-clause p + ul, .egt .egt-clause ul + p { margin-top: 0.6rem; }
.egt .egt-items { display: grid; gap: 0.45rem; }
.egt .egt-items li { position: relative; padding-left: 1.25rem; color: #d4d4d8; }
.egt .egt-items li::before {
  content: ''; position: absolute; left: 0.1rem; top: 0.62em; width: 0.42rem; height: 0.42rem;
  border-radius: 2px; background: var(--red); transform: rotate(45deg);
}
.egt .egt-split { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 0.75rem; margin-top: 0.2rem; }
.egt .egt-box { background: var(--panel2); border: 1px solid var(--line); border-radius: 12px; padding: 0.85rem 1rem; }
.egt .egt-box .egt-label {
  font-size: 0.75rem; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: var(--mute);
  margin-bottom: 0.5rem;
}
@media (prefers-reduced-motion: reduce) {
  .egt *, .egt *::before { transition: none; scroll-behavior: auto; }
}
</style>

<div class="egt">
<section class="egt-hero">
<p class="egt-kicker">Zona info</p>
<h1>Termeni si conditii</h1>
<p class="egt-lede">Regulile de baza dintre tine si serverul ELITEGAMERS.RO: cine poate juca, cum te porti, cum se dau sanctiunile si ce date pastram despre tine.</p>
<ol class="egt-toc" aria-label="Cuprins">
<li><a href="#egt-1">Acceptarea termenilor</a></li>
<li><a href="#egt-2">Acces si eligibilitate</a></li>
<li><a href="#egt-3">Comportament si roleplay</a></li>
<li><a href="#egt-4">Moderare si sanctiuni</a></li>
<li><a href="#egt-5">Confidentialitate si date</a></li>
<li><a href="#egt-6">Modificarea termenilor</a></li>
</ol>
</section>
<div class="egt-clauses">
<section class="egt-clause" id="egt-1">
<h2><span class="egt-num">1</span>Acceptarea termenilor</h2>
<p>Daca intri si joci pe serverul <b>ELITEGAMERS.RO</b>, accepti in totalitate termenii si conditiile de pe aceasta pagina.</p>
<p>Iti recomandam sa citesti tot <a href="/zona-info/regulament">regulamentul</a>. Asa eviti sanctiunile si ne ajuti sa pastram jocul corect si realist.</p>
</section>
<section class="egt-clause" id="egt-2">
<h2><span class="egt-num">2</span>Acces si eligibilitate</h2>
<p>Ca sa joci pe server, ai nevoie de:</p>
<ul class="egt-items">
<li>o <b>copie originala</b> a jocului <b>Grand Theft Auto V</b></li>
<li>clientul <b>FiveM</b> instalat</li>
<li>un <b>microfon care functioneaza</b>, pentru ca in joc vorbesti cu ceilalti pe voce</li>
</ul>
</section>
<section class="egt-clause strong" id="egt-3">
<h2><span class="egt-num">3</span>Comportament si roleplay</h2>
<p>Pe server te porti <b>matur, responsabil si realist</b>.</p>
<p>Ai <b>strict interzis</b> sa:</p>
<ul class="egt-items">
<li>folosesti bug-uri, cheat-uri sau modificari interzise</li>
<li>incalci regulile de roleplay (<i>metagaming, powergaming, combat logging</i>)</li>
<li>jignesti sau sa te porti ostil cu alti jucatori sau cu staff-ul</li>
</ul>
</section>
<section class="egt-clause strong" id="egt-4">
<h2><span class="egt-num">4</span>Moderare si sanctiuni</h2>
<p>Echipa de administrare are autoritatea sa pastreze ordinea si sa impuna respectarea regulilor. Pentru asta, poate:</p>
<ul class="egt-items">
<li>sa te suspende <b>temporar sau permanent</b>, dupa cat de grava e abaterea</li>
<li>sa verifice si sa analizeze sesizarile, pe baza <b>dovezilor trimise</b></li>
<li>sa aplice sanctiunea direct, <b>fara sa te anunte inainte</b>, daca fapta o justifica</li>
</ul>
</section>
<section class="egt-clause" id="egt-5">
<h2><span class="egt-num">5</span>Confidentialitate si date personale</h2>
<p>Serverul colecteaza doar datele minime de care are nevoie ca sa functioneze si sa fie sigur.</p>
<div class="egt-split">
<div class="egt-box">
<p class="egt-label">Ce colectam, de exemplu</p>
<ul class="egt-items">
<li>adresa IP</li>
<li>activitatea ta in joc</li>
<li>numele de utilizator</li>
<li>conturile asociate: Discord, licenta GTA V, HWID si altele de acest fel</li>
<li>imagini din joc</li>
<li>clipuri video fara sunet din joc</li>
</ul>
</div>
<div class="egt-box">
<p class="egt-label">Ce facem cu ele</p>
<ul class="egt-items">
<li>le folosim <b>doar intern</b>, pentru administrarea serverului</li>
<li><b>nu le dam tertilor</b>, cu exceptia cazurilor prevazute de lege</li>
</ul>
</div>
</div>
</section>
<section class="egt-clause" id="egt-6">
<h2><span class="egt-num">6</span>Modificarea termenilor</h2>
<p>Termenii si conditiile se pot actualiza oricand, ca sa tina pasul cu:</p>
<ul class="egt-items">
<li>schimbarile din legislatie</li>
<li>schimbarile din interiorul comunitatii</li>
</ul>
<p>E responsabilitatea ta sa verifici din cand in cand aceasta pagina, ca sa stii ce s-a schimbat.</p>
</section>
</div>
</div>
