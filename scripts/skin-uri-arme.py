"""Build the weapon skin catalog page (docs/zona-info/skin-uri-arme.md) from the eg-weaponskins catalogue
and the uz_AutoShot renders. Re-run after a skin or weapon is added: python3 scripts/skin-uri-arme.py"""
import re
import sys
from pathlib import Path
from PIL import Image

WIKI = Path(__file__).resolve().parent.parent
RES = WIKI.parent
SKINS_LUA = RES / '[eg]/eg-weaponskins/shared/config_skins.lua'
WEAPONS_LUA = RES / '[ox]/ox_inventory/data/weapons.lua'
SHOTS = RES / '[dev]/uz_AutoShot/shots/weapons'
OUT_IMG = WIKI / 'docs/public/skin-uri-arme'
OUT_MD = WIKI / 'docs/zona-info/skin-uri-arme.md'

TIERS = [('legendary', 'Legendare', '#f5b301'), ('rare', 'Rare', '#a855f7'), ('common', 'Comune', '#9ca3af')]
MATERIALS = {'vinyl_film': 'Folie de vinil', 'metal_flakes': 'Fulgi metalici', 'gold_leaf': 'Foita de aur',
             'pigment_black': 'Pigment negru', 'pigment_green': 'Pigment verde', 'pigment_red': 'Pigment rosu',
             'pigment_white': 'Pigment alb'}


def parse_skins(text):
    """skin item -> { label, tier, pigment, weapons: [(weapon, component)] }, in catalogue order"""
    skins = {}
    body = text.split('Config.Skins = {', 1)[1]
    for m in re.finditer(r'\n    (skin_\w+) = \{(.*?)\n    \},', body, re.S):
        block = m.group(2)
        skins[m.group(1)] = {
            'label': re.search(r"label = '([^']+)'", block).group(1),
            'tier': re.search(r"tier = '(\w+)'", block).group(1),
            'pigment': (re.search(r"pigment = '(\w+)'", block) or [None, None])[1],
            'weapons': sorted(re.findall(r"(WEAPON_\w+) = '(COMPONENT_\w+)'", block)),
        }
    return skins


def parse_tier_costs(text):
    """tier -> [(item, amount)]"""
    block = text.split('Config.SkinTiers = {', 1)[1].split('\n}', 1)[0]
    return {tier: re.findall(r"item = '(\w+)', amount = (\d+)", items)
            for tier, items in re.findall(r'(\w+) = \{(.*?)\},$', block, re.M)}


def webp(name):
    """Convert one render to webp in the public folder; returns its URL or None when the render is missing"""
    src = SHOTS / f'{name}.png'
    if not src.exists():
        return None
    Image.open(src).save(OUT_IMG / f'{name}.webp', 'WEBP', quality=80)
    return f'/skin-uri-arme/{name}.webp'


def card(img, title):
    return (f'<div class="sk-card"><img src="{img}" alt="{title}" loading="lazy"><span>{title}</span></div>'
            if img else f'<div class="sk-card sk-missing"><span>{title}</span></div>')


def main():
    text = SKINS_LUA.read_text()
    skins, costs = parse_skins(text), parse_tier_costs(text)
    labels = dict(re.findall(r"\['(WEAPON_\w+)'\] = \{\s*label = '([^']+)'", WEAPONS_LUA.read_text()))
    OUT_IMG.mkdir(parents=True, exist_ok=True)
    missing = []
    out = [PAGE_HEAD]
    for tier, tier_label, color in TIERS:
        recipe = ', '.join(f'{amount}x {MATERIALS.get(item, "pigmentul skin-ului" if item == "pigment" else item)}'
                           for item, amount in costs[tier])
        out.append(f'\n## Skin-uri {tier_label}\n\n<p class="sk-recipe" style="--c:{color}">Reteta: {recipe}</p>\n')
        for item, skin in skins.items():
            if skin['tier'] != tier:
                continue
            pigment = f' &middot; {MATERIALS[skin["pigment"]]}' if skin['pigment'] else ''
            out.append(f'\n### {skin["label"]}\n\n<p class="sk-meta">{len(skin["weapons"])} arme{pigment}</p>\n')
            cards = []
            for weapon, component in skin['weapons']:
                img = webp(f'{weapon}__{component}')
                if not img:
                    missing.append(f'{weapon}__{component}')
                cards.append(card(img, labels.get(weapon, weapon)))
            out.append(f'<div class="sk-grid" style="--c:{color}">{"".join(cards)}</div>\n')
    OUT_MD.write_text(''.join(out))
    print(f'{len(skins)} skins -> {OUT_MD.relative_to(WIKI)}; missing renders: {len(missing)}')
    for name in missing:
        print('  missing', name)
    return 1 if missing else 0


PAGE_HEAD = '''---
outline: [2, 3]
---

<style>
  .sk-recipe { border-left: 4px solid var(--c); padding: .5rem 1rem; background: #ffffff0a; border-radius: 6px; }
  .sk-meta { color: #9ca3af; margin-top: -.5rem; }
  .sk-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: .75rem; }
  .sk-card { background: #ffffff08; border: 1px solid #ffffff14; border-top: 3px solid var(--c); border-radius: 8px;
    padding: .5rem; text-align: center; font-size: .85rem; }
  .sk-card img { width: 100%; aspect-ratio: 1; object-fit: contain; }
  .sk-missing { display: flex; align-items: center; justify-content: center; min-height: 150px; color: #6b7280; }
</style>

# Skin-uri arme

Skin-urile schimba aspectul armei tale. Le creezi la **Atelier skin-uri**, langa plantatia de mac, din materiale
gasite in butoaiele din No Man's Land. Tot acolo le aplici si le scoti de pe arma.

- Fiecare skin are o durabilitate (100 cand e creat). La fiecare scoatere de pe arma pierde din ea, iar la 0 se rupe.
- Un skin se pune doar pe armele din lista lui. Aplicarea pe arme mai bune costa materiale in plus, platite la atelier.
'''

if __name__ == '__main__':
    sys.exit(main())
