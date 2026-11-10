---
outline: false
---

<style>
.vpn {
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
  --green: #4ade80;
  max-width: 960px;
  margin: 0 auto;
  color: var(--text);
  font-family: Inter, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.vpn *, .vpn *::before, .vpn *::after { box-sizing: border-box; }
.vpn p, .vpn li { margin: 0; line-height: 1.6; color: var(--text); }
.vpn ul, .vpn ol { list-style: none; padding: 0; margin: 0; }
.vpn li + li { margin-top: 0; }
.vpn b { color: #fff; font-weight: 650; }
.vpn a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.vpn a:hover { color: #fecaca; }
.vpn a:focus-visible { outline: 3px solid var(--red); outline-offset: 3px; border-radius: 8px; }
.vpn kbd { font: inherit; font-size: 0.85em; font-weight: 700; color: #fff; background: var(--blood); border-radius: 6px; padding: 0.05rem 0.45rem; }
/* ---------- hero ---------- */
.vpn .vpn-hero {
  position: relative; overflow: hidden; isolation: isolate;
  display: grid; grid-template-columns: minmax(0, 1fr); gap: 1.4rem; align-items: center;
  background: radial-gradient(90% 120% at 100% 0%, rgba(214, 165, 74, 0.08), transparent 55%), radial-gradient(120% 90% at 0% 120%, rgba(185, 28, 28, 0.3), transparent 60%), var(--ink);
  border: 1px solid var(--line); border-radius: 22px;
  padding: clamp(1.15rem, 4vw, 2.4rem);
}
.vpn .vpn-hero::after {
  content: ''; position: absolute; inset: 0; z-index: -1; pointer-events: none;
  background: repeating-linear-gradient(0deg, rgba(255, 255, 255, 0.018) 0 1px, transparent 1px 4px);
}
.vpn .vpn-kicker {
  display: inline-flex; align-items: center; gap: 0.5rem; margin-bottom: 0.7rem;
  font: 700 0.74rem/1.2 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace;
  letter-spacing: 0.18em; text-transform: uppercase; color: var(--red);
}
.vpn .vpn-kicker::before { content: ''; width: 8px; height: 8px; border-radius: 50%; background: var(--red); box-shadow: 0 0 0 4px var(--ember); animation: vpn-rec 1.6s steps(1, end) infinite; }
@keyframes vpn-rec { 0%, 60% { opacity: 1; } 61%, 100% { opacity: 0.25; } }
.vpn .vpn-hero h1 {
  margin: 0 0 0.8rem; padding: 0; border: 0; color: #fff;
  font-size: clamp(2.1rem, 7vw, 3.6rem); line-height: 1.02; font-weight: 850; letter-spacing: -0.035em;
}
.vpn .vpn-hero h1 span { color: var(--red); }
.vpn .vpn-lede { max-width: 56ch; color: var(--mute); font-size: 1.05rem; }
.vpn .vpn-chips { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1.1rem; }
.vpn .vpn-chips li {
  display: inline-flex; align-items: baseline; gap: 0.4rem;
  background: rgba(15, 15, 17, 0.9); border: 1px solid var(--line2); border-radius: 999px; padding: 0.3rem 0.8rem;
  font-size: 0.85rem; color: var(--mute);
}
.vpn .vpn-chips b { font-size: 1rem; font-variant-numeric: tabular-nums; }
/* in-game stand labels */
.vpn .vpn-board { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 13.5rem), 1fr)); gap: 0.55rem; }
.vpn .vpn-board li {
  display: grid; grid-template-columns: auto minmax(0, 1fr); align-items: center; gap: 0.7rem;
  background: rgba(15, 15, 17, 0.92); border: 1px solid var(--line2); border-radius: 14px; padding: 0.65rem 0.8rem;
}
.vpn .vpn-board .k { display: grid; place-items: center; width: 1.9rem; height: 1.9rem; border-radius: 8px; background: var(--blood); color: #fff; font: 800 0.85rem/1 Inter, system-ui, sans-serif; }
.vpn .vpn-board .t { font: 700 0.86rem/1.35 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; color: #fff; }
.vpn .vpn-board .s { display: block; font-family: Inter, system-ui, sans-serif; font-weight: 500; font-size: 0.78rem; color: var(--dim); }
.vpn .vpn-board li.free .t span { color: var(--green); }
.vpn .vpn-board li.full .t span { color: var(--brass); }
.vpn .vpn-board .t .n { white-space: nowrap; }
.vpn .vpn-board li.empty { opacity: 0.7; }
.vpn .vpn-board-cap { margin-top: 0.45rem; font-size: 0.78rem; color: var(--dim); }
@media (prefers-reduced-motion: reduce) { .vpn .vpn-kicker::before { animation: none; } }
/* ---------- sections ---------- */
.vpn .vpn-h2 {
  display: flex; align-items: baseline; gap: 0.7rem;
  margin: 3rem 0 0.6rem; padding: 0; border: 0;
  font-size: 1.5rem; line-height: 1.25; font-weight: 750; letter-spacing: -0.015em; color: #fff;
}
.vpn .vpn-h2 span { font: 700 0.8rem/1 ui-monospace, Menlo, Consolas, monospace; color: var(--red); letter-spacing: 0.1em; }
.vpn .vpn-sub { color: var(--mute); max-width: 68ch; margin-bottom: 1.1rem; }
.vpn .vpn-h3 { margin: 0 0 0.35rem; padding: 0; border: 0; font-size: 1.06rem; line-height: 1.3; font-weight: 700; color: #fff; }
.vpn .vpn-card { background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 1.1rem 1.2rem; }
.vpn .vpn-card > p { color: var(--mute); font-size: 0.95rem; }
.vpn .vpn-note { margin-top: 0.85rem; color: var(--mute); font-size: 0.92rem; }
/* facts about the place */
.vpn .vpn-facts { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 210px), 1fr)); gap: 0.75rem; }
.vpn .vpn-facts li { background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 1rem 1.1rem; }
.vpn .vpn-facts .ico { display: grid; place-items: center; width: 2.2rem; height: 2.2rem; margin-bottom: 0.6rem; border-radius: 11px; background: var(--wine); color: var(--red); border: 1px solid #5b1414; }
.vpn .vpn-facts .ico svg { width: 1.15rem; height: 1.15rem; }
.vpn .vpn-facts p { color: var(--mute); font-size: 0.93rem; line-height: 1.5; }
/* two lanes */
.vpn .vpn-lanes { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0.8rem; }
@media (max-width: 760px) { .vpn .vpn-lanes { grid-template-columns: minmax(0, 1fr); } }
.vpn .vpn-lane { border-radius: 18px; border: 1px solid var(--line); padding: 1.1rem clamp(0.9rem, 3vw, 1.25rem) 1.2rem; background: var(--panel); }
.vpn .vpn-lane.sell { background: linear-gradient(180deg, rgba(214, 165, 74, 0.08), var(--panel) 40%); border-color: #3d3217; }
.vpn .vpn-lane.buy { background: linear-gradient(180deg, rgba(239, 68, 68, 0.08), var(--panel) 40%); border-color: #4c1414; }
.vpn .vpn-lane .who { display: flex; align-items: center; gap: 0.55rem; margin-bottom: 0.9rem; }
.vpn .vpn-lane .who span { font: 700 0.7rem/1.2 ui-monospace, Menlo, Consolas, monospace; letter-spacing: 0.14em; text-transform: uppercase; }
.vpn .vpn-lane.sell .who span { color: var(--brass); }
.vpn .vpn-lane.buy .who span { color: var(--red); }
.vpn .vpn-lane .who b { font-size: 1.15rem; }
.vpn .vpn-steps { counter-reset: vpn-s; display: grid; gap: 0.55rem; }
.vpn .vpn-steps li { position: relative; counter-increment: vpn-s; padding: 0.7rem 0.85rem 0.7rem 2.75rem; background: rgba(6, 6, 7, 0.55); border: 1px solid var(--line); border-radius: 12px; color: var(--mute); font-size: 0.94rem; line-height: 1.5; }
.vpn .vpn-steps li::before { content: counter(vpn-s); position: absolute; left: 0.75rem; top: 0.72rem; width: 1.35rem; height: 1.35rem; border-radius: 50%; display: grid; place-items: center; font-size: 0.74rem; font-weight: 800; color: #111; }
.vpn .vpn-lane.sell .vpn-steps li::before { background: var(--brass); }
.vpn .vpn-lane.buy .vpn-steps li::before { background: var(--red); color: #fff; }
.vpn .vpn-anon { margin-top: 0.8rem; display: flex; gap: 0.7rem; align-items: flex-start; padding: 0.75rem 0.85rem; border-radius: 12px; border: 1px dashed #5b1414; background: #140707; }
.vpn .vpn-anon svg { flex: none; width: 1.3rem; height: 1.3rem; color: var(--red); margin-top: 0.1rem; }
.vpn .vpn-anon p { color: #fecaca; font-size: 0.92rem; line-height: 1.5; }
/* listing rules */
.vpn .vpn-rules { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr)); gap: 0; border: 1px solid var(--line); border-radius: 16px; overflow: hidden; background: var(--panel); }
.vpn .vpn-rules li { padding: 0.85rem 1.05rem; border-bottom: 1px solid var(--line); border-right: 1px solid var(--line); color: var(--mute); font-size: 0.93rem; line-height: 1.5; }
.vpn .vpn-rules li > b:first-child { display: block; font-size: 0.96rem; margin-bottom: 0.15rem; }
/* banned */
.vpn .vpn-ban { position: relative; border: 1px solid #4c1414; border-radius: 18px; padding: 1.15rem clamp(0.9rem, 3vw, 1.3rem) 1.2rem; background: repeating-linear-gradient(135deg, #0f0707 0 14px, #120808 14px 28px); }
.vpn .vpn-ban .stamp {
  display: inline-block; margin-bottom: 0.9rem; padding: 0.25rem 0.7rem; border: 2px solid var(--red); border-radius: 6px; transform: rotate(-2deg);
  font: 800 0.8rem/1.2 ui-monospace, Menlo, Consolas, monospace; letter-spacing: 0.2em; text-transform: uppercase; color: var(--red);
}
.vpn .vpn-ban ul { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 240px), 1fr)); gap: 0.5rem; }
.vpn .vpn-ban li { display: flex; gap: 0.6rem; align-items: flex-start; padding: 0.6rem 0.75rem; border-radius: 12px; background: rgba(6, 6, 7, 0.7); border: 1px solid var(--line); color: var(--mute); font-size: 0.92rem; line-height: 1.45; }
.vpn .vpn-ban li::before { content: ''; flex: none; width: 0.95rem; height: 0.95rem; margin-top: 0.18rem; border-radius: 50%; border: 2px solid var(--red); background: linear-gradient(135deg, transparent 44%, var(--red) 44% 56%, transparent 56%); }
.vpn .vpn-ban li b { color: #fff; }
/* closing cases */
.vpn .vpn-cases { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 210px), 1fr)); gap: 0.75rem; }
.vpn .vpn-cases li { background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 0.95rem 1.05rem; border-top: 3px solid var(--c, var(--blood)); }
.vpn .vpn-cases .k { display: block; font: 700 0.7rem/1.2 ui-monospace, Menlo, Consolas, monospace; letter-spacing: 0.12em; text-transform: uppercase; color: var(--dim); margin-bottom: 0.35rem; }
.vpn .vpn-cases .v { display: block; font-weight: 700; color: #fff; margin-bottom: 0.3rem; }
.vpn .vpn-cases p { color: var(--mute); font-size: 0.92rem; line-height: 1.5; }
/* npc */
.vpn .vpn-npc { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 0.8rem; align-items: stretch; }
@media (max-width: 760px) { .vpn .vpn-npc { grid-template-columns: minmax(0, 1fr); } }
.vpn .vpn-claim { background: #0b0b0d; border: 1px solid var(--line2); border-radius: 16px; padding: 0.8rem; }
.vpn .vpn-claim .hd { padding: 0.35rem 0.4rem 0.6rem; font: 700 0.72rem/1.2 ui-monospace, Menlo, Consolas, monospace; letter-spacing: 0.14em; text-transform: uppercase; color: var(--mute); }
.vpn .vpn-claim li { display: flex; justify-content: space-between; align-items: center; gap: 0.6rem; padding: 0.55rem 0.7rem; margin-top: 0.35rem; border-radius: 10px; background: var(--panel2); border: 1px solid var(--line); font-size: 0.9rem; color: var(--mute); }
.vpn .vpn-claim li b { font-size: 0.92rem; }
.vpn .vpn-claim li.all { justify-content: center; background: var(--blood); border-color: var(--blood); color: #fff; font-weight: 700; }
.vpn .vpn-claim .q { font: 700 0.8rem/1 ui-monospace, Menlo, Consolas, monospace; color: var(--brass); }
/* the rest of the underworld */
.vpn .vpn-more { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 210px), 1fr)); gap: 0.75rem; }
/* two-level subgrid: tag, title, text and link share row heights across a row of cards, so a 2-line title doesn't push its text lower */
.vpn .vpn-more li { display: grid; grid-row: span 4; grid-template-rows: subgrid; row-gap: 0; }
.vpn .vpn-more li > a, .vpn .vpn-more li > div { grid-row: 1 / -1; display: grid; grid-template-rows: subgrid; row-gap: 0.35rem; align-content: start; }
.vpn .vpn-more a, .vpn .vpn-more div {
  display: flex; flex-direction: column; gap: 0.35rem; width: 100%; padding: 1rem 1.1rem; border-radius: 16px; text-decoration: none; color: var(--text);
  background: linear-gradient(180deg, var(--panel2), var(--panel)); border: 1px solid var(--line); box-shadow: inset 0 1px 0 rgba(239, 68, 68, 0.16);
  transition: transform 0.2s ease, border-color 0.2s ease;
}
.vpn .vpn-more a:hover { transform: translateY(-3px); border-color: #7f1d1d; color: var(--text); }
.vpn .vpn-more .tag { font: 700 0.68rem/1.2 ui-monospace, Menlo, Consolas, monospace; letter-spacing: 0.14em; text-transform: uppercase; color: var(--red); }
.vpn .vpn-more .t { font-size: 1.05rem; font-weight: 750; color: #fff; }
.vpn .vpn-more .d { color: var(--mute); font-size: 0.92rem; line-height: 1.5; }
.vpn .vpn-more .go { margin-top: auto; padding-top: 0.2rem; font-size: 0.85rem; font-weight: 650; color: #fca5a5; }
@media (prefers-reduced-motion: reduce) { .vpn .vpn-more a { transition: none; } .vpn .vpn-more a:hover { transform: none; } }
.vpn .vpn-quote { margin-top: 2.6rem; padding: 1.2rem 1.3rem; border-radius: 16px; border: 1px solid #4c1414; background: linear-gradient(110deg, #1d0808, var(--panel) 70%); }
.vpn .vpn-quote p { color: #fecaca; font-size: 1.02rem; font-weight: 600; }
.vpn .vpn-quote ul { margin-top: 0.6rem; display: grid; gap: 0.4rem; }
.vpn .vpn-quote li { position: relative; padding-left: 1.2rem; color: var(--mute); font-size: 0.93rem; line-height: 1.5; }
.vpn .vpn-quote li::before { content: ''; position: absolute; left: 0; top: 0.55em; width: 7px; height: 7px; transform: rotate(45deg); background: var(--red); }
</style>

<div class="vpn">
<section class="vpn-hero">
<div>
<p class="vpn-kicker">Viata ilegala / Piata neagra</p>
<h1>Piata <span>Neagra</span></h1>
<p class="vpn-lede">Un loc retras si pazit, unde inchiriezi o taraba si iti vinzi marfa fara sa iti arati fata. Cumparatorul vede doar numarul tarabei. Totul se plateste in bani murdari.</p>
<ul class="vpn-chips">
<li><b>19</b> tarabe</li>
<li>vanzatori <b>anonimi</b></li>
<li>doar <b>bani murdari</b></li>
<li>zona <b>sigura</b></li>
</ul>
</div>
<div>
<ul class="vpn-board" aria-label="Asa arata eticheta de deasupra unei tarabe in joc">
<li class="free"><span class="k">E</span><span class="t">Stand #4 - <span>Liber</span><span class="s">Inchiriezi din meniul tarabei</span></span></li>
<li class="full"><span class="k">E</span><span class="t">Stand #7 - Inchiriat&nbsp;- <span class="n">Iteme: 6</span><span class="s">Deschizi lista si cumperi</span></span></li>
<li class="empty"><span class="k">E</span><span class="t">Stand #12 - Inchiriat&nbsp;- <span class="n">Niciun item listat</span></span></li>
</ul>
<p class="vpn-board-cap">Eticheta de deasupra fiecarei tarabe</p>
</div>
</section>
<h2 class="vpn-h2" id="locul"><span>01</span>Locul</h2>
<ul class="vpn-facts">
<li><span class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9.88 9.88a3 3 0 1 0 4.24 4.24"/><path d="M10.73 5.08A10.43 10.43 0 0 1 12 5c7 0 10 7 10 7a13.16 13.16 0 0 1-1.67 2.68"/><path d="M6.61 6.61A13.53 13.53 0 0 0 2 12s3 7 10 7a9.74 9.74 0 0 0 5.39-1.61"/><path d="m2 2 20 20"/></svg></span><h3 class="vpn-h3">Ascunsa</h3><p>Piata nu apare pe harta. Afli unde e prin contacte, in RP.</p></li>
<li><span class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></span><h3 class="vpn-h3">Zona sigura</h3><p>Inauntru nu se trage si nu ataci pe nimeni. Vii, faci afacerea si pleci.</p></li>
<li><span class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg></span><h3 class="vpn-h3">Paza inarmata</h3><p>Gardienii nu pot fi raniti. Cand se apropie un politist, deschid focul asupra lui.</p></li>
<li><span class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="m4.9 4.9 14.2 14.2"/></svg></span><h3 class="vpn-h3">Fara politie si medici</h3><p>Cu jobul de politist sau de medic nu poti inchiria, vinde, cumpara si nici ridica bani de la NPC.</p></li>
</ul>
<h2 class="vpn-h2" id="cum-functioneaza"><span>02</span>Vanzator sau cumparator</h2>
<p class="vpn-sub">La orice taraba te apropii si apesi <kbd>E</kbd>. Ce vezi depinde de cine esti: una libera o poti inchiria, pe a ta o gestionezi, iar la a altcuiva vezi marfa.</p>
<div class="vpn-lanes">
<div class="vpn-lane sell">
<div class="who"><span>Vanzator</span><b>Iti deschizi taraba</b></div>
<ol class="vpn-steps">
<li>Alegi o taraba <b>libera</b> si ii platesti chiria pe cate zile vrei. Chiria se plateste in avans, in <img class="eg-item" src="/items/dirtymoney.webp" alt="">bani murdari din inventar. Numarul maxim de zile apare in fereastra.</li>
<li>Din <b>Gestioneaza standul</b> pui iteme din inventar: alegi cantitatea si pretul pe bucata. Tot de aici retragi marfa sau schimbi pretul.</li>
<li>Prelungesti chiria oricand din <b>Prelungeste chiria</b>, cat timp zilele ramase nu trec de maxim.</li>
<li>Banii din vanzari nu ajung la tine in buzunar. Ii iei de la <b>NPC-ul de recuperare</b>, ca bani murdari.</li>
</ol>
</div>
<div class="vpn-lane buy">
<div class="who"><span>Cumparator</span><b>Faci cumparaturi</b></div>
<ol class="vpn-steps">
<li>Mergi la o taraba <b>inchiriata</b>. Eticheta iti arata cate iteme sunt puse la vanzare.</li>
<li>Vezi marfa si pretul pe bucata. La armele cu skin vezi si skin-ul. Pui in cos ce vrei.</li>
<li>Confirmi. Banii murdari ies din inventar, iar marfa intra la tine.</li>
<li>Ai nevoie de loc in inventar. Daca nu incape, cumpararea nu se face.</li>
</ol>
<div class="vpn-anon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg><p>Nu vezi niciodata cine vinde: nici nume, nici CNP, nici ID. Doar numarul tarabei si marfa.</p></div>
</div>
</div>
<h2 class="vpn-h2" id="reguli-de-listare"><span>03</span>Reguli de listare</h2>
<ul class="vpn-rules">
<li><b>Pret pe bucata</b>Fiecare item are un pret minim si unul maxim. In afara lor nu il poti pune la vanzare.</li>
<li><b>Arme si munitie</b>Au pret maxim separat pe bucata. Lista o gasesti la orice taraba, la <b>Preturi maxime arme</b>.</li>
<li><b>Acelasi item, acelasi pret</b>Se aduna intr-un singur rand pe taraba.</li>
<li><b>Arme cu serie sau skin</b>Fiecare sta pe randul ei, ca sa nu se piarda seria sau skin-ul.</li>
<li><b>Loc limitat</b>O taraba are un numar maxim de randuri. Meniul iti arata cate ai ocupat.</li>
<li><b>Nu cumperi de la tine</b>Nu poti cumpara de la propria taraba.</li>
</ul>
<h2 class="vpn-h2" id="ce-nu-se-vinde"><span>04</span>Ce nu intra pe taraba</h2>
<div class="vpn-ban">
<span class="stamp">Interzis</span>
<ul>
<li><span><b>Bani si monede:</b> bani murdari, bani curati, monedele de pe server.</span></li>
<li><span><b>Acte:</b> buletin, permis de conducere, documente.</span></li>
<li><span><b>Iteme din magazinul premium:</b> sistem audio, antilag, jante premium, ghiozdan premium.</span></li>
<li><span><b>Echipament medical:</b> NARCAN, defibrilator, truse si bandaje din farmacia ambulantei.</span></li>
<li><span><b>Iteme date de politie sau ambulanta:</b> filtrul le recunoaste dupa marcaj.</span></li>
<li><span><b>Pusca de vanatoare</b> si munitia ei.</span></li>
<li><span><b>Tableta Sentinel.</b></span></li>
</ul>
<p class="vpn-note">Filtrul e automat: daca pui ceva interzis, primesti un mesaj si itemul ramane la tine.</p>
</div>
<h2 class="vpn-h2" id="cand-se-inchide-taraba"><span>05</span>Cand se inchide taraba</h2>
<p class="vpn-sub">In orice caz, marfa ramasa nu se pierde: ajunge la NPC-ul de recuperare. Daca esti online, primesti un mesaj cand taraba ta se inchide singura.</p>
<ul class="vpn-cases">
<li style="--c: #d6a54a"><span class="k">Expira chiria</span><span class="v">Taraba devine libera</span><p>Ce era pe ea merge la NPC. Prelungeste la timp daca vrei sa o pastrezi.</p></li>
<li style="--c: #ef4444"><span class="k">O inchizi tu</span><span class="v">Chiria nu se intoarce</span><p>Banii platiti pe zilele ramase se pierd. Marfa merge la NPC.</p></li>
<li style="--c: #4ade80"><span class="k">Ai vandut tot</span><span class="v">Se inchide singura</span><p>Cand ultimul item se vinde, taraba se elibereaza si o poate lua altcineva.</p></li>
<li style="--c: #71717a"><span class="k">Personajul primeste CK</span><span class="v">Toate tarabele se inchid</span><p>Marfa si banii nerevendicati raman pe personajul care a primit CK.</p></li>
</ul>
<h2 class="vpn-h2" id="npc-ul-de-recuperare"><span>06</span>NPC-ul de recuperare</h2>
<div class="vpn-npc">
<div class="vpn-card">
<p>La marginea pietei sta un NPC. Te apropii, apesi <kbd>E</kbd> si vezi tot ce ai de ridicat:</p>
<ul class="vpn-rules" style="margin-top: 0.8rem">
<li><b>Banii din vanzari</b>Tot ce au platit cumparatorii pentru marfa ta, in bani murdari.</li>
<li><b>Marfa ramasa</b>Ce era pe taraba cand a expirat chiria sau cand ai inchis-o.</li>
</ul>
<p class="vpn-note">Iei cate un rand, alegand cantitatea, sau totul odata. Ce nu incape in inventar ramane la NPC pentru data viitoare.</p>
</div>
<div class="vpn-claim" aria-label="Exemplu de lista de revendicare">
<p class="hd">Iteme de revendicat</p>
<ul>
<li><b><img class="eg-item" src="/items/dirtymoney.webp" alt="">Bani murdari</b><span class="q">din vanzari</span></li>
<li><b><img class="eg-item" src="/items/WEAPON_PISTOL.webp" alt="">Pistol</b><span class="q">x1</span></li>
<li><b><img class="eg-item" src="/items/ammo-9.webp" alt="">Munitie 9mm</b><span class="q">x40</span></li>
<li class="all">Revendica tot</li>
</ul>
</div>
</div>
<h2 class="vpn-h2" id="restul-lumii-ilegale"><span>07</span>Unde mai circula marfa ilegala</h2>
<ul class="vpn-more">
<li><a href="/viata-ilegala/sistem-teritorial#cele-8-teritorii"><span class="tag">Spalatorie</span><span class="t">Spalarea banilor</span><span class="d">La port, la masa de spalat, schimbi bani murdari pe bani curati si pierzi un procent. Familia care tine teritoriul Spalatorie pierde mai putin.</span><span class="go">Vezi teritoriile</span></a></li>
<li><a href="/viata-ilegala/droguri-efecte#livrari"><span class="tag">Livrari</span><span class="t">Livrari de droguri</span><span class="d">Duci plicuri si pachete la clienti prin oras si primesti bani murdari.</span><span class="go">Vezi livrarile</span></a></li>
<li><a href="/joburi/jafuribijuterii"><span class="tag">Bijuterii</span><span class="t">Cumparatorul de bijuterii</span><span class="d">Bijuteriile furate le vinzi pe bani murdari. Unde sta, afli in joc.</span><span class="go">Vezi jaful</span></a></li>
<li><div><span class="tag">Piata legala</span><span class="t">Piata</span><span class="d">Pentru marfa curata exista Piata, marcata pe harta: aceleasi tarabe, dar platesti in euro, iar vanzatorul primeste banii direct in banca. Drogurile, armele si uneltele de furt nu au voie acolo.</span></div></li>
</ul>
<div class="vpn-quote">
<p>Piata neagra e un loc de RP, nu un automat de vanzari.</p>
<ul>
<li>Nu deschide focul, nu sechestra si nu provoca pe nimeni inauntru.</li>
<li>Daca afli pe alta cale decat RP cine vinde la o taraba, nu folosi informatia.</li>
<li>Gardienii fac parte din decor. Nu ii ataca.</li>
</ul>
</div>
</div>
