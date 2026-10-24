# S0 vs S1 — review sheet

S0 = simple search (lowercase only).  S1 = English search (stemming + stopwords).
Same query and same filter for both. Mark each result: **yes** / **kinda** / **no**.
Then pick **one topic where S1 is better** and **one where S0 is better**.

## Overlap (top 10)

| Need | Topic | S0 hits | S1 hits | Shared in top 10 | Only S0 | Only S1 | Jaccard |
|---|---|---:|---:|---:|---:|---:|---:|
| IN1 | Confessions coerced by police ill-treatment | 10391 | 5989 | 7 | 3 | 3 | 0.54 |
| IN2 | Journalists sanctioned for articles about public figures | 8526 | 8695 | 4 | 6 | 6 | 0.25 |
| IN3 | Unfair trial due to restricted access to evidence or witnesses | 10958 | 8578 | 5 | 5 | 5 | 0.33 |
| IN4 | Bans on religious symbols and clothing | 10993 | 1826 | 8 | 2 | 2 | 0.67 |
| IN5 | Overcrowded and unsanitary detention in Southern European states | 477 | 537 | 6 | 4 | 4 | 0.43 |
| IN6 | Expulsion or extradition to a risk of torture | 11000 | 6902 | 8 | 2 | 2 | 0.67 |
| IN7 | Civilian casualties from bombardment and shelling | 2238 | 3359 | 8 | 2 | 2 | 0.67 |

---

## IN1 — Confessions coerced by police ill-treatment

- type: `T2`
- query: `confession coerced by police beating ill-treatment`
- filter: none
- look for: Cases where the applicant alleges they were beaten or coerced by police into confessing to a crime.
- relevant if: Relevant: physical violence, threats or psychological pressure by police or investigators during arrest or questioning with the aim of obtaining a confession or self-incriminating statement, including cases where such a confession was later used at trial. Not relevant: ill-treatment during arrest, in prison or at demonstrations with no link to a confession or statement; confessions retracted for reasons other than coercion.
- overlap: 7/10 shared (`001-101321`, `001-145580`, `001-153349`, `001-182845`, `001-191483`, `001-78369`, `001-81352`)

### S0 — simple (lowercase only)  (10391 matching cases)

