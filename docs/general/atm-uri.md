---
outline: false
---

<style>
.atm {
  --panel: #17171a;
  --line: #2f2f36;
  --text: #f4f4f5;
  --mute: #a1a1aa;
  --red: #ef4444;
  --red-deep: #b91c1c;
  --red-soft: rgba(239, 68, 68, 0.14);
  max-width: 900px;
  margin: 0 auto;
  color: var(--text);
  font-family: Inter, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.atm *, .atm *::before, .atm *::after { box-sizing: border-box; }
.atm p, .atm li { line-height: 1.6; color: var(--text); margin: 0; }
.atm ul, .atm ol { list-style: none; padding: 0; margin: 0; }
.atm li + li { margin-top: 0; }
.atm b { color: #fff; font-weight: 650; }
.atm a { color: #fff; text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.atm a:focus-visible { outline: 3px solid var(--red); outline-offset: 3px; border-radius: 6px; }
.atm kbd {
  font: inherit; font-size: 0.85em; font-weight: 700; color: #fff; background: var(--red-deep);
  border-radius: 6px; padding: 0.05rem 0.45rem; white-space: nowrap;
}
.atm code { font-size: 0.88em; color: #fecaca; background: #26262b; border-radius: 6px; padding: 0.05rem 0.35rem; }
.atm .atm-head { border-bottom: 1px solid var(--line); padding-bottom: 1.2rem; }
.atm .atm-kicker { font-size: 0.78rem; font-weight: 700; letter-spacing: 0.16em; text-transform: uppercase; color: var(--red); margin-bottom: 0.4rem; }
.atm .atm-head h1 { margin: 0 0 0.6rem; border: 0; padding: 0; font-size: clamp(2rem, 6vw, 3rem); line-height: 1.05; font-weight: 800; letter-spacing: -0.03em; color: #fff; }
.atm .atm-lede { color: var(--mute); max-width: 62ch; font-size: 1.05rem; }
.atm .atm-h2 {
  display: flex; align-items: center; gap: 0.65rem;
  margin: 2.4rem 0 0.9rem; border: 0; padding: 0;
  font-size: 1.35rem; font-weight: 750; letter-spacing: -0.015em; line-height: 1.25; color: #fff;
}
.atm .atm-h2::before {
  content: ''; flex: none; width: 0.6rem; height: 0.6rem; border-radius: 2px; background: var(--red);
  transform: rotate(45deg); box-shadow: 0 0 0 4px var(--red-soft);
}
.atm .atm-h3 { margin: 0 0 0.3rem; border: 0; padding: 0; font-size: 1.02rem; font-weight: 700; color: #fff; line-height: 1.3; }
.atm .atm-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 200px), 1fr)); gap: 0.75rem; }
.atm .atm-card { background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 1rem 1.15rem; }
.atm .atm-card p { color: var(--mute); font-size: 0.95rem; }
.atm .atm-card p + p { margin-top: 0.45rem; }
.atm .atm-list li { position: relative; padding-left: 1.2rem; color: var(--mute); font-size: 0.96rem; }
.atm .atm-list li + li { margin-top: 0.45rem; }
.atm .atm-list li::before { content: ''; position: absolute; left: 0.1rem; top: 0.62em; width: 0.42rem; height: 0.42rem; border-radius: 50%; background: var(--red); }
.atm .atm-list b { color: var(--text); }
</style>

<div class="atm">
<header class="atm-head">
<p class="atm-kicker">Sisteme generale</p>
<h1>ATM-uri</h1>
<p class="atm-lede">Peste 100 de bancomate in tot orasul. Nu ai nevoie de card sau PIN: te apropii, apesi <kbd>E</kbd> la bula <b>Bancomat</b> si lucrezi direct pe ecran.</p>
</header>

<h2 class="atm-h2" id="ce-poti-face">Ce poti face</h2>
<div class="atm-grid">
<div class="atm-card"><h3 class="atm-h3">Retragere</h3><p>Scoti bani din cont in numerar.</p></div>
<div class="atm-card"><h3 class="atm-h3">Depunere</h3><p>Pui numerar in cont. <b>Tot numerarul</b> completeaza suma cu toti banii cash.</p></div>
<div class="atm-card"><h3 class="atm-h3">Transfer</h3><p>Trimiti bani din cont dupa <b>ID-ul</b> jucatorului. Taxa de transfer o vezi pe ecran inainte sa confirmi, iar el primeste suma intreaga.</p></div>
<div class="atm-card"><h3 class="atm-h3">Extras cont</h3><p>Ultimele 25 de operatii din cont. Istoricul se pastreaza 14 zile.</p></div>
</div>

<h2 class="atm-h2" id="ecranul">Ecranul</h2>
<div class="atm-card">
<ul class="atm-list">
<li>Dai click cu mouse-ul pe butoanele de pe ecran.</li>
<li>Sumele si ID-ul le scrii si de la tastatura: <kbd>Enter</kbd> confirma, <kbd>Backspace</kbd> sterge.</li>
<li><kbd>ESC</kbd> te scoate de la bancomat.</li>
</ul>
</div>

<h2 class="atm-h2" id="bun-de-stiut">Bun de stiut</h2>
<div class="atm-card">
<ul class="atm-list">
<li><b>Telefon → Banca:</b> vezi soldul si istoricul si faci transferuri si fara bancomat.</li>
<li><b>Payday:</b> o data pe ora primesti in cont salariul de job, de factiune si de VIP. Tot atunci platesti impozitul pe vehicule.</li>
<li><b>Poprire:</b> daca nu ai bani de impozit, nu mai intri in garaj si nu mai cumperi din magazine pana platesti din <kbd>K</kbd> → <b>Jucator</b> → <b>Plateste taxe</b> sau cu <code>/paytaxes</code>.</li>
<li><b>Bancomat spart:</b> dupa un jaf, bancomatul nu mai merge o vreme. Foloseste altul.</li>
</ul>
</div>
</div>
