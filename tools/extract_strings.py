"""List translatable strings in index.html (text nodes + key attributes)."""
import sys, json
from html.parser import HTMLParser
ATTRS = {'alt', 'placeholder', 'aria-label', 'title'}
class P(HTMLParser):
    def __init__(s):
        super().__init__(convert_charrefs=False); s.skip = 0; s.out = []
    def handle_starttag(s, t, a):
        if t in ('style', 'script', 'svg'): s.skip += 1
        for k, v in a:
            if k in ATTRS and v and v.strip(): s.out.append(v.strip())
            if t == 'meta' and k == 'content' and dict(a).get('name') == 'description': s.out.append(v)
    def handle_endtag(s, t):
        if t in ('style', 'script', 'svg'): s.skip -= 1
    def handle_data(s, d):
        if not s.skip and d.strip(): s.out.append(' '.join(d.split()))
p = P(); p.feed(open(sys.argv[1], encoding='utf-8').read())
seen = []
for x in p.out:
    if x not in seen: seen.append(x)
print(json.dumps(seen, ensure_ascii=False, indent=0))
