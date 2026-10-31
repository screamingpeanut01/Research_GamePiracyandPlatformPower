# From Emulation to AI-Enabled Replication: How Console Platform Owners Govern the Execution of Their Games Outside the Console

[Name] · [Student ID] · Digital Platform Research (MAC613) · Final Paper Proposal

## 1. Research Background

Video game consoles are one of the standard examples in the theory of two-sided markets (Rochet & Tirole, 2003). A console connects players on one side with game developers and publishers on the other, and the value of the console to each side depends on how many participants join the other side. In this proposal, the *platform owner* is the firm that runs the console platform (Sony, Microsoft, or Nintendo), and a *complementor* is a firm that supplies games to the platform, such as a developer or a publisher. Platform owners are also complementors, because they publish games through their own studios. Exclusive games have long been a central means of competition between consoles, since a game that is available on only one console gives players a reason to choose that console. The console market remains large. According to Newzoo, global games revenue in 2025 was USD 201.6 billion, and consoles accounted for 22% of it.[^1] The PlayStation 5 had reportedly shipped 95.3 million units as of 30 June 2026,[^2] and, according to Nintendo, the Switch and the Switch 2 had shipped 156.59 million and 23.68 million units by the same date.[^3]

Attempts to run console games outside the console are not new. In this proposal, *running console games outside the console* is a descriptive phrase, not a concept. It refers to cases in which a game that was released for a console runs on a PC, in a web browser, or on another device without the permission of the platform owner. Two practices have made this possible. *Emulation* imitates the original hardware and operating system so that the original game binary can run on other hardware. *Decompilation-based porting* recovers source code from the binary and then rebuilds the game for another environment; static recompilation and browser ports belong to this practice. In *Sony v. Connectix* (2000), a U.S. court held that copying the console BIOS during the development of an emulator was fair use. Even so, this work has required years of specialist effort. It reportedly took about 11 years from the launch of the PlayStation 3, and again of the PlayStation 4, until a flagship title of each generation became playable on an emulator.[^4] According to decomp.dev, the decompilation of *Super Smash Bros. Melee* took six years to reach 100%.[^5] Platform owners responded mainly through legal enforcement. In March 2024, Nintendo reportedly settled with Tropic Haze, the developer of the Switch emulator Yuzu, for USD 2.4 million. The claims rested on the ban on trafficking in circumvention tools under the Digital Millennium Copyright Act (DMCA) and on contributory infringement, not on emulation itself.[^6] Two months later, a single DMCA notice from Nintendo reportedly removed 8,535 repositories that copied Yuzu.[^7] In 2023, the release of the Dolphin emulator on Steam was reportedly abandoned after a request from Nintendo.[^8]

From late 2025, records began to appear which suggest that coding agents built on large language models have lowered both the cost of this work and the skill that it requires. In this proposal, *AI-enabled replication* refers to decompilation and porting that are carried out with the help of such agents. It is the object that the study examines, and it is not treated in advance as a new concept. According to the developer's own account, *Snowboard Kids* for the Nintendo 64 was decompiled to a 100% match in 84 days.[^9] In psxrecomp, a static recompiler for PlayStation games, 1,519 of 3,123 commits are labeled as AI co-authored, and the developer describes themselves as having had no prior experience in the field.[^10] In the commit history of the PSP emulator PPSSPP, commits co-authored by Claude rose from none through June 2026 to 543 between 1 and 14 October 2026.[^11] Because developers add such labels voluntarily, these counts are lower bounds. In September and October 2026, browser versions of *Halo: Combat Evolved*, *Call of Duty: Black Ops*, and *Grand Theft Auto: Vice City* were reportedly released.[^12]

During this period, the responses of the three platform owners diverged. A type of response that was not visible before, absorption, also appeared (Table 1). Whether this change is only a faster form of an existing phenomenon, or a new phenomenon that existing concepts cannot explain, has not yet been examined.

**Table 1.** Selected events and platform-owner responses

