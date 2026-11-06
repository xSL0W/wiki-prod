---
outline: false
---

<style>
.dmv {
  --ink: #0b0b0d;
  --panel: #17171a;
  --panel2: #1f1f23;
  --line: #2f2f36;
  --text: #f4f4f5;
  --mute: #a1a1aa;
  --red: #ef4444;
  --red-deep: #b91c1c;
  --red-soft: rgba(239, 68, 68, 0.14);
  --green: #4ade80;
  --green-soft: rgba(74, 222, 128, 0.13);
  --amber: #fbbf24;
  max-width: 960px;
  margin: 0 auto;
  color: var(--text);
  font-family: Inter, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.dmv *, .dmv *::before, .dmv *::after { box-sizing: border-box; }
.dmv p, .dmv li { line-height: 1.6; color: var(--text); margin: 0; }
.dmv ul, .dmv ol { list-style: none; padding: 0; margin: 0; }
.dmv li + li { margin-top: 0; }
.dmv b { color: #fff; font-weight: 650; }
.dmv a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.dmv a:hover { color: #fecaca; }
.dmv a:focus-visible { outline: 3px solid var(--red); outline-offset: 3px; border-radius: 6px; }
.dmv kbd {
  font: inherit; font-size: 0.85em; font-weight: 700; color: #fff; background: var(--red-deep);
  border: 0; border-radius: 6px; padding: 0.05rem 0.45rem;
}
.dmv code { font-size: 0.86em; background: var(--panel2); color: #fff; border-radius: 6px; padding: 0.1rem 0.4rem; overflow-wrap: anywhere; }
/* ---------- hero ---------- */
.dmv .dmv-hero {
  position: relative; overflow: hidden; isolation: isolate;
  background: radial-gradient(90% 120% at 100% 0%, rgba(74, 222, 128, 0.1), transparent 55%),
              radial-gradient(110% 120% at 0% 100%, rgba(185, 28, 28, 0.3), var(--ink) 62%);
  border: 1px solid var(--line); border-radius: 22px;
  padding: clamp(1.15rem, 4vw, 2.4rem);
}
.dmv .dmv-kicker { font-size: 0.78rem; font-weight: 700; letter-spacing: 0.16em; text-transform: uppercase; color: var(--red); margin-bottom: 0.55rem; }
.dmv .dmv-hero h1 {
  margin: 0 0 0.75rem; border: 0; padding: 0;
  font-size: clamp(2rem, 6.4vw, 3.4rem); line-height: 1.04; font-weight: 800; letter-spacing: -0.03em; color: #fff;
}
.dmv .dmv-hero h1 span { color: var(--green); }
.dmv .dmv-lede { max-width: 60ch; color: var(--mute); font-size: 1.05rem; }
/* route drawing */
.dmv .dmv-route { display: block; width: 100%; height: auto; margin-top: 1.3rem; border-radius: 14px; background: #0e0e11; border: 1px solid var(--line); }
.dmv-route .grid line { stroke: #19191e; stroke-width: 1; }
.dmv-route .road { fill: none; stroke: #2a2a31; stroke-width: 16; stroke-linecap: round; stroke-linejoin: round; }
.dmv-route .lane { fill: none; stroke: #f4f4f5; stroke-width: 1.6; stroke-dasharray: 7 9; opacity: 0.5; animation: dmv-lane 1.4s linear infinite; }
.dmv-route .car { fill: none; stroke: var(--green); stroke-width: 9; stroke-linecap: round; stroke-dasharray: 16 984; stroke-dashoffset: 1000; animation: dmv-drive 14s linear infinite; }
.dmv-route .cp { fill: var(--red); }
.dmv-route .cp-ring { fill: none; stroke: var(--red); stroke-width: 2; opacity: 0; transform-box: fill-box; transform-origin: center; animation: dmv-ping 14s ease-out infinite; }
.dmv-route .cp-ring.r2 { animation-delay: 3.1s; }
.dmv-route .cp-ring.r3 { animation-delay: 6.3s; }
.dmv-route .cp-ring.r4 { animation-delay: 9.2s; }
.dmv-route .cp-ring.r5 { animation-delay: 13.4s; }
.dmv-route .sign { fill: #fff; stroke: var(--red); stroke-width: 4; }
.dmv-route .sign-t { fill: #111; font: 800 14px Inter, system-ui, sans-serif; text-anchor: middle; }
.dmv-route .zone { fill: var(--mute); font: 700 13px Inter, system-ui, sans-serif; letter-spacing: 0.12em; text-anchor: middle; }
.dmv-route .flag { fill: var(--green); font: 800 13px Inter, system-ui, sans-serif; letter-spacing: 0.1em; }
@keyframes dmv-lane { to { stroke-dashoffset: -32; } }
@keyframes dmv-drive { to { stroke-dashoffset: 0; } }
@keyframes dmv-ping { 0% { opacity: 0.9; transform: scale(0.6); } 12% { opacity: 0; transform: scale(2.4); } 100% { opacity: 0; transform: scale(2.4); } }
.dmv .dmv-stats { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 0.6rem; margin-top: 1.2rem; }
.dmv .dmv-stats li { background: rgba(23, 23, 26, 0.85); border: 1px solid var(--line); border-radius: 14px; padding: 0.7rem 0.9rem; }
.dmv .dmv-stats b { display: block; font-size: clamp(1.3rem, 4vw, 1.75rem); line-height: 1.1; font-weight: 800; color: #fff; font-variant-numeric: tabular-nums; }
.dmv .dmv-stats span { display: block; color: var(--mute); font-size: 0.82rem; line-height: 1.35; margin-top: 0.2rem; }
@media (max-width: 640px) { .dmv .dmv-stats { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
/* ---------- sections ---------- */
.dmv .dmv-h2 {
  display: flex; align-items: center; gap: 0.65rem;
  margin: 3rem 0 0.9rem; border: 0; padding: 0;
  font-size: 1.5rem; font-weight: 750; letter-spacing: -0.015em; line-height: 1.25; color: #fff;
}
.dmv .dmv-h2::before { content: ''; flex: none; width: 0.55rem; height: 1.3rem; border-radius: 3px; background: var(--red); }
.dmv .dmv-p { color: var(--mute); max-width: 70ch; }
.dmv .dmv-p + .dmv-p { margin-top: 0.6rem; }
/* where */
.dmv .dmv-where { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 240px), 1fr)); gap: 0.7rem; }
.dmv .dmv-where li { background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 0.85rem 1rem; }
.dmv .dmv-where b { display: block; font-size: 0.78rem; letter-spacing: 0.1em; text-transform: uppercase; color: var(--red); margin-bottom: 0.25rem; }
.dmv .dmv-where span { display: block; color: var(--text); }
/* photos */
.dmv .dmv-shots { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 300px), 1fr)); gap: 0.8rem; margin-top: 1.1rem; }
.dmv .dmv-shot { margin: 0; background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 0.5rem; }
.dmv .dmv-shot img { display: block; width: 100%; height: auto; border-radius: 11px; margin: 0; }
.dmv .dmv-shot figcaption { color: var(--mute); font-size: 0.88rem; padding: 0.55rem 0.35rem 0.15rem; }
.dmv .dmv-shot.small { max-width: 256px; margin: 1.1rem auto 0; }
/* steps */
.dmv .dmv-steps { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 220px), 1fr)); gap: 0.7rem; counter-reset: dmvstep; }
.dmv .dmv-steps li { position: relative; background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 1rem 1rem 1rem 3.3rem; counter-increment: dmvstep; }
.dmv .dmv-steps li::before {
  content: counter(dmvstep); position: absolute; left: 0.9rem; top: 0.95rem;
  width: 1.75rem; height: 1.75rem; border-radius: 50%; display: grid; place-items: center;
  background: var(--red-soft); color: var(--red); font-weight: 800; font-size: 0.92rem;
}
.dmv .dmv-steps b { display: block; margin-bottom: 0.15rem; }
.dmv .dmv-steps span { color: var(--mute); font-size: 0.95rem; }
/* exam panels */
.dmv .dmv-panel { background: var(--panel); border: 1px solid var(--line); border-radius: 18px; padding: clamp(1rem, 3vw, 1.4rem); }
.dmv .dmv-panel + .dmv-panel { margin-top: 0.9rem; }
.dmv .dmv-meter { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 0.5rem; margin-bottom: 1rem; }
.dmv .dmv-meter li { background: var(--panel2); border-radius: 12px; padding: 0.6rem 0.7rem; text-align: center; }
.dmv .dmv-meter b { display: block; font-size: 1.35rem; font-weight: 800; line-height: 1.15; font-variant-numeric: tabular-nums; }
.dmv .dmv-meter span { display: block; color: var(--mute); font-size: 0.78rem; line-height: 1.3; }
.dmv .dmv-meter .ok b { color: var(--green); }
.dmv .dmv-meter .bad b { color: var(--red); }
@media (max-width: 560px) { .dmv .dmv-meter { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
.dmv .dmv-list li { position: relative; padding-left: 1.2rem; color: var(--text); }
.dmv .dmv-list li + li { margin-top: 0.45rem; }
.dmv .dmv-list li::before { content: ''; position: absolute; left: 0; top: 0.62em; width: 0.45rem; height: 0.45rem; border-radius: 2px; background: var(--red); }
/* route legs */
.dmv .dmv-legs { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 0.5rem; margin-bottom: 1rem; }
.dmv .dmv-legs li { background: var(--panel2); border-radius: 12px; padding: 0.7rem; display: flex; align-items: center; gap: 0.6rem; }
.dmv .dmv-legs i {
  flex: none; width: 2.4rem; height: 2.4rem; border-radius: 50%; display: grid; place-items: center;
  background: #fff; border: 4px solid var(--red); color: #111; font-style: normal; font-weight: 800; font-size: 0.8rem;
}
.dmv .dmv-legs b { display: block; line-height: 1.2; }
.dmv .dmv-legs span { display: block; color: var(--mute); font-size: 0.8rem; line-height: 1.3; }
@media (max-width: 680px) { .dmv .dmv-legs { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
/* fail grid */
.dmv .dmv-fails { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 210px), 1fr)); gap: 0.7rem; }
.dmv .dmv-fails li { background: linear-gradient(160deg, rgba(239, 68, 68, 0.1), var(--panel) 60%); border: 1px solid var(--line); border-radius: 16px; padding: 0.95rem 1rem; }
.dmv .dmv-fails b { display: block; color: #fff; margin-bottom: 0.2rem; }
.dmv .dmv-fails span { color: var(--mute); font-size: 0.93rem; }
.dmv .dmv-fails em { font-style: normal; display: inline-block; font-size: 0.72rem; font-weight: 800; letter-spacing: 0.08em; text-transform: uppercase; color: var(--red); margin-bottom: 0.3rem; }
/* license card */
.dmv .dmv-licwrap { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1.1fr); gap: 1rem; align-items: center; }
@media (max-width: 720px) { .dmv .dmv-licwrap { grid-template-columns: minmax(0, 1fr); } }
.dmv .dmv-card {
  position: relative; overflow: hidden; border-radius: 16px; padding: 1rem 1.1rem;
  background: linear-gradient(135deg, #e8f5ec 0%, #cfe9d8 55%, #b9dcc6 100%); color: #14251b;
  box-shadow: 0 14px 34px rgba(0, 0, 0, 0.45); max-width: 380px; width: 100%;
}
.dmv .dmv-card::after { content: ''; position: absolute; right: -40px; top: -40px; width: 140px; height: 140px; border-radius: 50%; background: rgba(20, 83, 45, 0.1); }
.dmv .dmv-card .top { display: flex; justify-content: space-between; align-items: baseline; font-weight: 800; letter-spacing: 0.08em; font-size: 0.78rem; color: #14532d; }
.dmv .dmv-card .top span { font-size: 0.7rem; letter-spacing: 0.12em; }
.dmv .dmv-card .body { display: grid; grid-template-columns: 74px minmax(0, 1fr); gap: 0.85rem; margin-top: 0.8rem; }
.dmv .dmv-card .photo { height: 90px; border-radius: 8px; background: linear-gradient(180deg, #9cb8a6, #7d9b88); position: relative; }
.dmv .dmv-card .photo::before { content: ''; position: absolute; left: 50%; top: 16px; width: 30px; height: 30px; margin-left: -15px; border-radius: 50%; background: #5d7b68; }
.dmv .dmv-card .photo::after { content: ''; position: absolute; left: 50%; bottom: 0; width: 52px; height: 30px; margin-left: -26px; border-radius: 26px 26px 0 0; background: #5d7b68; }
.dmv .dmv-card dl { margin: 0; display: grid; grid-template-columns: auto minmax(0, 1fr); gap: 0.15rem 0.6rem; font-size: 0.82rem; }
.dmv .dmv-card dt { color: #3f6b50; font-weight: 600; }
.dmv .dmv-card dd { margin: 0; color: #0f1f15; font-weight: 750; }
.dmv .dmv-card .cat { display: inline-block; background: #14532d; color: #fff; border-radius: 6px; padding: 0 0.45rem; }
/* note */
.dmv .dmv-note { margin-top: 1rem; display: flex; gap: 0.7rem; align-items: flex-start; background: var(--green-soft); border: 1px solid rgba(74, 222, 128, 0.3); border-radius: 14px; padding: 0.8rem 1rem; }
.dmv .dmv-note svg { flex: none; width: 1.25rem; height: 1.25rem; margin-top: 0.15rem; color: var(--green); }
.dmv .dmv-note p { color: var(--text); }
.dmv .dmv-note.warn { background: var(--red-soft); border-color: rgba(239, 68, 68, 0.35); }
.dmv .dmv-note.warn svg { color: var(--red); }
@media (prefers-reduced-motion: reduce) {
  .dmv .dmv-route .lane, .dmv .dmv-route .car, .dmv .dmv-route .cp-ring { animation: none; }
  .dmv .dmv-route .car { stroke-dashoffset: 1000; opacity: 0; }
}
</style>

<div class="dmv">
<section class="dmv-hero">
<p class="dmv-kicker">Locatii · DRPCIV</p>
<h1>Scoala de <span>soferi</span></h1>
<p class="dmv-lede">Aici iti iei permisul de conducere. Dai o proba teoretica la calculator, apoi o proba practica pe un traseu prin oras, pe drum national si pe autostrada. Daca le treci pe amandoua, primesti permisul pe loc, in inventar.</p>
<svg class="dmv-route" viewBox="0 0 640 210" role="img" aria-label="Traseul probei practice: oras, drum national, autostrada si inapoi in oras, cu limitele de viteza">
<g class="grid"><line x1="0" y1="42" x2="640" y2="42"/><line x1="0" y1="84" x2="640" y2="84"/><line x1="0" y1="126" x2="640" y2="126"/><line x1="0" y1="168" x2="640" y2="168"/><line x1="80" y1="0" x2="80" y2="210"/><line x1="160" y1="0" x2="160" y2="210"/><line x1="240" y1="0" x2="240" y2="210"/><line x1="320" y1="0" x2="320" y2="210"/><line x1="400" y1="0" x2="400" y2="210"/><line x1="480" y1="0" x2="480" y2="210"/><line x1="560" y1="0" x2="560" y2="210"/></g>
<path class="road" d="M30 170 C80 170 100 128 150 128 S240 172 300 152 S380 70 440 70 S560 110 610 60"/>
<path class="lane" d="M30 170 C80 170 100 128 150 128 S240 172 300 152 S380 70 440 70 S560 110 610 60"/>
<path class="car" pathLength="1000" d="M30 170 C80 170 100 128 150 128 S240 172 300 152 S380 70 440 70 S560 110 610 60"/>
<circle class="cp" cx="30" cy="170" r="5"/><circle class="cp-ring" cx="30" cy="170" r="7"/>
<circle class="cp" cx="150" cy="128" r="5"/><circle class="cp-ring r2" cx="150" cy="128" r="7"/>
<circle class="cp" cx="300" cy="152" r="5"/><circle class="cp-ring r3" cx="300" cy="152" r="7"/>
<circle class="cp" cx="440" cy="70" r="5"/><circle class="cp-ring r4" cx="440" cy="70" r="7"/>
<circle class="cp" cx="610" cy="60" r="5"/><circle class="cp-ring r5" cx="610" cy="60" r="7"/>
<text class="flag" x="14" y="200">START</text>
<circle class="sign" cx="90" cy="60" r="20"/><text class="sign-t" x="90" y="65">100</text><text class="zone" x="90" y="100">ORAS</text>
<circle class="sign" cx="240" cy="60" r="20"/><text class="sign-t" x="240" y="65">100</text><text class="zone" x="240" y="100">NATIONAL</text>
<circle class="sign" cx="380" cy="170" r="20"/><text class="sign-t" x="380" y="175">200</text><text class="zone" x="380" y="128">AUTOSTRADA</text>
<circle class="sign" cx="540" cy="160" r="20"/><text class="sign-t" x="540" y="165">150</text><text class="zone" x="540" y="196">ORAS</text>
<text class="flag" x="560" y="36">ADMIS</text>
</svg>
<ul class="dmv-stats">
<li><b>2</b><span>probe: teorie si traseu</span></li>
<li><b>10</b><span>intrebari la teorie</span></li>
<li><b>33</b><span>puncte pe traseu</span></li>
<li><b>B</b><span>categoria de pe permis</span></li>
</ul>
</section>
<h2 class="dmv-h2">Unde o gasesti</h2>
<ul class="dmv-where">
<li><b>Pe telefon</b><span><code>Telefon → Harti → Locatii importante → Scoala de soferi</code></span></li>
<li><b>Pe harta</b><span>Blip verde cu masina, „Scoala de soferi”, langa codul postal 836.</span></li>
<li><b>Instructorul</b><span>Sta la receptie. Te apropii si apesi <kbd>E</kbd> ca sa vorbesti cu el.</span></li>
</ul>
<div class="dmv-shots">
<figure class="dmv-shot"><img src="../public/dmv/dmv.png" alt="Cladirea scolii de soferi, vazuta din parcare" loading="lazy"><figcaption>Cladirea scolii de soferi. Masina de examen pleaca din parcarea din fata.</figcaption></figure>
<figure class="dmv-shot"><img src="../public/dmv/dmv2.png" alt="Instructorul auto la receptia scolii de soferi" loading="lazy"><figcaption>Instructorul auto te asteapta la receptie.</figcaption></figure>
</div>
<h2 class="dmv-h2">Ce iti ofera instructorul</h2>
<p class="dmv-p">Cand vorbesti cu instructorul, ai trei optiuni. O optiune pe care nu o poti folosi apare blocata, cu motivul scris sub ea (de exemplu „Ai trecut deja proba teoretica”).</p>
<ol class="dmv-steps">
<li><b>Proba teoretica</b><span>Testul de la calculator. Se blocheaza dupa ce il treci.</span></li>
<li><b>Proba practica</b><span>Traseul cu masina scolii. Merge doar dupa ce ai trecut teoria.</span></li>
<li><b>Solicita duplicat permis</b><span>Un permis nou, daca l-ai pierdut sau ti-ai schimbat numele.</span></li>
</ol>
<figure class="dmv-shot small"><img src="../public/dmv/dmv3.png" alt="Optiunile instructorului auto: proba teoretica, proba practica, duplicat permis" loading="lazy"><figcaption>Cele trei optiuni ale instructorului.</figcaption></figure>
<p class="dmv-p" style="margin-top:1rem">Daca ai deja permis valid, nu mai poti da examenele. Instructorul iti spune „Ai deja permis de conducere”.</p>
<h2 class="dmv-h2">Proba teoretica</h2>
<div class="dmv-panel">
<ul class="dmv-meter">
<li><b>10</b><span>intrebari</span></li>
<li><b>20:00</b><span>minute pe ceas</span></li>
<li class="ok"><b>1</b><span>greseala permisa</span></li>
<li class="bad"><b>2</b><span>greseli = respins</span></li>
</ul>
<ul class="dmv-list">
<li>Alegi categoria <b>B, B1</b> si limba romana, apoi raspunzi la <b>3 intrebari de acomodare</b>. Ele nu se puncteaza.</li>
<li>Testul are <b>10 intrebari</b>, alese la intamplare din 19: indicatoare, prioritate, viteze legale, situatii din trafic. Unele au o poza.</li>
<li>Bifezi raspunsul si apesi <b>Trimite raspunsul</b>. Cu <b>Modifica raspunsul</b> stergi bifa, iar cu <b>Raspunde mai tarziu</b> muti intrebarea la coada.</li>
<li>La a doua greseala testul se opreste si esti <b>respins</b>. La fel daca expira cele 20 de minute sau daca apesi <kbd>ESC</kbd>.</li>
<li>Daca pici, poti incerca din nou imediat, de la instructor.</li>
</ul>
<div class="dmv-note"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg><p>Teoria trecuta ramane valabila. Daca pici traseul, dai din nou doar proba practica, nu si testul.</p></div>
</div>
<h2 class="dmv-h2">Proba practica</h2>
<div class="dmv-panel">
<p class="dmv-p">Pornesti proba de la instructor. Te urci la volanul unei <b>Primo</b> a scolii, cu motorul pornit si plinul facut. Langa tine sta examinatorul (un politist), iar in spate doi pasageri. Primii 20 de metri nu ai coliziuni, ca sa iesi usor din parcare.</p>
<ul class="dmv-legs" style="margin-top:1rem">
<li><i>100</i><div><b>Oras</b><span>12 puncte</span></div></li>
<li><i>100</i><div><b>National</b><span>10 puncte</span></div></li>
<li><i>200</i><div><b>Autostrada</b><span>5 puncte</span></div></li>
<li><i>150</i><div><b>Oras</b><span>6 puncte, la final 100</span></div></li>
</ul>
<ul class="dmv-list">
<li>Mergi din punct in punct. Urmatorul punct apare pe harta cu traseul marcat, iar pe drum vezi un stalp rosu de lumina.</li>
<li>Jos pe ecran vezi viteza maxima a portiunii si cate greseli ai. Cand se schimba limita, primesti o notificare.</li>
<li>Traseul are <b>33 de puncte</b>, cam 7 km, si se termina langa scoala.</li>
<li>Dupa ultimul punct esti <b>admis</b> si primesti permisul.</li>
</ul>
</div>
<h2 class="dmv-h2">Ce te pica la traseu</h2>
<ul class="dmv-fails">
<li><em>Greseala</em><b>Viteza peste limita</b><span>Daca mergi cu mai mult de 30 km/h peste limita, primesti o greseala. Viteza se verifica la cateva secunde, deci daca ramai prea rapid, greselile se aduna.</span></li>
<li><em>Picat</em><b>3 greseli</b><span>La a treia greseala ai picat traseul.</span></li>
<li><em>Picat pe loc</em><b>Masina avariata</b><span>O lovitura care strica motorul sau caroseria cu peste 10% te pica pe loc.</span></li>
<li><em>Anulat</em><b>Iesi din masina</b><span>Ai 60 de secunde sa revii in masina de examen. Altfel traseul se anuleaza. Se anuleaza si daca masina dispare.</span></li>
</ul>
<div class="dmv-note warn"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 9v4M12 17h.01"/><path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0Z"/></svg><p>Daca pici, pe harta apare drumul inapoi spre scoala. Duci masina acolo, la marcajul rosu, si poti incerca din nou. Daca altcineva tocmai a pornit un traseu, asteapti 15 secunde inainte sa pornesti tu.</p></div>
<h2 class="dmv-h2">Permisul</h2>
<div class="dmv-licwrap">
<div class="dmv-card" aria-label="Exemplu de permis de conducere">
<div class="top">PERMIS DE CONDUCERE<span>RO</span></div>
<div class="body">
<div class="photo"></div>
<dl><dt>Nume</dt><dd>Numele tau</dd><dt>Categorie</dt><dd><span class="cat">B</span></dd><dt>Puncte</dt><dd>0</dd><dt>Valabil</dt><dd>10 ani</dd></dl>
</div>
</div>
<ul class="dmv-list">
<li>Permisul intra direct in inventar, pe numele, data nasterii si CNP-ul tau.</li>
<li>Pornesti cu <b>0 puncte de penalizare</b>. Categoria scrisa pe el e <b>B</b>.</li>
<li>Pe document scrie data eliberarii si o valabilitate de <b>10 ani</b>.</li>
</ul>
</div>
<h2 class="dmv-h2">Duplicat de permis</h2>
<p class="dmv-p">Ceri duplicatul de la instructor, cu <b>Solicita duplicat permis</b>. Inainte sa platesti, vezi pretul si confirmi. Duplicatul pastreaza punctele de penalizare pe care le ai.</p>
<ul class="dmv-list" style="margin-top:0.8rem">
<li>Ai nevoie de un permis valid, adica sa fi trecut proba practica.</li>
<li>Nu poti cere duplicat cat timp permisul ti-e <b>suspendat</b> de politie. Instructorul iti spune cat mai ai.</li>
<li>Daca ai deja in inventar un permis pe numele actual, optiunea e blocata. Daca ti-ai schimbat numele, iei duplicat pe numele nou.</li>
<li>Daca ai permisul vechi la tine, el se actualizeaza pe loc. Altfel iti trebuie loc in inventar. Daca nu incape, primesti banii inapoi.</li>
</ul>
</div>
