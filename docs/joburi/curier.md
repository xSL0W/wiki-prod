---
outline: false
---

<style>
.cr {
  --cr-night: #15110d;
  --cr-box: #201912;
  --cr-edge: #3b2f22;
  --cr-kraft: #c08f58;
  --cr-kraft-deep: #8a6236;
  --cr-paper: #f4eee2;
  --cr-ink: #1c1712;
  --cr-text: #efe6d7;
  --cr-mute: #b8a993;
  --cr-tape: #e9c45c;
  --cr-stamp: #c8412c;
  max-width: 920px;
  margin: 0 auto;
  color: var(--cr-text);
  font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.cr *, .cr *::before, .cr *::after { box-sizing: border-box; }
.cr p, .cr li { line-height: 1.6; color: var(--cr-text); margin: 0; }
.cr ul, .cr ol { list-style: none; padding: 0; margin: 0; }
.cr b { color: #fff; font-weight: 650; }
.cr code { white-space: normal; }

/* hero: a cardboard box with a shipping label on it */
.cr-hero {
  position: relative;
  border-radius: 18px;
  padding: clamp(1rem, 4vw, 2.25rem);
  background:
    linear-gradient(90deg, transparent 47%, rgba(0, 0, 0, 0.12) 47% 53%, transparent 53%),
    linear-gradient(160deg, var(--cr-kraft) 0%, var(--cr-kraft-deep) 100%);
  overflow: hidden;
}
.cr-label {
  position: relative;
  max-width: 640px;
  margin: 0 auto;
  background: var(--cr-paper);
  color: var(--cr-ink);
  border-radius: 6px;
  box-shadow: 0 14px 30px rgba(0, 0, 0, 0.35);
  transform: rotate(-1.2deg);
}
.cr-label::before {
  content: '';
  position: absolute;
  top: -14px; left: 50%;
  width: 120px; height: 28px;
  transform: translateX(-50%) rotate(2deg);
  background: rgba(233, 196, 92, 0.85);
}
.cr-label-top {
  display: flex; justify-content: space-between; align-items: center; gap: 0.75rem;
  padding: 0.7rem 1.1rem;
  border-bottom: 2px solid var(--cr-ink);
  font: 700 0.78rem/1.2 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}
.cr-label-body { padding: 1rem 1.1rem 1.1rem; }
.cr-hero h1 {
  margin: 0 0 0.5rem;
  border: 0;
  padding: 0;
  font-size: clamp(2rem, 7vw, 3.3rem);
  line-height: 1.05;
  font-weight: 850;
  letter-spacing: -0.03em;
  color: var(--cr-ink);
}
.cr-hrs {
  display: inline-block;
  font-size: 0.55em;
  vertical-align: middle;
  padding: 0.1em 0.45em;
  border: 3px solid var(--cr-ink);
  border-radius: 8px;
  letter-spacing: 0;
}
.cr-label-body p { color: #3d342a; max-width: 46ch; }
.cr .cr-fields {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 0;
  margin-top: 1rem;
  border-top: 2px solid var(--cr-ink);
}
.cr-fields li { padding: 0.55rem 0.7rem 0.55rem 0; border-bottom: 1px dashed #9c8f7d; color: var(--cr-ink); }
.cr-fields small {
  display: block;
  font: 700 0.68rem/1.2 ui-monospace, Menlo, Consolas, monospace;
  letter-spacing: 0.14em;
  color: #6f6252;
}
.cr-code { display: block; width: 100%; height: 54px; margin-top: 1rem; }
.cr-code rect { fill: var(--cr-ink); }
.cr-stamp {
  position: absolute;
  right: 1rem; top: 3.2rem;
  padding: 0.2rem 0.6rem;
  border: 3px solid var(--cr-stamp);
  border-radius: 6px;
  color: var(--cr-stamp);
  font: 800 1rem/1 ui-monospace, Menlo, Consolas, monospace;
  letter-spacing: 0.18em;
  transform: rotate(12deg);
  opacity: 0.85;
}
@media (max-width: 520px) { .cr-stamp { top: auto; bottom: 5.4rem; } }

/* sections */
.cr h2 {
  margin: 3rem 0 1rem;
  border: 0;
  padding: 0;
  font-size: 1.5rem;
  font-weight: 750;
  letter-spacing: -0.015em;
  color: #fff;
}
.cr h2 span {
  display: inline-block;
  margin-right: 0.5rem;
  font: 700 0.8rem/1 ui-monospace, Menlo, Consolas, monospace;
  color: var(--cr-tape);
  vertical-align: middle;
}
.cr-lead { max-width: 62ch; }
.cr kbd {
  font: inherit; font-size: 0.85em; font-weight: 800; color: var(--cr-ink); background: var(--cr-tape);
  border-radius: 6px; padding: 0.05rem 0.45rem;
}

/* the shift as a parcel tracking history */
.cr-track { position: relative; }
.cr-track li {
  position: relative;
  display: grid;
  grid-template-columns: 2.6rem 1fr;
  gap: 0.9rem;
  padding-bottom: 1.4rem;
}
.cr-track li:last-child { padding-bottom: 0; }
.cr-track li::after {
  content: '';
  position: absolute;
  left: calc(1.3rem - 1px); top: 2.6rem; bottom: 0.2rem;
  width: 2px;
  background: repeating-linear-gradient(to bottom, var(--cr-edge) 0 5px, transparent 5px 10px);
}
.cr-track li:last-child::after { display: none; }
.cr-pin {
  width: 2.6rem; height: 2.6rem;
  display: grid; place-items: center;
  border-radius: 10px;
  background: var(--cr-box);
  border: 2px solid var(--cr-kraft);
}
.cr-pin svg { width: 1.3rem; height: 1.3rem; fill: none; stroke: var(--cr-kraft); stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.cr-track li.now .cr-pin { background: var(--cr-kraft); }
.cr-track li.now .cr-pin svg { stroke: var(--cr-ink); }
.cr-track li.now .cr-pin { animation: cr-ping 2.2s ease-out infinite; }
@keyframes cr-ping {
  0% { box-shadow: 0 0 0 0 rgba(192, 143, 88, 0.55); }
  70% { box-shadow: 0 0 0 12px rgba(192, 143, 88, 0); }
  100% { box-shadow: 0 0 0 0 rgba(192, 143, 88, 0); }
}
@media (prefers-reduced-motion: reduce) {
  .cr-track li.now .cr-pin { animation: none; }
}
.cr-status {
  display: block;
  font: 700 0.72rem/1.4 ui-monospace, Menlo, Consolas, monospace;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--cr-tape);
}
.cr-track p { color: var(--cr-mute); }
.cr-track strong { color: #fff; }

/* solo vs team: two parcels */
.cr-crew { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; }
.cr-parcel {
  position: relative;
  background: var(--cr-box);
  border: 1px solid var(--cr-edge);
  border-radius: 14px;
  padding: 1.5rem 1.3rem 1.25rem;
}
.cr-parcel::before {
  content: '';
  position: absolute; top: 0; left: 1.3rem;
  width: 3.5rem; height: 6px;
  border-radius: 0 0 4px 4px;
  background: var(--cr-kraft);
}
.cr-parcel.team { border-color: var(--cr-kraft); }
.cr-parcel.team::before { background: var(--cr-tape); width: 7rem; }
.cr-parcel h3 { margin: 0 0 0.5rem; border: 0; padding: 0; font-size: 1.15rem; color: #fff; }
.cr-parcel p { color: var(--cr-mute); }

/* tips as handling instructions */
.cr-care { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 0.75rem; }
.cr-care li {
  display: grid;
  grid-template-columns: 2.4rem 1fr;
  gap: 0.75rem;
  align-items: start;
  padding: 0.9rem 1rem;
  border: 1px dashed var(--cr-edge);
  border-radius: 12px;
}
.cr-care svg { width: 2.4rem; height: 2.4rem; fill: none; stroke: var(--cr-text); stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.cr-care p { color: var(--cr-mute); font-size: 0.95rem; }

.cr a:focus-visible { outline: 3px solid var(--cr-tape); outline-offset: 2px; }
</style>

<div class="cr">

<section class="cr-hero">
<div class="cr-label">
<div class="cr-label-top"><span>Curierat Los Santos</span><span>Job public</span></div>
<div class="cr-label-body">
<h1>Curier <span class="cr-hrs">- 0h</span></h1>
<p>Incarci coletele in duba, le duci la clienti prin tot orasul si te intorci dupa altele. Se poate face singur sau cu un prieten.</p>
<ul class="cr-fields">
<li><small>DE LA</small>Depozitul din port</li>
<li><small>CATRE</small>Clienti din tot orasul</li>
<li><small>VEHICUL</small>Duba alba a jobului</li>
<li><small>ECHIPA</small>Singur sau in doi</li>
</ul>
<svg class="cr-code" viewBox="0 0 300 54" preserveAspectRatio="none" aria-hidden="true">
<rect x="0" y="0" width="4" height="54"/><rect x="7" y="0" width="2" height="54"/><rect x="12" y="0" width="6" height="54"/><rect x="21" y="0" width="2" height="54"/><rect x="26" y="0" width="3" height="54"/><rect x="33" y="0" width="7" height="54"/><rect x="43" y="0" width="2" height="54"/><rect x="48" y="0" width="4" height="54"/><rect x="55" y="0" width="2" height="54"/><rect x="60" y="0" width="5" height="54"/><rect x="69" y="0" width="2" height="54"/><rect x="74" y="0" width="3" height="54"/><rect x="80" y="0" width="6" height="54"/><rect x="89" y="0" width="2" height="54"/><rect x="94" y="0" width="4" height="54"/><rect x="101" y="0" width="2" height="54"/><rect x="106" y="0" width="7" height="54"/><rect x="116" y="0" width="3" height="54"/><rect x="122" y="0" width="2" height="54"/><rect x="127" y="0" width="5" height="54"/><rect x="135" y="0" width="2" height="54"/><rect x="140" y="0" width="4" height="54"/><rect x="148" y="0" width="6" height="54"/><rect x="157" y="0" width="2" height="54"/><rect x="162" y="0" width="3" height="54"/><rect x="168" y="0" width="2" height="54"/><rect x="173" y="0" width="7" height="54"/><rect x="183" y="0" width="2" height="54"/><rect x="188" y="0" width="4" height="54"/><rect x="195" y="0" width="3" height="54"/><rect x="202" y="0" width="5" height="54"/><rect x="210" y="0" width="2" height="54"/><rect x="215" y="0" width="6" height="54"/><rect x="224" y="0" width="2" height="54"/><rect x="229" y="0" width="3" height="54"/><rect x="236" y="0" width="4" height="54"/><rect x="243" y="0" width="2" height="54"/><rect x="248" y="0" width="7" height="54"/><rect x="258" y="0" width="2" height="54"/><rect x="263" y="0" width="5" height="54"/><rect x="271" y="0" width="2" height="54"/><rect x="276" y="0" width="3" height="54"/><rect x="282" y="0" width="6" height="54"/><rect x="291" y="0" width="2" height="54"/><rect x="296" y="0" width="4" height="54"/>
</svg>
</div>
<div class="cr-stamp" aria-hidden="true">FRAGIL</div>
</div>
</section>

<h2><span>01</span>Cum incep?</h2>
<p class="cr-lead">Angajeaza-te ca <b>Curier</b> la Primarie (<code>Telefon → Harti → Locatii importante → Primarie</code>). Nu ai nevoie de ore jucate. Apoi mergi la <b>depozitul de curierat din port</b>, in sudul orasului, si vorbeste cu <b>seful de curierat</b>. Locul il gasesti si pe harta de la Primarie. Te poti angaja si direct de la el.</p>

<h2><span>02</span>Traseul unui colet</h2>
<ol class="cr-track">
<li><div class="cr-pin"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></div><div><span class="cr-status">Tura pornita</span><p>La seful de curierat alege <strong>Incepe tura</strong>. Liderul primeste duba alba a jobului, direct la volan.</p></div></li>
<li><div class="cr-pin"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 8l9-5 9 5v8l-9 5-9-5z"/><path d="M3 8l9 5 9-5M12 13v8"/></svg></div><div><span class="cr-status">Preluat la depozit</span><p>Mergi la markerul verde din depozit si apasa <kbd>E</kbd> ca sa ridici o cutie. Cari o singura cutie odata.</p></div></li>
<li><div class="cr-pin"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M2 7h12v10H2zM14 10h4l3 3v4h-7z"/><circle cx="6" cy="18" r="1.6"/><circle cx="17" cy="18" r="1.6"/></svg></div><div><span class="cr-status">Incarcat in duba</span><p>Deschide portbagajul dubei si muta cutia din inventar in portbagaj. Urmatoarea cutie te asteapta in alt loc din depozit, iar notificarea iti arata cate ai incarcat.</p></div></li>
<li class="now"><div class="cr-pin"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/></svg></div><div><span class="cr-status">In curs de livrare</span><p>Dupa ultima cutie, GPS-ul iti arata prima adresa. Coboara din duba, ia o cutie din portbagaj si apasa <kbd>E</kbd> la client ca sa livrezi coletul.</p></div></li>
<li><div class="cr-pin"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12l5 5L20 7"/></svg></div><div><span class="cr-status">Livrat</span><p>Plata intra in contul din banca dupa fiecare colet, apoi GPS-ul te duce la urmatorul client.</p></div></li>
<li><div class="cr-pin"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 12H5M11 6l-6 6 6 6"/></svg></div><div><span class="cr-status">Retur la depozit</span><p>Cand duba s-a golit, te intorci la depozit si incarci din nou. Tura se termina cand alegi <strong>Termina tura</strong> la sef.</p></div></li>
</ol>

<h2><span>03</span>Singur sau in echipa</h2>
<div class="cr-crew">
<div class="cr-parcel">
<h3>Singur</h3>
<p>Incarci, conduci si livrezi tu. Ritmul il alegi tu, iar plata e toata a ta.</p>
</div>
<div class="cr-parcel team">
<h3>Cu un prieten</h3>
<p>Formati echipa din <b>Meniu echipa</b>, la seful de curierat. Amandoi trebuie sa fiti curieri. Liderul porneste tura si primeste duba, amandoi puteti incarca si livra, iar <b>fiecare primeste plata intreaga</b> la fiecare colet.</p>
</div>
</div>

<h2><span>04</span>Instructiuni de manipulare</h2>
<ul class="cr-care">
<li><svg viewBox="0 0 40 40" aria-hidden="true"><rect x="6" y="14" width="22" height="14" rx="2"/><path d="M28 18h4l3 4v6h-7"/><path d="M14 8l4 4 4-4"/></svg><p><b>Coboara din duba.</b> Coletul se preda doar pe jos, cu cutia in mana.</p></li>
<li><svg viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="20" r="13"/><path d="M20 12v8l5 4"/></svg><p><b>Fara graba.</b> Intre doua livrari trebuie sa treaca un timp minim.</p></li>
<li><svg viewBox="0 0 40 40" aria-hidden="true"><path d="M8 14l12-6 12 6v12l-12 6-12-6z"/><path d="M20 20v12M8 14l12 6 12-6"/></svg><p><b>Fa loc in inventar.</b> Fara loc liber nu poti ridica nicio cutie.</p></li>
<li><svg viewBox="0 0 40 40" aria-hidden="true"><path d="M20 6l15 26H5z"/><path d="M20 16v7M20 27v.5"/></svg><p><b>Nu iesi in mijlocul turei.</b> Daca un membru iese de pe server sau renunta la job, tura se opreste pentru toata echipa, duba dispare si cutiile se pierd.</p></li>
</ul>

</div>
