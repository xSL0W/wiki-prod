---
outline: false
---

<style>
.sgp {
  --bg: #0c0c0e;
  --card: #18181b;
  --edge: #27272a;
  --line: #3f3f46;
  --text: #f4f4f5;
  --mute: #a1a1aa;
  --red: #cc2b2b;
  --red-deep: #b91c1c;
  --red-soft: rgba(204, 43, 43, 0.14);
  --amber: #f59e0b;
  --green: #4ade80;
  max-width: 920px;
  margin: 0 auto;
  color: var(--text);
  font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.sgp *, .sgp *::before, .sgp *::after { box-sizing: border-box; }
.sgp p, .sgp li { line-height: 1.6; color: var(--text); margin: 0; }
.sgp ul, .sgp ol { list-style: none; padding: 0; margin: 0; }
.sgp li + li { margin-top: 0; }
.sgp b { color: #fff; font-weight: 650; }
.sgp code { white-space: normal; overflow-wrap: anywhere; }
.sgp a { color: #ff6b6b; text-decoration: underline; text-underline-offset: 3px; overflow-wrap: anywhere; }
.sgp a:hover { color: #fff; }
.sgp a:focus-visible { outline: 3px solid var(--red); outline-offset: 2px; border-radius: 4px; }
.sgp kbd {
  font: inherit; font-size: 0.85em; font-weight: 700; color: #fff; background: var(--red-deep);
  border-radius: 6px; padding: 0.05rem 0.45rem; white-space: nowrap;
}
/* hero */
.sgp-hero {
  background: radial-gradient(110% 120% at 100% 0%, rgba(185, 28, 28, 0.28), var(--bg) 60%);
  border: 1px solid var(--edge);
  border-radius: 20px;
  padding: clamp(1.25rem, 4vw, 2.5rem);
}
.sgp-hero h1 {
  margin: 0 0 0.6rem; border: 0; padding: 0;
  font-size: clamp(2rem, 6vw, 3.2rem); line-height: 1.05; font-weight: 800; letter-spacing: -0.03em; color: #fff;
}
.sgp-hero h1 span { color: var(--red); }
.sgp .sgp-lead { max-width: 60ch; color: var(--mute); font-size: 1.05rem; }
.sgp .sgp-jump { display: flex; flex-wrap: wrap; gap: 0.45rem; margin-top: 1.2rem; }
.sgp .sgp-jump li { margin: 0; }
.sgp .sgp-jump a {
  display: inline-block; text-decoration: none; color: var(--text); font-size: 0.88rem; font-weight: 600;
  border: 1px solid var(--line); border-radius: 999px; padding: 0.2rem 0.75rem; background: var(--bg);
}
.sgp .sgp-jump a:hover { border-color: var(--red); color: #fff; }
.sgp .sgp-jump a span { color: var(--red); font-weight: 800; margin-right: 0.3rem; }
/* sections */
.sgp h2 {
  margin: 3rem 0 0.4rem; border: 0; padding: 0; scroll-margin-top: 90px;
  font-size: 1.5rem; font-weight: 750; letter-spacing: -0.015em; color: #fff;
}
.sgp h2 span { color: var(--red); margin-right: 0.4rem; }
.sgp .sgp-intro { color: var(--mute); max-width: 66ch; margin-bottom: 1rem; }
.sgp .sgp-label {
  margin: 1.2rem 0 0.5rem; font-size: 0.72rem; font-weight: 800; letter-spacing: 0.1em;
  text-transform: uppercase; color: var(--mute);
}
.sgp .sgp-note {
  margin-top: 1rem; padding: 0.7rem 0.9rem; border-left: 3px solid var(--amber);
  background: var(--card); border-radius: 0 10px 10px 0; color: var(--mute); font-size: 0.93rem;
}
.sgp .sgp-note.red { border-left-color: var(--red); }
.sgp .sgp-note b { color: #fff; }
/* fps presets */
.sgp .sgp-presets { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 0.8rem; }
.sgp .sgp-preset {
  background: var(--card); border: 1px solid var(--edge); border-radius: 16px; padding: 1rem;
  display: flex; flex-direction: column; gap: 0.6rem;
}
.sgp .sgp-preset.hot { border-color: var(--red-deep); background: linear-gradient(160deg, var(--red-soft), var(--card) 65%); }
.sgp .sgp-preset h3 { margin: 0; border: 0; padding: 0; font-size: 1.1rem; font-weight: 750; color: #fff; }
.sgp .sgp-preset p { font-size: 0.92rem; color: var(--mute); }
.sgp .sgp-bars { display: grid; gap: 0.35rem; margin-top: auto; }
.sgp .sgp-bar { display: grid; grid-template-columns: 5.6rem 1fr; align-items: center; gap: 0.5rem; font-size: 0.75rem; color: var(--mute); }
.sgp .sgp-bar i { display: block; height: 6px; border-radius: 999px; background: var(--edge); overflow: hidden; }
.sgp .sgp-bar i::after { content: ''; display: block; height: 100%; width: var(--v); background: var(--red); border-radius: 999px; }
.sgp .sgp-bar.q i::after { background: var(--mute); }
/* steps */
.sgp .sgp-do { display: grid; gap: 0.45rem; counter-reset: sgp-s; }
.sgp .sgp-do > li { margin: 0; position: relative; padding-left: 2rem; counter-increment: sgp-s; }
.sgp .sgp-do > li::before {
  content: counter(sgp-s); position: absolute; left: 0; top: 0.15em;
  display: grid; place-items: center; width: 1.4rem; height: 1.4rem; border-radius: 50%;
  background: var(--edge); color: #fff; font-size: 0.75rem; font-weight: 800;
}
.sgp .sgp-panel {
  background: var(--card); border: 1px solid var(--edge); border-radius: 18px;
  padding: clamp(1rem, 3vw, 1.5rem);
}
/* console commands */
.sgp .sgp-cmds { display: grid; gap: 0.6rem; }
.sgp .sgp-cmd {
  display: grid; grid-template-columns: minmax(0, 15rem) 1fr; gap: 0.4rem 1rem; align-items: baseline;
  background: var(--card); border: 1px solid var(--edge); border-radius: 14px; padding: 0.8rem 1rem;
}
.sgp .sgp-cmd code { font-size: 0.95rem; }
.sgp .sgp-cmd p { color: var(--mute); font-size: 0.93rem; }
/* gta settings */
.sgp .sgp-tier { margin-top: 1.4rem; }
.sgp .sgp-tier h3 {
  display: flex; align-items: flex-start; gap: 0.6rem; margin: 0 0 0.6rem; border: 0; padding: 0;
  font-size: 1.1rem; font-weight: 750; color: #fff;
}
.sgp .sgp-tier h3 em {
  font-style: normal; font-size: 0.7rem; font-weight: 800; letter-spacing: 0.08em; text-transform: uppercase;
  border-radius: 999px; padding: 0.1rem 0.55rem; color: #fff; background: var(--red-deep);
}
.sgp .sgp-tier.mid h3 em { background: #92400e; }
.sgp .sgp-tier.low h3 em { background: var(--line); }
.sgp .sgp-rows { background: var(--card); border: 1px solid var(--edge); border-radius: 16px; overflow: hidden; }
.sgp .sgp-row {
  display: grid; grid-template-columns: minmax(0, 1.3fr) minmax(0, 0.8fr) minmax(0, 0.8fr); gap: 0.3rem 0.8rem;
  padding: 0.75rem 1rem; border-top: 1px solid var(--edge); align-items: start;
}
.sgp .sgp-row:first-child { border-top: 0; }
.sgp .sgp-row.head { background: var(--bg); font-size: 0.72rem; font-weight: 800; letter-spacing: 0.08em; text-transform: uppercase; color: var(--mute); }
.sgp .sgp-row .sgp-name { font-weight: 700; color: #fff; }
.sgp .sgp-row .sgp-why { grid-column: 1 / -1; color: var(--mute); font-size: 0.88rem; }
.sgp .sgp-val { font-size: 0.9rem; }
.sgp .sgp-val small { display: none; color: var(--mute); font-size: 0.72rem; margin-right: 0.3rem; }
.sgp .sgp-val.best { color: var(--green); font-weight: 650; }
/* pc tips */
.sgp .sgp-cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 0.8rem; }
.sgp .sgp-card { background: var(--card); border: 1px solid var(--edge); border-radius: 16px; padding: 1rem; }
.sgp .sgp-card h3 { margin: 0 0 0.6rem; border: 0; padding: 0; font-size: 1.05rem; font-weight: 750; color: #fff; }
.sgp .sgp-card .sgp-do > li { font-size: 0.93rem; }
/* still low */
.sgp .sgp-help {
  margin-top: 3rem; border: 1px solid var(--red-deep); border-radius: 18px;
  background: linear-gradient(160deg, var(--red-soft), var(--card) 60%);
  padding: clamp(1.1rem, 3vw, 1.6rem);
}
.sgp .sgp-help h2 { margin: 0 0 0.6rem; }
.sgp .sgp-help .sgp-do { margin-top: 0.6rem; }
@media (max-width: 560px) {
  .sgp .sgp-cmd { grid-template-columns: 1fr; }
  .sgp .sgp-row { grid-template-columns: 1fr; }
  .sgp .sgp-row .sgp-name { grid-column: 1 / -1; }
  .sgp .sgp-row.head { display: none; }
  .sgp .sgp-val small { display: inline; }
}
@media (prefers-reduced-motion: no-preference) {
  .sgp .sgp-jump a { transition: border-color 0.2s, color 0.2s; }
}
</style>

<div class="sgp">
<section class="sgp-hero">
<h1>Setari pentru <span>performanta</span></h1>
<p class="sgp-lead">Ai FPS mic sau sacadeaza jocul in oras? Incepe cu FPS Booster-ul din joc, apoi scade setarile GTA care costa cel mai mult. La final, pune Windows-ul si placa video sa lucreze pentru joc.</p>
<ul class="sgp-jump">
<li><a href="#fps-booster"><span>1</span>FPS Booster</a></li>
<li><a href="#masoara"><span>2</span>Vezi cat FPS ai</a></li>
<li><a href="#beta"><span>3</span>FiveM pe Beta</a></li>
<li><a href="#setari-gta"><span>4</span>Setarile GTA V</a></li>
<li><a href="#windows"><span>5</span>Windows si placa video</a></li>
</ul>
</section>
<h2 id="fps-booster"><span>1</span>FPS Booster: comanda /fps</h2>
<p class="sgp-intro">Scrie <code>/fps</code> in chat si alege un profil. Profilul taie din umbre si din lumini, lucrurile care trag cel mai tare de placa video in oras.</p>
<div class="sgp-presets">
<div class="sgp-preset">
<h3>Dezactivat</h3>
<p>Jocul ramane cu setarile lui normale. Alege-l ca sa scoti profilul pus inainte.</p>
<div class="sgp-bars"><div class="sgp-bar"><span>Performanta</span><i style="--v: 15%"></i></div><div class="sgp-bar q"><span>Calitate</span><i style="--v: 100%"></i></div></div>
</div>
<div class="sgp-preset">
<h3>Medium</h3>
<p>Umbre mai scurte, luminile se vad de mai aproape. Luminile orasului raman aprinse. Bun daca ai FPS putin sub cat vrei.</p>
<div class="sgp-bars"><div class="sgp-bar"><span>Performanta</span><i style="--v: 50%"></i></div><div class="sgp-bar q"><span>Calitate</span><i style="--v: 70%"></i></div></div>
</div>
<div class="sgp-preset hot">
<h3>Low</h3>
<p>Umbrele aproape dispar si se sting luminile orasului: stalpi, cladiri, reclame. Farurile masinilor raman aprinse. Nu mai vezi urme de gloante sau de sange.</p>
<div class="sgp-bars"><div class="sgp-bar"><span>Performanta</span><i style="--v: 80%"></i></div><div class="sgp-bar q"><span>Calitate</span><i style="--v: 40%"></i></div></div>
</div>
<div class="sgp-preset hot">
<h3>Ultra Low</h3>
<p>Ca Low, dar taie si mai mult din lumini, inclusiv din raza lanternei. Pentru PC-uri slabe, cand ai nevoie de fiecare cadru.</p>
<div class="sgp-bars"><div class="sgp-bar"><span>Performanta</span><i style="--v: 100%"></i></div><div class="sgp-bar q"><span>Calitate</span><i style="--v: 20%"></i></div></div>
</div>
</div>
<p class="sgp-note"><b>Profilul ramane salvat pe personaj.</b> Il pui o data si porneste singur la fiecare intrare. In interioare (case, magazine, sedii) profilul se opreste singur si revine cand iesi afara.</p>
<p class="sgp-note red"><b>Noaptea, pe Low si Ultra Low, orasul e intunecat</b>, pentru ca se sting luminile de pe strada si de pe cladiri. Daca vezi prea greu, treci pe Medium.</p>
<p class="sgp-note">Daca stai mai mult de 30 de secunde sub 35 FPS si nu ai niciun profil pus, primesti o notificare care iti aminteste de <code>/fps</code>.</p>
<h2 id="masoara"><span>2</span>Vezi cat FPS ai</h2>
<p class="sgp-intro">Inainte sa schimbi ceva, uita-te cat FPS ai acum, ca sa vezi daca o setare chiar ajuta. Apasa <kbd>F8</kbd> ca sa deschizi consola FiveM, scrie comanda si apasa Enter. Cu <code>false</code> in loc de <code>true</code> o opresti.</p>
<div class="sgp-cmds">
<div class="sgp-cmd"><code>cl_drawfps true</code><p>Arata FPS-ul in coltul ecranului.</p></div>
<div class="sgp-cmd"><code>cl_drawperf true</code><p>Arata FPS, ping, pierderea de pachete, cat lucreaza procesorul si placa video si temperatura placii video.</p></div>
<div class="sgp-cmd"><code>resmon true</code><p>Arata cat consuma fiecare script de pe server. Merge doar pe canalul <b>Beta</b> (vezi pasul 3).</p></div>
</div>
<p class="sgp-note">Placa video la 99% inseamna ca ea te tine pe loc: scade setarile grafice de la pasul 4. Placa video mult sub 99% si FPS tot mic inseamna ca procesorul nu tine pasul: scade <b>Distance Scaling</b> si <b>Population Density</b> si inchide programele din fundal.</p>
<h2 id="beta"><span>3</span>FiveM pe canalul Beta</h2>
<p class="sgp-intro">Pe serverul nostru recomandam canalul de actualizare <b>Beta</b> al FiveM. Primesti mai repede reparatiile facute de echipa FiveM, iar comenzile de diagnostic ca <code>resmon</code> merg direct.</p>
<div class="sgp-panel">
<p class="sgp-label" style="margin-top: 0">Din meniul FiveM</p>
<ol class="sgp-do">
<li>Deschide FiveM si intra in <b>Settings</b> (rotita din dreapta sus).</li>
<li>La <b>Update Channel</b> alege <b>Beta</b>. Nu alege <b>Latest</b>: e o versiune de test si poate da crash.</li>
<li>Inchide FiveM si deschide-l din nou. Se actualizeaza singur.</li>
</ol>
<p class="sgp-label">Sau din fisier</p>
<ol class="sgp-do">
<li>Apasa <kbd>Win + R</kbd>, scrie <code>%localappdata%\FiveM\FiveM.app\CitizenFX.ini</code> si apasa Enter.</li>
<li>Sub <code>[Game]</code> adauga randul <code>UpdateChannel=beta</code>.</li>
<li>Optional, adauga si <code>SavedBuildNumber=3570</code>. FiveM porneste direct pe versiunea de GTA ceruta de server, asa ca nu se mai reporneste la conectare.</li>
<li>Salveaza fisierul si porneste FiveM.</li>
</ol>
</div>
<h2 id="setari-gta"><span>4</span>Setarile GTA V</h2>
<p class="sgp-intro">Apasa <kbd>ESC</kbd>, apoi <b>Setari joc</b>. In meniul GTA intra la <b>Settings → Graphics</b> si <b>Settings → Advanced Graphics</b>. Le-am pus in ordinea in care merita sa le scazi: sus sunt cele care iti mananca cele mai multe FPS.</p>
<div class="sgp-tier">
<h3><em>Mare</em>Scade-le pe acestea primele</h3>
<div class="sgp-rows">
<div class="sgp-row head"><span>Setare</span><span>PC slab</span><span>PC puternic</span></div>
<div class="sgp-row"><span class="sgp-name">MSAA</span><span class="sgp-val best"><small>PC slab:</small>Off</span><span class="sgp-val"><small>PC puternic:</small>Off sau 2x</span><span class="sgp-why">Netezeste marginile, dar e cea mai scumpa setare din joc. Foloseste FXAA in locul ei.</span></div>
<div class="sgp-row"><span class="sgp-name">Grass Quality</span><span class="sgp-val best"><small>PC slab:</small>Normal</span><span class="sgp-val"><small>PC puternic:</small>High</span><span class="sgp-why">Pe Very High si Ultra iarba scade FPS-ul mult, mai ales in afara orasului.</span></div>
<div class="sgp-row"><span class="sgp-name">Shadow Quality</span><span class="sgp-val best"><small>PC slab:</small>Normal</span><span class="sgp-val"><small>PC puternic:</small>High</span><span class="sgp-why">Umbrele costa mult in oras, unde sunt multe cladiri.</span></div>
<div class="sgp-row"><span class="sgp-name">Reflection Quality</span><span class="sgp-val best"><small>PC slab:</small>Normal</span><span class="sgp-val"><small>PC puternic:</small>High</span><span class="sgp-why">Reflexiile din geamuri, masini si balti.</span></div>
<div class="sgp-row"><span class="sgp-name">Reflection MSAA</span><span class="sgp-val best"><small>PC slab:</small>Off</span><span class="sgp-val"><small>PC puternic:</small>Off</span><span class="sgp-why">MSAA doar pe reflexii. Costa mult si aproape nu se vede.</span></div>
<div class="sgp-row"><span class="sgp-name">Post FX</span><span class="sgp-val best"><small>PC slab:</small>Normal</span><span class="sgp-val"><small>PC puternic:</small>High</span><span class="sgp-why">Efectele de imagine: stralucire, ceata, blur. Pe Very High si Ultra costa mult.</span></div>
<div class="sgp-row"><span class="sgp-name">Distance Scaling</span><span class="sgp-val best"><small>PC slab:</small>sub jumatate</span><span class="sgp-val"><small>PC puternic:</small>dupa gust</span><span class="sgp-why">Cat de departe vezi detalii. Incarca mai ales procesorul.</span></div>
<div class="sgp-row"><span class="sgp-name">Population Density / Variety</span><span class="sgp-val best"><small>PC slab:</small>la minim</span><span class="sgp-val"><small>PC puternic:</small>la jumatate</span><span class="sgp-why">Incarca procesorul si memoria video. Daca ai procesor slab, scade-le.</span></div>
</div>
</div>
<div class="sgp-tier mid">
<h3><em>Mediu</em>Pune-le la mijloc</h3>
<div class="sgp-rows">
<div class="sgp-row head"><span>Setare</span><span>PC slab</span><span>PC puternic</span></div>
<div class="sgp-row"><span class="sgp-name">Soft Shadows</span><span class="sgp-val best"><small>PC slab:</small>Sharp</span><span class="sgp-val"><small>PC puternic:</small>Softer</span><span class="sgp-why">NVIDIA PCSS si AMD CHS arata frumos, dar costa mult.</span></div>
<div class="sgp-row"><span class="sgp-name">Ambient Occlusion</span><span class="sgp-val best"><small>PC slab:</small>Off</span><span class="sgp-val"><small>PC puternic:</small>Normal</span><span class="sgp-why">Umbrele mici din colturi si de sub obiecte.</span></div>
<div class="sgp-row"><span class="sgp-name">Particles Quality</span><span class="sgp-val best"><small>PC slab:</small>Normal</span><span class="sgp-val"><small>PC puternic:</small>High</span><span class="sgp-why">Fum, foc, praf, scantei. Cade mult FPS-ul in schimburi de focuri si la explozii.</span></div>
<div class="sgp-row"><span class="sgp-name">Water Quality</span><span class="sgp-val best"><small>PC slab:</small>Normal</span><span class="sgp-val"><small>PC puternic:</small>High</span><span class="sgp-why">Conteaza doar langa apa.</span></div>
<div class="sgp-row"><span class="sgp-name">Shader Quality</span><span class="sgp-val best"><small>PC slab:</small>Normal</span><span class="sgp-val"><small>PC puternic:</small>Very High</span><span class="sgp-why">Lumina si materialele. Schimba mult cum arata jocul.</span></div>
<div class="sgp-row"><span class="sgp-name">Tessellation</span><span class="sgp-val best"><small>PC slab:</small>Off</span><span class="sgp-val"><small>PC puternic:</small>Normal</span><span class="sgp-why">Adauga relief pe copaci si pe unele suprafete.</span></div>
<div class="sgp-row"><span class="sgp-name">Motion Blur / Depth of Field</span><span class="sgp-val best"><small>PC slab:</small>0 / Off</span><span class="sgp-val"><small>PC puternic:</small>dupa gust</span><span class="sgp-why">Blur la miscare si fundal estompat. Multi le opresc ca sa vada mai clar.</span></div>
</div>
</div>
<div class="sgp-tier low">
<h3><em>Mic</em>Pe acestea le poti lasa sus</h3>
<div class="sgp-rows">
<div class="sgp-row head"><span>Setare</span><span>PC slab</span><span>PC puternic</span></div>
<div class="sgp-row"><span class="sgp-name">FXAA</span><span class="sgp-val best"><small>PC slab:</small>On</span><span class="sgp-val"><small>PC puternic:</small>On</span><span class="sgp-why">Netezeste marginile aproape gratis. Imaginea iese putin mai moale.</span></div>
<div class="sgp-row"><span class="sgp-name">Anisotropic Filtering</span><span class="sgp-val best"><small>PC slab:</small>x8</span><span class="sgp-val"><small>PC puternic:</small>x16</span><span class="sgp-why">Drumurile si zidurile vazute din unghi raman clare. Costa foarte putin.</span></div>
<div class="sgp-row"><span class="sgp-name">Texture Quality</span><span class="sgp-val best"><small>PC slab:</small>Normal</span><span class="sgp-val"><small>PC puternic:</small>Very High</span><span class="sgp-why">Nu scade mult FPS-ul, dar umple memoria video. Urmareste bara Video Memory din susul meniului.</span></div>
</div>
</div>
<div class="sgp-tier">
<h3><em>Afisaj</em>Imaginea si Advanced Graphics</h3>
<div class="sgp-rows">
<div class="sgp-row head"><span>Setare</span><span>Ce alegi</span><span></span></div>
<div class="sgp-row"><span class="sgp-name">DirectX Version</span><span class="sgp-val best"><small>Alegi:</small>DirectX 11</span><span class="sgp-val"></span><span class="sgp-why">Versiunile mai vechi taie din grafica si nu aduc FPS in plus pe placile video de azi.</span></div>
<div class="sgp-row"><span class="sgp-name">Screen Type</span><span class="sgp-val best"><small>Alegi:</small>Fullscreen</span><span class="sgp-val"></span><span class="sgp-why">In fullscreen jocul are de obicei FPS mai mare si mai stabil decat in Windowed.</span></div>
<div class="sgp-row"><span class="sgp-name">Resolution / Refresh Rate</span><span class="sgp-val best"><small>Alegi:</small>cele ale monitorului</span><span class="sgp-val"></span><span class="sgp-why">Rezolutia nativa si rata maxima a monitorului (de exemplu 144Hz).</span></div>
<div class="sgp-row"><span class="sgp-name">VSync</span><span class="sgp-val best"><small>Alegi:</small>Off</span><span class="sgp-val"></span><span class="sgp-why">Pe On FPS-ul se blocheaza la rata monitorului si poti simti o mica intarziere. Pune-l pe On doar daca vezi imaginea rupta.</span></div>
<div class="sgp-row"><span class="sgp-name">Ignore Suggested Limits</span><span class="sgp-val best"><small>Alegi:</small>Off</span><span class="sgp-val"></span><span class="sgp-why">Pe On poti trece de memoria video a placii: texturi care nu se incarca si crash-uri.</span></div>
<div class="sgp-row"><span class="sgp-name">Long Shadows, High Resolution Shadows, Extended Shadows Distance</span><span class="sgp-val best"><small>Alegi:</small>Off</span><span class="sgp-val"></span><span class="sgp-why">Umbre mai lungi si mai fine, cu un cost mare.</span></div>
<div class="sgp-row"><span class="sgp-name">Extended Distance Scaling, High Detail Streaming While Flying</span><span class="sgp-val best"><small>Alegi:</small>Off</span><span class="sgp-val"></span><span class="sgp-why">Detalii in plus la distanta si din aer. Incarca procesorul.</span></div>
<div class="sgp-row"><span class="sgp-name">Frame Scaling Mode</span><span class="sgp-val best"><small>Alegi:</small>Off</span><span class="sgp-val"></span><span class="sgp-why">Peste Off jocul randeaza la rezolutie mai mare si FPS-ul se duce. Sub Off (de exemplu 5/6) castigi FPS pe o placa video slaba, dar imaginea iese mai neclara.</span></div>
</div>
</div>
<p class="sgp-note"><b>Harta sau hainele se incarca greu?</b> In <b>Settings → Graphics</b> FiveM adauga setarea <b>Extended Texture Budget</b>. Daca bara Video Memory mai are loc, creste-o putin. Daca bara e plina, scade <b>Texture Quality</b>.</p>
<p class="sgp-note red"><b>Fara moduri grafice.</b> ReShade, NaturalVision, QuantV si altele scad FPS-ul si dau crash pe server. Le scoti cum scrie la <a href="/zona-info/probleme-generale#pas-9">Probleme generale, pasul 9</a>.</p>
<h2 id="windows"><span>5</span>Windows si placa video</h2>
<p class="sgp-intro">Cateva setari din afara jocului care ajuta mult, mai ales pe laptop.</p>
<div class="sgp-cards">
<div class="sgp-card">
<h3>Windows</h3>
<ol class="sgp-do">
<li>Pune FiveM pe placa video dedicata si porneste <b>Game Mode</b>: <a href="/zona-info/probleme-generale#pas-4">Probleme generale, pasul 4</a>.</li>
<li>In <b>Settings → System → Power</b> alege <b>Best performance</b>.</li>
<li>Pe laptop, joaca cu incarcatorul in priza. Pe baterie placa video merge mai incet.</li>
<li>Inchide ce nu folosesti: browser-ul cu multe taburi, programe de inregistrare, overlay-uri (Steam, Discord, NVIDIA).</li>
</ol>
</div>
<div class="sgp-card">
<h3>NVIDIA</h3>
<ol class="sgp-do">
<li>Tine driverul la zi: <a href="/zona-info/probleme-generale#pas-3">Probleme generale, pasul 3</a>.</li>
<li>Deschide <b>NVIDIA Control Panel → Manage 3D settings → Program Settings</b> si adauga <code>FiveM_b3570_GTAProcess.exe</code> (il gasesti in Task Manager cat esti in joc).</li>
<li>La <b>Power management mode</b> alege <b>Prefer maximum performance</b>.</li>
<li>La <b>Low Latency Mode</b> alege <b>On</b>.</li>
</ol>
</div>
<div class="sgp-card">
<h3>AMD</h3>
<ol class="sgp-do">
<li>Tine driverul la zi: <a href="/zona-info/probleme-generale#pas-3">Probleme generale, pasul 3</a>.</li>
<li>Deschide <b>AMD Software: Adrenalin Edition → Gaming → Graphics</b>.</li>
<li>Porneste <b>Radeon Anti-Lag</b>.</li>
<li>Opreste <b>Radeon Chill</b>: iti blocheaza FPS-ul cand stai pe loc.</li>
</ol>
</div>
</div>
<p class="sgp-note">Jocul se incarca mai repede de pe <b>SSD</b> decat de pe HDD: orasul si hainele apar mai repede cand te misti. Daca ai SSD, pune GTA V si FiveM pe el.</p>
<section class="sgp-help">
<h2>Tot ai FPS mic sau crash-uri?</h2>
<p>De multe ori nu e de la setari, ci de la cache, drivere sau fisierele jocului. Treci prin pasii de pe pagina de probleme:</p>
<ol class="sgp-do">
<li><a href="/zona-info/probleme-generale#pas-5">Sterge cache-ul FiveM</a> daca ai crash la intrare sau texturi lipsa.</li>
<li><a href="/zona-info/probleme-generale#pas-3">Actualizeaza driverele</a> daca ai ecran negru sau artefacte.</li>
<li><a href="/zona-info/probleme-generale#pas-7">Verifica fisierele GTA V</a> daca jocul da crash fara motiv.</li>
</ol>
</section>
</div>
