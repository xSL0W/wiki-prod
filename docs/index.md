---
layout: home
title: EliteGamers RP - Wiki
---

<script setup>
import SiteMap from './.vitepress/components/SiteMap.vue'
</script>

<style>
.hm {
  --ink: #09090b;
  --panel: #18181b;
  --panel-2: #1f1f23;
  --line: #2e2e33;
  --text: #f4f4f5;
  --mute: #a1a1aa;
  --red: #cc2b2b;
  --red-deep: #b91c1c;
  --red-soft: rgba(204, 43, 43, 0.14);
  max-width: 1152px;
  margin: 0 auto;
  padding: 2rem 24px 4rem;
  color: var(--text);
  font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.hm *, .hm *::before, .hm *::after { box-sizing: border-box; }
.hm p, .hm li { margin: 0; line-height: 1.6; color: var(--text); }
.hm ul { list-style: none; padding: 0; margin: 0; }
.hm li + li { margin-top: 0; }
.hm a { color: inherit; text-decoration: none; }
.hm a:focus-visible { outline: 3px solid var(--red); outline-offset: 3px; border-radius: 12px; }
.hm h1, .hm h2, .hm h3 { border: 0; padding: 0; margin: 0; letter-spacing: -0.02em; color: #fff; }

/* hero */
.hm .hm-hero {
  position: relative; overflow: hidden;
  display: grid; grid-template-columns: minmax(0, 1.4fr) minmax(0, 1fr); gap: 2rem; align-items: center;
  background: radial-gradient(120% 120% at 100% 0%, rgba(204, 43, 43, 0.28), transparent 55%), var(--ink);
  border: 1px solid var(--line); border-radius: 24px;
  padding: clamp(1.5rem, 5vw, 3.25rem);
}
.hm .hm-kicker { font: 700 0.75rem/1 ui-monospace, Menlo, Consolas, monospace; letter-spacing: 0.18em; text-transform: uppercase; color: var(--red); }
.hm .hm-hero h1 { margin-top: 0.8rem; font-size: clamp(1.7rem, 8vw, 4rem); line-height: 1.02; font-weight: 850; }
.hm .hm-hero h1 span { color: var(--red); }
.hm .hm-lede { margin-top: 1rem; max-width: 46ch; color: var(--mute); font-size: 1.08rem; }
.hm .hm-cta { display: flex; flex-wrap: wrap; gap: 0.7rem; margin-top: 1.6rem; }
.hm .hm-btn {
  display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.7rem 1.15rem; border-radius: 12px;
  font-weight: 700; border: 1px solid var(--line); background: var(--panel); color: #fff; transition: border-color 0.2s, transform 0.2s;
}
.hm .hm-btn:hover { border-color: var(--red); transform: translateY(-1px); }
.hm .hm-btn.primary { background: var(--red-deep); border-color: var(--red-deep); }
.hm .hm-btn.primary:hover { background: var(--red); }
.hm .hm-join {
  display: inline-flex; flex-wrap: wrap; align-items: center; gap: 0.6rem; max-width: 100%; margin-top: 1.2rem; padding: 0.45rem 0.8rem; border-radius: 999px;
  background: var(--panel); border: 1px dashed var(--line); color: var(--mute); font-size: 0.9rem;
}
.hm .hm-join code { color: #fff; background: none; padding: 0; font-size: 0.9rem; overflow-wrap: anywhere; }
.hm .hm-dot { width: 8px; height: 8px; border-radius: 50%; background: #22c55e; box-shadow: 0 0 0 4px rgba(34, 197, 94, 0.18); }
.hm .hm-logo { position: relative; display: grid; place-items: center; }
.hm .hm-logo::before {
  content: ''; position: absolute; width: 78%; aspect-ratio: 1; border-radius: 50%;
  background: radial-gradient(circle, rgba(204, 43, 43, 0.45), transparent 65%); filter: blur(6px);
}
.hm .hm-logo img { position: relative; width: min(100%, 320px); height: auto; animation: hm-float 6s ease-in-out infinite; }
@keyframes hm-float { 50% { transform: translateY(-10px); } }

/* sections */
.hm .hm-sec { margin-top: 3.5rem; }
.hm .hm-sec > h2 { font-size: clamp(1.4rem, 3vw, 1.8rem); font-weight: 800; }
.hm .hm-sec > p { margin-top: 0.4rem; color: var(--mute); }

/* quick start */
.hm .hm-quick { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 0.9rem; margin-top: 1.3rem; }
.hm .hm-card {
  position: relative; display: block; height: 100%; padding: 1.15rem 1.2rem 1.2rem 1.2rem;
  background: var(--panel); border: 1px solid var(--line); border-radius: 16px; transition: border-color 0.2s, transform 0.2s, background 0.2s;
}
.hm .hm-card:hover { border-color: var(--red); background: var(--panel-2); transform: translateY(-2px); }
.hm .hm-card svg { width: 26px; height: 26px; color: var(--red); }
.hm .hm-card h3 { margin-top: 0.7rem; font-size: 1.08rem; font-weight: 750; }
.hm .hm-card p { margin-top: 0.25rem; color: var(--mute); font-size: 0.93rem; }
.hm .hm-card .hm-go { position: absolute; top: 1.1rem; right: 1.1rem; color: var(--mute); transition: color 0.2s, transform 0.2s; }
.hm .hm-card:hover .hm-go { color: var(--red); transform: translateX(3px); }
.hm .hm-step { position: absolute; top: 1rem; right: 2.6rem; font: 700 0.7rem/1 ui-monospace, Menlo, monospace; color: var(--red); background: var(--red-soft); padding: 0.25rem 0.45rem; border-radius: 6px; }

/* explore */
.hm .hm-explore { display: grid; grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); gap: 0.7rem; margin-top: 1.3rem; }
.hm .hm-tile {
  display: flex; flex-direction: column; justify-content: flex-end; min-height: 120px; padding: 1rem;
  border-radius: 16px; border: 1px solid var(--line); transition: border-color 0.2s, transform 0.2s;
  background: linear-gradient(160deg, var(--tint, rgba(204, 43, 43, 0.18)), var(--panel) 60%);
}
.hm .hm-tile:hover { border-color: var(--red); transform: translateY(-2px); }
.hm .hm-tile b { color: #fff; font-size: 1.02rem; }
.hm .hm-tile span { color: var(--mute); font-size: 0.86rem; }

/* team */
.hm .hm-team { display: grid; grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: 0.9rem; margin-top: 1.3rem; }
.hm .hm-member { text-align: center; padding: 1.4rem 1rem 1.2rem; background: var(--panel); border: 1px solid var(--line); border-radius: 18px; }
.hm .hm-ava {
  position: relative; width: 84px; height: 84px; margin: 0 auto; border-radius: 50%; overflow: hidden;
  display: grid; place-items: center; background: linear-gradient(145deg, var(--red-deep), #3f0d0d);
  box-shadow: 0 0 0 3px var(--ink), 0 0 0 5px var(--line);
}
.hm .hm-ava span { font-size: 2.1rem; font-weight: 850; color: #fff; }
.hm .hm-ava img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; margin: 0; }
.hm .hm-member h3 { margin-top: 0.85rem; font-size: 1.1rem; font-weight: 800; }
.hm .hm-role { display: inline-block; margin-top: 0.35rem; padding: 0.15rem 0.6rem; border-radius: 999px; background: var(--red-soft); color: #ffb4b4; font-size: 0.78rem; font-weight: 700; }
.hm .hm-member p { margin-top: 0.6rem; color: var(--mute); font-size: 0.9rem; }

.hm .hm-mapnote { margin-top: 3.5rem; }

@media (max-width: 760px) {
  .hm { padding: 1.25rem 16px 3rem; }
  .hm .hm-hero { grid-template-columns: minmax(0, 1fr); padding: 1.4rem 1.2rem; }
  .hm .hm-logo { order: -1; }
  .hm .hm-logo img { width: 150px; }
}
@media (prefers-reduced-motion: reduce) {
  .hm .hm-logo img { animation: none; }
  .hm .hm-card, .hm .hm-tile, .hm .hm-btn { transition: none; }
}
</style>

<div class="hm">
<section class="hm-hero">
<div>
<p class="hm-kicker">Wiki oficial</p>
<h1>EliteGamers <span>Romania</span><br>Imersiv Roleplay</h1>
<p class="hm-lede">Tot ce ai nevoie ca sa intri pe server, sa iti gasesti un job si sa traiesti orasul: reguli, sisteme, joburi si raspunsuri la intrebarile de zi cu zi.</p>
<div class="hm-cta">
<a class="hm-btn primary" href="/zona-info/cum-intru-pe-server">Cum intru pe server</a>
<a class="hm-btn" href="/zona-info/regulament">Regulament</a>
<a class="hm-btn" href="https://discord.gg/elitegamers-ro-351058903271735306" target="_blank" rel="noopener">Discord</a>
</div>
<a class="hm-join" href="https://cfx.re/join/p9a86y" target="_blank" rel="noopener"><i class="hm-dot" aria-hidden="true"></i>Intra direct: <code>cfx.re/join/p9a86y</code></a>
</div>
<div class="hm-logo"><img src="/elitegamers.webp" alt="EliteGamers" width="320" height="320"></div>
</section>
<section class="hm-sec">
<h2>Primii pasi</h2>
<p>Esti nou? Ia-le in ordine si esti gata de oras.</p>
<div class="hm-quick">
<a class="hm-card" href="/zona-info/cum-intru-pe-server"><span class="hm-step">PAS 1</span><svg class="hm-go" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"/><path d="M10 17l5-5-5-5"/><path d="M15 12H3"/></svg><h3>Intra pe server</h3><p>Instalezi FiveM si te conectezi in cinci pasi.</p></a>
<a class="hm-card" href="/zona-info/regulament"><span class="hm-step">PAS 2</span><svg class="hm-go" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg><h3>Citeste regulamentul</h3><p>Ce ai voie si ce nu ai voie in roleplay.</p></a>
<a class="hm-card" href="/joburi/curier"><span class="hm-step">PAS 3</span><svg class="hm-go" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg><h3>Gaseste un job</h3><p>Joburile legale, de la 0 ore in sus.</p></a>
<a class="hm-card" href="/zona-info/faq"><svg class="hm-go" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M9.1 9a3 3 0 0 1 5.8 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg><h3>Intrebari si raspunsuri</h3><p>Raspunsuri scurte la ce se intreaba des.</p></a>
<a class="hm-card" href="/zona-info/probleme-generale"><svg class="hm-go" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.8-3.8a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9z"/></svg><h3>Probleme tehnice</h3><p>Crash, lag sau nu se incarca? Aici gasesti rezolvarea.</p></a>
</div>
</section>
<section class="hm-sec">
<h2>Exploreaza orasul</h2>
<div class="hm-explore">
<a class="hm-tile" href="/joburi/curier" style="--tint: rgba(34, 197, 94, 0.18)"><b>Joburi legale</b><span>Munca cinstita, platita</span></a>
<a class="hm-tile" href="/joburi/jafuriatm" style="--tint: rgba(204, 43, 43, 0.24)"><b>Jafuri si misiuni</b><span>De la ATM la banca</span></a>
<a class="hm-tile" href="/viata-ilegala/introducere" style="--tint: rgba(168, 85, 247, 0.2)"><b>Viata ilegala</b><span>Familii, mafii, teritorii</span></a>
<a class="hm-tile" href="/proprietati/despre-case" style="--tint: rgba(59, 130, 246, 0.2)"><b>Proprietati</b><span>Case si apartamente</span></a>
<a class="hm-tile" href="/general/garaje" style="--tint: rgba(234, 179, 8, 0.18)"><b>Sisteme</b><span>Garaje, telefon, tuning</span></a>
<a class="hm-tile" href="/zona-info/store" style="--tint: rgba(245, 158, 11, 0.2)"><b>Magazin</b><span>VIP si EG Coins</span></a>
</div>
</section>
<section class="hm-sec">
<h2>Echipa</h2>
<p>Oamenii care tin serverul in viata.</p>
<div class="hm-team">
<div class="hm-member"><div class="hm-ava"><span aria-hidden="true">Q</span><img src="/quo.jpg" alt="Quo" loading="lazy" onerror="this.remove()"></div><h3>Quo</h3><span class="hm-role">Fondator</span><p>Conduce echipa de staff si coordoneaza proiectele comunitatii.</p></div>
<div class="hm-member"><div class="hm-ava"><span aria-hidden="true">X</span><img src="https://cdn.discordapp.com/avatars/262600228719427584/cb935ab9648fedf2747866af9256ea85.png" alt="xSL0W" loading="lazy" onerror="this.remove()"></div><h3>xSL0W</h3><span class="hm-role">Developer si fondator</span><p>Raspunde de partea tehnica.</p></div>
<div class="hm-member"><div class="hm-ava"><span aria-hidden="true">S</span><img src="https://cdn.discordapp.com/avatars/295581149986553857/14ab973e2e0ad5cf4ecf5f55c0d8a94b.webp?size=256" alt="sNok3" loading="lazy" onerror="this.remove()"></div><h3>sNok3</h3><span class="hm-role">Developer</span><p>Raspunde de partea tehnica.</p></div>
<div class="hm-member"><div class="hm-ava"><span aria-hidden="true">C</span></div><h3>Crixus99</h3><span class="hm-role">Community Manager</span><p>Ajuta la gestionarea comunitatii si organizeaza activitatile.</p></div>
<div class="hm-member"><div class="hm-ava"><span aria-hidden="true">D</span></div><h3>dey</h3><span class="hm-role">Creator de asset-uri</span><p>Face asset-urile serverului si ajuta la dezvoltarea lui.</p></div>
</div>
</section>
<section class="hm-mapnote">
<SiteMap />
</section>
</div>