| Period | Date | Actor | Event or response | Source |
|---|---|---|---|---|
| Pre-agent | May–Jul 2023 | Nintendo / Valve | Dolphin's release on Steam is abandoned after a request from Nintendo (reportedly) | Shacknews[^8] |
| Pre-agent | Mar 2024 | Nintendo | USD 2.4 million settlement with the developer of Yuzu, based on the DMCA ban on circumvention tools and on contributory infringement (reportedly) | VGC[^6] |
| Pre-agent | May 2024 | Nintendo | One DMCA notice removes 8,535 repositories that copied Yuzu (reportedly) | VGC[^7] |
| AI-enabled | Dec 2025 | Take-Two (comparison case) | Takedown request under the DMCA against the DOS.Zone browser version of *GTA: Vice City* (reportedly); whether AI was used in this version is unknown | 80.lv[^13] |
| AI-enabled | Mar 2026 | Microsoft | States that its next console, Project Helix, is "designed to play console and PC games" | Windows Experience Blog[^14] |
| AI-enabled | May 2026 | Sony | According to Bloomberg, narrative single-player first-party games return to PlayStation exclusivity; the PC port of *Ghost of Yōtei* is cancelled (reportedly) | Push Square[^15] |
| AI-enabled | Aug 2026 | Nintendo | Seven DMCA notices remove 401 repositories of Switch emulators (reportedly) | VGC[^16] |
| AI-enabled | Early Oct 2026 | Microsoft subsidiaries | ZeniMax sends a cease-and-desist letter against the browser game *Fallout: New York*; Activision sends takedown requests against browser ports of *Call of Duty* (reportedly) | Destructoid[^17]; XDA[^18] |
| AI-enabled | 13 Oct 2026 | Microsoft | Launches Xbox Labs; the memo is quoted as seeking "unmistakably good outcomes for players, even when (and sometimes because) they challenge our existing business models" | VGC[^19] |

*Note.* Periods are assigned by date only. An event that falls in the AI-enabled period does not imply that AI was used in it.

## 2. Research Purpose and Significance

This study has two purposes. The first is to determine whether AI-enabled replication differs from the earlier ways of running console games outside the console and, if it does, in what respects. The second is to explain whether the governance responses of console platform owners changed in the AI-enabled period, and why the responses differ from one platform owner to another.

The study is needed for three reasons. The first reason is theoretical. Research on two-sided platforms has treated multihoming as a choice that users and complementors make, and it has treated piracy as the copying of original files. When a third party makes a complement run in another environment, the phenomenon does not fit fully into either concept. This study therefore first establishes how far the existing concepts can explain it. The second reason concerns governance. Research on boundary resources has examined how platform owners adjust the balance between openness and control, but it has not examined situations in which outside actors cross the boundary of a platform without permission. The third reason is timeliness and policy. AI marks a period of technological transition for the platform industry, and the rules that govern this area are under review. In the United States, the rulemaking on exemptions to DMCA §1201 for 2027 began on 9 June 2026, according to the U.S. Copyright Office.[^20] In the European Union, the European Commission reportedly said that it would begin to discuss a voluntary code of conduct on ending game services by the end of 2026.[^21]

## 3. Theoretical Background

### 3.1 Consoles as two-sided platforms

A two-sided platform serves as an intermediary between two groups of users, and each group benefits from the size of the other group (Rochet & Tirole, 2003; Hagiu & Wright, 2015). These cross-side network effects explain why console makers compete for games as well as for players. Two strategies follow from this structure. The first is exclusivity: a platform owner can secure games that are available only on its console. The second is vertical integration: a platform owner can own the studios that make such games. Lee (2013) examines how exclusive contracts and vertical integration affect competition between console platforms. Cennamo and Santaló (2013) treat such choices as part of the strategic trade-offs that platform owners face. In both studies, the platform owner controls which games run on which console.

### 3.2 Existing concepts for running complements outside the platform

Four existing concepts explain part of the phenomenon. Each one also stops at a certain point.

The first concept is *multihoming*. Landsman and Stremersch (2011) study how releasing a game on several consoles affects console sales. In their framework, multihoming is a choice that publishers and users make. The concept does not cover cases in which a third party creates a new way to run a game without the permission of either the platform owner or the publisher.

The second concept is *emulation*, which Kretschmer and Claussen (2016) treat as a form of backward compatibility. An unofficial emulator resembles backward compatibility that has not been authorized. This view explains how original binaries run on other hardware. It does not explain cases in which the source code is recovered and the game is rebuilt as a native or browser version, or cases in which parts of different games are combined.

The third concept is *disintermediation*. Gu and Zhu (2021) study how participants in a marketplace bypass the platform and transact directly. The phenomenon studied here shares the bypassing of the platform. However, what is replaced is the environment in which the game runs, not a transaction.

