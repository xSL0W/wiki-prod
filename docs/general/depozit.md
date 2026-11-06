---
outline: false
---

<style>
.dpz {
  --ink: #0b0b0d;
  --panel: #17171a;
  --panel2: #1f1f23;
  --line: #2f2f36;
  --text: #f4f4f5;
  --mute: #a1a1aa;
  --red: #ef4444;
  --red-deep: #b91c1c;
  --red-soft: rgba(239, 68, 68, 0.14);
  --amber: #f5b931;
  max-width: 960px;
  margin: 0 auto;
  color: var(--text);
  font-family: Inter, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.dpz *, .dpz *::before, .dpz *::after { box-sizing: border-box; }
.dpz p, .dpz li { line-height: 1.6; color: var(--text); margin: 0; }
.dpz ul, .dpz ol { list-style: none; padding: 0; margin: 0; }
.dpz li + li { margin-top: 0; }
.dpz b { color: #fff; font-weight: 650; }
.dpz a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.dpz a:hover { color: #fecaca; }
.dpz a:focus-visible { outline: 3px solid var(--red); outline-offset: 3px; border-radius: 6px; }
.dpz kbd {
  font: inherit; font-size: 0.85em; font-weight: 700; color: #fff; background: var(--red-deep);
  border-radius: 6px; padding: 0.05rem 0.45rem;
}
/* ---------- hero ---------- */
.dpz .dpz-hero {
  position: relative; overflow: hidden;
  display: grid; grid-template-columns: minmax(0, 1.25fr) minmax(0, 1fr); gap: clamp(1rem, 3vw, 2rem); align-items: center;
  background: radial-gradient(110% 120% at 0% 100%, rgba(185, 28, 28, 0.28), var(--ink) 62%);
  border: 1px solid var(--line); border-radius: 22px;
  padding: clamp(1.15rem, 4vw, 2.4rem);
}
.dpz .dpz-kicker {
  font-size: 0.78rem; font-weight: 700; letter-spacing: 0.16em; text-transform: uppercase; color: var(--red);
  margin-bottom: 0.55rem;
}
.dpz .dpz-hero h1 {
  margin: 0 0 0.75rem; border: 0; padding: 0;
  font-size: clamp(2rem, 6.4vw, 3.3rem); line-height: 1.04; font-weight: 800; letter-spacing: -0.03em; color: #fff;
}
.dpz .dpz-hero h1 span { color: var(--red); }
.dpz .dpz-lead { color: #d4d4d8; font-size: clamp(1rem, 2.2vw, 1.1rem); max-width: 34rem; }
.dpz .dpz-art { width: 100%; max-width: 340px; justify-self: center; }
.dpz .dpz-art svg { display: block; width: 100%; height: auto; }
.dpz .dpz-shutter { animation: dpz-roll 9s ease-in-out infinite; }
@keyframes dpz-roll {
  0%, 12% { transform: translateY(0); }
  38%, 70% { transform: translateY(-104px); }
  92%, 100% { transform: translateY(0); }
}
.dpz .dpz-marker { animation: dpz-bob 2.4s ease-in-out infinite; transform-origin: 160px 40px; }
@keyframes dpz-bob { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(8px); } }
.dpz .dpz-glow { animation: dpz-glow 9s ease-in-out infinite; }
@keyframes dpz-glow { 0%, 15% { opacity: 0; } 40%, 70% { opacity: 1; } 90%, 100% { opacity: 0; } }
/* ---------- stats ---------- */
.dpz .dpz-stats {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 0.75rem; margin: 1.25rem 0 0;
}
.dpz .dpz-stat { background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 0.95rem 1.05rem; }
.dpz .dpz-stat .dpz-num { display: block; font-size: 1.6rem; font-weight: 800; color: #fff; letter-spacing: -0.02em; line-height: 1.1; }
.dpz .dpz-stat .dpz-lbl { display: block; color: var(--mute); font-size: 0.88rem; margin-top: 0.2rem; }
/* ---------- sections ---------- */
.dpz .dpz-sec { margin-top: 2.4rem; }
.dpz .dpz-h2 {
  margin: 0 0 0.4rem; padding: 0; border: 0;
  font-size: clamp(1.35rem, 3.6vw, 1.7rem); font-weight: 800; letter-spacing: -0.02em; color: #fff;
}
.dpz .dpz-sub { color: var(--mute); margin-bottom: 1.1rem; }
/* steps */
.dpz .dpz-steps { display: grid; gap: 0.7rem; counter-reset: dpz; }
.dpz .dpz-step {
  counter-increment: dpz; position: relative;
  background: var(--panel); border: 1px solid var(--line); border-radius: 16px;
  padding: 0.95rem 1.05rem 0.95rem 3.6rem;
}
.dpz .dpz-step::before {
  content: counter(dpz); position: absolute; left: 1rem; top: 0.9rem;
  width: 1.9rem; height: 1.9rem; border-radius: 50%; display: grid; place-items: center;
  background: var(--red-soft); color: var(--red); font-weight: 800; border: 1px solid rgba(239, 68, 68, 0.4);
}
.dpz .dpz-step b { display: block; margin-bottom: 0.15rem; }
.dpz .dpz-step p { color: #d4d4d8; }
/* rules */
.dpz .dpz-rules { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 0.75rem; }
.dpz .dpz-rule { background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 1rem 1.05rem; }
.dpz .dpz-rule .dpz-ico {
  width: 2.2rem; height: 2.2rem; border-radius: 10px; display: grid; place-items: center;
  background: var(--red-soft); color: var(--red); margin-bottom: 0.6rem;
}
.dpz .dpz-rule .dpz-ico svg { width: 1.2rem; height: 1.2rem; }
.dpz .dpz-rule .dpz-h3 { margin: 0 0 0.25rem; padding: 0; border: 0; font-size: 1.02rem; font-weight: 700; color: #fff; }
.dpz .dpz-rule p { color: #d4d4d8; font-size: 0.95rem; }
/* places */
.dpz .dpz-places { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 380px), 1fr)); gap: 1rem; }
.dpz .dpz-place { background: var(--panel); border: 1px solid var(--line); border-radius: 18px; overflow: hidden; display: flex; flex-direction: column; }
.dpz .dpz-place .dpz-img { display: block; width: 100%; height: auto; aspect-ratio: 16 / 9; object-fit: cover; margin: 0; border-bottom: 1px solid var(--line); }
.dpz .dpz-place .dpz-noimg {
  aspect-ratio: 16 / 9; display: grid; place-items: center; border-bottom: 1px solid var(--line);
  background: radial-gradient(80% 90% at 50% 100%, rgba(185, 28, 28, 0.22), var(--panel2) 70%);
  color: var(--mute); font-size: 0.9rem;
}
.dpz .dpz-place .dpz-noimg svg { width: 3rem; height: 3rem; color: var(--red); display: block; margin: 0 auto 0.4rem; }
.dpz .dpz-body { padding: 1rem 1.1rem 1.15rem; }
.dpz .dpz-tag {
  display: inline-block; font-size: 0.72rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase;
  color: var(--red); margin-bottom: 0.3rem;
}
.dpz .dpz-place .dpz-h3 { margin: 0 0 0.3rem; padding: 0; border: 0; font-size: 1.15rem; font-weight: 750; color: #fff; }
.dpz .dpz-place p { color: #d4d4d8; font-size: 0.95rem; }
/* note */
.dpz .dpz-note {
  margin-top: 2.4rem; border: 1px solid rgba(239, 68, 68, 0.35); background: var(--red-soft);
  border-radius: 16px; padding: 1rem 1.15rem;
}
.dpz .dpz-note p { color: #fde2e2; }
@media (max-width: 720px) {
  .dpz .dpz-hero { grid-template-columns: 1fr; }
  .dpz .dpz-art { max-width: 260px; }
}
@media (prefers-reduced-motion: reduce) {
  .dpz .dpz-shutter, .dpz .dpz-marker, .dpz .dpz-glow { animation: none; }
  .dpz .dpz-glow { opacity: 1; }
  .dpz .dpz-shutter { transform: translateY(-104px); }
}
</style>

<div class="dpz">
<section class="dpz-hero">
<div>
<p class="dpz-kicker">Locatii</p>
<h1>Depozit <span>personal</span></h1>
<p class="dpz-lead">Ai prea multe lucruri in buzunare sau in portbagaj? Ai patru depozite publice: trei in oras si unul pe Cayo Perico. Fiecare jucator are acolo spatiul lui, la care are acces doar el. Platesti o taxa de fiecare data cand il deschizi.</p>
</div>
<div class="dpz-art" aria-hidden="true">
<svg viewBox="0 0 320 240" xmlns="http://www.w3.org/2000/svg">
<defs>
<clipPath id="dpz-door"><rect x="70" y="92" width="180" height="108"/></clipPath>
<linearGradient id="dpz-slat" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#52525b"/><stop offset="1" stop-color="#3f3f46"/></linearGradient>
<radialGradient id="dpz-light" cx="0.5" cy="1" r="0.8"><stop offset="0" stop-color="#ef4444" stop-opacity="0.45"/><stop offset="1" stop-color="#ef4444" stop-opacity="0"/></radialGradient>
</defs>
<path d="M30 92 L160 62 L290 92 Z" fill="#27272a" stroke="#3f3f46" stroke-width="2"/>
<rect x="30" y="92" width="260" height="120" fill="#1f1f23" stroke="#3f3f46" stroke-width="2"/>
<rect x="62" y="86" width="196" height="118" rx="3" fill="#0b0b0d" stroke="#52525b" stroke-width="2"/>
<g clip-path="url(#dpz-door)">
<rect x="70" y="92" width="180" height="108" fill="#0f0f12"/>
<rect class="dpz-glow" x="70" y="92" width="180" height="108" fill="url(#dpz-light)"/>
<g fill="#a16207" stroke="#78350f" stroke-width="1.5">
<rect x="88" y="150" width="46" height="46" rx="2"/>
<rect x="140" y="160" width="40" height="36" rx="2"/>
<rect x="186" y="140" width="50" height="56" rx="2"/>
<rect x="104" y="116" width="34" height="34" rx="2"/>
</g>
<g stroke="#78350f" stroke-width="1.5" fill="none">
<path d="M88 166 H134 M140 174 H180 M186 158 H236 M104 128 H138"/>
</g>
<g class="dpz-shutter">
<rect x="70" y="92" width="180" height="108" fill="url(#dpz-slat)"/>
<g stroke="#27272a" stroke-width="2">
<path d="M70 104 H250 M70 116 H250 M70 128 H250 M70 140 H250 M70 152 H250 M70 164 H250 M70 176 H250 M70 188 H250"/>
</g>
<rect x="148" y="192" width="24" height="5" rx="2" fill="#18181b"/>
</g>
</g>
<rect x="20" y="210" width="280" height="6" rx="3" fill="#27272a"/>
<g class="dpz-marker">
<path d="M146 26 H174 L160 50 Z" fill="#ef4444"/>
</g>
</svg>
</div>
</section>
<ul class="dpz-stats">
<li class="dpz-stat"><span class="dpz-num">4</span><span class="dpz-lbl">depozite in oras si pe Cayo Perico</span></li>
<li class="dpz-stat"><span class="dpz-num">200</span><span class="dpz-lbl">sloturi in fiecare depozit</span></li>
<li class="dpz-stat"><span class="dpz-num">2.000 kg</span><span class="dpz-lbl">greutate maxima</span></li>
<li class="dpz-stat"><span class="dpz-num">Doar tu</span><span class="dpz-lbl">ai acces la ce pui inauntru</span></li>
</ul>
<section class="dpz-sec">
<h2 class="dpz-h2">Cum il folosesti</h2>
<p class="dpz-sub">Nu cumperi si nu inchiriezi nimic. Vii, platesti si deschizi.</p>
<ol class="dpz-steps">
<li class="dpz-step"><b>Mergi la un depozit</b><p>Toate patru sunt pe harta, cu numele lor: Depozit Vespucci, Depozit Port, Depozit Autostrada si Depozit Cayo.</p></li>
<li class="dpz-step"><b>Coboara din masina</b><p>Din masina nu poti deschide depozitul. Mergi pe jos pana la markerul rosu.</p></li>
<li class="dpz-step"><b>Apasa <kbd>E</kbd> langa marker</b><p>Pe eticheta de deasupra markerului vezi cat costa o deschidere.</p></li>
<li class="dpz-step"><b>Platesti taxa</b><p>Banii se iau intai din cash, apoi din banca. Daca nu ai destui, depozitul ramane inchis.</p></li>
<li class="dpz-step"><b>Muti lucrurile</b><p>Se deschide inventarul depozitului langa al tau. Tragi ce vrei sa lasi sau sa iei.</p></li>
</ol>
</section>
<section class="dpz-sec">
<h2 class="dpz-h2">Ce trebuie sa stii</h2>
<ul class="dpz-rules">
<li class="dpz-rule"><div class="dpz-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg></div><h3 class="dpz-h3">E doar al tau</h3><p>Fiecare caracter are spatiul lui. Nimeni altcineva nu vede ce ai pus, nici prietenii tai. Nu il poti imparti cu altcineva.</p></li>
<li class="dpz-rule"><div class="dpz-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 9l9-6 9 6v11a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1z"/><path d="M9 21V12h6v9"/></svg></div><h3 class="dpz-h3">Fiecare depozit e separat</h3><p>Ce lasi in Port gasesti doar in Port. Daca mergi la Vespucci, acolo ai alt spatiu, gol pana pui ceva in el.</p></li>
<li class="dpz-rule"><div class="dpz-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v10M9 10h4.5a1.5 1.5 0 0 1 0 3h-3a1.5 1.5 0 0 0 0 3H15"/></svg></div><h3 class="dpz-h3">Platesti la fiecare deschidere</h3><p>Taxa nu e un abonament. O platesti de fiecare data cand deschizi depozitul. Fiecare depozit are pretul lui.</p></li>
<li class="dpz-rule"><div class="dpz-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div><h3 class="dpz-h3">Zona sigura in jur</h3><p>Pe o raza de 40 de metri in jurul fiecarui depozit armele nu merg si jucatorii nu se pot rani intre ei.</p></li>
</ul>
</section>
<section class="dpz-sec">
<h2 class="dpz-h2">Unde le gasesti</h2>
<p class="dpz-sub">Toate au aceeasi capacitate: 200 de sloturi si 2.000 kg. Difera doar locul si pretul.</p>
<div class="dpz-places">
<article class="dpz-place"><img class="dpz-img" src="/depozit/depozit1.png" alt="Depozit Vespucci, garajele de langa plaja" width="1500" height="844" loading="lazy"><div class="dpz-body"><span class="dpz-tag">Vest</span><h3 class="dpz-h3">Depozit Vespucci</h3><p>Garajele galbene de langa plaja Vespucci, cu parcul de distractii pe chei in spate.</p></div></article>
<article class="dpz-place"><img class="dpz-img" src="/depozit/depozit2.png" alt="Depozit Port, hala din port" width="1440" height="810" loading="lazy"><div class="dpz-body"><span class="dpz-tag">Sud</span><h3 class="dpz-h3">Depozit Port</h3><p>O hala din portul din sudul orasului, printre macarale si containere.</p></div></article>
<article class="dpz-place"><img class="dpz-img" src="/depozit/depozit3.png" alt="Depozit Autostrada, rampa de descarcare" width="1500" height="844" loading="lazy"><div class="dpz-body"><span class="dpz-tag">Est</span><h3 class="dpz-h3">Depozit Autostrada</h3><p>Rampa de descarcare a unei hale din zona industriala, langa autostrada din estul orasului.</p></div></article>
<article class="dpz-place"><div class="dpz-noimg" aria-hidden="true"><div><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22c4-3 6-6 6-10a6 6 0 0 0-12 0c0 4 2 7 6 10z"/><circle cx="12" cy="11" r="2.2"/></svg>Cayo Perico</div></div><div class="dpz-body"><span class="dpz-tag">Insula</span><h3 class="dpz-h3">Depozit Cayo</h3><p>Pe insula Cayo Perico. Ai unde sa lasi lucrurile cand esti pe insula, fara sa te intorci in oras.</p></div></article>
</div>
</section>
<div class="dpz-note"><p><b>Atentie:</b> daca vezi pe eticheta ca depozitul e <b>indisponibil</b>, nu il poti deschide in acel moment. Incearca mai tarziu sau mergi la alt depozit.</p></div>
</div>
