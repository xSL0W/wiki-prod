---
outline: false
---

<style>
.acl {
  --ink: #0c0c0e;
  --panel: #18181b;
  --panel2: #202024;
  --line: #34343b;
  --text: #f4f4f5;
  --mute: #a1a1aa;
  --red: #dc2626;
  --acc: #e879f9;
  --acc2: #22d3ee;
  --acc-soft: rgba(232, 121, 249, 0.13);
  max-width: 960px;
  margin: 0 auto;
  color: var(--text);
}
.acl *, .acl *::before, .acl *::after { box-sizing: border-box; }
.acl p, .acl li { margin: 0; line-height: 1.6; color: var(--text); }
.acl ul, .acl ol { list-style: none; padding: 0; margin: 0; }
.acl li + li { margin-top: 0; }
.acl b { color: #fff; font-weight: 650; }
.acl code { white-space: normal; overflow-wrap: anywhere; }
.acl a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.acl a:hover { color: #fecaca; }
.acl a:focus-visible { outline: 3px solid var(--acc); outline-offset: 3px; border-radius: 6px; }
/* hero */
.acl .acl-hero {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr)); gap: 1.5rem; align-items: center;
  background: radial-gradient(80% 110% at 100% 0%, rgba(232, 121, 249, 0.2), transparent 60%),
              radial-gradient(70% 90% at 60% 100%, rgba(34, 211, 238, 0.12), transparent 60%),
              radial-gradient(110% 120% at 0% 100%, rgba(185, 28, 28, 0.24), var(--ink) 65%);
  border: 1px solid var(--line); border-radius: 22px; padding: clamp(1.25rem, 4vw, 2.5rem); overflow: hidden;
}
.acl .acl-kicker { font-size: 0.78rem; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: var(--acc); margin-bottom: 0.6rem; }
.acl .acl-hero h1 {
  margin: 0 0 0.8rem; border: 0; padding: 0;
  font-size: clamp(2.3rem, 8vw, 3.6rem); line-height: 1; font-weight: 800; letter-spacing: -0.03em; color: #fff;
  text-shadow: 0 0 18px rgba(232, 121, 249, 0.55);
}
.acl .acl-lede { color: var(--mute); font-size: 1.05rem; max-width: 46ch; }
/* equalizer */
.acl .acl-eq { display: flex; align-items: flex-end; justify-content: center; gap: clamp(4px, 1.2vw, 8px); height: clamp(120px, 26vw, 180px); padding: 0.5rem; }
.acl .acl-eq span {
  flex: 1; max-width: 18px; height: 100%; border-radius: 4px 4px 2px 2px; transform-origin: bottom;
  background: linear-gradient(0deg, var(--acc2), var(--acc) 60%, #fff);
  box-shadow: 0 0 12px rgba(232, 121, 249, 0.45);
  animation: acl-eq 1.2s ease-in-out infinite alternate;
}
.acl .acl-eq span:nth-child(1) { animation-delay: -0.2s; }
.acl .acl-eq span:nth-child(2) { animation-delay: -0.9s; animation-duration: 0.9s; }
.acl .acl-eq span:nth-child(3) { animation-delay: -0.5s; }
.acl .acl-eq span:nth-child(4) { animation-delay: -1.1s; animation-duration: 0.8s; }
.acl .acl-eq span:nth-child(5) { animation-delay: -0.3s; animation-duration: 1.4s; }
.acl .acl-eq span:nth-child(6) { animation-delay: -0.7s; }
.acl .acl-eq span:nth-child(7) { animation-delay: -0.1s; animation-duration: 1s; }
.acl .acl-eq span:nth-child(8) { animation-delay: -0.6s; animation-duration: 0.7s; }
.acl .acl-eq span:nth-child(9) { animation-delay: -1s; }
.acl .acl-eq span:nth-child(10) { animation-delay: -0.4s; animation-duration: 1.1s; }
@keyframes acl-eq { from { transform: scaleY(0.18); } to { transform: scaleY(1); } }
/* facts */
.acl .acl-facts { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 130px), 1fr)); gap: 0.7rem; margin-top: 1rem; }
.acl .acl-facts li { background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 0.9rem 1rem; }
.acl .acl-facts b { display: block; font-size: 1.5rem; line-height: 1.1; color: var(--acc); font-variant-numeric: tabular-nums; }
.acl .acl-facts span { color: var(--mute); font-size: 0.92rem; }
/* sections */
.acl h2 {
  display: flex; align-items: flex-start; gap: 0.65rem;
  margin: 3rem 0 1rem; border: 0; padding: 0;
  font-size: 1.45rem; font-weight: 750; letter-spacing: -0.015em; color: #fff;
}
.acl h2::before { margin-top: calc(0.5lh - 1rem / 2);
  content: ''; flex: none; width: 1rem; height: 1rem;
  background: linear-gradient(var(--acc), var(--acc)) 0 100% / 24% 55% no-repeat,
              linear-gradient(var(--acc2), var(--acc2)) 50% 100% / 24% 100% no-repeat,
              linear-gradient(var(--acc), var(--acc)) 100% 100% / 24% 75% no-repeat;
}
.acl .acl-sub { color: var(--mute); margin: -0.4rem 0 1rem; max-width: 64ch; }
/* night plan: zones of the club */
.acl .acl-zones { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr)); gap: 0.9rem; }
.acl .acl-zone {
  background: linear-gradient(160deg, var(--acc-soft), var(--panel) 45%); border: 1px solid var(--line);
  border-radius: 18px; padding: 1.1rem 1.2rem;
}
.acl .acl-zone.cyan { background: linear-gradient(160deg, rgba(34, 211, 238, 0.12), var(--panel) 45%); }
.acl .acl-zone h3 { margin: 0 0 0.25rem; border: 0; padding: 0; font-size: 1.15rem; font-weight: 750; color: #fff; }
.acl .acl-zone .acl-tag { margin-bottom: 0.6rem; font-size: 0.75rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: var(--acc); }
.acl .acl-zone.cyan .acl-tag { color: var(--acc2); }
.acl .acl-zone > p:last-child { color: var(--mute); }
.acl .acl-chips { display: flex; flex-wrap: wrap; gap: 0.35rem; margin: 0.2rem 0 0.7rem; }
.acl .acl-chips li { background: var(--panel2); border: 1px solid var(--line); border-radius: 999px; padding: 0.1rem 0.65rem; font-size: 0.86rem; }
/* staff */
.acl .acl-staff { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 220px), 1fr)); gap: 0.7rem; }
.acl .acl-staff li { background: var(--panel); border: 1px solid var(--line); border-top: 3px solid var(--acc); border-radius: 14px; padding: 0.9rem 1rem; color: var(--mute); font-size: 0.94rem; }
.acl .acl-staff li:nth-child(2n) { border-top-color: var(--acc2); }
.acl .acl-more { margin-top: 0.7rem; }
.acl .acl-staff b { display: block; color: #fff; font-size: 1rem; }
/* location */
.acl .acl-loc {
  display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 0.8rem;
  background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 1rem 1.2rem;
}
.acl .acl-loc b { display: block; font-size: 1.15rem; }
.acl .acl-loc span { color: var(--mute); }
.acl .acl-loc code { color: var(--acc); }
.acl .acl-foot { margin-top: 2.5rem; padding: 1rem 1.2rem; border: 1px dashed var(--line); border-radius: 14px; color: var(--mute); }
@media (prefers-reduced-motion: reduce) {
  .acl .acl-eq span { animation: none; transform: scaleY(0.6); }
}
</style>

<div class="acl">
<section class="acl-hero">
<div>
<p class="acl-kicker">Afaceri · Locatii</p>
<h1>Club</h1>
<p class="acl-lede">Viata de noapte a orasului. Clubul e o firma cu bar, bilete la intrare si cabina de DJ.</p>
</div>
<div class="acl-eq" aria-hidden="true"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></div>
</section>
<ul class="acl-facts">
<li><b>1</b><span>club in oras</span></li>
<li><b>7</b><span>puncte de bar</span></li>
<li><b>2</b><span>tipuri de bilet</span></li>
<li><b>2</b><span>deck-uri in cabina de DJ</span></li>
</ul>
<h2>O noapte in club</h2>
<div class="acl-zones">
<div class="acl-zone">
<p class="acl-tag">La intrare</p>
<h3>Bilete</h3>
<ul class="acl-chips"><li>Standard</li><li>VIP</li></ul>
<p>Le cumperi de la casa de bilete din club. Pe bilet scrie numele clubului, data si prenumele tau, ca sa-l poata verifica cei de la intrare.</p>
</div>
<div class="acl-zone cyan">
<p class="acl-tag">La bar</p>
<h3>Bauturi si tigari</h3>
<ul class="acl-chips"><li>Apa</li><li>Cola</li><li>Cafea</li><li>Bere</li><li>Whiskey</li><li>Vodka</li><li>Tigari</li><li>Baton Twerks</li><li>Baton Snikkel</li></ul>
<p>Barul vinde doar ce au adus angajatii in depozitul clubului.</p>
</div>
<div class="acl-zone">
<p class="acl-tag">Pe ring</p>
<h3>Cabina de DJ</h3>
<ul class="acl-chips"><li>Lumini</li><li>Lasere</li><li>Fum</li><li>Flacari</li></ul>
<p>Doua deck-uri, cautare de melodii pe YouTube, coada de melodii si volum. Din cabina pornesti efectele, le misti si le schimbi culoarea.</p>
</div>
<div class="acl-zone cyan">
<p class="acl-tag">Peste tot</p>
<h3>Zona sigura</h3>
<p>Clubul e zona sigura: cand intri, ti se ia arma din mana. Membrii clubului isi pot folosi armele. Ecranul mare din club il controleaza tot ei.</p>
</div>
</div>
<h2>Echipa clubului</h2>
<p class="acl-sub">Totul se conduce din Tableta firma. Ce vezi in ea depinde de functia ta.</p>
<ul class="acl-staff">
<li><b>Patron si sefi</b>Pun preturile la bar si la bilete, angajeaza oameni si vad vanzarile.</li>
<li><b>DJ si restul echipei</b>Orice angajat al clubului poate folosi cabina de DJ. Daca nimeni din club nu e pontat, cabina e libera pentru oricine.</li>
<li><b>Aprovizionare</b>Furnizor Bar sta langa ceilalti furnizori, la codul postal <code>313</code>. Cumperi marfa cu banii tai, desfaci cutia si pui produsele in depozitul clubului.</li>
</ul>
<ul class="acl-staff acl-more">
<li><b>Bani pentru firma</b>Firma primeste o parte din fiecare bilet si din fiecare comanda de la bar. Partea creste cu fiecare angajat pontat aflat la cel mult 100 m de club, pana la o limita.</li>
<li><b>Seif</b>Seiful clubului il deschid doar patronul si sefii.</li>
</ul>
<h2>Locatie</h2>
<div class="acl-loc">
<div><b>Club Haute</b><span>Scrie in chat <code>/cod 623</code> ca sa pui punct pe harta.</span></div>
</div>
<p class="acl-foot">Cum cumperi o firma, cum angajezi oameni si cum se platesc salariile afli la <a href="/afaceri/elite-business-center">Elite Business Center</a>.</p>
</div>