1. **001-153349**  score 10.38  
   CASE OF NALBANDYAN v. ARMENIA (2015)  |  ARMENIA  |  art. 3,6  
   match? yes / kinda / no
   snippet: She further alleges that she saw both her father and her mother at the [police] department and that they bore signs of [ill]-[treatment].  (also S1 #1)

2. **001-78369**  score 9.74  
   CASE OF SHEYDAYEV v. RUSSIA (2006)  |  RUSSIA  |  art. 13,3,5,6  
   match? yes / kinda / no
   snippet: In the proceedings before the Garrison Military Court the applicant complained in detail about the [ill]-[treatment] during the [police] custody and submitted that his [confession] had been made under duress.  (also S1 #3)

3. **001-81352**  score 9.14  
   CASE OF HARUTYUNYAN v. ARMENIA (2007)  |  ARMENIA  |  art. 6  
   match? yes / kinda / no
   snippet: [The [police] officers] also threatened the victims with retaliation if they informed any higher authority about the [ill]-[treatment] ... On 5 January 2000, in his office in the military [police] department in Yerevan, [[police] officer M.] forced [serviceman A.] to state in relation to the [ill]-[treatment] that he was not familiar with [[police] officer M.], that nobody had beaten him and that the injuries on his fingers had been sustained as a result of his hand being squashed [by] a car door ...   (also S1 #2)

4. **001-186723**  score 8.80  
   CASE OF GOLUBYATNIKOV AND ZHUCHKOV v. RUSSIA (2018)  |  RUSSIA  |  art. 3,5,6  
   match? yes / kinda / no
   snippet: On the same day the Town Court heard the applicants and their co-accused. All four defendants complained that they had been subjected to [ill]-[treatment] [by] [police] officers. The first applicant argued, inter alia, that the second applicant’s [confession] incriminating him of having murdered S. had been obtained as a result of the second applicant’s [ill]-[treatment] [by] the [police] officers and therefore constituted inadmissible evidence.   (**only in S0**)

5. **001-145580**  score 8.75  
   CASE OF OSAKOVSKIY v. UKRAINE (2014)  |  UKRAINE  |  art. 3,5,6  
   match? yes / kinda / no  (also S1 #9)

6. **001-180827**  score 8.69  
   CASE OF ULAY v. TURKEY (2018)  |  TURKEY  |  art. 6  
   match? yes / kinda / no
   snippet: In a petition dated 11 September 2003, the applicant argued that he had been [coerced] into making self-incriminating statements, in that he had been subjected to [ill]-[treatment] and psychological duress [by] the [police], who had threatened him with bringing charges against his family members if he did not confess to having murdered H.A.   (**only in S0**)

7. **001-182845**  score 8.64  
   CASE OF SERGEY IVANOV v. RUSSIA (2018)  |  RUSSIA  |  art. 3,6  
   match? yes / kinda / no  (also S1 #5)

8. **001-101321**  score 8.56  
   CASE OF LEONID LAZARENKO v. UKRAINE (2010)  |  UKRAINE  |  art. 6  
   match? yes / kinda / no
   snippet: s car. The court examined the applicant's allegation of [ill]-[treatment] and found it to be no more than defence tactics. The [police] officer responsible for the applicant's arrest was questioned at the hearing and denied having [coerced] him in any way.   (also S1 #7)

9. **001-191483**  score 8.52  
   CASE OF GABBAZOV v. RUSSIA (2019)  |  RUSSIA  |  art. 3  
   match? yes / kinda / no
   snippet: At trial, the applicant pleaded not guilty. He stated that on 16 June 2007 he had been arrested, driven to a [police] station and physically assaulted [by] [police] officers. The trial court dismissed the applicant’s allegations of [ill]-[treatment] [by] the [police]. It relied mainly on the investigator’s refusal to open a criminal case against the [police] officers of 14 September 2007 (subsequently overruled), noting there was no objective information showing that physical violence had been used against the applicant.  (also S1 #4)

10. **001-115307**  score 8.51  
   CASE OF DVALISHVILI v. GEORGIA (2012)  |  GEORGIA  |  art. 3  
   match? yes / kinda / no
   snippet: According to the record of the hearing, the defence lawyer had requested the Tskaltubo District Court to declare the applicant’s pre-trial testimony inadmissible, arguing that his [confession] had been extracted [by] [ill]-[treatment]; however, the request was dismissed. The court concluded that there was no evidence to substantiate the applicant’s allegations of [ill]-[treatment].  (**only in S0**)


### S1 — English (stemming + stopwords)  (5989 matching cases)

1. **001-153349**  score 10.64  
   CASE OF NALBANDYAN v. ARMENIA (2015)  |  ARMENIA  |  art. 3,6  
   match? yes / kinda / no
   snippet: The first applicant alleges that on the same date he was taken to the Vardenis [Police] Department where he was unlawfully kept without his arrest being formally recorded. At the [police] department he was subjected to continual [beatings] by [police] officers in an attempt to [coerce] him to [confess] to the above-mentioned murder.  (also S0 #1)

2. **001-81352**  score 10.09  
   CASE OF HARUTYUNYAN v. ARMENIA (2007)  |  ARMENIA  |  art. 6  
   match? yes / kinda / no
   snippet: On 5 January 2000 [police] officer M. threatened to kill him if he informed the investigator about the [ill]-[treatment].  (also S0 #3)

3. **001-78369**  score 9.89  
   CASE OF SHEYDAYEV v. RUSSIA (2006)  |  RUSSIA  |  art. 13,3,5,6  
   match? yes / kinda / no
   snippet: In the proceedings before the Garrison Military Court the applicant complained in detail about the [ill]-[treatment] during the [police] custody and submitted that his [confession] had been made under duress.  (also S0 #2)

4. **001-191483**  score 9.57  
   CASE OF GABBAZOV v. RUSSIA (2019)  |  RUSSIA  |  art. 3  
   match? yes / kinda / no
   snippet: The applicant continued to be physically assaulted in the presence of investigator A.I. from the South-West Administrative Circuit [police], who threatened him with imprisonment. The applicant refused to sign any [confession] statements. The [police] officers [coerced] K. to [confess] to the robbery, physically assaulting him and making him see the applicant’s [beatings].   (also S0 #9)

5. **001-182845**  score 9.53  
   CASE OF SERGEY IVANOV v. RUSSIA (2018)  |  RUSSIA  |  art. 3,6  
   match? yes / kinda / no  (also S0 #7)

6. **001-159759**  score 9.12  
   CASE OF MINIKAYEV v. RUSSIA (2016)  |  RUSSIA  |  art. 13,3  
   match? yes / kinda / no
   snippet: As a result, he [confessed] to the robbery of 30 December 2004. However, the [police] officers forged the date on the [confession], indicating that he [confessed] on 20 April 2005.  (**only in S1**)

7. **001-101321**  score 8.98  
   CASE OF LEONID LAZARENKO v. UKRAINE (2010)  |  UKRAINE  |  art. 6  
   match? yes / kinda / no
   snippet: s car. The court examined the applicant's allegation of [ill]-[treatment] and found it to be no more than defence tactics. The [police] officer responsible for the applicant's arrest was questioned at the hearing and denied having [coerced] him in any way.   (also S0 #8)

8. **001-147038**  score 8.94  
   CASE OF MOSTIPAN v. RUSSIA (2014)  |  RUSSIA  |  art. 3,6  
   match? yes / kinda / no
   snippet: During the new trial, the applicant admitted that she had participated in S.’s abduction and battery but denied any involvement in organising S.’s rape and murder. She further claimed that she had been subjected to [ill]-[treatment] while in [police] custody and forced to [confess].  (**only in S1**)

9. **001-145580**  score 8.94  
   CASE OF OSAKOVSKIY v. UKRAINE (2014)  |  UKRAINE  |  art. 3,5,6  
   match? yes / kinda / no  (also S0 #5)

10. **001-191928**  score 8.75  
   CASE OF KONYAYEV v. RUSSIA (2019)  |  RUSSIA  |  art. 3  
   match? yes / kinda / no  (**only in S1**)


---

## IN2 — Journalists sanctioned for articles about public figures

- type: `T4`
- query: `journalist convicted defamation article about politician public official`
- filter: none
- look for: Cases where a journalist or publisher was convicted or ordered to pay damages for an article about a public official or politician.
- relevant if: Relevant: criminal conviction, fine or civil damages imposed on a journalist, editor or publisher because of a published article, broadcast or book concerning a politician, civil servant, judge or other public official. Not relevant: journalists as victims of violence or surveillance; defamation proceedings between private individuals; sanctions for content not concerning a public figure.
- overlap: 4/10 shared (`001-112432`, `001-113919`, `001-151007`, `001-61441`)

### S0 — simple (lowercase only)  (8526 matching cases)

1. **001-151007**  score 13.46  
   CASE OF COJOCARU v. ROMANIA (2015)  |  ROMANIA  |  art. 10  
   match? yes / kinda / no
   snippet: The [article] also contained a statement by another [politician] and the mayor’s point of view on the investigation.  (also S1 #1)

2. **001-61441**  score 10.80  
   CASE OF SCHARSACH AND NEWS VERLAGSGESELLSCHAFT v. AUSTRIA (2003)  |  AUSTRIA  |  art. 10  
   match? yes / kinda / no  (also S1 #6)

3. **001-113919**  score 10.45  
   CASE OF JUCHA AND ŻAK v. POLAND (2012)  |  POLAND  |  art. 10  
   match? yes / kinda / no  (also S1 #4)

4. **001-77831**  score 10.14  
   CASE OF STANDARD VERLAGS GMBH AND KRAWAGNA-PFEIFER v. AUSTRIA (2006)  |  AUSTRIA  |  art. 10,6  
   match? yes / kinda / no
   snippet: The dissemination of true statements of fact could only violate the interests of the person concerned if there was no prevailing [public] interest in receiving the information. However, information [about] the personal credibility of a [politician], demonstrated by his conviction for [defamation], was in the [public] interest, in particular in pre-election times when the general [public] gathered information [about] the different parties and their representatives.  (**only in S0**)

5. **001-105557**  score 9.78  
   CASE OF WIZERKANIUK v. POLAND (2011)  |  POLAND  |  art. 10  
   match? yes / kinda / no
   snippet: In a democratic state a [politician], a [public] person, has no right to manipulate his or her statements post factum. If he or she resorts to such manipulation, the [public] opinion is entitled to know this because it is an important element relevant for [public] image of a [politician] if he or she tampers with his or her [public] statements.   (**only in S0**)

6. **001-126629**  score 9.69  
   CASE OF PRINT ZEITUNGSVERLAG GMBH v. AUSTRIA (2013)  |  AUSTRIA  |  art. 10  
   match? yes / kinda / no
   snippet: It accepted that the local [public] had an interest in knowing [about] a campaign against the chairman of the tourism association and a local [politician]. However, [public] interest did not justify reproduction of the anonymous letter in the [article].   (**only in S0**)

7. **001-91475**  score 9.69  
   CASE OF DŁUGOŁĘCKI v. POLAND (2009)  |  POLAND  |  art. 10  
   match? yes / kinda / no
   snippet: On 4 April 2000 the Gdańsk District Court found the applicant guilty of [defamation] under [Article] 212 of the Criminal Code as well as of proffering insult under [Article] 216 of the Criminal Code. The applicant was sentenced to a fine of 1,000 Polish zlotys (PLN) and was ordered to pay PLN 200 to a charity.   (**only in S0**)

8. **001-112432**  score 9.45  
   CASE OF ZIEMBIŃSKI v. POLAND (2012)  |  POLAND  |  art. 10  
   match? yes / kinda / no
   snippet: Such actions do not benefit from the protection granted to freedom of expression and the right to criticise under [Article] 31 § 3 of the Constitution or [Article] 10 § 2 of the Convention. The real effect of the applicant’s publication cannot be assessed in isolation from the [public] office held by M.D.   (also S1 #8)

9. **001-184654**  score 9.38  
   CASE OF MAKRADULI v. "THE FORMER YUGOSLAV REPUBLIC OF MACEDONIA" (2018)  |  FORMER YUGOSLAV MACEDONIA  |  art. 10  
   match? yes / kinda / no
   snippet: He reiterated his arguments that he had been punished for a question that he had raised at a press conference that had been held on behalf of his political party. The question had been addressed to the [public] and had been based on information submitted to his political party [about] suspected irregularities in the work of a State [official]. The aim had been to stimulate [public] debate on whether the [official] had been diligent in performing his [official] duty.  (**only in S0**)

10. **001-111626**  score 9.18  
   CASE OF CIESIELCZYK v. POLAND (2012)  |  POLAND  |  art. 10  
   match? yes / kinda / no
   snippet: Secondly, the applicant was found guilty of disseminating, on the above-mentioned Internet site, inaccurate information [about] one of the journalists working for S.Tar TV, Mr G. J., which had debased the victim in the eyes of the [public] and had undermined [public] confidence in him: [public] confidence was necessary for his profession.   (**only in S0**)


### S1 — English (stemming + stopwords)  (8695 matching cases)

1. **001-151007**  score 12.93  
   CASE OF COJOCARU v. ROMANIA (2015)  |  ROMANIA  |  art. 10  
   match? yes / kinda / no
   snippet: The [article] also contained a statement by another [politician] and the mayor’s point of view on the investigation.  (also S0 #1)

2. **001-79591**  score 11.34  
   CASE OF FALTER ZEITSCHRIFTEN GMBH v. AUSTRIA (2007)  |  AUSTRIA  |  art. 10  
   match? yes / kinda / no
   snippet: The “informer affair” involves much more than just a few corrupt police officers and a web of [officials], [journalists] and [politicians] who for years went unpunished in downloading secret material [about] political opponents from the police computer system and distributing it among themselves with a view to making [public] attacks – especially in the Kronen Zeitung – on people they did not like.   (**only in S1**)

3. **001-95810**  score 10.70  
   CASE OF FLUX v. MOLDOVA (No. 7) (2009)  |  MOLDOVA  |  art. 10  
   match? yes / kinda / no  (**only in S1**)

4. **001-113919**  score 10.65  
   CASE OF JUCHA AND ŻAK v. POLAND (2012)  |  POLAND  |  art. 10  
   match? yes / kinda / no
   snippet: II K 807/03 [convicting] the applicant of [defamation] in respect of the Tarnów cable television and its [journalists].  (also S0 #3)

5. **001-67457**  score 10.49  
   CASE OF KARHUVAARA AND ILTALEHTI v. FINLAND (2004)  |  FINLAND  |  art. 10  
   match? yes / kinda / no
   snippet: The fact that the [conviction] of the spouse of a [politician] could affect people’s voting intentions did not in itself render the matter of [public] interest such as to justify the [publication].   (**only in S1**)

6. **001-61441**  score 10.48  
   CASE OF SCHARSACH AND NEWS VERLAGSGESELLSCHAFT v. AUSTRIA (2003)  |  AUSTRIA  |  art. 10  
   match? yes / kinda / no  (also S0 #2)

7. **001-77786**  score 10.45  
   CASE OF KOBENTER AND STANDARD VERLAGS GMBH v. AUSTRIA (2006)  |  AUSTRIA  |  art. 10  
   match? yes / kinda / no
   snippet: Arguing that [journalistic] liberty also allowed a certain degree of exaggeration and even provocation, and considering the [public] discussion caused by the reasoning of the judgment not only in various media but also among judges, the polemical style of the [article] was not disproportionate either.  (**only in S1**)

8. **001-112432**  score 10.43  
   CASE OF ZIEMBIŃSKI v. POLAND (2012)  |  POLAND  |  art. 10  
   match? yes / kinda / no
   snippet: On 8 February 2006 the Piotrków Trybunalski District Court gave judgment. It acquitted the applicant of the first charge and [convicted] him of [defamation] committed through the mass media in respect of the second charge. The District Court held that the applicant had wrongly alleged in his [articles] that the district mayor had known that D.K. accepted bribes but had not informed the police [about] it, despite having been under a duty to do so.   (also S0 #8)

9. **001-109189**  score 10.31  
   CASE OF TUŞALP v. TURKEY (2012)  |  TURKEY  |  art. 10  
   match? yes / kinda / no
   snippet: It held that a [politician] naturally had to bear and tolerate reasonable criticism. However, the court considered that, in the instant case, the remarks made in the [article] went beyond the limits of acceptable criticism and belittled the Prime Minister in the [public] and the political arena.   (**only in S1**)

10. **001-80865**  score 10.07  
   CASE OF GORELISHVILI v. GEORGIA (2007)  |  GEORGIA  |  art. 10  
   match? yes / kinda / no  (**only in S1**)


---

## IN3 — Unfair trial due to restricted access to evidence or witnesses

- type: `T3`
- query: `fair trial no access to classified evidence unable to cross-examine witnesses`
- filter: none
- look for: Cases where the right to a fair trial was compromised because the applicant could not access classified documents, cross-examine key witnesses, or review the opposing party's evidence.
- relevant if: Relevant: the applicant (in criminal, civil or administrative proceedings) was refused access to secret or classified material used against them; was convicted on statements of absent or anonymous witnesses they could not question; or could not see or comment on evidence or submissions of the other party. Not relevant: fair-trial complaints about length of proceedings, judicial impartiality, legal aid, or non-enforcement of judgments.
- overlap: 5/10 shared (`001-108072`, `001-138919`, `001-154022`, `001-167538`, `001-81682`)

### S0 — simple (lowercase only)  (10958 matching cases)

1. **001-167538**  score 8.67  
   CASE OF CONSTANTINIDES v. GREECE (2016)  |  GREECE  |  art. 6  
   match? yes / kinda / no
   snippet: Nevertheless, the applicant had been deprived of his right [to] [cross]-[examine] her.  (also S1 #6)

2. **001-105764**  score 8.28  
   CASE OF LIU v. RUSSIA (No. 2) (2011)  |  RUSSIA  |  art. 46,8  
   match? yes / kinda / no
   snippet: Accordingly, their right [to] a [fair] [trial] had not been violated.  (**only in S0**)

3. **001-108072**  score 8.25  
   CASE OF AL-KHAWAJA AND TAHERY v. THE UNITED KINGDOM (2011)  |  UNITED KINGDOM  |  art. 6  
   match? yes / kinda / no
   snippet: The defence was given the opportunity [to] [cross]-[examine] all the [witnesses] who gave live [evidence]. The first applicant gave [evidence] in his own defence. He also called a number of [witnesses], who gave [evidence] as [to] his good character.  (also S1 #3)

4. **001-102282**  score 8.24  
   CASE OF TREPASHKIN v. RUSSIA (NO. 2) (2010)  |  RUSSIA  |  art. 3,34,5,6  
   match? yes / kinda / no  (**only in S0**)

5. **001-154022**  score 8.22  
   CASE OF YAREMENKO v. UKRAINE (No. 2) (2015)  |  UKRAINE  |  art. 6  
   match? yes / kinda / no  (also S1 #10)

6. **001-81682**  score 7.97  
   CASE OF GECAS v. LITHUANIA (2007)  |  LITHUANIA  |  art. 6  
   match? yes / kinda / no  (also S1 #9)

7. **001-96033**  score 7.97  
   CASE OF CAKA v. ALBANIA (2009)  |  ALBANIA  |  art. 6  
   match? yes / kinda / no
   snippet: In so far as the appeal was directed against the District Court's refusal [to] allow the applicant [to] [cross]-[examine] witness M., the Court of Appeal noted that at the hearing of 23 February 2000 the applicant's counsel had stated that he had [no] questions [to] ask.   (**only in S0**)

8. **001-178174**  score 7.89  
   CASE OF KAMENOS v. CYPRUS (2017)  |  CYPRUS  |  art. 6  
   match? yes / kinda / no
   snippet: He argued that that was contrary [to] the rules of natural justice and the right [to] a [fair] [trial]. He stressed, however, that this had nothing [to] do with the judges as individuals.  (**only in S0**)

9. **001-110445**  score 7.88  
   CASE OF DAMIR SIBGATULLIN v. RUSSIA (2012)  |  RUSSIA  |  art. 38,6  
   match? yes / kinda / no
   snippet: The parties’ closing arguments followed. The defence argued that there was [no] material [evidence], such as fingerprints, bloodstains and so on, linking the applicant [to] the criminal offences, and that the applicant had been denied an important right [to] [cross]-[examine] [witnesses] against him.  (**only in S0**)

10. **001-138919**  score 7.84  
   CASE OF DONOHOE v. IRELAND (2013)  |  IRELAND  |  art. 6  
   match? yes / kinda / no
   snippet: The exercise of the [trial] court’s discretion [to] review the files furnished by the Chief Superintendent PK did not infringe the right [to] a [fair] [trial]. It found [no] [evidence] that would have assisted the accused and the material examined constituted a good basis for the belief of the Chief Superintendent.   (also S1 #8)


### S1 — English (stemming + stopwords)  (8578 matching cases)

1. **001-102637**  score 7.72  
   CASE OF MCKEOWN v. THE UNITED KINGDOM (2011)  |  UNITED KINGDOM  |  art. 6  
   match? yes / kinda / no  (**only in S1**)

2. **001-105823**  score 7.56  
   CASE OF HUSEYN AND OTHERS v. AZERBAIJAN (2011)  |  AZERBAIJAN  |  art. 6  
   match? yes / kinda / no  (**only in S1**)

3. **001-108072**  score 7.47  
   CASE OF AL-KHAWAJA AND TAHERY v. THE UNITED KINGDOM (2011)  |  UNITED KINGDOM  |  art. 6  
   match? yes / kinda / no
   snippet: The defence was given the opportunity to [cross]-[examine] all the [witnesses] who gave live [evidence]. The first applicant gave [evidence] in his own defence. He also called a number of [witnesses], who gave [evidence] as to his good character.  (also S0 #3)

4. **001-90677**  score 7.37  
   CASE OF TAXQUET v. BELGIUM (2009)  |  BELGIUM  |  art. 46,6  
   match? yes / kinda / no
   snippet: It does not appear from the Assize Court's reply to the appellants' submissions that the [trial] courts contested their right to rebut the [evidence] produced at the [trial]. On that account, these grounds of appeal cannot be allowed. As to the remaining grounds, a breach of Article 6 § 3 (d) of the Convention ... does not result from the mere fact that the [trial] court considered it unnecessary, or impossible, to order the [cross]-[examination] of the anonymous informer whose disclosures provided helpful guidance for the investigation.   (**only in S1**)

5. **001-175667**  score 7.28  
   CASE OF M v. THE NETHERLANDS (2017)  |  NETHERLANDS  |  art. 5,6,8  
   match? yes / kinda / no  (**only in S1**)

6. **001-167538**  score 7.11  
   CASE OF CONSTANTINIDES v. GREECE (2016)  |  GREECE  |  art. 6  
   match? yes / kinda / no
   snippet: Nevertheless, the applicant had been deprived of his right to [cross]-[examine] her.  (also S0 #1)

7. **001-148673**  score 7.10  
   CASE OF HORNCASTLE AND OTHERS v. THE UNITED KINGDOM (2014)  |  UNITED KINGDOM  |  art. 6  
   match? yes / kinda / no
   snippet: He identified the principal issue raised by the appeals as being whether a conviction based “solely or to a decisive extent” on the statement of a [witness] whom the defendant had had no chance of [cross]-[examining] necessarily infringed his right to a [fair] [trial] under Article 6 §§ 1 and 3 (d).  (**only in S1**)

8. **001-138919**  score 7.05  
   CASE OF DONOHOE v. IRELAND (2013)  |  IRELAND  |  art. 6  
   match? yes / kinda / no
   snippet: The SCC totally rejected a suggestion put to the Chief Superintendent PK, in [cross]-[examination] that his [evidence] was a fiction.  (also S0 #10)

9. **001-81682**  score 7.01  
   CASE OF GECAS v. LITHUANIA (2007)  |  LITHUANIA  |  art. 6  
   match? yes / kinda / no
   snippet: On 30 September 2002 the Klaipėda Regional Court decided to adjourn the proceedings until the issue of the use of and [access] to the [classified] [evidence] was resolved.  (also S0 #6)

10. **001-154022**  score 6.99  
   CASE OF YAREMENKO v. UKRAINE (No. 2) (2015)  |  UKRAINE  |  art. 6  
   match? yes / kinda / no
   snippet: On 24 June 2001 investigating prosecutor G. informed the applicant that his request for [cross]-[examination] had been rejected, since no discrepancies had been found between his and S.’s statements.  (also S0 #5)


---

## IN4 — Bans on religious symbols and clothing

- type: `T4`
- query: `ban on wearing religious symbols headscarf veil school workplace`
- filter: none
- look for: Cases involving restrictions or bans on manifesting religion, such as wearing religious symbols or clothing in public institutions, schools or the workplace.
- relevant if: Relevant: prohibitions or sanctions for wearing headscarves, veils, skullcaps, crosses or other religious clothing or symbols, or the display of religious symbols (e.g. crucifixes) in state institutions, schools, courts or employment. Not relevant: religious organisations' registration, conscientious objection, religious education marks, or cases where the applicant's religion is mentioned without a restriction on manifesting it.
- overlap: 8/10 shared (`001-104040`, `001-121567`, `001-144129`, `001-159070`, `001-175660`, `001-180506`, `001-70956`, `001-90039`)

### S0 — simple (lowercase only)  (10993 matching cases)

1. **001-175660**  score 14.31  
   CASE OF DAKIR v. BELGIUM (2017)  |  BELGIUM  |  art. 14,2,6,8,9  
   match? yes / kinda / no  (also S1 #3)

2. **001-90039**  score 13.77  
   CASE OF DOGRU v. FRANCE (2008)  |  FRANCE  |  art. 9  
   match? yes / kinda / no  (also S1 #2)

3. **001-159070**  score 12.86  
   CASE OF EBRAHIMIAN v. FRANCE (2015)  |  FRANCE  |  art. 9  
   match? yes / kinda / no
   snippet: The court considered that [on] the basis of the above-mentioned principles concerning the expression of [religious] opinions within the public services, the administrative authorities had not committed an error of assessment in refusing to renew the contract [on] the implied ground of her [wearing] of “attire manifesting, in an ostensible manner, allegiance to a religion”.   (also S1 #1)

4. **001-180506**  score 10.86  
   CASE OF SEKMADIENIS LTD. v. LITHUANIA (2018)  |  LITHUANIA  |  art. 10  
   match? yes / kinda / no
   snippet: [On] 5 March 2013 the latter submitted the following opinion: “[Religious] [symbols] are not just simple signs, pictures or logos. In the Christian tradition, a [religious] symbol is a visible sign representing the invisible sacred reality.   (also S1 #7)

5. **001-70956**  score 10.54  
   CASE OF LEYLA ŞAHİN v. TURKEY (2005)  |  TURKEY  |  art. 10,14,8,9,P1-2  
   match? yes / kinda / no  (also S1 #4)

6. **001-144129**  score 9.25  
   CASE OF MUSTAFA ERDOĞAN AND OTHERS v. TURKEY (2014)  |  TURKEY  |  art. 10  
   match? yes / kinda / no
   snippet: Most of them concern expressions of concern [about] the social consequences of the lack of freedom created by the prohibition [on] [wearing] the [headscarf]. In other words, these statements have the nature of being demands for freedom voiced by Members of Parliament – mostly from the podium of Parliament.   (also S1 #8)

7. **001-104040**  score 8.97  
   CASE OF LAUTSI AND OTHERS v. ITALY (2011)  |  ITALY  |  art. P1-2  
   match? yes / kinda / no
   snippet: [On] 27 May 2002, by ten votes to two with one abstention, the school's governors decided to keep [religious] [symbols] in classrooms.  (also S1 #5)

8. **001-187904**  score 8.66  
   CASE OF URAT v. TURKEY (2018)  |  TURKEY  |  art. 6  
   match? yes / kinda / no
   snippet: One teacher colleague stated that he believed the applicant was a Hizbullah supporter as he had seen his wife [wearing] a çarşaf (chador). In respect of the second applicant, the teachers said that they knew him to be [religious] but that they had not witnessed him engaging in any ideological propaganda at [school].   (**only in S0**)

9. **001-99384**  score 8.64  
   CASE OF GRZELAK v. POLAND (2010)  |  POLAND  |  art. 14,9  
   match? yes / kinda / no  (**only in S0**)

10. **001-121567**  score 7.80  
   CASE OF M.Y.H. AND OTHERS v. SWEDEN (2013)  |  SWEDEN  |  art. 3  
   match? yes / kinda / no
   snippet: The second and third applicants claimed that they had been forced to wear the [veil]. Moreover, while the two parents had higher education in economics and administration, their daughter had not been able to study since the family feared that she would be kidnapped as Christian women were often exposed to kidnapping, rape and murder [on] their way to university.  (also S1 #9)


### S1 — English (stemming + stopwords)  (1826 matching cases)

1. **001-159070**  score 14.38  
   CASE OF EBRAHIMIAN v. FRANCE (2015)  |  FRANCE  |  art. 9  
   match? yes / kinda / no
   snippet: It concluded “thus, even though [the applicant’s] employer tolerated the [wearing] of this [veil] for several months and [her] conduct cannot be considered as deliberately provocative or proselytising, the hospital has not acted illegally in deciding not to renew the contract following her refusal to stop [wearing] the [veil]”.  (also S0 #3)

2. **001-90039**  score 13.80  
   CASE OF DOGRU v. FRANCE (2008)  |  FRANCE  |  art. 9  
   match? yes / kinda / no
   snippet: It also found that the applicant's attitude had created an atmosphere of tension within the [school] and that on the basis of all the factors involved her expulsion from the [school] had been justified, regardless of the proposal she had made at the end of January to [wear] a hat instead of her [headscarf].  (also S0 #2)

3. **001-175660**  score 13.46  
   CASE OF DAKIR v. BELGIUM (2017)  |  BELGIUM  |  art. 14,2,6,8,9  
   match? yes / kinda / no
   snippet: The applicant stated that she was a Muslim and had decided, on her own initiative, to [wear] the niqab – a [veil] covering the face except for the eyes – in accordance with her [religious] beliefs. She said that she had taken the decision to [wear] the full-face [veil] when she was sixteen years old.   (also S0 #1)

4. **001-70956**  score 10.68  
   CASE OF LEYLA ŞAHİN v. TURKEY (2005)  |  TURKEY  |  art. 10,14,8,9,P1-2  
   match? yes / kinda / no
   snippet: She comes from a traditional family of practising Muslims and considers it her [religious] duty to [wear] the Islamic [headscarf].  (also S0 #5)

5. **001-104040**  score 10.28  
   CASE OF LAUTSI AND OTHERS v. ITALY (2011)  |  ITALY  |  art. P1-2  
   match? yes / kinda / no
   snippet: On 27 May 2002, by ten votes to two with one abstention, the [school's] governors decided to keep [religious] [symbols] in classrooms.  (also S0 #7)

6. **001-145466**  score 10.07  
   CASE OF S.A.S. v. FRANCE (2014)  |  FRANCE  |  art. 11,14,34,8,9  
   match? yes / kinda / no  (**only in S1**)

7. **001-180506**  score 9.95  
   CASE OF SEKMADIENIS LTD. v. LITHUANIA (2018)  |  LITHUANIA  |  art. 10  
   match? yes / kinda / no
   snippet: It stated: “The Inspectorate, having examined the material presented to it, is of the view that the advertisements use [religious] [symbols] in a disrespectful and inappropriate manner. [Religious] people always react very sensitively to any use of [religious] [symbols] or [religious] personalities in advertising.   (also S0 #4)

8. **001-144129**  score 9.66  
   CASE OF MUSTAFA ERDOĞAN AND OTHERS v. TURKEY (2014)  |  TURKEY  |  art. 10  
   match? yes / kinda / no
   snippet: In other words, according to the Constitutional Court, the election of a citizen who [wears] a [headscarf] as an MP and her attempt to take the oath in Parliament while [wearing] the [headscarf] are contrary to secularism. This is an unsound understanding for many reasons.   (also S0 #6)

9. **001-121567**  score 9.25  
   CASE OF M.Y.H. AND OTHERS v. SWEDEN (2013)  |  SWEDEN  |  art. 3  
   match? yes / kinda / no
   snippet: The family also claimed that it had not been possible to practise their religion where they had lived because of fear of terrorists destroying the church. The second and third applicants claimed that they had been forced to [wear] the [veil]. Moreover, while the two parents had higher education in economics and administration, their daughter had not been able to study since the family feared that she would be kidnapped as Christian women were often exposed to kidnapping, rape and murder on their way to university.  (also S0 #10)

10. **001-60936**  score 9.11  
   CASE OF REFAH PARTISI (THE WELFARE PARTY) AND OTHERS v. TURKEY (2003)  |  TURKEY  |  art. 11  
   match? yes / kinda / no
   snippet: In our time there was never any question of hostility to the [wearing] of headscarves ...” In his speech of 14 December 1995 before the general election he had said: “... [university] chancellors are going to retreat before the [headscarf] when Refah comes to power.”   (**only in S1**)


---

## IN5 — Overcrowded and unsanitary detention in Southern European states

- type: `T5`
- query: `overcrowded prison cells poor sanitary conditions`
- filter: `defendants:(ALBANIA OR ANDORRA OR "BOSNIA & HERZEGOVINA" OR CROATIA OR CYPRUS OR "FORMER YUGOSLAV MACEDONIA" OR "NORTH MACEDONIA" OR GREECE OR ITALY OR MALTA OR MONTENEGRO OR PORTUGAL OR "SAN MARINO" OR SERBIA OR SLOVENIA OR SPAIN)`
- look for: Cases against Southern European states concerning overcrowding and inadequate sanitary conditions in detention centres.
- relevant if: Relevant: facts describe cell size or number of inmates, insufficient personal space, lack of toilets, hygiene, ventilation or hot water in a prison, remand centre or police or immigration detention facility of a Southern European state. Not relevant: complaints only about the length or lawfulness of detention, or ill-treatment by guards without a description of material conditions.
- overlap: 6/10 shared (`001-113387`, `001-148283`, `001-156245`, `001-167483`, `001-170837`, `001-72704`)

### S0 — simple (lowercase only)  (477 matching cases)

1. **001-72704**  score 11.57  
   CASE OF CENBAUER v. CROATIA (2006)  |  CROATIA  |  art. 3  
   match? yes / kinda / no
   snippet: Toiletries and other personal hygiene products were provided only every four to five months. The food served to the inmates was of insufficient quantity and [poor] quality; the inmates were served only carbohydrates, without any vegetables and hardly any meat. In general, the [prison] was [overcrowded]. The [prison] buildings, built about two hundred years ago, were in a very [poor] state of repair.   (also S1 #1)

2. **001-113387**  score 10.60  
   CASE OF DIMITRIOS DIMOPOULOS v. GREECE (2012)  |  GREECE  |  art. 3,5  
   match? yes / kinda / no  (also S1 #2)

3. **001-167483**  score 10.44  
   CASE OF MURŠIĆ v. CROATIA (2016)  |  CROATIA  |  art. 3  
   match? yes / kinda / no  (also S1 #5)

4. **001-148283**  score 9.71  
   CASE OF POZAIĆ v. CROATIA (2014)  |  CROATIA  |  art. 3  
   match? yes / kinda / no
   snippet: On 11 October 2010 the sentence-execution judge of the Bjelovar County Court dismissed the applicant’s complaints as ill-founded. She explained that the information received from Bjelovar [Prison] did not suggest that the applicant had been placed in [overcrowded] [cells], and that, as regards the general [conditions] of Bjelovar [Prison], she had herself visited the [prison] facilities and had found that in general they had not been inappropriate.   (also S1 #8)

5. **001-170837**  score 9.59  
   CASE OF IGBO AND OTHERS v. GREECE (2017)  |  GREECE  |  art. 13,3  
   match? yes / kinda / no  (also S1 #7)

6. **001-156245**  score 9.19  
   CASE OF MARTZAKLIS AND OTHERS v. GREECE (2015)  |  GREECE  |  art. 13,14,3  
   match? yes / kinda / no  (also S1 #10)

7. **001-182869**  score 8.65  
   CASE OF ZABELOS AND OTHERS v. GREECE (2018)  |  GREECE  |  art. 13,3  
   match? yes / kinda / no  (**only in S0**)

8. **001-172855**  score 8.59  
   CASE OF CELA AND OTHERS v. GREECE (2017)  |  GREECE  |  art. 13,3  
   match? yes / kinda / no  (**only in S0**)

9. **001-182447**  score 8.40  
   CASE OF TSARPELAS v. GREECE (2018)  |  GREECE  |  art. 13,3  
   match? yes / kinda / no  (**only in S0**)

10. **001-170704**  score 8.35  
   CASE OF SINGH AND OTHERS v. GREECE (2017)  |  GREECE  |  art. 13,3  
   match? yes / kinda / no
   snippet: (on average) to 8.30 a.m. and from 11.30 a.m. to 2.45 p.m. every day. They had had to take their meals, which were of [poor] quality and nutritional value, inside their [cells].  (**only in S0**)


### S1 — English (stemming + stopwords)  (537 matching cases)

1. **001-72704**  score 11.09  
   CASE OF CENBAUER v. CROATIA (2006)  |  CROATIA  |  art. 3  
   match? yes / kinda / no
   snippet: He further informed the delegation that the [prison] held 683 inmates. He admitted that the [prison] was [overcrowded], especially B wing. Tour of LSP B wing We found [cell] 17 situated next to the communal bathroom.   (also S0 #1)

2. **001-113387**  score 10.48  
   CASE OF DIMITRIOS DIMOPOULOS v. GREECE (2012)  |  GREECE  |  art. 3,5  
   match? yes / kinda / no  (also S0 #2)

3. **001-184485**  score 10.44  
   CASE OF DAOUKOPOULOS v. GREECE (2018)  |  GREECE  |  art. 13,3  
   match? yes / kinda / no  (**only in S1**)

4. **001-60728**  score 9.87  
   CASE OF BENZAN v. CROATIA (2002)  |  CROATIA  |  art. 3,38,39  
   match? yes / kinda / no
   snippet: The applicant stated that he could not address himself to the social services in the [prison]. There were no entertainment or other activities in the [prison]. In general, the [prison] was [overcrowded]. The [prison] buildings had been built about two hundred years ago and are in a very [poor] state.   (**only in S1**)

5. **001-167483**  score 9.54  
   CASE OF MURŠIĆ v. CROATIA (2016)  |  CROATIA  |  art. 3  
   match? yes / kinda / no  (also S0 #3)

6. **001-139924**  score 9.47  
   CASE OF JEVSNIK v. SLOVENIA (2014)  |  SLOVENIA  |  art. 13,3  
   match? yes / kinda / no  (**only in S1**)

7. **001-170837**  score 9.31  
   CASE OF IGBO AND OTHERS v. GREECE (2017)  |  GREECE  |  art. 13,3  
   match? yes / kinda / no  (also S0 #5)

8. **001-148283**  score 9.07  
   CASE OF POZAIĆ v. CROATIA (2014)  |  CROATIA  |  art. 3  
   match? yes / kinda / no
   snippet: On 11 October 2010 the sentence-execution judge of the Bjelovar County Court dismissed the applicant’s complaints as ill-founded. She explained that the information received from Bjelovar [Prison] did not suggest that the applicant had been placed in [overcrowded] [cells], and that, as regards the general [conditions] of Bjelovar [Prison], she had herself visited the [prison] facilities and had found that in general they had not been inappropriate.   (also S0 #4)

9. **001-148284**  score 8.74  
   CASE OF LONIĆ v. CROATIA (2014)  |  CROATIA  |  art. 13,3,6  
   match? yes / kinda / no
   snippet: In particular, he alleged that during the transfer he had been threatened with being shot and had not been medically examined upon arrival in Pula [Prison]. He also complained that he had been placed in a [cell] with seven other persons and that the hygiene [conditions] in the [cell] had been very [poor]. He stressed that by his transfer to Pula [Prison] he had been distanced from his family.  (**only in S1**)

10. **001-156245**  score 8.74  
   CASE OF MARTZAKLIS AND OTHERS v. GREECE (2015)  |  GREECE  |  art. 13,14,3  
   match? yes / kinda / no  (also S0 #6)


---

## IN6 — Expulsion or extradition to a risk of torture

- type: `T1`
- query: `extradition deportation risk of torture ill-treatment in receiving country`
- filter: none
- look for: Cases concerning the proposed extradition or deportation of an applicant to a third country where they faced a real risk of torture or inhuman treatment.
- relevant if: Relevant: the applicant contests a planned or executed extradition, deportation or expulsion, arguing they would face torture, ill-treatment, persecution or death in the destination country. Not relevant: expulsion cases argued only on family-life grounds; detention pending deportation without a risk argument; ill-treatment suffered in the respondent state itself.
- overlap: 8/10 shared (`001-100198`, `001-101586`, `001-108162`, `001-108629`, `001-116330`, `001-86086`, `001-99796`, `001-99798`)

### S0 — simple (lowercase only)  (11000 matching cases)

1. **001-101586**  score 14.45  
   CASE OF SULTANOV v. RUSSIA (2010)  |  RUSSIA  |  art. 3,5,6  
   match? yes / kinda / no
   snippet: However, if [in] fact there would appear to be a [risk] [of] [ill]-[treatment], can diplomatic assurances received from the authorities [of] a [country] where [torture] and [ill]-[treatment] is widely practised ever offer sufficient protection against that [risk]?   (also S1 #3)

2. **001-100198**  score 14.41  
   CASE OF KARIMOV v. RUSSIA (2010)  |  RUSSIA  |  art. 13,3,5  
   match? yes / kinda / no
   snippet: However, if [in] fact there would appear to be a [risk] [of] [ill]-[treatment], can diplomatic assurances received from the authorities [of] a [country] where [torture] and [ill]-[treatment] is widely practised ever offer sufficient protection against that [risk]?   (also S1 #1)

3. **001-99796**  score 14.28  
   CASE OF YULDASHEV v. RUSSIA (2010)  |  RUSSIA  |  art. 13,3,5  
   match? yes / kinda / no
   snippet: However, if [in] fact there would appear to be a [risk] [of] [ill]-[treatment], can diplomatic assurances received from the authorities [of] a [country] where [torture] and [ill]-[treatment] is widely practised ever offer sufficient protection against that [risk]?   (also S1 #5)

4. **001-116330**  score 14.17  
   CASE OF ZOKHIDOV v. RUSSIA (2013)  |  RUSSIA  |  art. 3,34,5  
   match? yes / kinda / no
   snippet: The decision was silent on the applicant’s arguments concerning the [risk] [of] [ill]-[treatment] [in] case [of] his return to his home [country].  (also S1 #6)

5. **001-86086**  score 13.96  
   CASE OF ISMOILOV AND OTHERS v. RUSSIA (2008)  |  RUSSIA  |  art. 3,5,6  
   match? yes / kinda / no
   snippet: People accused [of] participation [in] the Andijan events are at an increased [risk] [of] [torture]: we have documented tens [of] cases [of] extraction [of] confessions by means [of] [torture] and other forms [of] inhuman and degrading [treatment].   (also S1 #4)

6. **001-99798**  score 13.89  
   CASE OF ABDULAZHON ISAKOV v. RUSSIA (2010)  |  RUSSIA  |  art. 13,3,5  
   match? yes / kinda / no
   snippet: However, if [in] fact there would appear to be a [risk] [of] [ill]-[treatment], can diplomatic assurances received from the authorities [of] a [country] where [torture] and [ill]-[treatment] is widely practised ever offer sufficient protection against that [risk]?   (also S1 #2)

7. **001-108629**  score 13.21  
   CASE OF OTHMAN (ABU QATADA) v. THE UNITED KINGDOM (2012)  |  UNITED KINGDOM  |  art. 13,3,5,6  
   match? yes / kinda / no  (also S1 #9)

8. **001-108162**  score 13.08  
   CASE OF ERGASHEV v. RUSSIA (2011)  |  RUSSIA  |  art. 3,5,6  
   match? yes / kinda / no
   snippet: However, if [in] fact there would appear to be a [risk] [of] [ill]-[treatment], can diplomatic assurances received from the authorities [of] a [country] where [torture] and [ill]-[treatment] is widely practised ever offer sufficient protection against that [risk]?   (also S1 #7)

9. **001-145788**  score 12.74  
   CASE OF TERSHIYEV v. AZERBAIJAN (2014)  |  AZERBAIJAN  |  art. 13,3  
   match? yes / kinda / no  (**only in S0**)

10. **001-147333**  score 12.49  
   CASE OF MAMAZHONOV v. RUSSIA (2014)  |  RUSSIA  |  art. 13,3,34,46  
   match? yes / kinda / no  (**only in S0**)


### S1 — English (stemming + stopwords)  (6902 matching cases)

1. **001-100198**  score 14.24  
   CASE OF KARIMOV v. RUSSIA (2010)  |  RUSSIA  |  art. 13,3,5  
   match? yes / kinda / no
   snippet: However, if in fact there would appear to be a [risk] of [ill]-[treatment], can diplomatic assurances [received] from the authorities of a [country] where [torture] and [ill]-[treatment] is widely practised ever offer sufficient protection against that [risk]?   (also S0 #2)

2. **001-99798**  score 14.19  
   CASE OF ABDULAZHON ISAKOV v. RUSSIA (2010)  |  RUSSIA  |  art. 13,3,5  
   match? yes / kinda / no
   snippet: However, if in fact there would appear to be a [risk] of [ill]-[treatment], can diplomatic assurances [received] from the authorities of a [country] where [torture] and [ill]-[treatment] is widely practised ever offer sufficient protection against that [risk]?   (also S0 #6)

3. **001-101586**  score 14.13  
   CASE OF SULTANOV v. RUSSIA (2010)  |  RUSSIA  |  art. 3,5,6  
   match? yes / kinda / no
   snippet: However, if in fact there would appear to be a [risk] of [ill]-[treatment], can diplomatic assurances [received] from the authorities of a [country] where [torture] and [ill]-[treatment] is widely practised ever offer sufficient protection against that [risk]?   (also S0 #1)

4. **001-86086**  score 14.08  
   CASE OF ISMOILOV AND OTHERS v. RUSSIA (2008)  |  RUSSIA  |  art. 3,5,6  
   match? yes / kinda / no
   snippet: Amnesty International considers all such detained individuals to be at serious [risk] of being subjected to [torture] and other [ill]-[treatment]. Amnesty International also considers those individuals who have been charged with criminal offences to be at [risk] of being tried in a manner that violates international fair trial standards. ...   (also S0 #5)

5. **001-99796**  score 13.99  
   CASE OF YULDASHEV v. RUSSIA (2010)  |  RUSSIA  |  art. 13,3,5  
   match? yes / kinda / no
   snippet: However, if in fact there would appear to be a [risk] of [ill]-[treatment], can diplomatic assurances [received] from the authorities of a [country] where [torture] and [ill]-[treatment] is widely practised ever offer sufficient protection against that [risk]?   (also S0 #3)

6. **001-116330**  score 13.80  
   CASE OF ZOKHIDOV v. RUSSIA (2013)  |  RUSSIA  |  art. 3,34,5  
   match? yes / kinda / no
   snippet: The applicant appealed against the decision, reiterating that, as a person accused of participation in a proscribed religious and extremist organisation and of crimes against State security, he ran an increased [risk] of [ill]-[treatment] and [torture] in case of his [extradition]. In this connection, he relied on reports from various international organisations, which specifically pointed out that individuals accused of membership of HT were particularly exposed to a [risk] of [torture].   (also S0 #4)

7. **001-108162**  score 13.17  
   CASE OF ERGASHEV v. RUSSIA (2011)  |  RUSSIA  |  art. 3,5,6  
   match? yes / kinda / no
   snippet: However, if in fact there would appear to be a [risk] of [ill]-[treatment], can diplomatic assurances [received] from the authorities of a [country] where [torture] and [ill]-[treatment] is widely practised ever offer sufficient protection against that [risk]?   (also S0 #8)

8. **001-128055**  score 12.77  
   CASE OF KASYMAKHUNOV v. RUSSIA (2013)  |  RUSSIA  |  art. 3,34,5  
   match? yes / kinda / no
   snippet: The applicant asked the Prosecutor General’s Office of the Russian Federation to refuse the request for his [extradition]. He submitted, in particular, that he would run a real [risk] of [torture] or inhuman [treatment] if [extradited] to Uzbekistan. Relying on Article 3 of the Convention and the Court’s case-law (he referred to Ismoilov and Others v.   (**only in S1**)

9. **001-108629**  score 12.69  
   CASE OF OTHMAN (ABU QATADA) v. THE UNITED KINGDOM (2012)  |  UNITED KINGDOM  |  art. 13,3,5,6  
   match? yes / kinda / no  (also S0 #7)

10. **001-183361**  score 12.68  
   CASE OF BATYRKHAIROV v. TURKEY (2018)  |  TURKEY  |  art. 13,3,5  
   match? yes / kinda / no
   snippet: In his petition, he stated, inter alia, that a person who would be subjected to [torture] or other forms of [ill]-[treatment] in his [country] of origin should not be [extradited] to that [country].  (**only in S1**)


---

## IN7 — Civilian casualties from bombardment and shelling

- type: `T1`
- query: `aerial bombardment shelling civilians killed military operation`
- filter: none
- look for: Cases where civilians were killed or injured, or property destroyed, by aerial bombardment or shelling during military operations.
- relevant if: Relevant: deaths, injuries or destruction of homes and property caused by air strikes, artillery or mortar shelling in the course of military or security operations. Not relevant: terrorist bomb attacks and prosecutions of bombers; disappearances or extrajudicial killings without an attack; landmine accidents.
- overlap: 8/10 shared (`001-101936`, `001-104159`, `001-110944`, `001-68379`, `001-68381`, `001-82544`, `001-83578`, `001-90029`)

### S0 — simple (lowercase only)  (2238 matching cases)

1. **001-101936**  score 15.96  
   CASE OF ABUYEVA AND OTHERS v. RUSSIA (2010)  |  RUSSIA  |  art. 13,2,46,P1-1  
   match? yes / kinda / no
   snippet: Per the submitted documents, the investigation established that as a result of the [operation] 43 [civilians] had been [killed] and 53 wounded. Nineteen of the applicants' relatives were listed among the dead (not including the second applicant's son and four relatives of the twenty-fourth applicant).   (also S1 #2)

2. **001-68381**  score 15.21  
   CASE OF ISAYEVA v. RUSSIA (2005)  |  RUSSIA  |  art. 13,2  
   match? yes / kinda / no
   snippet: According to the Government's observations on the admissibility of the complaint, 53 federal servicemen were [killed] and over 200 were wounded during the assault on Katyr-Yurt. The Government also submitted that, as a result of the [military] [operation], over 180 fighters were [killed] and over 240 injured.   (also S1 #3)

3. **001-83578**  score 14.29  
   CASE OF TANGIYEVA v. RUSSIA (2007)  |  RUSSIA  |  art. 13,2,3,38  
   match? yes / kinda / no
   snippet: On 3 June 2005 a [military] prosecutor questioned the commander of one of the [military] units which had taken part in the counterterrorist [operation] in Grozny. He stated that he had not been aware of the applicant’s relatives’ killings.   (also S1 #4)

4. **001-90029**  score 14.09  
   CASE OF UMAYEVA v. RUSSIA (2008)  |  RUSSIA  |  art. 13,2  
   match? yes / kinda / no
   snippet: In October 1999 hostilities resumed between Russian forces and Chechen armed groups. Grozny came under heavy [aerial] and artillery [bombardment].  (also S1 #9)

5. **001-104159**  score 13.67  
   CASE OF ESMUKHAMBETOV AND OTHERS v. RUSSIA (2011)  |  RUSSIA  |  art. 13,2,3,8  
   match? yes / kinda / no  (also S1 #8)

6. **001-157697**  score 13.07  
   CASE OF ABAKAROVA v. RUSSIA (2015)  |  RUSSIA  |  art. 13,2,46  
   match? yes / kinda / no
   snippet: Over a period of three days most fighters present in the village were [killed] (one [military] unit had reported 386 [killed] fighters).  (**only in S0**)

7. **001-82544**  score 12.78  
   CASE OF GONCHARUK v. RUSSIA (2007)  |  RUSSIA  |  art. 13,2  
   match? yes / kinda / no
   snippet: The applicant and five other persons were hiding in a garage located in 4th Neftyanoy Lane and when the [shelling] intensified they ran to a nearby cellar. While running, the applicant was wounded in her leg. When the [shelling] subsided, several [military] servicemen appeared and ordered everyone out of the cellar.   (also S1 #6)

8. **001-159789**  score 11.81  
   CASE OF TRESKAVICA v. CROATIA (2016)  |  CROATIA  |  art. 2,6  
   match? yes / kinda / no
   snippet: The applicants lived in Knin, within the territory of Krajina. During [Operation] Storm the town of Knin was shelled by the Croatian army. During the [shelling] the applicants hid in the basement of their building. J.T. was found dead near a petrol station in Knin after one of the [shelling] attacks.   (**only in S0**)

9. **001-110944**  score 11.33  
   CASE OF DAMAYEV v. RUSSIA (2012)  |  RUSSIA  |  art. 13,2,3  
   match? yes / kinda / no
   snippet: On 12 April 2004 the UGA prosecutor’s office received a phone call from the Prime Minister of the Chechen Republic, informing them that at 2.30 p.m. on 8 April 2004 Mrs Damayeva and her five children had been [killed] as a result of an [aerial] [bombardment].  (also S1 #1)

10. **001-68379**  score 11.32  
   CASE OF ISAYEVA, YUSUPOVA AND BAZAYEVA v. RUSSIA (2005)  |  RUSSIA  |  art. 13,2,3,P1-1  
   match? yes / kinda / no  (also S1 #5)


### S1 — English (stemming + stopwords)  (3359 matching cases)

1. **001-110944**  score 17.49  
   CASE OF DAMAYEV v. RUSSIA (2012)  |  RUSSIA  |  art. 13,2,3  
   match? yes / kinda / no  (also S0 #9)

2. **001-101936**  score 14.20  
   CASE OF ABUYEVA AND OTHERS v. RUSSIA (2010)  |  RUSSIA  |  art. 13,2,46,P1-1  
   match? yes / kinda / no
   snippet: Since the beginning of [military] [operations] by the Russian [military] and security forces in Chechnya in the autumn of 1999, the village of Katyr-Yurt had been treated as a “safe zone.”   (also S0 #1)

3. **001-68381**  score 14.11  
   CASE OF ISAYEVA v. RUSSIA (2005)  |  RUSSIA  |  art. 13,2  
   match? yes / kinda / no
   snippet: According to the Government's observations on the admissibility of the complaint, 53 federal servicemen were [killed] and over 200 were wounded during the assault on Katyr-Yurt. The Government also submitted that, as a result of the [military] [operation], over 180 fighters were [killed] and over 240 injured.   (also S0 #2)

4. **001-83578**  score 14.03  
   CASE OF TANGIYEVA v. RUSSIA (2007)  |  RUSSIA  |  art. 13,2,3,38  
   match? yes / kinda / no
   snippet: On 3 June 2005 a [military] prosecutor questioned the commander of one of the [military] units which had taken part in the counterterrorist [operation] in Grozny. He stated that he had not been aware of the applicant’s relatives’ [killings].   (also S0 #3)

5. **001-68379**  score 13.44  
   CASE OF ISAYEVA, YUSUPOVA AND BAZAYEVA v. RUSSIA (2005)  |  RUSSIA  |  art. 13,2,3,P1-1  
   match? yes / kinda / no  (also S0 #10)

6. **001-82544**  score 13.37  
   CASE OF GONCHARUK v. RUSSIA (2007)  |  RUSSIA  |  art. 13,2  
   match? yes / kinda / no  (also S0 #7)

7. **001-104649**  score 13.28  
   CASE OF KHAMZAYEV AND OTHERS v. RUSSIA (2011)  |  RUSSIA  |  art. 2,8,P1-1  
   match? yes / kinda / no  (**only in S1**)

8. **001-104159**  score 12.86  
   CASE OF ESMUKHAMBETOV AND OTHERS v. RUSSIA (2011)  |  RUSSIA  |  art. 13,2,3,8  
   match? yes / kinda / no
   snippet: Protocol Additional to the Geneva Conventions of 12 August 1949, and Relating to the Protection of Victims of Non-International Armed Conflicts adopted on 8 June 1977 provides in its part IV relating to [civilian] population as follows: Article 13.-Protection of the [civilian] population “1. The [civilian] population and individual [civilians] shall enjoy general protection against the dangers arising from [military] [operations].   (also S0 #5)

9. **001-90029**  score 12.84  
   CASE OF UMAYEVA v. RUSSIA (2008)  |  RUSSIA  |  art. 13,2  
   match? yes / kinda / no
   snippet: In October 1999 hostilities resumed between Russian forces and Chechen armed groups. Grozny came under heavy [aerial] and artillery [bombardment].  (also S0 #4)

10. **001-104662**  score 12.52  
   CASE OF KERIMOVA AND OTHERS v. RUSSIA (2011)  |  RUSSIA  |  art. 2,8,P1-1  
   match? yes / kinda / no  (**only in S1**)


---

## Your notes

- Example where **S1 is better**:
- Example where **S0 is better**:
- Does IN5's country filter look correct?
- Anything else:
