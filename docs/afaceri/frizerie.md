---
outline: false
---

<style>
.afz {
  --ink: #0c0c0e;
  --panel: #18181b;
  --panel2: #202024;
  --line: #34343b;
  --text: #f4f4f5;
  --mute: #a1a1aa;
  --red: #dc2626;
  --acc: #60a5fa;
  --acc-soft: rgba(96, 165, 250, 0.13);
  max-width: 960px;
  margin: 0 auto;
  color: var(--text);
}
.afz *, .afz *::before, .afz *::after { box-sizing: border-box; }
.afz p, .afz li { margin: 0; line-height: 1.6; color: var(--text); }
.afz ul, .afz ol { list-style: none; padding: 0; margin: 0; }
.afz li + li { margin-top: 0; }
.afz b { color: #fff; font-weight: 650; }
.afz code { white-space: normal; overflow-wrap: anywhere; }
.afz a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.afz a:hover { color: #fecaca; }
.afz a:focus-visible { outline: 3px solid var(--acc); outline-offset: 3px; border-radius: 6px; }
/* hero */
.afz .afz-hero {
  display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: 1.5rem; align-items: center;
  background: radial-gradient(90% 120% at 100% 0%, rgba(96, 165, 250, 0.14), transparent 60%),
              radial-gradient(110% 120% at 0% 100%, rgba(185, 28, 28, 0.26), var(--ink) 65%);
  border: 1px solid var(--line); border-radius: 22px; padding: clamp(1.25rem, 4vw, 2.5rem); overflow: hidden;
}
.afz .afz-kicker { font-size: 0.78rem; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: var(--acc); margin-bottom: 0.6rem; }
.afz .afz-hero h1 {
  margin: 0 0 0.8rem; border: 0; padding: 0;
  font-size: clamp(2.1rem, 7vw, 3.3rem); line-height: 1.02; font-weight: 800; letter-spacing: -0.03em; color: #fff;
}
.afz .afz-lede { color: var(--mute); font-size: 1.05rem; max-width: 46ch; }
/* barber pole */
.afz .afz-pole { display: flex; flex-direction: column; align-items: center; width: clamp(56px, 12vw, 84px); }
.afz .afz-cap { width: 100%; height: 14px; border-radius: 8px; background: linear-gradient(180deg, #d4d4d8, #71717a); }
.afz .afz-cap.top { border-radius: 40px 40px 6px 6px; height: 22px; }
.afz .afz-tube {
  width: 78%; height: clamp(150px, 30vw, 210px); border-radius: 6px; overflow: hidden; position: relative;
  background: repeating-linear-gradient(-45deg, var(--red) 0 14px, #f4f4f5 14px 28px, var(--acc) 28px 42px, #f4f4f5 42px 56px);
  background-size: 100% 158px; animation: afz-pole 3s linear infinite;
  box-shadow: inset 8px 0 12px rgba(0, 0, 0, 0.35), inset -8px 0 12px rgba(0, 0, 0, 0.45);
}
@keyframes afz-pole { from { background-position: 0 0; } to { background-position: 0 158px; } }
@media (max-width: 480px) {
  .afz .afz-hero { grid-template-columns: minmax(0, 1fr); }
  .afz .afz-pole { flex-direction: row; width: 100%; height: 44px; }
  .afz .afz-cap, .afz .afz-cap.top { width: 14px; height: 100%; border-radius: 6px; }
  .afz .afz-tube { width: auto; flex: 1; height: 70%; background-size: 158px 100%; animation-name: afz-pole-x; }
}
@keyframes afz-pole-x { from { background-position: 0 0; } to { background-position: 158px 0; } }
/* facts */
.afz .afz-facts { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 190px), 1fr)); gap: 0.7rem; margin-top: 1rem; }
.afz .afz-facts li { background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 0.9rem 1rem; }
.afz .afz-facts b { display: block; font-size: 1.5rem; line-height: 1.1; color: var(--acc); font-variant-numeric: tabular-nums; }
.afz .afz-facts span { color: var(--mute); font-size: 0.92rem; }
/* sections */
.afz h2 {
  display: flex; align-items: flex-start; gap: 0.65rem;
  margin: 3rem 0 1rem; border: 0; padding: 0;
  font-size: 1.45rem; font-weight: 750; letter-spacing: -0.015em; color: #fff;
}
.afz h2::before { margin-top: calc(0.5lh - 1.3rem / 2);
  content: ''; flex: none; width: 0.6rem; height: 1.3rem; border-radius: 3px;
  background: repeating-linear-gradient(-45deg, var(--red) 0 4px, #f4f4f5 4px 8px, var(--acc) 8px 12px, #f4f4f5 12px 16px);
}
.afz .afz-sub { color: var(--mute); margin: -0.4rem 0 1rem; max-width: 64ch; }
/* menu board */
.afz .afz-board { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr)); gap: 0.9rem; }
.afz .afz-menu { background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 1.1rem 1.2rem; }
.afz .afz-menu h3 { margin: 0 0 0.25rem; border: 0; padding: 0; font-size: 1.1rem; font-weight: 750; color: #fff; }
.afz .afz-menu .afz-uses { color: var(--acc); font-size: 0.88rem; margin-bottom: 0.7rem; }
.afz .afz-menu .afz-items li { display: flex; align-items: baseline; gap: 0.5rem; padding: 0.3rem 0; font-size: 0.95rem; }
.afz .afz-menu .afz-items li::after { content: ''; order: 2; flex: 1; border-bottom: 1px dotted var(--line); transform: translateY(-0.25em); }
.afz .afz-menu .afz-items li span { order: 3; color: var(--mute); font-size: 0.85rem; }
.afz .afz-chips { display: flex; flex-wrap: wrap; gap: 0.4rem; }
.afz .afz-chips li { background: var(--panel2); border: 1px solid var(--line); border-radius: 999px; padding: 0.15rem 0.7rem; font-size: 0.88rem; }
.afz .afz-notes { display: grid; gap: 0.5rem; margin-top: 1rem; }
.afz .afz-notes li { position: relative; padding-left: 1.3rem; color: var(--mute); }
.afz .afz-notes li::before { content: ''; position: absolute; left: 0.2rem; top: 0.62em; width: 0.45rem; height: 0.45rem; border-radius: 50%; background: var(--acc); }
/* supply steps */
.afz .afz-steps { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 200px), 1fr)); gap: 0.7rem; counter-reset: afz; }
.afz .afz-steps li { counter-increment: afz; background: var(--panel); border: 1px solid var(--line); border-top: 3px solid var(--acc); border-radius: 14px; padding: 1rem 1.05rem; }
.afz .afz-steps li::before { content: 'Pas ' counter(afz); display: block; margin-bottom: 0.35rem; font-size: 0.75rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: var(--acc); }
.afz .afz-steps b { display: block; }
.afz .afz-steps span { color: var(--mute); font-size: 0.93rem; }
/* locations */
.afz .afz-locs { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 220px), 1fr)); gap: 0.7rem; }
.afz .afz-loc { background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 0.9rem 1rem; }
.afz .afz-loc b { display: block; }
.afz .afz-loc span { display: block; margin-top: 0.35rem; color: var(--mute); font-size: 0.9rem; }
.afz .afz-loc code { color: var(--acc); }
.afz .afz-foot { margin-top: 2.5rem; padding: 1rem 1.2rem; border: 1px dashed var(--line); border-radius: 14px; color: var(--mute); }
@media (prefers-reduced-motion: reduce) {
  .afz .afz-tube { animation: none; }
}
</style>

