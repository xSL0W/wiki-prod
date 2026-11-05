---
outline: false
---

<style>
.pg {
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
  max-width: 920px;
  margin: 0 auto;
  color: var(--text);
  font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.pg *, .pg *::before, .pg *::after { box-sizing: border-box; }
.pg p, .pg li { line-height: 1.6; color: var(--text); margin: 0; }
.pg ul, .pg ol { list-style: none; padding: 0; margin: 0; }
.pg b { color: #fff; font-weight: 650; }
.pg code { white-space: normal; overflow-wrap: anywhere; }
.pg a { color: #ff6b6b; text-decoration: underline; text-underline-offset: 3px; overflow-wrap: anywhere; }
.pg a:hover { color: #fff; }
.pg a:focus-visible { outline: 3px solid var(--red); outline-offset: 2px; border-radius: 4px; }
.pg kbd {
  font: inherit; font-size: 0.85em; font-weight: 700; color: #fff; background: var(--red-deep);
  border-radius: 6px; padding: 0.05rem 0.45rem; white-space: nowrap;
}
/* hero */
.pg-hero {
  background: radial-gradient(110% 120% at 100% 0%, rgba(185, 28, 28, 0.28), var(--bg) 60%);
  border: 1px solid var(--edge);
  border-radius: 20px;
  padding: clamp(1.25rem, 4vw, 2.5rem);
}
.pg-hero h1 {
  margin: 0 0 0.6rem; border: 0; padding: 0;
  font-size: clamp(2rem, 6vw, 3.2rem); line-height: 1.05; font-weight: 800; letter-spacing: -0.03em; color: #fff;
}
.pg-hero h1 span { color: var(--red); }
.pg .pg-lead { max-width: 58ch; color: var(--mute); font-size: 1.05rem; }
/* symptom finder: what you see -> which steps */
.pg h2 {
  margin: 3rem 0 1rem; border: 0; padding: 0;
  font-size: 1.5rem; font-weight: 750; letter-spacing: -0.015em; color: #fff;
}
.pg .pg-finder { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 0.8rem; }
.pg .pg-sym { margin: 0; background: var(--card); border: 1px solid var(--edge); border-radius: 14px; padding: 0.9rem 1rem; }
.pg .pg-sym h3 { margin: 0 0 0.6rem; border: 0; padding: 0; font-size: 1rem; font-weight: 700; color: #fff; }
.pg .pg-go { display: flex; flex-wrap: wrap; gap: 0.4rem; }
.pg .pg-go li { margin: 0; }
.pg .pg-go a {
  display: inline-block; text-decoration: none; color: var(--text); font-size: 0.85rem; font-weight: 600;
  border: 1px solid var(--line); border-radius: 999px; padding: 0.15rem 0.65rem; background: var(--bg);
}
.pg .pg-go a:hover { border-color: var(--red); color: #fff; }
.pg .pg-go a span { color: var(--red); font-weight: 800; margin-right: 0.25rem; }
/* fix cards */
.pg .pg-fixes { display: grid; gap: 1rem; counter-reset: pg-n; }
.pg .pg-fix {
  background: var(--card); border: 1px solid var(--edge); border-radius: 18px;
  padding: clamp(1rem, 3vw, 1.5rem); scroll-margin-top: 90px;
}
.pg .pg-head { display: flex; align-items: flex-start; gap: 0.9rem; }
.pg .pg-num {
  flex: none; display: grid; place-items: center; width: 2.6rem; height: 2.6rem; border-radius: 12px;
  background: var(--bg); border: 2px solid var(--red); color: #fff; font-weight: 800; font-size: 1.1rem;
}
.pg .pg-fix h3 { margin: 0.15rem 0 0.25rem; border: 0; padding: 0; font-size: 1.2rem; font-weight: 750; color: #fff; }
.pg .pg-why { color: var(--mute); font-size: 0.95rem; max-width: 66ch; }
.pg .pg-label {
  margin: 1rem 0 0.5rem; font-size: 0.72rem; font-weight: 800; letter-spacing: 0.1em;
  text-transform: uppercase; color: var(--mute);
}
.pg .pg-do { display: grid; gap: 0.45rem; counter-reset: pg-s; }
.pg .pg-do > li { margin: 0; position: relative; padding-left: 2rem; counter-increment: pg-s; }
.pg .pg-do > li::before {
  content: counter(pg-s); position: absolute; left: 0; top: 0.15em;
  display: grid; place-items: center; width: 1.4rem; height: 1.4rem; border-radius: 50%;
  background: var(--edge); color: #fff; font-size: 0.75rem; font-weight: 800;
}
.pg .pg-do .pg-files { display: flex; flex-wrap: wrap; gap: 0.35rem; margin-top: 0.35rem; }
.pg .pg-do .pg-files li { margin: 0; }
.pg .pg-vendors { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 0.7rem; margin-top: 0.5rem; }
.pg .pg-vendor { background: var(--bg); border: 1px solid var(--edge); border-radius: 12px; padding: 0.8rem 0.9rem; }
.pg .pg-vendor h4 { margin: 0 0 0.5rem; border: 0; padding: 0; font-size: 0.95rem; font-weight: 750; color: #fff; }
.pg .pg-vendor .pg-do > li { font-size: 0.92rem; }
.pg .pg-note {
  margin-top: 1rem; padding: 0.7rem 0.9rem; border-left: 3px solid var(--amber);
  background: var(--bg); border-radius: 0 10px 10px 0; color: var(--mute); font-size: 0.93rem;
}
.pg .pg-note.red { border-left-color: var(--red); }
.pg .pg-note b { color: #fff; }
.pg .pg-src { margin-top: 0.6rem; font-size: 0.78rem; color: var(--mute); }
.pg .pg-shot { margin: 1.1rem 0 0; }
.pg .pg-shot a { display: block; text-decoration: none; }
.pg .pg-shot img {
  display: block; width: 100%; height: auto; margin: 0;
  border: 1px solid var(--line); border-radius: 12px; background: var(--bg);
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.45);
}
.pg .pg-shot figcaption { margin-top: 0.5rem; font-size: 0.85rem; color: var(--mute); text-align: center; }
/* still stuck */
.pg .pg-help {
  margin-top: 3rem; border: 1px solid var(--red-deep); border-radius: 18px;
  background: linear-gradient(160deg, var(--red-soft), var(--card) 60%);
  padding: clamp(1.1rem, 3vw, 1.6rem);
}
.pg .pg-help h2 { margin: 0 0 0.6rem; }
.pg .pg-help .pg-do { margin-top: 0.6rem; }
@media (max-width: 560px) {
  .pg .pg-num { width: 2.2rem; height: 2.2rem; font-size: 0.95rem; border-radius: 10px; }
}
@media (prefers-reduced-motion: no-preference) {
  .pg .pg-go a { transition: border-color 0.2s, color 0.2s; }
}
</style>

<div class="pg">
<section class="pg-hero">
<h1>Probleme <span>generale</span></h1>
<p class="pg-lead">Crash la intrare, lag, FPS mic sau nu te poti conecta? Alege mai jos ce ti se intampla si sari direct la pasul care te ajuta. Daca nu stii de unde sa incepi, ia pasii in ordine: de la cel mai simplu la cel mai complicat.</p>
</section>
<h2>Ce problema ai?</h2>
<div class="pg-finder">
<div class="pg-sym">
<h3>Crash la intrare sau texturi lipsa</h3>
<ul class="pg-go">
<li><a href="#pas-5"><span>5</span>Cache</a></li>
<li><a href="#pas-7"><span>7</span>Fisiere GTA V</a></li>
<li><a href="#pas-9"><span>9</span>Moduri grafice</a></li>
<li><a href="#pas-8"><span>8</span>Reinstalare</a></li>
</ul>
</div>
<div class="pg-sym">
<h3>Ping mare, lag, deconectari</h3>
<ul class="pg-go">
<li><a href="#pas-2"><span>2</span>Router</a></li>
<li><a href="#pas-6"><span>6</span>Reset retea</a></li>
<li><a href="#pas-3"><span>3</span>Drivere</a></li>
</ul>
</div>
<div class="pg-sym">
<h3>FPS mic, ecran negru, artefacte</h3>
<ul class="pg-go">
<li><a href="#pas-3"><span>3</span>Drivere</a></li>
<li><a href="#pas-4"><span>4</span>Placa video</a></li>
<li><a href="#pas-9"><span>9</span>Moduri grafice</a></li>
</ul>
</div>
<div class="pg-sym">
<h3>Nu stii de unde vine</h3>
<ul class="pg-go">
<li><a href="#pas-1"><span>1</span>Restart PC</a></li>
<li><a href="#pas-2"><span>2</span>Router</a></li>
<li><a href="#pas-5"><span>5</span>Cache</a></li>
</ul>
</div>
</div>
<h2>Pasii, in ordine</h2>
<div class="pg-fixes">
<section class="pg-fix" id="pas-1">
<div class="pg-head"><div class="pg-num">1</div><div>
<h3>Reporneste calculatorul</h3>
<p class="pg-why">Cel mai simplu pas si de multe ori cel care rezolva. Restartul inchide procesele blocate, elibereaza RAM-ul si reporneste driverele blocate dupa o sesiune lunga.</p>
</div></div>
<p class="pg-label">Ce faci</p>
<ol class="pg-do">
<li>Inchide complet FiveM (si din bara de langa ceas, nu doar minimizat).</li>
<li>Apasa <b>Start → Power → Restart</b>. Nu folosi <b>Shut down</b> urmat de pornire: Windows porneste rapid (Fast Boot) si nu reseteaza tot.</li>
<li>Dupa ce porneste sistemul, incearca din nou sa te conectezi.</li>
</ol>
</section>
<section class="pg-fix" id="pas-2">
<div class="pg-head"><div class="pg-num">2</div><div>
<h3>Reporneste router-ul</h3>
<p class="pg-why">Ping mare, deconectari aleatorii sau eroarea „Failed handshake to server”? De cele mai multe ori vina e la router.</p>
</div></div>
<p class="pg-label">Ce faci</p>
<ol class="pg-do">
<li>Scoate din priza cablul de alimentare al router-ului.</li>
<li>Asteapta cel putin <b>30 de secunde</b>, ca router-ul sa se reseteze de tot.</li>
<li>Baga cablul la loc si asteapta sa se aprinda toate LED-urile (Internet, WAN, Wi-Fi).</li>
<li>Incearca din nou sa te conectezi.</li>
</ol>
<p class="pg-note">Pe <b>Wi-Fi</b> pierzi pachete si ping-ul sare. Daca poti, leaga calculatorul cu cablu de retea direct in router: FiveM simte asta mai tare decat alte jocuri.</p>
</section>
<section class="pg-fix" id="pas-3">
<div class="pg-head"><div class="pg-num">3</div><div>
<h3>Actualizeaza driverele, mai ales la placa video</h3>
<p class="pg-why">Un driver video vechi da crash, FPS mic, ecran negru, artefacte si erori ca „DXGI_ERROR_DEVICE_HUNG” sau „Out of GPU memory”. Motorul jocului (RAGE) e foarte sensibil la versiunea driverului.</p>
</div></div>
<p class="pg-label">Ce faci, dupa placa video</p>
<div class="pg-vendors">
<div class="pg-vendor">
<h4>NVIDIA</h4>
<ol class="pg-do">
<li>Descarca <a href="https://www.nvidia.com/en-us/software/nvidia-app/" target="_blank" rel="noopener">NVIDIA App</a> (sau GeForce Experience).</li>
<li>Mergi la <b>Drivers</b> si apasa <b>Check for updates</b>.</li>
<li>Alege <b>Download</b>, apoi <b>Express Installation</b>.</li>
<li>Reporneste calculatorul.</li>
</ol>
</div>
<div class="pg-vendor">
<h4>AMD</h4>
<ol class="pg-do">
<li>Descarca <a href="https://www.amd.com/en/support" target="_blank" rel="noopener">AMD Software: Adrenalin Edition</a>.</li>
<li>Deschide <b>Home</b> sau <b>Drivers &amp; Software</b>.</li>
<li>Apasa <b>Check for Updates</b> si instaleaza versiunea recomandata, nu pe cea „Optional”.</li>
<li>Reporneste calculatorul.</li>
</ol>
</div>
<div class="pg-vendor">
<h4>Intel (placa integrata)</h4>
<ol class="pg-do">
<li>Descarca <a href="https://www.intel.com/content/www/us/en/support/detect.html" target="_blank" rel="noopener">Intel Driver &amp; Support Assistant</a>.</li>
<li>Lasa-l sa scaneze sistemul si instaleaza actualizarile recomandate.</li>
</ol>
</div>
</div>
<p class="pg-note">Problema ramane si dupa actualizare? Sterge driverul vechi de tot cu <b>DDU (Display Driver Uninstaller)</b> in Safe Mode, apoi instaleaza-l pe cel nou. Multe conflicte grafice vin din fisierele ramase de la driverul vechi.</p>
<p class="pg-note red">Nu uita de driverele de <b>chipset</b>, <b>retea</b> si <b>sunet</b>. Un driver de retea vechi (Realtek, Intel, Killer) da ping instabil si deconectari. Le gasesti pe site-ul producatorului placii de baza sau al laptopului.</p>
</section>
<section class="pg-fix" id="pas-4">
<div class="pg-head"><div class="pg-num">4</div><div>
<h3>Porneste Game Mode si pune FiveM pe placa video dedicata</h3>
<p class="pg-why">Ecran negru in joc, artefacte sau crash-uri repetate? Verifica daca ai Game Mode pornit si daca FiveM foloseste placa video dedicata, nu pe cea integrata.</p>
</div></div>
<p class="pg-label">Game Mode</p>
<ol class="pg-do">
<li>Apasa <b>Start → Settings → Gaming → Game Mode</b>.</li>
<li>Pune comutatorul pe <b>On</b>.</li>
</ol>
<p class="pg-label">Placa video pentru FiveM</p>
<ol class="pg-do">
<li>Apasa <b>Start → Settings → Gaming → Graphics</b>.</li>
<li>Apasa <b>Add an app</b> (sau <b>Browse</b> pe Windows mai nou) si alege <code>FiveM.exe</code>, daca nu e deja in lista.</li>
<li>Apasa pe FiveM (sau pe <b>Options</b>) si alege placa video dedicata (NVIDIA RTX/GTX sau AMD Radeon), nu pe cea integrata (Intel HD/Iris sau AMD Vega integrata).</li>
<li>Salveaza si reporneste FiveM.</li>
</ol>
<p class="pg-note">Pe laptopurile cu doua placi video, FiveM porneste implicit pe cea integrata: FPS mic si joc instabil. Setarea de mai sus il muta pe placa dedicata.</p>
</section>
<section class="pg-fix" id="pas-5">
<div class="pg-head"><div class="pg-num">5</div><div>
<h3>Sterge cache-ul FiveM</h3>
<p class="pg-why">Cache-ul stricat e cauza numarul 1 pentru crash la intrare, texturi lipsa si erori „failed to load resource”.</p>
</div></div>
<p class="pg-label">Ce faci</p>
<ol class="pg-do">
<li>Click dreapta pe iconita FiveM, apoi <b>Open File Location</b>.</li>
<li>Intra in <b>FiveM Application Data</b>, apoi in <b>data</b>.</li>
<li>Sterge folderele:
<ul class="pg-files"><li><code>cache</code></li><li><code>server-cache</code></li><li><code>server-cache-priv</code></li></ul>
</li>
<li>Deschide FiveM si conecteaza-te. Prima intrare dureaza mai mult, pentru ca jocul descarca totul din nou.</li>
</ol>
<p class="pg-src">Tutorial video: <a href="https://www.youtube.com/watch?v=ROzbOEc7lak" target="_blank" rel="noopener">youtube.com/watch?v=ROzbOEc7lak</a></p>
<figure class="pg-shot">
<a href="/bg/cache.gif" target="_blank" rel="noopener"><img src="/bg/cache.gif" alt="Stergerea folderelor cache, server-cache si server-cache-priv din FiveM Application Data" width="1920" height="1080" loading="lazy"></a>
<figcaption>Folderele de sters. Apasa pe imagine pentru marime completa.</figcaption>
</figure>
</section>
<section class="pg-fix" id="pas-6">
<div class="pg-head"><div class="pg-num">6</div><div>
<h3>Reseteaza setarile de retea (script)</h3>
<p class="pg-why">Scriptul nostru <code>.bat</code> aduce setarile de retea ale Windows inapoi la valorile implicite. Ajuta cand ping-ul si deconectarile raman si dupa restartul router-ului.</p>
</div></div>
<p class="pg-label">Ce faci</p>
<ol class="pg-do">
<li>Descarca scriptul: <a href="https://jiraeg-j7wl0gw55c3cwjox.fsn1.your-objectstorage.com/cdn/rezolvare_optimizari_net.bat" target="_blank" rel="noopener">rezolvare_optimizari_net.bat</a>.</li>
<li>Click dreapta pe fisier, apoi <b>Run as administrator</b>. Fara drepturi de administrator scriptul nu merge.</li>
<li>Confirma cu <kbd>Y</kbd> si nu inchide fereastra neagra pana nu termina.</li>
<li>La final apare un mesaj. Cand apesi <b>OK</b>, calculatorul se reporneste singur, asa ca salveaza-ti inainte ce ai deschis.</li>
</ol>
<p class="pg-note red"><b>Ai IP sau DNS setate de mana?</b> Scriptul le poate sterge. Noteaza-le inainte, ca sa le pui la loc dupa restart.</p>
<p class="pg-note">Scriptul face o copie a setarilor vechi pe Desktop, intr-un folder <code>network_defaults_backup_...</code>. Daca Windows Defender sau antivirusul il blocheaza, e o alarma falsa: foloseste comenzi ca <code>netsh</code> si <code>ipconfig</code>, pe care antivirusurile le marcheaza des. Ruleaza-l doar daca l-ai luat de la linkul de mai sus.</p>
<p class="pg-src">Sursa scriptului: <a href="https://docs.illusioncloud.biz/books/faq/page/reset-your-windows-tcp-settings-recommended-for-illusioncloud-ddos-filtered-game-servers" target="_blank" rel="noopener">docs.illusioncloud.biz</a></p>
</section>
<section class="pg-fix" id="pas-7">
<div class="pg-head"><div class="pg-num">7</div><div>
<h3>Verifica fisierele GTA V</h3>
<p class="pg-why">Daca lipsesc fisiere din GTA V sau sunt stricate, FiveM da crash sau arata erori „Game Storage” la pornire.</p>
</div></div>
<p class="pg-label">Ce faci in Steam</p>
<ol class="pg-do">
<li>Deschide <b>Steam</b>, mergi in <b>Library</b> si cauta <b>Grand Theft Auto V</b>.</li>
<li>Click dreapta pe joc, apoi <b>Properties</b>.</li>
<li>Deschide <b>Installed Files</b> (pe versiunile vechi, <b>Local Files</b>).</li>
<li>Apasa <b>Verify integrity of game files</b>.</li>
<li>Asteapta intre <b>15 si 60 de minute</b>, dupa viteza HDD-ului sau SSD-ului. Steam descarca singur fisierele stricate.</li>
</ol>
<p class="pg-note">Pe <b>Rockstar Launcher</b> sau <b>Epic Games</b> cauta optiunea <b>Verify</b> sau <b>Repair</b> in setarile jocului.</p>
</section>
<section class="pg-fix" id="pas-8">
<div class="pg-head"><div class="pg-num">8</div><div>
<h3>Reinstaleaza FiveM</h3>
<p class="pg-why">Ultima solutie, daca pasii de mai sus nu au rezolvat. Reinstalarea scapa de fisierele stricate ale aplicatiei, de setarile gresite si de actualizarile esuate.</p>
</div></div>
<p class="pg-label">Ce faci</p>
<ol class="pg-do">
<li>Inchide complet FiveM.</li>
<li>Dezinstaleaza FiveM din <b>Apps &amp; Features</b> (Windows) sau cu dezinstalatorul din folderul lui.</li>
<li>Apasa <kbd>Win + R</kbd>, scrie <code>%localappdata%</code>, apasa Enter si sterge folderul <code>FiveM</code>.</li>
<li>Sterge si folderul de instalare, daca a ramas (de obicei pe Desktop sau in Documents).</li>
<li>Descarca FiveM din nou de pe <a href="https://fivem.net" target="_blank" rel="noopener">fivem.net</a>, instaleaza-l si conecteaza-te.</li>
</ol>
<p class="pg-note"><b>Nu pierzi nimic de pe server.</b> Personajul si tot ce ai sunt salvate la noi pe server, nu pe calculatorul tau. Reinstalarea schimba doar aplicatia FiveM.</p>
</section>
<section class="pg-fix" id="pas-9">
<div class="pg-head"><div class="pg-num">9</div><div>
<h3>Scoate modurile grafice</h3>
<p class="pg-why">ReShade, NaturalVision, QuantV si alte moduri grafice dau des crash si FPS mic in FiveM. Multe modifica fisierele jocului si intra in conflict cu anti-cheat-ul serverului.</p>
</div></div>
<p class="pg-label">Ce faci</p>
<ol class="pg-do">
<li>Deschide folderul GTA V (de obicei <code>C:\Program Files\Rockstar Games\Grand Theft Auto V</code> sau din Steam).</li>
<li>Sterge, daca le gasesti:
<ul class="pg-files"><li><code>dxgi.dll</code></li><li><code>d3d11.dll</code></li><li><code>d3d9.dll</code></li><li><code>ReShade.ini</code></li><li><code>reshade-shaders</code></li><li><code>ReShade</code></li><li><code>NVE</code></li><li><code>QuantV</code></li><li><code>NaturalVision</code></li></ul>
</li>
<li>Daca ai instalat modul cu un installer, foloseste optiunea <b>Uninstall</b> din el.</li>
<li>La final, verifica fisierele jocului (<a href="#pas-7">pasul 7</a>), ca sa pui la loc fisierele originale.</li>
</ol>
<p class="pg-note red">Pe serverul nostru, mai bine joci fara moduri grafice. Pentru o grafica mai buna, foloseste <a href="/general/setarigrafice">setarile grafice recomandate</a> din wiki.</p>
</section>
</div>
<section class="pg-help">
<h2>Tot nu merge?</h2>
<p>Daca ai trecut prin toti pasii si problema ramane, deschide un tichet pe <a href="https://discord.gg/elitegamers-ro-351058903271735306" target="_blank" rel="noopener">Discord</a> si scrie:</p>
<ol class="pg-do">
<li>Ce pasi ai incercat deja.</li>
<li>Ce eroare primesti, de preferat cu o captura de ecran.</li>
<li>Ce calculator ai: procesor, placa video, RAM si versiunea de Windows.</li>
</ol>
<p class="pg-src">Cu cat dai mai multe detalii, cu atat te ajutam mai repede.</p>
</section>
</div>
