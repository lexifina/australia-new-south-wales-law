"""Add acts from the cached Internet Archive captures of legislation.nsw.gov.au to corpus.json (private; reads .cache only).

usage: python -X utf8 add_acts.py <act id> <slug> <short> <title> [...]
Keeps every act already in corpus.json; replaces an act with the same slug.
"""
import collections, hashlib, html, json, re, sys
import nswlib
from nswlib import HERE, CACHE, parse_capture

BASE = 'https://legislation.nsw.gov.au/view/whole/html/inforce/current/'


def build_act(aid, slug, short, title, corpus):
    caps = [l.split() for l in (HERE / ('captures-%s.txt' % aid)).read_text().splitlines() if l.strip()]
    by_date = {}
    for ts, url, *_ in caps:
        u = 'http://web.archive.org/web/%sid_/%s' % (ts, url)
        p = CACHE / hashlib.sha256(u.encode()).hexdigest()
        if not p.exists():
            print('missing', ts, file=sys.stderr)
            continue
        raw = p.read_bytes()
        t = raw.decode('utf-8', 'replace')
        pit = collections.Counter(re.findall(r'pointInTime=(\d{4}-\d\d-\d\d)', t)).most_common(1)
        if not pit:
            print('no pointInTime', ts, file=sys.stderr)
            continue
        if '</html>' not in t[-3000:]:
            print('truncated capture skipped', ts, len(raw), file=sys.stderr)
            continue
        units = parse_capture(t)
        if len(units) < 5:
            print('too few units', ts, len(units), file=sys.stderr)
            continue
        by_date[pit[0][0]] = (ts, u, hashlib.sha256(raw).hexdigest(), units)   # later capture of the same version wins
    versions, prev = [], None
    for d in sorted(by_date):
        ts, u, sha, units = by_date[d]
        if prev is not None and units == prev:
            continue
        note = 'Version in force from %s as shown by the NSW legislation website (Internet Archive capture %s).' % (d, ts)
        if prev is None:
            v = {'from': d, 'source_url': u, 'sha256': sha, 'units': units, 'credits': {}, 'note': note}
        else:
            ch = {k: x for k, x in units.items() if prev.get(k) != x}
            ch.update({k: None for k in prev if k not in units})
            v = {'from': d, 'source_url': u, 'sha256': sha, 'changes': ch, 'credits': {}, 'note': note}
        versions.append(v)
        prev = units
    print(slug, title, [v['from'] for v in versions], [len(v.get('units') or v['changes']) for v in versions])
    act = {'slug': slug, 'short': short, 'title': title, 'url': BASE + aid, 'first_law': None, 'earlier_laws': [], 'versions': versions}
    corpus['acts'] = [a for a in corpus['acts'] if a['slug'] != slug] + [act]
    return title


corpus = json.loads((HERE / 'corpus.json').read_text('utf-8'))
a = sys.argv[1:]
for i in range(0, len(a), 4):
    build_act(a[i], a[i + 1], a[i + 2], a[i + 3], corpus)
corpus['sources'] = [s for s in corpus['sources'] if 'Constitution Act' in s['notes']] + [{
    'name': "NSW legislation (Parliamentary Counsel's Office): other Acts", 'url': 'https://legislation.nsw.gov.au', 'retrieved': '2026-10-30',
    'licence': 'Creative Commons Attribution 4.0 International (as stated on legislation.nsw.gov.au)',
    'notes': 'Whole-Act page of each Act as it stood on each date; read from Internet Archive captures of the NSW legislation website.'}]
decs = [d for d in corpus['decisions'] if not d.startswith('Other Acts:')]
decs.append('Other Acts: built the same way as the Constitution Act 1902 from the Internet Archive captures of the whole-Act page; only captured versions exist, versions between two captures are missing, and every change after the first captured version is committed by the publisher as unexplained because the captures do not name the amending Act. Versions after the first are stored as changes against the version before.')
corpus['decisions'] = decs
(HERE / 'corpus.json').write_text(json.dumps(corpus, ensure_ascii=False, indent=1) + '\n', 'utf-8', newline='\n')