<div class="afz">
<section class="afz-hero">
<div>
<p class="afz-kicker">Afaceri · Locatii</p>
<h1>Frizerie</h1>
<p class="afz-lede">Aici te tunzi, iti aranjezi barba si iti schimbi machiajul. Frizeria e o firma: conducerea pune preturile, iar angajatii aduc uneltele si produsele.</p>
</div>
<div class="afz-pole" role="img" aria-label="Stalp de frizerie">
<div class="afz-cap top"></div>
<div class="afz-tube"></div>
<div class="afz-cap"></div>
</div>
</section>
<ul class="afz-facts">
<li><b>3</b><span>frizerii pe harta</span></li>
<li><b>14</b><span>servicii, fiecare cu pretul lui</span></li>
<li><b>3</b><span>consumabile de tinut in stoc</span></li>
</ul>
<h2>Ce gasesti la frizer</h2>
<p class="afz-sub">Platesti pentru fiecare serviciu pe care il schimbi. Preturile le pune conducerea frizeriei, pana la un plafon.</p>
<div class="afz-board">
<div class="afz-menu">
<h3>Tuns</h3>
<p class="afz-uses">Consuma o <img class="eg-item" src="/items/hair_clipper.webp" alt="">masina de tuns si o <img class="eg-item" src="/items/scissors.webp" alt="">foarfeca</p>
<ul class="afz-items">
<li>Par<span>orice schimbare de tunsoare</span></li>
</ul>
</div>
<div class="afz-menu">
<h3>Fata si corp</h3>
<p class="afz-uses">Consuma <img class="eg-item" src="/items/face_products.webp" alt="">produse faciale, cate unul pe serviciu</p>
<ul class="afz-chips">
<li>Barba</li><li>Sprancene</li><li>Culoare ochi</li><li>Machiaj</li><li>Ruj</li><li>Fard de obraz</li><li>Ten</li><li>Imperfectiuni</li><li>Imbatranire</li><li>Arsuri solare</li><li>Alunite si pistrui</li><li>Par pe piept</li><li>Imperfectiuni corp</li>
</ul>
</div>
</div>
<ul class="afz-notes">
<li>Frizeria se deschide doar daca are stoc pentru cel putin un serviciu. Altfel primesti mesajul ca nu are stoc.</li>
<li>Meniul iti arata cate servicii mai acopera stocul, ca sa nu alegi mai multe decat poate face frizeria.</li>
</ul>
<h2>Cum aprovizionezi frizeria</h2>
<p class="afz-sub">Pentru angajatii unei frizerii. Stocul il vezi oricand in Tableta firma, la Stoc.</p>
<ol class="afz-steps">
<li><b>Furnizor Frizer</b><span>Sta langa ceilalti furnizori, la codul postal <code>313</code>. Vinde doar angajatilor unei frizerii.</span></li>
<li><b>Cumperi consumabile</b><span><img class="eg-item" src="/items/hair_clipper.webp" alt="">Masini de tuns, <img class="eg-item" src="/items/scissors.webp" alt="">foarfeci si <img class="eg-item" src="/items/face_products.webp" alt="">produse faciale. Platesti din banii tai si primesti o <img class="eg-item" src="/items/clothes_box.webp" alt="">cutie.</span></li>
<li><b>Deschizi cutia la frizerie</b><span>Langa frizeria ta, continutul intra direct in stocul firmei. Ce trece peste limita de stoc ramane in cutie.</span></li>
</ol>
<ul class="afz-notes">
<li>Preturile serviciilor le schimba conducerea din Tableta firma, la Preturi.</li>
<li>Firma primeste o parte din fiecare serviciu vandut. Partea creste cu fiecare angajat pontat aflat la cel mult 100 m de frizerie, pana la o limita.</li>
</ul>
<h2>Locatii</h2>
<p class="afz-sub">Scrie in chat <code>/cod</code> si numarul de mai jos, ca sa pui punct pe harta.</p>
<ul class="afz-locs">
<li class="afz-loc"><b>Frizerie Primarie</b><span>Cod postal <code>651</code></span></li>
<li class="afz-loc"><b>Frizerie Vinewood</b><span>Cod postal <code>617</code></span></li>
<li class="afz-loc"><b>Frizerie Groove</b><span>Cod postal <code>838</code></span></li>
</ul>
<p class="afz-foot">Cum cumperi o firma, cum angajezi oameni si cum se platesc salariile afli la <a href="/afaceri/elite-business-center">Elite Business Center</a>.</p>
</div>