The fourth concept is *piracy in two-sided markets*. Conner and Rumelt (1991) show that protection against piracy is not always in the interest of a software firm. Rasch and Wenzel (2013) show that, when piracy is possible, the interests of the platform owner and of developers can diverge. Kim and Kim (2025) find that users' evaluations of legitimate platforms affect their intention to use piracy websites. This literature, however, assumes that original files are copied. Some ports require users to supply their own copy of the original data, so they do not copy the game in this sense.

Table 2 summarizes what each concept captures and what it leaves out.

**Table 2.** What existing concepts capture and leave out

| Concept | Who acts | Platform authorization | What it captures | What it leaves out |
|---|---|---|---|---|
| Multihoming | Publishers, users | Yes | How participation in several platforms affects the value of exclusivity | Ways of running a game that third parties create without permission |
| Emulation / backward compatibility | Emulator developers | No (unofficial) or yes (official) | Running the original binary on other hardware | Recovery of source code, native and browser ports, and combinations of games |
| Disintermediation | Participants in a transaction | No | Transactions that bypass the platform | Replacement of the environment in which a game runs, which is not a transaction |
| Piracy in two-sided markets | Users | No | How copying original files affects the interests of the platform owner and developers | Ports that require the user's own original data and therefore do not copy it |

### 3.3 Platform governance and boundary resources

Platform owners act as private regulators of their ecosystems. They set the rules that decide who may participate and on what terms (Boudreau & Hagiu, 2009). Ghazawneh and Henfridsson (2013) describe how platform owners use *boundary resources*, the tools and rules through which outside developers work with a platform, to manage two goals. With *resourcing*, they open the platform to outside developers; with *securing*, they keep control over it. Eaton et al. (2015) add that boundary resources change through the actions of many parties, not only those of the platform owner. These studies, however, assume that outside actors cross the boundary through the resources that the platform provides. They do not examine actors who cross the boundary without permission.

### Analytical framework

From these three bodies of work, this study derives a framework with two dimensions. The first dimension is the *type of response*: suppression, re-closure, absorption, or tolerance. Suppression stops the activity; re-closure strengthens boundaries that are harder to replicate; absorption brings the activity inside the platform; and tolerance leaves it alone. The second dimension is the *lever* that the response uses: legal enforcement, technical measures, exclusivity and release strategy, or opening.

## 4. Research Questions and Propositions

The study asks three research questions.

- **RQ1.** Does AI-enabled replication differ from earlier ways of running console games outside the console, and if so, in which dimensions?
- **RQ2.** Did the governance responses of Sony, Microsoft, and Nintendo change between the pre-agent period and the AI-enabled period, and if so, how?
- **RQ3.** Which platform-level conditions account for the differences in responses across the three platform owners?

RQ1 is exploratory, so it has no proposition. It is answered by comparing the two periods on the dimensions in Table 3. RQ2 and RQ3 are guided by four propositions that are drawn from the existing concepts. Because the study compares three cases, the propositions are compared with the cases rather than tested statistically (Eisenhardt, 1989).

**P1.** The more the value of a platform depends on exclusive first-party games, the more its owner responds with legal enforcement (suppression) in both periods (Landsman & Stremersch, 2011; Lee, 2013). P1 would be supported if Nintendo continued mass takedown requests across both periods.

**P2.** When a platform owner is also a large complementor that releases games on several platforms, the responses of its platform division and of its publishing division diverge (Lee, 2013; Rasch & Wenzel, 2013). P2 would be supported by Microsoft's case, in which Xbox Labs (absorption) and the takedown requests from Activision and ZeniMax appeared in the same month.

**P3.** When control over the execution of code weakens, platform owners strengthen boundaries that are harder to replicate, such as exclusivity and release strategy, digital distribution, and accounts and services (re-closure) (Ghazawneh & Henfridsson, 2013; Eaton et al., 2015). P3 would be supported by Sony's return to exclusivity, its announced end of disc production for new games from January 2028,[^22] and the reported rise in the share of digital software, add-on content, and network services in PlayStation revenue, from 56% in FY2022 to 70% in FY2025.

