"""Build the weapon skin catalogue page (docs/general/skin-uri-arme-catalog.md): per weapon (grouped by weapon category),
the skins a player can make for it, with their tier and how each one is unlocked (no prices: they live in eg-eop), from the
eg-weaponskins catalogue + whitelist and the uz_AutoShot renders. Tier and weapon-type filters are pure CSS (radio inputs).
The page head (style + header + filter bar) is scripts/skin-uri-arme-catalog.head.md; this script fills its @@ slots.
No recipes: the general page (docs/general/skin-uri-arme.md, written by hand) explains the system.
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
HEAD_MD = WIKI / 'scripts/skin-uri-arme-catalog.head.md'

TIERS = {'sindicat': ('Sindicat', '#ff2a2a', 0), 'politie': ('Politie', '#38bdf8', 1), 'premium': ('Premium', '#facc15', 2),
         'event': ('Eveniment Special', '#14b8a6', 3), 'legendary': ('Legendar', '#f97316', 4),
         'contraband': ('Contrabanda', '#ec4899', 5), 'rare': ('Rar', '#a855f7', 6), 'special': ('Deosebit', '#3b82f6', 7),
         'common': ('Comun', '#9ca3af', 8)}
JOB_LABELS = {'police': 'Politie'}  # eg-core job -> the name the card shows (Doar <name>)
CATEGORIES = [('rifle', 'Pusti, snipere si MG-uri'), ('smg', 'SMG-uri si shotgun-uri'), ('pistol', 'Pistoale'),
              ('melee', 'Corp la corp')]
# CSS class keys of the page filters (tier and weapon-type radios)
TIER_KEYS = {'sindicat': 'sindicat', 'politie': 'politie', 'premium': 'premium', 'event': 'event',
             'legendary': 'legendar', 'contraband': 'contrabanda', 'rare': 'rar', 'special': 'deosebit',
             'common': 'comun'}
CAT_KEYS = {'rifle': 'pusti', 'smg': 'smg', 'pistol': 'pistoale', 'melee': 'melee'}


def parse_skins(text):
    """skin item -> { label, tier, faction (None = open to all; a job skin: its job's label), weapons: { WEAPON: COMPONENT } }"""
    body = text.split('Config.Skins = {', 1)[1]
    skins = {}
    for m in re.finditer(r'\n    (skin_\w+) = \{(.*?)\n    \},', body, re.S):
        block = m.group(2)
        skins[m.group(1)] = {
            'label': re.search(r"label = '([^']+)'", block).group(1),
            'tier': re.search(r"tier = '(\w+)'", block).group(1),
            'faction': (re.search(r"faction = '(\w+)'", block) or [None, None])[1]
            or JOB_LABELS.get((re.search(r"job = '(\w+)'", block) or [None, None])[1]),
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
    """WEAPON -> category key, category key -> price multiplier (Config.SkinWeaponTiers)"""
    body = text.split('Config.SkinWeaponTiers = {', 1)[1].split('\n}', 1)[0]
    tiers, multipliers = {}, {}
    for m in re.finditer(r'\n    (\w+) = \{ multiplier = ([\d.]+), weapons = \{(.*?)\} \},', body, re.S):
        multipliers[m.group(1)] = float(m.group(2))
        for weapon in re.findall(r'(WEAPON_\w+) = true', m.group(3)):
            tiers[weapon] = m.group(1)
    return tiers, multipliers


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


def unlock_text(skin):
    if skin['faction']:
        return f"Doar {skin['faction'].capitalize()}"
    if skin['tier'] == 'event':
        return 'Doar din evenimente'
    if skin['tier'] == 'premium':
        return 'Deblocare cu EG Coins'
    return 'Deblocare cu bani murdari'


def slug(weapon):
    return 'w-' + weapon.removeprefix('WEAPON_').lower().replace('_', '-')


def main():
    head, out_path = HEAD_MD.read_text(), OUT_MD
    OUT_IMG.mkdir(parents=True, exist_ok=True)
    skins_text = SKINS_LUA.read_text()
    skins, allowed = parse_skins(skins_text), parse_whitelist(WHITELIST_LUA.read_text())
    categories, _ = parse_weapon_tiers(skins_text)
    labels = dict(re.findall(r"\['(WEAPON_\w+)'\] = \{\s*label = '([^']+)'", WEAPONS_LUA.read_text()))

    per_weapon = {w: [] for w in parse_skin_weapons(skins_text)}
    for item, skin in skins.items():
        for weapon in sorted(allowed.get(item, ())):
            if weapon in skin['weapons']:
                per_weapon.setdefault(weapon, []).append((item, skin['weapons'][weapon]))

    missing, body = [], []
    shown_cards, shown_weapons = 0, 0
    index = []
    for key, _ in CATEGORIES:
        weapons = sorted((w for w in per_weapon if categories.get(w) == key), key=lambda w: labels.get(w, w))
        if not weapons:
            continue
        blocks, empty, cat_tiers = [], [], set()
        for weapon in weapons:
            entries = sorted(per_weapon[weapon], key=lambda e: (TIERS[skins[e[0]]['tier']][2], skins[e[0]]['label']))
            cards, tiers = [], set()
            for item, component in entries:
                name = f'{weapon}__{component}'
                if not image(name):
                    missing.append(f'{labels.get(weapon, weapon)}: {skins[item]["label"]} ({name}.webp)')
                    continue
                skin = skins[item]
                tier_label, color, _ = TIERS[skin['tier']]
                t = TIER_KEYS[skin['tier']]
                tiers.add(t)
                short = skin['label'].removeprefix('Skin ')
                cards.append(
                    f'<li class="skc-card t-{t}" style="--c:{color}">'
                    f'<img class="skc-img" src="/skin-uri-arme/{name}.webp" alt="Skin {short} pe {labels.get(weapon, weapon)}" '
                    f'width="512" height="512" loading="lazy" decoding="async">'
                    f'<span class="skc-name">{short}</span>'
                    f'<span class="skc-badge">{tier_label}</span>'
                    f'<span class="skc-how">{unlock_text(skin)}</span></li>')
            name = labels.get(weapon, weapon)
            if not cards:
                empty.append(name)
                continue
            shown_weapons += 1
            shown_cards += len(cards)
            cat_tiers |= tiers
            index.append((key, name, slug(weapon), tiers))
            base = weapon_image(weapon)
            pic = (f'<img class="skc-wimg" src="{base}" alt="" width="96" height="96" '
                   f'loading="lazy" decoding="async">') if base else ''
            dots = ''.join(f'<i style="--c:{TIERS[k][1]}" title="{TIERS[k][0]}"></i>'
                           for k in sorted({skins[i]['tier'] for i, c in entries
                                            if (OUT_IMG / f"{weapon}__{c}.webp").exists()},
                                           key=lambda k: TIERS[k][2]))
            n = len(cards)
            blocks.append(
                f'<section class="skc-w {" ".join("h-" + t for t in sorted(tiers))}" id="{slug(weapon)}">'
                f'<header class="skc-whead">{pic}<div class="skc-wtitle"><h3 class="skc-h3">{name}</h3>'
                f'<span class="skc-count">{n} {"skin" if n == 1 else "skin-uri"}</span></div>'
                f'<span class="skc-dots">{dots}</span></header>'
                f'<ul class="skc-grid">{"".join(cards)}</ul></section>')
        cat = CAT_KEYS[key]
        tier_cls = ' '.join('h-' + t for t in sorted(cat_tiers))
        tail = (f'<p class="skc-none">Fara skin-uri deocamdata: {", ".join(empty)}.</p>') if empty else ''
        body.append(f'<div class="skc-cat c-{cat} {tier_cls}"><h2 class="skc-h2">{dict(CATEGORIES)[key]}</h2>'
                    f'{"".join(blocks)}{tail}</div>')

    nav = ''.join(f'<a class="skc-jump j-{CAT_KEYS[k]} {" ".join("h-" + t for t in sorted(ts))}" href="#{s}">{n}</a>'
                  for k, n, s, ts in index)
    tier_order = sorted(TIERS, key=lambda k: TIERS[k][2])
    radios, tlabels, css = [], [], []
    radios.append('<input class="skc-radio" type="radio" name="skc-t" id="skc-t-all" checked>')
    tlabels.append('<label class="skc-chip" for="skc-t-all">Toate</label>')
    for k in tier_order:
        t, (lab, color, _) = TIER_KEYS[k], TIERS[k]
        radios.append(f'<input class="skc-radio" type="radio" name="skc-t" id="skc-t-{t}">')
        tlabels.append(f'<label class="skc-chip" for="skc-t-{t}" style="--c:{color}"><i></i>{lab}</label>')
        css.append(f'#skc-t-{t}:checked ~ .skc-list .skc-cat:not(.h-{t}), #skc-t-{t}:checked ~ .skc-list .skc-w:not(.h-{t}), '
                   f'#skc-t-{t}:checked ~ .skc-list .skc-card:not(.t-{t}), #skc-t-{t}:checked ~ .skc-nav .skc-jump:not(.h-{t}) {{ display: none; }}')
    radios.append('<input class="skc-radio" type="radio" name="skc-c" id="skc-c-all" checked>')
    clabels = ['<label class="skc-chip" for="skc-c-all">Toate</label>']
    for key, _ in CATEGORIES:
        c = CAT_KEYS[key]
        radios.append(f'<input class="skc-radio" type="radio" name="skc-c" id="skc-c-{c}">')
        clabels.append(f'<label class="skc-chip" for="skc-c-{c}">{dict(CATEGORIES)[key]}</label>')
        css.append(f'#skc-c-{c}:checked ~ .skc-list .skc-cat:not(.c-{c}), #skc-c-{c}:checked ~ .skc-nav .skc-jump:not(.j-{c}) {{ display: none; }}')
    ids = ['skc-t-all'] + [f'skc-t-{TIER_KEYS[k]}' for k in tier_order] + ['skc-c-all'] + [f'skc-c-{CAT_KEYS[k]}' for k, _ in CATEGORIES]
    css.append(', '.join(f'#{i}:checked ~ .skc-bar label[for="{i}"]' for i in ids) + ' { color: #fff; background: #2a2a30; border-color: var(--c, var(--red)); box-shadow: inset 0 -2px 0 var(--c, var(--red)); }')
    css.append(', '.join(f'#{i}:focus-visible ~ .skc-bar label[for="{i}"]' for i in ids) + ' { outline: 3px solid var(--red); outline-offset: 2px; }')
    page = (head.replace('@@WEAPONS@@', str(shown_weapons)).replace('@@SKINS@@', str(shown_cards))
            .replace('@@NAV@@', nav).replace('@@RADIOS@@', ''.join(radios)).replace('@@TIERS@@', ''.join(tlabels))
            .replace('@@CATS@@', ''.join(clabels)).replace('/*@@FILTERCSS@@*/', '\n'.join(css)).replace('@@BODY@@', '\n'.join(body)))
    out_path.write_text(page)
    print(f'{shown_weapons} weapons, {shown_cards} cards -> {out_path.relative_to(WIKI)}; missing renders: {len(missing)}')
    for m in missing:
        print('  missing', m)
    return 1 if missing else 0



if __name__ == '__main__':
    sys.exit(main())
