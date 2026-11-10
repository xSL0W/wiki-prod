"""Copy the ox_inventory item images the wiki uses into docs/public/items.

Pages show an item as <img class="eg-item" src="/items/<file>.webp" alt="">.
Run after editing pages: copies every referenced file, removes unreferenced
ones and fails when a page names an image ox_inventory does not have.
"""
import re
import shutil
import sys
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent
OX_IMAGES = WIKI.parent / '[ox]/ox_inventory/images'
OUT = WIKI / 'docs/public/items'

used = set()
for page in (WIKI / 'docs').rglob('*.md'):
    used |= set(re.findall(r'["(]/items/([\w.\-]+\.webp)', page.read_text(encoding='utf-8')))

missing = sorted(f for f in used if not (OX_IMAGES / f).is_file())
if missing:
    sys.exit('not in ox_inventory/images: ' + ', '.join(missing))

OUT.mkdir(exist_ok=True)
for f in sorted(used):
    shutil.copyfile(OX_IMAGES / f, OUT / f)
for old in OUT.glob('*.webp'):
    if old.name not in used:
        old.unlink()
print(f'{len(used)} item images in {OUT.relative_to(WIKI)}')
