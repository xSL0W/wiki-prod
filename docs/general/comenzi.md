---
outline: false
---

<style>
.cmd {
  --ink: #0b0b0d;
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
.cmd *, .cmd *::before, .cmd *::after { box-sizing: border-box; }
.cmd p, .cmd li { line-height: 1.55; color: var(--text); margin: 0; }
.cmd ul, .cmd ol { list-style: none; padding: 0; margin: 0; }
.cmd li + li { margin-top: 0; }
.cmd b { color: #fff; font-weight: 650; }
.cmd a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.cmd a:focus-visible { outline: 3px solid var(--red); outline-offset: 3px; border-radius: 6px; }
.cmd kbd {
  display: inline-block; min-width: 1.75em; text-align: center; white-space: nowrap;
  font: inherit; font-size: 0.8em; font-weight: 700; color: #fff; background: var(--red-deep);
  border-radius: 6px; padding: 0.1rem 0.45rem; box-shadow: inset 0 -2px 0 rgba(0, 0, 0, 0.35);
}
.cmd code {
  font: 600 0.86em/1.3 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace;
  color: #fecaca; background: var(--red-soft); border: 1px solid rgba(239, 68, 68, 0.28);
  border-radius: 6px; padding: 0.1rem 0.4rem; white-space: nowrap;
}
.cmd code i { font-style: normal; color: var(--mute); }
/* ---------- header ---------- */
.cmd .cmd-hero {
  position: relative; overflow: hidden;
  background: radial-gradient(110% 130% at 0% 100%, rgba(185, 28, 28, 0.26), var(--ink) 60%);
  border: 1px solid var(--line); border-radius: 22px;
  padding: clamp(1.15rem, 4vw, 2.2rem);
}
.cmd .cmd-kicker { font-size: 0.78rem; font-weight: 700; letter-spacing: 0.16em; text-transform: uppercase; color: var(--red); margin-bottom: 0.5rem; }
.cmd .cmd-hero h1 {
  margin: 0 0 0.6rem; border: 0; padding: 0;
  font-size: clamp(2rem, 6vw, 3rem); line-height: 1.05; font-weight: 800; letter-spacing: -0.03em; color: #fff;
}
.cmd .cmd-hero h1 span { color: var(--red); }
.cmd .cmd-lede { max-width: 62ch; color: var(--mute); font-size: 1.03rem; }
.cmd .cmd-prompt {
  display: flex; align-items: center; gap: 0.5rem; margin-top: 1.1rem; max-width: 30rem;
  background: #0d0d0f; border: 1px solid var(--line); border-radius: 12px; padding: 0.6rem 0.85rem;
  font: 600 0.92rem/1.3 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; color: #e4e4e7;
}
.cmd .cmd-prompt span { color: var(--red); }
.cmd .cmd-prompt i { width: 0.55rem; height: 1.05rem; background: var(--red); animation: cmd-caret 1.1s steps(1, end) infinite; }
@keyframes cmd-caret { 50% { opacity: 0; } }
@media (prefers-reduced-motion: reduce) { .cmd .cmd-prompt i { animation: none; } }
/* jump nav */
.cmd .cmd-nav { display: flex; flex-wrap: wrap; gap: 0.45rem; margin-top: 1.1rem; }
.cmd .cmd-nav a {
  display: inline-block; font-size: 0.84rem; font-weight: 650; color: var(--text); text-decoration: none;
  background: rgba(23, 23, 26, 0.9); border: 1px solid var(--line); border-radius: 999px; padding: 0.28rem 0.75rem;
}
.cmd .cmd-nav a:hover { border-color: var(--red); color: #fff; }
/* ---------- groups ---------- */
.cmd .cmd-h2 {
  display: flex; align-items: center; gap: 0.65rem; scroll-margin-top: 5rem;
  margin: 2.6rem 0 0.8rem; border: 0; padding: 0;
  font-size: 1.4rem; font-weight: 750; letter-spacing: -0.015em; line-height: 1.25; color: #fff;
}
.cmd .cmd-h2::before {
  content: ''; flex: none; width: 0.55rem; height: 0.55rem; border-radius: 2px; background: var(--red);
  transform: rotate(45deg); box-shadow: 0 0 0 4px var(--red-soft);
}
.cmd .cmd-sub { color: var(--mute); max-width: 66ch; margin: -0.3rem 0 0.9rem; font-size: 0.95rem; }
.cmd .cmd-label {
  margin: 1rem 0 0.5rem; font-size: 0.72rem; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: var(--mute);
}
.cmd .cmd-list {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 340px), 1fr));
  background: var(--panel); border: 1px solid var(--line); border-radius: 14px; overflow: hidden;
}
.cmd .cmd-list li {
  display: grid; grid-template-columns: 10rem minmax(0, 1fr); gap: 0.4rem 0.85rem; align-items: baseline;
  padding: 0.62rem 0.9rem; box-shadow: 0 1px 0 var(--line), 1px 0 0 var(--line);
}
.cmd .cmd-list .c { display: flex; flex-wrap: wrap; gap: 0.25rem; min-width: 0; }
.cmd .cmd-list .c code { max-width: 100%; white-space: normal; overflow-wrap: anywhere; }
.cmd .cmd-list .d { color: var(--mute); font-size: 0.92rem; }
@media (max-width: 420px) { .cmd .cmd-list li { grid-template-columns: minmax(0, 1fr); } }
/* clothing chips */
.cmd .cmd-chips { display: flex; flex-wrap: wrap; gap: 0.4rem; }
/* tips */
.cmd .cmd-tips { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr)); gap: 0.8rem; }
.cmd .cmd-card { background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 1rem 1.15rem; }
.cmd .cmd-h3 { margin: 0 0 0.4rem; border: 0; padding: 0; font-size: 1.02rem; font-weight: 700; color: #fff; line-height: 1.3; }
.cmd .cmd-card p { color: var(--mute); font-size: 0.94rem; }
.cmd .cmd-card p + p { margin-top: 0.5rem; }
.cmd .cmd-path {
  display: inline-block; margin-top: 0.4rem; font-size: 0.86rem; font-weight: 650; color: #fff;
  background: var(--panel2); border: 1px solid var(--line); border-radius: 8px; padding: 0.25rem 0.6rem;
}
.cmd .cmd-code {
  display: block; margin-top: 0.5rem; overflow-x: auto; white-space: pre;
  font: 600 0.88rem/1.4 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; color: #e4e4e7;
  background: #0d0d0f; border: 1px solid var(--line); border-radius: 10px; padding: 0.55rem 0.75rem;
}
</style>

<div class="cmd">
<header class="cmd-hero">
<div class="cmd-kicker">Sisteme generale</div>
<h1>Comenzi si <span>taste</span></h1>
<p class="cmd-lede">Comenzile le scrii in chat (<kbd>T</kbd>), cu <b>/</b> in fata. Tastele de mai jos sunt cele implicite: le poti schimba oricand din setarile jocului.</p>
<div class="cmd-prompt" aria-hidden="true"><span>/</span>e wait2<i></i></div>
<nav class="cmd-nav" aria-label="Sari la grupa">
<a href="#cmd-chat">Chat si staff</a>
<a href="#cmd-meniuri">Meniuri si inventar</a>
<a href="#cmd-personaj">Personaj si cont</a>
<a href="#cmd-animatii">Animatii</a>
<a href="#cmd-haine">Haine</a>
<a href="#cmd-vehicul">Vehicul</a>
<a href="#cmd-voce">Voce si statie</a>
<a href="#cmd-casa">Casa</a>
<a href="#cmd-activitati">Joburi si activitati</a>
<a href="#cmd-setari">HUD si setari</a>
<a href="#cmd-taste">Schimba tastele</a>
</nav>
</header>
<h2 class="cmd-h2" id="cmd-chat">Chat si staff</h2>
<ul class="cmd-list">
<li><span class="c"><code>/me <i>actiune</i></code></span><span class="d">Descrii ce face personajul. Mesajul il vad jucatorii din jur.</span></li>
<li><span class="c"><code>/g <i>mesaj</i></code><code>/global</code></span><span class="d">Scrii in chat-ul global.</span></li>
<li><span class="c"><code>/faction <i>mesaj</i></code></span><span class="d">Chat-ul politiei sau al medicilor, doar pentru ei.</span></li>
<li><span class="c"><code>/clear</code></span><span class="d">Iti golesti chat-ul.</span></li>
<li><span class="c"><code>/report</code><code>/ticket</code></span><span class="d">Deschizi un ticket catre staff: intrebari, buguri, reclamatii.</span></li>
<li><span class="c"><code>/cancelreport</code></span><span class="d">Anulezi ticketul tau, cat timp nu l-a preluat nimeni.</span></li>
</ul>
<h2 class="cmd-h2" id="cmd-meniuri">Meniuri si inventar</h2>
<ul class="cmd-list">
<li><span class="c"><kbd>K</kbd></span><span class="d">Meniul radial: jucator, vehicul, job, magazine.</span></li>
<li><span class="c"><kbd>G</kbd> tinut</span><span class="d">Interactionezi cu oameni, vehicule si obiecte.</span></li>
<li><span class="c"><kbd>TAB</kbd></span><span class="d">Inventarul.</span></li>
<li><span class="c"><kbd>I</kbd></span><span class="d">Torpedoul masinii sau portbagajul de langa tine.</span></li>
<li><span class="c"><kbd>J</kbd></span><span class="d">Arati bara rapida.</span></li>
<li><span class="c"><kbd>1</kbd> - <kbd>5</kbd></span><span class="d">Folosesti obiectul din slotul rapid.</span></li>
<li><span class="c"><kbd>R</kbd></span><span class="d">Incarci arma.</span></li>
<li><span class="c"><kbd>M</kbd></span><span class="d">Telefonul.</span></li>
<li><span class="c"><kbd>ESC</kbd></span><span class="d">Meniul de pauza: harta, setari HUD, magazin, wiki.</span></li>
<li><span class="c"><kbd>F6</kbd><code>/wikieg</code></span><span class="d">Deschizi wiki-ul direct in joc.</span></li>
<li><span class="c"><code>/browser</code></span><span class="d">Deschizi wiki-ul in browserul tau.</span></li>
<li><span class="c"><kbd>HOME</kbd></span><span class="d">Lista jucatorilor de pe server.</span></li>
<li><span class="c"><kbd>DELETE</kbd> tinut</span><span class="d">Vezi ID-urile jucatorilor din jur.</span></li>
<li><span class="c"><code>/store</code></span><span class="d">Magazinul EG (EG Coins).</span></li>
</ul>
<h2 class="cmd-h2" id="cmd-personaj">Personaj si cont</h2>
<ul class="cmd-list">
<li><span class="c"><code>/job</code></span><span class="d">Vezi jobul, gradul si daca esti in serviciu.</span></li>
<li><span class="c"><code>/factiune</code></span><span class="d">Vezi factiunea si gradul tau.</span></li>
<li><span class="c"><code>/ore</code></span><span class="d">Vezi cate ore ai jucat.</span></li>
<li><span class="c"><code>/vip</code></span><span class="d">Vezi ce VIP ai si cand expira.</span></li>
<li><span class="c"><code>/checkstats</code></span><span class="d">Vezi stamina, forta si bonusul de greutate in inventar.</span></li>
<li><span class="c"><code>/premii</code></span><span class="d">Recompensele zilnice pentru timpul jucat.</span></li>
<li><span class="c"><code>/happyhour</code></span><span class="d">Calendarul evenimentelor Happy Hour.</span></li>
<li><span class="c"><code>/referral</code><code>/ref</code></span><span class="d">Completezi cine te-a adus pe server si primesti recompensa.</span></li>
<li><span class="c"><code>/paytaxes</code></span><span class="d">Platesti taxele restante.</span></li>
<li><span class="c"><code>/firma <i>ID</i></code></span><span class="d">Vezi la ce firma lucreaza un jucator.</span></li>
<li><span class="c"><code>/teams</code></span><span class="d">Faci o echipa cu prietenii pentru activitati.</span></li>
<li><span class="c"><code>/topcombat</code></span><span class="d">Clasamentul de lupta: K/D, headshot-uri, precizie.</span></li>
<li><span class="c"><code>/showdamage</code></span><span class="d">Vezi in chat dauna si distanta fiecarei lovituri date.</span></li>
</ul>
<h2 class="cmd-h2" id="cmd-animatii">Animatii si miscare</h2>
<ul class="cmd-list">
<li><span class="c"><code>/e <i>nume</i></code></span><span class="d">Pornesti o animatie.</span></li>
<li><span class="c"><code>/e c</code></span><span class="d">Opresti animatia curenta.</span></li>
<li><span class="c"><code>/e l</code></span><span class="d">Lista tuturor animatiilor.</span></li>
<li><span class="c"><kbd>F4</kbd><code>/em</code></span><span class="d">Meniul de animatii si stiluri de mers.</span></li>
<li><span class="c"><kbd>F5</kbd></span><span class="d">Opresti animatia curenta.</span></li>
<li><span class="c"><code>/w <i>stil</i></code></span><span class="d">Schimbi stilul de mers.</span></li>
<li><span class="c"><code>/f <i>expresie</i></code></span><span class="d">Schimbi expresia fetei.</span></li>
<li><span class="c"><code>/k</code></span><span class="d">Te pui in genunchi cu mainile la ceafa.</span></li>
<li><span class="c"><kbd>X</kbd></span><span class="d">Ridici mainile.</span></li>
<li><span class="c"><kbd>B</kbd></span><span class="d">Arati cu degetul.</span></li>
<li><span class="c"><kbd>Ctrl</kbd></span><span class="d">Te ghemuiesti.</span></li>
<li><span class="c"><kbd>Z</kbd></span><span class="d">Te tarasti pe jos.</span></li>
<li><span class="c"><kbd>Shift</kbd> + <kbd>J</kbd></span><span class="d">Plonjezi din fuga.</span></li>
<li><span class="c"><kbd>Space</kbd><kbd>Backspace</kbd></span><span class="d">Te ridici de pe scaun.</span></li>
<li><span class="c"><code>/carry</code></span><span class="d">Iei un jucator pe umar (minim 35 de ore jucate). Inca o data il lasi jos.</span></li>
<li><span class="c"><code>/th</code><code>/takehostage</code></span><span class="d">Iei ostatic jucatorul cel mai apropiat. Ai nevoie de o arma cu munitie. <kbd>G</kbd> il eliberezi.</span></li>
<li><span class="c"><code>/stopsmoking</code></span><span class="d">Stingi tigara sau jointul.</span></li>
</ul>
<h2 class="cmd-h2" id="cmd-haine">Haine</h2>
<p class="cmd-sub">Fiecare comanda scoate piesa sau o pune la loc. Personajul face si animatia potrivita.</p>
<div class="cmd-chips">
<code>/palarie</code><code>/masca</code><code>/ochelari</code><code>/bandana</code><code>/vizor</code><code>/par</code><code>/ureche</code><code>/gat</code><code>/top</code><code>/tricou</code><code>/vesta</code><code>/manusi</code><code>/ceas</code><code>/bratara</code><code>/pantaloni</code><code>/pantofi</code><code>/rucsac</code><code>/geanta</code><code>/emblema</code>
</div>
<ul class="cmd-list" style="margin-top: 0.8rem">
<li><span class="c"><code>/reloadskin</code><code>/fixskin</code></span><span class="d">Reincarci hainele si fata cand apar gresit.</span></li>
</ul>
<h2 class="cmd-h2" id="cmd-vehicul">Vehicul</h2>
<ul class="cmd-list">
<li><span class="c"><kbd>L</kbd></span><span class="d">Incui sau descui vehiculul.</span></li>
<li><span class="c"><kbd>X</kbd></span><span class="d">Pornesti sau opresti motorul (ai nevoie de cheie).</span></li>
<li><span class="c"><kbd>O</kbd></span><span class="d">Meniul vehiculului: usi, geamuri, capota, portbagaj, computer de bord, muzica.</span></li>
<li><span class="c"><kbd>B</kbd></span><span class="d">Pui sau scoti centura.</span></li>
<li><span class="c"><kbd>Z</kbd></span><span class="d">Cruise control (doar soferul).</span></li>
<li><span class="c"><kbd>←</kbd><kbd>→</kbd></span><span class="d">Semnalizezi stanga / dreapta.</span></li>
<li><span class="c"><kbd>↓</kbd></span><span class="d">Avariile.</span></li>
<li><span class="c"><kbd>Alt</kbd> tinut</span><span class="d">Impingi o masina stricata (<kbd>A</kbd> <kbd>D</kbd> o vireaza).</span></li>
<li><span class="c"><code>/locatevehicles</code></span><span class="d">Vezi vehiculele tale scoase din garaj si pui un punct pe harta spre ele.</span></li>
<li><span class="c"><code>/towdestroyed<wbr>vehicles</code></span><span class="d">Tractezi in garaj vehiculele tale distruse, contra cost.</span></li>
<li><span class="c"><code>/ancora</code></span><span class="d">Arunci sau ridici ancora barcii (doar soferul).</span></li>
</ul>
<h2 class="cmd-h2" id="cmd-voce">Voce si statie</h2>
<ul class="cmd-list">
<li><span class="c"><kbd>`</kbd></span><span class="d">Schimbi cat de departe se aude vocea ta (tasta de sub <kbd>ESC</kbd>).</span></li>
<li><span class="c"><kbd>Alt</kbd> tinut</span><span class="d">Vorbesti pe statie.</span></li>
<li><span class="c"><kbd>=</kbd><code>/radio</code></span><span class="d">Deschizi statia (trebuie sa o ai in inventar).</span></li>
<li><span class="c"><kbd>.</kbd><kbd>,</kbd></span><span class="d">Treci pe canalul urmator / anterior.</span></li>
<li><span class="c"><code>/vol <i>1-100</i></code></span><span class="d">Volumul statiei si al apelurilor.</span></li>
</ul>
<h2 class="cmd-h2" id="cmd-casa">Casa</h2>
<ul class="cmd-list">
<li><span class="c"><code>/sleep</code></span><span class="d">Dormi in casa sau apartamentul tau (detinut sau inchiriat). Strangi ore jucate, nu primesti salariu si nu platesti taxe. Inca o data te trezesti.</span></li>
<li><span class="c"><code>/leavehouse</code></span><span class="d">Renunti la chiria casei in care esti. Nu primesti banii inapoi.</span></li>
</ul>
<h2 class="cmd-h2" id="cmd-activitati">Joburi si activitati</h2>
<p class="cmd-sub">Comenzile fiecarui job (politie, medici, mecanici) sunt pe pagina jobului.</p>
<ul class="cmd-list">
<li><span class="c"><kbd>F7</kbd><code>/apeluri</code></span><span class="d">Apelurile disponibile pentru servicii, in telefon.</span></li>
<li><span class="c"><code>/raport</code></span><span class="d">Raportul tau de activitate pe job sau factiune.</span></li>
<li><span class="c"><code>/leaveairsoft</code></span><span class="d">Iesi din lobby-ul sau meciul de airsoft.</span></li>
<li><span class="c"><kbd>F</kbd> tinut</span><span class="d">Clasamentul, in meciul de airsoft.</span></li>
<li><span class="c"><code>/tv</code></span><span class="d">Meniul televizorului la care te uiti.</span></li>
<li><span class="c"><code>/broadcast</code></span><span class="d">Pornesti sau opresti transmisia ta live la TV.</span></li>
</ul>
<h2 class="cmd-h2" id="cmd-setari">HUD si setari</h2>
<ul class="cmd-list">
<li><span class="c"><code>/hud</code></span><span class="d">Setarile HUD-ului.</span></li>
<li><span class="c"><code>/tinta</code><code>/crosshair</code></span><span class="d">Iti personalizezi tinta.</span></li>
<li><span class="c"><code>/keybinds</code></span><span class="d">Arati sau ascunzi tastele in meniul de pauza.</span></li>
<li><span class="c"><code>/fps</code></span><span class="d">Setari rapide pentru mai multe FPS.</span></li>
<li><span class="c"><code>/streamermode</code></span><span class="d">Opresti muzica din joc, pentru stream.</span></li>
<li><span class="c"><code>/disableleavetext</code></span><span class="d">Ascunzi sau arati mesajele cand iese cineva de pe server.</span></li>
<li><span class="c"><kbd>INSERT</kbd></span><span class="d">Deschizi sondajul activ.</span></li>
</ul>
<h2 class="cmd-h2" id="cmd-taste">Schimba tastele</h2>
<div class="cmd-tips">
<div class="cmd-card">
<h3 class="cmd-h3">Din setarile jocului</h3>
<p>Orice tasta de pe pagina asta se schimba din meniu. Alegi actiunea, apesi <kbd>Enter</kbd> si apoi tasta noua.</p>
<span class="cmd-path">ESC → Settings → Key Bindings → FiveM</span>
</div>
<div class="cmd-card">
<h3 class="cmd-h3">Din consola</h3>
<p>Deschide consola cu <kbd>F8</kbd> si leaga orice comanda de o tasta libera. Exemplu: animatia <b>wait2</b> pe <kbd>Num 1</kbd>.</p>
<code class="cmd-code">bind keyboard NUMPAD1 "e wait2"</code>
</div>
</div>
</div>
