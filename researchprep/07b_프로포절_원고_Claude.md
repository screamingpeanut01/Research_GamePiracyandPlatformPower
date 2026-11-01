# From Emulation to AI-Enabled Replication: How Console Platform Owners Govern the Execution of Their Games Outside the Console

[Name] · [Student ID] · Digital Platform Research (MAC613) · Final Paper Proposal

## 1. Research Background

Video game consoles are one of the standard examples in the theory of two-sided markets (Rochet & Tirole, 2003). A console connects players on one side with game developers and publishers on the other, and the value of the console to each side depends on how many participants join the other side. In this proposal, the *platform owner* is the firm that runs the console platform (Sony, Microsoft, or Nintendo), and a *complementor* is a firm that supplies games to the platform, such as a developer or a publisher. Platform owners are also complementors, because they publish games through their own studios. Exclusive games have long been a central means of competition between consoles, since a game that is available on only one console gives players a reason to choose that console. The console market remains large. According to Newzoo, global games revenue in 2025 was USD 201.6 billion, and consoles accounted for 22% of it.[^1]

Attempts to run console games outside the console are not new. In this proposal, *running console games outside the console* refers to cases in which a game that was released for a console runs on a PC, in a web browser, or on another device without the permission of the platform owner. Two practices have made this possible. *Emulation* imitates the original hardware and operating system so that the original game binary can run on other hardware. *Decompilation-based porting* recovers source code from the binary and then rebuilds the game for another environment; static recompilation and browser ports belong to this practice. In *Sony v. Connectix* (2000), a U.S. court held that copying the console BIOS during the development of an emulator was fair use. Even so, this work has required years of specialist effort. For example, it was not until July 2024, more than ten years after the PlayStation 4 was launched in November 2013, that the emulator shadPS4 could run the PlayStation 4 exclusive *Bloodborne* as far as its character creation menu.[^2] According to decomp.dev, the decompilation of *Super Smash Bros. Melee* took six years to reach 100%.[^3] Ports built from decompiled code also predate coding agents: Nintendo reportedly had a PC port of *Super Mario 64* removed in 2020, but no action has been reported against *Ship of Harkinian*, a 2022 port that requires users' own copy of the game (Table 1). In this period, Nintendo relied on legal enforcement, while Microsoft and Sony began to release their own games on PC. When Nintendo reached a settlement with the developer of the Switch emulator Yuzu in 2024, its claims reportedly rested on the ban on trafficking in circumvention tools under the Digital Millennium Copyright Act (DMCA) and on contributory infringement, not on emulation itself.[^4]

From late 2025, records began to appear which suggest that coding agents built on large language models have lowered both the cost of this work and the skill that it requires. *AI-enabled replication* refers here to decompilation and porting that are carried out with the help of such agents; whether it calls for a new concept is one of the questions of this study. According to the developer's own account, *Snowboard Kids* for the Nintendo 64 was decompiled to a 100% match in 84 days.[^5] In psxrecomp, a static recompiler for PlayStation games, 1,519 of 3,123 commits are labeled as AI co-authored, and the developer describes themselves as having had no prior experience in the field.[^6] In the commit history of the PSP emulator PPSSPP, commits co-authored by Claude rose from none through June 2026 to 543 between 1 and 14 October 2026.[^7] Because developers add such labels voluntarily, these counts are lower bounds. In September and October 2026, browser versions of *Halo: Combat Evolved*, *Call of Duty: Black Ops*, and *Grand Theft Auto: Vice City* were reportedly released.[^8]

The period before November 2025 is called here the pre-agent period, and the period since then the AI-enabled period. In the AI-enabled period, the responses of the three platform owners began to diverge, and Microsoft announced a response that can be read as a new type, *absorption*, which brings outside activity inside the platform (Table 1). Whether this change is only a faster form of an existing phenomenon, or a new phenomenon that existing concepts cannot explain, has not yet been examined.

**Table 1.** Selected events and platform-owner responses

