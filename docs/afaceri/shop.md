---
outline: false
---

<style>
.ash {
  --ink: #0c0c0e;
  --panel: #18181b;
  --panel2: #202024;
  --line: #34343b;
  --text: #f4f4f5;
  --mute: #a1a1aa;
  --red: #dc2626;
  --acc: #4ade80;
  --acc-soft: rgba(74, 222, 128, 0.12);
  --paper: #f4f1ea;
  --paper-ink: #27272a;
  width: 960px;
  max-width: 100%;
  margin: 0 auto;
  color: var(--text);
}
.ash *, .ash *::before, .ash *::after { box-sizing: border-box; }
.ash p, .ash li { margin: 0; line-height: 1.6; color: var(--text); }
.ash ul, .ash ol { list-style: none; padding: 0; margin: 0; }
.ash li + li { margin-top: 0; }
.ash b { color: #fff; font-weight: 650; }
.ash code { white-space: normal; overflow-wrap: anywhere; }
.ash a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.ash a:hover { color: #fecaca; }
.ash a:focus-visible { outline: 3px solid var(--acc); outline-offset: 3px; border-radius: 6px; }
/* hero */
.ash .ash-hero {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr)); gap: 1.5rem; align-items: center;
  background: radial-gradient(90% 120% at 100% 0%, rgba(74, 222, 128, 0.13), transparent 60%),
              radial-gradient(110% 120% at 0% 100%, rgba(185, 28, 28, 0.26), var(--ink) 65%);
  border: 1px solid var(--line); border-radius: 22px; padding: clamp(1.25rem, 4vw, 2.5rem); overflow: hidden;
}
.ash .ash-kicker { font-size: 0.78rem; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: var(--acc); margin-bottom: 0.6rem; }
.ash .ash-hero h1 {
  margin: 0 0 0.8rem; border: 0; padding: 0;
  font-size: clamp(2.1rem, 7vw, 3.3rem); line-height: 1.02; font-weight: 800; letter-spacing: -0.03em; color: #fff;
}
.ash .ash-lede { color: var(--mute); font-size: 1.05rem; max-width: 46ch; }
/* neon sign */
.ash .ash-sign {
  justify-self: center; display: grid; place-items: center; gap: 0.2rem;
  border: 2px solid rgba(74, 222, 128, 0.5); border-radius: 18px; padding: 1.1rem 1.6rem; background: rgba(0, 0, 0, 0.35);
}
.ash .ash-sign .n {
  font: 900 clamp(3rem, 12vw, 4.6rem)/1 ui-monospace, Menlo, Consolas, monospace; letter-spacing: -0.04em; color: #dcfce7;
  text-shadow: 0 0 6px var(--acc), 0 0 18px var(--acc), 0 0 36px rgba(74, 222, 128, 0.6);
  animation: ash-flicker 6s linear infinite;
}
.ash .ash-sign .o { font-size: 0.8rem; font-weight: 800; letter-spacing: 0.4em; text-transform: uppercase; color: var(--red); text-shadow: 0 0 10px rgba(220, 38, 38, 0.8); padding-left: 0.4em; }
@keyframes ash-flicker { 0%, 18%, 22%, 60%, 64%, 100% { opacity: 1; } 20%, 62% { opacity: 0.35; } }
/* facts */
.ash .ash-facts { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 190px), 1fr)); gap: 0.7rem; margin-top: 1rem; }
.ash .ash-facts li { background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 0.9rem 1rem; }
.ash .ash-facts b { display: block; font-size: 1.5rem; line-height: 1.1; color: var(--acc); font-variant-numeric: tabular-nums; }
.ash .ash-facts span { color: var(--mute); font-size: 0.92rem; }
/* sections */
.ash h2 {
  display: flex; align-items: baseline; gap: 0.65rem;
  margin: 3rem 0 1rem; border: 0; padding: 0;
  font-size: 1.45rem; font-weight: 750; letter-spacing: -0.015em; color: #fff;
}
.ash h2::before { content: '24'; flex: none; font: 800 0.7rem/1 ui-monospace, Menlo, Consolas, monospace; color: var(--ink); background: var(--acc); border-radius: 4px; padding: 0.25rem 0.3rem; }
.ash .ash-sub { color: var(--mute); margin: -0.4rem 0 1rem; max-width: 64ch; }
/* receipt */
.ash .ash-wrap { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 300px), 1fr)); gap: 1.2rem; align-items: start; }
.ash .ash-receipt {
  background: var(--paper); color: var(--paper-ink); border-radius: 6px 6px 0 0; padding: 1.2rem 1.2rem 1.6rem;
  font-family: ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; font-size: 0.88rem;
  -webkit-mask: radial-gradient(circle 7px at 50% 100%, transparent 98%, #000) 0 0 / 18px 100% repeat-x;
          mask: radial-gradient(circle 7px at 50% 100%, transparent 98%, #000) 0 0 / 18px 100% repeat-x;
}
.ash .ash-receipt p, .ash .ash-receipt li { color: var(--paper-ink); }
.ash .ash-receipt .head { text-align: center; font-weight: 800; letter-spacing: 0.2em; }
.ash .ash-receipt .rule { border-top: 1px dashed #a1a1aa; margin: 0.7rem 0; }
.ash .ash-receipt .cat { font-weight: 800; text-transform: uppercase; letter-spacing: 0.08em; margin-top: 0.6rem; }
.ash .ash-receipt .cat:first-of-type { margin-top: 0; }
.ash .ash-receipt ul li { padding-left: 1rem; position: relative; line-height: 1.5; }
.ash .ash-receipt ul li::before { content: '1x'; position: absolute; left: -0.2rem; color: #71717a; font-size: 0.75rem; top: 0.1em; }
.ash .ash-receipt .end { text-align: center; color: #52525b; }
.ash .ash-side { display: grid; gap: 0.7rem; }
.ash .ash-side li { background: var(--panel); border: 1px solid var(--line); border-left: 3px solid var(--acc); border-radius: 14px; padding: 0.85rem 1rem; color: var(--mute); }
.ash .ash-side b { display: block; color: #fff; }
/* restock lane */
.ash .ash-lane { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 200px), 1fr)); gap: 0.6rem; counter-reset: ash; }
.ash .ash-lane li {
  counter-increment: ash; position: relative; background: var(--panel); border: 1px solid var(--line); border-radius: 14px;
  padding: 2.4rem 1rem 1rem;
}
.ash .ash-lane li::before {
  content: counter(ash); position: absolute; top: 0.8rem; left: 1rem; font: 800 0.8rem/1 ui-monospace, Menlo, Consolas, monospace;
  color: var(--acc); border: 1px solid var(--acc); border-radius: 4px; padding: 0.2rem 0.4rem;
}
.ash .ash-lane b { display: block; }
.ash .ash-lane span { color: var(--mute); font-size: 0.93rem; }
.ash .ash-notes { display: grid; gap: 0.5rem; margin-top: 1rem; }
.ash .ash-notes li { position: relative; padding-left: 1.3rem; color: var(--mute); }
.ash .ash-notes li::before { content: ''; position: absolute; left: 0.2rem; top: 0.62em; width: 0.5rem; height: 0.5rem; border-radius: 2px; background: var(--acc); }
/* locations */
.ash .ash-locs { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 180px), 1fr)); gap: 0.7rem; }
.ash .ash-loc { display: flex; flex-direction: column; background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 0.9rem 1rem; }
.ash .ash-loc b { display: block; flex: 1; }
.ash .ash-loc span { display: block; margin-top: 0.35rem; color: var(--mute); font-size: 0.9rem; }
.ash .ash-loc code { color: var(--acc); }
.ash .ash-foot { margin-top: 2.5rem; padding: 1rem 1.2rem; border: 1px dashed var(--line); border-radius: 14px; color: var(--mute); }
@media (prefers-reduced-motion: reduce) {
  .ash .ash-sign .n { animation: none; }
}
</style>

