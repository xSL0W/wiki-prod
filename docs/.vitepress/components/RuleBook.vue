<script setup>
/**
 * RuleBook: turns a markdown rules page into rule cards without touching its text.
 * On mount it groups every h3/h4 with the content under it into a card, splits "1.4 META GAMING [MG]"
 * into number / name / code badge ("Art. 1.1 ..." too) and turns ":::danger SANCTIUNE" / "Atentie!" blocks into penalty pills.
 */
import { onMounted } from 'vue'

/** Text of a heading without its "#" anchor */
const headingText = (h) => [...h.childNodes].filter((n) => !(n.classList && n.classList.contains('header-anchor'))).map((n) => n.textContent).join('').trim()

/** Rebuild "1.4 META GAMING [MG]" / "Art. 1.1 Limite de viteza" as number / name / code spans (same characters, anchor kept) */
function decorate(h) {
  const m = headingText(h).match(/^((?:Art\.\s*)?\d+(?:\.\d+)*)\.?\s+(.*?)(?:\s*\[([^\]]+)\])?$/)
  if (!m) return null
  const anchor = h.querySelector('.header-anchor')
  h.textContent = ''
  // the page outline (Cuprins) reads the heading text: keep the spaces and brackets, only hide them
  const hidden = (t) => { const i = document.createElement('i'); i.className = 'rb-hide'; i.textContent = t; return i }
  const num = document.createElement('span'); num.className = 'rb-num'; num.textContent = m[1]
  const name = document.createElement('span'); name.className = 'rb-name'; name.textContent = m[2]
  h.append(num, hidden(' '), name)
  if (m[3]) {
    const code = document.createElement('span'); code.className = 'rb-code'
    code.append(hidden(' ['), m[3], hidden(']'))
    h.append(code)
  }
  if (anchor) h.append(anchor)
  return m[3] || null
}

/** Penalty pills: one per "/"-separated sanction in a paragraph, one per "+"-separated part of a list item */
function pills(texts, sep) {
  const box = document.createElement('p')
  box.className = 'rb-pills'
  for (const text of texts) {
    for (const part of text.split(sep).map((x) => x.trim()).filter(Boolean)) {
      const pill = document.createElement('span'); pill.textContent = part
      box.append(pill)
    }
  }
  return box
}

/** ":::danger SANCTIUNE" (regulamente) and ":::danger Atentie!" (cod penal) blocks -> a pill strip */
function decorateSanction(block) {
  const title = block.querySelector('.custom-block-title')
  if (!title || !/sanc|aten/i.test(title.textContent)) return
  block.classList.add('rb-sanction')
  for (const p of block.querySelectorAll('p:not(.custom-block-title)')) {
    if (p.textContent.split('/').length < 2) continue
    p.replaceWith(pills([p.textContent], '/'))
  }
  for (const ul of block.querySelectorAll('ul')) {
    ul.replaceWith(pills([...ul.children].map((li) => li.textContent), ' + '))
  }
}

onMounted(() => {
  const root = document.querySelector('.vp-doc > div')
  if (!root) return
  let card = null
  let inChapter = false
  let seenH3 = false // an h4 is a sub-rule only under an h3; pages whose rules are h4 get full cards
  for (const el of [...root.children]) {
    const tag = el.tagName
    if (tag === 'H1') {
      card = null
      inChapter = true
      seenH3 = false
      el.classList.add('rb-chapter')
      continue
    }
    if (tag === 'H2' || tag === 'H3' || tag === 'H4') {
      card = document.createElement('section')
      if (tag === 'H3') seenH3 = true
      if (tag === 'H2') seenH3 = false
      card.className = tag === 'H4' && seenH3 ? 'rb-rule rb-sub' : 'rb-rule'
      el.before(card)
      decorate(el)
      card.append(el)
      continue
    }
    if (tag === 'HR') continue
    if (!card && inChapter) {
      // text right under a chapter title, before any rule heading, gets its own card
      card = document.createElement('section')
      card.className = 'rb-rule rb-intro'
      el.before(card)
    }
    if (card) card.append(el)
  }
  for (const block of root.querySelectorAll('.custom-block.danger')) decorateSanction(block)
  for (const block of root.querySelectorAll('.custom-block.info')) block.classList.add('rb-example')
})

