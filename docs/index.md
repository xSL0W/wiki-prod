---
# https://vitepress.dev/reference/default-theme-home-page
layout: home

hero:
  name: 'EliteGamers Romania
  IMERSIV Roleplay'
  text:  'Official Wikipedia'
  tagline: Bine ai venit pe Wiki-ul official al server-ului EliteGamers RolePlay!
  actions:
    - theme: brand
      text: Explorează wiki
      link: zona-info/informatii
    - theme: alt
      text: FAQ
      link: 'zona-info/cum-intru-pe-server'
    - theme: alt
      text: Alatura-te noua
      link: https://discord.gg/elitegamers-ro-351058903271735306
  image:
    src: /elitegamers.webp
    alt: eliteGamers.ro

features:
  - title: Gameplay
    details: Detalii despre gameplay
    link: 'zona-info/cum-intru-pe-server'
  - title: Sisteme
    details: Prezentarea sistemelor noastre
    link: 'general/rewards'

  - title: FAQ
    details: Aici găsiți răspunsuri rapide la întrebările comune despre serverul nostru FiveM, pentru a vă ajuta să vă bucurați de experiența de joc
    link: 'zona-info/faq'
  - title: Our Team
    details: O echipă talentată dedicată inovației și excelenței
    features:
  - title: Regulament
    details: "Pe acest Wiki o sa gasesti si regulamentele necesare dezvoltarii tale."
    link: 'zona-info/regulament'

  - title: Scripts
    details: "Ai posibilitatea de a vedea ce sisteme folosim pe EliteGamers RP Romania!"
---



<script setup>
import { onMounted } from 'vue'
import SiteMap from './.vitepress/components/SiteMap.vue'


onMounted(() => {
  const cards = Array.from(document.querySelectorAll(".card-section .card"))
  const cardsContainer = document.querySelector(".card-section")
  if (!cardsContainer) return

  cardsContainer.addEventListener("mousemove", (e) => {
    for (const card of cards) {
      const rect = card.getBoundingClientRect()
      const x = e.clientX - rect.left
      const y = e.clientY - rect.top
      card.style.setProperty("--mouse-x", `${x}px`)
      card.style.setProperty("--mouse-y", `${y}px`)
    }
  })
})
</script>


## Our Team (Staff) { .eg-section-title }

<div class="eg-cards-team">

  <div class="eg-card">
    <img src="/public/quo.jpg" alt="Quo" />
    <div class="eg-name">Quo</div>
    <div class="eg-role">Fondator</div>
    <span class="eg-badge red">Founder</span>
    <div class="eg-desc">Conduce echipa staff și coordoneaza proiectele comunității</div>
  </div>

  <div class="eg-card">
    <img src="https://cdn.discordapp.com/avatars/262600228719427584/cb935ab9648fedf2747866af9256ea85.png" alt="xslow" />
    <div class="eg-name">xSL0W</div>
    <div class="eg-role">Developer & Fondator</div>
    <span class="eg-badge red">Founder</span>
    <div class="eg-desc">Responsabil pe partea tehnică</div>
  </div>

  <div class="eg-card">
    <img src="https://cdn.discordapp.com/avatars/295581149986553857/14ab973e2e0ad5cf4ecf5f55c0d8a94b.webp?size=1024" alt="sNok3" />
    <div class="eg-name">sNok3</div>
    <div class="eg-role">Developer</div>
    <span class="eg-badge red">Developer</span>
    <div class="eg-desc">Responsabil pe partea tehnică</div>
  </div>

  <div class="eg-card">
    <img src="https://cdn.discordapp.com/avatars/289800581420417025/9ad8a8799df6489541919ff4e1504343?size=1024" alt="Crixus99" />
    <div class="eg-name">Crixus99</div>
    <div class="eg-role">Community Manager</div>
    <span class="eg-badge red">Community Manager</span>
    <div class="eg-desc">Ajută în gestionarea comunității și organizarea activităților</div>
  </div>

  <div class="eg-card">
    <img src="https://cdn.discordapp.com/avatars/848867959219683360/afdd097081271465d4ea1e63fbe324cb.png" alt="dey" />
    <div class="eg-name">dey</div>
    <div class="eg-role">Official Assets Creator</div>
    <span class="eg-badge red">Official Assets Creator</span>
    <div class="eg-desc">Asigura asset-urile necesare si ajuta la dezvoltarea server-ului</div>
  </div>
 </div>


---

<SiteMap />
