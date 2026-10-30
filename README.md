# New South Wales (Australia): law history in git

The law of New South Wales (Australia) as a git history. Each provision is one file, each law gets one commit on the day it took effect, and the law that made each change is the commit's author. `git blame` names the law behind every paragraph and `git log` lists every change to an article.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `au-nsw/`.

This is an early build: the Constitution Act 1902 and the core Acts in the table, each with the versions the Internet Archive captured.

## What is in it now

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitution-act-1902/` | Constitution Act 1902 No 32 (sections, Parts, Divisions and Schedules) | 6 | Versions in force from 2020-03-25 to 2025-09-17; versions between captures, and earlier ones, are missing |
| `crimes-act-1900/` | Crimes Act 1900 No 40 (sections, Parts, Divisions and Schedules) | 19 | Versions in force from 2020-10-27 to 2025-12-24; versions between captures, and earlier ones, are missing |
| `civil-liability-act-2002/` | Civil Liability Act 2002 No 22 (sections, Parts, Divisions and Schedules) | 3 | Versions in force from 2020-03-01 to 2022-06-16; versions between captures, and earlier ones, are missing |
| `sale-of-goods-act-1923/` | Sale of Goods Act 1923 No 1 (sections, Parts, Divisions and Schedules) | 1 | Versions in force from 2012-01-30 to 2012-01-30; versions between captures, and earlier ones, are missing |

## Where the text comes from

The text is each Act in the table as shown on the NSW legislation website of the Parliamentary Counsel's Office (legislation.nsw.gov.au), the whole-Act view of the version in force. The site cannot be read by script, so each version is read from an Internet Archive capture of that page; the page names the date the version is in force from (its point-in-time date). Six distinct versions were captured between 2020 and December 2025, and the latest was retrieved on 29 October 2026 from the archive.

Language: English.

## Not included yet

- Versions between two captures, and every version before March 2020. The site holds the full history; this record only has what was captured.
- The Act that made each change. The captures do not say which Act amended which section, so every change after the first version is committed by the publisher and labelled unexplained. The site's history notes name the amending Acts but are not in the text here.
- Every New South Wales Act not in the table.

## Dates

Each version is dated by the point-in-time date the NSW legislation website gives for it, which is the day that version came into force. The first version (25 March 2020) is the oldest one captured, not the Act's first text (the Act is from 1902). Commits are dated noon, Australia/Sydney.

## How it is checked

Every version is read back from git on the day it took effect and on the day before; both must match the corpus the repository was built from. The results are in `REPRODUCE.md`.

## How it is built

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `tools/build.py` writes this repository from that file, and the same corpus always gives the same commit hashes; `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file.

## What "author" means

The author of a commit is the law that made the change. Its e-mail address cannot exist, so `git blame` and `git log --author` name laws. A version with no law of its own (the oldest version available) is authored by the publisher and says so. The committer is always Lexifina.
