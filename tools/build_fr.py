"""Build the French page (fr/index.html) from the English index.html.

Usage:  python3 tools/build_fr.py

Every visible text node and translatable attribute in index.html is looked up
in tools/fr_strings.py. Run this again after changing index.html; any English
text that has no translation yet is listed so it can be added to the dictionary.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from fr_strings import TEXT, JS, KEEP  # noqa: E402

src = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
missing = []


def norm(s):
    return ' '.join(s.split())


def tr_text(m):
    raw = m.group(1)
    key = norm(raw)
    if not key or key in KEEP or not re.search(r'[A-Za-z]{2}', key):
        return m.group(0)
    if key in TEXT:
        lead = raw[:len(raw) - len(raw.lstrip())]
        trail = raw[len(raw.rstrip()):]
        return '>' + lead + TEXT[key] + trail + '<'
    missing.append(key)
    return m.group(0)


def tr_attr(m):
    name, val = m.group(1), m.group(2)
    key = norm(val)
    if key in TEXT:
        return f'{name}="{TEXT[key]}"'
    if key not in KEEP and re.search(r'[a-z]{3} [a-z]', key):
        missing.append(key)
    return m.group(0)


# Split out <style>, <script> and <svg> blocks: only the markup between them is translated.
parts = re.split(r'(<(?:style|script|svg)\b.*?</(?:style|script|svg)>)', src, flags=re.S)
out = []
for i, part in enumerate(parts):
    if i % 2:  # a style/script/svg block
        out.append(part)
        continue
    part = re.sub(r'>([^<]+)<', tr_text, part)
    part = re.sub(r'\b(alt|placeholder|aria-label|title|content)="([^"]+)"', tr_attr, part)
    out.append(part)
html = ''.join(out)
for en, fr in JS:
    if en not in html:
        missing.append('JS: ' + en)
    html = html.replace(en, fr)

# Page-level changes for the French version.
html = html.replace('<html lang="en">', '<html lang="fr">', 1)
html = html.replace('src="assets/', 'src="../assets/')
html = html.replace('<a class="lang-switch" href="/fr/" hreflang="fr" lang="fr" aria-label="Version française">FR</a>',
                    '<a class="lang-switch" href="/" hreflang="en" lang="en" aria-label="English version">EN</a>')
html = html.replace('<a class="lang-m" href="/fr/" hreflang="fr" lang="fr">français<span>/</span></a>',
                    '<a class="lang-m" href="/" hreflang="en" lang="en">english<span>/</span></a>')

os.makedirs(os.path.join(ROOT, 'fr'), exist_ok=True)
open(os.path.join(ROOT, 'fr', 'index.html'), 'w', encoding='utf-8').write(html)

uniq = list(dict.fromkeys(missing))
if uniq:
    print(f'fr/index.html written; {len(uniq)} string(s) left in English:')
    for s in uniq:
        print('  -', s)
else:
    print('fr/index.html written; everything translated.')
