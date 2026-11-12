# S0 vs S1 — completed relevance review (draft)

**Based on:** [original `eval/runs/s0_vs_s1.md`](https://github.com/FreddieAlvin/Strasbourg-Engine/blob/s0-vs-s1-evaluation/eval/runs/s0_vs_s1.md), branch `s0-vs-s1-evaluation`; [evaluation criteria](https://github.com/FreddieAlvin/Strasbourg-Engine/blob/s0-vs-s1-evaluation/eval/needs.json).

**Important:** This is an annotated, regenerated review sheet, not a modification pushed to the GitHub repo. All 140 retrieved positions are rated; duplicate cases within the same topic get the same rating. Some judgments are **provisional** and need a human check of the full decision before being treated as final research ground truth. The original Solr scores/snippets remain in the source file linked above.

Scale from `needs.json`: **yes = 2** (central), **kinda = 1** (partial/secondary), **no = 0** (not relevant). A rating is about topical relevance, **not** whether the ECtHR ruled that a violation occurred.

## Evaluation summary

| Topic | S0 yes/kinda/no | S1 yes/kinda/no | S0 strict P@10 | S1 strict P@10 | S0 graded@10 | S1 graded@10 |
|---|---:|---:|---:|---:|---:|---:|
| IN1 | 10/0/0 | 10/0/0 | 1.00 | 1.00 | 1.00 | 1.00 |
| IN2 | 8/0/2 | 9/1/0 | 0.80 | 0.90 | 0.80 | 0.95 |
| IN3 | 7/1/2 | 10/0/0 | 0.70 | 1.00 | 0.75 | 1.00 |
| IN4 | 5/0/5 | 6/0/4 | 0.50 | 0.60 | 0.50 | 0.60 |
| IN5 | 10/0/0 | 10/0/0 | 1.00 | 1.00 | 1.00 | 1.00 |
| IN6 | 10/0/0 | 10/0/0 | 1.00 | 1.00 | 1.00 | 1.00 |
| IN7 | 9/1/0 | 9/1/0 | 0.90 | 0.90 | 0.95 | 0.95 |

**Interpretation:** strict P@10 counts only `yes`. `graded@10 = sum(relevance scores)/20` gives `kinda` half credit; this is a simple average graded relevance score, *not* nDCG@10. Differences in raw Solr scores across S0 and S1 must not be taken as a quality metric.

## IN1 — Confessions coerced by police ill-treatment

- **Query:** `confession coerced by police beating ill-treatment`

### S0 — Simple (lowercase only)

| Rank | HUDOC ID / case | match? | Why | Confidence |
|---:|---|---|---|---|
| 1 | [001-153349](https://hudoc.echr.coe.int/eng?i=001-153349) — Nalbandyan v. Armenia | **yes** | Applicant alleges police beatings to force a murder confession. | high |
| 2 | [001-78369](https://hudoc.echr.coe.int/eng?i=001-78369) — Sheydayev v. Russia | **yes** | Confession allegedly extracted under duress in police custody. | high |
| 3 | [001-81352](https://hudoc.echr.coe.int/eng?i=001-81352) — Harutyunyan v. Armenia | **yes** | Confession and witness statements obtained by police torture. | high |
| 4 | [001-186723](https://hudoc.echr.coe.int/eng?i=001-186723) — Golubyatnikov and Zhuchkov v. Russia | **yes** | Co-defendant confession allegedly obtained through police ill-treatment. | high |
| 5 | [001-145580](https://hudoc.echr.coe.int/eng?i=001-145580) — Osakovskiy v. Ukraine | **yes** | Allegation of coercion and use of forced incriminating statements. | medium |
| 6 | [001-180827](https://hudoc.echr.coe.int/eng?i=001-180827) — Ulay v. Turkey | **yes** | Explicit allegation of police threats and ill-treatment to force a confession. | high |
| 7 | [001-182845](https://hudoc.echr.coe.int/eng?i=001-182845) — Sergey Ivanov v. Russia | **yes** | Police-ill-treatment and confession-related criminal proceedings. | medium |
| 8 | [001-101321](https://hudoc.echr.coe.int/eng?i=001-101321) — Leonid Lazarenko v. Ukraine | **yes** | Claim of police coercion in connection with incriminating statements. | high |
| 9 | [001-191483](https://hudoc.echr.coe.int/eng?i=001-191483) — Gabbazov v. Russia | **yes** | Police beat applicant and coerced another suspect to confess; applicant refused to sign. | medium |
| 10 | [001-115307](https://hudoc.echr.coe.int/eng?i=001-115307) — Dvalishvili v. Georgia | **yes** | Defence explicitly said pre-trial confession was extracted by ill-treatment. | high |

### S1 — English (stemming + stopwords)

| Rank | HUDOC ID / case | match? | Why | Confidence |
|---:|---|---|---|---|
| 1 | [001-153349](https://hudoc.echr.coe.int/eng?i=001-153349) — Nalbandyan v. Armenia | **yes** | Applicant alleges police beatings to force a murder confession. | high |
| 2 | [001-81352](https://hudoc.echr.coe.int/eng?i=001-81352) — Harutyunyan v. Armenia | **yes** | Confession and witness statements obtained by police torture. | high |
| 3 | [001-78369](https://hudoc.echr.coe.int/eng?i=001-78369) — Sheydayev v. Russia | **yes** | Confession allegedly extracted under duress in police custody. | high |
| 4 | [001-191483](https://hudoc.echr.coe.int/eng?i=001-191483) — Gabbazov v. Russia | **yes** | Police beat applicant and coerced another suspect to confess; applicant refused to sign. | medium |
| 5 | [001-182845](https://hudoc.echr.coe.int/eng?i=001-182845) — Sergey Ivanov v. Russia | **yes** | Police-ill-treatment and confession-related criminal proceedings. | medium |
| 6 | [001-159759](https://hudoc.echr.coe.int/eng?i=001-159759) — Minikayev v. Russia | **yes** | Police interrogation leading to a contested robbery confession. | medium |
| 7 | [001-101321](https://hudoc.echr.coe.int/eng?i=001-101321) — Leonid Lazarenko v. Ukraine | **yes** | Claim of police coercion in connection with incriminating statements. | high |
| 8 | [001-147038](https://hudoc.echr.coe.int/eng?i=001-147038) — Mostipan v. Russia | **yes** | Applicant said police ill-treatment forced her to confess. | high |
| 9 | [001-145580](https://hudoc.echr.coe.int/eng?i=001-145580) — Osakovskiy v. Ukraine | **yes** | Allegation of coercion and use of forced incriminating statements. | medium |
| 10 | [001-191928](https://hudoc.echr.coe.int/eng?i=001-191928) — Konyayev v. Russia | **yes** | Police allegedly beat and electroshocked applicant to force confessions. | high |

## IN2 — Journalists sanctioned for articles about public figures

- **Query:** `journalist convicted defamation article about politician public official`

### S0 — Simple (lowercase only)

| Rank | HUDOC ID / case | match? | Why | Confidence |
|---:|---|---|---|---|
| 1 | [001-151007](https://hudoc.echr.coe.int/eng?i=001-151007) — Cojocaru v. Romania | **yes** | Journalistic publication involving a mayor/politician and Article 10 sanctions. | medium |
| 2 | [001-61441](https://hudoc.echr.coe.int/eng?i=001-61441) — Scharsach and News Verlagsgesellschaft v. Austria | **yes** | Media liability for criticism of a political/public figure. | high |
| 3 | [001-113919](https://hudoc.echr.coe.int/eng?i=001-113919) — Jucha and Żak v. Poland | **yes** | Journalist and editor convicted for articles about a local councillor. | high |
| 4 | [001-77831](https://hudoc.echr.coe.int/eng?i=001-77831) — Standard Verlags GmbH and Krawagna-Pfeifer v. Austria | **yes** | Media sanctions concerning the credibility of a politician. | high |
| 5 | [001-105557](https://hudoc.echr.coe.int/eng?i=001-105557) — Wizerkaniuk v. Poland | **yes** | Journalist punished for publishing an interview with a politician. | medium |
| 6 | [001-126629](https://hudoc.echr.coe.int/eng?i=001-126629) — Print Zeitungsverlag GmbH v. Austria | **yes** | Publisher sanctioned in relation to article about a public/local political figure. | medium |
| 7 | [001-91475](https://hudoc.echr.coe.int/eng?i=001-91475) — Długołęcki v. Poland | **yes** | Journalist fined for published criticism of a village mayor. | high |
| 8 | [001-112432](https://hudoc.echr.coe.int/eng?i=001-112432) — Ziembiński v. Poland | **yes** | Defamation conviction for articles concerning a district mayor. | high |
| 9 | [001-184654](https://hudoc.echr.coe.int/eng?i=001-184654) — Makraduli v. North Macedonia | **no** | Applicant was a politician speaking at a press conference, not a journalist or publisher. | high |
| 10 | [001-111626](https://hudoc.echr.coe.int/eng?i=001-111626) — Ciesielczyk v. Poland | **no** | Sanction concerned statements about a journalist rather than a public official. | medium |

### S1 — English (stemming + stopwords)

| Rank | HUDOC ID / case | match? | Why | Confidence |
|---:|---|---|---|---|
| 1 | [001-151007](https://hudoc.echr.coe.int/eng?i=001-151007) — Cojocaru v. Romania | **yes** | Journalistic publication involving a mayor/politician and Article 10 sanctions. | medium |
| 2 | [001-79591](https://hudoc.echr.coe.int/eng?i=001-79591) — Falter Zeitschriften GmbH v. Austria | **yes** | Newspaper ordered to pay politician over published criticism. | high |
| 3 | [001-95810](https://hudoc.echr.coe.int/eng?i=001-95810) — Flux v. Moldova (No. 7) | **yes** | Newspaper defamation dispute concerning a public official. | medium |
| 4 | [001-113919](https://hudoc.echr.coe.int/eng?i=001-113919) — Jucha and Żak v. Poland | **yes** | Journalist and editor convicted for articles about a local councillor. | high |
| 5 | [001-67457](https://hudoc.echr.coe.int/eng?i=001-67457) — Karhuvaara and Iltalehti v. Finland | **kinda** | Article primarily about criminal conduct of politician’s husband, though the MP was named. | high |
| 6 | [001-61441](https://hudoc.echr.coe.int/eng?i=001-61441) — Scharsach and News Verlagsgesellschaft v. Austria | **yes** | Media liability for criticism of a political/public figure. | high |
| 7 | [001-77786](https://hudoc.echr.coe.int/eng?i=001-77786) — Kobenter and Standard Verlags GmbH v. Austria | **yes** | Publication criticised a judge; ensuing media-liability proceedings. | high |
| 8 | [001-112432](https://hudoc.echr.coe.int/eng?i=001-112432) — Ziembiński v. Poland | **yes** | Defamation conviction for articles concerning a district mayor. | high |
| 9 | [001-109189](https://hudoc.echr.coe.int/eng?i=001-109189) — Tuşalp v. Turkey | **yes** | Damages for an article criticising the Prime Minister. | high |
| 10 | [001-80865](https://hudoc.echr.coe.int/eng?i=001-80865) — Gorelishvili v. Georgia | **yes** | Journalist ordered to compensate a politician over reporting. | high |

## IN3 — Unfair trial due to restricted access to evidence or witnesses

- **Query:** `fair trial no access to classified evidence unable to cross-examine witnesses`

### S0 — Simple (lowercase only)

| Rank | HUDOC ID / case | match? | Why | Confidence |
|---:|---|---|---|---|
| 1 | [001-167538](https://hudoc.echr.coe.int/eng?i=001-167538) — Constantinides v. Greece | **yes** | Applicant was unable to cross-examine a key witness. | high |
| 2 | [001-105764](https://hudoc.echr.coe.int/eng?i=001-105764) — Liu v. Russia (No. 2) | **no** | Case is primarily about expulsion/family life, not evidence or witnesses in a trial. | high |
| 3 | [001-108072](https://hudoc.echr.coe.int/eng?i=001-108072) — Al-Khawaja and Tahery v. UK | **yes** | Conviction relied on absent witnesses whose statements could not be challenged. | high |
| 4 | [001-102282](https://hudoc.echr.coe.int/eng?i=001-102282) — Trepashkin v. Russia (No. 2) | **kinda** | Some case-file access restricted to court premises; lawyers could access materials. | high |
| 5 | [001-154022](https://hudoc.echr.coe.int/eng?i=001-154022) — Yaremenko v. Ukraine (No. 2) | **yes** | Request to cross-examine a key witness was refused. | high |
| 6 | [001-81682](https://hudoc.echr.coe.int/eng?i=001-81682) — Gecas v. Lithuania | **yes** | Fair-trial dispute involving access to classified evidence. | medium |
| 7 | [001-96033](https://hudoc.echr.coe.int/eng?i=001-96033) — Caka v. Albania | **yes** | Defence raised refusal to permit cross-examination of a witness. | high |
| 8 | [001-178174](https://hudoc.echr.coe.int/eng?i=001-178174) — Kamenos v. Cyprus | **no** | Article 6 complaint concerns judge impartiality/disciplinary tribunal structure. | high |
| 9 | [001-110445](https://hudoc.echr.coe.int/eng?i=001-110445) — Damir Sibgatullin v. Russia | **yes** | Defence alleged inability to cross-examine prosecution witnesses. | high |
| 10 | [001-138919](https://hudoc.echr.coe.int/eng?i=001-138919) — Donohoe v. Ireland | **yes** | Fair-trial dispute over undisclosed material underlying police expert belief. | high |

### S1 — English (stemming + stopwords)

| Rank | HUDOC ID / case | match? | Why | Confidence |
|---:|---|---|---|---|
| 1 | [001-102637](https://hudoc.echr.coe.int/eng?i=001-102637) — McKeown v. UK | **yes** | Disclosure of withheld prosecution evidence central to Article 6 complaint. | high |
| 2 | [001-105823](https://hudoc.echr.coe.int/eng?i=001-105823) — Huseyn and Others v. Azerbaijan | **yes** | Defence objections to key testimony and requested witnesses central to the case. | high |
| 3 | [001-108072](https://hudoc.echr.coe.int/eng?i=001-108072) — Al-Khawaja and Tahery v. UK | **yes** | Conviction relied on absent witnesses whose statements could not be challenged. | high |
| 4 | [001-90677](https://hudoc.echr.coe.int/eng?i=001-90677) — Taxquet v. Belgium | **yes** | Applicant could not examine anonymous informer; Article 6 issue. | high |
| 5 | [001-175667](https://hudoc.echr.coe.int/eng?i=001-175667) — M v. the Netherlands | **yes** | Security-sensitive classified materials restricted the defence. | medium |
| 6 | [001-167538](https://hudoc.echr.coe.int/eng?i=001-167538) — Constantinides v. Greece | **yes** | Applicant was unable to cross-examine a key witness. | high |
| 7 | [001-148673](https://hudoc.echr.coe.int/eng?i=001-148673) — Horncastle and Others v. UK | **yes** | Hearsay/absent witnesses and cross-examination central to Article 6 issue. | high |
| 8 | [001-138919](https://hudoc.echr.coe.int/eng?i=001-138919) — Donohoe v. Ireland | **yes** | Fair-trial dispute over undisclosed material underlying police expert belief. | high |
| 9 | [001-81682](https://hudoc.echr.coe.int/eng?i=001-81682) — Gecas v. Lithuania | **yes** | Fair-trial dispute involving access to classified evidence. | medium |
| 10 | [001-154022](https://hudoc.echr.coe.int/eng?i=001-154022) — Yaremenko v. Ukraine (No. 2) | **yes** | Request to cross-examine a key witness was refused. | high |

## IN4 — Bans on religious symbols and clothing

- **Query:** `ban on wearing religious symbols headscarf veil school workplace`

### S0 — Simple (lowercase only)

| Rank | HUDOC ID / case | match? | Why | Confidence |
|---:|---|---|---|---|
| 1 | [001-175660](https://hudoc.echr.coe.int/eng?i=001-175660) — Dakir v. Belgium | **yes** | Restriction on wearing a full-face veil in public. | high |
| 2 | [001-90039](https://hudoc.echr.coe.int/eng?i=001-90039) — Dogru v. France | **yes** | School expulsion for refusing to remove religious headscarf. | high |
| 3 | [001-159070](https://hudoc.echr.coe.int/eng?i=001-159070) — Ebrahimian v. France | **yes** | Hospital employee contract not renewed over wearing headscarf. | high |
| 4 | [001-180506](https://hudoc.echr.coe.int/eng?i=001-180506) — Sekmadienis Ltd. v. Lithuania | **no** | Religious imagery in commercial advertisements, not clothing or religious displays in institutions. | high |
| 5 | [001-70956](https://hudoc.echr.coe.int/eng?i=001-70956) — Leyla Şahin v. Turkey | **yes** | University headscarf prohibition. | high |
| 6 | [001-144129](https://hudoc.echr.coe.int/eng?i=001-144129) — Mustafa Erdoğan and Others v. Turkey | **no** | Article 10 case about published criticism; headscarf restrictions merely discussed. | high |
| 7 | [001-104040](https://hudoc.echr.coe.int/eng?i=001-104040) — Lautsi and Others v. Italy | **yes** | Controversy over display of religious crucifixes in state-school classrooms. | high |
| 8 | [001-187904](https://hudoc.echr.coe.int/eng?i=001-187904) — Urat v. Turkey | **no** | Religious dress of a third party mentioned in employment/fair-trial proceedings. | high |
| 9 | [001-99384](https://hudoc.echr.coe.int/eng?i=001-99384) — Grzelak v. Poland | **no** | Religious education grade/exemption dispute, not a symbol or clothing restriction. | high |
| 10 | [001-121567](https://hudoc.echr.coe.int/eng?i=001-121567) — M.Y.H. and Others v. Sweden | **no** | Asylum claim about persecution abroad; no challenged institutional dress ban. | high |

### S1 — English (stemming + stopwords)

| Rank | HUDOC ID / case | match? | Why | Confidence |
|---:|---|---|---|---|
| 1 | [001-159070](https://hudoc.echr.coe.int/eng?i=001-159070) — Ebrahimian v. France | **yes** | Hospital employee contract not renewed over wearing headscarf. | high |
| 2 | [001-90039](https://hudoc.echr.coe.int/eng?i=001-90039) — Dogru v. France | **yes** | School expulsion for refusing to remove religious headscarf. | high |
| 3 | [001-175660](https://hudoc.echr.coe.int/eng?i=001-175660) — Dakir v. Belgium | **yes** | Restriction on wearing a full-face veil in public. | high |
| 4 | [001-70956](https://hudoc.echr.coe.int/eng?i=001-70956) — Leyla Şahin v. Turkey | **yes** | University headscarf prohibition. | high |
| 5 | [001-104040](https://hudoc.echr.coe.int/eng?i=001-104040) — Lautsi and Others v. Italy | **yes** | Controversy over display of religious crucifixes in state-school classrooms. | high |
| 6 | [001-145466](https://hudoc.echr.coe.int/eng?i=001-145466) — S.A.S. v. France | **yes** | Nationwide prohibition on full-face veil in public places. | high |
| 7 | [001-180506](https://hudoc.echr.coe.int/eng?i=001-180506) — Sekmadienis Ltd. v. Lithuania | **no** | Religious imagery in commercial advertisements, not clothing or religious displays in institutions. | high |
| 8 | [001-144129](https://hudoc.echr.coe.int/eng?i=001-144129) — Mustafa Erdoğan and Others v. Turkey | **no** | Article 10 case about published criticism; headscarf restrictions merely discussed. | high |
| 9 | [001-121567](https://hudoc.echr.coe.int/eng?i=001-121567) — M.Y.H. and Others v. Sweden | **no** | Asylum claim about persecution abroad; no challenged institutional dress ban. | high |
| 10 | [001-60936](https://hudoc.echr.coe.int/eng?i=001-60936) — Refah Partisi and Others v. Turkey | **no** | Dissolution of a political party; remarks about headscarves incidental. | high |

## IN5 — Overcrowded and unsanitary detention in Southern European states

- **Query:** `overcrowded prison cells poor sanitary conditions`
- **Filter:** Southern Europe state filter as specified in `needs.json` (unchanged).

### S0 — Simple (lowercase only)

| Rank | HUDOC ID / case | match? | Why | Confidence |
|---:|---|---|---|---|
| 1 | [001-72704](https://hudoc.echr.coe.int/eng?i=001-72704) — Cenbauer v. Croatia | **yes** | Overcrowded prison, insufficient toiletries and poor hygiene. | high |
| 2 | [001-113387](https://hudoc.echr.coe.int/eng?i=001-113387) — Dimitrios Dimopoulos v. Greece | **yes** | Complaint about material conditions of detention in Greece. | medium |
| 3 | [001-167483](https://hudoc.echr.coe.int/eng?i=001-167483) — Muršić v. Croatia | **yes** | Personal cell space and prison overcrowding central to the case. | high |
| 4 | [001-148283](https://hudoc.echr.coe.int/eng?i=001-148283) — Pozaić v. Croatia | **yes** | Prison-cell crowding and material conditions explicitly disputed. | high |
| 5 | [001-170837](https://hudoc.echr.coe.int/eng?i=001-170837) — Igbo and Others v. Greece | **yes** | Greek prison overcrowding and material detention conditions. | high |
| 6 | [001-156245](https://hudoc.echr.coe.int/eng?i=001-156245) — Martzaklis and Others v. Greece | **yes** | Prison accommodation and inadequate conditions for detainees. | medium |
| 7 | [001-182869](https://hudoc.echr.coe.int/eng?i=001-182869) — Zabelos and Others v. Greece | **yes** | Complaints about poor conditions of detention. | medium |
| 8 | [001-172855](https://hudoc.echr.coe.int/eng?i=001-172855) — Cela and Others v. Greece | **yes** | Overcrowding and material conditions at Korydallos prison. | high |
| 9 | [001-182447](https://hudoc.echr.coe.int/eng?i=001-182447) — Tsarpelas v. Greece | **yes** | Complaint about detention conditions in Greek prison. | medium |
| 10 | [001-170704](https://hudoc.echr.coe.int/eng?i=001-170704) — Singh and Others v. Greece | **yes** | Overcrowding, poor facilities, nutrition and in-cell conditions. | high |

### S1 — English (stemming + stopwords)

| Rank | HUDOC ID / case | match? | Why | Confidence |
|---:|---|---|---|---|
| 1 | [001-72704](https://hudoc.echr.coe.int/eng?i=001-72704) — Cenbauer v. Croatia | **yes** | Overcrowded prison, insufficient toiletries and poor hygiene. | high |
| 2 | [001-113387](https://hudoc.echr.coe.int/eng?i=001-113387) — Dimitrios Dimopoulos v. Greece | **yes** | Complaint about material conditions of detention in Greece. | medium |
| 3 | [001-184485](https://hudoc.echr.coe.int/eng?i=001-184485) — Daoukopoulos v. Greece | **yes** | Less than 3 sqm per inmate, inadequate ventilation and sanitation. | high |
| 4 | [001-60728](https://hudoc.echr.coe.int/eng?i=001-60728) — Benzan v. Croatia | **yes** | Overcrowded, dilapidated prison with poor facilities. | high |
| 5 | [001-167483](https://hudoc.echr.coe.int/eng?i=001-167483) — Muršić v. Croatia | **yes** | Personal cell space and prison overcrowding central to the case. | high |
| 6 | [001-139924](https://hudoc.echr.coe.int/eng?i=001-139924) — Jevsnik v. Slovenia | **yes** | Prison conditions and personal living space in Slovenia. | medium |
| 7 | [001-170837](https://hudoc.echr.coe.int/eng?i=001-170837) — Igbo and Others v. Greece | **yes** | Greek prison overcrowding and material detention conditions. | high |
| 8 | [001-148283](https://hudoc.echr.coe.int/eng?i=001-148283) — Pozaić v. Croatia | **yes** | Prison-cell crowding and material conditions explicitly disputed. | high |
| 9 | [001-148284](https://hudoc.echr.coe.int/eng?i=001-148284) — Lonić v. Croatia | **yes** | Shared overcrowded cell with poor hygiene conditions. | high |
| 10 | [001-156245](https://hudoc.echr.coe.int/eng?i=001-156245) — Martzaklis and Others v. Greece | **yes** | Prison accommodation and inadequate conditions for detainees. | medium |

## IN6 — Expulsion or extradition to a risk of torture

- **Query:** `extradition deportation risk of torture ill-treatment in receiving country`

### S0 — Simple (lowercase only)

| Rank | HUDOC ID / case | match? | Why | Confidence |
|---:|---|---|---|---|
| 1 | [001-101586](https://hudoc.echr.coe.int/eng?i=001-101586) — Sultanov v. Russia | **yes** | Extradition and substantial risk of ill-treatment in receiving state. | high |
| 2 | [001-100198](https://hudoc.echr.coe.int/eng?i=001-100198) — Karimov v. Russia | **yes** | Extradition risk of torture in destination country. | high |
| 3 | [001-99796](https://hudoc.echr.coe.int/eng?i=001-99796) — Yuldashev v. Russia | **yes** | Risk of torture following extradition. | high |
| 4 | [001-116330](https://hudoc.echr.coe.int/eng?i=001-116330) — Zokhidov v. Russia | **yes** | Applicant challenged extradition given risk of torture/ill-treatment. | high |
| 5 | [001-86086](https://hudoc.echr.coe.int/eng?i=001-86086) — Ismoilov and Others v. Russia | **yes** | Uzbekistan extradition and real risk of torture. | high |
| 6 | [001-99798](https://hudoc.echr.coe.int/eng?i=001-99798) — Abdulazhon Isakov v. Russia | **yes** | Extradition to receiving state with serious ill-treatment risk. | high |
| 7 | [001-108629](https://hudoc.echr.coe.int/eng?i=001-108629) — Othman (Abu Qatada) v. UK | **yes** | Proposed deportation to Jordan and Article 3 risk assessment. | high |
| 8 | [001-108162](https://hudoc.echr.coe.int/eng?i=001-108162) — Ergashev v. Russia | **yes** | Extradition and danger of ill-treatment in receiving country. | high |
| 9 | [001-145788](https://hudoc.echr.coe.int/eng?i=001-145788) — Tershiyev v. Azerbaijan | **yes** | Removal/extradition and risks facing applicant in destination. | medium |
| 10 | [001-147333](https://hudoc.echr.coe.int/eng?i=001-147333) — Mamazhonov v. Russia | **yes** | Uzbekistan extradition and anticipated risk of torture. | high |

### S1 — English (stemming + stopwords)

| Rank | HUDOC ID / case | match? | Why | Confidence |
|---:|---|---|---|---|
| 1 | [001-100198](https://hudoc.echr.coe.int/eng?i=001-100198) — Karimov v. Russia | **yes** | Extradition risk of torture in destination country. | high |
| 2 | [001-99798](https://hudoc.echr.coe.int/eng?i=001-99798) — Abdulazhon Isakov v. Russia | **yes** | Extradition to receiving state with serious ill-treatment risk. | high |
| 3 | [001-101586](https://hudoc.echr.coe.int/eng?i=001-101586) — Sultanov v. Russia | **yes** | Extradition and substantial risk of ill-treatment in receiving state. | high |
| 4 | [001-86086](https://hudoc.echr.coe.int/eng?i=001-86086) — Ismoilov and Others v. Russia | **yes** | Uzbekistan extradition and real risk of torture. | high |
| 5 | [001-99796](https://hudoc.echr.coe.int/eng?i=001-99796) — Yuldashev v. Russia | **yes** | Risk of torture following extradition. | high |
| 6 | [001-116330](https://hudoc.echr.coe.int/eng?i=001-116330) — Zokhidov v. Russia | **yes** | Applicant challenged extradition given risk of torture/ill-treatment. | high |
| 7 | [001-108162](https://hudoc.echr.coe.int/eng?i=001-108162) — Ergashev v. Russia | **yes** | Extradition and danger of ill-treatment in receiving country. | high |
| 8 | [001-128055](https://hudoc.echr.coe.int/eng?i=001-128055) — Kasymakhunov v. Russia | **yes** | Applicant explicitly alleged torture risk if extradited to Uzbekistan. | high |
| 9 | [001-108629](https://hudoc.echr.coe.int/eng?i=001-108629) — Othman (Abu Qatada) v. UK | **yes** | Proposed deportation to Jordan and Article 3 risk assessment. | high |
| 10 | [001-183361](https://hudoc.echr.coe.int/eng?i=001-183361) — Batyrkhairov v. Turkey | **yes** | Extradition challenge based on alleged risk of torture in home country. | high |

## IN7 — Civilian casualties from bombardment and shelling

- **Query:** `aerial bombardment shelling civilians killed military operation`

### S0 — Simple (lowercase only)

| Rank | HUDOC ID / case | match? | Why | Confidence |
|---:|---|---|---|---|
| 1 | [001-101936](https://hudoc.echr.coe.int/eng?i=001-101936) — Abuyeva and Others v. Russia | **yes** | Civilian deaths and injuries in air/artillery attack on Katyr-Yurt. | high |
| 2 | [001-68381](https://hudoc.echr.coe.int/eng?i=001-68381) — Isayeva v. Russia | **yes** | Military bombardment of inhabited village causing civilian losses. | high |
| 3 | [001-83578](https://hudoc.echr.coe.int/eng?i=001-83578) — Tangiyeva v. Russia | **kinda** | Relatives killed amid fighting; gunshot deaths central, shelling explanation contested. | high |
| 4 | [001-90029](https://hudoc.echr.coe.int/eng?i=001-90029) — Umayeva v. Russia | **yes** | Civilian harm in Grozny during aerial/artillery bombardment. | medium |
| 5 | [001-104159](https://hudoc.echr.coe.int/eng?i=001-104159) — Esmukhambetov and Others v. Russia | **yes** | Military operations affecting civilians and their homes. | medium |
| 6 | [001-157697](https://hudoc.echr.coe.int/eng?i=001-157697) — Abakarova v. Russia | **yes** | Applicant wounded and family killed in village airstrikes/shelling. | high |
| 7 | [001-82544](https://hudoc.echr.coe.int/eng?i=001-82544) — Goncharuk v. Russia | **yes** | Applicant wounded while escaping shelling. | high |
| 8 | [001-159789](https://hudoc.echr.coe.int/eng?i=001-159789) — Treskavica v. Croatia | **yes** | Civilian death during artillery shelling of Knin. | high |
| 9 | [001-110944](https://hudoc.echr.coe.int/eng?i=001-110944) — Damayev v. Russia | **yes** | Woman and five children killed in aerial bombardment. | high |
| 10 | [001-68379](https://hudoc.echr.coe.int/eng?i=001-68379) — Isayeva, Yusupova and Bazayeva v. Russia | **yes** | Civilians killed/injured by aerial strike on civilian convoy. | high |

### S1 — English (stemming + stopwords)

| Rank | HUDOC ID / case | match? | Why | Confidence |
|---:|---|---|---|---|
| 1 | [001-110944](https://hudoc.echr.coe.int/eng?i=001-110944) — Damayev v. Russia | **yes** | Woman and five children killed in aerial bombardment. | high |
| 2 | [001-101936](https://hudoc.echr.coe.int/eng?i=001-101936) — Abuyeva and Others v. Russia | **yes** | Civilian deaths and injuries in air/artillery attack on Katyr-Yurt. | high |
| 3 | [001-68381](https://hudoc.echr.coe.int/eng?i=001-68381) — Isayeva v. Russia | **yes** | Military bombardment of inhabited village causing civilian losses. | high |
| 4 | [001-83578](https://hudoc.echr.coe.int/eng?i=001-83578) — Tangiyeva v. Russia | **kinda** | Relatives killed amid fighting; gunshot deaths central, shelling explanation contested. | high |
| 5 | [001-68379](https://hudoc.echr.coe.int/eng?i=001-68379) — Isayeva, Yusupova and Bazayeva v. Russia | **yes** | Civilians killed/injured by aerial strike on civilian convoy. | high |
| 6 | [001-82544](https://hudoc.echr.coe.int/eng?i=001-82544) — Goncharuk v. Russia | **yes** | Applicant wounded while escaping shelling. | high |
| 7 | [001-104649](https://hudoc.echr.coe.int/eng?i=001-104649) — Khamzayev and Others v. Russia | **yes** | Airstrikes killed civilians and destroyed/damaged homes. | high |
| 8 | [001-104159](https://hudoc.echr.coe.int/eng?i=001-104159) — Esmukhambetov and Others v. Russia | **yes** | Military operations affecting civilians and their homes. | medium |
| 9 | [001-90029](https://hudoc.echr.coe.int/eng?i=001-90029) — Umayeva v. Russia | **yes** | Civilian harm in Grozny during aerial/artillery bombardment. | medium |
| 10 | [001-104662](https://hudoc.echr.coe.int/eng?i=001-104662) — Kerimova and Others v. Russia | **yes** | Airstrike on residential building killed/injured civilians. | high |

## Examples and methodological notes

- **Clear S1 advantage (IN4):** `S.A.S. v. France` (S1 #6) directly concerns a full-face veil prohibition (`yes`), whereas S0 has `Urat v. Turkey` (#8) and `Grzelak v. Poland` (#9) (`no`).
- **S0-exclusive useful case, not proof S0 wins overall:** `Treskavica v. Croatia` (IN7, S0 #8) concerns civilian death during shelling and is absent from S1 top 10. However, the other S1-only cases also appear relevant; do **not** claim S0 has better overall relevance for IN7 based on this alone.
- **S0-exclusive useful case (IN1):** `Ulay v. Turkey` (S0 #6) directly alleges police pressure to obtain an incriminating confession; both S0 and S1 still score highly on that topic.
- **No established S0-winning topic:** On the current relevance labels, we cannot defensibly show a topic on which S0 beats S1 on P@10. That is a legitimate finding; do not manufacture a winner. If a slide requires such an example, use an individual S0-only useful case or evaluate rank-sensitive nDCG@10 with verified labels.
- **IN5 filter:** It appears consistent with the team’s declared definition, which adopts the UN M49 Southern Europe region plus Cyprus. The team should explicitly confirm that chosen geographic definition, especially the inclusion of Cyprus and exclusion of Turkey/Bulgaria.
- **Confidence:** `high` = supported by visible excerpts and/or accessible case summaries; `medium` = plausible assessment that particularly merits reading the complete HUDOC judgment before final submission.
- **No automated label inference from Solr scores:** Every result was assigned a topical label against the narratives in `needs.json`; Solr score is solely ranking evidence.

## Selected sources used for case checks

- [Harutyunyan v. Armenia — ECtHR reports summary](https://ks.echr.coe.int/documents/d/echr-ks/reports_recueil_2007-iii)
- [Jucha and Żak v. Poland — judgment](https://www.bailii.org/eu/cases/ECHR/2012/1830.html)
- [Falter Zeitschriften GmbH v. Austria — judgment](https://www.bailii.org/eu/cases/ECHR/2007/173.html)
- [Karhuvaara and Iltalehti v. Finland — legal summary](https://hudoc.echr.coe.int/eng?i=002-4146)
- [Taxquet v. Belgium — legal summary](https://hudoc.echr.coe.int/eng?i=002-1728)
- [Trepashkin v. Russia (No. 2) — judgment](https://hudoc.echr.coe.int/eng?i=001-102282)
- [Daoukopoulos v. Greece — judgment](https://www.bailii.org/eu/cases/ECHR/2018/607.html)
- [Kerimova/Khamzayev v. Russia — case note](https://hudoc.echr.coe.int/eng?i=002-197)
- [Abakarova v. Russia — case summary](https://ehrac.org.uk/en_gb/key-ehrac-cases/abakarova-v-russia/)