**P4.** In the AI-enabled period, the legal basis of enforcement shifts from copyright in code and the ban on circumvention to copyright in game assets and trademarks (Boudreau & Hagiu, 2009). P4 would be supported if takedowns were limited to projects that distributed original assets or used a trademark, and if projects that require a user's own disc image were left untouched. The Activision ports reportedly used maps, models, and animations that were extracted from the original PC game, and the ZeniMax letter reportedly relied on its trademark.[^17] In contrast, no enforcement action has been reported against the browser version of *Halo: Combat Evolved* or the PC recompilation of *Fable 2*, an Xbox 360 exclusive that Microsoft owns. Neither distributes game data, and both require users to make their own disc image.[^23][^24]

The study defines a new concept only under a stated condition. A *difference in kind* must appear in at least one dimension of the phenomenon and in at least one dimension of the response in Table 3. A difference in kind means that a category of actor, a form of output, a lever of response, or a legal basis appears that did not exist in the pre-agent period. A reduction in time or cost alone counts as a difference in degree. If the condition is not met, the conclusion that a combination of existing concepts explains the phenomenon is reported as a result. If the condition is met, the new concept is defined following the procedures of Chaffee (1991) and Podsakoff et al. (2016).

## 5. Methodology

The study uses a longitudinal multiple-case design that compares two periods (Eisenhardt, 1989). The cases are Sony Interactive Entertainment, Microsoft (Xbox, together with Activision Blizzard and ZeniMax), and Nintendo. Take-Two, a publisher that does not own a platform, serves as a comparison case. The unit of analysis is a response event by a platform owner. Microsoft is divided into two subunits, its platform division and its publishing subsidiaries, so that P2 can be examined.

The two periods are provisional. The pre-agent period runs from January 2016 to October 2025 and includes the years in which emulators and decompilation projects for the PlayStation 4 and Switch generation were active. The AI-enabled period runs from November 2025 to December 2026. Its start is set at the earliest record of AI-assisted decompilation that was found, the work on *Snowboard Kids 2* in November 2025. The main study will fix this boundary by examining when AI co-authored commits first appear in major repositories and by reviewing the eras of emulation proposed by Hansen (2024, 2026).

