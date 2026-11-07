---
outline: deep
---

<style>
.vif {
  --ink: #060607;
  --panel: #0f0f11;
  --panel2: #151518;
  --line: #232327;
  --line2: #303036;
  --text: #f4f4f5;
  --mute: #a1a1aa;
  --dim: #71717a;
  --red: #ef4444;
  --blood: #b91c1c;
  --wine: #3b0a0a;
  --ember: rgba(239, 68, 68, 0.14);
  --brass: #d6a54a;
  max-width: 960px;
  margin: 0 auto;
  color: var(--text);
  font-family: Inter, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.vif *, .vif *::before, .vif *::after { box-sizing: border-box; }
.vif p, .vif li { margin: 0; line-height: 1.6; color: var(--text); }
.vif ul, .vif ol { list-style: none; padding: 0; margin: 0; }
.vif li + li { margin-top: 0; }
.vif b { color: #fff; font-weight: 650; }
.vif a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.vif a:hover { color: #fecaca; }
.vif a:focus-visible { outline: 3px solid var(--red); outline-offset: 3px; border-radius: 8px; }
.vif kbd {
  font: inherit; font-size: 0.85em; font-weight: 700; color: #fff; background: var(--blood);
  border-radius: 6px; padding: 0.05rem 0.45rem;
}
/* ---------- header ---------- */
.vif .vif-head {
  display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: 1.2rem; align-items: end;
  padding: clamp(1.1rem, 4vw, 2rem); border-radius: 20px; border: 1px solid var(--line);
  background: radial-gradient(90% 140% at 0% 0%, rgba(185, 28, 28, 0.22), transparent 60%), var(--ink);
}
.vif .vif-kicker {
  margin-bottom: 0.55rem; font: 700 0.74rem/1.2 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace;
  letter-spacing: 0.18em; text-transform: uppercase; color: var(--red);
}
.vif .vif-head h1 {
  margin: 0 0 0.6rem; padding: 0; border: 0; color: #fff;
  font-size: clamp(2rem, 6vw, 3rem); line-height: 1.05; font-weight: 850; letter-spacing: -0.03em;
}
.vif .vif-lede { color: var(--mute); max-width: 56ch; }
.vif .vif-rank { display: grid; gap: 0.35rem; min-width: 11rem; }
.vif .vif-rank li {
  display: flex; align-items: center; gap: 0.55rem; padding: 0.4rem 0.7rem; border-radius: 10px;
  border: 1px solid var(--line); color: var(--dim); font-size: 0.85rem; font-weight: 600;
}
.vif .vif-rank li::before { content: ''; width: 8px; height: 8px; border-radius: 50%; background: #3f3f46; }
.vif .vif-rank li.on { color: #fff; border-color: #7f1d1d; background: var(--wine); }
.vif .vif-rank li.on::before { background: var(--red); box-shadow: 0 0 0 4px var(--ember); }
@media (max-width: 640px) { .vif .vif-head { grid-template-columns: minmax(0, 1fr); } .vif .vif-rank { min-width: 0; } }
/* ---------- sections ---------- */
.vif .vif-h2 {
  display: flex; align-items: flex-start; gap: 0.65rem;
  margin: 2.8rem 0 0.6rem; padding: 0; border: 0;
  font-size: 1.45rem; line-height: 1.25; font-weight: 750; letter-spacing: -0.015em; color: #fff;
}
.vif .vif-h2::before { margin-top: calc(0.5lh - 1.2em / 2); content: ''; flex: none; width: 4px; height: 1.2em; border-radius: 2px; background: var(--red); }
.vif .vif-h3 { margin: 0 0 0.35rem; padding: 0; border: 0; font-size: 1.05rem; line-height: 1.3; font-weight: 700; color: #fff; }
.vif .vif-sub { color: var(--mute); max-width: 66ch; margin-bottom: 1rem; }
.vif .vif-card { background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 1.1rem 1.2rem; }
.vif .vif-card > p { color: var(--mute); font-size: 0.95rem; }
.vif .vif-card > p + p { margin-top: 0.5rem; }
/* road */
.vif .vif-road { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 200px), 1fr)); gap: 0.7rem; counter-reset: vif-step; }
.vif .vif-road li {
  position: relative; counter-increment: vif-step; padding: 2.7rem 1rem 1rem;
  background: var(--panel); border: 1px solid var(--line); border-radius: 16px;
}
.vif .vif-road li::before {
  content: counter(vif-step, decimal-leading-zero); position: absolute; top: 0.85rem; left: 1rem;
  font: 800 1rem/1 ui-monospace, Menlo, Consolas, monospace; color: var(--red);
}
.vif .vif-road li::after {
  content: ''; position: absolute; top: 1.3rem; left: 3rem; right: 1rem; height: 1px;
  background: linear-gradient(90deg, #7f1d1d, transparent);
}
.vif .vif-road p { color: var(--mute); font-size: 0.92rem; }
/* requirements */
.vif .vif-req { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0.8rem; }
@media (max-width: 720px) { .vif .vif-req { grid-template-columns: minmax(0, 1fr); } }
.vif .vif-tag {
  display: inline-block; margin-bottom: 0.5rem; font: 700 0.7rem/1.2 ui-monospace, Menlo, Consolas, monospace;
  letter-spacing: 0.14em; text-transform: uppercase; color: var(--red);
}
.vif .vif-tag.gold { color: var(--brass); }
.vif .vif-rows li { display: flex; justify-content: space-between; gap: 1rem; padding: 0.5rem 0; border-bottom: 1px dashed var(--line2); font-size: 0.93rem; }
.vif .vif-rows li:last-child { border-bottom: 0; }
.vif .vif-rows span { color: var(--mute); }
.vif .vif-rows b { text-align: right; font-variant-numeric: tabular-nums; }
.vif .vif-small { margin-top: 0.6rem; color: var(--dim); font-size: 0.86rem; line-height: 1.5; }
/* perks */
.vif .vif-perks { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 250px), 1fr)); gap: 0.75rem; }
.vif .vif-perks li { background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 1rem 1.1rem; }
.vif .vif-perks .ico {
  display: grid; place-items: center; width: 2.2rem; height: 2.2rem; margin-bottom: 0.65rem; border-radius: 10px;
  background: var(--wine); border: 1px solid #5b1414; color: var(--red);
}
.vif .vif-perks .ico svg { width: 1.15rem; height: 1.15rem; }
.vif .vif-perks p { color: var(--mute); font-size: 0.92rem; }
.vif .vif-guns { display: flex; flex-wrap: wrap; gap: 0.35rem; margin-top: 0.55rem; }
.vif .vif-guns li {
  padding: 0.15rem 0.55rem; border-radius: 999px; border: 1px solid var(--line2); background: var(--panel2);
  font-size: 0.8rem; font-weight: 600; color: var(--text);
}
/* hiring */
.vif .vif-hire { display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(0, 1fr); gap: 0.8rem; }
@media (max-width: 760px) { .vif .vif-hire { grid-template-columns: minmax(0, 1fr); } }
.vif .vif-check { display: grid; gap: 0.55rem; margin-top: 0.4rem; }
.vif .vif-check li { position: relative; padding-left: 1.7rem; color: var(--mute); font-size: 0.93rem; line-height: 1.5; }
.vif .vif-check li::before {
  content: ''; position: absolute; left: 0; top: 0.15rem; width: 1.1rem; height: 1.1rem; border-radius: 5px;
  border: 1.5px solid var(--red); background: var(--ember);
}
.vif .vif-check li::after {
  content: ''; position: absolute; left: 0.38rem; top: 0.33rem; width: 0.32rem; height: 0.58rem;
  border: solid var(--red); border-width: 0 2px 2px 0; transform: rotate(45deg);
}
.vif .vif-acts { display: grid; gap: 0.5rem; margin-top: 0.4rem; }
.vif .vif-acts li { padding: 0.6rem 0.75rem; border-radius: 12px; background: var(--panel2); border: 1px solid var(--line); font-size: 0.92rem; color: var(--mute); line-height: 1.5; }
.vif .vif-acts b { display: block; }
/* front business */
.vif .vif-front {
  display: grid; grid-template-columns: minmax(0, 1.2fr) minmax(0, 1fr); gap: 1rem;
  padding: 1.2rem 1.3rem; border-radius: 18px; border: 1px solid #3d3217;
  background: linear-gradient(150deg, rgba(214, 165, 74, 0.09), var(--panel) 55%);
}
@media (max-width: 760px) { .vif .vif-front { grid-template-columns: minmax(0, 1fr); } }
.vif .vif-front > div > p { color: var(--mute); font-size: 0.95rem; }
.vif .vif-front > div > p + p { margin-top: 0.5rem; }
.vif .vif-biz { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-top: 0.7rem; }
.vif .vif-biz li { padding: 0.2rem 0.6rem; border-radius: 8px; background: #141005; border: 1px solid #4a3a17; color: #f5deb3; font-size: 0.83rem; font-weight: 600; }
.vif .vif-dots { display: grid; gap: 0.45rem; }
.vif .vif-dots li { position: relative; padding-left: 1.1rem; color: var(--mute); font-size: 0.92rem; line-height: 1.5; }
.vif .vif-dots li::before { content: ''; position: absolute; left: 0; top: 0.6em; width: 6px; height: 6px; border-radius: 50%; background: var(--brass); }
/* next */
.vif .vif-next {
  display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 0.8rem;
  margin-top: 2.6rem; padding: 1.1rem 1.25rem; border-radius: 16px; border: 1px solid #4c1414;
  background: linear-gradient(110deg, #1d0808, var(--panel) 70%);
}
.vif .vif-next p { color: var(--mute); max-width: 52ch; }
.vif .vif-next a {
  flex: none; padding: 0.55rem 1rem; border-radius: 10px; background: var(--blood); color: #fff;
  font-weight: 700; text-decoration: none;
}
.vif .vif-next a:hover { background: #dc2626; color: #fff; }
</style>

<div class="vif">
<header class="vif-head">
<div>
<p class="vif-kicker">Viata ilegala / Stadiul I</p>
<h1>Familie IC</h1>
<p class="vif-lede">Primul pas in lumea interlopa. Aduni oameni de incredere, va faceti un nume in oras si demonstrati Sindicatului ca meritati mai mult.</p>
</div>
<ul class="vif-rank" aria-label="Stadiul familiei">
<li class="on">Familie IC</li>
<li>Mafie Neoficiala</li>
<li>Mafie Oficiala</li>
</ul>
</header>
<h2 class="vif-h2" id="drumul-familiei">Drumul familiei</h2>
<ol class="vif-road">
<li><h3 class="vif-h3">Nucleul</h3><p>Strange 3-4 oameni de incredere. Stabiliti numele, povestea familiei, ce va uneste si ce vreti sa obtineti.</p></li>
<li><h3 class="vif-h3">Infiintarea</h3><p>Cand ai minim 10 membri activi, Sindicatul creeaza familia, ii alege gradele si il numeste pe lider.</p></li>
<li><h3 class="vif-h3">Proba</h3><p>Activitate constanta, roleplay bun, disciplina. Mafiile Neoficiale te urmaresc si te pot recomanda.</p></li>
<li><h3 class="vif-h3">Avansarea</h3><p>Doar Sindicatul te poate urca la Mafie Neoficiala, pe baza recomandarilor si a unor taskuri speciale.</p></li>
</ol>
<h2 class="vif-h2" id="cerinte">Cerinte</h2>
<p class="vif-sub">Doua liste diferite: regulamentul spune ce trebuie sa ai ca sa existi, tableta arata cat de sanatoasa e familia.</p>
<div class="vif-req">
<div class="vif-card">
<span class="vif-tag">Regulament</span>
<ul class="vif-rows">
<li><span>Membri activi</span><b>10 - 25</b></li>
<li><span>Ore jucate ca sa intri in familie</span><b>150</b></li>
<li><span>Varsta minima a liderului</span><b>16 ani</b></li>
<li><span>Numele familiei</span><b>fictiv, nu se schimba</b></li>
</ul>
<p class="vif-small">Toate regulile, in <a href="/zona-info/regulament-mafii#_1-infiintare-si-statut">Regulamentul Mafiilor, sectiunea 1</a>.</p>
</div>
<div class="vif-card">
<span class="vif-tag gold">Clasament in Tableta Sentinel</span>
<ul class="vif-rows">
<li><span>Membri</span><b>minim 15</b></li>
<li><span>Puncte de reputatie</span><b>minim 7.500</b></li>
<li><span>Activitate</span><b>75% din membri</b></li>
</ul>
<p class="vif-small">Activitate = cel putin 75% din membri au peste 80 de ore jucate in familie in ultimele 30 de zile. Membrii intrati de mai putin de 30 de zile nu se numara. Fiecare cerinta apare verde (In regula), galben (In pericol) sau rosu (Critic).</p>
</div>
</div>
<h2 class="vif-h2" id="ce-primeste-familia">Ce primeste familia</h2>
<ul class="vif-perks">
<li><span class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="5" y="2" width="14" height="20" rx="2"/><path d="M12 18h.01"/></svg></span><h3 class="vif-h3">Tableta Sentinel</h3><p>Se deschide pentru orice membru. Vezi clasamentul, teritoriile, taxele, amenzile si obiectivele primite de la Sindicat.</p></li>
<li><span class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="12" cy="12" r="3"/><path d="M12 9V7"/><path d="M3 9h2"/><path d="M3 15h2"/></svg></span><h3 class="vif-h3">Seiful familiei</h3><p>Il pune Sindicatul, intr-un loc ales de el. Seful decide de la ce grad il pot deschide membrii. Ce tii in seif (arme, munitie, bani, droguri, obiecte rare) aduce puncte in clasament.</p></li>
<li><span class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M19 8v6"/><path d="M22 11h-6"/></svg></span><h3 class="vif-h3">Meniul sefului</h3><p>Un punct pus de Sindicat unde liderul apasa <kbd>E</kbd> si angajeaza, promoveaza sau da afara membri.</p></li>
<li><span class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></span><h3 class="vif-h3">Echipament</h3><p>Nea Marcel vinde doar familiilor: vesta anti-glont usoara si grea, catuse si punga de pus in cap. Locul il aflati IC.</p></li>
<li><span class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 8h13l3 3v2h-5l-1 2h-3l-1 4H5l1-6H3z"/></svg></span><h3 class="vif-h3">Arme de familie</h3><p>Armele de mai jos le pot tine in mana doar membrii familiilor. Altcuiva arma ii este scoasa din mana.</p><ul class="vif-guns"><li>Micro SMG</li><li>SMG</li><li>Assault Rifle</li><li>Compact Rifle</li><li>Marksman Pistol</li></ul></li>
<li><span class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg></span><h3 class="vif-h3">Atelierul de arme</h3><p>Familiile pot face arme, munitie si componente la un atelier dintr-o zona No Man's Land, deschis intre 18:00 si 02:00.</p></li>
</ul>
<p class="vif-small">Cu catuse sau punga in inventar, orice membru al unei familii poate folosi pe alt jucator optiunile <b>Pune catusele</b> si <b>Pune punga</b>.</p>
<h2 class="vif-h2" id="angajarea">Angajarea</h2>
<div class="vif-hire">
<div class="vif-card">
<h3 class="vif-h3">Inainte sa angajezi pe cineva</h3>
<ul class="vif-check">
<li>Sta langa tine, la cel mult 10 metri.</li>
<li>Are minim 150 de ore jucate.</li>
<li>Nu lucreaza la Politie. Trebuie sa-si dea demisia inainte.</li>
<li>Nu are pauza dupa plecarea din alta familie sau din Politie: 7 zile daca a stat acolo cel putin 30 de zile, altfel 14 zile.</li>
<li>Nu e pe lista neagra pentru mafii (o gestioneaza adminii).</li>
<li>Familia nu are deja 25 de membri.</li>
</ul>
</div>
<div class="vif-card">
<h3 class="vif-h3">Ce poate face seful</h3>
<ul class="vif-acts">
<li><b>Angajeaza</b>Noul membru intra pe primul grad. Sindicatul poate da si unui grad de recrutor dreptul sa angajeze.</li>
<li><b>Promoveaza si retrogradeaza</b>Doar membri cu grad mai mic decat al lui, si doar pana la un grad sub al lui.</li>
<li><b>Da afara</b>Doar membri cu grad mai mic. Cine pleaca intra in pauza de 7 sau 14 zile.</li>
<li><b>Seiful</b>Alege din Tableta Sentinel gradul minim care poate deschide seiful.</li>
</ul>
</div>
</div>
<h2 class="vif-h2" id="afacerea-paravan">Afacerea paravan</h2>
<div class="vif-front">
<div>
<span class="vif-tag gold">Privilegiu, nu drept</span>
<p>O Familie IC poate cumpara o afacere legala la <a href="/afaceri/elite-business-center">Elite Business Center</a>, dar doar cu o recomandare oficiala de la Mafia Neoficiala care tine teritoriul pe care activati.</p>
<p>Afacerea ramane legala in fata orasului. Prin ea va cunoasteti angajatii si alegeti pe cine aduceti in familie.</p>
<ul class="vif-biz">
<li>Service auto</li><li>Magazin 24/7</li><li>Magazin de haine</li><li>Magazin de arme</li><li>Frizerie</li><li>Salon de tatuaje</li><li>Club</li><li>Salon de infrumusetare</li>
</ul>
</div>
<div>
<h3 class="vif-h3">Ce datorezi mafiei sponsor</h3>
<ul class="vif-dots">
<li>Afacerea merge cinstit, ca orice firma.</li>
<li>Mafia sponsor afla ce faceti acolo.</li>
<li>Nu ajutati rivalii ei.</li>
<li>Recrutati discret, fara presiune.</li>
</ul>
<p class="vif-small">Tradarea, scandalurile mari sau sanctiunile grave pot duce la pierderea afacerii. Detalii in <a href="/zona-info/regulament-mafii#_6-afaceri-paravan">Regulamentul Mafiilor, sectiunea 6</a>.</p>
</div>
</div>
<div class="vif-next">
<p><b>Urmatorul pas:</b> intrati in atentia unei Mafii Neoficiale din zona voastra. Fara recomandarea ei, familia nu avanseaza.</p>
<a href="/viata-ilegala/mafie-neoficiala">Mafie Neoficiala &amp; Oficiala</a>
</div>
</div>
