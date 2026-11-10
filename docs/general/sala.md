---
outline: false
---

<style>
.gym {
  --ink: #0b0b0d;
  --panel: #17171a;
  --panel2: #1f1f23;
  --line: #2f2f36;
  --text: #f4f4f5;
  --mute: #a1a1aa;
  --red: #ef4444;
  --red-deep: #b91c1c;
  --red-soft: rgba(239, 68, 68, 0.14);
  --sky: #38bdf8;
  --sky-soft: rgba(56, 189, 248, 0.14);
  max-width: 960px;
  margin: 0 auto;
  color: var(--text);
  font-family: Inter, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.gym *, .gym *::before, .gym *::after { box-sizing: border-box; }
.gym p, .gym li { line-height: 1.6; color: var(--text); margin: 0; }
.gym ul, .gym ol { list-style: none; padding: 0; margin: 0; }
.gym li + li { margin-top: 0; }
.gym b { color: #fff; font-weight: 650; }
.gym a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.gym a:hover { color: #fecaca; }
.gym a:focus-visible { outline: 3px solid var(--red); outline-offset: 3px; border-radius: 6px; }
.gym kbd {
  font: inherit; font-size: 0.85em; font-weight: 700; color: #fff; background: var(--red-deep);
  border: 0; border-radius: 6px; padding: 0.05rem 0.45rem;
}
.gym code { font-size: 0.86em; background: var(--panel2); color: #fff; border-radius: 6px; padding: 0.1rem 0.4rem; overflow-wrap: anywhere; }
/* ---------- hero ---------- */
.gym .gym-hero {
  position: relative; overflow: hidden; isolation: isolate;
  background: radial-gradient(90% 120% at 100% 0%, rgba(56, 189, 248, 0.1), transparent 55%),
              radial-gradient(110% 120% at 0% 100%, rgba(185, 28, 28, 0.32), var(--ink) 62%);
  border: 1px solid var(--line); border-radius: 22px;
  padding: clamp(1.15rem, 4vw, 2.4rem);
}
.gym .gym-kicker { font-size: 0.78rem; font-weight: 700; letter-spacing: 0.16em; text-transform: uppercase; color: var(--red); margin-bottom: 0.55rem; }
.gym .gym-hero h1 {
  margin: 0 0 0.75rem; border: 0; padding: 0;
  font-size: clamp(2rem, 6.4vw, 3.4rem); line-height: 1.04; font-weight: 800; letter-spacing: -0.03em; color: #fff;
}
.gym .gym-hero h1 span { color: var(--red); }
.gym .gym-lede { max-width: 60ch; color: var(--mute); font-size: 1.05rem; }
.gym .gym-pulse { display: block; width: 100%; height: auto; margin-top: 1.3rem; border-radius: 14px; background: #0e0e11; border: 1px solid var(--line); }
.gym-pulse .grid line { stroke: #1a1a20; stroke-width: 1; }
.gym-pulse .ecg-dim { fill: none; stroke: #3a1616; stroke-width: 2.5; stroke-linejoin: round; stroke-linecap: round; }
.gym-pulse .ecg { fill: none; stroke: var(--red); stroke-width: 3; stroke-linejoin: round; stroke-linecap: round; stroke-dasharray: 160 840; stroke-dashoffset: 1000; animation: gym-beat 3.2s linear infinite; }
.gym-pulse .bell rect { fill: #2c2c33; }
.gym-pulse .bell .plate { fill: #3d3d46; }
.gym-pulse .bell { transform-box: fill-box; transform-origin: center; animation: gym-lift 3.2s ease-in-out infinite; }
.gym-pulse .lab { fill: var(--mute); font: 700 13px Inter, system-ui, sans-serif; letter-spacing: 0.12em; }
.gym-pulse .val { fill: #fff; font: 800 15px Inter, system-ui, sans-serif; }
.gym-pulse .track { fill: #1f1f25; }
.gym-pulse .fill-s { fill: var(--red); transform-box: fill-box; transform-origin: left center; animation: gym-fill 6.4s ease-in-out infinite; }
.gym-pulse .fill-a { fill: var(--sky); transform-box: fill-box; transform-origin: left center; animation: gym-fill 6.4s ease-in-out -2.2s infinite; }
@keyframes gym-beat { to { stroke-dashoffset: 0; } }
@keyframes gym-lift { 0%, 100% { transform: translateY(0); } 45% { transform: translateY(-10px); } 60% { transform: translateY(-10px); } }
@keyframes gym-fill { 0% { transform: scaleX(0.18); } 55% { transform: scaleX(1); } 80% { transform: scaleX(1); } 100% { transform: scaleX(0.18); } }
.gym .gym-stats { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 0.6rem; margin-top: 1.2rem; }
.gym .gym-stats li { background: rgba(23, 23, 26, 0.85); border: 1px solid var(--line); border-radius: 14px; padding: 0.7rem 0.9rem; }
.gym .gym-stats b { display: block; font-size: clamp(1.3rem, 4vw, 1.75rem); line-height: 1.1; font-weight: 800; color: #fff; font-variant-numeric: tabular-nums; }
.gym .gym-stats span { display: block; color: var(--mute); font-size: 0.82rem; line-height: 1.35; margin-top: 0.2rem; }
@media (max-width: 640px) { .gym .gym-stats { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
/* ---------- sections ---------- */
.gym .gym-h2 {
  display: flex; align-items: center; gap: 0.65rem;
  margin: 3rem 0 0.9rem; border: 0; padding: 0;
  font-size: 1.5rem; font-weight: 750; letter-spacing: -0.015em; line-height: 1.25; color: #fff;
}
.gym .gym-h2::before { content: ''; flex: none; width: 0.55rem; height: 1.3rem; border-radius: 3px; background: var(--red); }
.gym .gym-p { color: var(--mute); max-width: 70ch; }
.gym .gym-p + .gym-p { margin-top: 0.6rem; }
/* two stats */
.gym .gym-twin { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr)); gap: 0.8rem; }
.gym .gym-stat { border: 1px solid var(--line); border-radius: 18px; padding: 1.1rem 1.15rem; background: var(--panel); }
.gym .gym-stat.str { background: linear-gradient(160deg, rgba(239, 68, 68, 0.13), var(--panel) 55%); }
.gym .gym-stat.sta { background: linear-gradient(160deg, rgba(56, 189, 248, 0.12), var(--panel) 55%); }
.gym .gym-stat .gym-sh { display: flex; align-items: baseline; justify-content: space-between; gap: 0.6rem; margin-bottom: 0.5rem; }
.gym .gym-stat .gym-sh b { font-size: 1.2rem; }
.gym .gym-stat .gym-sh span { font-weight: 800; font-size: 1.05rem; font-variant-numeric: tabular-nums; }
.gym .gym-stat.str .gym-sh span { color: var(--red); }
.gym .gym-stat.sta .gym-sh span { color: var(--sky); }
.gym .gym-stat p { color: var(--mute); font-size: 0.96rem; }
.gym .gym-stat p + p { margin-top: 0.45rem; }
/* where */
.gym .gym-where { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 240px), 1fr)); gap: 0.7rem; }
.gym .gym-where li { background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 0.85rem 1rem; }
.gym .gym-where b { display: block; font-size: 0.78rem; letter-spacing: 0.1em; text-transform: uppercase; color: var(--red); margin-bottom: 0.25rem; }
.gym .gym-where span { display: block; color: var(--text); }
/* memberships */
.gym .gym-pass { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 0.7rem; margin-top: 1rem; }
.gym .gym-pass li { position: relative; overflow: hidden; border-radius: 16px; padding: 1rem 1.1rem; background: var(--panel2); border: 1px solid var(--line); }
.gym .gym-pass li::after { content: ''; position: absolute; right: -24px; bottom: -24px; width: 80px; height: 80px; border-radius: 50%; border: 10px solid rgba(255, 255, 255, 0.04); }
.gym .gym-pass b { display: block; font-size: 1.1rem; }
.gym .gym-pass span { display: block; color: var(--mute); font-size: 0.9rem; padding-right: 2.5rem; }
.gym .gym-pass .vip { border-color: rgba(239, 68, 68, 0.45); background: linear-gradient(150deg, rgba(185, 28, 28, 0.25), var(--panel2) 60%); }
@media (max-width: 600px) { .gym .gym-pass { grid-template-columns: minmax(0, 1fr); } }
/* exercises */
.gym .gym-ex { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 270px), 1fr)); gap: 0.7rem; }
.gym .gym-ex li { background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 0.95rem 1rem; }
.gym .gym-ex .gym-eh { display: flex; justify-content: space-between; align-items: baseline; gap: 0.5rem; }
.gym .gym-ex .gym-eh b { font-size: 1.05rem; }
.gym .gym-ex .gym-eh small { color: var(--mute); font-size: 0.8rem; white-space: nowrap; }
.gym .gym-ex .gym-key { display: block; color: var(--mute); font-size: 0.86rem; margin: 0.1rem 0 0.6rem; }
.gym .gym-bar { display: grid; grid-template-columns: 4.2rem minmax(0, 1fr) 4.6rem; align-items: center; gap: 0.5rem; font-size: 0.8rem; color: var(--mute); }
.gym .gym-bar + .gym-bar { margin-top: 0.3rem; }
.gym .gym-bar i { display: block; height: 0.5rem; border-radius: 99px; background: #26262c; overflow: hidden; }
.gym .gym-bar i::before { content: ''; display: block; height: 100%; width: var(--w); border-radius: 99px; background: var(--red); }
.gym .gym-bar.sta i::before { background: var(--sky); }
.gym .gym-bar em { font-style: normal; text-align: right; color: var(--text); font-variant-numeric: tabular-nums; }
/* steps */
.gym .gym-steps { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 200px), 1fr)); gap: 0.7rem; counter-reset: gymstep; }
.gym .gym-steps li { position: relative; background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 1rem 1rem 1rem 3.3rem; counter-increment: gymstep; }
.gym .gym-steps li::before {
  content: counter(gymstep); position: absolute; left: 0.9rem; top: 0.95rem;
  width: 1.75rem; height: 1.75rem; border-radius: 50%; display: grid; place-items: center;
  background: var(--red-soft); color: var(--red); font-weight: 800; font-size: 0.92rem;
}
.gym .gym-steps b { display: block; margin-bottom: 0.15rem; }
.gym .gym-steps span { color: var(--mute); font-size: 0.95rem; }
.gym .gym-list li { position: relative; padding-left: 1.2rem; }
.gym .gym-list li + li { margin-top: 0.45rem; }
.gym .gym-list li::before { content: ''; position: absolute; left: 0; top: 0.62em; width: 0.45rem; height: 0.45rem; border-radius: 2px; background: var(--red); }
/* supplements */
.gym .gym-sup { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 210px), 1fr)); gap: 0.7rem; }
.gym .gym-sup li { background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 0.95rem 1rem; }
.gym .gym-sup b { display: block; }
.gym .gym-sup em { display: inline-block; font-style: normal; font-weight: 800; font-size: 0.78rem; letter-spacing: 0.06em; color: var(--red); margin: 0.15rem 0 0.35rem; }
.gym .gym-sup span { display: block; color: var(--mute); font-size: 0.93rem; }
.gym .gym-sup .risk { border-color: rgba(239, 68, 68, 0.45); }
/* decay */
.gym .gym-decay { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0.7rem; }
.gym .gym-decay li { background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 1rem 1.1rem; }
.gym .gym-decay b { display: block; font-size: clamp(1.5rem, 5vw, 2rem); line-height: 1.1; font-weight: 800; font-variant-numeric: tabular-nums; }
.gym .gym-decay span { display: block; color: var(--mute); font-size: 0.92rem; margin-top: 0.2rem; }
.gym .gym-decay .pro b { color: var(--sky); }
@media (max-width: 520px) { .gym .gym-decay { grid-template-columns: minmax(0, 1fr); } }
.gym .gym-note { margin-top: 1rem; display: flex; gap: 0.7rem; align-items: flex-start; background: var(--sky-soft); border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 14px; padding: 0.8rem 1rem; }
.gym .gym-note svg { flex: none; width: 1.25rem; height: 1.25rem; margin-top: 0.15rem; color: var(--sky); }
.gym .gym-cmd { display: flex; flex-wrap: wrap; align-items: center; gap: 0.6rem 1rem; background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 0.95rem 1.1rem; }
.gym .gym-cmd code { font-size: 1rem; padding: 0.25rem 0.6rem; background: var(--red-deep); }
.gym .gym-cmd span { color: var(--mute); }
@media (prefers-reduced-motion: reduce) {
  .gym .gym-pulse .ecg, .gym .gym-pulse .bell, .gym .gym-pulse .fill-s, .gym .gym-pulse .fill-a { animation: none; }
  .gym .gym-pulse .ecg { stroke-dasharray: none; stroke-dashoffset: 0; }
}
</style>

<div class="gym">
<section class="gym-hero">
<p class="gym-kicker">Locatii · Muscle Sands Gym</p>
<h1>Sala de <span>sport</span></h1>
<p class="gym-lede">Te antrenezi pe plaja din Vespucci si cresti doua statistici: <b>forta</b>, care iti da kilograme in plus in inventar, si <b>stamina</b>, care te ajuta sa-ti revii mai repede dupa sprint. Ai nevoie de abonament.</p>
<svg class="gym-pulse" viewBox="0 0 640 220" role="img" aria-label="Puls de antrenament si cele doua statistici: forta pana la 20 kg si stamina pana la 100">
<g class="grid"><line x1="0" y1="40" x2="640" y2="40"/><line x1="0" y1="80" x2="640" y2="80"/><line x1="0" y1="120" x2="640" y2="120"/><line x1="64" y1="0" x2="64" y2="130"/><line x1="128" y1="0" x2="128" y2="130"/><line x1="192" y1="0" x2="192" y2="130"/><line x1="256" y1="0" x2="256" y2="130"/><line x1="320" y1="0" x2="320" y2="130"/><line x1="384" y1="0" x2="384" y2="130"/><line x1="448" y1="0" x2="448" y2="130"/><line x1="512" y1="0" x2="512" y2="130"/><line x1="576" y1="0" x2="576" y2="130"/></g>
<path class="ecg-dim" d="M0 80 H120 L135 80 L145 60 L155 80 L170 80 L180 20 L192 120 L204 80 L230 80 L242 66 L254 80 H420 L435 80 L445 60 L455 80 L470 80 L480 20 L492 120 L504 80 L530 80 L542 66 L554 80 H640"/>
<path class="ecg" pathLength="1000" d="M0 80 H120 L135 80 L145 60 L155 80 L170 80 L180 20 L192 120 L204 80 L230 80 L242 66 L254 80 H420 L435 80 L445 60 L455 80 L470 80 L480 20 L492 120 L504 80 L530 80 L542 66 L554 80 H640"/>
<g class="bell"><rect x="286" y="76" width="68" height="8" rx="3"/><rect class="plate" x="276" y="58" width="12" height="44" rx="3"/><rect class="plate" x="352" y="58" width="12" height="44" rx="3"/><rect class="plate" x="264" y="64" width="10" height="32" rx="3"/><rect class="plate" x="366" y="64" width="10" height="32" rx="3"/></g>
<text class="lab" x="24" y="160">FORTA</text><text class="val" x="566" y="160">20 kg</text>
<rect class="track" x="110" y="150" width="440" height="12" rx="6"/><rect class="fill-s" x="110" y="150" width="440" height="12" rx="6"/>
<text class="lab" x="24" y="196">STAMINA</text><text class="val" x="566" y="196">100</text>
<rect class="track" x="110" y="186" width="440" height="12" rx="6"/><rect class="fill-a" x="110" y="186" width="440" height="12" rx="6"/>
</svg>
<ul class="gym-stats">
<li><b>20 kg</b><span>forta maxima</span></li>
<li><b>100</b><span>stamina maxima</span></li>
<li><b>+20 kg</b><span>in inventar, la forta maxima</span></li>
<li><b>6</b><span>tipuri de exercitii</span></li>
</ul>
</section>
<h2 class="gym-h2">Ce castigi</h2>
<div class="gym-twin">
<div class="gym-stat str">
<div class="gym-sh"><b>Forta</b><span>0 - 20 kg</span></div>
<p>Fiecare kilogram intreg de forta iti da <b>+1 kg</b> capacitate in inventar. La 20 kg cari cu 20 kg mai mult.</p>
<p>O cresti la greutati, tractiuni si flotari, iar mai putin la abdomene si yoga.</p>
</div>
<div class="gym-stat sta">
<div class="gym-sh"><b>Stamina</b><span>0 - 100</span></div>
<p>Cu cat ai mai multa stamina, cu atat iti revii mai repede dupa sprint. La 100 iti revii de doua ori mai repede decat la 0.</p>
<p>O cresti pe banda de alergat, iar mai putin la abdomene si yoga.</p>
</div>
</div>
<p class="gym-p" style="margin-top:0.9rem">Amandoua pornesc de la 0. Cand una ajunge la maxim, exercitiile pentru ea nu-ti mai dau nimic si primesti un mesaj.</p>
<h2 class="gym-h2">Unde e sala</h2>
<ul class="gym-where">
<li><b>Muscle Sands Gym</b><span>Sala in aer liber de pe plaja din Vespucci, langa codul postal 693.</span></li>
<li><b>Pe harta</b><span>Blipul rosu „Sala de Sport”. Langa el e si „Suplimente Sala”.</span></li>
<li><b>Zona sigura</b><span>Sala e zona sigura, deci te antrenezi linistit.</span></li>
</ul>
<h2 class="gym-h2">Abonamentul</h2>
<p class="gym-p">Aparatele merg doar cu abonament activ. Il cumperi de la <b>receptionerul</b> de la intrare: te apropii si apesi <kbd>E</kbd>. Inainte sa platesti, vezi pretul si durata fiecarui abonament.</p>
<ul class="gym-pass">
<li><b>Basic</b><span>Toate aparatele, cea mai scurta durata</span></li>
<li><b>Premium</b><span>Toate aparatele, durata mai lunga</span></li>
<li class="vip"><b>VIP</b><span>Toate aparatele, cea mai lunga durata</span></li>
</ul>
<ul class="gym-list" style="margin-top:1rem">
<li>Toate trei iti dau acces la toate aparatele. Difera doar durata.</li>
<li>Nu poti cumpara un abonament nou cat timp il ai pe cel vechi activ.</li>
<li>Cu <b>Verifica abonamentul</b> vezi ce abonament ai si cat mai e pana expira.</li>
</ul>
<h2 class="gym-h2">Exercitiile</h2>
<p class="gym-p">Langa fiecare aparat apare un buton cu <kbd>E</kbd>. Cifrele de mai jos arata cat castigi dupa un exercitiu reusit si cate aparate de fiecare fel are sala.</p>
<ul class="gym-ex" style="margin-top:1rem">
<li><div class="gym-eh"><b>Banda de alergat</b><small>7,5 s · 5 aparate</small></div><span class="gym-key">Alearga pe banda</span><div class="gym-bar sta"><span>Stamina</span><i style="--w:100%"></i><em>+0.083</em></div></li>
<li><div class="gym-eh"><b>Greutati</b><small>7,5 s · 4 aparate</small></div><span class="gym-key">Ridica greutatile</span><div class="gym-bar"><span>Forta</span><i style="--w:100%"></i><em>+0.017 kg</em></div></li>
<li><div class="gym-eh"><b>Tractiuni</b><small>6 s · 2 bare</small></div><span class="gym-key">Fa tractiuni</span><div class="gym-bar"><span>Forta</span><i style="--w:100%"></i><em>+0.017 kg</em></div></li>
<li><div class="gym-eh"><b>Flotari</b><small>6 s · 1 saltea</small></div><span class="gym-key">Fa flotari</span><div class="gym-bar"><span>Forta</span><i style="--w:82%"></i><em>+0.014 kg</em></div></li>
<li><div class="gym-eh"><b>Abdomene</b><small>5 s · 1 saltea</small></div><span class="gym-key">Fa abdomene</span><div class="gym-bar"><span>Forta</span><i style="--w:47%"></i><em>+0.008 kg</em></div><div class="gym-bar sta"><span>Stamina</span><i style="--w:48%"></i><em>+0.04</em></div></li>
<li><div class="gym-eh"><b>Yoga</b><small>12,5 s · 1 saltea</small></div><span class="gym-key">Fa yoga</span><div class="gym-bar"><span>Forta</span><i style="--w:59%"></i><em>+0.01 kg</em></div><div class="gym-bar sta"><span>Stamina</span><i style="--w:60%"></i><em>+0.05</em></div></li>
</ul>
<p class="gym-p" style="margin-top:0.9rem">Ca reper, o ora de greutati si tractiuni te urca cu aproximativ 1 kg de forta, iar o ora pe banda cu aproximativ 5 puncte de stamina.</p>
<h2 class="gym-h2">Cum decurge un exercitiu</h2>
<ol class="gym-steps">
<li><b>Apesi <kbd>E</kbd> la aparat</b><span>Daca aparatul e ocupat de altcineva, astepti sa se elibereze.</span></li>
<li><b>Bara de progres</b><span>Personajul face exercitiul. Poti anula, dar atunci nu primesti nimic.</span></li>
<li><b>Skillcheck</b><span>La final apasa <kbd>E</kbd> la momentul potrivit.</span></li>
<li><b>Rezultat</b><span>Reusit: primesti castigul. Ratat: nu primesti nimic.</span></li>
</ol>
<ul class="gym-list" style="margin-top:1rem">
<li>Intre doua exercitii ai o pauza de <b>4 secunde</b>.</li>
<li>Cat timp te antrenezi, personajul pune arma la loc si nu poti folosi inventarul.</li>
<li>Pe un aparat se antreneaza un singur jucator.</li>
</ul>
<h2 class="gym-h2">Suplimente</h2>
<p class="gym-p">Le cumperi de la magazinul <b>Suplimente Sala</b>, langa receptie. Fiecare doza adauga efect, pana la maxim <b>3 doze</b> cumulate. Efectul scade treptat si primesti un mesaj cand se termina.</p>
<ul class="gym-sup" style="margin-top:1rem">
<li><b><img class="eg-item" src="/items/gym_proteins.webp" alt="">Proteina</b><em>Pierzi forta mai incet</em><span>Cat timp e activa, pierderea vine la 20 de ore jucate in loc de 15.</span></li>
<li><b><img class="eg-item" src="/items/gym_creatine.webp" alt="">Creatina</b><em>+25% castig</em><span>Castigi forta si stamina mai repede la fiecare exercitiu.</span></li>
<li><b><img class="eg-item" src="/items/gym_energy_drink.webp" alt="">Bautura Energizanta</b><em>-15% timp</em><span>Exercitiile dureaza cu 15% mai putin.</span></li>
<li class="risk"><b><img class="eg-item" src="/items/gym_steroids.webp" alt="">Steroizi</b><em>+25% castig, cu risc</em><span>La fel ca creatina, dar pierzi 5 HP la fiecare 30 de minute cat sunt activi. Daca ii folosesti des, devii dependent.</span></li>
</ul>
<h2 class="gym-h2">Pierderea statisticilor</h2>
<p class="gym-p">Forta si stamina scad in timp, dar doar cat esti conectat. Cat esti offline nu pierzi nimic.</p>
<ul class="gym-decay" style="margin-top:1rem">
<li><b>15 ore</b><span>jucate: pierzi 1 kg forta si 5 stamina</span></li>
<li class="pro"><b>20 de ore</b><span>jucate, cu proteina activa: aceeasi pierdere</span></li>
</ul>
<div class="gym-note"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v4h1"/></svg><p>Antrenamentul nu opreste ceasul. Pierderea merge oricum, iar ce castigi la sala se aduna peste ea. Daca te antrenezi mai mult decat pierzi, cresti. Cand scade ceva, primesti o notificare cu cat ai pierdut.</p></div>
<h2 class="gym-h2">Din magazinul EG</h2>
<p class="gym-p">In <a href="/zona-info/store">magazinul EG</a> poti lua, cu EG Coins, forta si stamina direct la maxim. Ceasul pierderii porneste de la zero. Nu merge daca ai deja amandoua la maxim.</p>
<h2 class="gym-h2">Comanda</h2>
<div class="gym-cmd"><code>/checkstats</code><span>Iti arata stamina, forta si cat bonus ai in inventar.</span></div>
</div>
