---
outline: false
---

<style>
.ap {
  --ink: #09090b;
  --panel: #18181b;
  --panel2: #1f1f23;
  --line: #2e2e33;
  --text: #f4f4f5;
  --mute: #a1a1aa;
  --red: #ef4444;
  --red-deep: #b91c1c;
  --red-soft: rgba(239, 68, 68, 0.14);
  --glass: #7dd3fc;
  --glass-soft: rgba(125, 211, 252, 0.12);
  --lamp: #fbbf24;
  --green: #4ade80;
  max-width: 960px;
  margin: 0 auto;
  color: var(--text);
  font-family: Inter, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.ap *, .ap *::before, .ap *::after { box-sizing: border-box; }
.ap p, .ap li { margin: 0; line-height: 1.6; color: var(--text); }
.ap ul, .ap ol { list-style: none; padding: 0; margin: 0; }
.ap li + li { margin-top: 0; }
.ap b { color: #fff; font-weight: 650; }
.ap a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.ap a:hover { color: #fecaca; }
.ap a:focus-visible { outline: 3px solid var(--red); outline-offset: 3px; border-radius: 6px; }
.ap kbd {
  font: inherit; font-size: 0.85em; font-weight: 700; color: #fff; background: var(--red-deep);
  border: 0; border-radius: 6px; padding: 0.05rem 0.45rem; white-space: nowrap;
}
.ap code { font-size: 0.88em; color: #fff; background: #27272a; border-radius: 6px; padding: 0.1rem 0.4rem; }
/* ---------- hero: tower with a running elevator ---------- */
.ap .ap-hero {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 330px), 1fr)); align-items: end; gap: 0.5rem;
  position: relative; overflow: hidden; isolation: isolate;
  border: 1px solid var(--line); border-radius: 22px;
  background: radial-gradient(90% 110% at 100% 0%, rgba(125, 211, 252, 0.12), transparent 55%),
              radial-gradient(110% 120% at 0% 100%, rgba(185, 28, 28, 0.28), var(--ink) 62%);
}
.ap .ap-hero-text { padding: clamp(1.1rem, 4vw, 2.3rem); align-self: center; }
.ap .ap-kicker {
  margin: 0 0 0.5rem; font: 700 0.75rem/1 ui-monospace, Menlo, Consolas, monospace;
  letter-spacing: 0.18em; text-transform: uppercase; color: var(--red);
}
.ap .ap-hero h1 {
  margin: 0 0 0.7rem; border: 0; padding: 0;
  font-size: clamp(2rem, 6vw, 3rem); line-height: 1.02; overflow-wrap: normal; word-break: normal; hyphens: none; font-weight: 800; letter-spacing: -0.03em; color: #fff;
}
.ap .ap-lede { max-width: 52ch; color: var(--mute); font-size: 1.05rem; }
.ap .ap-stats { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 0.55rem; margin-top: 1.2rem; }
.ap .ap-stats li { background: rgba(24, 24, 27, 0.9); border: 1px solid var(--line); border-radius: 14px; padding: 0.65rem 0.8rem; }
.ap .ap-stats b { display: block; font-size: clamp(1.3rem, 4vw, 1.7rem); line-height: 1.1; font-weight: 800; font-variant-numeric: tabular-nums; }
.ap .ap-stats span { display: block; margin-top: 0.2rem; color: var(--mute); font-size: 0.8rem; line-height: 1.35; }
@media (max-width: 480px) {
  .ap .ap-stats li { padding: 0.6rem 0.65rem; }
  .ap .ap-stats span { font-size: 0.74rem; }
}
.ap .ap-tower { display: block; width: 100%; max-width: 420px; height: auto; margin: 0 auto; }
.ap .ap-tower { padding: 0 1rem; }
.ap-tower .star { fill: #fff; opacity: 0.3; animation: ap-twinkle 5s ease-in-out infinite; }
.ap-tower .star:nth-of-type(2n) { animation-delay: -1.8s; }
.ap-tower .star:nth-of-type(3n) { animation-delay: -3.3s; }
.ap-tower .body { fill: #0e0e12; stroke: #2c2c34; stroke-width: 1.2; }
.ap-tower .eco { fill: #0c0c0f; stroke: #26262d; stroke-width: 1.2; }
.ap-tower .crown { fill: #15151a; stroke: #2c2c34; stroke-width: 1.2; }
.ap-tower .beacon { fill: var(--red); animation: ap-beacon 2.4s ease-in-out infinite; }
.ap-tower .shaft { fill: rgba(125, 211, 252, 0.07); stroke: rgba(125, 211, 252, 0.35); stroke-width: 1; }
.ap-tower .cable { stroke: rgba(125, 211, 252, 0.35); stroke-width: 1; }
.ap-tower .car { animation: ap-lift 12s cubic-bezier(.55, 0, .35, 1) infinite; }
.ap-tower .car rect { fill: var(--glass); }
.ap-tower .ground { fill: #050506; }
.ap-tower .door { fill: var(--lamp); opacity: 0.85; }
.ap-tower .w { fill: var(--lamp); opacity: 0.07; animation: ap-lights 13s steps(1, end) infinite; }
.ap-tower .w.c { fill: var(--glass); }
.ap-tower .d1 { animation-delay: 0s; }
.ap-tower .d2 { animation-delay: -1.5s; }
.ap-tower .d3 { animation-delay: -3s; }
.ap-tower .d4 { animation-delay: -4.4s; }
.ap-tower .d5 { animation-delay: -6.1s; }
.ap-tower .d6 { animation-delay: -7.6s; }
.ap-tower .d7 { animation-delay: -9.2s; }
.ap-tower .d8 { animation-delay: -10.8s; }
.ap-tower .bubble { animation: ap-bob 4s ease-in-out infinite; }
@keyframes ap-lift {
  0%, 8% { transform: translateY(0); }
  22%, 34% { transform: translateY(-96px); }
  50%, 62% { transform: translateY(-192px); }
  76%, 86% { transform: translateY(-48px); }
  100% { transform: translateY(0); }
}
@keyframes ap-lights { 0% { opacity: 0.07; } 28% { opacity: 0.9; } 85% { opacity: 0.07; } }
@keyframes ap-twinkle { 0%, 100% { opacity: 0.15; } 50% { opacity: 0.75; } }
@keyframes ap-beacon { 0%, 100% { opacity: 0.25; } 50% { opacity: 1; } }
@keyframes ap-bob { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-4px); } }
/* ---------- sections ---------- */
.ap .ap-h2 {
  display: flex; align-items: flex-start; gap: 0.65rem;
  margin: 3rem 0 0.9rem; border: 0; padding: 0;
  font-size: 1.5rem; font-weight: 750; letter-spacing: -0.015em; line-height: 1.25; color: #fff;
}
.ap .ap-h2::before { margin-top: calc(0.5lh - 0.95rem / 2);
  content: ''; flex: none; width: 0.55rem; height: 0.95rem; border-radius: 2px; background: var(--red);
  box-shadow: 0.75rem 0 0 -0.1rem var(--red-soft);
}
.ap .ap-h3 { margin: 0 0 0.35rem; border: 0; padding: 0; font-size: 1.05rem; font-weight: 700; color: #fff; line-height: 1.3; }
.ap .ap-sub { max-width: 66ch; margin-bottom: 1rem; color: var(--mute); }
.ap .ap-card { background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 1.1rem 1.2rem; }
.ap .ap-card p { color: var(--mute); font-size: 0.96rem; }
.ap .ap-card p + p { margin-top: 0.5rem; }
.ap .ap-note { margin-top: 0.85rem; color: var(--mute); font-size: 0.93rem; }
.ap .ap-card .ap-h3 { color: #fff; font-size: 1.05rem; }
.ap .ap-card .ap-steps { margin-top: 0.4rem; }
.ap .ap-two { display: grid; grid-template-columns: repeat(auto-fit, minmax(270px, 1fr)); gap: 0.75rem; }
.ap .ap-tag {
  display: inline-block; margin-bottom: 0.45rem; font-size: 0.7rem; font-weight: 700; letter-spacing: 0.12em;
  text-transform: uppercase; color: var(--glass);
}
.ap .ap-tag.r { color: var(--red); }
/* building directory: floors as rows */
.ap .ap-bld { padding: 0; overflow: hidden; display: flex; flex-direction: column; }
.ap .ap-bld-head { padding: 1rem 1.2rem 0.8rem; border-bottom: 1px solid var(--line); background: var(--panel2); }
.ap .ap-bld-head p { font-size: 0.9rem; }
.ap .ap-floors li {
  display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: 0.15rem 1rem; align-items: baseline;
  padding: 0.7rem 1.2rem; border-top: 1px solid var(--line);
}
.ap .ap-floors li:first-child { border-top: 0; }
.ap .ap-floors .t { font-weight: 700; color: #fff; }
.ap .ap-floors .n { font: 800 0.9rem/1 ui-monospace, Menlo, Consolas, monospace; color: var(--glass); white-space: nowrap; }
.ap .ap-floors .d { grid-column: 1 / -1; color: var(--mute); font-size: 0.88rem; line-height: 1.4; }
.ap .ap-bld-foot { margin-top: auto; display: flex; flex-wrap: wrap; gap: 0.4rem; padding: 0.8rem 1.2rem 1rem; border-top: 1px solid var(--line); }
.ap .ap-chip {
  font-size: 0.8rem; font-weight: 650; color: var(--text); border: 1px solid var(--line); border-radius: 999px;
  padding: 0.2rem 0.65rem; background: rgba(9, 9, 11, 0.6);
}
/* steps */
.ap .ap-steps { display: grid; gap: 0.6rem; counter-reset: ap-step; }
.ap .ap-steps li {
  position: relative; counter-increment: ap-step; padding-left: 2.3rem; color: var(--mute); font-size: 0.95rem;
}
.ap .ap-steps li::before {
  content: counter(ap-step); position: absolute; left: 0; top: 0.05rem;
  width: 1.5rem; height: 1.5rem; border-radius: 50%; display: grid; place-items: center;
  font-size: 0.78rem; font-weight: 800; color: #fff; background: var(--red-deep);
}
/* interphone flow */
.ap .ap-flow { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 0.6rem; }
.ap .ap-flow li { position: relative; background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 0.95rem 1rem; }
.ap .ap-flow .who { display: block; margin-bottom: 0.3rem; font-size: 0.7rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: var(--glass); }
.ap .ap-flow .who.o { color: var(--lamp); }
.ap .ap-flow p { color: var(--mute); font-size: 0.93rem; }
/* lists */
.ap .ap-list li { position: relative; padding-left: 1.1rem; color: var(--mute); font-size: 0.95rem; }
.ap .ap-list li + li { margin-top: 0.4rem; }
.ap .ap-list li::before {
  content: ''; position: absolute; left: 0; top: 0.62em; width: 0.42rem; height: 0.42rem; border-radius: 2px; background: var(--red);
}
/* styles swatches */
.ap .ap-swatches { display: flex; flex-wrap: wrap; gap: 0.45rem; margin-top: 0.7rem; }
.ap .ap-swatches li {
  display: inline-flex; align-items: center; gap: 0.45rem; font-size: 0.86rem; font-weight: 600; color: var(--text);
  background: var(--ink); border: 1px solid var(--line); border-radius: 999px; padding: 0.25rem 0.7rem 0.25rem 0.35rem;
}
.ap .ap-swatches i { display: inline-block; width: 1rem; height: 1rem; border-radius: 50%; border: 1px solid rgba(255, 255, 255, 0.2); }
.ap .s1 { background: linear-gradient(135deg, #e4e4e7, #71717a); }
.ap .s2 { background: linear-gradient(135deg, #3f3f46, #18181b); }
.ap .s3 { background: linear-gradient(135deg, #f97316, #db2777); }
.ap .s4 { background: linear-gradient(135deg, #a8a29e, #44403c); }
.ap .s5 { background: linear-gradient(135deg, #fafafa, #09090b); }
.ap .s6 { background: linear-gradient(135deg, #be123c, #4c0519); }
.ap .s7 { background: linear-gradient(135deg, #facc15, #7c2d12); }
.ap .s8 { background: linear-gradient(135deg, #22d3ee, #0e7490); }
.ap .h1c { background: linear-gradient(135deg, #d4d4d8, #52525b); }
.ap .h2c { background: linear-gradient(135deg, #f59e0b, #78350f); }
.ap .h3c { background: linear-gradient(135deg, #a8a29e, #292524); }
.ap .h4c { background: linear-gradient(135deg, #f59e0b, #44403c); }
.ap .h5c { background: linear-gradient(135deg, #ec4899, #7c3aed); }
@media (prefers-reduced-motion: reduce) {
  .ap .ap-tower .w, .ap .ap-tower .star, .ap .ap-tower .beacon, .ap .ap-tower .car, .ap .ap-tower .bubble { animation: none; }
  .ap .ap-tower .w.d1, .ap .ap-tower .w.d3, .ap .ap-tower .w.d5, .ap .ap-tower .w.d8 { opacity: 0.85; }
  .ap .ap-tower .beacon { opacity: 1; }
}
</style>

<div class="ap">
<section class="ap-hero">
<div class="ap-hero-text">
<p class="ap-kicker">Proprietati</p>
<h1>Apartamente</h1>
<p class="ap-lede">Un apartament intr-un bloc al orasului, cu seif, garderoba si interfon.</p>
<ul class="ap-stats">
<li><b>36</b><span>apartamente</span></li>
<li><b>2</b><span>blocuri</span></li>
<li><b>6</b><span>tipuri de interior</span></li>
</ul>
</div>
<svg class="ap-tower" viewBox="0 0 360 330" role="img" aria-label="Un turn de apartamente noaptea, cu liftul urcand si coborand intre etaje">
<circle class="star" cx="30" cy="30" r="1.3"/><circle class="star" cx="90" cy="62" r="1.1"/><circle class="star" cx="310" cy="26" r="1.4"/><circle class="star" cx="336" cy="88" r="1.1"/><circle class="star" cx="60" cy="112" r="1.2"/><circle class="star" cx="290" cy="130" r="1.2"/>
<rect class="crown" x="142" y="26" width="96" height="16"/>
<line x1="190" y1="8" x2="190" y2="26" stroke="#3f3f46" stroke-width="2"/>
<circle class="beacon" cx="190" cy="8" r="3.5"/>
<rect class="body" x="132" y="42" width="116" height="250"/>
<rect class="shaft" x="181" y="48" width="18" height="238"/>
<line class="cable" x1="190" y1="48" x2="190" y2="280"/>
<g class="car"><rect x="183" y="262" width="14" height="20" rx="2"/></g>
<rect class="w d1" x="142" y="56" width="14" height="10"/><rect class="w d5" x="160" y="56" width="14" height="10"/><rect class="w c d3" x="206" y="56" width="14" height="10"/><rect class="w d7" x="224" y="56" width="14" height="10"/>
<rect class="w d4" x="142" y="80" width="14" height="10"/><rect class="w c d8" x="160" y="80" width="14" height="10"/><rect class="w d2" x="206" y="80" width="14" height="10"/><rect class="w d6" x="224" y="80" width="14" height="10"/>
<rect class="w d6" x="142" y="104" width="14" height="10"/><rect class="w d1" x="160" y="104" width="14" height="10"/><rect class="w d5" x="206" y="104" width="14" height="10"/><rect class="w c d3" x="224" y="104" width="14" height="10"/>
<rect class="w c d2" x="142" y="128" width="14" height="10"/><rect class="w d7" x="160" y="128" width="14" height="10"/><rect class="w d8" x="206" y="128" width="14" height="10"/><rect class="w d4" x="224" y="128" width="14" height="10"/>
<rect class="w d8" x="142" y="152" width="14" height="10"/><rect class="w d3" x="160" y="152" width="14" height="10"/><rect class="w c d1" x="206" y="152" width="14" height="10"/><rect class="w d5" x="224" y="152" width="14" height="10"/>
<rect class="w d5" x="142" y="176" width="14" height="10"/><rect class="w d2" x="160" y="176" width="14" height="10"/><rect class="w d6" x="206" y="176" width="14" height="10"/><rect class="w d8" x="224" y="176" width="14" height="10"/>
<rect class="w d3" x="142" y="200" width="14" height="10"/><rect class="w c d6" x="160" y="200" width="14" height="10"/><rect class="w d4" x="206" y="200" width="14" height="10"/><rect class="w d1" x="224" y="200" width="14" height="10"/>
<rect class="w d7" x="142" y="224" width="14" height="10"/><rect class="w d4" x="160" y="224" width="14" height="10"/><rect class="w d2" x="206" y="224" width="14" height="10"/><rect class="w c d7" x="224" y="224" width="14" height="10"/>
<rect class="w d1" x="142" y="248" width="14" height="10"/><rect class="w d8" x="224" y="248" width="14" height="10"/>
<rect class="door" x="176" y="270" width="28" height="22" rx="2"/>
<rect class="eco" x="22" y="196" width="92" height="96"/>
<rect class="w d2" x="32" y="208" width="14" height="10"/><rect class="w d6" x="58" y="208" width="14" height="10"/><rect class="w d3" x="84" y="208" width="14" height="10"/>
<rect class="w d7" x="32" y="232" width="14" height="10"/><rect class="w c d4" x="58" y="232" width="14" height="10"/><rect class="w d1" x="84" y="232" width="14" height="10"/>
<rect class="w d5" x="32" y="256" width="14" height="10"/><rect class="w d8" x="84" y="256" width="14" height="10"/>
<rect class="eco" x="266" y="226" width="70" height="66"/>
<rect class="w d3" x="276" y="238" width="14" height="10"/><rect class="w d7" x="310" y="238" width="14" height="10"/><rect class="w c d5" x="276" y="262" width="14" height="10"/>
<g class="bubble"><rect x="134" y="300" width="112" height="22" rx="11" fill="#18181b" stroke="#b91c1c" stroke-width="1.5"/><text x="190" y="315" text-anchor="middle" fill="#fff" font-family="Inter, system-ui, sans-serif" font-size="10" font-weight="700">[E] Eclipse Towers</text></g>
<rect class="ground" x="0" y="292" width="360" height="6"/>
</svg>
</section>
<h2 class="ap-h2">Blocurile</h2>
<p class="ap-sub">Pe harta, blocurile au iconita de cladire cu numele lor. La intrare apare <b>[E] Eclipse Towers</b> sau <b>[E] Apartamente Eco</b>. In fiecare bloc, jumatate din apartamente se vand pe euro si jumatate pe EG Coins.</p>
<div class="ap-two">
<div class="ap-card ap-bld">
<div class="ap-bld-head"><span class="ap-tag">Bloc de lux</span><p class="ap-h3">Eclipse Towers</p><p>24 de apartamente, in patru tipuri de interior.</p></div>
<ul class="ap-floors">
<li><span class="t">Penthouse Suite 1</span><span class="n">6 ap.</span><span class="d">Penthouse la ultimul etaj, 8 stiluri de renovare.</span></li>
<li><span class="t">Penthouse Suite 2</span><span class="n">6 ap.</span><span class="d">Penthouse, 8 stiluri de renovare.</span></li>
<li><span class="t">Penthouse Suite 3</span><span class="n">6 ap.</span><span class="d">Penthouse, 8 stiluri de renovare.</span></li>
<li><span class="t">Apartment 3</span><span class="n">6 ap.</span><span class="d">Apartament obisnuit in turn, 5 stiluri de renovare.</span></li>
</ul>
<div class="ap-bld-foot"><span class="ap-chip">Seif 2.000 kg</span><span class="ap-chip">Garderoba</span><span class="ap-chip">Interfon</span></div>
</div>
<div class="ap-card ap-bld">
<div class="ap-bld-head"><span class="ap-tag">Bloc pentru inceput</span><p class="ap-h3">Apartamente Eco</p><p>12 apartamente, in doua tipuri de interior.</p></div>
<ul class="ap-floors">
<li><span class="t">Apartament Standard</span><span class="n">6 ap.</span><span class="d">Apartament de nivel mediu, 5 stiluri de renovare.</span></li>
<li><span class="t">Garsoniera</span><span class="n">6 ap.</span><span class="d">Garsoniera mica, 5 stiluri de renovare.</span></li>
</ul>
<div class="ap-bld-foot"><span class="ap-chip">Seif 1.000 kg</span><span class="ap-chip">Garderoba</span><span class="ap-chip">Interfon</span></div>
</div>
</div>
<h2 class="ap-h2">Cum cumperi un apartament</h2>
<div class="ap-two">
<div class="ap-card"><span class="ap-tag">De la agent</span><p class="ap-h3">Cumpara</p><ol class="ap-steps">
<li>Mergi la <b>Emilio Corso</b>, agentul imobiliar de langa primarie, si apasa <kbd>E</kbd>.</li>
<li>Alege <b>Apartamente</b>. Langa fiecare bloc vezi cate apartamente mai sunt libere.</li>
<li>Alege apartamentul. Fisa iti arata pretul, intretinerea, cat incape in seif si cati chiriasi poti avea.</li>
<li><b>Cumpara apartament</b>: banii se iau din banca (euro) sau din EG Coins. Primesti <b>Contractul de vanzare-cumparare</b>.</li>
</ol><p class="ap-note">Cu <b>Vezi locatia pe GPS</b> iti pui un punct pe harta, la intrarea blocului.</p></div>
<div class="ap-card"><span class="ap-tag">Inainte sa cumperi</span><p class="ap-h3">Viziteaza</p><ol class="ap-steps">
<li>Mergi la intrarea blocului si apasa <kbd>E</kbd>.</li>
<li>Alege <b>Viziteaza un apartament</b>. Apar doar apartamentele scoase la vanzare.</li>
<li>Alege apartamentul si stilul de renovare pe care vrei sa-l vezi.</li>
<li>Intri singur intr-o copie a apartamentului. Iesi cu <kbd>E</kbd> la usa.</li>
</ol></div>
</div>
<h2 class="ap-h2">Intrarea si interfonul</h2>
<p class="ap-sub">La intrarea blocului apesi <kbd>E</kbd>. Daca ai un apartament sau stai cu chirie, alegi <b>Intra in apartament</b>. Ceilalti cer voie prin interfon.</p>
<ol class="ap-flow">
<li><span class="who">Vizitator</span><p>La intrare alege <b>Cere acces la un apartament</b> si apartamentul. Proprietarul trebuie sa fie pe server.</p></li>
<li><span class="who o">Proprietar</span><p>Primeste mesajul <b>Interfon</b> si are 45 de secunde sa raspunda.</p></li>
<li><span class="who o">Proprietar</span><p>Merge la usa apartamentului, apasa <kbd>H</kbd> si accepta sau refuza cererea.</p></li>
<li><span class="who">Vizitator</span><p>Daca a ramas la intrarea blocului, intra. Daca nu primeste raspuns, cererea expira.</p></li>
</ol>
<p class="ap-note">Din apartament iesi cu <kbd>E</kbd> la usa si ajungi la intrarea blocului.</p>
<h2 class="ap-h2">In apartament</h2>
<div class="ap-two">
<div class="ap-card"><p class="ap-h3">Seiful</p><p>Langa seif apesi <kbd>G</kbd> si alegi <b>Deschide seiful</b>. Merge doar din interiorul apartamentului, pentru proprietar si pentru chiriasii carora le dai acces. Chiria intra aici, in bani cash.</p></div>
<div class="ap-card"><p class="ap-h3">Garderoba</p><p>Apesi <kbd>E</kbd> la garderoba si iti schimbi tinuta cu una din cele salvate.</p></div>
<div class="ap-card"><p class="ap-h3">Meniul proprietarului</p><p>La punctul din apartament apesi <kbd>E</kbd>: chiriasi, intretinere si renovare.</p></div>
<div class="ap-card"><p class="ap-h3">Patul</p><p>Ca proprietar sau chirias, scrii <code>/sleep</code> oriunde in apartament. Ce primesti si ce pierzi cand dormi afli pe pagina <a href="/proprietati/despre-case">Case</a>.</p></div>
</div>
<h2 class="ap-h2">Renovarea</h2>
<p class="ap-sub">Din meniul proprietarului → <b>Renovare</b> schimbi stilul interiorului. Cand esti in apartament, <b>Previzualizeaza</b> iti arata stilul gratuit timp de 120 de secunde, apoi revine cel vechi. <b>Aplica renovarea</b> costa EG Coins, iar pretul il vezi in meniu.</p>
<div class="ap-two">
<div class="ap-card"><span class="ap-tag">Penthouse Suite 1, 2, 3</span><p class="ap-h3">8 stiluri</p><ul class="ap-swatches">
<li><i class="s1"></i>Modern</li><li><i class="s2"></i>Mohorat</li><li><i class="s3"></i>Vibrant</li><li><i class="s4"></i>Elegant</li><li><i class="s5"></i>Monocrom</li><li><i class="s6"></i>Seducator</li><li><i class="s7"></i>Regal</li><li><i class="s8"></i>Aqua</li>
</ul></div>
<div class="ap-card"><span class="ap-tag">Apartment 3, Standard, Garsoniera</span><p class="ap-h3">5 stiluri</p><ul class="ap-swatches">
<li><i class="h1c"></i>Standard</li><li><i class="h2c"></i>Bar</li><li><i class="h3c"></i>Salon de fumat</li><li><i class="h4c"></i>Salon Relaxat</li><li><i class="h5c"></i>Petrecere Plina</li>
</ul></div>
</div>
<h2 class="ap-h2">Chiriasi</h2>
<div class="ap-two">
<div class="ap-card"><span class="ap-tag">Proprietar</span><ul class="ap-list">
<li>Meniul proprietarului → <b>Gestioneaza chiriasi</b> → <b>Adauga chirias nou</b>. Jucatorul trebuie sa fie langa tine, la cel mult 5 metri.</li>
<li>Stabilesti chiria pe ora, in limitele serverului. Cati chiriasi incap scrie in fisa apartamentului.</li>
<li>Vezi ultima plata a fiecarui chirias sau <b>Plata esuata</b>.</li>
<li>Poti schimba chiria, poti da sau lua accesul la seif si poti scoate chiriasul.</li>
<li>Din <b>Telefon → Case</b> vezi cine are cheie si poti da sau lua chei.</li>
</ul></div>
<div class="ap-card"><span class="ap-tag r">Chirias</span><ul class="ap-list">
<li>Intri direct de la intrarea blocului, fara interfon.</li>
<li>Chiria se ia la fiecare payday, o data pe ora, cat timp esti pe server: intai cash, apoi banca. Banii ajung in seiful apartamentului.</li>
<li>Seiful il deschizi doar daca proprietarul iti da acces.</li>
<li>Din apartament nu poti renunta singur la chirie. Ii ceri proprietarului sa te scoata.</li>
</ul></div>
</div>
<h2 class="ap-h2">Intretinerea</h2>
<div class="ap-card"><ul class="ap-list">
<li>Platesti din meniul proprietarului → <b>Plateste intretinerea lunara</b>, in moneda din fisa apartamentului. Acolo vezi si data scadenta.</li>
<li>Fiecare plata muta scadenta cu o perioada, pornind de la vechea scadenta. Poti plati din timp.</li>
<li>Cu 5 zile inainte de scadenta primesti un mesaj cand intri pe server, iar dupa scadenta ti se spune ca ai intarziat.</li>
<li>Dupa cateva zile de intarziere pierzi apartamentul, iar chiriasii sunt scosi.</li>
</ul></div>
<h2 class="ap-h2">Character kill (CK)</h2>
<div class="ap-two">
<div class="ap-card"><span class="ap-tag">Cumparat cu EG Coins</span><p>Apartamentul trece la noul tau caracter, cu aceeasi data de scadenta.</p></div>
<div class="ap-card"><span class="ap-tag r">Cumparat cu euro</span><p>Pierzi apartamentul. In ambele cazuri seiful se goleste, iar chiriile tale se incheie.</p></div>
</div>
</div>
