---
outline: false
---

<style>
.cj {
  --bg: #0c0c0e;
  --card: #18181b;
  --edge: #27272a;
  --line: #3f3f46;
  --text: #f4f4f5;
  --mute: #a1a1aa;
  --red: #cc2b2b;
  --red-deep: #b91c1c;
  --red-soft: rgba(204, 43, 43, 0.14);
  max-width: 920px;
  margin: 0 auto;
  color: var(--text);
  font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.cj *, .cj *::before, .cj *::after { box-sizing: border-box; }
.cj p, .cj li { line-height: 1.6; color: var(--text); margin: 0; }
.cj ul, .cj ol { list-style: none; padding: 0; margin: 0; }
.cj b { color: #fff; font-weight: 650; }
.cj code { white-space: normal; overflow-wrap: anywhere; }
.cj a { color: #ff6b6b; text-decoration: underline; text-underline-offset: 3px; }
.cj a:hover { color: #fff; }
.cj a:focus-visible { outline: 3px solid var(--red); outline-offset: 2px; border-radius: 4px; }
.cj kbd {
  font: inherit; font-size: 0.85em; font-weight: 700; color: #fff; background: var(--red-deep);
  border-radius: 6px; padding: 0.05rem 0.45rem; white-space: nowrap;
}
/* hero: the five steps as a progress track */
.cj-hero {
  background: radial-gradient(110% 120% at 100% 0%, rgba(185, 28, 28, 0.28), var(--bg) 60%);
  border: 1px solid var(--edge);
  border-radius: 20px;
  padding: clamp(1.25rem, 4vw, 2.5rem);
  overflow: hidden;
}
.cj-hero h1 {
  margin: 0 0 0.6rem; border: 0; padding: 0;
  font-size: clamp(2rem, 6vw, 3.2rem); line-height: 1.05; font-weight: 800; letter-spacing: -0.03em; color: #fff;
}
.cj-hero h1 span { color: var(--red); }
.cj .cj-lead { max-width: 56ch; color: var(--mute); font-size: 1.05rem; }
.cj .cj-track {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 0.6rem;
  margin-top: 1.6rem; counter-reset: cj-t;
}
.cj .cj-track li {
  margin: 0; counter-increment: cj-t;
  display: flex; align-items: center; gap: 0.6rem;
  background: var(--card); border: 1px solid var(--edge); border-radius: 12px;
  padding: 0.6rem 0.8rem; font-size: 0.92rem; font-weight: 600; line-height: 1.25;
}
.cj .cj-track li::before {
  content: counter(cj-t); flex: none; display: grid; place-items: center;
  width: 1.7rem; height: 1.7rem; border-radius: 50%;
  background: var(--red-deep); color: #fff; font-weight: 800; font-size: 0.85rem;
}
.cj .cj-track a { color: inherit; text-decoration: none; }
/* steps */
.cj .cj-steps { margin-top: 2.5rem; display: grid; gap: 1.1rem; }
.cj .cj-step {
  display: grid; grid-template-columns: 3rem minmax(0, 1fr); gap: 0 1.1rem;
  background: var(--card); border: 1px solid var(--edge); border-radius: 18px;
  padding: clamp(1rem, 3vw, 1.5rem); scroll-margin-top: 90px;
}
.cj .cj-step.must { border-color: var(--red-deep); background: linear-gradient(160deg, var(--red-soft), var(--card) 55%); }
.cj .cj-num {
  display: grid; place-items: center; width: 3rem; height: 3rem; border-radius: 14px;
  background: var(--bg); border: 2px solid var(--red); color: #fff; font-weight: 800; font-size: 1.3rem;
}
.cj .cj-step h2 {
  margin: 0.2rem 0 0.5rem; border: 0; padding: 0;
  font-size: 1.3rem; font-weight: 750; letter-spacing: -0.01em; color: #fff;
  display: flex; flex-wrap: wrap; align-items: center; gap: 0.5rem;
}
.cj .cj-tag {
  font-size: 0.7rem; font-weight: 800; letter-spacing: 0.08em; text-transform: uppercase;
  border-radius: 999px; padding: 0.15rem 0.6rem; background: var(--edge); color: var(--mute);
}
.cj .cj-tag.req { background: var(--red-deep); color: #fff; }
.cj .cj-body { min-width: 0; }
.cj .cj-body > p { color: var(--mute); max-width: 64ch; }
.cj .cj-do { margin-top: 0.8rem; display: grid; gap: 0.45rem; }
.cj .cj-do li { margin: 0; position: relative; padding-left: 1.3rem; }
.cj .cj-do li::before {
  content: ''; position: absolute; left: 0.15rem; top: 0.62em; width: 7px; height: 7px;
  border-radius: 2px; background: var(--red); transform: rotate(45deg);
}
.cj .cj-path {
  display: flex; flex-wrap: wrap; align-items: center; gap: 0.35rem; margin-top: 0.8rem;
}
.cj .cj-path span {
  font-size: 0.85rem; font-weight: 600; border: 1px solid var(--line); border-radius: 8px;
  padding: 0.15rem 0.55rem; background: var(--bg);
}
.cj .cj-path i { font-style: normal; color: var(--mute); }
.cj .cj-hint {
  margin-top: 0.9rem; padding: 0.7rem 0.9rem; border-left: 3px solid var(--red);
  background: var(--bg); border-radius: 0 10px 10px 0; color: var(--mute); font-size: 0.95rem;
}
/* screenshots */
.cj .cj-shot { grid-column: 1 / -1; margin: 1.1rem 0 0; }
.cj .cj-shot a { display: block; text-decoration: none; }
.cj .cj-shot img {
  display: block; width: 100%; height: auto; margin: 0;
  border: 1px solid var(--line); border-radius: 12px; background: var(--bg);
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.45);
}
.cj .cj-shot figcaption { margin-top: 0.5rem; font-size: 0.85rem; color: var(--mute); text-align: center; }
@media (max-width: 560px) {
  .cj .cj-step { grid-template-columns: minmax(0, 1fr); }
  .cj .cj-num { width: 2.4rem; height: 2.4rem; font-size: 1.05rem; border-radius: 11px; margin-bottom: 0.4rem; }
}
@media (prefers-reduced-motion: no-preference) {
  .cj .cj-track li { transition: border-color 0.2s; }
  .cj .cj-track li:hover { border-color: var(--red); }
}
</style>

<div class="cj">
<section class="cj-hero">
<h1>Cum intri pe <span>EliteGamers</span></h1>
<p class="cj-lead">Cinci pasi de la zero pana in oras. Primii doi ii faci o singura data, restul doar cand ai nevoie.</p>
<ol class="cj-track">
<li><a href="#pas-1">Instaleaza FiveM</a></li>
<li><a href="#pas-2">Treci pe Beta</a></li>
<li><a href="#pas-3">Sterge cache-ul</a></li>
<li><a href="#pas-4">Conecteaza-te</a></li>
<li><a href="#pas-5">Citeste regulile</a></li>
</ol>
</section>
<div class="cj-steps">
<section class="cj-step" id="pas-1">
<div class="cj-num">1</div>
<div class="cj-body">
<h2>Instaleaza FiveM</h2>
<p>FiveM este aplicatia prin care intri pe serverele de GTA V. Ai nevoie de GTA V cumparat pe PC.</p>
<ul class="cj-do">
<li>Descarca FiveM de pe <a href="https://fivem.net" target="_blank" rel="noopener">fivem.net</a> si instaleaza-l.</li>
<li>Deschide FiveM si asteapta sa se incarce complet.</li>
</ul>
</div>
</section>
<section class="cj-step must" id="pas-2">
<div class="cj-num">2</div>
<div class="cj-body">
<h2>Treci pe versiunea Beta <span class="cj-tag req">Recomandat</span></h2>
<p>Iti recomandam canalul Beta: cu el jocul merge cel mai bine pe server. Setarea ramane salvata, o faci o singura data.</p>
<div class="cj-path"><span>Rotita (Settings)</span><i>›</i><span>Game</span><i>›</i><span>Update channel</span><i>›</i><span>Beta</span></div>
<ul class="cj-do">
<li>FiveM iti cere restart. Inchide-l si deschide-l din nou.</li>
</ul>
</div>
<figure class="cj-shot">
<a href="/bg/eg.gif" target="_blank" rel="noopener"><img src="/bg/eg.gif" alt="Setarile FiveM: Game, Update channel, Beta" width="1920" height="1080" loading="lazy"></a>
<figcaption>Settings, Game, Update channel, Beta. Apasa pe imagine pentru marime completa.</figcaption>
</figure>
</section>
<section class="cj-step" id="pas-3">
<div class="cj-num">3</div>
<div class="cj-body">
<h2>Sterge cache-ul <span class="cj-tag">Recomandat</span></h2>
<p>Un cache vechi sau stricat da crash la intrare si texturi lipsa. Sterge-l inainte de prima intrare si oricand ai probleme.</p>
<ul class="cj-do">
<li>Click dreapta pe iconita FiveM, apoi <b>Open file location</b>.</li>
<li>Intra in <b>FiveM Application Data</b>, apoi in folderul <b>data</b>.</li>
<li>Sterge folderele <code>cache</code>, <code>server-cache</code> si <code>server-cache-priv</code>.</li>
</ul>
<p class="cj-hint">Prima conectare dupa stergere dureaza mai mult, pentru ca jocul descarca totul din nou. Alte solutii gasesti la <a href="/zona-info/probleme-generale">Probleme generale</a>.</p>
</div>
<figure class="cj-shot">
<a href="/bg/cache.gif" target="_blank" rel="noopener"><img src="/bg/cache.gif" alt="Stergerea folderelor cache, server-cache si server-cache-priv din FiveM Application Data" width="1920" height="1080" loading="lazy"></a>
<figcaption>Folderele de sters din FiveM Application Data, data.</figcaption>
</figure>
</section>
<section class="cj-step" id="pas-4">
<div class="cj-num">4</div>
<div class="cj-body">
<h2>Cauta serverul si conecteaza-te</h2>
<ul class="cj-do">
<li>In FiveM, apasa <b>Play</b> si scrie <b>ELITEGAMERS</b> in bara de cautare.</li>
<li>Apasa pe serverul EliteGamers din lista.</li>
<li>Apasa <b>Connect</b> si asteapta sa se incarce.</li>
</ul>
<p class="cj-hint">Mai rapid: deschide <a href="https://cfx.re/join/p9a86y" target="_blank" rel="noopener">cfx.re/join/p9a86y</a> si ajungi direct la pagina serverului.</p>
</div>
</section>
<section class="cj-step" id="pas-5">
<div class="cj-num">5</div>
<div class="cj-body">
<h2>Citeste regulamentul</h2>
<p>Inainte sa incepi roleplay-ul, citeste <a href="/zona-info/regulament">regulamentul</a>. Asa stii ce ai voie si ce nu pe server.</p>
<p class="cj-hint">In joc, apasa <kbd>F6</kbd> si wiki-ul se deschide direct pe ecran.</p>
</div>
</section>
</div>
</div>