Four sources of data are used. The first is the record of enforcement. GitHub publishes the DMCA notices that it receives in a public repository (github/dmca),[^25] which has accumulated notices since 2011 and so covers both periods. A preliminary count found 7,104 notices from January 2024 to October 2026 alone. Many of them are unrelated to games, so each notice will be read and classified. Takedowns outside GitHub will be traced through the Lumen Database and news reports. The second source is the record of development: commit histories of decompilation and emulator repositories, including labels of AI co-authorship, and the progress rates reported by decomp.dev. These data are used to set the boundary between the periods. Because developers label AI co-authorship voluntarily, these data undercount the use of AI. The third source is corporate documents: annual reports (Sony's Form 20-F, Microsoft's Form 10-K, and Nintendo's annual report), official blogs, and changes to terms of use. The fourth source is industry reporting and historical research on emulation (Hansen, 2024, 2026), which are used to reconstruct the events of the pre-agent period.

Table 3 lists the dimensions on which the two periods and the three cases are compared.

**Table 3.** Comparison dimensions and coding scheme

| Area | Dimension | Categories or indicators |
|---|---|---|
| Phenomenon (RQ1) | Time and cost | Time from the start of a project to its completion |
| Phenomenon | Actors | Specialist community / non-specialist individual / firm |
| Phenomenon | Output form | Emulator / native port / browser port / mashup |
| Phenomenon | Original-data requirement | Requires the user's original image / bundles the assets |
| Phenomenon | Reappearance after takedown | Time until the same output is published again after a takedown |
| Response (RQ2, RQ3) | Response type | Suppression / re-closure / absorption / tolerance |
| Response | Lever | Legal enforcement / technical measures / exclusivity and release strategy / opening |
| Response | Legal basis | Copyright in code / copyright in assets / anti-circumvention / trademark / not stated |
| Response | Organizational unit | Platform division / publisher subsidiary |

The analysis proceeds in four steps. First, a chronological table of events is built for each case. Second, the two periods are compared within each case. Third, patterns across the cases are compared with P1 to P4. Fourth, if the condition stated in Section 4 is met, a new concept is defined, with reference to the inductive data structure of Gioia et al. (2013).

This final paper examines the AI-enabled period in detail and covers the pre-agent period only through enforcement records and major events. The main study, which begins in 2027, will extend the pre-agent period and the observation period. The study has four limitations. It covers only three cases. It depends on public records. It does not isolate the causal role of AI and relies only on the comparison of periods. Finally, the events are still unfolding.

## 6. Expected Results and Contributions

The following expectations are to be checked against the data, not findings. For RQ1, the difference in time and cost is expected to be clear. Differences in kind may appear in the range of actors (non-specialist individuals), in the form of output (browser ports and mashups), and in how quickly outputs reappear after a takedown. For RQ2 and RQ3, Nintendo is expected to rely on suppression in both periods, and Sony is expected to move toward re-closure in the AI-enabled period. Microsoft is expected to show absorption for the first time in the AI-enabled period, alongside continued enforcement by its publishing subsidiaries. Across the cases, the legal basis of enforcement is expected to shift toward game assets and trademarks.

The study is expected to make three theoretical contributions. First, it sets out how far existing concepts explain the running of console games outside the console, and where they stop. Second, if the condition in Section 4 is met, it proposes a new concept for AI-enabled replication. Third, it examines whether the dual position of a platform owner, as both a platform and a complementor, is a condition that divides its responses.

The study also has practical and policy implications. It informs the exclusivity strategies of platform firms. It also informs current debates on exemptions for preservation and interoperability, such as the exemptions to DMCA §1201 and Article 6 of the EU Software Directive, which permits decompilation when it is necessary for interoperability.

## References

Boudreau, K. J., & Hagiu, A. (2009). Platform rules: Multi-sided platforms as regulators. In A. Gawer (Ed.), *Platforms, markets and innovation*. Edward Elgar. https://doi.org/10.4337/9781849803311.00014

Cennamo, C., & Santaló, J. (2013). Platform competition: Strategic trade-offs in platform markets. *Strategic Management Journal, 34*(11), 1331–1350. https://doi.org/10.1002/smj.2066

Chaffee, S. H. (1991). *Communication concepts 1: Explication*. Sage.

Conner, K. R., & Rumelt, R. P. (1991). Software piracy: An analysis of protection strategies. *Management Science, 37*(2), 125–139. https://doi.org/10.1287/mnsc.37.2.125

Eaton, B., Elaluf-Calderwood, S., Sørensen, C., & Yoo, Y. (2015). Distributed tuning of boundary resources: The case of Apple's iOS service system. *MIS Quarterly, 39*(1), 217–243. https://doi.org/10.25300/MISQ/2015/39.1.10

Eisenhardt, K. M. (1989). Building theories from case study research. *Academy of Management Review, 14*(4), 532–550. https://doi.org/10.2307/258557

Ghazawneh, A., & Henfridsson, O. (2013). Balancing platform control and external contribution in third-party development: The boundary resources model. *Information Systems Journal, 23*(2), 173–192. https://doi.org/10.1111/j.1365-2575.2012.00406.x

Gioia, D. A., Corley, K. G., & Hamilton, A. L. (2013). Seeking qualitative rigor in inductive research: Notes on the Gioia methodology. *Organizational Research Methods, 16*(1), 15–31. https://doi.org/10.1177/1094428112452151

Gu, G., & Zhu, F. (2021). Trust and disintermediation: Evidence from an online freelance marketplace. *Management Science, 67*(2), 794–807. https://doi.org/10.1287/mnsc.2020.3583

Hagiu, A., & Wright, J. (2015). Multi-sided platforms. *International Journal of Industrial Organization, 43*, 162–174. https://doi.org/10.1016/j.ijindorg.2015.03.003

Hansen, J. (2024). Toward a history of emulation: Five eras for videogame emulators. *DiGRA Digital Library*. https://doi.org/10.26503/dl.v2024i3.2796

Hansen, J. (2026). A chronicle of emulation: Proposed eras for video game emulators. *DiGRA Digital Library*. https://doi.org/10.26503/dl.v2026i3.2808

Kim, M. S., & Kim, S. (2025). Why do individuals use online video piracy websites? *Computers in Human Behavior, 166*, Article 108575. https://doi.org/10.1016/j.chb.2025.108575

Kretschmer, T., & Claussen, J. (2016). Generational transitions in platform markets: The role of backward compatibility. *Strategy Science, 1*(2), 90–104. https://doi.org/10.1287/stsc.2015.0009

Landsman, V., & Stremersch, S. (2011). Multihoming in two-sided markets: An empirical inquiry in the video game console industry. *Journal of Marketing, 75*(6), 39–54. https://doi.org/10.1509/jm.09.0199

Lee, R. S. (2013). Vertical integration and exclusivity in platform and two-sided markets. *American Economic Review, 103*(7), 2960–3000. https://doi.org/10.1257/aer.103.7.2960

Podsakoff, P. M., MacKenzie, S. B., & Podsakoff, N. P. (2016). Recommendations for creating better concept definitions in the organizational, behavioral, and social sciences. *Organizational Research Methods, 19*(2), 159–203. https://doi.org/10.1177/1094428115624965

Rasch, A., & Wenzel, T. (2013). Piracy in a two-sided software market. *Journal of Economic Behavior & Organization, 88*, 78–89. https://doi.org/10.1016/j.jebo.2013.01.009

Rochet, J.-C., & Tirole, J. (2003). Platform competition in two-sided markets. *Journal of the European Economic Association, 1*(4), 990–1029. https://doi.org/10.1162/154247603322493212

[^1]: Newzoo, via PocketGamer.biz. https://www.pocketgamer.biz/global-games-revenue-surpasses-200bn-for-the-first-time-mobile-generates-113bn/
[^2]: Gematsu. https://www.gematsu.com/2026/07/ps5-shipments-top-95-3-million
[^3]: Nintendo Investor Relations. https://www.nintendo.co.jp/ir/en/finance/hard_soft/index.html
[^4]: shadPS4. https://en.wikipedia.org/wiki/ShadPS4
[^5]: decomp.dev. https://decomp.dev/doldecomp/melee
[^6]: VGC. https://videogameschronicle.com/news/switch-emulator-creator-settles-nintendo-lawsuit-for-2-4m
[^7]: VGC. https://www.videogameschronicle.com/news/nintendo-takes-down-more-than-8500-clones-of-switch-emulator-yuzu-with-a-single-dmca-notice
[^8]: Shacknews. https://shacknews.com/article/136341/dolphin-emulator-steam-launch-abandoned
[^9]: Chris Lewis. https://blog.chrislewis.au/decompiling-a-nintendo-64-game-in-84-days/
[^10]: Developer's account of psxrecomp. https://1379.tech/i-built-a-ps1-static-recompiler-with-no-prior-experience-and-claude-code/
[^11]: PPSSPP repository. https://github.com/hrydgard/ppsspp
[^12]: Kotaku, 9 October 2026. https://kotaku.com/we-might-be-cooked-as-these-vibe-coded-web-browser-ports-of-halo-the-simpsons-hit-and-run-and-gta-vice-city-seem-to-work-perfectly-2000743300
[^13]: 80.lv. https://80.lv/articles/take-two-takes-down-browser-version-of-gta-vice-city-with-dmca-request
[^14]: Windows Experience Blog, 11 March 2026. https://blogs.windows.com/windowsexperience/2026/03/11/gdc-2026-next-generation-of-xbox-designed-to-play-console-and-pc-games/
[^15]: Push Square. https://www.pushsquare.com/news/2026/05/sony-reportedly-confirms-shift-back-to-ps5-single-player-exclusive-games
[^16]: VGC. https://videogameschronicle.com/news/nintendo-wipes-out-400-more-switch-emulator-repositories-on-github-as-it-continues-its-fight-on-piracy
[^17]: Destructoid. https://www.destructoid.com/activision-bethesda-take-down-ai-generated-mods/
[^18]: XDA. https://www.xda-developers.com/activision-hits-vibe-coded-classic-call-of-duty-browser-ports-with-dmca-takedowns/
[^19]: VGC. https://www.videogameschronicle.com/news/asha-sharma-forms-xbox-labs-in-response-to-explosion-of-ai-powered-mods-and-ports/
[^20]: U.S. Copyright Office. https://www.copyright.gov/1201/2027/
[^21]: European Commission, reply to the European Citizens' Initiative "Stop Destroying Videogames". https://citizens-initiative.europa.eu/stop-destroying-videogames-commissions-reply-european-citizens-initiative_en
[^22]: PlayStation Blog, 1 July 2026. https://blog.playstation.com/2026/07/01/physical-disc-production-ending-in-january-2028-for-new-games-releasing-on-playstation-consoles/
[^23]: PC Gamer. https://www.pcgamer.com/hardware/you-can-now-play-halo-combat-evolved-in-a-web-browser-and-it-even-has-multiplayer/
[^24]: DSOGaming. https://dsogaming.com/news/fable-2-unofficial-native-pc-port-available-for-download/
[^25]: GitHub DMCA repository. https://github.com/github/dmca