</script>

<template>
  <!-- the component only rearranges the page content on mount; one empty element keeps hydration simple -->
  <span class="rb-root" hidden></span>
</template>

<style>
/* Page chrome: separators out, chapters as dividers */
.rule-book .vp-doc > div > hr { display: none !important; }
.rule-book .rb-hide { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); white-space: pre; }
.rule-book .vp-doc h1.rb-chapter {
  margin: 64px 0 18px; padding: 18px 0 0; border-top: 1px solid var(--vp-c-divider);
  font-size: clamp(1.5rem, 3vw, 2rem); font-weight: 800; letter-spacing: -0.02em; color: #fff;
}
.rule-book .vp-doc h1.rb-chapter:first-of-type { margin-top: 24px; border-top: 0; padding-top: 0; }

/* Rule cards */
.rule-book .rb-rule {
  margin: 12px 0; padding: 18px 20px 6px; border-radius: 14px;
  background: #111113; border: 1px solid var(--vp-c-border);
  scroll-margin-top: 200px;
}
.rule-book .rb-rule.rb-sub { margin-left: clamp(0px, 3vw, 28px); background: #0e0e10; border-style: dashed; }
.rule-book .rb-rule > h2, .rule-book .rb-rule > h3, .rule-book .rb-rule > h4 {
  display: flex; flex-wrap: wrap; align-items: baseline; gap: 6px 10px;
  margin: 0 0 10px; font-size: 1.08rem; font-weight: 750; letter-spacing: 0; text-transform: none; color: #fff;
  scroll-margin-top: 220px;
}
.rule-book .rb-num { font-family: var(--vp-font-family-mono); font-size: 0.85em; color: var(--eg-red-hi); }
.rule-book .rb-name { letter-spacing: 0.01em; }
.rule-book .rb-code {
  margin-left: auto; padding: 2px 8px; border-radius: 6px; font-family: var(--vp-font-family-mono); font-size: 0.72em;
  background: rgba(220, 38, 38, 0.14); color: #fca5a5; border: 1px solid rgba(220, 38, 38, 0.35);
}
.rule-book .rb-rule ul, .rule-book .rb-rule ol { padding-left: 1.3rem; }
.rule-book .rb-rule li { margin: 6px 0; color: var(--vp-c-text-2); }
.rule-book .rb-rule li::marker { color: var(--eg-red); }
.rule-book .rb-rule p { color: var(--vp-c-text-2); }

/* INTERZIS words already colored red in the markdown */
.rule-book .vp-doc span[style*='color: red'], .rule-book .vp-doc span[style*='color:red'] {
  color: #fecaca !important; background: rgba(220, 38, 38, 0.2); padding: 0 6px; border-radius: 5px; font-weight: 700; font-size: 0.92em;
}

/* Sanctions and examples inside a card */
.rule-book .rb-rule .custom-block { margin: 14px -8px 12px; }
.rule-book .rb-sanction {
  display: flex; flex-wrap: wrap; align-items: center; gap: 10px;
  padding: 10px 12px !important; border: 0 !important; border-top: 1px dashed rgba(220, 38, 38, 0.35) !important;
  border-radius: 0 0 10px 10px; background: transparent !important;
}
.rule-book .rb-sanction .custom-block-title { margin: 0; font-size: 11px; letter-spacing: 0.12em; text-transform: uppercase; color: var(--eg-red-hi); }
.rule-book .rb-sanction p { margin: 0 !important; color: #fecaca; }
.rule-book .rb-pills { display: flex; flex-wrap: wrap; gap: 6px; }
.rule-book .rb-pills span { padding: 3px 10px; border-radius: 999px; background: rgba(220, 38, 38, 0.14); border: 1px solid rgba(220, 38, 38, 0.35); color: #fecaca; font-size: 12.5px; font-weight: 600; }
.rule-book .rb-example { background: #141417 !important; border-left-color: #52525b !important; }
.rule-book .rb-example .custom-block-title { color: var(--vp-c-text-3); font-size: 11px; letter-spacing: 0.12em; text-transform: uppercase; }
</style>
