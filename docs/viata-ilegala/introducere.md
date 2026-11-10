---
outline: false
---

<style>
.vii {
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
.vii *, .vii *::before, .vii *::after { box-sizing: border-box; }
.vii p, .vii li { margin: 0; line-height: 1.6; color: var(--text); }
.vii ul, .vii ol { list-style: none; padding: 0; margin: 0; }
.vii li + li { margin-top: 0; }
.vii b { color: #fff; font-weight: 650; }
.vii a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.vii a:hover { color: #fecaca; }
.vii a:focus-visible { outline: 3px solid var(--red); outline-offset: 3px; border-radius: 8px; }
/* ---------- hero ---------- */
.vii .vii-hero {
  position: relative; overflow: hidden; isolation: isolate;
  background: radial-gradient(120% 90% at 50% 120%, rgba(185, 28, 28, 0.35), transparent 60%), var(--ink);
  border: 1px solid var(--line); border-radius: 22px;
  padding: clamp(1.15rem, 4vw, 2.4rem) clamp(1.15rem, 4vw, 2.4rem) 0;
}
.vii .vii-hero::after {
  content: ''; position: absolute; inset: 0; z-index: -1; pointer-events: none;
  background: repeating-linear-gradient(0deg, rgba(255, 255, 255, 0.018) 0 1px, transparent 1px 4px);
}
.vii .vii-kicker {
  display: inline-flex; align-items: center; gap: 0.5rem; margin-bottom: 0.7rem;
  font: 700 0.74rem/1.2 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace;
  letter-spacing: 0.18em; text-transform: uppercase; color: var(--red);
}
.vii .vii-kicker::before { content: ''; width: 8px; height: 8px; border-radius: 50%; background: var(--red); box-shadow: 0 0 0 4px var(--ember); animation: vii-rec 1.6s steps(1, end) infinite; }
@keyframes vii-rec { 0%, 60% { opacity: 1; } 61%, 100% { opacity: 0.25; } }
.vii .vii-hero h1 {
  margin: 0 0 0.8rem; padding: 0; border: 0; color: #fff;
  font-size: clamp(2.1rem, 7vw, 3.6rem); line-height: 1.02; font-weight: 850; letter-spacing: -0.035em;
}
.vii .vii-hero h1 span { color: var(--red); }
.vii .vii-lede { max-width: 60ch; color: var(--mute); font-size: 1.05rem; }
.vii .vii-chips { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1.1rem; }
.vii .vii-chips li {
  display: inline-flex; align-items: baseline; gap: 0.4rem;
  background: rgba(15, 15, 17, 0.9); border: 1px solid var(--line2); border-radius: 999px; padding: 0.3rem 0.8rem;
  font-size: 0.85rem; color: var(--mute);
}
.vii .vii-chips b { font-size: 1rem; font-variant-numeric: tabular-nums; }
.vii .vii-net { display: block; width: 100%; height: auto; margin-top: 1.2rem; }
.vii-net .sky { fill: url(#vii-sky); }
.vii-net .haze { fill: url(#vii-haze); }
.vii-net .beam { fill: url(#vii-beam); transform-box: view-box; }
.vii-net .beam.l { transform-origin: 120px 300px; animation: vii-sweep-l 14s ease-in-out infinite; }
.vii-net .beam.r { transform-origin: 690px 300px; animation: vii-sweep-r 17s ease-in-out infinite; }
@keyframes vii-sweep-l { 0%, 100% { transform: rotate(-18deg); } 50% { transform: rotate(16deg); } }
@keyframes vii-sweep-r { 0%, 100% { transform: rotate(14deg); } 50% { transform: rotate(-20deg); } }
.vii-net .smoke { fill: rgba(255, 255, 255, 0.05); filter: url(#vii-blur); animation: vii-drift 22s ease-in-out infinite; }
.vii-net .smoke.b { animation-duration: 28s; animation-delay: -9s; }
@keyframes vii-drift { 0%, 100% { transform: translateX(-40px); } 50% { transform: translateX(40px); } }
.vii-net .wire { fill: none; stroke: #2a2a30; stroke-width: 1.5; }
.vii-net .flow { fill: none; stroke: var(--red); stroke-width: 2; stroke-linecap: round; stroke-dasharray: 3 12; animation: vii-flow 1.8s linear infinite; }
.vii-net .flow.mid { stroke: #f87171; animation-duration: 2.3s; }
.vii-net .flow.top { stroke: var(--brass); animation-duration: 2.8s; }
@keyframes vii-flow { to { stroke-dashoffset: -30; } }
.vii-net .n1 { fill: #16161a; stroke: #7f1d1d; stroke-width: 2; animation: vii-blink 6s steps(1, end) infinite; }
.vii-net .n1:nth-of-type(2n) { animation-delay: -2s; }
.vii-net .n1:nth-of-type(3n) { animation-delay: -4s; }
@keyframes vii-blink { 0%, 70% { fill: #16161a; } 71%, 84% { fill: var(--red); } 85%, 100% { fill: #16161a; } }
.vii-net .n2 { fill: #1c0b0b; stroke: var(--blood); stroke-width: 2.5; }
.vii-net .n3 { fill: #2a0b0b; stroke: var(--red); stroke-width: 3; }
.vii-net .crown { fill: #140f05; stroke: var(--brass); stroke-width: 3; }
.vii-net .gem { fill: var(--brass); }
.vii-net .ring { fill: none; stroke: var(--red); stroke-width: 2; transform-box: fill-box; transform-origin: center; animation: vii-ring 3s ease-out infinite; }
.vii-net .ring.gold { stroke: var(--brass); animation-delay: -1.5s; }
@keyframes vii-ring { 0% { opacity: 0.8; transform: scale(0.6); } 100% { opacity: 0; transform: scale(2.2); } }
.vii-net .city { fill: #040405; }
.vii-net .win rect { fill: #fbbf24; opacity: 0.12; }
.vii-net .win .on { animation: vii-lamp 9s steps(1, end) infinite; }
.vii-net .win .on:nth-child(2n) { animation-delay: -3s; }
.vii-net .win .on:nth-child(3n) { animation-delay: -6s; }
@keyframes vii-lamp { 0%, 40% { opacity: 0.12; } 41%, 80% { opacity: 0.8; } 81%, 100% { opacity: 0.12; } }
.vii-net .tier { font: 700 9px ui-monospace, Menlo, Consolas, monospace; letter-spacing: 0.12em; fill: #52525b; }
@media (max-width: 560px) { .vii-net .tier { display: none; } }
/* ---------- sections ---------- */
.vii .vii-h2 {
  display: flex; align-items: baseline; gap: 0.7rem;
  margin: 3rem 0 0.6rem; padding: 0; border: 0;
  font-size: 1.5rem; line-height: 1.25; font-weight: 750; letter-spacing: -0.015em; color: #fff;
}
.vii .vii-h2 span { font: 700 0.8rem/1 ui-monospace, Menlo, Consolas, monospace; color: var(--red); letter-spacing: 0.1em; }
.vii .vii-sub { color: var(--mute); max-width: 66ch; margin-bottom: 1.1rem; }
.vii .vii-h3 { margin: 0 0 0.35rem; padding: 0; border: 0; font-size: 1.08rem; line-height: 1.3; font-weight: 700; color: #fff; }
/* section map */
.vii .vii-map { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr)); gap: 0.8rem; }
.vii .vii-map li { display: flex; }
.vii .vii-map a {
  position: relative; display: flex; flex-direction: column; gap: 0.5rem; width: 100%;
  padding: 1.1rem 1.15rem 1.15rem; border-radius: 16px; text-decoration: none; color: var(--text);
  background: linear-gradient(180deg, var(--panel2), var(--panel)); border: 1px solid var(--line);
  box-shadow: inset 0 1px 0 rgba(239, 68, 68, 0.18);
  transition: transform 0.2s ease, border-color 0.2s ease;
}
.vii .vii-map a:hover { transform: translateY(-3px); border-color: #7f1d1d; color: var(--text); }
.vii .vii-map .top { display: flex; align-items: center; justify-content: space-between; gap: 0.6rem; }
.vii .vii-map .ico {
  display: grid; place-items: center; width: 2.4rem; height: 2.4rem; border-radius: 12px;
  background: var(--wine); color: var(--red); border: 1px solid #5b1414;
}
.vii .vii-map .ico svg { width: 1.25rem; height: 1.25rem; }
.vii .vii-map .num { font: 800 1.6rem/1 ui-monospace, Menlo, Consolas, monospace; color: #27272a; }
.vii .vii-map .tag { font: 700 0.7rem/1.2 ui-monospace, Menlo, Consolas, monospace; letter-spacing: 0.14em; text-transform: uppercase; color: var(--red); }
.vii .vii-map .t { font-size: 1.1rem; font-weight: 750; color: #fff; line-height: 1.25; }
.vii .vii-map .d { color: var(--mute); font-size: 0.93rem; line-height: 1.5; }
.vii .vii-map .go { margin-top: auto; padding-top: 0.3rem; font-size: 0.85rem; font-weight: 650; color: #fca5a5; }
.vii .vii-map .rules a { background: transparent; border-style: dashed; border-color: var(--line2); box-shadow: none; }
.vii .vii-map .rules .ico { background: #141005; color: var(--brass); border-color: #4a3a17; }
.vii .vii-map .rules .tag { color: var(--brass); }
/* ladder */
.vii .vii-ladder { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 0.8rem; align-items: end; }
.vii .vii-ladder > li {
  background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 1rem 1.1rem 1.1rem;
  border-top: 3px solid #7f1d1d;
}
.vii .vii-ladder > li:nth-child(2) { padding-top: 2.2rem; border-top-color: var(--blood); }
.vii .vii-ladder > li:nth-child(3) { padding-top: 3.4rem; border-top-color: var(--red); background: linear-gradient(180deg, #1a0909, var(--panel) 55%); }
.vii .vii-ladder .st { font: 700 0.72rem/1.2 ui-monospace, Menlo, Consolas, monospace; letter-spacing: 0.14em; text-transform: uppercase; color: var(--dim); }
.vii .vii-ladder .nm { display: block; margin: 0.2rem 0 0.8rem; font-size: 1.2rem; font-weight: 800; color: #fff; line-height: 1.2; }
.vii .vii-ladder dl { margin: 0; display: grid; gap: 0.45rem; }
.vii .vii-ladder dl div { display: flex; justify-content: space-between; gap: 0.8rem; border-bottom: 1px dashed var(--line2); padding-bottom: 0.4rem; }
.vii .vii-ladder dl div:last-child { border-bottom: 0; padding-bottom: 0; }
.vii .vii-ladder dt { color: var(--mute); font-size: 0.86rem; line-height: 1.35; }
.vii .vii-ladder dd { margin: 0; color: #fff; font-weight: 700; font-size: 0.92rem; text-align: right; white-space: nowrap; font-variant-numeric: tabular-nums; }
@media (max-width: 720px) {
  .vii .vii-ladder { grid-template-columns: minmax(0, 1fr); }
  .vii .vii-ladder > li:nth-child(2), .vii .vii-ladder > li:nth-child(3) { padding-top: 1rem; }
}
.vii .vii-note { margin-top: 0.85rem; color: var(--mute); font-size: 0.92rem; }
/* sindicat + tablet */
.vii .vii-duo { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1.15fr); gap: 0.8rem; }
@media (max-width: 760px) { .vii .vii-duo { grid-template-columns: minmax(0, 1fr); } }
.vii .vii-card { background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 1.15rem 1.25rem; }
.vii .vii-card.gold { background: linear-gradient(160deg, rgba(214, 165, 74, 0.1), var(--panel) 55%); border-color: #3d3217; }
.vii .vii-card > p { color: var(--mute); font-size: 0.96rem; }
.vii .vii-ticks { margin-top: 0.7rem; display: grid; gap: 0.45rem; }
.vii .vii-ticks li { position: relative; padding-left: 1.2rem; color: var(--mute); font-size: 0.94rem; line-height: 1.5; }
.vii .vii-ticks li::before { content: ''; position: absolute; left: 0; top: 0.55em; width: 7px; height: 7px; transform: rotate(45deg); background: var(--brass); }
.vii .vii-tabs { margin-top: 0.75rem; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 130px), 1fr)); gap: 0.5rem; }
.vii .vii-tabs li { background: var(--panel2); border: 1px solid var(--line); border-radius: 12px; padding: 0.55rem 0.7rem; font-size: 0.88rem; color: var(--mute); line-height: 1.4; }
.vii .vii-tabs b { display: block; font-size: 0.92rem; }
.vii .vii-quote {
  margin-top: 2.6rem; padding: 1.2rem 1.3rem; border-radius: 16px; border: 1px solid #4c1414;
  background: linear-gradient(110deg, #1d0808, var(--panel) 70%);
}
.vii .vii-quote p { color: #fecaca; font-size: 1.05rem; font-weight: 600; }
.vii .vii-quote span { display: block; margin-top: 0.35rem; color: var(--mute); font-size: 0.9rem; font-weight: 400; }
@media (prefers-reduced-motion: reduce) {
  .vii .vii-kicker::before, .vii-net .beam, .vii-net .smoke, .vii-net .flow, .vii-net .n1, .vii-net .ring, .vii-net .win .on { animation: none; }
  .vii-net .ring { opacity: 0; }
  .vii .vii-map a { transition: none; }
  .vii .vii-map a:hover { transform: none; }
}
</style>

<div class="vii">
<section class="vii-hero">
<p class="vii-kicker">Viata ilegala</p>
<h1>De la strada la <span>imperiu</span></h1>
<p class="vii-lede">Aici afli cum pornesti o familie, cum urci pana la Mafie Oficiala si cum va impartiti orasul cu celelalte mafii. Peste toate sta Sindicatul, iar totul se vede in Tableta Sentinel.</p>
<ul class="vii-chips">
<li><b>3</b> stadii</li>
<li><b>45</b> membri maxim</li>
<li><b>8</b> teritorii</li>
<li><b>1</b> Sindicat</li>
</ul>
<svg class="vii-net" viewBox="0 0 800 300" role="img" aria-label="Retea de familii care urca spre Sindicat">
<defs>
<linearGradient id="vii-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#060607" stop-opacity="0"/><stop offset="1" stop-color="#1a0606"/></linearGradient>
<radialGradient id="vii-haze" cx="0.5" cy="1" r="0.6"><stop offset="0" stop-color="#b91c1c" stop-opacity="0.45"/><stop offset="1" stop-color="#b91c1c" stop-opacity="0"/></radialGradient>
<linearGradient id="vii-beam" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#ffffff" stop-opacity="0.16"/><stop offset="1" stop-color="#ffffff" stop-opacity="0"/></linearGradient>
<filter id="vii-blur" x="-30%" y="-60%" width="160%" height="220%"><feGaussianBlur stdDeviation="16"/></filter>
</defs>
<rect class="sky" width="800" height="300"/>
<polygon class="beam l" points="114,300 126,300 196,0 44,0"/>
<polygon class="beam r" points="684,300 696,300 766,0 614,0"/>
<ellipse class="smoke" cx="260" cy="120" rx="170" ry="34"/>
<ellipse class="smoke b" cx="560" cy="80" rx="150" ry="28"/>
<ellipse class="haze" cx="400" cy="300" rx="430" ry="140"/>
<text class="tier" x="12" y="44">SINDICAT</text>
<text class="tier" x="12" y="92">OFICIALA</text>
<text class="tier" x="12" y="146">NEOFICIALA</text>
<text class="tier" x="12" y="230">FAMILIE IC</text>
<g>
<path class="wire" d="M90 198 L180 140"/><path class="wire" d="M170 206 L180 140"/><path class="wire" d="M250 198 L180 140"/>
<path class="wire" d="M250 198 L330 146"/><path class="wire" d="M330 206 L330 146"/>
<path class="wire" d="M470 206 L470 146"/><path class="wire" d="M550 198 L470 146"/>
<path class="wire" d="M550 198 L620 140"/><path class="wire" d="M630 206 L620 140"/><path class="wire" d="M710 198 L620 140"/>
<path class="wire" d="M180 140 L290 88"/><path class="wire" d="M330 146 L290 88"/><path class="wire" d="M330 146 L510 88"/>
<path class="wire" d="M470 146 L510 88"/><path class="wire" d="M620 140 L510 88"/>
<path class="wire" d="M290 88 L400 40"/><path class="wire" d="M510 88 L400 40"/>
</g>
<g>
<path class="flow" d="M90 198 L180 140"/><path class="flow" d="M170 206 L180 140"/><path class="flow" d="M250 198 L180 140"/>
<path class="flow" d="M250 198 L330 146"/><path class="flow" d="M330 206 L330 146"/>
<path class="flow" d="M470 206 L470 146"/><path class="flow" d="M550 198 L470 146"/>
<path class="flow" d="M550 198 L620 140"/><path class="flow" d="M630 206 L620 140"/><path class="flow" d="M710 198 L620 140"/>
<path class="flow mid" d="M180 140 L290 88"/><path class="flow mid" d="M330 146 L290 88"/><path class="flow mid" d="M330 146 L510 88"/>
<path class="flow mid" d="M470 146 L510 88"/><path class="flow mid" d="M620 140 L510 88"/>
<path class="flow top" d="M290 88 L400 40"/><path class="flow top" d="M510 88 L400 40"/>
</g>
<g>
<circle class="n1" cx="90" cy="198" r="6"/><circle class="n1" cx="170" cy="206" r="6"/><circle class="n1" cx="250" cy="198" r="6"/><circle class="n1" cx="330" cy="206" r="6"/>
<circle class="n1" cx="470" cy="206" r="6"/><circle class="n1" cx="550" cy="198" r="6"/><circle class="n1" cx="630" cy="206" r="6"/><circle class="n1" cx="710" cy="198" r="6"/>
</g>
<circle class="n2" cx="180" cy="140" r="9"/><circle class="n2" cx="330" cy="146" r="9"/><circle class="n2" cx="470" cy="146" r="9"/><circle class="n2" cx="620" cy="140" r="9"/>
<circle class="ring" cx="290" cy="88" r="12"/><circle class="ring" cx="510" cy="88" r="12"/>
<circle class="n3" cx="290" cy="88" r="12"/><circle class="n3" cx="510" cy="88" r="12"/>
<circle class="ring gold" cx="400" cy="40" r="17"/>
<circle class="crown" cx="400" cy="40" r="17"/>
<rect class="gem" x="393" y="33" width="14" height="14" transform="rotate(45 400 40)"/>
<path class="city" d="M0 300 V262 H30 V250 H58 V268 H80 V240 H104 V256 H126 V246 H150 V270 H176 V236 H196 V230 H214 V252 H240 V262 H262 V242 H290 V256 H316 V234 H334 V226 H350 V244 H378 V258 H404 V238 H430 V248 H456 V230 H476 V252 H500 V266 H524 V244 H548 V234 H570 V258 H598 V248 H624 V238 H646 V262 H672 V246 H700 V256 H724 V236 H748 V258 H772 V248 H800 V300 Z"/>
<g class="win">
<rect class="on" x="84" y="248" width="4" height="5"/><rect x="94" y="258" width="4" height="5"/><rect class="on" x="182" y="244" width="4" height="5"/><rect x="200" y="238" width="4" height="5"/>
<rect class="on" x="320" y="242" width="4" height="5"/><rect x="338" y="236" width="4" height="5"/><rect class="on" x="460" y="240" width="4" height="5"/><rect x="530" y="252" width="4" height="5"/>
<rect class="on" x="552" y="244" width="4" height="5"/><rect x="628" y="248" width="4" height="5"/><rect class="on" x="728" y="246" width="4" height="5"/><rect x="738" y="256" width="4" height="5"/>
</g>
</svg>
</section>
<h2 class="vii-h2" id="harta-sectiunii"><span>01</span>Harta sectiunii</h2>
<p class="vii-sub">Sase pagini, o singura lume. Incepe cu stadiul in care esti acum si citeste regulamentul inainte de prima actiune.</p>
<ul class="vii-map">
<li><a href="/viata-ilegala/familie-ic"><span class="top"><span class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></span><span class="num">01</span></span><span class="tag">Stadiul I</span><span class="t">Familie IC</span><span class="d">Cum ia nastere familia, ce primeste de la Sindicat, cum angajezi si cum ajungi in atentia mafiilor.</span><span class="go">Deschide pagina</span></a></li>
<li><a href="/viata-ilegala/mafie-neoficiala"><span class="top"><span class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 20h20"/><path d="M4 20 3 8l5 4 4-7 4 7 5-4-1 12"/></svg></span><span class="num">02</span></span><span class="tag">Stadiile II si III</span><span class="t">Mafie Neoficiala &amp; Oficiala</span><span class="d">Ce cere avansarea, ce primesti in plus, uneltele sefului si rapirea membrilor de rang inalt.</span><span class="go">Deschide pagina</span></a></li>
<li><a href="/viata-ilegala/sistem-teritorial"><span class="top"><span class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M1 6v16l7-4 8 4 7-4V2l-7 4-8-4-7 4z"/><path d="M8 2v16"/><path d="M16 6v16"/></svg></span><span class="num">03</span></span><span class="tag">Harta</span><span class="t">Teritorii &amp; Razboaie</span><span class="d">Zonele orasului, ce castiga cine le tine si cum se desfasoara un razboi pentru ele.</span><span class="go">Deschide pagina</span></a></li>
<li><a href="/viata-ilegala/piata-neagra"><span class="top"><span class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 3h18l-2 7H5L3 3z"/><path d="M5 10v10a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V10"/><path d="M9 14h6"/></svg></span><span class="num">04</span></span><span class="tag">Comert</span><span class="t">Piata Neagra</span><span class="d">Unde vinzi si cumperi marfa care nu are ce cauta intr-un magazin.</span><span class="go">Deschide pagina</span></a></li>
<li><a href="/viata-ilegala/droguri-efecte"><span class="top"><span class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 2v7.31"/><path d="M14 9.3V2"/><path d="M8.5 2h7"/><path d="M14 9.3a6.5 6.5 0 1 1-4 0"/><path d="M5.52 16h12.96"/></svg></span><span class="num">05</span></span><span class="tag">Substante</span><span class="t">Droguri &amp; Efecte</span><span class="d">Ce face fiecare drog, cat tine efectul si ce patesti daca exagerezi.</span><span class="go">Deschide pagina</span></a></li>
<li class="rules"><a href="/zona-info/regulament-mafii"><span class="top"><span class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5z"/><path d="M4 19.5V21h16"/></svg></span><span class="num">!!</span></span><span class="tag">Obligatoriu</span><span class="t">Regulamentul Mafiilor</span><span class="d">Reguli pentru fiecare familie si mafie: infiintare, conduita, sanctiuni, razboaie, rapiri.</span><span class="go">Citeste regulamentul</span></a></li>
</ul>
<h2 class="vii-h2" id="scara-puterii"><span>02</span>Scara puterii</h2>
<p class="vii-sub">Fiecare familie trece prin aceleasi trei stadii. Sindicatul decide cand urci. Stadiul familiei schimba cati membri poti avea si cat de mare e seiful.</p>
<ul class="vii-ladder">
<li><span class="st">Stadiul I</span><span class="nm">Familie IC</span><dl><div><dt>Membri (regulament)</dt><dd>10 - 25</dd></div><div><dt>Ore ca sa intri</dt><dd>150</dd></div><div><dt>Clasament: membri</dt><dd>15</dd></div><div><dt>Clasament: puncte</dt><dd>7.500</dd></div><div><dt>Seif</dt><dd>x1</dd></div></dl></li>
<li><span class="st">Stadiul II</span><span class="nm">Mafie Neoficiala</span><dl><div><dt>Membri (regulament)</dt><dd>15 - 35</dd></div><div><dt>Ore ca sa intri</dt><dd>250</dd></div><div><dt>Clasament: membri</dt><dd>25</dd></div><div><dt>Clasament: puncte</dt><dd>15.000</dd></div><div><dt>Clasament: teritorii</dt><dd>2</dd></div><div><dt>Seif</dt><dd>x2</dd></div></dl></li>
<li><span class="st">Stadiul III</span><span class="nm">Mafie Oficiala</span><dl><div><dt>Membri (regulament)</dt><dd>20 - 45</dd></div><div><dt>Ore ca sa intri</dt><dd>500</dd></div><div><dt>Clasament: membri</dt><dd>30</dd></div><div><dt>Clasament: puncte</dt><dd>30.000</dd></div><div><dt>Clasament: teritorii</dt><dd>3</dd></div><div><dt>Seif</dt><dd>x3</dd></div></dl></li>
</ul>
<p class="vii-note"><b>Regulament</b> = minimul ca familia sa existe. <b>Clasament</b> = cat iti cere Tableta Sentinel ca familia sa fie "In regula" la stadiul ei. Cand ajungi la limita maxima de membri, nu mai poti angaja pe nimeni.</p>
<h2 class="vii-h2" id="sindicat-si-tableta"><span>03</span>Sindicatul si Tableta Sentinel</h2>
<div class="vii-duo">
<div class="vii-card gold">
<h3 class="vii-h3">Sindicatul</h3>
<p>Autoritatea suprema a lumii criminale. Pastreaza ordinea intre familii, iar membrii lui nu pot fi jigniti, raniti sau omorati.</p>
<ul class="vii-ticks">
<li>Infiinteaza familiile si le numeste liderul.</li>
<li>Hotaraste cand o familie urca in stadiul urmator.</li>
<li>Alege culoarea familiei pe harta si poate da sau lua teritorii direct.</li>
<li>Da amenzi, avertismente si obiective cu termen.</li>
<li>Poate anula oricand un razboi.</li>
<li>Trimite codurile de alerta: Cod Albastru doar pentru lideri, Cod Galben si Cod Rosu pentru toti membrii familiilor.</li>
</ul>
</div>
<div class="vii-card">
<h3 class="vii-h3"><img class="eg-item" src="/items/sentinel_tablet.webp" alt="">Tableta Sentinel</h3>
<p>Un item din inventar care se deschide doar pentru membrii unei familii sau mafii. Tot ce tine de familie se vede aici:</p>
<ul class="vii-tabs">
<li><b>Clasament</b>Scorul familiilor, membrii si cerintele stadiului.</li>
<li><b>Teritorii</b>Harta zonelor si razboaiele.</li>
<li><b>Taxe</b>Taxele de protectie stranse pe teritoriile tale.</li>
<li><b>Rezervari</b>Calendarul cu sloturi rezervate de sefi.</li>
<li><b>Informatii</b>Ponturi pe care seful le poate cumpara.</li>
<li><b>Statistici</b>Rezultatele razboaielor.</li>
<li><b>Amenzi</b>Ce ai de platit Sindicatului si pana cand.</li>
<li><b>Obiective</b>Sarcinile primite de la Sindicat.</li>
<li><b>Avertismente</b>Avertismentele active ale familiei.</li>
</ul>
</div>
</div>
<div class="vii-quote">
<p>Roleplay-ul vine inaintea actiunii. O poveste buna valoreaza mai mult decat o suta de victorii fara sens.</p>
<span>Familiile care urca sunt cele care se fac remarcate prin roleplay, nu prin numarul de focuri trase.</span>
</div>
</div>
