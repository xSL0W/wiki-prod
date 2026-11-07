---
outline: false
---

<style>
.att {
  --ink: #0c0c0e;
  --panel: #18181b;
  --panel2: #202024;
  --line: #34343b;
  --text: #f4f4f5;
  --mute: #a1a1aa;
  --red: #dc2626;
  --acc: #a78bfa;
  --acc-soft: rgba(167, 139, 250, 0.13);
  max-width: 960px;
  margin: 0 auto;
  color: var(--text);
}
.att *, .att *::before, .att *::after { box-sizing: border-box; }
.att p, .att li { margin: 0; line-height: 1.6; color: var(--text); }
.att ul, .att ol { list-style: none; padding: 0; margin: 0; }
.att li + li { margin-top: 0; }
.att b { color: #fff; font-weight: 650; }
.att code { white-space: normal; overflow-wrap: anywhere; }
.att a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.att a:hover { color: #fecaca; }
.att a:focus-visible { outline: 3px solid var(--acc); outline-offset: 3px; border-radius: 6px; }
/* hero */
.att .att-hero {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr)); gap: 1.5rem; align-items: center;
  background: radial-gradient(90% 120% at 100% 0%, rgba(167, 139, 250, 0.15), transparent 60%),
              radial-gradient(110% 120% at 0% 100%, rgba(185, 28, 28, 0.26), var(--ink) 65%);
  border: 1px solid var(--line); border-radius: 22px; padding: clamp(1.25rem, 4vw, 2.5rem); overflow: hidden;
}
.att .att-kicker { font-size: 0.78rem; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: var(--acc); margin-bottom: 0.6rem; }
.att .att-hero h1 {
  margin: 0 0 0.8rem; border: 0; padding: 0;
  font-size: clamp(2.1rem, 7vw, 3.3rem); line-height: 1.02; font-weight: 800; letter-spacing: -0.03em; color: #fff;
}
.att .att-lede { color: var(--mute); font-size: 1.05rem; max-width: 46ch; }
.att .att-art { display: block; width: 100%; max-width: 240px; height: auto; margin: 0 auto; }
.att-art path, .att-art circle, .att-art line { fill: none; stroke-linecap: round; stroke-linejoin: round; }
.att-art .ink { stroke: var(--text); stroke-width: 3; stroke-dasharray: 700; stroke-dashoffset: 0; animation: att-draw 7s ease-in-out infinite; }
.att-art .ink.red { stroke: var(--red); }
.att-art .ink.violet { stroke: var(--acc); }
.att-art .spark { stroke: var(--acc); stroke-width: 2.5; }
@keyframes att-draw { 0% { stroke-dashoffset: 700; } 45%, 85% { stroke-dashoffset: 0; } 100% { stroke-dashoffset: -700; } }
/* facts */
.att .att-facts { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 190px), 1fr)); gap: 0.7rem; margin-top: 1rem; }
.att .att-facts li { background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 0.9rem 1rem; }
.att .att-facts b { display: block; font-size: 1.5rem; line-height: 1.1; color: var(--acc); font-variant-numeric: tabular-nums; }
.att .att-facts span { color: var(--mute); font-size: 0.92rem; }
/* sections */
.att h2 {
  display: flex; align-items: flex-start; gap: 0.65rem;
  margin: 3rem 0 1rem; border: 0; padding: 0;
  font-size: 1.45rem; font-weight: 750; letter-spacing: -0.015em; color: #fff;
}
.att h2::before { margin-top: calc(0.5lh - 3px / 2); content: ''; flex: none; width: 1.4rem; height: 3px; border-radius: 3px; background: linear-gradient(90deg, var(--acc), var(--red)); }
.att .att-sub { color: var(--mute); margin: -0.4rem 0 1rem; max-width: 64ch; }
/* body zones */
.att .att-zones { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 140px), 1fr)); gap: 0.6rem; }
.att .att-zones li {
  background: var(--panel); border: 1px solid var(--line); border-radius: 12px; padding: 0.7rem 0.9rem;
  font-weight: 650; text-align: center; border-bottom: 2px solid var(--acc);
}
/* session steps */
.att .att-session { display: grid; gap: 0.6rem; margin-top: 1rem; }
.att .att-session li {
  display: grid; grid-template-columns: 2.6rem minmax(0, 1fr); gap: 0.8rem; align-items: start;
  background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 0.85rem 1rem;
}
.att .att-session li > span {
  display: grid; place-items: center; width: 2.6rem; height: 2.6rem; border-radius: 50%;
  border: 2px dashed var(--acc); color: var(--acc); font-weight: 800;
}
.att .att-session p { color: var(--mute); }
.att .att-session b { display: block; color: #fff; }
/* consumables */
.att .att-kit { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 240px), 1fr)); gap: 0.8rem; }
.att .att-item {
  background: linear-gradient(180deg, var(--acc-soft), var(--panel) 60%); border: 1px solid var(--line);
  border-radius: 16px; padding: 1rem 1.1rem;
}
.att .att-item b { display: block; font-size: 1.05rem; }
.att .att-item span { color: var(--mute); font-size: 0.93rem; }
.att .att-notes { display: grid; gap: 0.5rem; margin-top: 1rem; }
.att .att-notes li { position: relative; padding-left: 1.3rem; color: var(--mute); }
.att .att-notes li::before { content: ''; position: absolute; left: 0.15rem; top: 0.55em; width: 0.55rem; height: 0.55rem; border-radius: 50% 50% 50% 0; background: var(--acc); transform: rotate(-45deg); }
/* locations */
.att .att-locs { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 220px), 1fr)); gap: 0.7rem; }
.att .att-loc { background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 0.9rem 1rem; }
.att .att-loc b { display: block; }
.att .att-loc span { display: block; margin-top: 0.35rem; color: var(--mute); font-size: 0.9rem; }
.att .att-loc code { color: var(--acc); }
.att .att-foot { margin-top: 2.5rem; padding: 1rem 1.2rem; border: 1px dashed var(--line); border-radius: 14px; color: var(--mute); }
@media (prefers-reduced-motion: reduce) {
  .att-art .ink { animation: none; stroke-dasharray: none; }
}
</style>

