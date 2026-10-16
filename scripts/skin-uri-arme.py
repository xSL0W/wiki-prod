"""Build the weapon skin catalogue page (docs/general/skin-uri-arme-catalog.md): per weapon (collapsed, grouped by
weapon category), the skins a player can make for it, from the eg-weaponskins catalogue + whitelist and the
uz_AutoShot renders. No recipes: the general page (docs/general/skin-uri-arme.md, written by hand) explains the system.
Re-run after a skin or weapon is added: python3 scripts/skin-uri-arme.py
Renders: [dev]/uz_AutoShot/shots/weapons/<WEAPON>__<COMPONENT>.png and <WEAPON>__base.png; a custom skin (addon
component, no uz_AutoShot shot) uses its card already placed in docs/public/skin-uri-arme. PNG -> WEBP with Pillow,
or with ffmpeg (FFMPEG env var or on PATH) when Pillow is missing."""
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent
RES = WIKI.parent
SKINS_LUA = RES / '[eg]/eg-weaponskins/shared/config_skins.lua'
WHITELIST_LUA = RES / '[eg]/eg-weaponskins/shared/config_whitelist.lua'
WEAPONS_LUA = RES / '[ox]/ox_inventory/data/weapons.lua'
SHOTS = RES / '[dev]/uz_AutoShot/shots/weapons'
OX_IMAGES = RES / '[ox]/ox_inventory/images'
OUT_IMG = WIKI / 'docs/public/skin-uri-arme'
OUT_MD = WIKI / 'docs/general/skin-uri-arme-catalog.md'

TIERS = {'contraband': ('Contrabanda', '#ef4444', 0), 'premium': ('Premium', '#f5b301', 1), 'rare': ('Rar', '#a855f7', 2),
         'common': ('Comun', '#9ca3af', 3)}
CATEGORIES = [('rifle', 'Pusti, sniper-e si MG-uri'), ('smg', 'SMG-uri si shotgun-uri'), ('pistol', 'Pistoale'),
              ('melee', 'Corp la corp')]


def parse_skins(text):
    """skin item -> { label, tier, faction (None = open to all), weapons: { WEAPON: COMPONENT } }"""
    body = text.split('Config.Skins = {', 1)[1]
    skins = {}
    for m in re.finditer(r'\n    (skin_\w+) = \{(.*?)\n    \},', body, re.S):
        block = m.group(2)
        skins[m.group(1)] = {
            'label': re.search(r"label = '([^']+)'", block).group(1),
            'tier': re.search(r"tier = '(\w+)'", block).group(1),
            'faction': (re.search(r"faction = '(\w+)'", block) or [None, None])[1],
            'weapons': dict(re.findall(r"(WEAPON_\w+) = '(COMPONENT_\w+)'", block)),
        }
    return skins


def parse_whitelist(text):
    """skin item -> set of WEAPON names allowed"""
    body = text.split('Config.SkinWhitelist = {', 1)[1]
    return {m.group(1): set(re.findall(r'(WEAPON_\w+) = true', m.group(2)))
            for m in re.finditer(r'\n    (skin_\w+) = \{(.*?)\n    \},', body, re.S)}


def parse_skin_weapons(text):
    """Config.SkinWeapons: every weapon the catalogue shows, with or without a skin"""
    return re.findall(r"'(WEAPON_\w+)'", text.split('Config.SkinWeapons = {', 1)[1].split('\n}', 1)[0])


def parse_weapon_tiers(text):
    """WEAPON -> category key (Config.SkinWeaponTiers)"""
    body = text.split('Config.SkinWeaponTiers = {', 1)[1].split('\n}', 1)[0]
    tiers = {}
    for m in re.finditer(r'\n    (\w+) = \{ multiplier = [\d.]+, weapons = \{(.*?)\} \},', body, re.S):
        for weapon in re.findall(r'(WEAPON_\w+) = true', m.group(2)):
            tiers[weapon] = m.group(1)
    return tiers


def to_webp(src, dst):
    try:
        from PIL import Image
        Image.open(src).save(dst, 'WEBP', quality=80)
    except ImportError:
        ffmpeg = os.environ.get('FFMPEG') or shutil.which('ffmpeg')
        if not ffmpeg:
            sys.exit('neither Pillow nor ffmpeg (set FFMPEG) is available to convert the renders')
        subprocess.run([ffmpeg, '-loglevel', 'error', '-y', '-i', str(src), '-c:v', 'libwebp', '-quality', '80', str(dst)],
                       check=True)


def image(name):
    """URL of a render (converted from the shot; an already placed card when there is no shot), None when missing"""
    src, dst = SHOTS / f'{name}.png', OUT_IMG / f'{name}.webp'
    if src.exists() and (not dst.exists() or src.stat().st_mtime > dst.stat().st_mtime):
        to_webp(src, dst)
    return f'/skin-uri-arme/{name}.webp' if dst.exists() else None


def weapon_image(weapon):
    """The weapon's render (uz_AutoShot base shot), else its ox_inventory item image copied next to the renders"""
    url = image(f'{weapon}__base')
    if url:
        return url
    ox = OX_IMAGES / f'{weapon}.webp'
    if not ox.exists():
        return None
    shutil.copyfile(ox, OUT_IMG / f'{weapon}__base.webp')
    return f'/skin-uri-arme/{weapon}__base.webp'