<div class="ash">
<section class="ash-hero">
<div>
<p class="ash-kicker">Afaceri · Locatii</p>
<h1>Magazin 24/7</h1>
<p class="ash-lede">Magazinul de cartier: mancare, bauturi, tigari si kituri pentru masina. Fiecare magazin e o firma, iar rafturile le umplu angajatii.</p>
</div>
<div class="ash-sign" aria-hidden="true"><span class="n">24/7</span><span class="o">Deschis</span></div>
</section>
<ul class="ash-facts">
<li><b>5</b><span>magazine 24/7 pe harta</span></li>
<li><b>5</b><span>raioane pe raft</span></li>
<li><b>1</b><span>depozit al firmei, din care se vinde</span></li>
</ul>
<h2>Ce gasesti pe raft</h2>
<div class="ash-wrap">
<div class="ash-receipt">
<p class="head">MAGAZIN 24/7</p>
<div class="rule"></div>
<p class="cat">Kit-uri masina</p>
<ul><li><img class="eg-item" src="/items/tirekit_civil.webp" alt="">Kit de reparatii roata</li><li><img class="eg-item" src="/items/repairkit_civil.webp" alt="">Kit de reparatii motor</li><li><img class="eg-item" src="/items/tow_strap.webp" alt="">Chinga de tractare</li><li><img class="eg-item" src="/items/cleaningkit.webp" alt="">Kit de curatat</li><li><img class="eg-item" src="/items/clonekeystool.webp" alt="">Trusa de clonat chei</li></ul>
<p class="cat">Mancare</p>
<ul><li><img class="eg-item" src="/items/sandwich.webp" alt="">Sandwich</li><li><img class="eg-item" src="/items/tosti.webp" alt="">Sandwich cu cascaval</li><li><img class="eg-item" src="/items/twerks_candy.webp" alt="">Baton Twerks</li><li><img class="eg-item" src="/items/snikkel_candy.webp" alt="">Baton Snikkel</li></ul>
<p class="cat">Bauturi</p>
<ul><li><img class="eg-item" src="/items/water_bottle.webp" alt="">Apa, <img class="eg-item" src="/items/kurkakola.webp" alt="">cola, <img class="eg-item" src="/items/coffee.webp" alt="">cafea</li><li><img class="eg-item" src="/items/beer.webp" alt="">Bere, <img class="eg-item" src="/items/whiskey.webp" alt="">whiskey, <img class="eg-item" src="/items/vodka.webp" alt="">vodka</li></ul>
<p class="cat">Tigari si altele</p>
<ul><li><img class="eg-item" src="/items/tigari.webp" alt="">Tigari</li><li><img class="eg-item" src="/items/bucata_de_hartie_goala.webp" alt="">Bucata de hartie</li><li><img class="eg-item" src="/items/mapa_documente.webp" alt="">Mapa documente</li><li><img class="eg-item" src="/items/megaphone.webp" alt="">Megafon</li></ul>
<div class="rule"></div>
<p class="end">Va multumim!</p>
</div>
<ul class="ash-side">
<li><b>Se vinde doar ce e in stoc</b>Tot ce cumperi iese din depozitul firmei. Daca un produs s-a terminat, asteapta pana il aduc angajatii.</li>
<li><b>Pretul il pune conducerea</b>Daca nu l-a schimbat, platesti pretul de baza. Daca l-a schimbat, nu poate trece de un plafon.</li>
<li><b>Bani pentru firma</b>Firma primeste o parte din fiecare vanzare. Partea creste cu fiecare angajat pontat aflat la cel mult 100 m de magazin, pana la o limita.</li>
</ul>
</div>
<h2>Cum umpli rafturile</h2>
<p class="ash-sub">Pentru angajatii unui magazin 24/7.</p>
<ol class="ash-lane">
<li><b>Furnizor Magazin</b><span>Sta langa ceilalti furnizori, la codul postal <code>313</code>. Vinde doar angajatilor magazinelor.</span></li>
<li><b>Cumperi marfa</b><span>Alegi produsul si cantitatea, platesti din banii tai si primesti o <img class="eg-item" src="/items/clothes_box.webp" alt="">cutie.</span></li>
<li><b>Desfaci cutia</b><span>Marfa iti intra in inventar.</span></li>
<li><b>O pui in depozit</b><span>Depozitul firmei e chiar in magazin. Ce pui acolo apare la vanzare.</span></li>
</ol>
<ul class="ash-notes">
<li>Fiecare produs are o limita de stoc in depozit.</li>
<li>In Tableta firma vezi Stocul si Vanzarile. Conducerea schimba preturile la Preturi.</li>
</ul>
<h2>Locatii</h2>
<p class="ash-sub">Scrie in chat <code>/cod</code> si numarul de mai jos, ca sa pui punct pe harta.</p>
<ul class="ash-locs">
<li class="ash-loc"><b>24/7 Rockford</b><span>Cod postal <code>594</code></span></li>
<li class="ash-loc"><b>24/7 Strawberry</b><span>Cod postal <code>850</code></span></li>
<li class="ash-loc"><b>24/7 Davis</b><span>Cod postal <code>847</code></span></li>
<li class="ash-loc"><b>24/7 Little Seoul</b><span>Cod postal <code>726</code></span></li>
<li class="ash-loc"><b>24/7 Sandy</b><span>Cod postal <code>297</code></span></li>
</ul>
<p class="ash-foot">Cum cumperi o firma, cum angajezi oameni si cum se platesc salariile afli la <a href="/afaceri/elite-business-center">Elite Business Center</a>.</p>
</div>
