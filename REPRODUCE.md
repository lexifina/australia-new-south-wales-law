# How this repository was made (New South Wales)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| NSW legislation (Parliamentary Counsel's Office) | <https://legislation.nsw.gov.au/view/whole/html/inforce/current/act-1902-032> | 2026-10-29 | Creative Commons Attribution 4.0 International (as stated on legislation.nsw.gov.au) |
| NSW legislation (Parliamentary Counsel's Office): other Acts | <https://legislation.nsw.gov.au> | 2026-10-30 | Creative Commons Attribution 4.0 International (as stated on legislation.nsw.gov.au) |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution-act-1902` | Constitution Act 1902 No 32 | 6 | 2020-03-25 to 2025-09-17 |
| `crimes-act-1900` | Crimes Act 1900 No 40 | 19 | 2020-10-27 to 2025-12-24 |
| `civil-liability-act-2002` | Civil Liability Act 2002 No 22 | 3 | 2020-03-01 to 2022-06-16 |
| `sale-of-goods-act-1923` | Sale of Goods Act 1923 No 1 | 1 | 2012-01-30 to 2012-01-30 |

The build made 29 commits:

| Commits | Kind |
| ---: | --- |
| 4 | first version of an act |
| 0 | one law on its in-force day |
| 25 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 0 laws in the record.
- 29 tags.

## Dates

Each commit is dated at noon (Australia/Sydney) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Each version is dated by the point-in-time date the NSW legislation website gives for it. No general rule on commencement was used. https://legislation.nsw.gov.au/view/whole/html/inforce/current/act-1902-032

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `f031c36e017c39d4eff1b7578e8245f3934c394a5414936532caf1a6b1161c74` (2041543 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3e59cb6f05eccb94a9ec14431a7f6781221e83ef`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- Only the versions that the Internet Archive captured are recorded; versions between two captures are missing, and a change that appears is credited to no law because the capture does not say which Act made it (the commit is labelled unexplained).
- Each version is dated by the point-in-time date in the page's own links; the oldest one is recorded as the oldest version available.
- Sections, Parts, Divisions and Schedules are separate files; the history notes are left out of the text.
- Other Acts: built the same way as the Constitution Act 1902 from the Internet Archive captures of the whole-Act page; only captured versions exist, versions between two captures are missing, and every change after the first captured version is committed by the publisher as unexplained because the captures do not name the amending Act. Versions after the first are stored as changes against the version before.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none