<div class="att">
<section class="att-hero">
<div>
<p class="att-kicker">Afaceri · Locatii</p>
<h1>Salon de tatuaje</h1>
<p class="att-lede">Aici iti faci tatuaje. Salonul e o firma: conducerea pune preturile, iar angajatii aduc masinile de tatuaj si cerneala fara de care salonul nu poate lucra.</p>
</div>
<svg class="att-art" viewBox="0 0 240 240" role="img" aria-label="Desen de tatuaj: inima strapunsa de un pumnal">
<path class="ink red" d="M120 196C62 156 36 118 64 86c18-20 44-14 56 10 12-24 38-30 56-10 28 32 2 70-56 110z"/>
<path class="ink" d="M112 60h16v128l-8 22-8-22z"/>
<path class="ink" d="M90 56h60M120 56V30"/>
<circle class="ink" cx="120" cy="22" r="7"/>
<path class="ink violet" d="M40 124h160l12 14-12 14H40l-12-14z"/>
<path class="spark" d="M196 52v16M188 60h16M48 182v12M42 188h12M200 186v10M195 191h10"/>
</svg>
</section>
<ul class="att-facts">
<li><b>3</b><span>saloane de tatuaje pe harta</span></li>
<li><b>6</b><span>zone ale corpului</span></li>
<li><b>1 + 1</b><span>masina de tatuaj si cerneala la fiecare tatuaj</span></li>
</ul>
<h2>Unde te poti tatua</h2>
<p class="att-sub">Pretul e pe tatuaj si depinde de zona. Il pune conducerea salonului, pana la un plafon.</p>
<ul class="att-zones">
<li>Cap</li><li>Torso</li><li>Brat stang</li><li>Brat drept</li><li>Picior stang</li><li>Picior drept</li>
</ul>
<ol class="att-session">
<li><span>1</span><p><b>Intri in salon</b>Salonul se deschide doar daca are in stoc cel putin o masina de tatuaj si o cerneala. Altfel primesti mesajul ca nu are stoc.</p></li>
<li><span>2</span><p><b>Alegi tatuajele</b>Meniul iti arata cate tatuaje mai acopera stocul, ca sa nu alegi mai multe decat poate face salonul.</p></li>
<li><span>3</span><p><b>Platesti si pleci tatuat</b>Fiecare tatuaj consuma o masina si o cerneala din stocul salonului.</p></li>
</ol>
<h2>Cum aprovizionezi salonul</h2>
<p class="att-sub">Pentru angajatii unui salon de tatuaje. Stocul il vezi oricand in Tableta firma, la Stoc.</p>
<div class="att-kit">
<div class="att-item"><b>Masina de tatuaj</b><span>Se consuma una la fiecare tatuaj.</span></div>
<div class="att-item"><b>Cerneala tatuaj</b><span>Se consuma una la fiecare tatuaj.</span></div>
</div>
<ul class="att-notes">
<li>Le cumperi de la Furnizor Tatuaje, langa ceilalti furnizori, la codul postal <code>313</code>. Vinde doar angajatilor unui salon de tatuaje si platesti din banii tai.</li>
<li>Primesti o cutie de consumabile. O deschizi langa salonul tau si continutul intra direct in stocul firmei. Ce trece peste limita de stoc ramane in cutie.</li>
<li>Preturile pe zone le schimba conducerea din Tableta firma, la Preturi.</li>
<li>Firma primeste o parte din fiecare tatuaj vandut. Partea creste cu fiecare angajat pontat aflat la cel mult 100 m de salon, pana la o limita.</li>
</ul>
<h2>Locatii</h2>
<p class="att-sub">Scrie in chat <code>/cod</code> si numarul de mai jos, ca sa pui punct pe harta.</p>
<ul class="att-locs">
<li class="att-loc"><b>Vespucci Canals</b><span>Cod postal <code>696</code></span></li>
<li class="att-loc"><b>Downtown Vinewood</b><span>Cod postal <code>596</code></span></li>
<li class="att-loc"><b>El Burro Heights</b><span>Cod postal <code>792</code></span></li>
</ul>
<p class="att-foot">Cum cumperi o firma, cum angajezi oameni si cum se platesc salariile afli la <a href="/afaceri/elite-business-center">Elite Business Center</a>.</p>
</div>