def card(img, title, tier, faction=None):
    label, color, _ = TIERS[tier]
    pic = f'<img src="{img}" alt="{title}" loading="lazy">' if img else '<div class="sk-noimg">fara imagine</div>'
    only = f'<small>Doar {faction.capitalize()}</small>' if faction else ''
    return f'<div class="sk-card" style="--c:{color}">{pic}<span>{title}</span><small>{label}</small>{only}</div>'


def main():
    skins_text = SKINS_LUA.read_text()
    skins, allowed = parse_skins(skins_text), parse_whitelist(WHITELIST_LUA.read_text())
    categories = parse_weapon_tiers(skins_text)
    labels = dict(re.findall(r"\['(WEAPON_\w+)'\] = \{\s*label = '([^']+)'", WEAPONS_LUA.read_text()))
    OUT_IMG.mkdir(parents=True, exist_ok=True)

    per_weapon = {w: [] for w in parse_skin_weapons(skins_text)}  # WEAPON -> [(skin, component)], also skin-less
    for item, skin in skins.items():
        for weapon in sorted(allowed.get(item, ())):
            if weapon in skin['weapons']:
                per_weapon.setdefault(weapon, []).append((item, skin['weapons'][weapon]))

    missing, out, total = [], [PAGE_HEAD], 0
    for key, title in CATEGORIES:
        # weapons with skins first, the skin-less ones (shown with 0) at the end of the group
        weapons = sorted((w for w in per_weapon if categories.get(w) == key),
                         key=lambda w: (not per_weapon[w], labels.get(w, w)))
        if not weapons:
            continue
        out.append(f'\n## {title}\n\n')
        for weapon in weapons:
            entries = sorted(per_weapon[weapon], key=lambda e: (TIERS[skins[e[0]]['tier']][2], skins[e[0]]['label']))
            base = weapon_image(weapon)
            pic = f'<img src="{base}" alt="" loading="lazy">' if base else ''
            name = labels.get(weapon, weapon)
            total += 1
            if not entries:  # no skin for it yet: shown with 0, nothing to open
                out.append(f'<div class="sk-weapon sk-empty"><div class="sk-row">{pic}<b>{name}</b>'
                           f'<span>0 skin-uri</span></div></div>\n\n')
                continue
            cards = []
            for item, component in entries:
                img = image(f'{weapon}__{component}')
                if not img:
                    missing.append(f'{weapon}__{component}')
                cards.append(card(img, skins[item]['label'], skins[item]['tier'], skins[item]['faction']))
            count = len(entries)
            out.append(f'<details class="sk-weapon"><summary>{pic}<b>{name}</b>'
                       f'<span>{count} {"skin" if count == 1 else "skin-uri"}</span></summary>\n'
                       f'<div class="sk-grid">{"".join(cards)}</div>\n</details>\n\n')
    OUT_MD.write_text(''.join(out))
    print(f'{total} weapons, {sum(len(v) for v in per_weapon.values())} skins -> {OUT_MD.relative_to(WIKI)}; '
          f'missing renders: {len(missing)}')
    for name in missing:
        print('  missing', name)
    return 1 if missing else 0


PAGE_HEAD = '''---
outline: [2, 2]
---

<style>
  .sk-weapon { background: #ffffff06; border: 1px solid #ffffff14; border-radius: 10px; margin: .6rem 0; }
  .sk-weapon > summary { display: flex; align-items: center; gap: .9rem; padding: .5rem .9rem; cursor: pointer;
    list-style: none; }
  .sk-weapon > summary::-webkit-details-marker { display: none; }
  .sk-weapon > summary::after { content: '+'; margin-left: auto; font-size: 1.3rem; color: #9ca3af; }
  .sk-weapon[open] > summary::after { content: '\\2212'; }
  .sk-weapon > summary img, .sk-row img { width: 128px; height: 128px; object-fit: contain; }
  .sk-weapon > summary span, .sk-row span { color: #9ca3af; font-size: .85rem; }
  .sk-row { display: flex; align-items: center; gap: .9rem; padding: .5rem .9rem; }
  .sk-empty { opacity: .55; }
  .sk-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: .75rem;
    padding: 0 .9rem .9rem; }
  .sk-card { background: #ffffff08; border: 1px solid #ffffff14; border-top: 3px solid var(--c); border-radius: 8px;
    padding: .5rem; text-align: center; font-size: .85rem; display: flex; flex-direction: column; gap: .2rem; }
  .sk-card img { width: 100%; aspect-ratio: 1; object-fit: contain; }
  .sk-card small { color: var(--c); font-weight: 600; text-transform: uppercase; letter-spacing: .05em; font-size: .7rem; }
  .sk-noimg { aspect-ratio: 1; display: flex; align-items: center; justify-content: center; color: #6b7280; }
</style>

# Catalog skin-uri arme

Fiecare arma, cu skin-urile pe care le poti face pentru ea. Apasa pe o arma ca sa vezi skin-urile. Cum se fac si cum
se pun: [Skin-uri arme](./skin-uri-arme).
'''

if __name__ == '__main__':
    sys.exit(main())
