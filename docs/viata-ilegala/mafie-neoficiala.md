---
outline: deep
---

<style>
.vim {
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
.vim *, .vim *::before, .vim *::after { box-sizing: border-box; }
.vim p, .vim li { margin: 0; line-height: 1.6; color: var(--text); }
.vim ul, .vim ol { list-style: none; padding: 0; margin: 0; }
.vim li + li { margin-top: 0; }
.vim b { color: #fff; font-weight: 650; }
.vim a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.vim a:hover { color: #fecaca; }
.vim a:focus-visible { outline: 3px solid var(--red); outline-offset: 3px; border-radius: 8px; }
/* ---------- header ---------- */
.vim .vim-head {
  position: relative; overflow: hidden; padding: clamp(1.1rem, 4vw, 2rem); border-radius: 20px; border: 1px solid var(--line);
  background: radial-gradient(80% 140% at 100% 0%, rgba(214, 165, 74, 0.12), transparent 55%),
              radial-gradient(90% 140% at 0% 100%, rgba(185, 28, 28, 0.25), transparent 60%), var(--ink);
}
.vim .vim-kicker {
  margin-bottom: 0.55rem; font: 700 0.74rem/1.2 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace;
  letter-spacing: 0.18em; text-transform: uppercase; color: var(--red); text-wrap: balance;
}
.vim .vim-head h1 {
  margin: 0 0 0.6rem; padding: 0; border: 0; color: #fff;
  font-size: clamp(1.9rem, 6vw, 3rem); line-height: 1.05; font-weight: 850; letter-spacing: -0.03em;
}
.vim .vim-head h1 span { color: var(--brass); }
.vim .vim-lede { color: var(--mute); max-width: 60ch; }
.vim .vim-jump { display: flex; flex-wrap: wrap; gap: 0.45rem; margin-top: 1rem; }
.vim .vim-jump a {
  padding: 0.3rem 0.75rem; border-radius: 999px; border: 1px solid var(--line2); background: rgba(15, 15, 17, 0.9);
  font-size: 0.85rem; font-weight: 600; text-decoration: none; color: var(--text);
}
.vim .vim-jump a:hover { border-color: #7f1d1d; color: #fff; }
/* ---------- sections ---------- */
.vim .vim-h2 {
  display: flex; align-items: flex-start; gap: 0.65rem;
  margin: 2.8rem 0 0.6rem; padding: 0; border: 0;
  font-size: 1.45rem; line-height: 1.25; font-weight: 750; letter-spacing: -0.015em; color: #fff;
}
.vim .vim-h2::before { margin-top: calc(0.5lh - 1.2em / 2); content: ''; flex: none; width: 4px; height: 1.2em; border-radius: 2px; background: var(--red); }
.vim .vim-h3 { margin: 0 0 0.35rem; padding: 0; border: 0; font-size: 1.05rem; line-height: 1.3; font-weight: 700; color: #fff; }
.vim .vim-sub { color: var(--mute); max-width: 66ch; margin-bottom: 1rem; }
.vim .vim-card { background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 1.1rem 1.2rem; }
.vim .vim-card > p { color: var(--mute); font-size: 0.95rem; }
.vim .vim-card > p + p { margin-top: 0.5rem; }
.vim .vim-small { margin-top: 0.7rem; color: var(--dim); font-size: 0.86rem; line-height: 1.5; }
/* compare matrix */
.vim .vim-matrix { border: 1px solid var(--line); border-radius: 16px; overflow: hidden; background: var(--panel); }
.vim .vim-matrix li {
  display: grid; grid-template-columns: minmax(0, 1.35fr) repeat(3, minmax(0, 1fr)); align-items: center; gap: 0.5rem;
  padding: 0.6rem 0.9rem; border-top: 1px solid var(--line); font-size: 0.9rem;
}
.vim .vim-matrix li:first-child { border-top: 0; background: var(--panel2); }
.vim .vim-matrix li:first-child span { font-size: 0.72rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; color: var(--mute); }
.vim .vim-matrix li:first-child span:nth-child(3) { color: #fca5a5; }
.vim .vim-matrix li:first-child span:nth-child(4) { color: var(--brass); }
.vim .vim-matrix li > span:first-child { color: var(--mute); }
.vim .vim-matrix li > span:not(:first-child) { text-align: center; font-weight: 650; color: #fff; font-variant-numeric: tabular-nums; }
.vim .vim-matrix .no { color: #52525b; font-weight: 500; }
.vim .vim-matrix .yes { color: #4ade80; }
@media (max-width: 520px) {
  .vim .vim-matrix li { padding: 0.55rem 0.6rem; font-size: 0.8rem; gap: 0.3rem; }
  .vim .vim-matrix li:first-child span { font-size: 0.7rem; letter-spacing: 0; text-transform: none; }
}
/* transition */
.vim .vim-steps { display: grid; gap: 0.6rem; counter-reset: vim-s; }
.vim .vim-steps li {
  position: relative; counter-increment: vim-s; padding: 0.85rem 1rem 0.85rem 3.2rem;
  background: var(--panel); border: 1px solid var(--line); border-radius: 14px; color: var(--mute); font-size: 0.94rem;
}
.vim .vim-steps li::before {
  content: counter(vim-s); position: absolute; left: 1rem; top: 0.85rem; width: 1.5rem; height: 1.5rem; border-radius: 50%;
  display: grid; place-items: center; font-size: 0.8rem; font-weight: 800; color: #fff; background: var(--blood);
}
/* roles */
.vim .vim-two { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0.8rem; }
@media (max-width: 720px) { .vim .vim-two { grid-template-columns: minmax(0, 1fr); } }
.vim .vim-card.neo { border-top: 3px solid var(--blood); }
.vim .vim-card.ofi { border-top: 3px solid var(--brass); background: linear-gradient(170deg, rgba(214, 165, 74, 0.08), var(--panel) 50%); }
.vim .vim-dots { display: grid; gap: 0.45rem; margin-top: 0.55rem; }
.vim .vim-dots li { position: relative; padding-left: 1.1rem; color: var(--mute); font-size: 0.93rem; line-height: 1.5; }
.vim .vim-dots li::before { content: ''; position: absolute; left: 0; top: 0.6em; width: 6px; height: 6px; border-radius: 50%; background: var(--red); }
.vim .ofi .vim-dots li::before { background: var(--brass); }
.vim .vim-guns { display: flex; flex-wrap: wrap; gap: 0.35rem; margin-top: 0.4rem; }
.vim .vim-guns li { padding: 0.15rem 0.55rem; border-radius: 999px; border: 1px solid var(--line2); background: var(--panel2); font-size: 0.8rem; font-weight: 600; }
/* points */
.vim .vim-points { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 210px), 1fr)); gap: 0.6rem; }
.vim .vim-points li { background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 0.8rem 0.95rem; }
.vim .vim-points b { display: block; margin-bottom: 0.15rem; }
.vim .vim-points span { color: var(--mute); font-size: 0.9rem; line-height: 1.45; display: block; }
.vim .vim-points .minus { border-color: #4c1414; }
.vim .vim-points .minus b { color: #fca5a5; }
.vim .vim-heist { margin-top: 0.8rem; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 150px), 1fr)); gap: 0.4rem; }
.vim .vim-heist li { display: flex; justify-content: space-between; gap: 0.6rem; padding: 0.45rem 0.7rem; border-radius: 10px; background: var(--panel2); border: 1px solid var(--line); font-size: 0.88rem; color: var(--mute); }
.vim .vim-heist b { font-variant-numeric: tabular-nums; }
/* boss tools */
.vim .vim-tools { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr)); gap: 0.7rem; }
.vim .vim-tools li { background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 1rem 1.1rem; }
.vim .vim-tools .who {
  display: inline-block; margin-bottom: 0.45rem; padding: 0.1rem 0.5rem; border-radius: 6px;
  font: 700 0.68rem/1.4 ui-monospace, Menlo, Consolas, monospace; letter-spacing: 0.1em; text-transform: uppercase;
  color: #fca5a5; background: var(--wine);
}
.vim .vim-tools .who.all { color: var(--mute); background: var(--panel2); }
.vim .vim-tools .who.sin { color: var(--brass); background: #141005; }
.vim .vim-tools p { color: var(--mute); font-size: 0.92rem; }
/* operation */
.vim .vim-op { border: 1px solid #4c1414; border-radius: 18px; overflow: hidden; background: var(--panel); }
.vim .vim-op-top {
  display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 0.6rem;
  padding: 0.85rem 1.2rem; background: repeating-linear-gradient(135deg, #1d0808 0 14px, #170606 14px 28px);
  border-bottom: 1px solid #4c1414;
}
.vim .vim-op-top strong { font: 800 0.8rem/1.2 ui-monospace, Menlo, Consolas, monospace; letter-spacing: 0.16em; text-transform: uppercase; color: #fca5a5; }
.vim .vim-op-top span { font-size: 0.85rem; color: var(--mute); }
/* flex, not grid: the last row stretches, so no empty bordered cell is left */
.vim .vim-facts { display: flex; flex-wrap: wrap; border-bottom: 1px solid var(--line); }
.vim .vim-facts li { flex: 1 1 150px; min-width: 0; padding: 0.8rem 1rem; box-shadow: inset -1px 0 0 var(--line), inset 0 -1px 0 var(--line); }
.vim .vim-facts b { display: block; font-size: 1.15rem; font-variant-numeric: tabular-nums; }
.vim .vim-facts span { color: var(--mute); font-size: 0.85rem; line-height: 1.4; display: block; }
.vim .vim-phases { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 0.8rem; padding: 1rem 1.2rem 1.2rem; }
@media (max-width: 760px) { .vim .vim-phases { grid-template-columns: minmax(0, 1fr); } }
.vim .vim-phases .vim-dots li::before { background: var(--red); }
.vim .vim-code {
  margin-top: 0.8rem; padding: 1rem 1.2rem; border-radius: 16px; border: 1px solid #7f1d1d;
  background: linear-gradient(110deg, #2a0909, var(--panel) 75%);
}
.vim .vim-code p { color: var(--mute); font-size: 0.94rem; }
.vim .vim-code p + p { margin-top: 0.45rem; }
.vim .vim-code .vim-h3 { color: #fca5a5; }
</style>

<div class="vim">
<header class="vim-head">
<p class="vim-kicker">Viata ilegala / Stadiile II si III</p>
<h1>Mafie Neoficiala <span>&amp;</span> Oficiala</h1>
<p class="vim-lede">Dupa Familie IC vin cele doua stadii mari. Mai multi oameni, seif mai mare, arme mai grele si mai multa raspundere fata de Sindicat.</p>
<nav class="vim-jump" aria-label="Pe aceasta pagina">
<a href="#ce-se-schimba">Ce se schimba</a>
<a href="#avansarea">Avansarea</a>
<a href="#clasamentul">Clasamentul</a>
<a href="#uneltele-sefului">Uneltele sefului</a>
<a href="#rapirea">Rapirea</a>
</nav>
</header>
<h2 class="vim-h2" id="ce-se-schimba">Ce se schimba de la un stadiu la altul</h2>
<ul class="vim-matrix">
<li><span>Stadiu</span><span>Familie IC</span><span>Neoficiala</span><span>Oficiala</span></li>
<li><span>Membri (regulament)</span><span>10 - 25</span><span>15 - 35</span><span>20 - 45</span></li>
<li><span>Ore jucate ca sa intri</span><span>150</span><span>250</span><span>500</span></li>
<li><span>Clasament: membri</span><span>15</span><span>25</span><span>30</span></li>
<li><span>Clasament: puncte</span><span>7.500</span><span>15.000</span><span>30.000</span></li>
<li><span>Clasament: teritorii</span><span class="no">-</span><span>2</span><span>3</span></li>
<li><span>Marimea seifului</span><span>x1</span><span>x2</span><span>x3</span></li>
<li><span>Atelier de arme No Man's Land</span><span class="yes">da</span><span class="yes">da</span><span class="yes">da</span></li>
<li><span>Ateliere de arme pe Cayo Perico</span><span class="no">nu</span><span class="yes">da</span><span class="yes">da</span></li>
<li><span>Arme in plus</span><span class="no">-</span><span class="yes">da</span><span class="yes">da</span></li>
<li><span>Raspundere colectiva</span><span class="no">nu</span><span class="yes">da</span><span class="yes">da</span></li>
</ul>
<p class="vim-small">Echipamentul de la Nea Marcel, catusele, punga si armele de familie le ai deja de la Familie IC (vezi <a href="/viata-ilegala/familie-ic#ce-primeste-familia">Familie IC</a>). Raspundere colectiva = mafia raspunde impreuna, prin amenzi, pentru abaterile membrilor.</p>
<h2 class="vim-h2" id="avansarea">Avansarea</h2>
<p class="vim-sub">Nu treci automat in stadiul urmator, oricate puncte ai. Decide Sindicatul.</p>
<ol class="vim-steps">
<li><b>Recomandarea.</b> Mafiile Neoficiale existente urmaresc Familiile IC si le recomanda pe cele care merita.</li>
<li><b>Misiunile speciale.</b> Sindicatul va da obiective. Le vedeti in Tableta Sentinel, cu termenul lor.</li>
<li><b>Casa liderului.</b> Pentru Mafie Neoficiala, liderul trebuie sa detina o casa mare platita cu EG Coins.</li>
<li><b>Taxa de infiintare.</b> O stabileste Sindicatul. Se plateste in bani curati, inainte de ceremonia de investire.</li>
<li><b>Ceremonia.</b> Sindicatul schimba stadiul familiei. Limita de membri creste pe loc, iar seiful se mareste.</li>
</ol>
<p class="vim-small">Daca liderul pleaca, mafia nu se inchide. Un succesor preia conducerea doar cu aprobarea Sindicatului. Detalii in <a href="/zona-info/regulament-mafii#_1-infiintare-si-statut">Regulamentul Mafiilor, sectiunea 1</a>.</p>
<h2 class="vim-h2" id="rolul-in-oras">Rolul in oras</h2>
<div class="vim-two">
<div class="vim-card neo">
<h3 class="vim-h3">Mafie Neoficiala</h3>
<ul class="vim-dots">
<li>Urmareste Familiile IC din zona ei si le recomanda Sindicatului.</li>
<li>Poate da unei Familii IC recomandarea pentru o afacere paravan pe teritoriul ei.</li>
<li>Ca orice familie cu teritorii, le pazeste, apara oamenii care livreaza si strange taxele: 20:00 - 02:00 in Los Santos, 18:00 - 00:00 pe Cayo Perico.</li>
<li>Intra in atelierele de arme, componente si atasamente de pe Cayo Perico.</li>
<li>Poate tine in mana si aceste arme:</li>
</ul>
<ul class="vim-guns"><li><img class="eg-item" src="/items/WEAPON_BULLPUPRIFLE.webp" alt="">Bullpup Rifle</li><li><img class="eg-item" src="/items/WEAPON_TACTICALRIFLE.webp" alt="">Tactical Rifle</li><li><img class="eg-item" src="/items/WEAPON_NAVYREVOLVER.webp" alt="">Navy Revolver</li></ul>
</div>
<div class="vim-card ofi">
<h3 class="vim-h3">Mafie Oficiala</h3>
<ul class="vim-dots">
<li>Varful scarii: pana la 45 de membri.</li>
<li>Cel mai mare seif, de trei ori cat al unei Familii IC.</li>
<li>Pastreaza tot ce are o Mafie Neoficiala: ateliere, arme, rolul pe teritorii.</li>
<li>Ca sa ramana "In regula" in clasament are nevoie de 30 de membri, 30.000 de puncte si 3 teritorii.</li>
</ul>
</div>
</div>
<h2 class="vim-h2" id="clasamentul">Clasamentul Sindicatului</h2>
<p class="vim-sub">Tableta Sentinel calculeaza un scor pentru fiecare familie. Scorul si cerintele stadiului apar in pagina Clasament.</p>
<ul class="vim-points">
<li><b>Seiful</b><span>Armele, munitia, banii, drogurile, obiectele din jafuri si obiectele rare din seif.</span></li>
<li><b>Membrii</b><span>25 de puncte pentru fiecare membru.</span></li>
<li><b>Teritoriile</b><span>Fiecare teritoriu tinut aduce punctele lui. Vezi <a href="/viata-ilegala/sistem-teritorial">Teritorii &amp; Razboaie</a>.</span></li>
<li><b>Jafurile duse pana la capat</b><span>Conteaza 30 de zile, daca cel putin 60% din cei care au participat sunt din familia ta.</span></li>
<li><b>Sindicatul</b><span>Poate da sau lua puncte. Ajustarea conteaza 30 de zile.</span></li>
<li class="minus"><b>Cazierele</b><span>Fiecare cazier primit de un membru scade 15 puncte.</span></li>
</ul>
<ul class="vim-heist" aria-label="Puncte pe jaf">
<li><span>ATM</span><b>2</b></li><li><span>Magazin</span><b>5</b></li><li><span>Masina</span><b>5</b></li><li><span>Misiune</span><b>3</b></li><li><span>Misiune grea</span><b>5</b></li><li><span>Casa</span><b>15</b></li><li><span>Casa de lux</span><b>25</b></li><li><span>Bijuterii</span><b>75</b></li><li><span>Banca</span><b>300</b></li>
</ul>
<p class="vim-small">Activitatea: cel putin 75% din membri trebuie sa aiba peste 80 de ore jucate in familie in ultimele 30 de zile. Cei intrati de mai putin de 30 de zile nu se numara.</p>
<h2 class="vim-h2" id="uneltele-sefului">Uneltele sefului in Tableta Sentinel</h2>
<ul class="vim-tools">
<li><span class="who">Sef</span><h3 class="vim-h3">Razboaie</h3><p>Declara razboi pentru un teritoriu si, cand familia e atacata, alege ziua si ora bataliei. Totul in <a href="/viata-ilegala/sistem-teritorial">Teritorii &amp; Razboaie</a>.</p></li>
<li><span class="who">Sef</span><h3 class="vim-h3">Rezervari</h3><p>Rezerva un interval in calendarul pus la dispozitie de Sindicat, cu cel mult 3 zile inainte. O singura rezervare activa pe fiecare tip.</p></li>
<li><span class="who">Sef</span><h3 class="vim-h3">Informatii</h3><p>Cumpara ponturi pe bani murdari: transporturi de armament, transporturi de persoane, airdrop-uri. Un pont de armament il pot cumpara cel mult doua familii.</p></li>
<li><span class="who">Sef</span><h3 class="vim-h3">Seiful</h3><p>Alege gradul minim de la care membrii pot deschide seiful familiei.</p></li>
<li><span class="who all">Orice membru</span><h3 class="vim-h3">Taxe</h3><p>Trece in registru taxa de protectie platita de cineva pe un teritoriu al familiei.</p></li>
<li><span class="who sin">De la Sindicat</span><h3 class="vim-h3">Amenzi, obiective, avertismente</h3><p>Amenzile vin cu termen de plata, obiectivele cu termen de indeplinire. Avertismentele expira dupa 30 de zile. Sindicatul le da intregi sau pe jumatate, iar familia poate avea cel mult 3 active.</p></li>
</ul>
<h2 class="vim-h2" id="rapirea">Rapirea membrilor de rang inalt</h2>
<p class="vim-sub">Una dintre cele mai riscante operatiuni din oras. Tensiune, negocieri si urmari serioase pentru ambele tabere.</p>
<div class="vim-op">
<div class="vim-op-top"><strong>Operatiune: capturarea protejatului</strong><span>Regulament, sectiunea 5</span></div>
<ul class="vim-facts">
<li><b>Tinte</b><span>Membrii Sindicatului si liderii mafiilor Neoficiale si Oficiale</span></li>
<li><b>20:00 - 24:00</b><span>Singurul interval permis</span></li>
<li><b>8 - 16</b><span>Minim 8 din aceeasi familie, maxim 16 in total</span></li>
<li><b>1 ora</b><span>Cat trebuie tinuta tinta fara sa fie eliberata</span></li>
<li><b>GoPro</b><span>Toata operatiunea filmata</span></li>
</ul>
<div class="vim-phases">
<div><h3 class="vim-h3">Pregatirea</h3><ul class="vim-dots"><li>Planificati totul, fara improvizatii.</li><li>Alegeti un loc sigur, dar accesibil. Locurile inaccesibile si exploit-urile sunt interzise.</li><li>Stabiliti echipa in limita de participanti.</li></ul></div>
<div><h3 class="vim-h3">Executia</h3><ul class="vim-dots"><li>Prindeti tinta printr-un roleplay bine pus la punct.</li><li>Duceti-o la locul stabilit.</li><li>Din acel moment incepe ora. Daca tinta e eliberata, operatiunea a esuat.</li></ul></div>
<div><h3 class="vim-h3">Negocierea</h3><ul class="vim-dots"><li>Pentru un lider, negociati cu familia lui. Pe langa bani se pot cere si alte avantaje.</li><li>Pentru un membru al Sindicatului, negociati direct cu Sindicatul. Suma depinde de rangul lui.</li><li>Membrii Sindicatului raman intangibili si cand sunt rapiti.</li></ul></div>
</div>
</div>
<div class="vim-code">
<h3 class="vim-h3">Codul Rosu</h3>
<p>Cand un membru de rang inalt este rapit, toti membrii disponibili trebuie sa raspunda. Sindicatul poate da Cod Rosu: alerta apare pe harta tuturor membrilor familiilor, cu locul de unde a fost trimisa.</p>
<p>Rascumpararea unui membru al Sindicatului o platesc cei care nu l-au recuperat si cei care nu au raspuns la Codul Rosu. Refuzul de plata aduce consecinte diplomatice grave.</p>
</div>
<p class="vim-small">Regulile complete: <a href="/zona-info/regulament-mafii#_5-rapirea-membrilor-de-rang-inalt">Regulamentul Mafiilor, sectiunea 5</a>.</p>
</div>
