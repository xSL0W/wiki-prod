---
outline: false
---

<style>
.alg {
  --ink: #0b0b0d;
  --panel: #151517;
  --panel2: #1d1d20;
  --line: #2f2f35;
  --text: #f4f4f5;
  --mute: #a1a1aa;
  --red: #dc2626;
  --red2: #ef4444;
  --amber: #f59e0b;
  --fire: #fb923c;
  --carbon: repeating-linear-gradient(45deg, rgba(255, 255, 255, 0.022) 0 2px, transparent 2px 6px), repeating-linear-gradient(-45deg, rgba(0, 0, 0, 0.28) 0 2px, transparent 2px 6px), #111113;
  max-width: 980px;
  margin: 0 auto;
  color: var(--text);
}
.alg *, .alg *::before, .alg *::after { box-sizing: border-box; }
.alg p, .alg li { margin: 0; line-height: 1.6; color: var(--text); }
.alg ul, .alg ol { list-style: none; padding: 0; margin: 0; }
.alg li + li { margin-top: 0; }
.alg b { color: #fff; font-weight: 650; }
.alg kbd {
  display: inline-block; min-width: 1.6em; padding: 0.05rem 0.45rem; border-radius: 6px; text-align: center;
  font: 700 0.82em ui-monospace, Menlo, Consolas, monospace; color: #fff;
  background: var(--panel2); border: 1px solid var(--line); border-bottom-width: 3px;
}
.alg a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.alg a:hover { color: #fed7aa; }
.alg a:focus-visible { outline: 3px solid var(--amber); outline-offset: 3px; border-radius: 6px; }
/* group nav (shared by the Tuning pages) */
.alg .alg-group { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1rem; }
.alg .alg-group a {
  display: inline-flex; align-items: center; gap: 0.55rem; text-decoration: none; color: var(--mute);
  background: var(--panel); border: 1px solid var(--line); border-radius: 10px; padding: 0.35rem 0.85rem 0.35rem 0.4rem;
  font-weight: 700; font-size: 0.9rem;
}
.alg .alg-group a span { font: 800 0.75rem ui-monospace, Menlo, Consolas, monospace; color: var(--ink); background: var(--mute); border-radius: 6px; padding: 0.1rem 0.35rem; }
.alg .alg-group a:hover { color: #fff; border-color: var(--red); }
.alg .alg-group a[aria-current="page"] { color: #fff; border-color: var(--red); background: rgba(220, 38, 38, 0.12); }
.alg .alg-group a[aria-current="page"] span { background: var(--red); color: #fff; }
/* hero */
.alg .alg-hero {
  position: relative; overflow: hidden; border: 1px solid var(--line); border-radius: 22px;
  background: radial-gradient(70% 100% at 20% 60%, rgba(251, 146, 60, 0.2), transparent 62%), var(--carbon);
  padding: clamp(1.25rem, 4vw, 2.4rem); padding-top: calc(clamp(1.25rem, 4vw, 2.4rem) + 12px);
  display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 300px), 1fr)); gap: 1.5rem; align-items: center;
}
.alg .alg-hero::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 12px;
  background: conic-gradient(#e4e4e7 0 25%, #0b0b0d 0 50%, #e4e4e7 0 75%, #0b0b0d 0) 0 0 / 12px 12px; opacity: 0.85;
}
.alg .alg-kicker { font: 800 0.75rem ui-monospace, Menlo, Consolas, monospace; letter-spacing: 0.16em; text-transform: uppercase; color: var(--fire); margin-bottom: 0.6rem; }
.alg .alg-hero h1 {
  margin: 0 0 0.8rem; border: 0; padding: 0; font-style: italic;
  font-size: clamp(2.4rem, 8vw, 3.6rem); line-height: 1; font-weight: 900; letter-spacing: -0.035em; color: #fff;
}
.alg .alg-lede { color: var(--mute); font-size: 1.05rem; max-width: 46ch; }
.alg .alg-tags { display: flex; flex-wrap: wrap; gap: 0.45rem; margin-top: 1.1rem; }
.alg .alg-tags li { font: 700 0.8rem ui-monospace, Menlo, Consolas, monospace; text-transform: uppercase; letter-spacing: 0.06em; color: var(--fire); border: 1px solid rgba(251, 146, 60, 0.45); border-radius: 999px; padding: 0.15rem 0.7rem; }
.alg .alg-art { display: block; width: 100%; max-width: 420px; height: auto; margin: 0 auto; }
.alg-art .bumper { fill: #1c1c20; stroke: #e4e4e7; stroke-width: 2.2; stroke-linejoin: round; }
.alg-art .diffuser { fill: #0b0b0d; stroke: #3f3f46; stroke-width: 1.5; }
.alg-art .tip { fill: #3f3f46; stroke: #d4d4d8; stroke-width: 2; }
.alg-art .hole { fill: #050506; }
.alg-art .light { fill: var(--red); opacity: 0.9; }
.alg-art .flame { transform-box: fill-box; transform-origin: right center; transform: scaleX(0); }
.alg-art .flame.outer { fill: var(--fire); animation: alg-burst 2.6s ease-out infinite, alg-hue 18.2s steps(1) infinite; }
.alg-art .flame.inner { fill: #fef3c7; animation: alg-burst 2.6s ease-out infinite; }
.alg-art .flame.b { animation-delay: 0.12s, 0.12s; }
.alg-art .ring { fill: none; stroke: #fde68a; stroke-width: 2; transform-box: fill-box; transform-origin: center; opacity: 0; animation: alg-ring 2.6s ease-out infinite; }
.alg-art .ring.d2 { animation-delay: 0.35s; }
.alg-art .ring.d3 { animation-delay: 0.7s; }
.alg-art .spark { fill: #fde68a; opacity: 0; animation: alg-spark 2.6s ease-out infinite; }
.alg-art .spark.s2 { animation-delay: 0.2s; }
.alg-art .spark.s3 { animation-delay: 0.45s; }
@keyframes alg-burst {
  0%, 8% { transform: scaleX(0); opacity: 0; }
  12% { transform: scaleX(1); opacity: 1; }
  18% { transform: scaleX(0.35); opacity: 0.8; }
  24% { transform: scaleX(0.95); opacity: 1; }
  30% { transform: scaleX(0.3); opacity: 0.7; }
  36% { transform: scaleX(0.85); opacity: 1; }
  48%, 100% { transform: scaleX(0); opacity: 0; }
}
@keyframes alg-hue {
  0% { fill: #ff7814; } 14.28% { fill: #286eff; } 28.57% { fill: #28ff50; } 42.85% { fill: #aa32ff; }
  57.14% { fill: #ff1414; } 71.42% { fill: #ff3cb4; } 85.71% { fill: #f4f4f5; }
}
@keyframes alg-ring { 0%, 10% { opacity: 0; transform: scale(0.3); } 14% { opacity: 1; } 40%, 100% { opacity: 0; transform: scale(2.4); } }
@keyframes alg-spark { 0%, 12% { opacity: 0; transform: translate(0, 0); } 16% { opacity: 1; } 42%, 100% { opacity: 0; transform: translate(-70px, -26px); } }
/* section heads */
.alg .alg-h2 {
  display: flex; align-items: flex-start; gap: 0.7rem; margin: 3rem 0 0.9rem; line-height: 32px; border: 0; padding: 0;
  font-size: 1.45rem; font-weight: 850; letter-spacing: -0.015em; color: #fff; font-style: italic;
}
.alg .alg-h2 span { flex: none; font: 800 0.8rem ui-monospace, Menlo, Consolas, monospace; font-style: normal; color: #fff; background: var(--red); border-radius: 6px; padding: 0.15rem 0.45rem; transform: skewX(-10deg); margin-top: 6px; }
.alg .alg-sub { color: var(--mute); margin: -0.3rem 0 1rem; max-width: 66ch; }
.alg .alg-card { background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 1rem 1.15rem; }
.alg .alg-card h3 { margin: 0 0 0.45rem; border: 0; padding: 0; font-size: 1.02rem; font-weight: 800; color: #fff; }
.alg .alg-card p { color: var(--mute); font-size: 0.95rem; }
.alg .alg-card p + p { margin-top: 0.5rem; }
/* needs */
.alg .alg-needs { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 220px), 1fr)); gap: 0.7rem; }
.alg .alg-needs li { position: relative; background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 1rem 1.1rem 1rem 3.3rem; color: var(--mute); font-size: 0.95rem; }
.alg .alg-needs li::before {
  content: ''; position: absolute; left: 1rem; top: 1.05rem; width: 1.5rem; height: 1.5rem; border-radius: 50%;
  background: radial-gradient(circle, var(--ink) 0 35%, transparent 36%), var(--fire);
}
.alg .alg-needs li b { display: block; color: #fff; font-size: 1rem; }
/* install timeline */
.alg .alg-line { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 200px), 1fr)); gap: 0; border: 1px solid var(--line); border-radius: 14px; overflow: hidden; background: var(--panel); }
/* dividers as outer shadows: the outermost ones fall on the list border, so any column count works */
.alg .alg-line li { padding: 1rem 1.1rem; color: var(--mute); font-size: 0.94rem; box-shadow: 1px 0 0 var(--line), 0 1px 0 var(--line); }
.alg .alg-line li i { display: block; font: 900 1.6rem/1 ui-monospace, Menlo, Consolas, monospace; font-style: italic; color: var(--fire); margin-bottom: 0.4rem; }
.alg .alg-line li b { display: block; color: #fff; }
.alg .alg-bar { position: relative; height: 10px; margin-top: 0.7rem; border-radius: 3px; background: var(--panel2); overflow: hidden; }
.alg .alg-bar::after { content: ''; position: absolute; inset: 0; background: linear-gradient(90deg, var(--red), var(--fire)); transform-origin: left; animation: alg-load 10s linear infinite; }
@keyframes alg-load { from { transform: scaleX(0); } to { transform: scaleX(1); } }
.alg .alg-barlbl { display: flex; justify-content: space-between; margin-top: 0.3rem; font: 700 0.75rem ui-monospace, Menlo, Consolas, monospace; color: var(--mute); }
/* vehicle menu mock */
.alg .alg-panel { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 270px), 1fr)); gap: 0.7rem; padding: 0.8rem; border: 1px solid var(--line); border-radius: 18px; background: var(--carbon); }
.alg .alg-toggle { display: flex; gap: 0.9rem; align-items: flex-start; }
.alg .alg-toggle .sw { flex: none; width: 2.6rem; height: 1.45rem; margin-top: 0.15rem; border-radius: 999px; background: var(--red); position: relative; }
.alg .alg-toggle .sw::after { content: ''; position: absolute; top: 0.2rem; right: 0.2rem; width: 1.05rem; height: 1.05rem; border-radius: 50%; background: #fff; }
.alg .alg-swatches { display: flex; flex-wrap: wrap; gap: 0.45rem; margin-top: 0.4rem; }
.alg .alg-swatches li { display: flex; align-items: center; gap: 0.4rem; font-size: 0.85rem; color: var(--mute); background: var(--panel2); border: 1px solid var(--line); border-radius: 999px; padding: 0.15rem 0.65rem 0.15rem 0.25rem; }
.alg .alg-swatches li::before { content: ''; width: 1rem; height: 1rem; border-radius: 50%; background: var(--c); box-shadow: 0 0 10px var(--c); }
.alg .alg-styles { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-top: 0.4rem; }
.alg .alg-styles li { font-weight: 700; font-size: 0.88rem; border: 1px solid var(--line); border-radius: 8px; padding: 0.15rem 0.7rem; background: var(--panel2); }
.alg .alg-styles li:first-child { border-color: var(--fire); color: var(--fire); }
/* telemetry */
.alg .alg-tele { border: 1px solid var(--line); border-radius: 14px; overflow: hidden; }
.alg .alg-tele li { display: grid; grid-template-columns: minmax(0, 1.4fr) 5.5rem minmax(0, 1fr); gap: 0.8rem; align-items: center; padding: 0.7rem 1rem; background: var(--panel); }
.alg .alg-tele li + li { border-top: 1px solid var(--line); }
.alg .alg-tele li.head { background: var(--panel2); font: 700 0.72rem ui-monospace, Menlo, Consolas, monospace; text-transform: uppercase; letter-spacing: 0.1em; color: var(--mute); }
.alg .alg-tele .rpm { height: 8px; border-radius: 2px; background: #27272a; overflow: hidden; }
.alg .alg-tele .rpm span { display: block; height: 100%; width: var(--r); background: linear-gradient(90deg, var(--amber), var(--red)); }
.alg .alg-tele .fx { color: var(--fire); font-weight: 700; font-size: 0.92rem; }
.alg .alg-tele .what { font-size: 0.94rem; }
/* launch */
.alg .alg-launch { display: grid; grid-template-columns: auto 1fr; gap: 1.2rem; align-items: center; background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 1.1rem 1.2rem; }
.alg .alg-tree { display: grid; gap: 0.35rem; padding: 0.6rem; background: #0b0b0d; border: 1px solid var(--line); border-radius: 12px; }
.alg .alg-tree i { display: block; width: 1.3rem; height: 1.3rem; border-radius: 50%; background: #27272a; }
.alg .alg-tree i.y1 { animation: alg-amber 3s infinite; }
.alg .alg-tree i.y2 { animation: alg-amber 3s 0.4s infinite; }
.alg .alg-tree i.y3 { animation: alg-amber 3s 0.8s infinite; }
.alg .alg-tree i.g { animation: alg-green 3s 1.2s infinite; }
@keyframes alg-amber { 0%, 100% { background: #27272a; box-shadow: none; } 5%, 35% { background: var(--amber); box-shadow: 0 0 12px var(--amber); } 40% { background: #27272a; box-shadow: none; } }
@keyframes alg-green { 0%, 100% { background: #27272a; box-shadow: none; } 5%, 30% { background: #22c55e; box-shadow: 0 0 14px #22c55e; } 35% { background: #27272a; box-shadow: none; } }
.alg .alg-launch ul li { position: relative; padding: 0.4rem 0 0.4rem 1.2rem; color: var(--mute); }
.alg .alg-launch ul li + li { border-top: 1px solid var(--line); }
.alg .alg-launch ul li::before { content: ''; position: absolute; left: 0; top: 0.9rem; width: 8px; height: 8px; background: var(--fire); transform: skewX(-15deg); }
.alg .alg-launch ul li b { color: #fff; }
.alg .alg-warn { border-left: 4px solid var(--amber); }
.alg .alg-warn ul li { position: relative; padding: 0.4rem 0 0.4rem 1.2rem; color: var(--mute); }
.alg .alg-warn ul li + li { border-top: 1px solid var(--line); }
.alg .alg-warn ul li::before { content: '!'; position: absolute; left: 0; top: 0.4rem; font-weight: 900; color: var(--amber); }
.alg .alg-foot { margin-top: 2.5rem; padding: 1rem 1.2rem; border: 1px dashed var(--line); border-radius: 14px; color: var(--mute); }
@media (max-width: 560px) {
  .alg .alg-tele li { grid-template-columns: 1fr 4.5rem; }
  .alg .alg-tele li .fx { grid-column: 1 / -1; }
  .alg .alg-tele li.head span:last-child { display: none; }
  .alg .alg-launch { grid-template-columns: 1fr; }
  .alg .alg-tree { grid-auto-flow: column; justify-content: start; justify-self: start; }
}
@media (prefers-reduced-motion: reduce) {
  .alg-art .flame, .alg-art .ring, .alg-art .spark, .alg .alg-bar::after, .alg .alg-tree i { animation: none; }
  .alg-art .flame { transform: scaleX(0.85); }
  .alg .alg-bar::after { transform: scaleX(1); }
  .alg .alg-tree i.g { background: #22c55e; }
}
</style>
<div class="alg">
<nav class="alg-group" aria-label="Pagini tuning">
<a href="/general/tuning"><span>01</span>Tuning</a>
<a href="/general/antilag" aria-current="page"><span>02</span>Antilag</a>
<a href="/general/offroad"><span>03</span>Offroad</a>
</nav>
<section class="alg-hero">
<div>
<p class="alg-kicker">Piesa premium · Evacuare</p>
<h1>Antilag</h1>
<p class="alg-lede">Pops & bangs si flacari colorate pe evacuare. Pocnesc cand iei piciorul de pe acceleratie, cand schimbi treapta si la limitator. Le vad si le aud toti jucatorii din jur.</p>
<ul class="alg-tags"><li>Necesita turbo</li><li>7 culori</li><li>4 stiluri</li><li>2-Step</li></ul>
</div>
<svg class="alg-art" viewBox="0 0 420 200" role="img" aria-label="Spatele unei masini: din doua evacuari ies flacari in rafale, in culori diferite">
<path class="flame outer" d="M262 118 Q190 98 96 116 Q150 118 120 126 Q190 140 262 132 Z"/>
<path class="flame inner" d="M262 121 Q214 112 160 120 Q214 130 262 129 Z"/>
<path class="flame outer b" d="M262 152 Q196 136 112 150 Q160 154 134 160 Q196 172 262 166 Z"/>
<path class="flame inner b" d="M262 155 Q218 147 172 154 Q218 164 262 163 Z"/>
<circle class="ring" cx="244" cy="125" r="14"/>
<circle class="ring d2" cx="244" cy="159" r="14"/>
<circle class="ring d3" cx="232" cy="142" r="18"/>
<circle class="spark" cx="236" cy="118" r="2.2"/>
<circle class="spark s2" cx="236" cy="166" r="2"/>
<circle class="spark s3" cx="230" cy="140" r="1.8"/>
<path class="bumper" d="M262 60 L380 52 Q404 52 408 76 L412 168 Q412 186 392 186 L262 186 Z"/>
<path class="diffuser" d="M262 150 L330 150 L340 186 L262 186 Z"/>
<rect class="light" x="372" y="66" width="30" height="12" rx="3"/>
<rect x="262" y="96" width="140" height="6" fill="#3f3f46"/>
<ellipse class="tip" cx="262" cy="125" rx="9" ry="14"/>
<ellipse class="hole" cx="262" cy="125" rx="5" ry="9"/>
<ellipse class="tip" cx="262" cy="159" rx="9" ry="14"/>
<ellipse class="hole" cx="262" cy="159" rx="5" ry="9"/>
</svg>
</section>
<h2 class="alg-h2"><span>01</span>Ce iti trebuie</h2>
<ul class="alg-needs">
<li><b>Item-ul Antilag</b>Il iei din <a href="/zona-info/store">Magazin</a>, cu EG Coins. Nu il poti da altcuiva, arunca sau vinde in Piata.</li>
<li><b>Turbina montata</b>Fara turbina nu poti monta antilag. O pui la <a href="/general/tuning">Tuning</a>, la Performanta.</li>
<li><b>Masina ta, tu la volan</b>Montezi doar pe o masina personala, din scaunul soferului. O masina primeste un singur antilag.</li>
</ul>
<h2 class="alg-h2"><span>02</span>Montare</h2>
<ol class="alg-line">
<li><i>1</i><b>Urca la volan</b>In masina pe care vrei antilag-ul.</li>
<li><i>2</i><b>Foloseste item-ul</b>Il folosesti din inventar, cat stai la volan.</li>
<li><i>3</i><b>Asteapta 10 secunde</b>Item-ul se consuma, iar antilag-ul ramane pe masina si dupa ce o bagi in garaj.</li>
</ol>
<div class="alg-bar" aria-hidden="true"></div>
<div class="alg-barlbl" aria-hidden="true"><span>0 s</span><span>10 s</span></div>
<h2 class="alg-h2"><span>03</span>Meniul vehiculului</h2>
<p class="alg-sub">Apasa <kbd>O</kbd> la volan si deschide tab-ul <b>Antilag</b>. Apare doar pe masinile care il au montat. Tot ce alegi aici se salveaza pe masina.</p>
<div class="alg-panel">
<div class="alg-card">
<div class="alg-toggle"><span class="sw" aria-hidden="true"></span><div><h3>Flacari</h3><p>Flacari pe evacuare cand iei piciorul de pe acceleratie la turatie mare, la schimbarea treptei si la limitator.</p></div></div>
</div>
<div class="alg-card">
<div class="alg-toggle"><span class="sw" aria-hidden="true"></span><div><h3>Pops & bangs</h3><p>Pocnituri in aceleasi momente, plus pocnitura de pornire si crackle-ul la ralanti.</p></div></div>
</div>
<div class="alg-card">
<h3>Culoare flacari</h3>
<ul class="alg-swatches">
<li style="--c:#ff7814">Portocaliu</li>
<li style="--c:#286eff">Albastru</li>
<li style="--c:#28ff50">Verde</li>
<li style="--c:#aa32ff">Mov</li>
<li style="--c:#ff1414">Rosu</li>
<li style="--c:#ff3cb4">Roz</li>
<li style="--c:#ffffff">Alb</li>
</ul>
</div>
<div class="alg-card">
<h3>Stil pops & bangs</h3>
<ul class="alg-styles"><li>Mix</li><li>Usor</li><li>Agresiv</li><li>Crackle</li></ul>
<p style="margin-top:0.5rem">Cand alegi un stil nou, auzi pe loc cum suna.</p>
</div>
</div>
<h2 class="alg-h2"><span>04</span>Cand pocneste</h2>
<ul class="alg-tele">
<li class="head"><span>Ce faci</span><span>Turatie</span><span>Ce iese</span></li>
<li><span class="what">Iei piciorul de pe acceleratie</span><span class="rpm"><span style="--r:70%"></span></span><span class="fx">Rafala de pocnituri si flacari</span></li>
<li><span class="what">Schimbi treapta in sus sau in jos</span><span class="rpm"><span style="--r:58%"></span></span><span class="fx">Cateva pocnituri</span></li>
<li><span class="what">Tii motorul la limitator</span><span class="rpm"><span style="--r:98%"></span></span><span class="fx">Pocnituri repetate</span></li>
<li><span class="what">Tii acceleratia la maxim</span><span class="rpm"><span style="--r:80%"></span></span><span class="fx">Crackle continuu</span></li>
<li><span class="what">Stai pe loc sau rulezi incet, sub ~40 km/h, fara acceleratie</span><span class="rpm"><span style="--r:20%"></span></span><span class="fx">Crackle la ralanti</span></li>
<li><span class="what">Pornesti motorul</span><span class="rpm"><span style="--r:12%"></span></span><span class="fx">Pocnitura de pornire</span></li>
</ul>
<h2 class="alg-h2"><span>05</span>2-Step si Launch Control</h2>
<div class="alg-launch">
<div class="alg-tree" aria-hidden="true"><i class="y1"></i><i class="y2"></i><i class="y3"></i><i class="g"></i></div>
<ul>
<li><b>2-Step:</b> stai pe loc, tii <b>frana de mana</b> si <b>acceleratia la maxim</b>. Masina pocneste rapid si scoate flacari, ca un limitator de lansare.</li>
<li><b>Launch Control:</b> dupa cel putin <b>1 secunda</b> de 2-Step, lasa frana de mana si tine acceleratia la maxim. Primesti un boost de putere de <b>1,5 secunde</b> la plecare.</li>
<li>Launch Control merge o data la <b>8 secunde</b>. 2-Step-ul merge cand ai pornit flacarile sau pocniturile.</li>
</ul>
</div>
<h2 class="alg-h2"><span>06</span>Limite</h2>
<div class="alg-card alg-warn">
<ul>
<li>Odata montat, <b>antilag-ul ramane pe masina</b>: nu il poti demonta si nu il poti muta pe alta masina. Culoarea si stilul alese raman salvate pe masina.</li>
<li>Cu motorul oprit sau distrus, efectele se opresc.</li>
<li>Efectele le vad si le aud jucatorii aflati la cel mult 80 m de masina.</li>
</ul>
</div>
<p class="alg-foot">Turbina si restul pieselor: <a href="/general/tuning">Tuning</a>. Condus pe teren: <a href="/general/offroad">Offroad</a>.</p>
</div>
