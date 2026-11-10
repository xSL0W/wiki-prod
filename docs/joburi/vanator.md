---
outline: false
---

<style>
.vn {
  --night: #0a100c;
  --moss: #121c15;
  --fern: #1b2a1f;
  --line: #2d4033;
  --text: #ece6d6;
  --mute: #a9ae9c;
  --blaze: #ff6a1f;
  --blaze-soft: rgba(255, 106, 31, 0.13);
  --contour: #2f4a37;
  --print: #d9c9a3;
  --danger: #ff4d4d;
  --serif: 'Iowan Old Style', 'Palatino Linotype', Palatino, Georgia, serif;
  max-width: 940px;
  margin: 0 auto;
  color: var(--text);
  font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.vn *, .vn *::before, .vn *::after { box-sizing: border-box; }
.vn p, .vn li { line-height: 1.6; color: var(--text); margin: 0; }
.vn ul, .vn ol { list-style: none; padding: 0; margin: 0; }
.vn h1, .vn h2, .vn h3 { border: 0; padding: 0; }
.vn a:focus-visible { outline: 3px solid var(--blaze); outline-offset: 2px; }
.vn b { color: #fff; font-weight: 650; }
.vn kbd {
  font: inherit; font-size: 0.85em; font-weight: 700; color: var(--night); background: var(--blaze);
  border-radius: 6px; padding: 0.05rem 0.45rem; white-space: nowrap;
}

/* hero: a topographic map with a trail on it */
.vn-hero {
  position: relative;
  background: var(--night);
  border: 1px solid var(--line);
  border-radius: 20px;
  padding: clamp(1.2rem, 4vw, 2.4rem);
  overflow: hidden;
}
.vn .vn-kicker { font-family: var(--serif); font-style: italic; color: var(--blaze); font-size: 1.05rem; }
.vn-hero h1 {
  margin: 0.4rem 0 0.6rem;
  font-family: var(--serif);
  font-size: clamp(2.2rem, 7vw, 3.8rem);
  line-height: 1.02;
  font-weight: 700;
  letter-spacing: -0.02em;
  color: #fff;
}
.vn-hours {
  display: inline-block; font-family: system-ui, sans-serif; font-size: 0.5em; font-weight: 800; vertical-align: 0.4em;
  color: var(--night); background: var(--blaze); border-radius: 999px; padding: 0.15em 0.6em; letter-spacing: 0;
}
.vn-hero > p { max-width: 54ch; color: var(--mute); font-size: 1.05rem; position: relative; }
.vn-topo { display: block; width: 100%; height: auto; margin-top: 1.4rem; }
.vn-topo .c { fill: none; stroke: var(--contour); stroke-width: 1.6; }
.vn-topo .c.hi { stroke: #3f6249; }
.vn-topo .p { fill: var(--print); opacity: 0; animation: vn-step 0.4s ease-out forwards; }
.vn-topo .aim { fill: none; stroke: var(--blaze); stroke-width: 2.5; }
.vn-topo .aim-dot { fill: var(--blaze); }
.vn-topo .n { fill: var(--mute); font-family: var(--serif); font-size: 15px; font-weight: 700; }
.vn-topo .needle { fill: var(--blaze); }
.vn-topo .needle-s { fill: var(--mute); }
@keyframes vn-step { to { opacity: 0.85; } }
@media (prefers-reduced-motion: reduce) {
  .vn-topo .p { animation: none; opacity: 0.85; }
}

/* sections */
.vn h2 {
  margin: 3rem 0 1rem;
  font-family: var(--serif);
  font-size: 1.65rem; font-weight: 700; letter-spacing: -0.01em; color: #fff;
}
.vn h2 small { display: block; font-family: system-ui, sans-serif; font-size: 0.75rem; letter-spacing: 0.18em; text-transform: uppercase; color: var(--blaze); margin-bottom: 0.2rem; }

/* gear as a packing list */
.vn-pack { display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 0.8rem; }
.vn-pack li {
  position: relative; background: var(--moss); border: 1px solid var(--line); border-radius: 14px;
  padding: 1rem 1.1rem 1rem 3rem;
}
.vn-pack li::before {
  content: ''; position: absolute; left: 1rem; top: 1.15rem; width: 18px; height: 18px; border-radius: 4px;
  border: 2px solid var(--blaze);
  background: linear-gradient(135deg, transparent 45%, var(--blaze) 45% 60%, transparent 60%);
}
.vn-pack strong { display: block; color: #fff; }
.vn-pack span { color: var(--mute); font-size: 0.93rem; }

/* the hunt as a trail of prints */
.vn-trail { position: relative; }
.vn-trail li { position: relative; padding: 0 0 1.4rem 3.2rem; }
.vn-trail li:last-child { padding-bottom: 0; }
.vn-trail li::before, .vn-trail li::after {
  content: ''; position: absolute; width: 10px; height: 15px; border-radius: 50% 50% 45% 45%; background: var(--print); opacity: 0.8;
}
.vn-trail li::before { left: 6px; top: 2px; transform: rotate(-12deg); }
.vn-trail li::after { left: 19px; top: 8px; transform: rotate(10deg); }
.vn-trail li:nth-child(even)::before { left: 10px; top: 6px; }
.vn-trail li:nth-child(even)::after { left: 22px; top: 1px; }
.vn-trail li:last-child::before, .vn-trail li:last-child::after { background: var(--blaze); opacity: 1; }

/* callouts */
.vn-warn {
  margin-top: 1.4rem; padding: 1rem 1.2rem; border-radius: 14px;
  background: linear-gradient(150deg, var(--blaze-soft), var(--moss) 60%); border: 1px solid var(--blaze);
}
.vn-warn strong { display: block; color: var(--blaze); margin-bottom: 0.2rem; }

/* field guide */
.vn-guide { display: grid; grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: 0.8rem; }
.vn-guide li { background: var(--moss); border: 1px solid var(--line); border-radius: 14px; padding: 0.9rem 1rem; }
.vn-guide li.hostile { border-color: var(--danger); background: linear-gradient(160deg, rgba(255, 77, 77, 0.1), var(--moss) 60%); }
.vn-guide h3 { margin: 0; font-family: var(--serif); font-size: 1.15rem; color: #fff; display: flex; justify-content: space-between; gap: 0.5rem; align-items: baseline; }
.vn-tag { font-family: system-ui, sans-serif; font-size: 0.68rem; font-weight: 800; letter-spacing: 0.1em; text-transform: uppercase; padding: 0.1rem 0.45rem; border-radius: 999px; }
.vn-tag.atk { background: var(--danger); color: #fff; }
.vn-tag.rare { background: var(--print); color: var(--night); }
.vn-shots { display: flex; gap: 4px; margin: 0.5rem 0 0.35rem; }
.vn-shots i { width: 11px; height: 11px; border-radius: 50%; border: 2px solid var(--line); }
.vn-shots i.f { background: var(--blaze); border-color: var(--blaze); }
.vn-guide p { color: var(--mute); font-size: 0.9rem; }
.vn .vn-legend { margin-top: 0.8rem; color: var(--mute); font-size: 0.93rem; }

/* two columns: tracks and selling */
.vn-two { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1rem; }
.vn-card { background: var(--moss); border: 1px solid var(--line); border-radius: 16px; padding: 1.2rem 1.3rem; }
.vn-card h3 { margin: 0 0 0.5rem; font-family: var(--serif); font-size: 1.2rem; color: #fff; }
.vn-card p { color: var(--mute); }
.vn-card p + p { margin-top: 0.5rem; }

/* tips */
.vn-tips li { padding: 0.85rem 0; border-top: 1px dashed var(--line); }
.vn-tips li:last-child { border-bottom: 1px dashed var(--line); }
/* block list: keeps the 8px row spacing the theme no longer adds to classed lists */
.vn .vn-trail > li + li, .vn .vn-tips > li + li { margin-top: 8px; }
</style>

<div class="vn">

<section class="vn-hero">
<p class="vn-kicker">Cel mai greu de deblocat job legal</p>
<h1>Vanator - <span class="vn-hours">750h</span></h1>
<p>Pleci cu pusca de vanatoare in zona din salbaticie, urmaresti animalele, le transezi pe loc si vinzi carnea si trofeele. Fiecare foc conteaza.</p>
<svg class="vn-topo" viewBox="0 0 640 200" role="img" aria-label="Harta topografica cu un sir de urme de animal care duc spre o tinta">
<path class="c" d="M-10 170 C 80 140, 150 190, 240 160 S 420 120, 520 150 S 640 130, 660 140"/>
<path class="c" d="M-10 130 C 70 100, 160 150, 250 120 S 410 80, 510 110 S 630 90, 660 100"/>
<path class="c hi" d="M-10 90 C 60 60, 170 110, 260 80 S 400 40, 500 70 S 620 50, 660 60"/>
<path class="c" d="M-10 50 C 50 25, 180 70, 270 40 S 390 5, 490 30 S 610 15, 660 20"/>
<path class="c" d="M330 112 c 25 -18, 70 -14, 80 6 s -30 32, -62 24 s -40 -16, -18 -30z"/>
<path class="c hi" d="M348 114 c 14 -8, 38 -6, 42 4 s -16 16, -32 12 s -20 -8, -10 -16z"/>
<g>
<ellipse class="p" cx="60" cy="168" rx="4" ry="6" transform="rotate(60 60 168)" style="animation-delay:.2s"/>
<ellipse class="p" cx="88" cy="150" rx="4" ry="6" transform="rotate(60 88 150)" style="animation-delay:.45s"/>
<ellipse class="p" cx="118" cy="162" rx="4" ry="6" transform="rotate(70 118 162)" style="animation-delay:.7s"/>
<ellipse class="p" cx="148" cy="142" rx="4" ry="6" transform="rotate(60 148 142)" style="animation-delay:.95s"/>
<ellipse class="p" cx="180" cy="150" rx="4" ry="6" transform="rotate(75 180 150)" style="animation-delay:1.2s"/>
<ellipse class="p" cx="210" cy="128" rx="4" ry="6" transform="rotate(55 210 128)" style="animation-delay:1.45s"/>
<ellipse class="p" cx="244" cy="134" rx="4" ry="6" transform="rotate(70 244 134)" style="animation-delay:1.7s"/>
<ellipse class="p" cx="274" cy="112" rx="4" ry="6" transform="rotate(55 274 112)" style="animation-delay:1.95s"/>
<ellipse class="p" cx="306" cy="118" rx="4" ry="6" transform="rotate(75 306 118)" style="animation-delay:2.2s"/>
</g>
<circle class="aim" cx="372" cy="112" r="22"/>
<path class="aim" d="M372 82 v14 M372 128 v14 M342 112 h14 M388 112 h14"/>
<circle class="aim-dot" cx="372" cy="112" r="3"/>
<g transform="translate(585 150)">
<path class="needle" d="M0 -26 L7 0 L-7 0 Z"/>
<path class="needle-s" d="M0 26 L7 0 L-7 0 Z"/>
<text class="n" x="0" y="-32" text-anchor="middle">N</text>
</g>
</svg>
</section>

<h2><small>Angajare</small>Cum incep?</h2>
<p>Angajeaza-te ca <b>Vanator</b> la Primarie (<code>Telefon → Harti → Locatii importante → Primarie</code>) sau direct la seful vanatorilor, cu <b>Angajeaza-te ca Vanator</b>. Ai nevoie de <b>750 de ore</b> jucate. Seful sta langa zona de vanatoare, iar dupa angajare zona apare pe harta.</p>

<h2><small>Echipament</small>Ce iei cu tine</h2>
<ul class="vn-pack">
<li><strong><img class="eg-item" src="/items/WEAPON_MUSKET.webp" alt="">Pusca de vanatoare</strong><span>De la magazinul de arme, sau o fabrici la masa de lucru de acolo. Se uzeaza cu fiecare foc.</span></li>
<li><strong><img class="eg-item" src="/items/ammo-musket.webp" alt="">Munitie pentru pusca</strong><span>Tot de la magazinul de arme, cumparata sau fabricata.</span></li>
<li><strong>Un <img class="eg-item" src="/items/WEAPON_KNIFE.webp" alt="">cutit</strong><span>Doar in inventar, nu trebuie tinut in mana. Fara el nu poti transa.</span></li>
<li><strong>Un vehicul</strong><span>Oricare. Te ajuta sa duci marfa pana la punctul de vanzare.</span></li>
</ul>

<h2><small>Pe teren</small>O partida de vanatoare</h2>
<ol class="vn-trail">
<li><p><b>Intra in zona de vanatoare.</b> Intri automat in tura, iar cand iesi din zona tura se opreste.</p></li>
<li><p><b>Cauta animalele.</b> In jurul tau apar cateva animale, iar pe masura ce le vanezi apar altele.</p></li>
<li><p><b>Impusca animalul cu <img class="eg-item" src="/items/WEAPON_MUSKET.webp" alt="">pusca de vanatoare.</b> Unele cad din doua focuri, altele au nevoie de trei sau patru.</p></li>
<li><p><b>Tine apasat <kbd>E</kbd></b> langa cadavru ca sa il transezi. Dureaza cateva secunde.</p></li>
<li><p><b>Primesti carne</b> si, din cand in cand, un trofeu: blana, piele, coarne, colti, pene sau gheare.</p></li>
<li><p><b>Vinde tot</b> la punctul de vanzare cand ai strans destul.</p></li>
</ol>
<div class="vn-warn"><strong>Doar pusca de vanatoare iti aduce ceva</strong><p>Daca animalul a murit din orice alt motiv (alta arma, masina, cutit), blana e distrusa si nu primesti nimic. Cadavrul ramane pe jos doua minute, apoi dispare.</p></div>

<h2><small>Atlas</small>Animalele</h2>
<ul class="vn-guide">
<li><h3>Iepure</h3><div class="vn-shots" aria-label="aproximativ 2 focuri"><i class="f"></i><i class="f"></i><i></i><i></i></div><p>Vanat de baza, des intalnit.</p></li>
<li><h3>Cerb</h3><div class="vn-shots" aria-label="aproximativ 3 focuri"><i class="f"></i><i class="f"></i><i class="f"></i><i></i></div><p>Vanat de baza, des intalnit.</p></li>
<li><h3>Porc salbatic</h3><div class="vn-shots" aria-label="aproximativ 3 focuri"><i class="f"></i><i class="f"></i><i class="f"></i><i></i></div><p>Vanat de baza.</p></li>
<li><h3>Mistret</h3><div class="vn-shots" aria-label="aproximativ 3 focuri"><i class="f"></i><i class="f"></i><i class="f"></i><i></i></div><p>Vanat de baza.</p></li>
<li><h3>Pescarus</h3><div class="vn-shots" aria-label="aproximativ 2 focuri"><i class="f"></i><i class="f"></i><i></i><i></i></div><p>Tinta mica si rapida.</p></li>
<li><h3>Cormoran</h3><div class="vn-shots" aria-label="aproximativ 2 focuri"><i class="f"></i><i class="f"></i><i></i><i></i></div><p>Tinta mica si rapida.</p></li>
<li><h3>Uliu <span class="vn-tag rare">rar</span></h3><div class="vn-shots" aria-label="aproximativ 2 focuri"><i class="f"></i><i class="f"></i><i></i><i></i></div><p>Cel mai rar animal din zona.</p></li>
<li class="hostile"><h3>Coiot <span class="vn-tag atk">ataca</span></h3><div class="vn-shots" aria-label="aproximativ 3 focuri"><i class="f"></i><i class="f"></i><i class="f"></i><i></i></div><p>Nu fuge de tine, vine dupa tine.</p></li>
<li class="hostile"><h3>Puma <span class="vn-tag atk">ataca</span></h3><div class="vn-shots" aria-label="aproximativ 4 focuri"><i class="f"></i><i class="f"></i><i class="f"></i><i class="f"></i></div><p>Rara si cea mai rezistenta. Nu se sperie de focuri.</p></li>
</ul>
<p class="vn-legend">Bulinele portocalii arata cam cate focuri ii trebuie fiecarui animal. Cu un foc in cap il dobori mai repede.</p>

<h2><small>Urme si vanzare</small>Unde gasesti si unde vinzi</h2>
<div class="vn-two">
<div class="vn-card">
<h3>Urmele de pe jos</h3>
<p>Prin zona gasesti urme de animale. Apasa <kbd>E</kbd> pe ele: ingenunchezi, le cercetezi, iar personajul iti spune ce animal e prin preajma si in ce directie a luat-o (nord, sud-est si asa mai departe).</p>
<p>Nu primesti punct pe harta sau distanta, doar directia. Restul e treaba ta.</p>
</div>
<div class="vn-card">
<h3>Punctul de vanzare vanat</h3>
<p>Carnea si trofeele se vand la bucatarul de la <b>Punct de vanzare vanat</b>, marcat pe harta. Trebuie sa ai jobul de vanator.</p>
<p>Plata depinde de animal si de trofeu, iar VIP-ul iti aduce un bonus.</p>
</div>
</div>

<h2><small>De retinut</small>Sfaturi</h2>
<ul class="vn-tips">
<li><b>Un foc sperie tot vanatul din jur.</b> Animalele din apropiere o iau la fuga. Coiotii si pumele nu.</li>
<li><b>Pusca se reincarca greu.</b> Daca ratezi primul foc in fata unei pume, ai o problema.</li>
<li><b>Zona de vanatoare e zona sigura.</b> Acolo nu se trage cu alte arme. Pusca de vanatoare merge doar in zona de vanatoare si nu trage cand tintesti un jucator.</li>
<li><b>Nu conteaza cati vanatori sunteti.</b> Fiecare are animalele lui in jur, dar oricine poate impusca si transa orice animal.</li>
<li><b>Obosesti.</b> Dupa multe animale transate intr-o ora primesti mai putin din fiecare, iar la un moment dat trebuie sa te odihnesti pana poti transa din nou.</li>
<li><b><img class="eg-item" src="/items/document.webp" alt="">Licenta de vanatoare</b> se cumpara de la Centrul de licente si e valabila 7 zile. Jobul merge si fara ea.</li>
</ul>

</div>
