# New South Wales (Australia): law history in git

The law of New South Wales (Australia) as a git history. Each provision is one file, each law gets one commit on the day it took effect, and the law that made each change is the commit's author. `git blame` names the law behind every paragraph and `git log` lists every change to an article.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `au-nsw/`.

This build holds 432 Acts, 175 regulations and other statutory instruments and 61 environmental planning instruments: every one whose in-force page the Internet Archive captured in 2025 or 2026, as its current text, and for four core Acts the earlier versions captured since 2020.

## What is in it now

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitution-act-1902/` | Constitution Act 1902 No 32 | 6 | Versions in force from 2020-03-25 to 2025-09-17; versions between captures, and earlier ones, are missing |
| `crimes-act-1900/` | Crimes Act 1900 No 40 | 19 | Versions in force from 2020-10-27 to 2025-12-24; versions between captures, and earlier ones, are missing |
| `civil-liability-act-2002/` | Civil Liability Act 2002 No 22 | 3 | Versions in force from 2020-03-01 to 2022-06-16; versions between captures, and earlier ones, are missing |
| `sale-of-goods-act-1923/` | Sale of Goods Act 1923 No 1 | 1 | Versions in force from 2012-01-30 to 2012-01-30; versions between captures, and earlier ones, are missing |
| `royal-society-of-new-south-wales-incorporation-act-private-act-of-1881/` | Royal Society of New South Wales Incorporation Act (Private Act) of 1881 | 1 | Current text: the version in force from 1881-12-16 (newest capture) |
| `compensation-to-relatives-act-1897/` | Compensation to Relatives Act 1897 No 31 | 1 | Current text: the version in force from 2018-06-15 (newest capture) |
| `probate-and-administration-act-1898/` | Probate and Administration Act 1898 No 13 | 1 | Current text: the version in force from 2020-09-28 (newest capture) |
| `oaths-act-1900/` | Oaths Act 1900 No 20 | 1 | Current text: the version in force from 2023-07-14 (newest capture) |
| `real-property-act-1900/` | Real Property Act 1900 No 25 | 1 | Current text: the version in force from 2025-08-15 (newest capture) |
| `inclosed-lands-protection-act-1901/` | Inclosed Lands Protection Act 1901 No 33 | 1 | Current text: the version in force from 2019-11-21 (newest capture) |
| `common-carriers-act-1902/` | Common Carriers Act 1902 No 48 | 1 | Current text: the version in force from 2000-01-01 (newest capture) |
| `piracy-punishment-act-1902/` | Piracy Punishment Act 1902 No 69 | 1 | Current text: the version in force from 1994-12-12 (newest capture) |
| `womens-college-act-1902/` | Women's College Act 1902 No 71 | 1 | Current text: the version in force from 1997-06-27 (newest capture) |
| `seat-of-government-surrender-act-1909/` | Seat of Government Surrender Act 1909 No 14 | 1 | Current text: the version in force from 2007-12-07 (newest capture) |
| `wesley-college-incorporation-act-1910-private-act/` | Wesley College Incorporation Act 1910 (Private Act) | 1 | Current text: the version in force from 2008-08-08 (newest capture) |
| `criminal-appeal-act-1912/` | Criminal Appeal Act 1912 No 16 | 1 | Current text: the version in force from 2025-11-24 (newest capture) |
| `water-act-1912/` | Water Act 1912 No 44 | 1 | Current text: the version in force from 2018-08-01 (newest capture) |
| `public-works-and-procurement-act-1912/` | Public Works and Procurement Act 1912 No 45 | 1 | Current text: the version in force from 2022-06-16 (newest capture) |
| `valuation-of-land-act-1916/` | Valuation of Land Act 1916 No 2 | 1 | Current text: the version in force from 2023-09-04 (newest capture) |
| `conveyancing-act-1919/` | Conveyancing Act 1919 No 6 | 1 | Current text: the version in force from 2025-08-15 (newest capture) |
| `baptist-union-incorporation-act-1919-private-act/` | Baptist Union Incorporation Act 1919 (Private Act) | 1 | Current text: the version in force from 2018-07-01 (newest capture) |
| `border-railways-act-1922/` | Border Railways Act 1922 No 16 | 1 | Current text: the version in force from 2007-12-07 (newest capture) |
| `encroachment-of-buildings-act-1922/` | Encroachment of Buildings Act 1922 No 23 | 1 | Current text: the version in force from 2016-03-01 (newest capture) |
| `royal-commissions-act-1923/` | Royal Commissions Act 1923 No 29 | 1 | Current text: the version in force from 2013-09-12 (newest capture) |
| `trustee-act-1925/` | Trustee Act 1925 No 14 | 1 | Current text: the version in force from 2020-09-28 (newest capture) |
| `moratorium-act-1932/` | Moratorium Act 1932 No 57 | 1 | Current text: the version in force from 2022-06-16 (newest capture) |
| `storage-liens-act-1935/` | Storage Liens Act 1935 No 19 | 1 | Current text: the version in force from 2024-05-31 (newest capture) |
| `soil-conservation-act-1938/` | Soil Conservation Act 1938 No 10 | 1 | Current text: the version in force from 2018-08-01 (newest capture) |
| `library-act-1939/` | Library Act 1939 No 40 | 1 | Current text: the version in force from 2025-10-01 (newest capture) |
| `workers-compensation-dust-diseases-act-1942/` | Workers' Compensation (Dust Diseases) Act 1942 No 14 | 1 | Current text: the version in force from 2022-10-18 (newest capture) |
| `roman-catholic-church-communities-lands-act-1942/` | Roman Catholic Church Communities' Lands Act 1942 No 23 | 1 | Current text: the version in force from 2024-06-28 (newest capture) |
| `restricted-premises-act-1943/` | Restricted Premises Act 1943 No 6 | 1 | Current text: the version in force from 2019-11-22 (newest capture) |
| `law-reform-miscellaneous-provisions-act-1944/` | Law Reform (Miscellaneous Provisions) Act 1944 No 28 | 1 | Current text: the version in force from 2007-12-07 (newest capture) |
| `annual-holidays-act-1944/` | Annual Holidays Act 1944 No 31 | 1 | Current text: the version in force from 2024-07-01 (newest capture) |
| `suitors-fund-act-1951/` | Suitors' Fund Act 1951 No 3 | 1 | Current text: the version in force from 2005-08-15 (newest capture) |
| `lord-howe-island-act-1953/` | Lord Howe Island Act 1953 No 39 | 1 | Current text: the version in force from 2020-10-27 (newest capture) |
| `judges-pensions-act-1953/` | Judges' Pensions Act 1953 No 41 | 1 | Current text: the version in force from 2018-11-28 (newest capture) |
| `long-service-leave-act-1955/` | Long Service Leave Act 1955 No 38 | 1 | Current text: the version in force from 2025-07-01 (newest capture) |
| `land-tax-management-act-1956/` | Land Tax Management Act 1956 No 26 | 1 | Current text: the version in force from 2024-12-02 (newest capture) |
| `land-tax-act-1956/` | Land Tax Act 1956 No 27 | 1 | Current text: the version in force from 2024-12-02 (newest capture) |
| `habitual-criminals-act-1957/` | Habitual Criminals Act 1957 No 19 | 1 | Current text: the version in force from 2009-07-06 (newest capture) |
| `fluoridation-of-public-water-supplies-act-1957/` | Fluoridation of Public Water Supplies Act 1957 No 58 | 1 | Current text: the version in force from 2024-03-01 (newest capture) |
| `land-sales-act-1964/` | Land Sales Act 1964 No 12 | 1 | Current text: the version in force from 2021-10-11 (newest capture) |
| `air-transport-act-1964/` | Air Transport Act 1964 No 36 | 1 | Current text: the version in force from 2016-01-15 (newest capture) |
| `geographical-names-act-1966/` | Geographical Names Act 1966 No 13 | 1 | Current text: the version in force from 2024-08-09 (newest capture) |
| `poisons-and-therapeutic-goods-act-1966/` | Poisons and Therapeutic Goods Act 1966 No 31 | 1 | Current text: the version in force from 2025-11-03 (newest capture) |
| `costs-in-criminal-cases-act-1967/` | Costs in Criminal Cases Act 1967 No 13 | 1 | Current text: the version in force from 2021-03-27 (newest capture) |
| `law-reform-commission-act-1967/` | Law Reform Commission Act 1967 No 39 | 1 | Current text: the version in force from 2015-07-15 (newest capture) |
| `imperial-acts-application-act-1969/` | Imperial Acts Application Act 1969 No 30 | 1 | Current text: the version in force from 2020-09-28 (newest capture) |
| `limitation-act-1969/` | Limitation Act 1969 No 31 | 1 | Current text: the version in force from 2022-06-16 (newest capture) |
| `council-of-law-reporting-act-1969/` | Council of Law Reporting Act 1969 No 59 | 1 | Current text: the version in force from 2024-07-01 (newest capture) |
| `solicitor-general-act-1969/` | Solicitor General Act 1969 No 80 | 1 | Current text: the version in force from 2025-03-02 (newest capture) |
| `supreme-court-act-1970/` | Supreme Court Act 1970 No 52 | 1 | Current text: the version in force from 2024-07-01 (newest capture) |
| `minors-property-and-contracts-act-1970/` | Minors (Property and Contracts) Act 1970 No 60 | 1 | Current text: the version in force from 2015-07-08 (newest capture) |
| `commonwealth-places-administration-of-laws-act-1970/` | Commonwealth Places (Administration of Laws) Act 1970 No 80 | 1 | Current text: the version in force from 1994-12-12 (newest capture) |
| `district-court-act-1973/` | District Court Act 1973 No 9 | 1 | Current text: the version in force from 2025-09-17 (newest capture) |
| `growth-centres-development-corporations-act-1974/` | Growth Centres (Development Corporations) Act 1974 No 49 | 1 | Current text: the version in force from 2023-10-31 (newest capture) |
| `ombudsman-act-1974/` | Ombudsman Act 1974 No 68 | 1 | Current text: the version in force from 2024-11-21 (newest capture) |
| `national-parks-and-wildlife-act-1974/` | National Parks and Wildlife Act 1974 No 80 | 1 | Current text: the version in force from 2025-12-03 (newest capture) |
| `anglican-church-of-australia-act-1976/` | Anglican Church of Australia Act 1976 No 21 | 1 | Current text: the version in force from 2003-11-27 (newest capture) |
| `registered-clubs-act-1976/` | Registered Clubs Act 1976 No 31 | 1 | Current text: the version in force from 2024-10-31 (newest capture) |
| `parents-and-citizens-associations-incorporation-act-1976/` | Parents and Citizens Associations Incorporation Act 1976 No 50 | 1 | Current text: the version in force from 2018-07-01 (newest capture) |
| `restraints-of-trade-act-1976/` | Restraints of Trade Act 1976 No 67 | 1 | Current text: the version in force from 2015-01-08 (newest capture) |
| `jury-act-1977/` | Jury Act 1977 No 18 | 1 | Current text: the version in force from 2025-03-10 (newest capture) |
| `animals-act-1977/` | Animals Act 1977 No 25 | 1 | Current text: the version in force from 2017-11-23 (newest capture) |
| `fellowship-of-congregational-churches-new-south-wales-incorporation-act-1977/` | Fellowship of Congregational Churches (New South Wales) Incorporation Act 1977 No 39 | 1 | Current text: the version in force from 1987-09-01 (newest capture) |
| `uniting-church-in-australia-act-1977/` | Uniting Church in Australia Act 1977 No 47 | 1 | Current text: the version in force from 2008-07-01 (newest capture) |
| `anti-discrimination-act-1977/` | Anti-Discrimination Act 1977 No 48 | 1 | Current text: the version in force from 2024-07-01 (newest capture) |
| `anatomy-act-1977/` | Anatomy Act 1977 No 126 | 1 | Current text: the version in force from 2018-06-15 (newest capture) |
| `heritage-act-1977/` | Heritage Act 1977 No 136 | 1 | Current text: the version in force from 2024-11-21 (newest capture) |
| `frustrated-contracts-act-1978/` | Frustrated Contracts Act 1978 No 105 | 1 | Current text: the version in force from 2015-01-08 (newest capture) |
| `funeral-funds-act-1979/` | Funeral Funds Act 1979 No 106 | 1 | Current text: the version in force from 2024-07-01 (newest capture) |
| `domicile-act-1979/` | Domicile Act 1979 No 118 | 1 | Current text: the version in force from 1997-03-03 (newest capture) |
| `prevention-of-cruelty-to-animals-act-1979/` | Prevention of Cruelty to Animals Act 1979 No 200 | 1 | Current text: the version in force from 2025-12-01 (newest capture) |
| `environmental-planning-and-assessment-act-1979/` | Environmental Planning and Assessment Act 1979 No 203 | 1 | Current text: the version in force from 2025-12-15 (newest capture) |
| `land-and-environment-court-act-1979/` | Land and Environment Court Act 1979 No 204 | 1 | Current text: the version in force from 2025-11-24 (newest capture) |
| `contracts-review-act-1980/` | Contracts Review Act 1980 No 16 | 1 | Current text: the version in force from 2021-12-01 (newest capture) |
| `royal-botanic-gardens-and-domain-trust-act-1980/` | Royal Botanic Gardens and Domain Trust Act 1980 No 19 | 1 | Current text: the version in force from 2024-12-02 (newest capture) |
| `teaching-service-act-1980/` | Teaching Service Act 1980 No 23 | 1 | Current text: the version in force from 2024-07-01 (newest capture) |
| `art-gallery-of-new-south-wales-act-1980/` | Art Gallery of New South Wales Act 1980 No 65 | 1 | Current text: the version in force from 2025-10-01 (newest capture) |
| `felons-civil-proceedings-act-1981/` | Felons (Civil Proceedings) Act 1981 No 84 | 1 | Current text: the version in force from 2000-01-01 (newest capture) |
| `prisoners-interstate-transfer-act-1982/` | Prisoners (Interstate Transfer) Act 1982 No 104 | 1 | Current text: the version in force from 2025-03-02 (newest capture) |
| `health-administration-act-1982/` | Health Administration Act 1982 No 135 | 1 | Current text: the version in force from 2023-10-30 (newest capture) |
| `forestry-revocation-and-national-parks-reservation-act-1983/` | Forestry Revocation and National Parks Reservation Act 1983 No 37 | 1 | Current text: the version in force from 2018-07-01 (newest capture) |
| `aboriginal-land-rights-act-1983/` | Aboriginal Land Rights Act 1983 No 42 | 1 | Current text: the version in force from 2024-12-11 (newest capture) |
| `lie-detectors-act-1983/` | Lie Detectors Act 1983 No 62 | 1 | Current text: the version in force from 2009-07-06 (newest capture) |
| `special-commissions-of-inquiry-act-1983/` | Special Commissions of Inquiry Act 1983 No 90 | 1 | Current text: the version in force from 2015-07-08 (newest capture) |
| `government-sector-audit-act-1983/` | Government Sector Audit Act 1983 No 152 | 1 | Current text: the version in force from 2025-07-03 (newest capture) |
| `human-tissue-act-1983/` | Human Tissue Act 1983 No 164 | 1 | Current text: the version in force from 2025-10-12 (newest capture) |
| `racing-appeals-tribunal-act-1983/` | Racing Appeals Tribunal Act 1983 No 199 | 1 | Current text: the version in force from 2022-12-16 (newest capture) |
| `perpetuities-act-1984/` | Perpetuities Act 1984 No 43 | 1 | Current text: the version in force from 1984-10-31 (newest capture) |
| `property-relationships-act-1984/` | Property (Relationships) Act 1984 No 147 | 1 | Current text: the version in force from 2023-07-14 (newest capture) |
| `motor-vehicle-sports-public-safety-act-1985/` | Motor Vehicle Sports (Public Safety) Act 1985 No 24 | 1 | Current text: the version in force from 2023-01-13 (newest capture) |
| `animal-research-act-1985/` | Animal Research Act 1985 No 123 | 1 | Current text: the version in force from 2025-08-15 (newest capture) |
| `biological-control-act-1985/` | Biological Control Act 1985 No 199 | 1 | Current text: the version in force from 2025-07-03 (newest capture) |
| `drug-misuse-and-trafficking-act-1985/` | Drug Misuse and Trafficking Act 1985 No 226 | 1 | Current text: the version in force from 2024-12-01 (newest capture) |
| `insurance-application-of-laws-act-1986/` | Insurance (Application of Laws) Act 1986 No 13 | 1 | Current text: the version in force from 2009-07-06 (newest capture) |
| `building-and-construction-industry-long-service-payments-act-1986/` | Building and Construction Industry Long Service Payments Act 1986 No 19 | 1 | Current text: the version in force from 2024-11-21 (newest capture) |
| `judicial-officers-act-1986/` | Judicial Officers Act 1986 No 100 | 1 | Current text: the version in force from 2024-07-01 (newest capture) |
| `exhibited-animals-protection-act-1986/` | Exhibited Animals Protection Act 1986 No 123 | 1 | Current text: the version in force from 2024-07-01 (newest capture) |
| `uranium-mining-and-nuclear-facilities-prohibitions-act-1986/` | Uranium Mining and Nuclear Facilities (Prohibitions) Act 1986 No 194 | 1 | Current text: the version in force from 2023-10-24 (newest capture) |
| `director-of-public-prosecutions-act-1986/` | Director of Public Prosecutions Act 1986 No 207 | 1 | Current text: the version in force from 2022-10-18 (newest capture) |
| `criminal-procedure-act-1986/` | Criminal Procedure Act 1986 No 209 | 1 | Current text: the version in force from 2025-05-01 (newest capture) |
| `interpretation-act-1987/` | Interpretation Act 1987 No 15 | 1 | Current text: the version in force from 2024-11-21 (newest capture) |
| `sydney-harbour-tunnel-private-joint-venture-act-1987/` | Sydney Harbour Tunnel (Private Joint Venture) Act 1987 No 49 | 1 | Current text: the version in force from 2025-07-03 (newest capture) |
| `community-welfare-act-1987/` | Community Welfare Act 1987 No 52 | 1 | Current text: the version in force from 2024-07-01 (newest capture) |
| `childrens-court-act-1987/` | Children's Court Act 1987 No 53 | 1 | Current text: the version in force from 2018-04-30 (newest capture) |
| `children-criminal-proceedings-act-1987/` | Children (Criminal Proceedings) Act 1987 No 55 | 1 | Current text: the version in force from 2025-10-28 (newest capture) |
| `children-community-service-orders-act-1987/` | Children (Community Service Orders) Act 1987 No 56 | 1 | Current text: the version in force from 2024-11-21 (newest capture) |
| `children-detention-centres-act-1987/` | Children (Detention Centres) Act 1987 No 57 | 1 | Current text: the version in force from 2025-03-02 (newest capture) |
| `fair-trading-act-1987/` | Fair Trading Act 1987 No 68 | 1 | Current text: the version in force from 2025-07-01 (newest capture) |
| `workers-compensation-act-1987/` | Workers Compensation Act 1987 No 70 | 1 | Current text: the version in force from 2025-07-01 (newest capture) |
| `energy-and-utilities-administration-act-1987/` | Energy and Utilities Administration Act 1987 No 103 | 1 | Current text: the version in force from 2024-11-21 (newest capture) |
| `standard-time-act-1987/` | Standard Time Act 1987 No 149 | 1 | Current text: the version in force from 2007-11-01 (newest capture) |
| `wilderness-act-1987/` | Wilderness Act 1987 No 196 | 1 | Current text: the version in force from 2018-07-01 (newest capture) |
| `education-school-administrative-and-support-staff-act-1987/` | Education (School Administrative and Support Staff) Act 1987 No 240 | 1 | Current text: the version in force from 2023-10-01 (newest capture) |
| `guardianship-act-1987/` | Guardianship Act 1987 No 257 | 1 | Current text: the version in force from 2021-03-27 (newest capture) |
| `summary-offences-act-1988/` | Summary Offences Act 1988 No 25 | 1 | Current text: the version in force from 2025-11-26 (newest capture) |
| `independent-commission-against-corruption-act-1988/` | Independent Commission Against Corruption Act 1988 No 35 | 1 | Current text: the version in force from 2025-11-24 (newest capture) |
| `city-of-sydney-act-1988/` | City of Sydney Act 1988 No 48 | 1 | Current text: the version in force from 2023-09-27 (newest capture) |
| `crown-proceedings-act-1988/` | Crown Proceedings Act 1988 No 70 | 1 | Current text: the version in force from 1999-12-03 (newest capture) |
| `motor-accidents-act-1988/` | Motor Accidents Act 1988 No 102 | 1 | Current text: the version in force from 2021-01-22 (newest capture) |
| `transport-administration-act-1988/` | Transport Administration Act 1988 No 109 | 1 | Current text: the version in force from 2025-10-28 (newest capture) |
| `dust-diseases-tribunal-act-1989/` | Dust Diseases Tribunal Act 1989 No 63 | 1 | Current text: the version in force from 2024-11-15 (newest capture) |
| `higher-education-amalgamation-act-1989/` | Higher Education (Amalgamation) Act 1989 No 65 | 1 | Current text: the version in force from 2006-06-20 (newest capture) |
| `university-of-newcastle-act-1989/` | University of Newcastle Act 1989 No 68 | 1 | Current text: the version in force from 2024-09-30 (newest capture) |
| `confiscation-of-proceeds-of-crime-act-1989/` | Confiscation of Proceeds of Crime Act 1989 No 90 | 1 | Current text: the version in force from 2023-02-01 (newest capture) |
| `rural-assistance-act-1989/` | Rural Assistance Act 1989 No 97 | 1 | Current text: the version in force from 2023-01-13 (newest capture) |
| `university-of-sydney-act-1989/` | University of Sydney Act 1989 No 124 | 1 | Current text: the version in force from 2024-09-30 (newest capture) |
| `university-of-new-south-wales-act-1989/` | University of New South Wales Act 1989 No 125 | 1 | Current text: the version in force from 2024-09-30 (newest capture) |
| `university-of-wollongong-act-1989/` | University of Wollongong Act 1989 No 127 | 1 | Current text: the version in force from 2024-09-30 (newest capture) |
| `state-owned-corporations-act-1989/` | State Owned Corporations Act 1989 No 134 | 1 | Current text: the version in force from 2025-01-01 (newest capture) |
| `subordinate-legislation-act-1989/` | Subordinate Legislation Act 1989 No 146 | 1 | Current text: the version in force from 2026-02-18 (newest capture) |
| `home-building-act-1989/` | Home Building Act 1989 No 147 | 1 | Current text: the version in force from 2024-08-20 (newest capture) |
| `parliamentary-remuneration-act-1989/` | Parliamentary Remuneration Act 1989 No 160 | 1 | Current text: the version in force from 2025-08-13 (newest capture) |
| `state-emergency-service-act-1989/` | State Emergency Service Act 1989 No 164 | 1 | Current text: the version in force from 2023-07-01 (newest capture) |
| `state-emergency-and-rescue-management-act-1989/` | State Emergency and Rescue Management Act 1989 No 165 | 1 | Current text: the version in force from 2025-01-01 (newest capture) |
| `stock-medicines-act-1989/` | Stock Medicines Act 1989 No 182 | 1 | Current text: the version in force from 2025-12-12 (newest capture) |
| `education-act-1990/` | Education Act 1990 No 8 | 1 | Current text: the version in force from 2020-12-11 (newest capture) |
| `protection-from-harmful-radiation-act-1990/` | Protection from Harmful Radiation Act 1990 No 13 | 1 | Current text: the version in force from 2025-12-12 (newest capture) |
| `criminal-assets-recovery-act-1990/` | Criminal Assets Recovery Act 1990 No 23 | 1 | Current text: the version in force from 2023-02-01 (newest capture) |
| `passenger-transport-act-1990/` | Passenger Transport Act 1990 No 39 | 1 | Current text: the version in force from 2025-11-26 (newest capture) |
| `luna-park-site-act-1990/` | Luna Park Site Act 1990 No 59 | 1 | Current text: the version in force from 2018-07-01 (newest capture) |
| `agricultural-tenancies-act-1990/` | Agricultural Tenancies Act 1990 No 64 | 1 | Current text: the version in force from 2024-05-31 (newest capture) |
| `national-trust-of-australia-new-south-wales-act-1990/` | National Trust of Australia (New South Wales) Act 1990 No 92 | 1 | Current text: the version in force from 2021-07-01 (newest capture) |
| `technical-and-further-education-commission-act-1990/` | Technical and Further Education Commission Act 1990 No 118 | 1 | Current text: the version in force from 2021-07-01 (newest capture) |
| `employees-liability-act-1991/` | Employees Liability Act 1991 No 4 | 1 | Current text: the version in force from 2004-01-01 (newest capture) |
| `criminal-records-act-1991/` | Criminal Records Act 1991 No 8 | 1 | Current text: the version in force from 2020-09-28 (newest capture) |
| `land-acquisition-just-terms-compensation-act-1991/` | Land Acquisition (Just Terms Compensation) Act 1991 No 22 | 1 | Current text: the version in force from 2024-07-05 (newest capture) |
| `hunter-water-act-1991/` | Hunter Water Act 1991 No 53 | 1 | Current text: the version in force from 2024-03-01 (newest capture) |
| `protection-of-the-environment-administration-act-1991/` | Protection of the Environment Administration Act 1991 No 60 | 1 | Current text: the version in force from 2025-12-12 (newest capture) |
| `charitable-fundraising-act-1991/` | Charitable Fundraising Act 1991 No 69 | 1 | Current text: the version in force from 2024-08-20 (newest capture) |
| `dividing-fences-act-1991/` | Dividing Fences Act 1991 No 72 | 1 | Current text: the version in force from 2018-07-01 (newest capture) |
| `driving-instructors-act-1992/` | Driving Instructors Act 1992 No 3 | 1 | Current text: the version in force from 2021-01-22 (newest capture) |
| `casino-control-act-1992/` | Casino Control Act 1992 No 15 | 1 | Current text: the version in force from 2024-08-20 (newest capture) |
| `mining-act-1992/` | Mining Act 1992 No 29 | 1 | Current text: the version in force from 2025-07-01 (newest capture) |
| `independent-pricing-and-regulatory-tribunal-act-1992/` | Independent Pricing and Regulatory Tribunal Act 1992 No 39 | 1 | Current text: the version in force from 2024-08-15 (newest capture) |
| `swimming-pools-act-1992/` | Swimming Pools Act 1992 No 49 | 1 | Current text: the version in force from 2024-08-20 (newest capture) |
| `mutual-recognition-new-south-wales-act-1992/` | Mutual Recognition (New South Wales) Act 1992 No 61 | 1 | Current text: the version in force from 2021-06-23 (newest capture) |
| `community-services-complaints-reviews-and-monitoring-act-1993/` | Community Services (Complaints, Reviews and Monitoring) Act 1993 No 2 | 1 | Current text: the version in force from 2024-08-20 (newest capture) |
| `charitable-trusts-act-1993/` | Charitable Trusts Act 1993 No 10 | 1 | Current text: the version in force from 2006-11-27 (newest capture) |
| `local-government-act-1993/` | Local Government Act 1993 No 30 | 1 | Current text: the version in force from 2025-11-24 (newest capture) |
| `roads-act-1993/` | Roads Act 1993 No 33 | 1 | Current text: the version in force from 2025-10-28 (newest capture) |
| `native-title-new-south-wales-act-1994/` | Native Title (New South Wales) Act 1994 No 45 | 1 | Current text: the version in force from 2024-05-31 (newest capture) |
| `retail-leases-act-1994/` | Retail Leases Act 1994 No 46 | 1 | Current text: the version in force from 2025-08-15 (newest capture) |
| `state-bank-privatisation-act-1994/` | State Bank (Privatisation) Act 1994 No 73 | 1 | Current text: the version in force from 1999-12-03 (newest capture) |
| `professional-standards-act-1994/` | Professional Standards Act 1994 No 81 | 1 | Current text: the version in force from 2017-06-27 (newest capture) |
| `sydney-water-act-1994/` | Sydney Water Act 1994 No 88 | 1 | Current text: the version in force from 2024-11-21 (newest capture) |
| `public-interest-disclosures-act-1994/` | Public Interest Disclosures Act 1994 No 92 | 1 | Current text: the version in force from 2023-01-13 (newest capture) |
| `ports-and-maritime-administration-act-1995/` | Ports and Maritime Administration Act 1995 No 13 | 1 | Current text: the version in force from 2025-03-02 (newest capture) |
| `evidence-act-1995/` | Evidence Act 1995 No 25 | 1 | Current text: the version in force from 2022-11-25 (newest capture) |
| `evidence-on-commission-act-1995/` | Evidence on Commission Act 1995 No 26 | 1 | Current text: the version in force from 2024-07-01 (newest capture) |
| `births-deaths-and-marriages-registration-act-1995/` | Births, Deaths and Marriages Registration Act 1995 No 62 | 1 | Current text: the version in force from 2025-07-01 (newest capture) |
| `classification-publications-films-and-computer-games-enforcement-act-1995/` | Classification (Publications, Films and Computer Games) Enforcement Act 1995 No 63 | 1 | Current text: the version in force from 2017-07-07 (newest capture) |
| `forfeiture-act-1995/` | Forfeiture Act 1995 No 65 | 1 | Current text: the version in force from 2021-03-27 (newest capture) |
| `uncollected-goods-act-1995/` | Uncollected Goods Act 1995 No 68 | 1 | Current text: the version in force from 2025-07-01 (newest capture) |
| `unclaimed-money-act-1995/` | Unclaimed Money Act 1995 No 75 | 1 | Current text: the version in force from 2025-07-02 (newest capture) |
| `electricity-supply-act-1995/` | Electricity Supply Act 1995 No 94 | 1 | Current text: the version in force from 2025-12-01 (newest capture) |
| `pawnbrokers-and-second-hand-dealers-act-1996/` | Pawnbrokers and Second-hand Dealers Act 1996 No 13 | 1 | Current text: the version in force from 2024-08-20 (newest capture) |
| `industrial-relations-act-1996/` | Industrial Relations Act 1996 No 17 | 1 | Current text: the version in force from 2025-11-26 (newest capture) |
| `thoroughbred-racing-act-1996/` | Thoroughbred Racing Act 1996 No 37 | 1 | Current text: the version in force from 2021-11-01 (newest capture) |
| `gas-supply-act-1996/` | Gas Supply Act 1996 No 38 | 1 | Current text: the version in force from 2025-04-09 (newest capture) |
| `firearms-act-1996/` | Firearms Act 1996 No 46 | 1 | Current text: the version in force from 2026-07-01 (newest capture) |
| `hawkesbury-racecourse-act-1996/` | Hawkesbury Racecourse Act 1996 No 74 | 1 | Current text: the version in force from 2018-07-01 (newest capture) |
| `status-of-children-act-1996/` | Status of Children Act 1996 No 76 | 1 | Current text: the version in force from 2025-03-02 (newest capture) |
| `public-lotteries-act-1996/` | Public Lotteries Act 1996 No 86 | 1 | Current text: the version in force from 2023-01-13 (newest capture) |
| `taxation-administration-act-1996/` | Taxation Administration Act 1996 No 97 | 1 | Current text: the version in force from 2024-12-02 (newest capture) |
| `fines-act-1996/` | Fines Act 1996 No 99 | 1 | Current text: the version in force from 2025-03-02 (newest capture) |
| `forestry-revocation-and-national-park-reservation-act-1996/` | Forestry Revocation and National Park Reservation Act 1996 No 131 | 1 | Current text: the version in force from 2018-07-01 (newest capture) |
| `national-electricity-new-south-wales-act-1997/` | National Electricity (New South Wales) Act 1997 No 20 | 1 | Current text: the version in force from 2015-06-04 (newest capture) |
| `totalizator-agency-board-privatisation-act-1997/` | Totalizator Agency Board Privatisation Act 1997 No 43 | 1 | Current text: the version in force from 2021-07-01 (newest capture) |
| `totalizator-act-1997/` | Totalizator Act 1997 No 45 | 1 | Current text: the version in force from 2023-01-13 (newest capture) |
| `young-offenders-act-1997/` | Young Offenders Act 1997 No 54 | 1 | Current text: the version in force from 2020-10-27 (newest capture) |
| `rural-fires-act-1997/` | Rural Fires Act 1997 No 65 | 1 | Current text: the version in force from 2025-10-28 (newest capture) |
| `administrative-decisions-review-act-1997/` | Administrative Decisions Review Act 1997 No 76 | 1 | Current text: the version in force from 2014-01-01 (newest capture) |
| `children-protection-and-parental-responsibility-act-1997/` | Children (Protection and Parental Responsibility) Act 1997 No 78 | 1 | Current text: the version in force from 2022-11-25 (newest capture) |
| `sea-carriage-documents-act-1997/` | Sea-Carriage Documents Act 1997 No 92 | 1 | Current text: the version in force from 1997-11-04 (newest capture) |
| `public-notaries-act-1997/` | Public Notaries Act 1997 No 98 | 1 | Current text: the version in force from 2015-07-01 (newest capture) |
| `snowy-hydro-corporatisation-act-1997/` | Snowy Hydro Corporatisation Act 1997 No 99 | 1 | Current text: the version in force from 2022-01-21 (newest capture) |
| `contractors-debts-act-1997/` | Contractors Debts Act 1997 No 110 | 1 | Current text: the version in force from 2009-07-06 (newest capture) |
| `western-sydney-university-act-1997/` | Western Sydney University Act 1997 No 116 | 1 | Current text: the version in force from 2024-09-30 (newest capture) |
| `duties-act-1997/` | Duties Act 1997 No 123 | 1 | Current text: the version in force from 2025-01-01 (newest capture) |
| `law-enforcement-controlled-operations-act-1997/` | Law Enforcement (Controlled Operations) Act 1997 No 136 | 1 | Current text: the version in force from 2019-10-28 (newest capture) |
| `contaminated-land-management-act-1997/` | Contaminated Land Management Act 1997 No 140 | 1 | Current text: the version in force from 2025-12-12 (newest capture) |
| `health-services-act-1997/` | Health Services Act 1997 No 154 | 1 | Current text: the version in force from 2025-07-01 (newest capture) |
| `protection-of-the-environment-operations-act-1997/` | Protection of the Environment Operations Act 1997 No 156 | 1 | Current text: the version in force from 2025-10-28 (newest capture) |
| `security-industry-act-1997/` | Security Industry Act 1997 No 157 | 1 | Current text: the version in force from 2023-10-30 (newest capture) |
| `saint-andrews-college-act-1998/` | Saint Andrew's College Act 1998 No 15 | 1 | Current text: the version in force from 2018-07-01 (newest capture) |
| `state-records-act-1998/` | State Records Act 1998 No 17 | 1 | Current text: the version in force from 2024-01-01 (newest capture) |
| `aboriginal-housing-act-1998/` | Aboriginal Housing Act 1998 No 47 | 1 | Current text: the version in force from 2021-07-01 (newest capture) |
| `workplace-injury-management-and-workers-compensation-act-1998/` | Workplace Injury Management and Workers Compensation Act 1998 No 86 | 1 | Current text: the version in force from 2024-07-01 (newest capture) |
| `companion-animals-act-1998/` | Companion Animals Act 1998 No 87 | 1 | Current text: the version in force from 2024-11-21 (newest capture) |
| `evidence-audio-and-audio-visual-links-act-1998/` | Evidence (Audio and Audio Visual Links) Act 1998 No 105 | 1 | Current text: the version in force from 2024-10-11 (newest capture) |
| `tow-truck-industry-act-1998/` | Tow Truck Industry Act 1998 No 111 | 1 | Current text: the version in force from 2024-08-20 (newest capture) |
| `unlawful-gambling-act-1998/` | Unlawful Gambling Act 1998 No 113 | 1 | Current text: the version in force from 2020-07-01 (newest capture) |
| `betting-and-racing-act-1998/` | Betting and Racing Act 1998 No 114 | 1 | Current text: the version in force from 2023-01-13 (newest capture) |
| `gambling-two-up-act-1998/` | Gambling (Two-up) Act 1998 No 115 | 1 | Current text: the version in force from 2018-04-03 (newest capture) |
| `marine-safety-act-1998/` | Marine Safety Act 1998 No 121 | 1 | Current text: the version in force from 2025-03-02 (newest capture) |
| `weapons-prohibition-act-1998/` | Weapons Prohibition Act 1998 No 127 | 1 | Current text: the version in force from 2025-09-29 (newest capture) |
| `privacy-and-personal-information-protection-act-1998/` | Privacy and Personal Information Protection Act 1998 No 133 | 1 | Current text: the version in force from 2024-11-21 (newest capture) |
| `drug-court-act-1998/` | Drug Court Act 1998 No 150 | 1 | Current text: the version in force from 2020-12-11 (newest capture) |
| `children-and-young-persons-care-and-protection-act-1998/` | Children and Young Persons (Care and Protection) Act 1998 No 157 | 1 | Current text: the version in force from 2025-10-28 (newest capture) |
| `motor-accidents-compensation-act-1999/` | Motor Accidents Compensation Act 1999 No 41 | 1 | Current text: the version in force from 2022-06-16 (newest capture) |
| `building-and-construction-industry-security-of-payment-act-1999/` | Building and Construction Industry Security of Payment Act 1999 No 46 | 1 | Current text: the version in force from 2024-08-20 (newest capture) |
| `pesticides-act-1999/` | Pesticides Act 1999 No 80 | 1 | Current text: the version in force from 2025-12-12 (newest capture) |
| `retirement-villages-act-1999/` | Retirement Villages Act 1999 No 81 | 1 | Current text: the version in force from 2025-08-15 (newest capture) |
| `crimes-sentencing-procedure-act-1999/` | Crimes (Sentencing Procedure) Act 1999 No 92 | 1 | Current text: the version in force from 2025-11-24 (newest capture) |
| `crimes-administration-of-sentences-act-1999/` | Crimes (Administration of Sentences) Act 1999 No 93 | 1 | Current text: the version in force from 2025-12-12 (newest capture) |
| `plantations-and-reafforestation-act-1999/` | Plantations and Reafforestation Act 1999 No 97 | 1 | Current text: the version in force from 2023-07-14 (newest capture) |
| `access-to-neighbouring-land-act-2000/` | Access to Neighbouring Land Act 2000 No 2 | 1 | Current text: the version in force from 2009-07-06 (newest capture) |
| `electronic-transactions-act-2000/` | Electronic Transactions Act 2000 No 8 | 1 | Current text: the version in force from 2021-11-29 (newest capture) |
| `first-home-owner-grant-and-shared-equity-act-2000/` | First Home Owner Grant and Shared Equity Act 2000 No 21 | 1 | Current text: the version in force from 2025-12-03 (newest capture) |
| `child-protection-offenders-registration-act-2000/` | Child Protection (Offenders Registration) Act 2000 No 42 | 1 | Current text: the version in force from 2025-09-29 (newest capture) |
| `crimes-forensic-procedures-act-2000/` | Crimes (Forensic Procedures) Act 2000 No 59 | 1 | Current text: the version in force from 2023-10-30 (newest capture) |
| `smoke-free-environment-act-2000/` | Smoke-free Environment Act 2000 No 69 | 1 | Current text: the version in force from 2024-12-02 (newest capture) |
| `adoption-act-2000/` | Adoption Act 2000 No 75 | 1 | Current text: the version in force from 2023-10-30 (newest capture) |
| `multicultural-nsw-act-2000/` | Multicultural NSW Act 2000 No 77 | 1 | Current text: the version in force from 2021-07-01 (newest capture) |
| `water-management-act-2000/` | Water Management Act 2000 No 92 | 1 | Current text: the version in force from 2023-07-01 (newest capture) |
| `corporations-commonwealth-powers-act-2001/` | Corporations (Commonwealth Powers) Act 2001 No 1 | 1 | Current text: the version in force from 2010-01-08 (newest capture) |
| `parramatta-park-trust-act-2001/` | Parramatta Park Trust Act 2001 No 17 | 1 | Current text: the version in force from 2022-07-01 (newest capture) |
| `health-care-liability-act-2001/` | Health Care Liability Act 2001 No 42 | 1 | Current text: the version in force from 2023-07-14 (newest capture) |
| `betting-tax-act-2001/` | Betting Tax Act 2001 No 43 | 1 | Current text: the version in force from 2022-07-01 (newest capture) |
| `housing-act-2001/` | Housing Act 2001 No 52 | 1 | Current text: the version in force from 2025-03-02 (newest capture) |
| `sydney-olympic-park-authority-act-2001/` | Sydney Olympic Park Authority Act 2001 No 57 | 1 | Current text: the version in force from 2025-08-15 (newest capture) |
| `waste-avoidance-and-resource-recovery-act-2001/` | Waste Avoidance and Resource Recovery Act 2001 No 58 | 1 | Current text: the version in force from 2025-12-12 (newest capture) |
| `gaming-machine-tax-act-2001/` | Gaming Machine Tax Act 2001 No 72 | 1 | Current text: the version in force from 2021-11-29 (newest capture) |
| `apprenticeship-and-traineeship-act-2001/` | Apprenticeship and Traineeship Act 2001 No 80 | 1 | Current text: the version in force from 2018-06-29 (newest capture) |
| `higher-education-act-2001/` | Higher Education Act 2001 No 102 | 1 | Current text: the version in force from 2017-06-08 (newest capture) |
| `crimes-appeal-and-review-act-2001/` | Crimes (Appeal and Review) Act 2001 No 120 | 1 | Current text: the version in force from 2025-11-24 (newest capture) |
| `gaming-machines-act-2001/` | Gaming Machines Act 2001 No 127 | 1 | Current text: the version in force from 2023-01-13 (newest capture) |
| `industrial-relations-ethical-clothing-trades-act-2001/` | Industrial Relations (Ethical Clothing Trades) Act 2001 No 128 | 1 | Current text: the version in force from 2019-01-08 (newest capture) |
| `landcom-corporation-act-2001/` | Landcom Corporation Act 2001 No 129 | 1 | Current text: the version in force from 2016-01-15 (newest capture) |
| `property-and-stock-agents-act-2002/` | Property and Stock Agents Act 2002 No 66 | 1 | Current text: the version in force from 2025-08-15 (newest capture) |
| `health-records-and-information-privacy-act-2002/` | Health Records and Information Privacy Act 2002 No 71 | 1 | Current text: the version in force from 2024-05-27 (newest capture) |
| `surveying-and-spatial-information-act-2002/` | Surveying and Spatial Information Act 2002 No 83 | 1 | Current text: the version in force from 2024-08-20 (newest capture) |
| `holiday-parks-long-term-casual-occupation-act-2002/` | Holiday Parks (Long-term Casual Occupation) Act 2002 No 88 | 1 | Current text: the version in force from 2024-05-31 (newest capture) |
| `law-enforcement-powers-and-responsibilities-act-2002/` | Law Enforcement (Powers and Responsibilities) Act 2002 No 103 | 1 | Current text: the version in force from 2025-12-03 (newest capture) |
| `terrorism-police-powers-act-2002/` | Terrorism (Police Powers) Act 2002 No 115 | 1 | Current text: the version in force from 2025-12-24 (newest capture) |
| `callan-park-special-provisions-act-2002/` | Callan Park (Special Provisions) Act 2002 No 139 | 1 | Current text: the version in force from 2022-07-01 (newest capture) |
| `conveyancers-licensing-act-2003/` | Conveyancers Licensing Act 2003 No 3 | 1 | Current text: the version in force from 2025-08-15 (newest capture) |
| `gene-technology-new-south-wales-act-2003/` | Gene Technology (New South Wales) Act 2003 No 11 | 1 | Current text: the version in force from 2012-01-06 (newest capture) |
| `explosives-act-2003/` | Explosives Act 2003 No 39 | 1 | Current text: the version in force from 2025-08-15 (newest capture) |
| `food-act-2003/` | Food Act 2003 No 43 | 1 | Current text: the version in force from 2024-08-09 (newest capture) |
| `commonwealth-powers-de-facto-relationships-act-2003/` | Commonwealth Powers (De Facto Relationships) Act 2003 No 49 | 1 | Current text: the version in force from 2010-01-08 (newest capture) |
| `powers-of-attorney-act-2003/` | Powers of Attorney Act 2003 No 53 | 1 | Current text: the version in force from 2025-03-02 (newest capture) |
| `hairdressers-act-2003/` | Hairdressers Act 2003 No 62 | 1 | Current text: the version in force from 2019-12-05 (newest capture) |
| `architects-act-2003/` | Architects Act 2003 No 89 | 1 | Current text: the version in force from 2021-07-01 (newest capture) |
| `natural-resources-commission-act-2003/` | Natural Resources Commission Act 2003 No 102 | 1 | Current text: the version in force from 2023-10-30 (newest capture) |
| `state-arms-symbols-and-emblems-act-2004/` | State Arms, Symbols and Emblems Act 2004 No 1 | 1 | Current text: the version in force from 2015-10-22 (newest capture) |
| `wool-hide-and-skin-dealers-act-2004/` | Wool, Hide and Skin Dealers Act 2004 No 7 | 1 | Current text: the version in force from 2020-12-11 (newest capture) |
| `snowy-mountains-cloud-seeding-act-2004/` | Snowy Mountains Cloud Seeding Act 2004 No 19 | 1 | Current text: the version in force from 2026-06-10 (newest capture) |
| `filming-approval-act-2004/` | Filming Approval Act 2004 No 38 | 1 | Current text: the version in force from 2014-12-19 (newest capture) |
| `child-protection-offenders-prohibition-orders-act-2004/` | Child Protection (Offenders Prohibition Orders) Act 2004 No 46 | 1 | Current text: the version in force from 2018-01-19 (newest capture) |
| `regional-development-act-2004/` | Regional Development Act 2004 No 58 | 1 | Current text: the version in force from 2024-09-30 (newest capture) |
| `teacher-accreditation-act-2004/` | Teacher Accreditation Act 2004 No 65 | 1 | Current text: the version in force from 2021-11-29 (newest capture) |
| `sheriff-act-2005/` | Sheriff Act 2005 No 6 | 1 | Current text: the version in force from 2024-02-19 (newest capture) |
| `water-efficiency-labelling-and-standards-new-south-wales-act-2005/` | Water Efficiency Labelling and Standards (New South Wales) Act 2005 No 12 | 1 | Current text: the version in force from 2025-07-03 (newest capture) |
| `photo-card-act-2005/` | Photo Card Act 2005 No 20 | 1 | Current text: the version in force from 2024-11-21 (newest capture) |
| `civil-procedure-act-2005/` | Civil Procedure Act 2005 No 28 | 1 | Current text: the version in force from 2025-09-17 (newest capture) |
| `workplace-surveillance-act-2005/` | Workplace Surveillance Act 2005 No 47 | 1 | Current text: the version in force from 2024-07-01 (newest capture) |
| `defamation-act-2005/` | Defamation Act 2005 No 77 | 1 | Current text: the version in force from 2025-03-02 (newest capture) |
| `mine-and-petroleum-site-safety-cost-recovery-act-2005/` | Mine and Petroleum Site Safety (Cost Recovery) Act 2005 No 116 | 1 | Current text: the version in force from 2023-01-13 (newest capture) |
| `crimes-high-risk-offenders-act-2006/` | Crimes (High Risk Offenders) Act 2006 No 7 | 1 | Current text: the version in force from 2024-06-21 (newest capture) |
| `succession-act-2006/` | Succession Act 2006 No 80 | 1 | Current text: the version in force from 2023-07-14 (newest capture) |
| `trees-disputes-between-neighbours-act-2006/` | Trees (Disputes Between Neighbours) Act 2006 No 126 | 1 | Current text: the version in force from 2025-03-02 (newest capture) |
| `drug-and-alcohol-treatment-act-2007/` | Drug and Alcohol Treatment Act 2007 No 7 | 1 | Current text: the version in force from 2025-06-11 (newest capture) |
| `mental-health-act-2007/` | Mental Health Act 2007 No 8 | 1 | Current text: the version in force from 2025-10-28 (newest capture) |
| `private-health-facilities-act-2007/` | Private Health Facilities Act 2007 No 9 | 1 | Current text: the version in force from 2025-06-11 (newest capture) |
| `payroll-tax-act-2007/` | Payroll Tax Act 2007 No 21 | 1 | Current text: the version in force from 2025-08-15 (newest capture) |
| `biofuels-act-2007/` | Biofuels Act 2007 No 23 | 1 | Current text: the version in force from 2024-11-21 (newest capture) |
| `surveillance-devices-act-2007/` | Surveillance Devices Act 2007 No 64 | 1 | Current text: the version in force from 2025-08-15 (newest capture) |
| `assisted-reproductive-technology-act-2007/` | Assisted Reproductive Technology Act 2007 No 69 | 1 | Current text: the version in force from 2024-05-27 (newest capture) |
| `crimes-domestic-and-personal-violence-act-2007/` | Crimes (Domestic and Personal Violence) Act 2007 No 80 | 1 | Current text: the version in force from 2025-11-24 (newest capture) |
| `liquor-act-2007/` | Liquor Act 2007 No 90 | 1 | Current text: the version in force from 2025-11-24 (newest capture) |
| `gaming-and-liquor-administration-act-2007/` | Gaming and Liquor Administration Act 2007 No 91 | 1 | Current text: the version in force from 2024-10-31 (newest capture) |
| `local-court-act-2007/` | Local Court Act 2007 No 93 | 1 | Current text: the version in force from 2025-10-28 (newest capture) |
| `retail-trading-act-2008/` | Retail Trading Act 2008 No 49 | 1 | Current text: the version in force from 2024-08-20 (newest capture) |
| `hemp-industry-act-2008/` | Hemp Industry Act 2008 No 58 | 1 | Current text: the version in force from 2023-07-14 (newest capture) |
| `sporting-venues-authorities-act-2008/` | Sporting Venues Authorities Act 2008 No 65 | 1 | Current text: the version in force from 2024-07-01 (newest capture) |
| `vexatious-proceedings-act-2008/` | Vexatious Proceedings Act 2008 No 80 | 1 | Current text: the version in force from 2024-07-01 (newest capture) |
| `public-health-tobacco-act-2008/` | Public Health (Tobacco) Act 2008 No 94 | 1 | Current text: the version in force from 2025-11-03 (newest capture) |
| `dangerous-goods-road-and-rail-transport-act-2008/` | Dangerous Goods (Road and Rail Transport) Act 2008 No 95 | 1 | Current text: the version in force from 2024-04-03 (newest capture) |
| `graffiti-control-act-2008/` | Graffiti Control Act 2008 No 100 | 1 | Current text: the version in force from 2025-03-02 (newest capture) |
| `barangaroo-act-2009/` | Barangaroo Act 2009 No 2 | 1 | Current text: the version in force from 2019-07-01 (newest capture) |
| `parking-space-levy-act-2009/` | Parking Space Levy Act 2009 No 5 | 1 | Current text: the version in force from 2021-12-01 (newest capture) |
| `associations-incorporation-act-2009/` | Associations Incorporation Act 2009 No 7 | 1 | Current text: the version in force from 2024-11-21 (newest capture) |
| `coroners-act-2009/` | Coroners Act 2009 No 41 | 1 | Current text: the version in force from 2024-11-21 (newest capture) |
| `nsw-trustee-and-guardian-act-2009/` | NSW Trustee and Guardian Act 2009 No 49 | 1 | Current text: the version in force from 2023-10-30 (newest capture) |
| `government-information-public-access-act-2009/` | Government Information (Public Access) Act 2009 No 52 | 1 | Current text: the version in force from 2025-08-15 (newest capture) |
| `major-events-act-2009/` | Major Events Act 2009 No 73 | 1 | Current text: the version in force from 2024-10-31 (newest capture) |
| `fisheries-management-amendment-act-2009/` | Fisheries Management Amendment Act 2009 No 114 | 1 | Current text: the version in force from 2010-04-02 (newest capture) |
| `industrial-relations-commonwealth-powers-act-2009/` | Industrial Relations (Commonwealth Powers) Act 2009 No 115 | 1 | Current text: the version in force from 2010-01-02 (newest capture) |
| `health-practitioner-regulation-national-law-nsw-no-86a-of-2009/` | Health Practitioner Regulation National Law (NSW) No 86a of 2009 | 1 | Current text: the version in force from 2025-06-11 (newest capture) |
| `relationships-register-act-2010/` | Relationships Register Act 2010 No 19 | 1 | Current text: the version in force from 2019-01-01 (newest capture) |
| `carers-recognition-act-2010/` | Carers (Recognition) Act 2010 No 20 | 1 | Current text: the version in force from 2017-06-08 (newest capture) |
| `residential-tenancies-act-2010/` | Residential Tenancies Act 2010 No 42 | 1 | Current text: the version in force from 2025-08-15 (newest capture) |
| `commercial-arbitration-act-2010/` | Commercial Arbitration Act 2010 No 61 | 1 | Current text: the version in force from 2018-01-14 (newest capture) |
| `parliamentary-budget-officer-act-2010/` | Parliamentary Budget Officer Act 2010 No 83 | 1 | Current text: the version in force from 2023-10-30 (newest capture) |
| `australian-jockey-and-sydney-turf-clubs-merger-act-2010/` | Australian Jockey and Sydney Turf Clubs Merger Act 2010 No 93 | 1 | Current text: the version in force from 2019-01-08 (newest capture) |
| `surrogacy-act-2010/` | Surrogacy Act 2010 No 102 | 1 | Current text: the version in force from 2011-06-07 (newest capture) |
| `children-education-and-care-services-national-law-nsw-no-104a-of-2010/` | Children (Education and Care Services) National Law (NSW) No 104a of 2010 | 1 | Current text: the version in force from 2025-12-15 (newest capture) |
| `court-suppression-and-non-publication-orders-act-2010/` | Court Suppression and Non-publication Orders Act 2010 No 106 | 1 | Current text: the version in force from 2024-07-01 (newest capture) |
| `public-holidays-act-2010/` | Public Holidays Act 2010 No 115 | 1 | Current text: the version in force from 2023-01-13 (newest capture) |
| `contract-cleaning-industry-portable-long-service-leave-scheme-act-2010/` | Contract Cleaning Industry (Portable Long Service Leave Scheme) Act 2010 No 122 | 1 | Current text: the version in force from 2024-11-21 (newest capture) |
| `public-health-act-2010/` | Public Health Act 2010 No 127 | 1 | Current text: the version in force from 2025-01-31 (newest capture) |
| `lobbying-of-government-officials-act-2011/` | Lobbying of Government Officials Act 2011 No 5 | 1 | Current text: the version in force from 2018-07-01 (newest capture) |
| `work-health-and-safety-act-2011/` | Work Health and Safety Act 2011 No 10 | 1 | Current text: the version in force from 2025-10-13 (newest capture) |
| `infrastructure-nsw-act-2011/` | Infrastructure NSW Act 2011 No 23 | 1 | Current text: the version in force from 2023-10-30 (newest capture) |
| `restart-nsw-fund-act-2011/` | Restart NSW Fund Act 2011 No 32 | 1 | Current text: the version in force from 2018-12-01 (newest capture) |
| `government-advertising-act-2011/` | Government Advertising Act 2011 No 35 | 1 | Current text: the version in force from 2021-07-01 (newest capture) |
| `plumbing-and-drainage-act-2011/` | Plumbing and Drainage Act 2011 No 59 | 1 | Current text: the version in force from 2024-08-20 (newest capture) |
| `crimes-criminal-organisations-control-act-2012/` | Crimes (Criminal Organisations Control) Act 2012 No 9 | 1 | Current text: the version in force from 2023-09-01 (newest capture) |
| `mental-health-commission-act-2012/` | Mental Health Commission Act 2012 No 13 | 1 | Current text: the version in force from 2018-11-22 (newest capture) |
| `tattoo-industry-act-2012/` | Tattoo Industry Act 2012 No 32 | 1 | Current text: the version in force from 2025-09-23 (newest capture) |
| `electricity-generator-assets-authorised-transactions-act-2012/` | Electricity Generator Assets (Authorised Transactions) Act 2012 No 35 | 1 | Current text: the version in force from 2021-07-01 (newest capture) |
| `child-protection-working-with-children-act-2012/` | Child Protection (Working with Children) Act 2012 No 51 | 1 | Current text: the version in force from 2026-02-16 (newest capture) |
| `workers-compensation-legislation-amendment-act-2012/` | Workers Compensation Legislation Amendment Act 2012 No 53 | 1 | Current text: the version in force from 2012-10-02 (newest capture) |
| `fiscal-responsibility-act-2012/` | Fiscal Responsibility Act 2012 No 58 | 1 | Current text: the version in force from 2021-07-01 (newest capture) |
| `community-housing-providers-adoption-of-national-law-act-2012/` | Community Housing Providers (Adoption of National Law) Act 2012 No 59 | 1 | Current text: the version in force from 2019-01-08 (newest capture) |
| `crime-commission-act-2012/` | Crime Commission Act 2012 No 66 | 1 | Current text: the version in force from 2023-10-01 (newest capture) |
| `boarding-houses-act-2012/` | Boarding Houses Act 2012 No 74 | 1 | Current text: the version in force from 2023-01-13 (newest capture) |
| `rail-safety-adoption-of-national-law-act-2012/` | Rail Safety (Adoption of National Law) Act 2012 No 82 | 1 | Current text: the version in force from 2024-07-01 (newest capture) |
| `electronic-conveyancing-adoption-of-national-law-act-2012/` | Electronic Conveyancing (Adoption of National Law) Act 2012 No 88 | 1 | Current text: the version in force from 2022-06-06 (newest capture) |
| `forestry-act-2012/` | Forestry Act 2012 No 96 | 1 | Current text: the version in force from 2024-11-21 (newest capture) |
| `rail-safety-national-law-nsw-no-82a-of-2012/` | Rail Safety National Law (NSW) No 82a of 2012 | 1 | Current text: the version in force from 2024-07-01 (newest capture) |
| `civil-and-administrative-tribunal-act-2013/` | Civil and Administrative Tribunal Act 2013 No 2 | 1 | Current text: the version in force from 2025-04-04 (newest capture) |
| `road-transport-act-2013/` | Road Transport Act 2013 No 18 | 1 | Current text: the version in force from 2025-11-26 (newest capture) |
| `bail-act-2013/` | Bail Act 2013 No 26 | 1 | Current text: the version in force from 2025-10-28 (newest capture) |
| `victims-rights-and-support-act-2013/` | Victims Rights and Support Act 2013 No 37 | 1 | Current text: the version in force from 2025-09-01 (newest capture) |
| `government-sector-employment-act-2013/` | Government Sector Employment Act 2013 No 40 | 1 | Current text: the version in force from 2025-08-15 (newest capture) |
| `members-of-parliament-staff-act-2013/` | Members of Parliament Staff Act 2013 No 41 | 1 | Current text: the version in force from 2023-10-30 (newest capture) |
| `heavy-vehicle-adoption-of-national-law-act-2013/` | Heavy Vehicle (Adoption of National Law) Act 2013 No 42 | 1 | Current text: the version in force from 2025-08-15 (newest capture) |
| `local-land-services-act-2013/` | Local Land Services Act 2013 No 51 | 1 | Current text: the version in force from 2024-11-21 (newest capture) |
| `work-health-and-safety-mines-and-petroleum-sites-act-2013/` | Work Health and Safety (Mines and Petroleum Sites) Act 2013 No 54 | 1 | Current text: the version in force from 2023-12-15 (newest capture) |
| `entertainment-industry-act-2013/` | Entertainment Industry Act 2013 No 73 | 1 | Current text: the version in force from 2023-07-14 (newest capture) |
| `education-standards-authority-act-2013/` | Education Standards Authority Act 2013 No 89 | 1 | Current text: the version in force from 2023-07-01 (newest capture) |
| `cemeteries-and-crematoria-act-2013/` | Cemeteries and Crematoria Act 2013 No 105 | 1 | Current text: the version in force from 2025-09-01 (newest capture) |
| `motor-dealers-and-repairers-act-2013/` | Motor Dealers and Repairers Act 2013 No 107 | 1 | Current text: the version in force from 2025-09-01 (newest capture) |
| `legal-profession-uniform-law-application-act-2014/` | Legal Profession Uniform Law Application Act 2014 No 16 | 1 | Current text: the version in force from 2025-09-01 (newest capture) |
| `advocate-for-children-and-young-people-act-2014/` | Advocate for Children and Young People Act 2014 No 29 | 1 | Current text: the version in force from 2023-10-30 (newest capture) |
| `disability-inclusion-act-2014/` | Disability Inclusion Act 2014 No 41 | 1 | Current text: the version in force from 2023-07-01 (newest capture) |
| `passenger-transport-act-2014/` | Passenger Transport Act 2014 No 46 | 1 | Current text: the version in force from 2025-11-26 (newest capture) |
| `mutual-recognition-automatic-licensed-occupations-recognition-act-2014/` | Mutual Recognition (Automatic Licensed Occupations Recognition) Act 2014 No 51 | 1 | Current text: the version in force from 2014-09-25 (newest capture) |
| `marine-estate-management-act-2014/` | Marine Estate Management Act 2014 No 72 | 1 | Current text: the version in force from 2024-08-09 (newest capture) |
| `legal-profession-uniform-law-nsw-no-16a-of-2014/` | Legal Profession Uniform Law (NSW) No 16a of 2014 | 1 | Current text: the version in force from 2022-07-01 (newest capture) |
| `state-insurance-and-care-governance-act-2015/` | State Insurance and Care Governance Act 2015 No 19 | 1 | Current text: the version in force from 2025-01-01 (newest capture) |
| `biosecurity-act-2015/` | Biosecurity Act 2015 No 24 | 1 | Current text: the version in force from 2025-10-31 (newest capture) |
| `dams-safety-act-2015/` | Dams Safety Act 2015 No 26 | 1 | Current text: the version in force from 2024-07-01 (newest capture) |
| `strata-schemes-management-act-2015/` | Strata Schemes Management Act 2015 No 50 | 1 | Current text: the version in force from 2025-10-27 (newest capture) |
| `strata-schemes-development-act-2015/` | Strata Schemes Development Act 2015 No 51 | 1 | Current text: the version in force from 2024-08-20 (newest capture) |
| `data-sharing-government-sector-act-2015/` | Data Sharing (Government Sector) Act 2015 No 60 | 1 | Current text: the version in force from 2023-07-01 (newest capture) |
| `crimes-serious-crime-prevention-orders-act-2016/` | Crimes (Serious Crime Prevention Orders) Act 2016 No 15 | 1 | Current text: the version in force from 2023-07-14 (newest capture) |
| `coastal-management-act-2016/` | Coastal Management Act 2016 No 20 | 1 | Current text: the version in force from 2024-08-09 (newest capture) |
| `point-to-point-transport-taxis-and-hire-vehicles-act-2016/` | Point to Point Transport (Taxis and Hire Vehicles) Act 2016 No 34 | 1 | Current text: the version in force from 2023-08-01 (newest capture) |
| – | – | 1 | Current text: the version in force from 2025-09-23 (newest capture) |
| `land-and-property-information-nsw-authorised-transaction-act-2016/` | Land and Property Information NSW (Authorised Transaction) Act 2016 No 46 | 1 | Current text: the version in force from 2021-07-01 (newest capture) |
| `fair-trading-amendment-commercial-agents-act-2016/` | Fair Trading Amendment (Commercial Agents) Act 2016 No 52 | 1 | Current text: the version in force from 2022-07-02 (newest capture) |
| `crown-land-management-act-2016/` | Crown Land Management Act 2016 No 58 | 1 | Current text: the version in force from 2024-11-21 (newest capture) |
| `law-enforcement-conduct-commission-act-2016/` | Law Enforcement Conduct Commission Act 2016 No 61 | 1 | Current text: the version in force from 2025-05-12 (newest capture) |
| `biodiversity-conservation-act-2016/` | Biodiversity Conservation Act 2016 No 63 | 1 | Current text: the version in force from 2025-12-05 (newest capture) |
| `rock-fishing-safety-act-2016/` | Rock Fishing Safety Act 2016 No 66 | 1 | Current text: the version in force from 2019-07-01 (newest capture) |
| `motor-accident-injuries-act-2017/` | Motor Accident Injuries Act 2017 No 10 | 1 | Current text: the version in force from 2023-04-01 (newest capture) |
| `greyhound-racing-act-2017/` | Greyhound Racing Act 2017 No 13 | 1 | Current text: the version in force from 2023-07-01 (newest capture) |
| `gas-and-electricity-consumer-safety-act-2017/` | Gas and Electricity (Consumer Safety) Act 2017 No 15 | 1 | Current text: the version in force from 2023-01-13 (newest capture) |
| `civil-liability-third-party-claims-against-insurers-act-2017/` | Civil Liability (Third Party Claims Against Insurers) Act 2017 No 19 | 1 | Current text: the version in force from 2017-06-02 (newest capture) |
| `emergency-services-levy-act-2017/` | Emergency Services Levy Act 2017 No 32 | 1 | Current text: the version in force from 2024-06-20 (newest capture) |
| `coal-mine-subsidence-compensation-act-2017/` | Coal Mine Subsidence Compensation Act 2017 No 37 | 1 | Current text: the version in force from 2025-07-01 (newest capture) |
| `aboriginal-languages-act-2017/` | Aboriginal Languages Act 2017 No 51 | 1 | Current text: the version in force from 2019-12-05 (newest capture) |
| `electoral-act-2017/` | Electoral Act 2017 No 66 | 1 | Current text: the version in force from 2024-10-09 (newest capture) |
| `terrorism-high-risk-offenders-act-2017/` | Terrorism (High Risk Offenders) Act 2017 No 68 | 1 | Current text: the version in force from 2025-03-02 (newest capture) |
| `building-products-safety-act-2017/` | Building Products (Safety) Act 2017 No 69 | 1 | Current text: the version in force from 2024-08-20 (newest capture) |
| `saint-johns-college-act-2018/` | Saint John's College Act 2018 No 6 | 1 | Current text: the version in force from 2019-01-08 (newest capture) |
| `state-debt-recovery-act-2018/` | State Debt Recovery Act 2018 No 11 | 1 | Current text: the version in force from 2024-12-02 (newest capture) |
| `electoral-funding-act-2018/` | Electoral Funding Act 2018 No 20 | 1 | Current text: the version in force from 2025-06-11 (newest capture) |
| `modern-slavery-act-2018/` | Modern Slavery Act 2018 No 30 | 1 | Current text: the version in force from 2025-03-02 (newest capture) |
| `nsw-generations-funds-act-2018/` | NSW Generations Funds Act 2018 No 37 | 1 | Current text: the version in force from 2023-09-27 (newest capture) |
| `paintball-act-2018/` | Paintball Act 2018 No 44 | 1 | Current text: the version in force from 2024-09-01 (newest capture) |
| `government-sector-finance-act-2018/` | Government Sector Finance Act 2018 No 55 | 1 | Current text: the version in force from 2025-08-15 (newest capture) |
| `community-gaming-act-2018/` | Community Gaming Act 2018 No 60 | 1 | Current text: the version in force from 2024-05-31 (newest capture) |
| `building-and-development-certifiers-act-2018/` | Building and Development Certifiers Act 2018 No 63 | 1 | Current text: the version in force from 2024-10-23 (newest capture) |
| `fair-trading-legislation-amendment-reform-act-2018/` | Fair Trading Legislation Amendment (Reform) Act 2018 No 65 | 1 | Current text: the version in force from 2020-10-27 (newest capture) |
| `government-telecommunications-act-2018/` | Government Telecommunications Act 2018 No 67 | 1 | Current text: the version in force from 2024-08-20 (newest capture) |
| `national-disability-insurance-scheme-worker-checks-act-2018/` | National Disability Insurance Scheme (Worker Checks) Act 2018 No 82 | 1 | Current text: the version in force from 2018-11-29 (newest capture) |
| `ageing-and-disability-commissioner-act-2019/` | Ageing and Disability Commissioner Act 2019 No 7 | 1 | Current text: the version in force from 2024-04-03 (newest capture) |
| `abortion-law-reform-act-2019/` | Abortion Law Reform Act 2019 No 11 | 1 | Current text: the version in force from 2025-06-11 (newest capture) |
| `music-festivals-act-2019/` | Music Festivals Act 2019 No 17 | 1 | Current text: the version in force from 2024-12-13 (newest capture) |
| `childrens-guardian-act-2019/` | Children's Guardian Act 2019 No 25 | 1 | Current text: the version in force from 2026-02-18 (newest capture) |
| `design-and-building-practitioners-act-2020/` | Design and Building Practitioners Act 2020 No 7 | 1 | Current text: the version in force from 2024-08-20 (newest capture) |
| `residential-apartment-buildings-compliance-and-enforcement-powers-act-2020/` | Residential Apartment Buildings (Compliance and Enforcement Powers) Act 2020 No 9 | 1 | Current text: the version in force from 2024-08-20 (newest capture) |
| `mental-health-and-cognitive-impairment-forensic-provisions-act-2020/` | Mental Health and Cognitive Impairment Forensic Provisions Act 2020 No 12 | 1 | Current text: the version in force from 2025-10-28 (newest capture) |
| `digital-restart-fund-act-2020/` | Digital Restart Fund Act 2020 No 15 | 1 | Current text: the version in force from 2020-08-03 (newest capture) |
| `personal-injury-commission-act-2020/` | Personal Injury Commission Act 2020 No 18 | 1 | Current text: the version in force from 2024-09-27 (newest capture) |
| `electricity-infrastructure-investment-act-2020/` | Electricity Infrastructure Investment Act 2020 No 44 | 1 | Current text: the version in force from 2025-12-01 (newest capture) |
| `community-land-development-act-2021/` | Community Land Development Act 2021 No 6 | 1 | Current text: the version in force from 2023-12-11 (newest capture) |
| `community-land-management-act-2021/` | Community Land Management Act 2021 No 7 | 1 | Current text: the version in force from 2025-10-27 (newest capture) |
| `mandatory-disease-testing-act-2021/` | Mandatory Disease Testing Act 2021 No 13 | 1 | Current text: the version in force from 2022-07-29 (newest capture) |
| `electric-vehicles-revenue-arrangements-act-2021/` | Electric Vehicles (Revenue Arrangements) Act 2021 No 25 | 1 | Current text: the version in force from 2024-01-01 (newest capture) |
| `plastic-reduction-and-circular-economy-act-2021/` | Plastic Reduction and Circular Economy Act 2021 No 31 | 1 | Current text: the version in force from 2025-12-12 (newest capture) |
| `public-spaces-unattended-property-act-2021/` | Public Spaces (Unattended Property) Act 2021 No 38 | 1 | Current text: the version in force from 2023-01-13 (newest capture) |
| `covid-19-and-other-legislation-amendment-regulatory-reforms-act-2022/` | COVID-19 and Other Legislation Amendment (Regulatory Reforms) Act 2022 No 5 | 1 | Current text: the version in force from 2024-01-31 (newest capture) |
| `greater-sydney-parklands-trust-act-2022/` | Greater Sydney Parklands Trust Act 2022 No 9 | 1 | Current text: the version in force from 2024-05-31 (newest capture) |
| `motor-sports-events-act-2022/` | Motor Sports Events Act 2022 No 11 | 1 | Current text: the version in force from 2022-04-14 (newest capture) |
| `public-interest-disclosures-act-2022/` | Public Interest Disclosures Act 2022 No 14 | 1 | Current text: the version in force from 2023-10-30 (newest capture) |
| `voluntary-assisted-dying-act-2022/` | Voluntary Assisted Dying Act 2022 No 17 | 1 | Current text: the version in force from 2023-11-29 (newest capture) |
| `medicines-poisons-and-therapeutic-goods-act-2022/` | Medicines, Poisons and Therapeutic Goods Act 2022 No 73 | 1 | Current text: the version in force from 2025-07-03 (newest capture) |
| `nsw-reconstruction-authority-act-2022/` | NSW Reconstruction Authority Act 2022 No 80 | 1 | Current text: the version in force from 2024-07-01 (newest capture) |
| `conversion-practices-ban-act-2024/` | Conversion Practices Ban Act 2024 No 19 | 1 | Current text: the version in force from 2025-04-05 (newest capture) |
| `community-services-sector-portable-long-service-leave-act-2024/` | Community Services Sector (Portable Long Service Leave) Act 2024 No 39 | 1 | Current text: the version in force from 2025-07-02 (newest capture) |
| `energy-security-corporation-act-2024/` | Energy Security Corporation Act 2024 No 45 | 1 | Current text: the version in force from 2024-06-24 (newest capture) |
| `creative-statement-to-parliament-act-2025/` | Creative Statement to Parliament Act 2025 No 3 | 1 | Current text: the version in force from 2025-03-02 (newest capture) |
| `product-lifecycle-responsibility-act-2025/` | Product Lifecycle Responsibility Act 2025 No 22 | 1 | Current text: the version in force from 2025-04-09 (newest capture) |
| `screen-and-digital-games-industries-act-2025/` | Screen and Digital Games Industries Act 2025 No 23 | 1 | Current text: the version in force from 2025-07-02 (newest capture) |
| `warringah-local-environmental-plan-2000/` | Warringah Local Environmental Plan 2000 | 1 | Current text: the version in force from 2022-11-21 (newest capture) |
| `standard-instrument-principal-local-environmental-plan-2006-epi-155a/` | Standard Instrument-Principal Local Environmental Plan (2006 EPI 155a) | 1 | Current text: the version in force from 2025-09-19 (newest capture) |
| `state-environmental-planning-policy-exempt-and-complying-development-codes-2008/` | State Environmental Planning Policy (Exempt and Complying Development Codes) 2008 | 1 | Current text: the version in force from 2026-07-08 (newest capture) |
| `wollongong-local-environmental-plan-2009-2010-epi-76/` | Wollongong Local Environmental Plan 2009 (2010 EPI 76) | 1 | Current text: the version in force from 2025-12-12 (newest capture) |
| `wingecarribee-local-environmental-plan-2010/` | Wingecarribee Local Environmental Plan 2010 | 1 | Current text: the version in force from 2025-02-21 (newest capture) |
| `greater-taree-local-environmental-plan-2010/` | Greater Taree Local Environmental Plan 2010 | 1 | Current text: the version in force from 2023-11-10 (newest capture) |
| `upper-lachlan-local-environmental-plan-2010/` | Upper Lachlan Local Environmental Plan 2010 | 1 | Current text: the version in force from 2025-09-19 (newest capture) |
| `albury-local-environmental-plan-2010/` | Albury Local Environmental Plan 2010 | 1 | Current text: the version in force from 2024-03-01 (newest capture) |
| `camden-local-environmental-plan-2010/` | Camden Local Environmental Plan 2010 | 1 | Current text: the version in force from 2024-09-06 (newest capture) |
| `penrith-local-environmental-plan-2010/` | Penrith Local Environmental Plan 2010 | 1 | Current text: the version in force from 2024-05-20 (newest capture) |
| `port-macquarie-hastings-local-environmental-plan-2011/` | Port Macquarie-Hastings Local Environmental Plan 2011 | 1 | Current text: the version in force from 2025-09-19 (newest capture) |
| `wollondilly-local-environmental-plan-2011/` | Wollondilly Local Environmental Plan 2011 | 1 | Current text: the version in force from 2023-12-15 (newest capture) |
| `coonamble-local-environmental-plan-2011/` | Coonamble Local Environmental Plan 2011 | 1 | Current text: the version in force from 2023-11-10 (newest capture) |
| `gilgandra-local-environmental-plan-2011/` | Gilgandra Local Environmental Plan 2011 | 1 | Current text: the version in force from 2023-11-10 (newest capture) |
| `liverpool-plains-local-environmental-plan-2011/` | Liverpool Plains Local Environmental Plan 2011 | 1 | Current text: the version in force from 2024-06-21 (newest capture) |
| `warringah-local-environmental-plan-2011/` | Warringah Local Environmental Plan 2011 | 1 | Current text: the version in force from 2025-10-31 (newest capture) |
| `maitland-local-environmental-plan-2011/` | Maitland Local Environmental Plan 2011 | 1 | Current text: the version in force from 2025-09-19 (newest capture) |
| `clarence-valley-local-environmental-plan-2011/` | Clarence Valley Local Environmental Plan 2011 | 1 | Current text: the version in force from 2024-08-09 (newest capture) |
| `cessnock-local-environmental-plan-2011/` | Cessnock Local Environmental Plan 2011 | 1 | Current text: the version in force from 2025-10-10 (newest capture) |
| `orange-local-environmental-plan-2011-2012-epi-55/` | Orange Local Environmental Plan 2011 (2012 EPI 55) | 1 | Current text: the version in force from 2025-04-04 (newest capture) |
| `richmond-valley-local-environmental-plan-2012/` | Richmond Valley Local Environmental Plan 2012 | 1 | Current text: the version in force from 2025-03-21 (newest capture) |
| `uralla-local-environmental-plan-2012/` | Uralla Local Environmental Plan 2012 | 1 | Current text: the version in force from 2023-11-10 (newest capture) |
| `bombala-local-environmental-plan-2012/` | Bombala Local Environmental Plan 2012 | 1 | Current text: the version in force from 2023-11-10 (newest capture) |
| `eurobodalla-local-environmental-plan-2012/` | Eurobodalla Local Environmental Plan 2012 | 1 | Current text: the version in force from 2024-06-07 (newest capture) |
| `cobar-local-environmental-plan-2012/` | Cobar Local Environmental Plan 2012 | 1 | Current text: the version in force from 2023-11-10 (newest capture) |
| `burwood-local-environmental-plan-2012/` | Burwood Local Environmental Plan 2012 | 1 | Current text: the version in force from 2024-06-28 (newest capture) |
| `sydney-local-environmental-plan-2012/` | Sydney Local Environmental Plan 2012 | 1 | Current text: the version in force from 2025-10-17 (newest capture) |
| `tweed-city-centre-local-environmental-plan-2012-2013-epi-14/` | Tweed City Centre Local Environmental Plan 2012 (2013 EPI 14) | 1 | Current text: the version in force from 2024-03-04 (newest capture) |
| `cowra-local-environmental-plan-2012-2013-epi-22/` | Cowra Local Environmental Plan 2012 (2013 EPI 22) | 1 | Current text: the version in force from 2024-02-23 (newest capture) |
| `kyogle-local-environmental-plan-2012-2013-epi-25/` | Kyogle Local Environmental Plan 2012 (2013 EPI 25) | 1 | Current text: the version in force from 2025-09-19 (newest capture) |
| `central-darling-local-environmental-plan-2012-2013-epi-33/` | Central Darling Local Environmental Plan 2012 (2013 EPI 33) | 1 | Current text: the version in force from 2024-06-14 (newest capture) |
| `hunters-hill-local-environmental-plan-2012-2013-epi-34/` | Hunters Hill Local Environmental Plan 2012 (2013 EPI 34) | 1 | Current text: the version in force from 2025-10-03 (newest capture) |
| `strathfield-local-environmental-plan-2012-2013-epi-115/` | Strathfield Local Environmental Plan 2012 (2013 EPI 115) | 1 | Current text: the version in force from 2025-10-31 (newest capture) |
| `shellharbour-local-environmental-plan-2013/` | Shellharbour Local Environmental Plan 2013 | 1 | Current text: the version in force from 2025-09-19 (newest capture) |
| `fairfield-local-environmental-plan-2013/` | Fairfield Local Environmental Plan 2013 | 1 | Current text: the version in force from 2025-10-31 (newest capture) |
| `canada-bay-local-environmental-plan-2013/` | Canada Bay Local Environmental Plan 2013 | 1 | Current text: the version in force from 2025-09-19 (newest capture) |
| `cootamundra-local-environmental-plan-2013/` | Cootamundra Local Environmental Plan 2013 | 1 | Current text: the version in force from 2025-09-19 (newest capture) |
| `bega-valley-local-environmental-plan-2013/` | Bega Valley Local Environmental Plan 2013 | 1 | Current text: the version in force from 2024-09-13 (newest capture) |
| `warrumbungle-local-environmental-plan-2013/` | Warrumbungle Local Environmental Plan 2013 | 1 | Current text: the version in force from 2026-07-01 (newest capture) |
| `kempsey-local-environmental-plan-2013/` | Kempsey Local Environmental Plan 2013 | 1 | Current text: the version in force from 2024-06-21 (newest capture) |
| `port-stephens-local-environmental-plan-2013/` | Port Stephens Local Environmental Plan 2013 | 1 | Current text: the version in force from 2026-07-01 (newest capture) |
| `great-lakes-local-environmental-plan-2014/` | Great Lakes Local Environmental Plan 2014 | 1 | Current text: the version in force from 2024-02-23 (newest capture) |
| `tweed-local-environmental-plan-2014/` | Tweed Local Environmental Plan 2014 | 1 | Current text: the version in force from 2024-12-13 (newest capture) |
| `shoalhaven-local-environmental-plan-2014/` | Shoalhaven Local Environmental Plan 2014 | 1 | Current text: the version in force from 2024-12-06 (newest capture) |
| `byron-local-environmental-plan-2014/` | Byron Local Environmental Plan 2014 | 1 | Current text: the version in force from 2024-09-20 (newest capture) |
| `lithgow-local-environmental-plan-2014/` | Lithgow Local Environmental Plan 2014 | 1 | Current text: the version in force from 2023-11-10 (newest capture) |
| `woollahra-local-environmental-plan-2014-2015-epi-20/` | Woollahra Local Environmental Plan 2014 (2015 EPI 20) | 1 | Current text: the version in force from 2025-07-25 (newest capture) |
| `ku-ring-gai-local-environmental-plan-2015/` | Ku-ring-gai Local Environmental Plan 2015 | 1 | Current text: the version in force from 2025-04-17 (newest capture) |
| `blacktown-local-environmental-plan-2015/` | Blacktown Local Environmental Plan 2015 | 1 | Current text: the version in force from 2025-09-19 (newest capture) |
| `sutherland-shire-local-environmental-plan-2015/` | Sutherland Shire Local Environmental Plan 2015 | 1 | Current text: the version in force from 2025-09-19 (newest capture) |
| `campbelltown-local-environmental-plan-2015/` | Campbelltown Local Environmental Plan 2015 | 1 | Current text: the version in force from 2025-11-28 (newest capture) |
| `bayside-local-environmental-plan-2021/` | Bayside Local Environmental Plan 2021 | 1 | Current text: the version in force from 2025-11-07 (newest capture) |
| `georges-river-local-environmental-plan-2021/` | Georges River Local Environmental Plan 2021 | 1 | Current text: the version in force from 2025-09-19 (newest capture) |
| `cumberland-local-environmental-plan-2021/` | Cumberland Local Environmental Plan 2021 | 1 | Current text: the version in force from 2025-02-14 (newest capture) |
| `state-environmental-planning-policy-housing-2021/` | State Environmental Planning Policy (Housing) 2021 | 1 | Current text: the version in force from 2025-08-29 (newest capture) |
| `state-environmental-planning-policy-biodiversity-and-conservation-2021/` | State Environmental Planning Policy (Biodiversity and Conservation) 2021 | 1 | Current text: the version in force from 2025-03-07 (newest capture) |
| `state-environmental-planning-policy-precincts-eastern-harbour-city-2021/` | State Environmental Planning Policy (Precincts-Eastern Harbour City) 2021 | 1 | Current text: the version in force from 2024-04-05 (newest capture) |
| `state-environmental-planning-policy-resilience-and-hazards-2021/` | State Environmental Planning Policy (Resilience and Hazards) 2021 | 1 | Current text: the version in force from 2023-08-04 (newest capture) |
| `inner-west-local-environmental-plan-2022/` | Inner West Local Environmental Plan 2022 | 1 | Current text: the version in force from 2024-11-01 (newest capture) |
| `state-environmental-planning-policy-sustainable-buildings-2022/` | State Environmental Planning Policy (Sustainable Buildings) 2022 | 1 | Current text: the version in force from 2025-10-31 (newest capture) |
| `parramatta-local-environmental-plan-2023/` | Parramatta Local Environmental Plan 2023 | 1 | Current text: the version in force from 2025-09-05 (newest capture) |
| `supreme-court-rules-1970/` | Supreme Court Rules 1970 | 1 | Current text: the version in force from 2024-09-13 (newest capture) |
| `fisheries-management-lobster-share-management-plan-regulation-2000/` | Fisheries Management (Lobster Share Management Plan) Regulation 2000 | 1 | Current text: the version in force from 2023-02-24 (newest capture) |
| `uniform-civil-procedure-rules-2005/` | Uniform Civil Procedure Rules 2005 | 1 | Current text: the version in force from 2025-08-08 (newest capture) |
| `university-of-new-south-wales-by-law-2005/` | University of New South Wales By-law 2005 | 1 | Current text: the version in force from 2022-10-19 (newest capture) |
| `electronic-transactions-ecm-courts-order-2005/` | Electronic Transactions (ECM Courts) Order 2005 | 1 | Current text: the version in force from 2024-07-01 (newest capture) |
| `conveyancers-licensing-qualifications-order-2006/` | Conveyancers Licensing (Qualifications) Order 2006 | 1 | Current text: the version in force from 2023-12-15 (newest capture) |
| `land-and-environment-court-rules-2007/` | Land and Environment Court Rules 2007 | 1 | Current text: the version in force from 2020-05-15 (newest capture) |
| `poisons-and-therapeutic-goods-regulation-2008/` | Poisons and Therapeutic Goods Regulation 2008 | 1 | Current text: the version in force from 2025-11-17 (newest capture) |
| `water-sharing-plan-for-the-greater-metropolitan-region-groundwater-sources-2011/` | Water Sharing Plan for the Greater Metropolitan Region Groundwater Sources 2011 | 1 | Current text: the version in force from 2015-01-01 (newest capture) |
| `public-interest-disclosures-regulation-2011/` | Public Interest Disclosures Regulation 2011 | 1 | Current text: the version in force from 2014-01-01 (newest capture) |
| `education-and-care-services-national-regulations-2011-si-653/` | Education and Care Services National Regulations (2011 SI 653) | 1 | Current text: the version in force from 2025-09-01 (newest capture) |
| `sydney-water-stormwater-drainage-areas-order-2011-2012-si-292/` | Sydney Water (Stormwater Drainage Areas) Order 2011 (2012 SI 292) | 1 | Current text: the version in force from 2022-03-18 (newest capture) |
| `heritage-regulation-2012/` | Heritage Regulation 2012 | 1 | Current text: the version in force from 2024-08-02 (newest capture) |
| `prevention-of-cruelty-to-animals-regulation-2012/` | Prevention of Cruelty to Animals Regulation 2012 | 1 | Current text: the version in force from 2021-06-17 (newest capture) |
| `protection-from-harmful-radiation-regulation-2013/` | Protection from Harmful Radiation Regulation 2013 | 1 | Current text: the version in force from 2024-04-03 (newest capture) |
| `child-protection-working-with-children-regulation-2013/` | Child Protection (Working with Children) Regulation 2013 | 1 | Current text: the version in force from 2025-10-02 (newest capture) |
| `boarding-houses-regulation-2013/` | Boarding Houses Regulation 2013 | 1 | Current text: the version in force from 2023-01-13 (newest capture) |
| `veterinary-practice-regulation-2013/` | Veterinary Practice Regulation 2013 | 1 | Current text: the version in force from 2021-07-01 (newest capture) |
| `co-operatives-national-regulations-2013-si-601/` | Co-operatives National Regulations (2013 SI 601) | 1 | Current text: the version in force from 2017-10-20 (newest capture) |
| `heavy-vehicle-fatigue-management-national-regulation-nsw-2013-si-245a/` | Heavy Vehicle (Fatigue Management) National Regulation (NSW) (2013 SI 245a) | 1 | Current text: the version in force from 2018-10-01 (newest capture) |
| `heavy-vehicle-vehicle-standards-national-regulation-nsw-2013-si-248a/` | Heavy Vehicle (Vehicle Standards) National Regulation (NSW) (2013 SI 248a) | 1 | Current text: the version in force from 2024-04-12 (newest capture) |
| `local-land-services-regulation-2014/` | Local Land Services Regulation 2014 | 1 | Current text: the version in force from 2024-11-21 (newest capture) |
| `government-sector-employment-senior-executive-bands-determination-2014/` | Government Sector Employment (Senior Executive Bands) Determination 2014 | 1 | Current text: the version in force from 2014-02-20 (newest capture) |
| `government-sector-employment-regulation-2014/` | Government Sector Employment Regulation 2014 | 1 | Current text: the version in force from 2025-03-05 (newest capture) |
| `government-sector-employment-general-rules-2014/` | Government Sector Employment (General) Rules 2014 | 1 | Current text: the version in force from 2025-08-29 (newest capture) |
| `dangerous-goods-road-and-rail-transport-regulation-2014/` | Dangerous Goods (Road and Rail Transport) Regulation 2014 | 1 | Current text: the version in force from 2020-10-09 (newest capture) |
| `electricity-supply-general-regulation-2014/` | Electricity Supply (General) Regulation 2014 | 1 | Current text: the version in force from 2025-11-28 (newest capture) |
| `electricity-supply-safety-and-network-management-regulation-2014/` | Electricity Supply (Safety and Network Management) Regulation 2014 | 1 | Current text: the version in force from 2018-09-01 (newest capture) |
| `photo-card-regulation-2014/` | Photo Card Regulation 2014 | 1 | Current text: the version in force from 2024-07-01 (newest capture) |
| `motor-dealers-and-repairers-regulation-2014/` | Motor Dealers and Repairers Regulation 2014 | 1 | Current text: the version in force from 2023-01-13 (newest capture) |
| `protection-of-the-environment-operations-waste-regulation-2014/` | Protection of the Environment Operations (Waste) Regulation 2014 | 1 | Current text: the version in force from 2025-08-22 (newest capture) |
| `road-rules-2014/` | Road Rules 2014 | 1 | Current text: the version in force from 2025-08-15 (newest capture) |
| `home-building-regulation-2014/` | Home Building Regulation 2014 | 1 | Current text: the version in force from 2025-05-16 (newest capture) |
| `legal-profession-uniform-admission-rules-2015/` | Legal Profession Uniform Admission Rules 2015 | 1 | Current text: the version in force from 2025-10-31 (newest capture) |
| `legal-profession-uniform-continuing-professional-development-barristers-rules-2015/` | Legal Profession Uniform Continuing Professional Development (Barristers) Rules 2015 | 1 | Current text: the version in force from 2019-12-13 (newest capture) |
| `legal-profession-uniform-continuing-professional-development-solicitors-rules-2015/` | Legal Profession Uniform Continuing Professional Development (Solicitors) Rules 2015 | 1 | Current text: the version in force from 2016-11-18 (newest capture) |
| `legal-profession-uniform-conduct-barristers-rules-2015/` | Legal Profession Uniform Conduct (Barristers) Rules 2015 | 1 | Current text: the version in force from 2022-03-04 (newest capture) |
| `legal-profession-uniform-law-australian-solicitors-conduct-rules-2015/` | Legal Profession Uniform Law Australian Solicitors' Conduct Rules 2015 | 1 | Current text: the version in force from 2024-08-09 (newest capture) |
| `legal-profession-uniform-legal-practice-solicitors-rules-2015/` | Legal Profession Uniform Legal Practice (Solicitors) Rules 2015 | 1 | Current text: the version in force from 2015-05-27 (newest capture) |
| `legal-profession-uniform-general-rules-2015/` | Legal Profession Uniform General Rules 2015 | 1 | Current text: the version in force from 2023-10-06 (newest capture) |
| `legal-profession-uniform-law-application-regulation-2015/` | Legal Profession Uniform Law Application Regulation 2015 | 1 | Current text: the version in force from 2019-04-01 (newest capture) |
| `rice-marketing-regulation-2015/` | Rice Marketing Regulation 2015 | 1 | Current text: the version in force from 2021-09-10 (newest capture) |
| `police-regulation-2015/` | Police Regulation 2015 | 1 | Current text: the version in force from 2024-09-30 (newest capture) |
| `registered-clubs-regulation-2015/` | Registered Clubs Regulation 2015 | 1 | Current text: the version in force from 2024-10-31 (newest capture) |
| `adoption-regulation-2015/` | Adoption Regulation 2015 | 1 | Current text: the version in force from 2022-12-16 (newest capture) |
| `food-regulation-2015/` | Food Regulation 2015 | 1 | Current text: the version in force from 2024-12-08 (newest capture) |
| `local-government-city-of-parramatta-and-cumberland-proclamation-2016/` | Local Government (City of Parramatta and Cumberland) Proclamation 2016 | 1 | Current text: the version in force from 2017-01-24 (newest capture) |
| `marine-safety-regulation-2016/` | Marine Safety Regulation 2016 | 1 | Current text: the version in force from 2025-07-01 (newest capture) |
| `poisons-and-therapeutic-goods-poisons-list-proclamation-2016/` | Poisons and Therapeutic Goods (Poisons List) Proclamation 2016 | 1 | Current text: the version in force from 2016-07-01 (newest capture) |
| `hemp-industry-regulation-2016/` | Hemp Industry Regulation 2016 | 1 | Current text: the version in force from 2023-01-13 (newest capture) |
| `mining-regulation-2016/` | Mining Regulation 2016 | 1 | Current text: the version in force from 2025-05-30 (newest capture) |
| `petroleum-offshore-regulation-2016/` | Petroleum (Offshore) Regulation 2016 | 1 | Current text: the version in force from 2016-08-12 (newest capture) |
| `petroleum-onshore-regulation-2016/` | Petroleum (Onshore) Regulation 2016 | 1 | Current text: the version in force from 2023-03-01 (newest capture) |
| `strata-schemes-management-regulation-2016/` | Strata Schemes Management Regulation 2016 | 1 | Current text: the version in force from 2025-10-27 (newest capture) |
| `air-transport-regulation-2016/` | Air Transport Regulation 2016 | 1 | Current text: the version in force from 2016-08-12 (newest capture) |
| `driving-instructors-regulation-2016/` | Driving Instructors Regulation 2016 | 1 | Current text: the version in force from 2024-07-01 (newest capture) |
| `guardianship-regulation-2016/` | Guardianship Regulation 2016 | 1 | Current text: the version in force from 2018-12-01 (newest capture) |
| `security-industry-regulation-2016/` | Security Industry Regulation 2016 | 1 | Current text: the version in force from 2025-09-23 (newest capture) |
| `smoke-free-environment-regulation-2016/` | Smoke-free Environment Regulation 2016 | 1 | Current text: the version in force from 2016-08-26 (newest capture) |
| `workers-compensation-regulation-2016/` | Workers Compensation Regulation 2016 | 1 | Current text: the version in force from 2024-07-24 (newest capture) |
| `strata-schemes-development-regulation-2016/` | Strata Schemes Development Regulation 2016 | 1 | Current text: the version in force from 2023-05-01 (newest capture) |
| `government-sector-employment-health-service-senior-executives-rules-2016/` | Government Sector Employment (Health Service Senior Executives) Rules 2016 | 1 | Current text: the version in force from 2016-12-16 (newest capture) |
| `waste-avoidance-and-resource-recovery-container-deposit-scheme-regulation-2017/` | Waste Avoidance and Resource Recovery (Container Deposit Scheme) Regulation 2017 | 1 | Current text: the version in force from 2025-08-15 (newest capture) |
| `biosecurity-regulation-2017/` | Biosecurity Regulation 2017 | 1 | Current text: the version in force from 2025-10-31 (newest capture) |
| `work-health-and-safety-regulation-2017/` | Work Health and Safety Regulation 2017 | 1 | Current text: the version in force from 2025-03-01 (newest capture) |
| `partnership-regulation-2017/` | Partnership Regulation 2017 | 1 | Current text: the version in force from 2017-08-11 (newest capture) |
| `point-to-point-transport-taxis-and-hire-vehicles-regulation-2017/` | Point to Point Transport (Taxis and Hire Vehicles) Regulation 2017 | 1 | Current text: the version in force from 2024-12-06 (newest capture) |
| `architects-regulation-2017/` | Architects Regulation 2017 | 1 | Current text: the version in force from 2020-07-01 (newest capture) |
| `biodiversity-conservation-regulation-2017/` | Biodiversity Conservation Regulation 2017 | 1 | Current text: the version in force from 2025-05-09 (newest capture) |
| `civil-procedure-regulation-2017/` | Civil Procedure Regulation 2017 | 1 | Current text: the version in force from 2024-07-01 (newest capture) |
| `criminal-procedure-regulation-2017/` | Criminal Procedure Regulation 2017 | 1 | Current text: the version in force from 2025-10-28 (newest capture) |
| `firearms-regulation-2017/` | Firearms Regulation 2017 | 1 | Current text: the version in force from 2022-12-16 (newest capture) |
| `pesticides-regulation-2017/` | Pesticides Regulation 2017 | 1 | Current text: the version in force from 2021-12-17 (newest capture) |
| `protection-of-the-environment-operations-noise-control-regulation-2017/` | Protection of the Environment Operations (Noise Control) Regulation 2017 | 1 | Current text: the version in force from 2025-08-15 (newest capture) |
| `road-transport-driver-licensing-regulation-2017/` | Road Transport (Driver Licensing) Regulation 2017 | 1 | Current text: the version in force from 2025-11-28 (newest capture) |
| `road-transport-vehicle-registration-regulation-2017/` | Road Transport (Vehicle Registration) Regulation 2017 | 1 | Current text: the version in force from 2025-12-12 (newest capture) |
| `weapons-prohibition-regulation-2017/` | Weapons Prohibition Regulation 2017 | 1 | Current text: the version in force from 2021-07-01 (newest capture) |
| `sydney-water-regulation-2017/` | Sydney Water Regulation 2017 | 1 | Current text: the version in force from 2024-11-21 (newest capture) |
| `passenger-transport-general-regulation-2017/` | Passenger Transport (General) Regulation 2017 | 1 | Current text: the version in force from 2024-08-02 (newest capture) |
| `independent-commission-against-corruption-regulation-2017/` | Independent Commission Against Corruption Regulation 2017 | 1 | Current text: the version in force from 2023-10-30 (newest capture) |
| `plumbing-and-drainage-regulation-2017/` | Plumbing and Drainage Regulation 2017 | 1 | Current text: the version in force from 2023-05-01 (newest capture) |
| `retirement-villages-regulation-2017/` | Retirement Villages Regulation 2017 | 1 | Current text: the version in force from 2024-05-31 (newest capture) |
| `surveying-and-spatial-information-regulation-2017/` | Surveying and Spatial Information Regulation 2017 | 1 | Current text: the version in force from 2023-10-30 (newest capture) |
| `motor-accident-injuries-regulation-2017/` | Motor Accident Injuries Regulation 2017 | 1 | Current text: the version in force from 2023-09-22 (newest capture) |
| `coal-mine-subsidence-compensation-regulation-2017/` | Coal Mine Subsidence Compensation Regulation 2017 | 1 | Current text: the version in force from 2024-06-21 (newest capture) |
| `environmental-planning-and-assessment-savings-transitional-and-other-provisions-regulation-2017-2018-si-67/` | Environmental Planning and Assessment (Savings, Transitional and Other Provisions) Regulation 2017 (2018 SI 67) | 1 | Current text: the version in force from 2024-10-23 (newest capture) |
| `crown-land-management-regulation-2018/` | Crown Land Management Regulation 2018 | 1 | Current text: the version in force from 2024-08-16 (newest capture) |
| `commons-management-regulation-2018/` | Commons Management Regulation 2018 | 1 | Current text: the version in force from 2018-07-13 (newest capture) |
| `companion-animals-regulation-2018/` | Companion Animals Regulation 2018 | 1 | Current text: the version in force from 2024-11-21 (newest capture) |
| `library-regulation-2018/` | Library Regulation 2018 | 1 | Current text: the version in force from 2019-07-01 (newest capture) |
| `liquor-regulation-2018/` | Liquor Regulation 2018 | 1 | Current text: the version in force from 2024-10-31 (newest capture) |
| `water-management-general-regulation-2018/` | Water Management (General) Regulation 2018 | 1 | Current text: the version in force from 2025-07-01 (newest capture) |
| `gas-and-electricity-consumer-safety-regulation-2018/` | Gas and Electricity (Consumer Safety) Regulation 2018 | 1 | Current text: the version in force from 2023-01-13 (newest capture) |
| `swimming-pools-regulation-2018/` | Swimming Pools Regulation 2018 | 1 | Current text: the version in force from 2021-12-01 (newest capture) |
| `transport-administration-general-regulation-2018/` | Transport Administration (General) Regulation 2018 | 1 | Current text: the version in force from 2025-01-01 (newest capture) |
| `regional-development-regulation-2018/` | Regional Development Regulation 2018 | 1 | Current text: the version in force from 2024-09-30 (newest capture) |
| `roads-regulation-2018/` | Roads Regulation 2018 | 1 | Current text: the version in force from 2025-08-15 (newest capture) |
| `sydney-olympic-park-authority-regulation-2018/` | Sydney Olympic Park Authority Regulation 2018 | 1 | Current text: the version in force from 2024-11-21 (newest capture) |
| `government-sector-finance-regulation-2018/` | Government Sector Finance Regulation 2018 | 1 | Current text: the version in force from 2024-01-01 (newest capture) |
| `privacy-and-personal-information-protection-regulation-2019/` | Privacy and Personal Information Protection Regulation 2019 | 1 | Current text: the version in force from 2024-10-01 (newest capture) |
| `victims-rights-and-support-regulation-2019/` | Victims Rights and Support Regulation 2019 | 1 | Current text: the version in force from 2019-08-16 (newest capture) |
| `national-parks-and-wildlife-regulation-2019/` | National Parks and Wildlife Regulation 2019 | 1 | Current text: the version in force from 2025-07-04 (newest capture) |
| `casino-control-regulation-2019/` | Casino Control Regulation 2019 | 1 | Current text: the version in force from 2025-03-28 (newest capture) |
| `criminal-records-regulation-2019/` | Criminal Records Regulation 2019 | 1 | Current text: the version in force from 2024-05-03 (newest capture) |
| `gaming-machines-regulation-2019/` | Gaming Machines Regulation 2019 | 1 | Current text: the version in force from 2025-01-01 (newest capture) |
| `greyhound-racing-regulation-2019/` | Greyhound Racing Regulation 2019 | 1 | Current text: the version in force from 2024-06-28 (newest capture) |
| `dams-safety-regulation-2019/` | Dams Safety Regulation 2019 | 1 | Current text: the version in force from 2023-01-13 (newest capture) |
| `property-and-stock-agents-qualifications-order-2019/` | Property and Stock Agents (Qualifications) Order 2019 | 1 | Current text: the version in force from 2022-11-18 (newest capture) |
| `residential-tenancies-regulation-2019/` | Residential Tenancies Regulation 2019 | 1 | Current text: the version in force from 2025-07-01 (newest capture) |
| `building-and-development-certifiers-regulation-2020/` | Building and Development Certifiers Regulation 2020 | 1 | Current text: the version in force from 2025-06-20 (newest capture) |
| `national-disability-insurance-scheme-worker-checks-regulation-2020/` | National Disability Insurance Scheme (Worker Checks) Regulation 2020 | 1 | Current text: the version in force from 2024-08-01 (newest capture) |
| `tow-truck-industry-regulation-2020/` | Tow Truck Industry Regulation 2020 | 1 | Current text: the version in force from 2025-08-15 (newest capture) |
| `community-gaming-regulation-2020/` | Community Gaming Regulation 2020 | 1 | Current text: the version in force from 2020-06-26 (newest capture) |
| `human-tissue-regulation-2020/` | Human Tissue Regulation 2020 | 1 | Current text: the version in force from 2023-02-12 (newest capture) |
| `trustee-regulation-2020/` | Trustee Regulation 2020 | 1 | Current text: the version in force from 2020-08-14 (newest capture) |
| `justices-of-the-peace-regulation-2020/` | Justices of the Peace Regulation 2020 | 1 | Current text: the version in force from 2022-10-28 (newest capture) |
| `motor-accidents-compensation-regulation-2020/` | Motor Accidents Compensation Regulation 2020 | 1 | Current text: the version in force from 2021-10-20 (newest capture) |
| `building-and-construction-industry-security-of-payment-regulation-2020/` | Building and Construction Industry Security of Payment Regulation 2020 | 1 | Current text: the version in force from 2021-03-01 (newest capture) |
| `drug-court-regulation-2020/` | Drug Court Regulation 2020 | 1 | Current text: the version in force from 2024-03-29 (newest capture) |
| `personal-injury-commission-rules-2021/` | Personal Injury Commission Rules 2021 | 1 | Current text: the version in force from 2024-11-25 (newest capture) |
| `pawnbrokers-and-second-hand-dealers-regulation-2021/` | Pawnbrokers and Second-hand Dealers Regulation 2021 | 1 | Current text: the version in force from 2023-01-13 (newest capture) |
| `electricity-infrastructure-investment-regulation-2021/` | Electricity Infrastructure Investment Regulation 2021 | 1 | Current text: the version in force from 2025-12-12 (newest capture) |
| `mental-health-and-cognitive-impairment-forensic-provisions-regulation-2021/` | Mental Health and Cognitive Impairment Forensic Provisions Regulation 2021 | 1 | Current text: the version in force from 2021-03-19 (newest capture) |
| `design-and-building-practitioners-regulation-2021/` | Design and Building Practitioners Regulation 2021 | 1 | Current text: the version in force from 2025-06-20 (newest capture) |
| `charitable-fundraising-regulation-2021/` | Charitable Fundraising Regulation 2021 | 1 | Current text: the version in force from 2022-07-01 (newest capture) |
| `long-service-leave-regulation-2021/` | Long Service Leave Regulation 2021 | 1 | Current text: the version in force from 2023-01-13 (newest capture) |
| `energy-and-utilities-administration-regulation-2021/` | Energy and Utilities Administration Regulation 2021 | 1 | Current text: the version in force from 2025-05-23 (newest capture) |
| `local-government-general-regulation-2021/` | Local Government (General) Regulation 2021 | 1 | Current text: the version in force from 2026-01-01 (newest capture) |
| `local-government-manufactured-home-estates-caravan-parks-camping-grounds-and-moveable-dwellings-regulation-2021/` | Local Government (Manufactured Home Estates, Caravan Parks, Camping Grounds and Moveable Dwellings) Regulation 2021 | 1 | Current text: the version in force from 2025-08-29 (newest capture) |
| `exhibited-animals-protection-regulation-2021/` | Exhibited Animals Protection Regulation 2021 | 1 | Current text: the version in force from 2023-08-25 (newest capture) |
| `road-transport-general-regulation-2021/` | Road Transport (General) Regulation 2021 | 1 | Current text: the version in force from 2025-07-01 (newest capture) |
| `conveyancers-licensing-regulation-2021/` | Conveyancers Licensing Regulation 2021 | 1 | Current text: the version in force from 2024-05-31 (newest capture) |
| `community-land-development-regulation-2021/` | Community Land Development Regulation 2021 | 1 | Current text: the version in force from 2021-10-14 (newest capture) |
| `environmental-planning-and-assessment-regulation-2021/` | Environmental Planning and Assessment Regulation 2021 | 1 | Current text: the version in force from 2025-10-17 (newest capture) |
| `childrens-guardian-regulation-2022/` | Children's Guardian Regulation 2022 | 1 | Current text: the version in force from 2025-07-01 (newest capture) |
| `heavy-vehicle-adoption-of-national-law-regulation-2022/` | Heavy Vehicle (Adoption of National Law) Regulation 2022 | 1 | Current text: the version in force from 2025-07-01 (newest capture) |
| `protection-of-the-environment-operations-general-regulation-2022/` | Protection of the Environment Operations (General) Regulation 2022 | 1 | Current text: the version in force from 2025-07-04 (newest capture) |
| `biofuels-regulation-2022/` | Biofuels Regulation 2022 | 1 | Current text: the version in force from 2024-05-31 (newest capture) |
| `cemeteries-and-crematoria-regulation-2022/` | Cemeteries and Crematoria Regulation 2022 | 1 | Current text: the version in force from 2024-07-01 (newest capture) |
| `health-records-and-information-privacy-regulation-2022/` | Health Records and Information Privacy Regulation 2022 | 1 | Current text: the version in force from 2024-10-01 (newest capture) |
| `public-health-tobacco-regulation-2022/` | Public Health (Tobacco) Regulation 2022 | 1 | Current text: the version in force from 2025-11-03 (newest capture) |
| `betting-and-racing-regulation-2022/` | Betting and Racing Regulation 2022 | 1 | Current text: the version in force from 2023-03-30 (newest capture) |
| `children-and-young-persons-care-and-protection-regulation-2022/` | Children and Young Persons (Care and Protection) Regulation 2022 | 1 | Current text: the version in force from 2022-08-26 (newest capture) |
| `conveyancing-sale-of-land-regulation-2022/` | Conveyancing (Sale of Land) Regulation 2022 | 1 | Current text: the version in force from 2022-08-26 (newest capture) |
| `game-and-feral-animal-control-regulation-2022/` | Game and Feral Animal Control Regulation 2022 | 1 | Current text: the version in force from 2022-08-26 (newest capture) |
| `gas-supply-safety-and-network-management-regulation-2022/` | Gas Supply (Safety and Network Management) Regulation 2022 | 1 | Current text: the version in force from 2022-08-26 (newest capture) |
| `jury-regulation-2022/` | Jury Regulation 2022 | 1 | Current text: the version in force from 2025-03-10 (newest capture) |
| `property-and-stock-agents-regulation-2022/` | Property and Stock Agents Regulation 2022 | 1 | Current text: the version in force from 2025-07-01 (newest capture) |
| `public-health-regulation-2022/` | Public Health Regulation 2022 | 1 | Current text: the version in force from 2025-12-01 (newest capture) |
| `work-health-and-safety-mines-and-petroleum-sites-regulation-2022/` | Work Health and Safety (Mines and Petroleum Sites) Regulation 2022 | 1 | Current text: the version in force from 2024-12-13 (newest capture) |
| `associations-incorporation-regulation-2022/` | Associations Incorporation Regulation 2022 | 1 | Current text: the version in force from 2025-06-27 (newest capture) |
| `administrative-arrangements-58th-parliament-order-2023/` | Administrative Arrangements (58th Parliament) Order 2023 | 1 | Current text: the version in force from 2025-10-01 (newest capture) |
| `administrative-arrangements-minns-ministry-administration-of-acts-order-2023/` | Administrative Arrangements (Minns Ministry-Administration of Acts) Order 2023 | 1 | Current text: the version in force from 2025-09-26 (newest capture) |
| `disability-inclusion-regulation-2023/` | Disability Inclusion Regulation 2023 | 1 | Current text: the version in force from 2023-08-11 (newest capture) |
| `pipelines-regulation-2023/` | Pipelines Regulation 2023 | 1 | Current text: the version in force from 2025-12-12 (newest capture) |
| `community-housing-providers-adoption-of-national-law-regulation-2023/` | Community Housing Providers (Adoption of National Law) Regulation 2023 | 1 | Current text: the version in force from 2023-08-25 (newest capture) |
| `childcare-and-economic-opportunity-fund-regulation-2023/` | Childcare and Economic Opportunity Fund Regulation 2023 | 1 | Current text: the version in force from 2023-12-01 (newest capture) |
| `marine-pollution-regulation-2024/` | Marine Pollution Regulation 2024 | 1 | Current text: the version in force from 2024-11-29 (newest capture) |
| `government-sector-finance-regulation-2024/` | Government Sector Finance Regulation 2024 | 1 | Current text: the version in force from 2025-07-01 (newest capture) |
| `poppy-industry-regulation-2024/` | Poppy Industry Regulation 2024 | 1 | Current text: the version in force from 2024-06-28 (newest capture) |
| `trees-disputes-between-neighbours-regulation-2024/` | Trees (Disputes Between Neighbours) Regulation 2024 | 1 | Current text: the version in force from 2024-08-16 (newest capture) |
| `apprenticeship-and-traineeship-regulation-2024/` | Apprenticeship and Traineeship Regulation 2024 | 1 | Current text: the version in force from 2024-08-23 (newest capture) |
| `government-advertising-regulation-2024/` | Government Advertising Regulation 2024 | 1 | Current text: the version in force from 2024-11-21 (newest capture) |
| `powers-of-attorney-regulation-2024/` | Powers of Attorney Regulation 2024 | 1 | Current text: the version in force from 2024-08-23 (newest capture) |
| `state-records-regulation-2024/` | State Records Regulation 2024 | 1 | Current text: the version in force from 2024-08-23 (newest capture) |
| `explosives-regulation-2024/` | Explosives Regulation 2024 | 1 | Current text: the version in force from 2025-08-15 (newest capture) |
| `private-health-facilities-regulation-2024/` | Private Health Facilities Regulation 2024 | 1 | Current text: the version in force from 2025-09-01 (newest capture) |
| `surveying-and-spatial-information-regulation-2024/` | Surveying and Spatial Information Regulation 2024 | 1 | Current text: the version in force from 2024-11-29 (newest capture) |
| `environmental-planning-and-assessment-housing-delivery-authority-order-2024/` | Environmental Planning and Assessment (Housing Delivery Authority) Order 2024 | 1 | Current text: the version in force from 2024-12-19 (newest capture) |
| `prevention-of-cruelty-to-animals-regulation-2025/` | Prevention of Cruelty to Animals Regulation 2025 | 1 | Current text: the version in force from 2025-01-31 (newest capture) |
| `uncollected-goods-regulation-2025/` | Uncollected Goods Regulation 2025 | 1 | Current text: the version in force from 2025-05-30 (newest capture) |
| `border-fence-maintenance-regulation-2025/` | Border Fence Maintenance Regulation 2025 | 1 | Current text: the version in force from 2025-08-22 (newest capture) |
| `health-practitioner-regulation-new-south-wales-regulation-2025/` | Health Practitioner Regulation (New South Wales) Regulation 2025 | 1 | Current text: the version in force from 2025-08-22 (newest capture) |
| `work-health-and-safety-regulation-2025/` | Work Health and Safety Regulation 2025 | 1 | Current text: the version in force from 2025-10-03 (newest capture) |
| `protection-from-harmful-radiation-regulation-2025/` | Protection from Harmful Radiation Regulation 2025 | 1 | Current text: the version in force from 2025-08-29 (newest capture) |

## Where the text comes from

The text is each instrument in the table as shown on the NSW legislation website of the Parliamentary Counsel's Office (legislation.nsw.gov.au), the whole-Act view of the version in force. The site cannot be read by script, so each version is read from an Internet Archive capture of that page; the page names the date the version is in force from (its point-in-time date). Six distinct versions were captured between 2020 and December 2025, and the latest was retrieved on 29 October 2026 from the archive.

Language: English.

## Not included yet

- Versions between two captures, and every version before March 2020. The site holds the full history; this record only has what was captured.
- The Act that made each change. The captures do not say which Act amended which section, so every change after the first version is committed by the publisher and labelled unexplained. The site's history notes name the amending Acts but are not in the text here.
- Every New South Wales Act, regulation or planning instrument not in the table: those the Internet Archive has not captured since 1 January 2025 (some may since have been repealed or remade).
- For all but the four core Acts, every version before the newest captured one.

## Dates

Each version is dated by the point-in-time date the NSW legislation website gives for it, which is the day that version came into force. For the four core Acts the first version is the oldest one captured, not the Act's first text. For every other instrument the one version is its current text, dated the day that version came into force (usually the commencement of its latest amendment); it is credited to the publisher because the page does not name the amending law, and it says nothing about the text before that day. Commits are dated noon, Australia/Sydney.

## How it is checked

Every version is read back from git on the day it took effect and on the day before; both must match the corpus the repository was built from. The results are in `REPRODUCE.md`.

## How it is built

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `tools/build.py` writes this repository from that file, and the same corpus always gives the same commit hashes; `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file.

## What "author" means

The author of a commit is the law that made the change. Its e-mail address cannot exist, so `git blame` and `git log --author` name laws. A version with no law of its own (the oldest version available) is authored by the publisher and says so. The committer is always Lexifina.
