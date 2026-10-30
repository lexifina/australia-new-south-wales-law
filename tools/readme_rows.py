"""Rewrite the table and wording in repo/README.md and repo/LICENSE from corpus.json (private)."""
import json, re, pathlib
H = pathlib.Path(__file__).parent
c = json.load(open(H / 'corpus.json', encoding='utf-8'))
rows = []
for a in c['acts']:
    v = a['versions']
    rows.append('| `%s/` | %s (sections, Parts, Divisions and Schedules) | %d | Versions in force from %s to %s; versions between captures, and earlier ones, are missing |' % (a['slug'], a['title'], len(v), v[0]['from'], v[-1]['from']))
s = (H / 'repo' / 'README.md').read_text('utf-8')
s = re.sub(r'(\| --- \| --- \| ---: \| --- \|\n)(\| `[a-z0-9-]+/` \|[^\n]*\n)+', lambda m: m.group(1) + ''.join(r + '\n' for r in rows), s, count=1)
s = s.replace('This is a first build: the Constitution Act 1902 only, with the versions the Internet Archive captured.', 'This is an early build: the Constitution Act 1902 and the core Acts in the table, each with the versions the Internet Archive captured.')
s = s.replace('- Every other New South Wales Act.', '- Every New South Wales Act not in the table.')
s = s.replace('The text is the Constitution Act 1902 No 32 as shown', 'The text is each Act in the table as shown')
(H / 'repo' / 'README.md').write_text(s, 'utf-8', newline='\n')
l = (H / 'repo' / 'LICENSE').read_text('utf-8')
names = ', '.join(a['title'] for a in c['acts'])
l = re.sub(r'Parliamentary Counsel\'s Office, Constitution Act 1902 No 32, read', "Parliamentary Counsel's Office, %s, read" % names, l, count=1) if 'Crimes' not in l else l.replace('Crimes Act 1900 No 40, read','Crimes Act 1900 No 40, ' + ', '.join(a['title'] for a in c['acts'][2:]) + ', read') if 'Civil Liability' not in l and len(c['acts'])>2 else l
(H / 'repo' / 'LICENSE').write_text(l, 'utf-8', newline='\n')