| Period | Date | Actor | Event or response | Source |
|---|---|---|---|---|
| Pre-agent | Jun 2016 | Microsoft | Announces Xbox Play Anywhere, under which a game bought once can be played on both Xbox One and Windows 10 PCs | The Next Web[^9] |
| Pre-agent | May 2020 | Nintendo | Copyright complaints remove the *Super Mario 64* PC port from YouTube and Google | Shacknews[^10] |
| Pre-agent | Aug 2020 | Sony | Releases *Horizon Zero Dawn*, a former PlayStation 4 exclusive, on PC | PlayStation Blog[^11] |
| Pre-agent | Mar 2022 | Nintendo | No action reported against *Ship of Harkinian*, which requires users' own copy of the game | Wikipedia[^12] |
| Pre-agent | May–Jul 2023 | Nintendo / Valve | Dolphin's release on Steam is abandoned after a request from Nintendo | Shacknews[^13] |
| Pre-agent | Mar 2024 | Nintendo | USD 2.4 million settlement with the developer of Yuzu | VGC[^4] |
| Pre-agent | May 2024 | Nintendo | One DMCA notice removes 8,535 repositories that copied Yuzu | VGC[^14] |
| AI-enabled | Dec 2025 | Take-Two (comparison case) | Takedown request under the DMCA against the DOS.Zone browser version of *GTA: Vice City*; whether AI was used in this version is unknown | 80.lv[^15] |
| AI-enabled | Mar 2026 | Microsoft | States that its next console, Project Helix, is "designed to play console and PC games" | Windows Experience Blog[^16] |
| AI-enabled | May 2026 | Sony | According to Bloomberg, narrative single-player first-party games return to PlayStation exclusivity; the PC port of *Ghost of Yōtei* is cancelled | Push Square[^17] |
| AI-enabled | 17 Aug 2026 | Nintendo | Seven DMCA notices remove 401 repositories of Switch emulators | VGC[^18] |
| AI-enabled | Late Sep 2026 | Microsoft (rights holder) | No action reported against the browser version of *Halo: Combat Evolved* or the PC recompilation of *Fable 2*; both require users' own disc images and distribute no game data | PC Gamer[^19]; DSOGaming[^20] |
| AI-enabled | Early Oct 2026 | Microsoft subsidiaries | ZeniMax sends a cease-and-desist letter against the browser game *Fallout: New York*; Activision sends takedown requests against browser ports of *Call of Duty* | Destructoid[^21]; XDA[^22] |
| AI-enabled | 13 Oct 2026 | Microsoft | Launches Xbox Labs; the memo is quoted as seeking "unmistakably good outcomes for players, even when (and sometimes because) they challenge our existing business models" | VGC[^23] |

*Note.* Periods are assigned by date only, so an event in the AI-enabled period does not imply that AI was used in it. All entries except Microsoft's announcement of March 2026 are based on news reports.

## 2. Research Purpose and Significance

This study has two purposes. The first is to determine whether AI-enabled replication differs from the earlier ways of running console games outside the console and, if it does, in what respects. The second is to determine whether the governance responses of console platform owners changed in the AI-enabled period and to explain why the responses differ from one platform owner to another.

The study is needed for three reasons. The first reason is theoretical. Research on two-sided platforms has treated multihoming as a choice that users and complementors make, and it has treated piracy as the copying of original files. When a third party makes a complement run in another environment, the phenomenon does not fit fully into either concept. The second reason concerns governance. Research on boundary resources, including the study of iPhone jailbreaking by Eaton et al. (2015), has examined outside actors who break a platform's controls on the platform's own device. How platform owners respond when their games run without that device has not been examined. The third reason is timeliness and policy. AI marks a period of technological transition for the platform industry, and the rules that govern this area are under review. In the United States, the rulemaking on exemptions to DMCA §1201 for 2027 began on 9 June 2026, according to the U.S. Copyright Office.[^24] In the European Union, the European Commission stated in June 2026 that it would begin to discuss a voluntary code of conduct on ending game services by the end of 2026.[^25]

## 3. Theoretical Background

Video game consoles are two-sided platforms. Each side benefits from the size of the other, so console makers compete for games as well as for players (Rochet & Tirole, 2003; Hagiu & Wright, 2015). Through exclusive contracts and vertical integration, the platform owner controls which games run on which console (Lee, 2013; Cennamo & Santaló, 2013).

Four existing concepts each explain part of the phenomenon. *Multihoming* treats running a game on several platforms as a choice made by publishers and users (Landsman & Stremersch, 2011), not as something that third parties do without permission. *Emulation* resembles backward compatibility, which Kretschmer and Claussen (2016) study across console generations, except that it is not authorized; it covers original binaries but not ports rebuilt from recovered source code. *Disintermediation* describes participants who bypass a platform in order to transact directly (Gu & Zhu, 2021); in the phenomenon studied here, what is bypassed is the environment in which the game runs. Research on *piracy in two-sided markets* shows that the interests of platform owners and developers can diverge (Conner & Rumelt, 1991; Rasch & Wenzel, 2013), and Kim and Kim (2025) find that users' evaluations of legitimate platforms affect their intention to use video piracy websites. This research, however, assumes that original files are copied, whereas some ports require users to supply their own copies.

