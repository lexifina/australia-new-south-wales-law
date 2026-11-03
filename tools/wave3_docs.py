"""Wave 3 (private): rewrite repo/README.md (table, scope, dates) and repo/LICENSE from corpus.json."""
import json, re, pathlib
H = pathlib.Path(__file__).parent
c = json.load(open(H / 'corpus.json', encoding='utf-8'))
FIRST = {'constitution-act-1902', 'crimes-act-1900', 'civil-liability-act-2002', 'sale-of-goods-act-1923'}
rows = []
kinds = {'act': 0, 'sl': 0, 'epi': 0}
for a in c['acts']:
    v = a['versions']
    k = a['url'].rsplit('/', 1)[-1].split('-')[0]
    kinds[k] += 1
    if a['slug'] in FIRST:
        hist = 'Versions in force from %s to %s; versions between captures, and earlier ones, are missing' % (v[0]['from'], v[-1]['from'])
    else:
        hist = 'Current text: the version in force from %s (newest capture)' % v[-1]['from']
    rows.append('| `%s/` | %s | %d | %s |' % (a['slug'], a['title'], len(v), hist))
s = (H / 'repo' / 'README.md').read_text('utf-8')
s = re.sub(r'(\| --- \| --- \| ---: \| --- \|\n)(\| `[a-z0-9-]+/` \|[^\n]*\n)+', lambda m: m.group(1) + ''.join(r + '\n' for r in rows), s, count=1)
s = re.sub(r'This is an early build:[^\n]*\n', 'This build holds %d Acts, %d regulations and other statutory instruments and %d environmental planning instruments: every one whose in-force page the Internet Archive captured in 2025 or 2026, as its current text, and for four core Acts the earlier versions captured since 2020.\n' % (kinds['act'], kinds['sl'], kinds['epi']), s, count=1)
s = s.replace('- Every New South Wales Act not in the table.', '- Every New South Wales Act, regulation or planning instrument not in the table: those the Internet Archive has not captured since 1 January 2025 (some may since have been repealed or remade).\n- For all but the four core Acts, every version before the newest captured one.')
s = s.replace('The text is each Act in the table as shown', 'The text is each instrument in the table as shown')
s = s.replace("The first version (25 March 2020) is the oldest one captured, not the Act's first text (the Act is from 1902).", "For the four core Acts the first version is the oldest one captured, not the Act's first text. For every other instrument the one version is its current text, dated the day that version came into force (usually the commencement of its latest amendment); it is credited to the publisher because the page does not name the amending law, and it says nothing about the text before that day.")
(H / 'repo' / 'README.md').write_text(s, 'utf-8', newline='\n')
lic = """The legal text comes from the NSW legislation website (https://legislation.nsw.gov.au), Parliamentary Counsel's Office, State of New South Wales: every Act, regulation and environmental planning instrument listed in README.md, read from Internet Archive captures of the website's whole in-force pages and retrieved between 29 October and 3 November 2026.

Based on content from the New South Wales Legislation website at 3 November 2026. For the latest information on New South Wales Government legislation please go to https://www.legislation.nsw.gov.au.

The NSW legislation website licenses its copyright material under the Creative Commons Attribution 4.0 International licence (https://creativecommons.org/licenses/by/4.0/). Its Copyright page (as captured by the Internet Archive on 17 December 2025) states: "Unless otherwise noted, all copyright material available on or through this website is licensed under a Creative Commons Attribution 4.0 International licence (CC BY 4.0)", and asks that changed content carry the attribution above. Copyright in the legislation: (c) State of New South Wales.

Changes made by Lexifina: the text was converted to one Markdown file per provision, one paragraph per line; spacing, quotes and dashes were normalised; history notes, footnotes, running heads and page numbers were removed; and the text was arranged as git commits. The wording of the law was not changed. The NSW Parliamentary Counsel's Office does not endorse this repository.

Lexifina's own contributions (the arrangement of the history, the commit messages, the tables and the tools) are dedicated to the public domain under CC0 1.0 Universal: https://creativecommons.org/publicdomain/zero/1.0/
"""
(H / 'repo' / 'LICENSE').write_text(lic, 'utf-8', newline='\n')
print(kinds, len(rows))
