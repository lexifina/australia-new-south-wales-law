"""Helpers for reading NSW legislation whole-Act pages (copied from parse.py)."""
import collections, hashlib, html, json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
CACHE = HERE / ".cache"

SPLIT = re.compile(r'<div id="([^"]+)" class="(frag-part|frag-division|frag-schedule|frag-clause)"')


def norm(s):
    s = html.unescape(s).replace(' ', ' ').replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = s.replace('–', '-').replace('—', '-')
    return re.sub(r'[ \t]+', ' ', s).strip()


def key_of(i):
    k = re.sub(r'\d+', lambda m: m.group().zfill(3), i)
    return re.sub(r'[^a-z0-9]+', '-', k.lower()).strip('-')


def text_of(frag):
    frag = re.sub(r'<div class="frag-historynote">.*?</div></div>', '', frag, flags=re.S)
    frag = re.sub(r'<div class="view-history-note">.*?</div>', '', frag, flags=re.S)
    frag = re.sub(r'<span class="frag-no">(.*?)</span>', lambda m: '\x01' + m.group(1) + ' ', frag, flags=re.S)
    frag = re.sub(r'</?(?:div|blockquote|p|br|li|tr|table|h\d)[^>]*>', '\n', frag)
    frag = re.sub(r'<[^>]+>', '', frag)
    out = []
    for l in html.unescape(frag).split('\n'):
        l = norm(l.replace('\x01', ''))
        if l:
            out.append(l)
    return out


def parse_capture(t):
    body = t[t.find('<div id="fragview">'):]
    body = body[:body.find('</div></div></div><script') if '</div></div></div><script' in body else len(body)]
    marks = [(m.start(), m.group(1), m.group(2)) for m in SPLIT.finditer(body)]
    units = {}
    for n, (st, i, cls) in enumerate(marks):
        en = marks[n + 1][0] if n + 1 < len(marks) else len(body)
        ls = text_of(body[st:en])
        if not ls:
            continue
        k = key_of(i)
        label = ls[0][:60] if cls != 'frag-clause' else ('s ' + i.split('.')[-1])
        kind = {'frag-part': 'part', 'frag-division': 'division', 'frag-schedule': 'schedule', 'frag-clause': 'section'}[cls]
        # heading first line, then provisions
        units[k] = {'label': ('Section ' + i.split('sec.')[-1]) if cls == 'frag-clause' else ls[0][:60], 'kind': kind,
                    'text': '# ' + ls[0] + '\n' + ''.join(l + '\n' for l in ls[1:])}
    front = re.search(r'<div id="frnt-lt"[^>]*>(.*?)</div></div>', t, re.S)
    if front:
        fl = text_of(front.group(1))
        if fl:
            units = {'long-title': {'label': 'Long title', 'kind': 'front', 'text': '# Long title\n' + '\n'.join(fl) + '\n'}, **units}
    return units