Platform owners act as private regulators of their ecosystems (Boudreau & Hagiu, 2009). They use *boundary resources*, the tools and rules through which outside developers work with a platform, both to open the platform and to keep control of it (Ghazawneh & Henfridsson, 2013). Eaton et al. (2015) show that outside actors also shape these resources: iPhone jailbreakers repeatedly broke Apple's controls, Apple answered with software updates and claims under the DMCA, and the U.S. Copyright Office exempted jailbreaking in 2010. Jailbreaking, however, still uses the platform's own device, whereas the ports studied here replace the device itself.

From these studies, the study classifies responses by type and by lever. The types are suppression (removing the output by legal or technical means), re-closure (tightening exclusivity, digital distribution, or account-based services), absorption (bringing the activity inside the platform's own offerings), and tolerance (no observable response). The levers are legal enforcement, technical measures, exclusivity and release strategy, and opening.

## 4. Research Questions and Propositions

- **RQ1.** Does AI-enabled replication differ from earlier ways of running console games outside the console, and if so, in which dimensions?
- **RQ2.** Did the governance responses of Sony, Microsoft, and Nintendo change between the pre-agent period and the AI-enabled period, and if so, how?
- **RQ3.** Which platform-level conditions account for the differences in responses across the three platform owners?

RQ1 is answered descriptively by comparing the two periods. For RQ2 and RQ3, the study states propositions rather than statistical hypotheses, because it compares three cases, and it compares each proposition with the case evidence through pattern matching (Yin, 2018). Each proposition is stated with an observation that would weaken it and is checked against events that were not used to form it.

**P1.** The more a platform depends on exclusive first-party games, the more its owner relies on legal enforcement in both periods (Lee, 2013). P1 would be weakened if Sony, which also depends on exclusive games, made few takedown requests.

**P2.** When a platform owner is also a large publisher on several platforms, its platform division and its publishing division respond differently (Rasch & Wenzel, 2013). P2 would be weakened if Microsoft's publishing subsidiaries also tolerated ports, or if its platform division sought their removal.

**P3.** When control over code weakens, platform owners strengthen boundaries that cannot be copied with the code, such as the timing of releases, digital distribution, and accounts (Ghazawneh & Henfridsson, 2013). P3 would be weakened if Sony's documents explain its return to exclusivity and its end of disc production[^26] by the sales of its PC ports or by production costs.

**P4.** In the AI-enabled period, enforcement rests on copyright in game assets and on trademarks rather than on copyright in code. P4 would be weakened if the same distinction already governed enforcement in the pre-agent period (Table 1), or if the ports left alone were limited to Microsoft's own games, because Microsoft's absorption strategy (P2) could also explain the absence of action.

A new concept is defined only if a *difference in kind*, that is, a new category of actor, form of output, type or lever of response, or legal basis, appears in both the phenomenon and the response. A reduction in time or effort alone is a difference in degree. If the condition is not met, the conclusion that existing concepts explain the phenomenon is reported as a result (Chaffee, 1991; Podsakoff et al., 2016).

## 5. Methodology

The study is a longitudinal comparison of three cases (Eisenhardt, 1989): Sony, Microsoft, and Nintendo. Microsoft's platform division and its publishing subsidiaries, Activision Blizzard and ZeniMax, are treated separately, and Take-Two, a publisher without a platform, serves as a comparison case. The unit of analysis is a replication event, such as the release of an emulator, a port, or a decompilation project. Each event is coded for the response that followed it, including no observable response. Projects that create new games in existing franchises, such as *Fallout: New York*, are recorded separately. The pre-agent period runs from January 2016 to October 2025, and the AI-enabled period from November 2025 to December 2026. The boundary is set at the earliest AI-assisted decompilation that was found, that of *Snowboard Kids 2* (a different project from the one in Section 1), and it remains provisional.

Four sources of data are used. The first is GitHub's public archive of DMCA notices, which held 7,104 notices from January 2024 to October 2026 alone; the notices will be filtered by party names and keywords before they are read.[^27] The Lumen Database supplements this archive. The second source is the commit histories and labels of AI co-authorship in decompilation and emulator repositories. The third is corporate documents, such as annual reports and official blogs, and the fourth is news reports and histories of emulation (Hansen, 2024, 2026). Events are compared on five dimensions of the phenomenon (time and effort, actors, output form, original-data requirement, and reappearance after takedown) and four dimensions of the response (type, lever, legal basis, and organizational unit).

Both periods are coded with the same scheme and the same sources. Differences between the periods may also reflect causes other than AI, such as the ageing of the console generation, Microsoft's release of its games on rival consoles, and the sales of Sony's PC ports; these explanations are checked against corporate documents. If the condition in Section 4 is met, the concept is defined with reference to Gioia et al. (2013).

## 6. Expected Results and Contributions

For RQ1, the clearest difference is expected in time and effort. Differences in kind may appear in actors (non-specialist individuals), in output forms (browser ports and mashups), and in how quickly outputs reappear after takedowns. For RQ2 and RQ3, the expected patterns are those in P1 to P4.

In theory, the study shows how far existing platform concepts explain the phenomenon and how it differs from jailbreaking, it may propose a new concept, and it examines whether a platform owner's dual role as platform and publisher divides its responses. In practice, it informs the exclusivity strategies of platform firms and the debates on exemptions for preservation and interoperability, such as those under DMCA §1201 and Article 6 of the EU Software Directive.

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

Yin, R. K. (2018). *Case study research and applications: Design and methods* (6th ed.). Sage.

[^1]: Newzoo, via PocketGamer.biz. https://www.pocketgamer.biz/global-games-revenue-surpasses-200bn-for-the-first-time-mobile-generates-113bn/
[^2]: Wikipedia, "ShadPS4". https://en.wikipedia.org/wiki/ShadPS4
[^3]: decomp.dev. https://decomp.dev/doldecomp/melee
[^4]: VGC. https://videogameschronicle.com/news/switch-emulator-creator-settles-nintendo-lawsuit-for-2-4m
[^5]: Chris Lewis. https://blog.chrislewis.au/decompiling-a-nintendo-64-game-in-84-days/
[^6]: Developer's account of psxrecomp. https://1379.tech/i-built-a-ps1-static-recompiler-with-no-prior-experience-and-claude-code/
[^7]: PPSSPP repository. https://github.com/hrydgard/ppsspp
[^8]: Kotaku, 9 October 2026. https://kotaku.com/we-might-be-cooked-as-these-vibe-coded-web-browser-ports-of-halo-the-simpsons-hit-and-run-and-gta-vice-city-seem-to-work-perfectly-2000743300
[^9]: The Next Web, 14 June 2016. https://thenextweb.com/news/xbox-play-anywhere-lets-enjoy-console-games-windows-10
[^10]: Shacknews, 8 May 2020. https://shacknews.com/article/117984/working-super-mario-64-pc-port-hit-by-nintendo-copyright-takedowns-of-course
[^11]: PlayStation Blog, 7 August 2020. https://blog.playstation.com/2020/08/07/horizon-zero-dawn-complete-edition-sees-pc-release-today/
[^12]: Wikipedia, "Ship of Harkinian". https://en.wikipedia.org/wiki/Ship_of_Harkinian
[^13]: Shacknews. https://shacknews.com/article/136341/dolphin-emulator-steam-launch-abandoned
[^14]: VGC. https://www.videogameschronicle.com/news/nintendo-takes-down-more-than-8500-clones-of-switch-emulator-yuzu-with-a-single-dmca-notice
[^15]: 80.lv. https://80.lv/articles/take-two-takes-down-browser-version-of-gta-vice-city-with-dmca-request
[^16]: Windows Experience Blog, 11 March 2026. https://blogs.windows.com/windowsexperience/2026/03/11/gdc-2026-next-generation-of-xbox-designed-to-play-console-and-pc-games/
[^17]: Push Square. https://www.pushsquare.com/news/2026/05/sony-reportedly-confirms-shift-back-to-ps5-single-player-exclusive-games
[^18]: VGC. https://videogameschronicle.com/news/nintendo-wipes-out-400-more-switch-emulator-repositories-on-github-as-it-continues-its-fight-on-piracy
[^19]: PC Gamer. https://www.pcgamer.com/hardware/you-can-now-play-halo-combat-evolved-in-a-web-browser-and-it-even-has-multiplayer/
[^20]: DSOGaming. https://dsogaming.com/news/fable-2-unofficial-native-pc-port-available-for-download/
[^21]: Destructoid. https://www.destructoid.com/activision-bethesda-take-down-ai-generated-mods/
[^22]: XDA. https://www.xda-developers.com/activision-hits-vibe-coded-classic-call-of-duty-browser-ports-with-dmca-takedowns/
[^23]: VGC. https://www.videogameschronicle.com/news/asha-sharma-forms-xbox-labs-in-response-to-explosion-of-ai-powered-mods-and-ports/
[^24]: U.S. Copyright Office. https://www.copyright.gov/1201/2027/
[^25]: European Commission, reply to the European Citizens' Initiative "Stop Destroying Videogames". https://citizens-initiative.europa.eu/stop-destroying-videogames-commissions-reply-european-citizens-initiative_en
[^26]: PlayStation Blog, 1 July 2026. https://blog.playstation.com/2026/07/01/physical-disc-production-ending-in-january-2028-for-new-games-releasing-on-playstation-consoles/
[^27]: GitHub DMCA repository. https://github.com/github/dmca
