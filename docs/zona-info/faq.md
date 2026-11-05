---
outline: false
---

<style>
.egq {
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
.egq *, .egq *::before, .egq *::after { box-sizing: border-box; }
.egq p, .egq li { line-height: 1.6; color: var(--text); margin: 0; }
.egq ul, .egq ol { list-style: none; padding: 0; margin: 0; }
.egq li + li { margin-top: 0; }
.egq b { color: #fff; font-weight: 650; }
.egq a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.egq a:hover { color: #ffb4b4; }
.egq a:focus-visible { outline: 3px solid var(--red); outline-offset: 3px; border-radius: 6px; }
.egq kbd {
  font: inherit; font-size: 0.85em; font-weight: 700; color: #fff; background: var(--red-deep);
  border-radius: 6px; padding: 0.05rem 0.45rem;
}
/* hero */
.egq-hero {
  background: radial-gradient(110% 120% at 100% 0%, rgba(185, 28, 28, 0.3), var(--ink) 62%);
  border: 1px solid var(--line);
  border-radius: 22px;
  padding: clamp(1.25rem, 4vw, 2.5rem);
}
.egq .egq-kicker {
  font-size: 0.78rem; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: var(--red);
  margin-bottom: 0.6rem;
}
.egq-hero h1 {
  margin: 0 0 0.8rem; border: 0; padding: 0;
  font-size: clamp(2rem, 6vw, 3.1rem); line-height: 1.05; font-weight: 800; letter-spacing: -0.03em; color: #fff;
}
.egq .egq-lede { max-width: 56ch; color: var(--mute); font-size: 1.05rem; }
.egq .egq-jump { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1.3rem; }
.egq .egq-jump a {
  text-decoration: none; color: #fff; font-weight: 650; font-size: 0.92rem;
  background: var(--panel); border: 1px solid var(--line); border-radius: 999px; padding: 0.35rem 0.9rem;
}
.egq .egq-jump a:hover { border-color: var(--red); }
/* groups */
.egq h2 {
  margin: 2.6rem 0 0.9rem; border: 0; padding: 0; scroll-margin-top: 80px;
  font-size: 1.35rem; font-weight: 750; letter-spacing: -0.015em; color: #fff;
}
.egq h2::before {
  content: ''; display: inline-block; width: 0.55rem; height: 0.55rem; margin-right: 0.6rem;
  border-radius: 2px; background: var(--red); vertical-align: middle; transform: translateY(-2px) rotate(45deg);
}
/* accordions */
.egq .egq-list { display: grid; gap: 0.6rem; }
.egq details.egq-q {
  margin: 0; background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 0;
  transition: border-color 0.2s ease;
}
.egq details.egq-q[open] { border-color: rgba(204, 43, 43, 0.6); background: var(--panel2); }
.egq details.egq-q summary {
  list-style: none; cursor: pointer; display: flex; align-items: center; justify-content: space-between; gap: 1rem;
  padding: 0.95rem 1.15rem; margin: 0; font-weight: 650; font-size: 1.02rem; color: #fff; border-radius: 14px;
}
.egq details.egq-q summary::-webkit-details-marker { display: none; }
.egq details.egq-q summary::after {
  content: ''; flex: none; width: 0.6rem; height: 0.6rem; margin-right: 0.2rem;
  border-right: 2px solid var(--red); border-bottom: 2px solid var(--red);
  transform: translateY(-3px) rotate(45deg); transition: transform 0.2s ease;
}
.egq details.egq-q[open] summary::after { transform: translateY(2px) rotate(-135deg); }
.egq details.egq-q summary:focus-visible { outline: 3px solid var(--red); outline-offset: 2px; }
.egq .egq-a { padding: 0 1.15rem 1.05rem; color: var(--mute); }
.egq .egq-a p { color: #d4d4d8; }
.egq .egq-a p + p { margin-top: 0.55rem; }
.egq .egq-a .egq-flag {
  margin-top: 0.7rem; padding: 0.6rem 0.85rem; border-left: 3px solid var(--red);
  background: var(--red-soft); border-radius: 0 10px 10px 0; color: #fff;
}
.egq .egq-foot { margin-top: 2.5rem; color: var(--mute); text-align: center; }
@media (prefers-reduced-motion: reduce) {
  .egq details.egq-q, .egq details.egq-q summary::after { transition: none; }
}
</style>

<div class="egq">
<section class="egq-hero">
<p class="egq-kicker">Zona info</p>
<h1>Intrebari si raspunsuri</h1>
<p class="egq-lede">Ce ne intreaba jucatorii cel mai des, inainte si dupa ce intra pe EliteGamers Imersiv Roleplay. Apasa pe o intrebare ca sa vezi raspunsul.</p>
<nav class="egq-jump" aria-label="Sectiuni">
<a href="#egq-start">Inainte sa intri</a>
<a href="#egq-joc">In joc</a>
<a href="#egq-comunitate">Staff si factiuni</a>
</nav>
</section>
<h2 id="egq-start">Inainte sa intri</h2>
<div class="egq-list">
<details class="egq-q">
<summary>Pe ce platforma ruleaza serverul?</summary>
<div class="egq-a">
<p>Pe <b>FiveM</b>. Il descarci de pe <a href="https://fivem.net" target="_blank" rel="noopener">fivem.net</a>, apoi urmezi pasii din <a href="/zona-info/cum-intru-pe-server">Cum intru pe server</a>.</p>
<p class="egq-flag">Ai nevoie de o copie <b>cumparata</b> a jocului GTA V.</p>
</div>
</details>
<details class="egq-q">
<summary>Ce este roleplay-ul?</summary>
<div class="egq-a">
<p>Joci un personaj intr-o lume virtuala si te porti cum s-ar purta el in viata reala. Scopul e o poveste realista, in care te implici cu adevarat.</p>
<p class="egq-flag">Nu il confunda cu RPG-ul. Roleplay-ul are reguli stricte, ca jocul sa ramana corect si realist. Citeste <a href="/zona-info/regulament">regulamentul</a>.</p>
</div>
</details>
<details class="egq-q">
<summary>Ce fel de roleplay se joaca aici?</summary>
<div class="egq-a">
<p>Serverul merge pe <b>Imersiv Roleplay</b>. Fiecare actiune trebuie sa fie realista si jucata cu toata seriozitatea.</p>
</div>
</details>
<details class="egq-q">
<summary>Trebuie sa dau un test ca sa intru?</summary>
<div class="egq-a">
<p><b>Nu</b>, oricine poate intra pe server.</p>
<p>Daca nu respecti <a href="/zona-info/regulament">regulamentul general</a>, primesti sanctiunea potrivita.</p>
</div>
</details>
</div>
<h2 id="egq-joc">In joc</h2>
<div class="egq-list">
<details class="egq-q">
<summary>Ce joburi am si cat castig din ele?</summary>
<div class="egq-a">
<p>Toate joburile, cu orele de joc de care ai nevoie si cum se lucreaza, sunt in sectiunea <b>Activitati legale (joburi)</b> din meniul wiki-ului.</p>
<p>De exemplu: <a href="/joburi/pescar">Pescar</a>.</p>
</div>
</details>
<details class="egq-q">
<summary>Pot schimba cum arata personajul?</summary>
<div class="egq-a">
<p>Fata si trasaturile le alegi la crearea personajului si <b>nu le mai poti schimba</b> dupa aceea. Singura exceptie e un <b>CK (Character Kill)</b>. Ai grija ce alegi la inceput.</p>
<p>Hainele le schimbi la magazinele de haine, iar parul si barba la frizerie.</p>
</div>
</details>
<details class="egq-q">
<summary>Cum fac o mafie sau o organizatie?</summary>
<div class="egq-a">
<p>Doar prin roleplay (IC), respectand regulile si structura serverului. Ce faci trebuie sa fie realist si justificat, iar staff-ul trebuie sa aprobe organizatia.</p>
</div>
</details>
<details class="egq-q">
<summary>Pot citi wiki-ul fara sa ies din joc?</summary>
<div class="egq-a">
<p>Da. Apasa <kbd>F6</kbd> si wiki-ul se deschide peste joc.</p>
</div>
</details>
</div>
<h2 id="egq-comunitate">Staff si factiuni</h2>
<div class="egq-list">
<details class="egq-q">
<summary>Cum aplic pentru staff?</summary>
<div class="egq-a">
<p>Aplicatiile pentru staff se anunta din cand in cand pe <a href="https://discord.gg/u8nnkDqZ2q" target="_blank" rel="noopener">Discord</a>.</p>
<p>Daca nu e nicio recrutare deschisa, inseamna ca nu sunt locuri libere acum.</p>
</div>
</details>
<details class="egq-q">
<summary>Cum intru intr-o factiune?</summary>
<div class="egq-a">
<p>Recrutarile pentru factiuni se anunta doar pe <a href="https://discord.gg/u8nnkDqZ2q" target="_blank" rel="noopener">Discord</a>.</p>
<p>Daca o factiune nu are recrutari deschise, nu cauta membri noi in acel moment.</p>
</div>
</details>
</div>
<p class="egq-foot">Nu ai gasit raspunsul? Intreaba pe <a href="https://discord.gg/u8nnkDqZ2q" target="_blank" rel="noopener">Discord</a>.</p>
</div>
