---
outline: false
---

<style>
.skc {
  --ink: #0b0b0d;
  --panel: #17171a;
  --panel2: #1f1f23;
  --line: #2f2f36;
  --text: #f4f4f5;
  --mute: #a1a1aa;
  --red: #ef4444;
  --red-deep: #b91c1c;
  --red-soft: rgba(239, 68, 68, 0.14);
  max-width: 1100px;
  margin: 0 auto;
  color: var(--text);
  font-family: Inter, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.skc *, .skc *::before, .skc *::after { box-sizing: border-box; }
.skc p, .skc li { line-height: 1.55; color: var(--text); margin: 0; }
.skc ul, .skc ol { list-style: none; padding: 0; margin: 0; }
.skc li + li { margin-top: 0; }
.skc b { color: #fff; font-weight: 650; }
.skc a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.skc a:hover { color: #fecaca; }
.skc a:focus-visible { outline: 3px solid var(--red); outline-offset: 3px; border-radius: 6px; }
/* ---------- header ---------- */
.skc .skc-hero {
  position: relative; overflow: hidden;
  background: radial-gradient(80% 140% at 100% 0%, rgba(168, 85, 247, 0.16), transparent 55%),
              radial-gradient(110% 130% at 0% 100%, rgba(185, 28, 28, 0.28), var(--ink) 62%);
  border: 1px solid var(--line); border-radius: 22px;
  padding: clamp(1.1rem, 4vw, 2.1rem);
}
.skc .skc-kicker { font-size: 0.78rem; font-weight: 700; letter-spacing: 0.16em; text-transform: uppercase; color: var(--red); margin-bottom: 0.5rem; }
.skc .skc-hero h1 {
  margin: 0 0 0.6rem; border: 0; padding: 0;
  font-size: clamp(1.9rem, 6vw, 3rem); line-height: 1.05; font-weight: 800; letter-spacing: -0.03em; color: #fff;
}
.skc .skc-lede { max-width: 62ch; color: var(--mute); font-size: 1.02rem; }
.skc .skc-stats { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1rem; }
.skc .skc-stats li { background: rgba(23, 23, 26, 0.85); border: 1px solid var(--line); border-radius: 12px; padding: 0.45rem 0.8rem; color: var(--mute); font-size: 0.85rem; }
.skc .skc-stats b { color: #fff; font-size: 1.1rem; font-weight: 800; margin-right: 0.25rem; font-variant-numeric: tabular-nums; }
/* ---------- filters (radio + label, no script) ---------- */
.skc .skc-radio { position: absolute; width: 1px; height: 1px; opacity: 0; pointer-events: none; }
.skc .skc-bar {
  margin-top: 1.1rem; display: grid; gap: 0.65rem;
  background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 0.85rem;
}
.skc .skc-group { display: flex; flex-wrap: wrap; align-items: center; gap: 0.4rem; }
.skc .skc-glabel { flex: 0 0 4.2rem; font-size: 0.72rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: var(--mute); }
.skc .skc-chip {
  display: inline-flex; align-items: center; gap: 0.4rem; cursor: pointer; user-select: none;
  font-size: 0.82rem; font-weight: 650; color: #d4d4d8;
  background: var(--panel2); border: 1px solid var(--line); border-radius: 999px; padding: 0.28rem 0.75rem;
  transition: border-color 0.15s, background 0.15s, color 0.15s;
}
.skc .skc-chip:hover { border-color: #52525b; color: #fff; }
.skc .skc-chip i { width: 8px; height: 8px; border-radius: 50%; background: var(--c); flex: none; }
.skc .skc-hint { font-size: 0.8rem; color: var(--mute); }
/*@@FILTERCSS@@*/
/* ---------- weapon index ---------- */
.skc .skc-nav { display: flex; flex-wrap: wrap; gap: 0.35rem; margin-top: 0.8rem; }
.skc .skc-jump {
  font-size: 0.78rem; font-weight: 600; color: var(--mute); text-decoration: none;
  border: 1px dashed var(--line); border-radius: 8px; padding: 0.18rem 0.55rem;
}
.skc .skc-jump:hover { color: #fff; border-color: var(--red); }
/* ---------- groups ---------- */
.skc .skc-h2 {
  display: flex; align-items: center; gap: 0.65rem;
  margin: 2.6rem 0 0.9rem; border: 0; padding: 0;
  font-size: 1.45rem; font-weight: 750; letter-spacing: -0.015em; line-height: 1.25; color: #fff;
}
.skc .skc-h2::before {
  content: ''; flex: none; width: 0.6rem; height: 0.6rem; border-radius: 2px; background: var(--red);
  transform: rotate(45deg); box-shadow: 0 0 0 4px var(--red-soft);
}
.skc .skc-w {
  background: var(--panel); border: 1px solid var(--line); border-radius: 18px;
  padding: 0.8rem; margin-top: 0.9rem; scroll-margin-top: 90px;
}
.skc .skc-whead { display: flex; align-items: center; gap: 0.8rem; padding: 0.1rem 0.2rem 0.7rem; }
.skc .skc-wimg { width: 72px; height: 72px; object-fit: contain; flex: none; background: var(--panel2); border-radius: 12px; }
.skc .skc-wtitle { min-width: 0; }
.skc .skc-h3 { margin: 0; border: 0; padding: 0; font-size: 1.12rem; font-weight: 750; color: #fff; line-height: 1.2; }
.skc .skc-count { display: block; font-size: 0.8rem; color: var(--mute); margin-top: 0.15rem; }
.skc .skc-dots { margin-left: auto; display: flex; gap: 0.25rem; flex-wrap: wrap; justify-content: flex-end; max-width: 40%; }
.skc .skc-dots i { width: 10px; height: 10px; border-radius: 3px; background: var(--c); }
#skc-t-all:not(:checked) ~ .skc-list .skc-count { visibility: hidden; }
#skc-t-all:not(:checked) ~ .skc-list .skc-none { display: none; }
/* ---------- cards ---------- */
.skc .skc-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(min(100%, 136px), 1fr)); gap: 0.55rem; }
.skc .skc-card {
  position: relative; display: flex; flex-direction: column; gap: 0.2rem;
  background: linear-gradient(180deg, #232328, #18181b 70%);
  border: 1px solid var(--line); border-radius: 14px; padding: 0.45rem 0.55rem 0.6rem;
  transition: transform 0.18s ease, border-color 0.18s ease;
}
.skc .skc-card::before {
  content: ''; position: absolute; left: 12px; right: 12px; top: 0; height: 3px; border-radius: 0 0 3px 3px; background: var(--c);
}
.skc .skc-card:hover { transform: translateY(-3px); border-color: var(--c); }
.skc .skc-img { display: block; width: 100%; height: auto; aspect-ratio: 3 / 2; object-fit: cover; margin: 0; }
.skc .skc-name { font-size: 0.9rem; font-weight: 700; color: #fff; line-height: 1.25; }
.skc .skc-badge {
  align-self: flex-start; font-size: 0.66rem; font-weight: 800; letter-spacing: 0.08em; text-transform: uppercase;
  color: var(--c); border: 1px solid var(--c); border-radius: 999px; padding: 0.05rem 0.5rem;
  letter-spacing: 0.04em; white-space: nowrap; max-width: 100%; overflow: hidden; text-overflow: ellipsis;
}
.skc .skc-how { font-size: 0.74rem; color: var(--mute); line-height: 1.3; }
.skc .skc-none { margin-top: 0.9rem; font-size: 0.85rem; color: var(--mute); }
.skc .skc-foot { margin-top: 2.4rem; font-size: 0.85rem; color: var(--mute); border-top: 1px solid var(--line); padding-top: 1rem; }
@media (max-width: 520px) {
  .skc .skc-glabel { flex-basis: 100%; }
  .skc .skc-wimg { width: 56px; height: 56px; }
  .skc .skc-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (prefers-reduced-motion: reduce) {
  .skc .skc-card, .skc .skc-chip { transition: none; }
  .skc .skc-card:hover { transform: none; }
}
</style>

<div class="skc">
<header class="skc-hero"><p class="skc-kicker">Skin-uri arme</p><h1>Catalog skin-uri</h1><p class="skc-lede">Fiecare arma, cu skin-urile pe care i le poti pune. Alege un nivel sau un tip de arma ca sa vezi doar ce te intereseaza. Cum faci un skin, cum il deblochezi si cum il pui pe arma afli pe pagina <a href="./skin-uri-arme">Skin-uri arme</a>.</p><ul class="skc-stats"><li><b>@@WEAPONS@@</b>arme cu skin-uri</li><li><b>@@SKINS@@</b>skin-uri pe arme</li><li><b>9</b>niveluri</li></ul></header>
@@RADIOS@@<div class="skc-bar"><div class="skc-group"><span class="skc-glabel">Nivel</span>@@TIERS@@</div><div class="skc-group"><span class="skc-glabel">Arma</span>@@CATS@@</div></div><nav class="skc-nav" aria-label="Arme">@@NAV@@</nav><div class="skc-list">
@@BODY@@
</div>
<p class="skc-foot">Un skin facut pentru o arma merge doar pe acea arma. Deblocarea se plateste o singura data pentru fiecare skin pe fiecare arma. Lista se schimba cand apar skin-uri noi.</p>
</div>
