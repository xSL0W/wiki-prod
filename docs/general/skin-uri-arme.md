---
outline: false
---

<style>
.skw {
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
.skw *, .skw *::before, .skw *::after { box-sizing: border-box; }
.skw p, .skw li { line-height: 1.6; color: var(--text); margin: 0; }
.skw ul, .skw ol { list-style: none; padding: 0; margin: 0; }
.skw li + li { margin-top: 0; }
.skw b { color: #fff; font-weight: 650; }
.skw a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.skw a:hover { color: #fecaca; }
.skw a:focus-visible { outline: 3px solid var(--red); outline-offset: 3px; border-radius: 6px; }
.skw kbd {
  font: inherit; font-size: 0.85em; font-weight: 700; color: #fff; background: var(--red-deep);
  border-radius: 6px; padding: 0.05rem 0.45rem;
}
/* ---------- hero ---------- */
.skw .skw-hero {
  position: relative; overflow: hidden; isolation: isolate;
  background: radial-gradient(80% 120% at 100% 0%, rgba(168, 85, 247, 0.16), transparent 55%),
              radial-gradient(110% 120% at 0% 100%, rgba(185, 28, 28, 0.3), var(--ink) 62%);
  border: 1px solid var(--line); border-radius: 22px;
  padding: clamp(1.15rem, 4vw, 2.4rem);
}
.skw .skw-kicker { font-size: 0.78rem; font-weight: 700; letter-spacing: 0.16em; text-transform: uppercase; color: var(--red); margin-bottom: 0.55rem; }
.skw .skw-hero h1 {
  margin: 0 0 0.75rem; border: 0; padding: 0;
  font-size: clamp(2rem, 6.4vw, 3.4rem); line-height: 1.04; font-weight: 800; letter-spacing: -0.03em; color: #fff;
}
.skw .skw-lede { max-width: 60ch; color: var(--mute); font-size: 1.05rem; }
.skw .skw-gun { display: block; width: 100%; height: auto; margin-top: 1.2rem; }
.skw-gun .body { fill: #1c1c21; stroke: #3f3f46; stroke-width: 2; stroke-linejoin: round; }
.skw-gun .line { fill: none; stroke: #52525b; stroke-width: 1.5; stroke-linejoin: round; }
.skw-gun .shine { fill: #fff; opacity: 0.07; }
.skw-gun .wrap { opacity: 0; animation: skw-wrap 15s cubic-bezier(.5, .05, .25, 1) infinite both; }
.skw-gun .wrap.w2 { animation-delay: 5s; }
.skw-gun .wrap.w3 { animation-delay: 10s; }
.skw-gun .edge { fill: #fff; opacity: 0.85; }
@keyframes skw-wrap {
  0% { transform: translateX(-640px); opacity: 1; }
  10% { transform: translateX(0); opacity: 1; }
  30% { transform: translateX(0); opacity: 1; }
  33.3%, 100% { transform: translateX(0); opacity: 0; }
}
.skw-gun .spark { fill: #fde68a; transform-box: fill-box; transform-origin: center; animation: skw-spark 3s ease-in-out infinite; }
.skw-gun .spark:nth-of-type(2) { animation-delay: -0.8s; fill: #fff; }
.skw-gun .spark:nth-of-type(3) { animation-delay: -1.6s; fill: #c4b5fd; }
.skw-gun .spark:nth-of-type(4) { animation-delay: -2.3s; }
@keyframes skw-spark { 0%, 100% { opacity: 0; transform: scale(0.3) rotate(0deg); } 50% { opacity: 0.95; transform: scale(1) rotate(45deg); } }
.skw .skw-facts { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 160px), 1fr)); gap: 0.6rem; margin-top: 1.2rem; }
.skw .skw-facts li { background: rgba(23, 23, 26, 0.85); border: 1px solid var(--line); border-radius: 14px; padding: 0.7rem 0.9rem; }
.skw .skw-facts span { display: block; font-size: 0.72rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: var(--mute); }
.skw .skw-facts b { display: block; margin-top: 0.15rem; font-size: 1.02rem; }
@media (prefers-reduced-motion: reduce) {
  .skw-gun .wrap, .skw-gun .spark { animation: none; }
  .skw-gun .wrap.w1 { opacity: 1; transform: none; }
  .skw-gun .wrap.w2, .skw-gun .wrap.w3, .skw-gun .edge { opacity: 0; }
  .skw-gun .spark { opacity: 0.8; }
}
/* ---------- sections ---------- */
.skw .skw-h2 {
  display: flex; align-items: center; gap: 0.65rem;
  margin: 3rem 0 0.9rem; border: 0; padding: 0;
  font-size: 1.5rem; font-weight: 750; letter-spacing: -0.015em; line-height: 1.25; color: #fff;
}
.skw .skw-h2::before {
  content: ''; flex: none; width: 0.6rem; height: 0.6rem; border-radius: 2px; background: var(--red);
  transform: rotate(45deg); box-shadow: 0 0 0 4px var(--red-soft);
}
.skw .skw-intro { color: var(--mute); max-width: 68ch; margin-bottom: 1rem; }
.skw .skw-card { background: var(--panel); border: 1px solid var(--line); border-radius: 18px; padding: 1.1rem 1.2rem; }
.skw .skw-h3 { margin: 0 0 0.55rem; border: 0; padding: 0; font-size: 1.08rem; font-weight: 750; color: #fff; line-height: 1.3; }
.skw .skw-two { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 300px), 1fr)); gap: 0.8rem; }
.skw .skw-list li { position: relative; padding-left: 1.1rem; color: #d4d4d8; }
.skw .skw-list li + li { margin-top: 0.4rem; }
.skw .skw-list li::before { content: ''; position: absolute; left: 0; top: 0.62em; width: 6px; height: 6px; border-radius: 50%; background: var(--red); }
/* steps */
.skw .skw-steps { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr)); gap: 0.7rem; counter-reset: skw; }
.skw .skw-steps li { position: relative; background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 2.6rem 1rem 1rem; counter-increment: skw; }
.skw .skw-steps li::before {
  content: counter(skw); position: absolute; top: 0.8rem; left: 1rem;
  width: 1.6rem; height: 1.6rem; border-radius: 8px; display: grid; place-items: center;
  font-weight: 800; font-size: 0.9rem; color: #fff; background: var(--red-deep);
}
.skw .skw-steps .t { display: block; margin-bottom: 0.2rem; font-weight: 700; color: #fff; font-size: 1rem; }
.skw .skw-steps span { color: var(--mute); font-size: 0.92rem; }
/* menu */
.skw .skw-menu { display: grid; gap: 0.45rem; margin-top: 0.8rem; }
.skw .skw-menu li { display: block; background: var(--panel2); border: 1px solid var(--line); border-radius: 12px; padding: 0.55rem 0.8rem; }
.skw .skw-menu .t { display: block; font-weight: 700; color: #fff; font-size: 1rem; }
.skw .skw-menu span { color: var(--mute); font-size: 0.92rem; }
/* materials */
.skw .skw-mats { display: grid; gap: 0.8rem; }
.skw .skw-mat-row { display: flex; flex-wrap: wrap; gap: 0.45rem; margin-top: 0.6rem; }
.skw .skw-chip {
  display: inline-flex; align-items: center; gap: 0.45rem; font-size: 0.86rem; font-weight: 600; color: #e4e4e7;
  background: var(--panel2); border: 1px solid var(--line); border-radius: 999px; padding: 0.25rem 0.75rem 0.25rem 0.35rem;
}
.skw .skw-chip i { width: 1.1rem; height: 1.1rem; border-radius: 50%; background: var(--c); border: 1px solid rgba(255, 255, 255, 0.25); flex: none; }
.skw .skw-chip i.flake { background: radial-gradient(circle at 30% 30%, #fff 0 12%, transparent 13%), radial-gradient(circle at 70% 60%, #fff 0 10%, transparent 11%), var(--c); }
.skw .skw-chip i.leaf { border-radius: 3px; transform: rotate(12deg); background: linear-gradient(135deg, #fff8 0%, transparent 45%), var(--c); }
/* recipe */
.skw .skw-recipe { display: flex; flex-wrap: wrap; align-items: center; gap: 0.5rem; margin-top: 0.4rem; }
.skw .skw-recipe .part { background: var(--panel2); border: 1px solid var(--line); border-radius: 12px; padding: 0.5rem 0.8rem; font-weight: 650; }
.skw .skw-recipe .part small { display: block; font-weight: 500; font-size: 0.78rem; color: var(--mute); }
.skw .skw-recipe .op { color: var(--red); font-weight: 800; font-size: 1.2rem; }
.skw .skw-tone { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 180px), 1fr)); gap: 0.5rem; margin-top: 0.9rem; }
.skw .skw-tone li { background: var(--panel2); border: 1px solid var(--line); border-radius: 12px; padding: 0.6rem 0.8rem; font-size: 0.9rem; color: #d4d4d8; }
.skw .skw-tone b { display: block; }
.skw .skw-scale { display: flex; flex-wrap: wrap; gap: 0.35rem; align-items: center; margin-top: 0.5rem; font-size: 0.88rem; }
.skw .skw-scale span { background: var(--panel2); border: 1px solid var(--line); border-radius: 8px; padding: 0.2rem 0.6rem; }
.skw .skw-scale em { font-style: normal; color: var(--red); font-weight: 800; }
@media (min-width: 561px) { .skw .skw-recipe .part { flex: 1 1 auto; } }
@media (max-width: 560px) {
  .skw .skw-recipe, .skw .skw-scale { flex-direction: column; align-items: stretch; }
  .skw .skw-recipe .op, .skw .skw-scale em { align-self: center; line-height: 1; }
}
/* tiers */
.skw .skw-tiers { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr)); gap: 0.6rem; }
.skw .skw-tier { position: relative; background: var(--panel); border: 1px solid var(--line); border-left: 4px solid var(--c); border-radius: 14px; padding: 0.75rem 0.9rem; }
.skw .skw-tier .name { display: block; font-weight: 800; color: var(--c); letter-spacing: 0.02em; }
.skw .skw-tier .how { display: block; font-size: 0.9rem; color: #e4e4e7; margin-top: 0.15rem; }
.skw .skw-tier .mat { display: block; font-size: 0.82rem; color: var(--mute); margin-top: 0.2rem; }
.skw .skw-note { margin-top: 0.9rem; background: rgba(239, 68, 68, 0.08); border: 1px solid rgba(239, 68, 68, 0.35); border-radius: 14px; padding: 0.75rem 0.95rem; color: #e4e4e7; }
/* cta */
.skw .skw-cta {
  display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 0.8rem;
  margin-top: 3rem; background: linear-gradient(120deg, rgba(185, 28, 28, 0.25), var(--panel) 60%);
  border: 1px solid var(--line); border-radius: 18px; padding: 1.1rem 1.2rem;
}
.skw .skw-cta p { color: #d4d4d8; max-width: 52ch; }
.skw .skw-btn {
  display: inline-block; text-decoration: none; font-weight: 750; color: #fff; background: var(--red-deep);
  border-radius: 12px; padding: 0.6rem 1.1rem;
}
.skw .skw-btn:hover { color: #fff; background: #dc2626; }
</style>

<div class="skw">
<header class="skw-hero">
<p class="skw-kicker">Sisteme generale</p>
<h1>Skin-uri arme</h1>
<p class="skw-lede">Un skin schimba aspectul armei tale. Strangi materiale din butoaiele de la plantatia de mac, deblochezi skin-ul pe arma pe care o vrei, faci folia la atelier si o lipesti pe arma cu un cutter.</p>
<svg class="skw-gun" viewBox="0 0 640 200" role="img" aria-label="O arma pe care se aplica pe rand trei folii de skin">
<defs>
<pattern id="skw-p1" width="26" height="26" patternUnits="userSpaceOnUse" patternTransform="rotate(35)"><rect width="26" height="26" fill="#ec4899"/><rect width="9" height="26" fill="#fbcfe8"/><rect x="13" width="4" height="26" fill="#9d174d"/></pattern>
<pattern id="skw-p2" width="60" height="44" patternUnits="userSpaceOnUse"><rect width="60" height="44" fill="#3f4a1f"/><ellipse cx="14" cy="12" rx="14" ry="8" fill="#65733a"/><ellipse cx="44" cy="30" rx="16" ry="9" fill="#1f2612"/><ellipse cx="38" cy="8" rx="8" ry="5" fill="#a3a07a"/><ellipse cx="8" cy="36" rx="9" ry="6" fill="#1f2612"/></pattern>
<linearGradient id="skw-g3" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f97316"/><stop offset="0.5" stop-color="#facc15"/><stop offset="1" stop-color="#b45309"/></linearGradient>
<pattern id="skw-p3" width="22" height="22" patternUnits="userSpaceOnUse" patternTransform="rotate(-30)"><rect width="22" height="22" fill="url(#skw-g3)"/><rect width="3" height="22" fill="#fff7cc" opacity="0.55"/></pattern>
<clipPath id="skw-clip"><path d="M22 82h18v16h-18z M40 86h112v8h-112z M160 58h8v16h-8z M150 74h152v30h-152z M290 62h142v8h-142z M300 70h132v34h-132z M318 104h124v14h-124z M335 118h30l16 56-28 6z M404 118h28l-12 50-22-4z M430 80h42v16h-42z M470 72L580 80L590 128L560 132L500 106L470 104z"/></clipPath>
</defs>
<path class="body" d="M22 82h18v16h-18z M40 86h112v8h-112z M160 58h8v16h-8z M150 74h152v30h-152z M290 62h142v8h-142z M300 70h132v34h-132z M318 104h124v14h-124z M335 118h30l16 56-28 6z M404 118h28l-12 50-22-4z M430 80h42v16h-42z M470 72L580 80L590 128L560 132L500 106L470 104z"/>
<g clip-path="url(#skw-clip)">
<g class="wrap w1"><rect x="0" y="40" width="640" height="150" fill="url(#skw-p1)"/><rect class="edge" x="636" y="40" width="4" height="150"/></g>
<g class="wrap w2"><rect x="0" y="40" width="640" height="150" fill="url(#skw-p2)"/><rect class="edge" x="636" y="40" width="4" height="150"/></g>
<g class="wrap w3"><rect x="0" y="40" width="640" height="150" fill="url(#skw-p3)"/><rect class="edge" x="636" y="40" width="4" height="150"/></g>
<rect class="shine" x="0" y="54" width="640" height="14"/>
</g>
<path class="line" d="M170 84h110M170 94h110M300 70v34M340 78h50v12h-50zM432 70v48"/>
<path class="spark" d="M250 30l4 10 10 4-10 4-4 10-4-10-10-4 10-4z"/>
<path class="spark" d="M470 36l3 7 7 3-7 3-3 7-3-7-7-3 7-3z"/>
<path class="spark" d="M560 150l4 9 9 4-9 4-4 9-4-9-9-4 9-4z"/>
<path class="spark" d="M120 132l3 7 7 3-7 3-3 7-3-7-7-3 7-3z"/>
</svg>
<ul class="skw-facts">
<li><span>Atelier</span><b>Sandy Shores</b></li>
<li><span>Materiale</span><b>Butoaie, plantatia de mac</b></li>
<li><span>Unealta</span><b>Cutter</b></li>
</ul>
</header>
<h2 class="skw-h2" id="pe-scurt">Pe scurt</h2>
<ol class="skw-steps">
<li><span class="t">Strangi materiale</span><span>Cauti in butoaiele de la plantatia de mac: vinil, pigmenti, fulgi si foite.</span></li>
<li><span class="t">Deblochezi skin-ul</span><span>O singura data, pentru fiecare skin pe fiecare arma.</span></li>
<li><span class="t">Faci folia</span><span>La atelier, din <b>Creeaza skin</b>. Primesti o <b>Folie skin</b> pentru arma aleasa.</span></li>
<li><span class="t">Lipesti folia</span><span>Tot la atelier, din <b>Aplica skin</b>, cu un cutter si un minigame.</span></li>
</ol>
<h2 class="skw-h2" id="atelier">Atelierul</h2>
<div class="skw-two">
<div class="skw-card">
<h3 class="skw-h3">Atelier skin-uri</h3>
<p>E in <b>Sandy Shores</b>. Pe harta il gasesti dupa iconita mov <b>Crafting Skin-uri</b>. Apropie-te de banc si apasa <kbd>E</kbd>.</p>
<ul class="skw-menu">
<li><span class="t">Creeaza skin</span><span>Deblochezi skin-uri si faci folii.</span></li>
<li><span class="t">Aplica skin</span><span>Pui o folie pe arma ei.</span></li>
<li><span class="t">Scoate skin</span><span>Scoti skin-ul de pe arma. Skin-ul se distruge.</span></li>
<li><span class="t">Catalog skin-uri</span><span>Deschide <a href="./skin-uri-arme-catalog">catalogul</a> cu toate skin-urile pe arme.</span></li>
</ul>
</div>
<div class="skw-card">
<h3 class="skw-h3">Atelier skin-uri Politie</h3>
<p>La sectia de politie din Vespucci e un banc doar pentru politisti. Acolo aplici si scoti <b>doar skin-urile Politie</b>. Nu poti face folii si nu poti debloca skin-uri acolo.</p>
<ul class="skw-list" style="margin-top:0.8rem">
<li>Skin-urile Politie le poti pune si la atelierul din Sandy Shores.</li>
<li>Nu poti lucra la banc din masina.</li>
</ul>
</div>
</div>
<h2 class="skw-h2" id="materiale">Materiale</h2>
<p class="skw-intro">Toate materialele vin din butoaiele de la <b>plantatia de mac</b>. Zona e un No Man's Land: acolo oricine te poate ataca si jefui.</p>
<div class="skw-mats">
<div class="skw-card">
<h3 class="skw-h3">Cum cauti</h3>
<ul class="skw-list">
<li>Apropie-te de un butoi si apasa <kbd>E</kbd> la <b>Cauta in butoi</b>. Cauti cateva secunde, apoi se deschide butoiul si iei ce e in el.</li>
<li>Unele butoaie sunt goale. Dupa ce cauti intr-un butoi, apare imediat altul, in alt loc din zona.</li>
<li>Dupa multe cautari la rand obosesti si trebuie sa faci o pauza scurta.</li>
<li>Politistii si medicii nu pot cauta in butoaie.</li>
</ul>
</div>
<div class="skw-card">
<h3 class="skw-h3">Ce gasesti</h3>
<div class="skw-mat-row">
<span class="skw-chip"><i style="--c:#e5e7eb"></i>Folie de vinil</span>
</div>
<div class="skw-mat-row">
<span class="skw-chip"><i style="--c:#111"></i>Pigment negru</span>
<span class="skw-chip"><i style="--c:#fafafa"></i>Pigment alb</span>
<span class="skw-chip"><i style="--c:#dc2626"></i>Pigment rosu</span>
<span class="skw-chip"><i style="--c:#16a34a"></i>Pigment verde</span>
<span class="skw-chip"><i style="--c:#2563eb"></i>Pigment albastru</span>
<span class="skw-chip"><i style="--c:#facc15"></i>Pigment galben</span>
<span class="skw-chip"><i style="--c:#f97316"></i>Pigment portocaliu</span>
<span class="skw-chip"><i style="--c:#9333ea"></i>Pigment mov</span>
<span class="skw-chip"><i style="--c:#ec4899"></i>Pigment roz</span>
<span class="skw-chip"><i style="--c:#14b8a6"></i>Pigment turcoaz</span>
</div>
<div class="skw-mat-row">
<span class="skw-chip"><i class="flake" style="--c:#9ca3af"></i>Fulgi metalici</span>
<span class="skw-chip"><i class="flake" style="--c:#b45309"></i>Fulgi de cupru</span>
<span class="skw-chip"><i class="flake" style="--c:#a78bfa"></i>Fulgi holografici</span>
<span class="skw-chip"><i class="leaf" style="--c:#eab308"></i>Foita de aur</span>
<span class="skw-chip"><i class="leaf" style="--c:#cbd5e1"></i>Foita de argint</span>
</div>
</div>
</div>
<h2 class="skw-h2" id="reteta">Din ce se face un skin</h2>
<p class="skw-intro">Reteta e aceeasi regula pentru orice skin. Lista exacta de materiale o vezi la atelier, pe fiecare skin.</p>
<div class="skw-card">
<div class="skw-recipe">
<span class="part">Folie de vinil<small>la orice skin</small></span><span class="op">+</span>
<span class="part">Pigmentii culorilor lui<small>ex. skin galben-albastru: galben si albastru</small></span><span class="op">+</span>
<span class="part">Fulgi sau foite<small>doar la nivelurile mai rare</small></span>
</div>
<ul class="skw-tone">
<li><b>Ton cald</b>Fulgi de cupru, foita de aur</li>
<li><b>Ton rece</b>Fulgi metalici, foita de argint</li>
<li><b>Holografic</b>Fulgi holografici, foita de argint</li>
</ul>
<p style="margin-top:1rem;color:#d4d4d8">Cu cat arma e mai buna, cu atat folia cere mai multe materiale:</p>
<div class="skw-scale"><span>Corp la corp</span><em>&lt;</em><span>Pistoale</span><em>&lt;</em><span>SMG-uri si shotgun-uri</span><em>&lt;</em><span>Pusti</span></div>
<p style="margin-top:0.9rem;color:#d4d4d8">Folia o faci pentru <b>o anumita arma</b> si primesti o <b>Folie skin</b> cu numele ei, de exemplu <b>Skin Camuflaj - SMG Mk2</b>. O pui pe arma cand vrei, nu trebuie aplicata imediat.</p>
</div>
<h2 class="skw-h2" id="niveluri">Niveluri si deblocare</h2>
<p class="skw-intro">Inainte sa faci sau sa pui un skin, il deblochezi <b>pe arma respectiva</b>. Deblocarea pe Assault Rifle nu merge si pe Micro SMG. La <b>Creeaza skin</b>, skin-urile blocate au lacat: tii apasat <kbd>E</kbd> ca sa platesti deblocarea.</p>
<div class="skw-tiers">
<div class="skw-tier" style="--c:#9ca3af"><span class="name">Comun</span><span class="how">Deblocare cu bani murdari</span><span class="mat">Vinil + pigmenti</span></div>
<div class="skw-tier" style="--c:#3b82f6"><span class="name">Deosebit</span><span class="how">Deblocare cu bani murdari</span><span class="mat">Vinil + pigmenti</span></div>
<div class="skw-tier" style="--c:#a855f7"><span class="name">Rar</span><span class="how">Deblocare cu bani murdari</span><span class="mat">Vinil + pigmenti + fulgi</span></div>
<div class="skw-tier" style="--c:#ec4899"><span class="name">Contrabanda</span><span class="how">Deblocare cu bani murdari</span><span class="mat">Vinil + pigmenti + fulgi</span></div>
<div class="skw-tier" style="--c:#f97316"><span class="name">Legendar</span><span class="how">Deblocare cu bani murdari</span><span class="mat">Vinil + pigmenti + foite</span></div>
<div class="skw-tier" style="--c:#facc15"><span class="name">Premium</span><span class="how">Deblocare cu EG Coins</span><span class="mat">Vinil + pigmenti + foite, sau folia gata, tot cu EG Coins</span></div>
<div class="skw-tier" style="--c:#14b8a6"><span class="name">Eveniment Special</span><span class="how">Nu se cumpara: o primesti din evenimente, pe o anumita arma</span><span class="mat">Dupa aceea faci folia la atelier, din vinil + pigmenti</span></div>
<div class="skw-tier" style="--c:#ff2a2a"><span class="name">Sindicat</span><span class="how">Doar pentru membrii factiunii Sindicat</span><span class="mat">Nu se deblocheaza si nu se face la atelier: folia o primesti de la staff</span></div>
<div class="skw-tier" style="--c:#38bdf8"><span class="name">Politie</span><span class="how">Doar pentru politisti</span><span class="mat">Nu se deblocheaza si nu se face la atelier: folia o primesti de la staff</span></div>
</div>
<ul class="skw-list" style="margin-top:1rem">
<li>Cu cat skin-ul e mai rar, cu atat cere mai multe materiale si deblocarea costa mai mult. Pretul creste si cu arma.</li>
<li>Bani murdari platesti din inventar.</li>
<li>Deblocarea iti da dreptul sa faci si sa pui skin-ul pe arma aceea. <b>Nu primesti si folia</b>: o faci separat, din materiale.</li>
<li>La skin-urile Premium deblocate poti alege <b>folia gata</b>, platita cu EG Coins, in loc sa o faci din materiale.</li>
</ul>
<p class="skw-note">La <b>Character Kill</b> pastrezi doar deblocarile platite cu EG Coins. Pe cele platite cu bani murdari si pe cele din evenimente le pierzi.</p>
<h2 class="skw-h2" id="aplicare">Aplicare si scoatere</h2>
<div class="skw-two">
<div class="skw-card">
<h3 class="skw-h3">Aplica skin</h3>
<ul class="skw-list">
<li>La atelier alegi <b>Aplica skin</b>, arma, apoi folia facuta pentru ea.</li>
<li>Ai nevoie de skin-ul deblocat pe acea arma si de un <b>cutter</b> (il cumperi de la magazinul Home Depot).</li>
<li>Treci printr-un minigame. La final folia si cutter-ul se consuma, iar skin-ul ramane pe arma.</li>
<li>O arma poate avea un singur skin.</li>
</ul>
</div>
<div class="skw-card">
<h3 class="skw-h3">Scoate skin</h3>
<ul class="skw-list">
<li>La atelier alegi <b>Scoate skin</b> si arma.</li>
<li>Esti intrebat daca esti sigur: <b>skin-ul scos se distruge</b>, nu il primesti inapoi.</li>
<li>Ai nevoie tot de un <b>cutter</b> si treci prin acelasi minigame. Cutter-ul se consuma.</li>
</ul>
</div>
</div>
<h2 class="skw-h2" id="bune-de-stiut">Bune de stiut</h2>
<div class="skw-card">
<ul class="skw-list">
<li>Foliile se pot <b>da sau vinde</b> ca orice obiect. Cine o primeste o poate aplica doar daca are si el skin-ul deblocat pe acea arma.</li>
<li>Un skin pus pe arma ramane pe ea si se vede si daca arma ajunge la alt jucator.</li>
<li>Cand treci cu mouse-ul peste arma in inventar, vezi ce skin are.</li>
<li>Skin-urile Sindicat si Politie le pot pune doar membrii lor. Oricine le poate scoate, dar se distrug.</li>
</ul>
</div>
<div class="skw-cta">
<p>Vrei sa vezi ce skin-uri are fiecare arma, pe niveluri? Il gasesti si la atelier, la <b>Catalog skin-uri</b>.</p>
<a class="skw-btn" href="./skin-uri-arme-catalog">Deschide catalogul</a>
</div>
</div>
