"""Wave 3 (private): add every Act, regulation and EPI fetched by wave3_fetch.py to corpus.json as one current-text
version each: the newest Internet Archive capture of its whole page, dated by the page's own point-in-time date (the
day that version came into force). Keeps every act already in corpus.json unchanged. Reads .cache only.

    python -X utf8 wave3_add.py
"""
import collections, hashlib, html, json, re, sys
from nswlib import HERE, CACHE, parse_capture, norm

BASE = 'https://legislation.nsw.gov.au/view/whole/html/inforce/current/'
KIND = {'act': 'Act', 'sl': 'regulation or other statutory instrument', 'epi': 'environmental planning instrument'}


def slug_of(title):
    t = re.sub(r'\s+No\s+[0-9a-z]+$', '', title, flags=re.I)
    return re.sub(r'[^a-z0-9]+', '-', t.lower().replace("'", '')).strip('-')


def main():
    corpus = json.loads((HERE / 'corpus.json').read_text('utf-8'))
    have = {a['slug'] for a in corpus['acts']}
    have_url = {a['url'] for a in corpus['acts']}
    fetched = json.loads((HERE / 'wave3-fetched.json').read_text())
    added, skipped = [], collections.Counter()
    for i in sorted(fetched):
        v = fetched[i]
        if not v or BASE + i in have_url:
            skipped['none' if not v else 'have'] += 1
            continue
        ts, orig, u = v
        raw = (CACHE / hashlib.sha256(u.encode()).hexdigest()).read_bytes()
        t = raw.decode('utf-8', 'replace')
        m = re.search(r'<h1 class="title"[^>]*>(.*?)</h1>', t, re.S)
        pit = collections.Counter(re.findall(r'pointInTime=(\d{4}-\d\d-\d\d)', t)).most_common(1)
        if not m or not pit:
            skipped['no title/date'] += 1
            continue
        title = norm(re.sub(r'<[^>]+>', '', m.group(1)))
        units = parse_capture(t)
        if not units:
            skipped['no units'] += 1
            continue
        d = pit[0][0]
        slug = slug_of(title)
        if slug in have:
            slug = slug + '-' + i
        have.add(slug)
        kind = KIND[i.split('-')[0]]
        note = 'Version in force from %s as shown by the NSW legislation website (Internet Archive capture %s); the newest captured version of this %s.' % (d, ts, kind)
        corpus['acts'].append({'slug': slug, 'short': title, 'title': title, 'url': BASE + i, 'first_law': None, 'earlier_laws': [],
                               'versions': [{'from': d, 'source_url': u, 'sha256': hashlib.sha256(raw).hexdigest(), 'units': units,
                                             'credits': {}, 'note': note}]})
        added.append(slug)
    decs = [x for x in corpus['decisions'] if not x.startswith('Wave 3:')]
    decs.append('Wave 3 (2026-11-03): every Act, regulation and environmental planning instrument whose whole in-force page the Internet Archive captured on or after 1 January 2025 was added as one version, the newest capture, dated by the point-in-time date the page gives for that version (the day it came into force, usually the commencement of its latest amendment); it is credited to the publisher because the page does not name the amending law. Instruments captured only before 2025 are left out, as they may since have been repealed (NSW regulations lapse after five years). legislation.nsw.gov.au itself is not reachable by script, so the Internet Archive is the only source used.')
    corpus['decisions'] = decs
    srcs = [s for s in corpus['sources'] if not s['name'].endswith('wave 3')]
    srcs.append({'name': "NSW legislation (Parliamentary Counsel's Office): Acts, regulations and EPIs in force, wave 3", 'url': 'https://legislation.nsw.gov.au',
                 'retrieved': '2026-11-03', 'licence': 'Creative Commons Attribution 4.0 International (as stated on legislation.nsw.gov.au)',
                 'notes': 'Newest Internet Archive capture (2025 or later) of the whole in-force page of each instrument.'})
    corpus['sources'] = srcs
    (HERE / 'corpus.json').write_text(json.dumps(corpus, ensure_ascii=False, indent=1) + '\n', 'utf-8', newline='\n')
    print(len(added), 'added', dict(skipped), len(corpus['acts']), 'acts')


main()
