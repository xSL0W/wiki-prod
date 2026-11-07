---
outline: false
---

<style>
.hs {
  --ink: #09090b;
  --panel: #18181b;
  --panel2: #1f1f23;
  --line: #2e2e33;
  --text: #f4f4f5;
  --mute: #a1a1aa;
  --red: #ef4444;
  --red-deep: #b91c1c;
  --red-soft: rgba(239, 68, 68, 0.14);
  --lamp: #fbbf24;
  --lamp-soft: rgba(251, 191, 36, 0.14);
  --green: #4ade80;
  max-width: 960px;
  margin: 0 auto;
  color: var(--text);
  font-family: Inter, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.hs *, .hs *::before, .hs *::after { box-sizing: border-box; }
.hs p, .hs li { margin: 0; line-height: 1.6; color: var(--text); }
.hs ul, .hs ol { list-style: none; padding: 0; margin: 0; }
.hs li + li { margin-top: 0; }
.hs b { color: #fff; font-weight: 650; }
.hs a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.hs a:hover { color: #fecaca; }
.hs a:focus-visible { outline: 3px solid var(--red); outline-offset: 3px; border-radius: 6px; }
.hs kbd {
  font: inherit; font-size: 0.85em; font-weight: 700; color: #fff; background: var(--red-deep);
  border: 0; border-radius: 6px; padding: 0.05rem 0.45rem; white-space: nowrap;
}
.hs code { font-size: 0.88em; color: #fff; background: #27272a; border-radius: 6px; padding: 0.1rem 0.4rem; }
/* ---------- hero: a street at dusk ---------- */
.hs .hs-hero {
  position: relative; overflow: hidden; isolation: isolate;
  border: 1px solid var(--line); border-radius: 22px;
  background: radial-gradient(120% 90% at 85% 0%, rgba(239, 68, 68, 0.22), transparent 60%), var(--ink);
}
.hs .hs-street { display: block; width: 100%; height: auto; }
.hs .hs-hero-text { padding: clamp(1.1rem, 4vw, 2.2rem); padding-top: 0.4rem; }
.hs .hs-kicker {
  margin: 0 0 0.5rem; font: 700 0.75rem/1 ui-monospace, Menlo, Consolas, monospace;
  letter-spacing: 0.18em; text-transform: uppercase; color: var(--red);
}
.hs .hs-hero h1 {
  margin: 0 0 0.7rem; border: 0; padding: 0;
  font-size: clamp(2.1rem, 7vw, 3.5rem); line-height: 1.02; font-weight: 800; letter-spacing: -0.03em; color: #fff;
}
.hs .hs-hero h1 span { color: var(--lamp); }
.hs .hs-hero .hs-lede { max-width: 60ch; color: var(--mute); font-size: 1.05rem; }
.hs .hs-stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 0.6rem; margin-top: 1.2rem; }
.hs .hs-stats li { background: rgba(24, 24, 27, 0.9); border: 1px solid var(--line); border-radius: 14px; padding: 0.7rem 0.9rem; }
.hs .hs-stats b { display: block; font-size: clamp(1.25rem, 4vw, 1.65rem); line-height: 1.15; font-weight: 800; font-variant-numeric: tabular-nums; }
.hs .hs-stats span { display: block; margin-top: 0.2rem; color: var(--mute); font-size: 0.82rem; line-height: 1.35; }
/* svg scene */
.hs-street .sky { fill: url(#hs-sky); }
.hs-street .moon { fill: #fde68a; opacity: 0.9; }
.hs-street .star { fill: #fff; opacity: 0.3; animation: hs-twinkle 5s ease-in-out infinite; }
.hs-street .star:nth-of-type(2n) { animation-delay: -1.6s; }
.hs-street .star:nth-of-type(3n) { animation-delay: -3.1s; }
.hs-street .hill { fill: #17121a; }
.hs-street .hill2 { fill: #110e13; }
.hs-street .house { fill: #0d0d10; stroke: #2a2a31; stroke-width: 1.2; }
.hs-street .roof { fill: #141418; stroke: #2a2a31; stroke-width: 1.2; }
.hs-street .door { fill: #1d1d22; }
.hs-street .road { fill: #050506; }
.hs-street .lane { stroke: #3f3f46; stroke-width: 2; stroke-dasharray: 18 16; }
.hs-street .pole { stroke: #3f3f46; stroke-width: 2; }
.hs-street .glow { fill: url(#hs-glow); animation: hs-hum 4s ease-in-out infinite; }
.hs-street .bulb { fill: var(--lamp); }
.hs-street .sign { fill: var(--red-deep); }
.hs-street .sign-t { fill: #fff; font: 800 10px Inter, system-ui, sans-serif; letter-spacing: 0.06em; }
.hs-street .win { fill: var(--lamp); opacity: 0.08; animation: hs-lights 14s steps(1, end) infinite; }
.hs-street .d1 { animation-delay: 0s; }
.hs-street .d2 { animation-delay: -1.2s; }
.hs-street .d3 { animation-delay: -2.6s; }
.hs-street .d4 { animation-delay: -3.9s; }
.hs-street .d5 { animation-delay: -5.3s; }
.hs-street .d6 { animation-delay: -6.4s; }
.hs-street .d7 { animation-delay: -7.7s; }
.hs-street .d8 { animation-delay: -9.1s; }
.hs-street .bubble { animation: hs-bob 4s ease-in-out infinite; }
@keyframes hs-lights { 0% { opacity: 0.08; } 30% { opacity: 0.92; } 88% { opacity: 0.08; } }
@keyframes hs-twinkle { 0%, 100% { opacity: 0.15; } 50% { opacity: 0.75; } }
@keyframes hs-hum { 0%, 100% { opacity: 0.75; } 50% { opacity: 1; } }
@keyframes hs-bob { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-4px); } }
/* ---------- sections ---------- */
.hs .hs-h2 {
  display: flex; align-items: flex-start; gap: 0.65rem;
  margin: 3rem 0 0.9rem; border: 0; padding: 0;
  font-size: 1.5rem; font-weight: 750; letter-spacing: -0.015em; line-height: 1.25; color: #fff;
}
.hs .hs-h2::before { margin-top: calc(0.5lh - 0.7rem / 2);
  content: ''; flex: none; width: 0.85rem; height: 0.7rem; background: var(--red);
  clip-path: polygon(50% 0, 100% 45%, 100% 100%, 0 100%, 0 45%);
}
.hs .hs-h3 { margin: 0 0 0.35rem; border: 0; padding: 0; font-size: 1.05rem; font-weight: 700; color: #fff; line-height: 1.3; }
.hs .hs-sub { max-width: 66ch; margin-bottom: 1rem; color: var(--mute); }
.hs .hs-card { background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 1.1rem 1.2rem; }
.hs .hs-card p { color: var(--mute); font-size: 0.96rem; }
.hs .hs-card p + p { margin-top: 0.5rem; }
.hs .hs-note { margin-top: 0.85rem; color: var(--mute); font-size: 0.93rem; }
.hs .hs-callout {
  margin-top: 1rem; padding: 0.9rem 1.1rem; border-radius: 14px;
  background: var(--red-soft); border: 1px solid rgba(239, 68, 68, 0.35);
}
.hs .hs-callout p { color: #fecaca; font-size: 0.95rem; }
/* steps */
.hs .hs-steps { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 0.75rem; counter-reset: hs-step; }
.hs .hs-steps li {
  position: relative; counter-increment: hs-step;
  background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 2.6rem 1.1rem 1rem;
}
.hs .hs-steps li::before {
  content: counter(hs-step); position: absolute; top: 0.9rem; left: 1.1rem;
  width: 1.5rem; height: 1.5rem; border-radius: 50%; display: grid; place-items: center;
  font-size: 0.8rem; font-weight: 800; color: #fff; background: var(--red-deep);
}
.hs .hs-steps p { color: var(--mute); font-size: 0.94rem; }
/* address board */
.hs .hs-board { border: 1px solid var(--line); border-radius: 16px; overflow: hidden; background: var(--panel); }
.hs .hs-board li {
  display: grid; grid-template-columns: 5.2rem minmax(0, 1fr) auto; align-items: center; gap: 0.3rem 1rem;
  padding: 0.85rem 1rem; border-top: 1px solid var(--line);
}
.hs .hs-board li:first-child { border-top: 0; }
.hs .hs-board .nr {
  font: 800 0.95rem/1 ui-monospace, Menlo, Consolas, monospace; color: var(--lamp); font-variant-numeric: tabular-nums;
  background: var(--lamp-soft); border-radius: 8px; padding: 0.45rem 0.5rem; text-align: center;
}
.hs .hs-board .t { font-weight: 700; color: #fff; }
.hs .hs-board .d { display: block; color: var(--mute); font-size: 0.9rem; line-height: 1.45; }
.hs .hs-board .kg { font-size: 0.82rem; color: var(--mute); text-align: right; white-space: nowrap; }
.hs .hs-board .kg b { display: block; font-size: 0.95rem; color: #fff; }
@media (max-width: 560px) {
  .hs .hs-board li { grid-template-columns: 4.4rem minmax(0, 1fr); }
  .hs .hs-board .kg { grid-column: 2; text-align: left; }
  .hs .hs-board .nr { align-self: start; }
  .hs .hs-board .kg b { display: inline; margin-right: 0.3rem; }
}
/* rooms grid */
.hs .hs-rooms { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 0.75rem; }
.hs .hs-room { position: relative; padding-top: 3.3rem; }
.hs .hs-room svg {
  position: absolute; top: 1rem; left: 1.2rem; width: 1.75rem; height: 1.75rem;
  fill: none; stroke: var(--lamp); stroke-width: 1.8; stroke-linecap: round; stroke-linejoin: round;
}
/* maintenance timeline */
.hs .hs-time { position: relative; display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 0.7rem; }
.hs .hs-time::before {
  content: ''; position: absolute; left: 1rem; right: 1rem; top: 0.55rem; height: 3px; border-radius: 3px;
  background: linear-gradient(90deg, var(--green), var(--lamp) 55%, var(--red));
}
.hs .hs-time li { position: relative; padding-top: 1.8rem; }
.hs .hs-time li::before {
  content: ''; position: absolute; top: 0; left: 0; width: 1.15rem; height: 1.15rem; border-radius: 50%;
  background: var(--ink); border: 3px solid var(--green);
}
.hs .hs-time li:nth-child(2)::before { border-color: #a3e635; }
.hs .hs-time li:nth-child(3)::before { border-color: var(--lamp); }
.hs .hs-time li:nth-child(4)::before { border-color: var(--red); }
.hs .hs-time p { color: var(--mute); font-size: 0.92rem; }
@media (max-width: 640px) {
  .hs .hs-time { grid-template-columns: minmax(0, 1fr); gap: 1rem; }
  .hs .hs-time::before { left: 0.5rem; right: auto; top: 0.5rem; bottom: 0.5rem; width: 3px; height: auto;
    background: linear-gradient(180deg, var(--green), var(--lamp) 55%, var(--red)); }
  .hs .hs-time li { padding-top: 0; padding-left: 2rem; }
}
/* lists inside cards */
.hs .hs-list li { position: relative; padding-left: 1.1rem; color: var(--mute); font-size: 0.95rem; }
.hs .hs-list li + li { margin-top: 0.4rem; }
.hs .hs-list li::before {
  content: ''; position: absolute; left: 0; top: 0.62em; width: 0.42rem; height: 0.42rem; border-radius: 2px; background: var(--red);
}
.hs .hs-list.ok li::before { background: var(--green); }
.hs .hs-list.no li::before { background: #71717a; }
.hs .hs-card .hs-h3, .hs .hs-steps .hs-h3 { color: #fff; font-size: 1.05rem; }
.hs .hs-card .hs-list { margin-top: 0.6rem; }
.hs .hs-two { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 0.75rem; }
.hs .hs-tag {
  display: inline-block; margin-bottom: 0.45rem; font-size: 0.7rem; font-weight: 700; letter-spacing: 0.12em;
  text-transform: uppercase; color: var(--lamp);
}
.hs .hs-tag.r { color: var(--red); }
.hs .hs-sleep { background: linear-gradient(160deg, rgba(129, 140, 248, 0.14), var(--panel) 60%); border-color: #34345a; }
.hs .hs-sleep .hs-tag { color: #a5b4fc; }
@media (prefers-reduced-motion: reduce) {
  .hs .hs-street .win, .hs .hs-street .star, .hs .hs-street .glow, .hs .hs-street .bubble { animation: none; }
  .hs .hs-street .win.d1, .hs .hs-street .win.d3, .hs .hs-street .win.d4, .hs .hs-street .win.d6, .hs .hs-street .win.d8 { opacity: 0.9; }
}
</style>

<div class="hs">
<section class="hs-hero">
<svg class="hs-street" viewBox="0 0 800 270" role="img" aria-label="O strada cu case la apus: luminile din ferestre se aprind pe rand">
<defs>
<linearGradient id="hs-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0b0b12"/><stop offset="0.6" stop-color="#2a1018"/><stop offset="1" stop-color="#4a1418"/></linearGradient>
<radialGradient id="hs-glow"><stop offset="0" stop-color="#fbbf24" stop-opacity="0.55"/><stop offset="1" stop-color="#fbbf24" stop-opacity="0"/></radialGradient>
</defs>
<rect class="sky" width="800" height="270"/>
<circle class="moon" cx="668" cy="52" r="17"/>
<circle class="star" cx="60" cy="30" r="1.4"/><circle class="star" cx="140" cy="62" r="1.1"/><circle class="star" cx="232" cy="24" r="1.5"/><circle class="star" cx="318" cy="54" r="1.1"/><circle class="star" cx="410" cy="20" r="1.3"/><circle class="star" cx="502" cy="46" r="1.2"/><circle class="star" cx="590" cy="22" r="1.4"/><circle class="star" cx="742" cy="78" r="1.2"/>
<path class="hill" d="M0 160 C120 118 230 140 330 124 C440 106 560 138 650 118 C720 104 770 116 800 112 L800 270 L0 270 Z"/>
<path class="hill2" d="M0 182 C150 160 260 176 400 166 C540 156 660 178 800 160 L800 270 L0 270 Z"/>
<rect class="house" x="28" y="150" width="150" height="62"/>
<rect class="roof" x="22" y="142" width="162" height="10"/>
<rect class="win d1" x="40" y="162" width="18" height="14"/><rect class="win d4" x="68" y="162" width="18" height="14"/><rect class="win d7" x="96" y="162" width="18" height="14"/><rect class="win d2" x="124" y="162" width="18" height="14"/><rect class="win d5" x="152" y="162" width="18" height="14"/>
<rect class="win d8" x="40" y="186" width="18" height="14"/><rect class="win d3" x="96" y="186" width="18" height="14"/><rect class="win d6" x="152" y="186" width="18" height="14"/>
<rect class="sign" x="62" y="122" width="88" height="17" rx="3"/><text class="sign-t" x="106" y="134" text-anchor="middle">MOTEL</text>
<path class="roof" d="M206 166 L250 132 L294 166 Z"/>
<rect class="house" x="212" y="166" width="76" height="46"/>
<rect class="win d3" x="222" y="176" width="16" height="14"/><rect class="win d6" x="262" y="176" width="16" height="14"/>
<rect class="door" x="243" y="190" width="14" height="22"/>
<g class="bubble"><rect x="214" y="98" width="72" height="22" rx="11" fill="#18181b" stroke="#b91c1c" stroke-width="1.5"/><text x="250" y="113" text-anchor="middle" fill="#fff" font-family="Inter, system-ui, sans-serif" font-size="10" font-weight="700">Casa nr. 16</text></g>
<rect class="house" x="324" y="150" width="120" height="62"/>
<rect class="roof" x="318" y="144" width="132" height="8"/>
<rect class="house" x="352" y="122" width="72" height="24"/>
<rect class="win d1" x="362" y="128" width="52" height="12"/>
<rect class="win d5" x="334" y="162" width="40" height="18"/><rect class="win d8" x="394" y="162" width="40" height="18"/>
<rect class="door" x="377" y="188" width="14" height="24"/>
<path class="roof" d="M478 168 L512 140 L546 168 Z"/>
<rect class="house" x="484" y="168" width="56" height="44"/>
<rect class="win d2" x="494" y="178" width="14" height="12"/><rect class="win d7" x="516" y="178" width="14" height="12"/>
<path class="roof" d="M574 160 L630 120 L686 160 Z"/>
<rect class="house" x="580" y="160" width="100" height="52"/>
<rect class="win d4" x="592" y="170" width="18" height="16"/><rect class="win d6" x="650" y="170" width="18" height="16"/>
<rect class="door" x="622" y="188" width="16" height="24"/>
<rect class="house" x="706" y="172" width="70" height="40"/>
<rect class="roof" x="700" y="166" width="82" height="8"/>
<rect class="win d5" x="716" y="182" width="20" height="12"/><rect class="win d1" x="746" y="182" width="20" height="12"/>
<line class="pole" x1="196" y1="214" x2="196" y2="168"/><circle class="glow" cx="196" cy="168" r="24"/><circle class="bulb" cx="196" cy="168" r="3"/>
<line class="pole" x1="462" y1="214" x2="462" y2="168"/><circle class="glow" cx="462" cy="168" r="24"/><circle class="bulb" cx="462" cy="168" r="3"/>
<line class="pole" x1="694" y1="214" x2="694" y2="168"/><circle class="glow" cx="694" cy="168" r="24"/><circle class="bulb" cx="694" cy="168" r="3"/>
<rect class="road" x="0" y="212" width="800" height="58"/>
<line class="lane" x1="0" y1="242" x2="800" y2="242"/>
</svg>
<div class="hs-hero-text">
<p class="hs-kicker">Proprietati</p>
<h1>Case <span>in Los Santos</span></h1>
<p class="hs-lede">Cumperi casa de la agentul imobiliar, o pastrezi platind intretinerea si o imparti cu chiriasii tai. In casa ai seif, garderoba si un pat in care dormi cand iei pauza.</p>
<ul class="hs-stats">
<li><b>40</b><span>case, de la camere de motel la vile</span></li>
<li><b>EUR / Coins</b><span>fiecare casa se vinde intr-una din monede</span></li>
<li><b>1.000-10.000 kg</b><span>seiful casei, in functie de casa</span></li>
</ul>
</div>
</section>
<h2 class="hs-h2">Cum cumperi o casa</h2>
<p class="hs-sub">Toate casele se cumpara de la <b>Emilio Corso</b>, agentul imobiliar de langa primarie. Pe harta il gasesti ca <b>Agent imobiliar Emilio Corso</b>.</p>
<ol class="hs-steps">
<li><p class="hs-h3">Vorbeste cu agentul</p><p>Mergi la Emilio Corso si apasa <kbd>E</kbd>. Daca nicio casa nu e de vanzare, agentul iti spune pe loc.</p></li>
<li><p class="hs-h3">Alege moneda</p><p><b>Case cu EURO</b> sau <b>Case cu EG Coins</b>. Langa fiecare vezi cate case sunt libere acum.</p></li>
<li><p class="hs-h3">Citeste fisa casei</p><p>Pretul, intretinerea, cat incape in seif si cati chiriasi poti avea. Daca e o casa care poate fi jefuita, scrie in fisa.</p></li>
<li><p class="hs-h3">Mergi s-o vezi</p><p><b>Vezi locatia pe GPS</b> iti pune un punct pe harta, la intrarea casei.</p></li>
<li><p class="hs-h3">Cumpara</p><p>Confirmi, iar banii se iau din cont: euro din banca sau EG Coins. Primesti <b>Contractul de vanzare-cumparare</b> si usile casei se deschid pentru tine.</p></li>
</ol>
<p class="hs-note">Preturile si intretinerea se schimba in timp, asa ca le vezi doar la agent, in joc.</p>
<h2 class="hs-h2">Unde sunt casele</h2>
<p class="hs-sub">Pe harta, casele au iconita verde <b>Casa</b>. La usa fiecareia apare eticheta <b>Casa nr. X</b>, numarul pe care il vezi si la agent.</p>
<ul class="hs-board">
<li><span class="nr">1-14</span><span><span class="t">Motelul Pink Cage</span><span class="d">Paisprezece camere de motel pe Hawick Avenue.</span></span><span class="kg"><b>1.000 kg</b>seif</span></li>
<li><span class="nr">15</span><span><span class="t">Rockford Hills</span><span class="d">Casa lui Michael.</span></span><span class="kg"><b>2.000 kg</b>seif</span></li>
<li><span class="nr">16</span><span><span class="t">Forum Drive</span><span class="d">Casa lui Franklin din Strawberry.</span></span><span class="kg"><b>1.500 kg</b>seif</span></li>
<li><span class="nr">17-22</span><span><span class="t">Mirror Park</span><span class="d">Sase case de familie in cartierul de langa lac.</span></span><span class="kg"><b>1.250-1.500 kg</b>seif</span></li>
<li><span class="nr">23-41</span><span><span class="t">Vile</span><span class="d">Vinewood Hills, Richman si dealurile din nord, plus cateva locuri aparte: podgoria din Tongva Valley (29), farul de la El Gordo (33) si ferma La Fuente Blanca (38).</span></span><span class="kg"><b>2.000-10.000 kg</b>seif</span></li>
</ul>
<h2 class="hs-h2">Ce ai in casa</h2>
<div class="hs-rooms">
<div class="hs-card hs-room"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="12" cy="12" r="3.5"/><path d="M12 8.5v-1M15.5 12h1M12 15.5v1M8.5 12h-1M7 20v1.5M17 20v1.5"/></svg><p class="hs-h3">Seiful</p><p>Stai langa seif, apasa <kbd>G</kbd> si alege <b>Deschide seiful</b>. Il deschizi tu si chiriasii carora le dai acces.</p><p>Tot aici intra, in bani cash, chiria platita de chiriasi.</p></div>
<div class="hs-card hs-room"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 4a3 3 0 0 0 6 0l4 2.5-1.5 4-2-1V20H8.5V9.5l-2 1L5 6.5Z"/></svg><p class="hs-h3">Garderoba</p><p>La garderoba apesi <kbd>E</kbd> si iti schimbi tinuta cu una din cele salvate.</p></div>
<div class="hs-card hs-room"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 11 12 4l9 7"/><path d="M5 10v10h14V10"/><path d="M9 14h6M9 17h4"/></svg><p class="hs-h3">Meniul proprietarului</p><p>La punctul din casa apesi <kbd>E</kbd> pe <b>Deschide meniul proprietarului</b>. De aici gestionezi chiriasii si platesti intretinerea.</p></div>
<div class="hs-card hs-room"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="3" width="14" height="18" rx="1.5"/><circle cx="15" cy="12" r="1.2"/></svg><p class="hs-h3">Usile</p><p>Usile casei le descui cu <kbd>E</kbd> doar tu si chiriasii tai. Cand pierzi casa sau chiria, pierzi si accesul la usi.</p></div>
<div class="hs-card hs-room"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="7" y="2.5" width="10" height="19" rx="2"/><path d="M11 18.5h2"/></svg><p class="hs-h3">Telefon → Case</p><p>Vezi casele pe care le detii sau le inchiriezi. Ca proprietar, incui si descui usile de oriunde si dai sau iei cheile (chiriasii).</p></div>
</div>
<h2 class="hs-h2">Intretinerea</h2>
<p class="hs-sub">Casa ramane a ta cat timp platesti intretinerea. O platesti din meniul proprietarului, la <b>Plateste intretinerea lunara</b>, in moneda scrisa in fisa casei. Acolo vezi si data scadenta.</p>
<ol class="hs-time">
<li><p class="hs-h3">Cumperi casa</p><p>Prima scadenta pleaca din ziua cumpararii.</p></li>
<li><p class="hs-h3">Platesti din timp</p><p>Fiecare plata muta scadenta cu o perioada, pornind de la vechea scadenta, nu de azi.</p></li>
<li><p class="hs-h3">Se apropie scadenta</p><p>Cu 5 zile inainte, primesti un mesaj cand intri pe server. Dupa scadenta, mesajul iti spune ca ai intarziat.</p></li>
<li><p class="hs-h3">Evacuare</p><p>Dupa cateva zile de intarziere pierzi casa. Chiriasii sunt scosi si ei.</p></li>
</ol>
<p class="hs-note">O casa luata pentru neplata nu intra singura inapoi la vanzare. O repune in vanzare staff-ul.</p>
<h2 class="hs-h2">Chiriasi</h2>
<div class="hs-two">
<div class="hs-card"><span class="hs-tag">Proprietar</span><p class="hs-h3">Iti iei chiriasi</p><ul class="hs-list">
<li>Meniul proprietarului → <b>Gestioneaza chiriasi</b> → <b>Adauga chirias nou</b>.</li>
<li>Jucatorul trebuie sa fie langa tine, la cel mult 5 metri.</li>
<li>Stabilesti chiria pe ora, in limitele serverului. Cati chiriasi incap scrie in fisa casei.</li>
<li>Pentru fiecare chirias vezi ultima plata sau <b>Plata esuata</b>, cu data.</li>
<li>Poti schimba chiria, poti da sau lua accesul la seif si poti scoate chiriasul. El primeste mesaj de fiecare data.</li>
</ul></div>
<div class="hs-card"><span class="hs-tag r">Chirias</span><p class="hs-h3">Platesti chiria</p><ul class="hs-list">
<li>Chiria se ia la fiecare payday, o data pe ora, cat timp esti pe server.</li>
<li>Se ia intai din cash, apoi din banca, si ajunge in seiful casei.</li>
<li>Daca nu ai bani, primesti mesaj, iar proprietarul vede plata esuata.</li>
<li>Intri in casa si dormi in ea, dar seiful il deschizi doar daca proprietarul iti da acces.</li>
<li>Ca sa renunti, stai in casa si scrie <code>/leavehouse</code> sau <kbd>K</kbd> → Jucator → Casa → <b>Renunta la chirie</b>. Banii platiti nu se returneaza.</li>
</ul></div>
</div>
<h2 class="hs-h2">Dormit si AFK</h2>
<div class="hs-two">
<div class="hs-card hs-sleep"><span class="hs-tag">/sleep</span><p class="hs-h3">Dormi in casa ta</p><p>In casa pe care o detii sau o inchiriezi scrii <code>/sleep</code> sau alegi <kbd>K</kbd> → Jucator → Casa → <b>Dormi</b>. Scrii <code>/sleep</code> din nou ca sa te trezesti.</p><ul class="hs-list ok">
<li>Orele jucate se aduna complet.</li>
<li>Foamea si setea nu scad.</li>
<li>Nu platesti taxele de la payday.</li>
</ul><ul class="hs-list no">
<li>Nu primesti salarii: job, factiune, VIP.</li>
<li>Iesi din tura si revii in ea la trezire, daca ai acelasi job.</li>
<li>Chiria se plateste in continuare.</li>
</ul></div>
<div class="hs-card"><span class="hs-tag r">AFK</span><p class="hs-h3">Stai pe loc fara sa dormi</p><ul class="hs-list">
<li>Dupa 5 minute fara sa te misti sau sa vorbesti, primesti un avertisment.</li>
<li>La 10 minute esti marcat AFK: nu mai aduni ore jucate si iesi din tura.</li>
<li>Vorbitul conteaza doar daca e un alt jucator la cel mult 15 metri de tine.</li>
<li>Revii cand te misti sau vorbesti.</li>
</ul></div>
</div>
<div class="hs-callout"><p><b>Atentie:</b> <code>/e sleep</code> e doar o animatie. Ca sa dormi de-adevaratelea si sa aduni orele, foloseste <code>/sleep</code>.</p></div>
<h2 class="hs-h2">Jafuri</h2>
<div class="hs-two">
<div class="hs-card"><span class="hs-tag">12 vile de lux</span><p>Cat timp au proprietar, nu pot fi jefuite.</p></div>
<div class="hs-card"><span class="hs-tag r">7 case obisnuite</span><p>Pot fi jefuite chiar daca sunt ale cuiva. Hotii iau ce gasesc prin casa, nu ce ai tu in seif.</p></div>
</div>
<p class="hs-note">Agentul iti arata in fisa daca o casa face parte din jafuri. Detalii despre jaf: <a href="/joburi/jafuricase">Jaf la case</a>.</p>
<h2 class="hs-h2">Character kill (CK)</h2>
<div class="hs-two">
<div class="hs-card"><span class="hs-tag">Cumparata cu EG Coins</span><p>Casa trece la noul tau caracter, cu aceeasi data de scadenta.</p></div>
<div class="hs-card"><span class="hs-tag r">Cumparata cu euro</span><p>Pierzi casa. In ambele cazuri seiful se goleste, iar chiriile tale se incheie.</p></div>
</div>
</div>
