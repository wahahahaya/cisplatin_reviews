# Stage 5 — Editorial Decision & Revision Roadmap

**Date:** 2026-05-25
**Manuscript:** Cisplatin Timing in Oral and Head-and-Neck Cancer
**Pipeline mode:** academic-pipeline → academic-paper-reviewer (full mode)
**Panel:** 5 independent reviewers (EIC + Methodology + Domain + Perspective + Devil's Advocate)

---

## Editorial Decision: **MAJOR REVISION**

| Reviewer | Decision | Key concern |
|---|---|---|
| EIC | Major Revision | Manuscript not yet submission-ready; OSCC-specific evidence thin; scope balance tilted to mechanism |
| Methodology | Major Revision | §7 trial design needs substantial tightening (sample size, endpoint window, sex interaction, dosing rule, biomarker validation) |
| Domain | Major Revision | §3 clinical landscape dated (missing Bonner/RTOG-1016/De-ESCALaTE/KEYNOTE-412); citation-to-claim mismatches; trial eligibility too permissive |
| Perspective | Minor Revision | BMAL1 paradox framing conflates host/tumor; tumor-clock under-developed; missing circadian immunology bridge |
| Devil's Advocate | Major Revision | **CRITICAL:** No direct human evidence for rate-limiting gates; Zhang 2018 misappropriated; Giacchetti 2006 underweighted as falsifying signal |

**Iron Rule #4 applied**: Devil's Advocate flagged 4 CRITICAL issues → Accept is precluded.

---

## Score consensus

| Dimension | Avg | Range |
|---|---|---|
| Originality | 7/10 | 7 (EIC) |
| Significance | 6/10 | 6 (EIC) |
| Mechanistic accuracy | 8.5/10 | 8.5 (Perspective) |
| Clinical accuracy | 6.5/10 | 6.5 (Domain) |
| Literature coverage | 5/10 | 5 (Domain) |
| Trial design rigor | 5/10 | 5 (Methodology) |
| Statistical reasoning | 4/10 | 4 (Methodology) |
| Endpoint validity | 5/10 | 5 (Methodology) |
| Reproducibility | 4/10 | 4 (Methodology) |
| BMAL1 paradox handling | 7/10 | 7 (Perspective) |
| Mouse-to-human translation honesty | 9/10 | 9 (Perspective) |

**Pattern:** Mechanistic content is strong; clinical-domain currency and trial-design methodology are the principal weak points.

---

## Revision Roadmap (prioritized)

### TIER 1 — CRITICAL (must address before Accept)

| # | Issue | Source | Action | Section |
|---|---|---|---|---|
| C1 | **Zhang 2018 misappropriated** — used as evidence for "chronotype-aware" scheduling but tested *sinusoidal infusion-rate modulation* (a different intervention) | DA-CRITICAL #3 | Rewrite §6.2 to honestly distinguish infusion-rate chronomodulation from chronotype-anchored timing; recharacterize Zhang 2018 as relevant but not directly supportive of the proposed framework | §6.2 lines 909–927 |
| C2 | **No direct human evidence for XPA/OCT2 oscillation in OSCC patient kidneys, cochlea, or mucosa** — Table 2 even admits this for XPA | DA-CRITICAL #1; EIC concern #2 | Add explicit "evidence gap" callout in §5 introduction; soften "mechanistically grounded" → "mechanistically plausible" in §1; downgrade related claims in Conclusion | §1 line 156; §5 intro; §8 |
| C3 | **Giacchetti 2006 underweighted** — sex×timing interaction was a direct falsifying signal in the largest platinum chronomodulation trial ever; current 2-sentence treatment is inadequate | DA-CRITICAL #2; Methodology weakness #3 | Expand §6.4 Giacchetti discussion to its own paragraph; add explicit "what the field learned from this failure" framing; revise §7.3 sex stratification with formal interaction test plan + DSMB-mandated interim safety review for female stratum | §6.4 lines 952–960; §7 Table 4 |
| C4 | **Manuscript not yet submission-ready** — author names TBD, affiliations TBD, Fig 1 + Fig 2 are `\placeholder{}` | EIC concern #1 | Resolve authorship; render both figures per `figure/figure.md` prompts | Title block lines 42–44; lines 1264–1287 |
| C5 | **§7 sample size is implausible** — 25% ARR off undefined baseline; α=0.10 one-sided is permissive; n=80/arm underpowered for realistic 10–15% ARR | Methodology weakness #1; DA-MAJOR #3 | State assumed baseline composite rate; provide sample-size sensitivity table for ARR 10/15/20/25%; cite formula (Farrington–Manning or χ²); consider Bayesian go/no-go reformulation | §7; Table 4 sample size row |
| C6 | **§7 endpoint window mismatch** — "cycles 1–2" means ~6 weeks for q3wk but only 2 weeks for weekly; misaligned with mucositis peak (week 4–6) and cumulative AKI | Methodology weakness #2 | Redefine endpoint window as fixed calendar period or per-cycle hazard; pre-specify component analysis with hierarchical testing; consider win-ratio | §7.2; Table 4 endpoint row |

### TIER 2 — MAJOR (significant credibility issues)

| # | Issue | Source | Action | Section |
|---|---|---|---|---|
| M1 | **§3 clinical landscape dated** — missing Bonner 2006 (cetuximab), RTOG 1016 + De-ESCALaTE (cisplatin > cetuximab HPV+), KEYNOTE-412/JAVELIN HN 100 (IO + CRT negative trials), Strojan 2016 (cumulative dose threshold) | Domain concern #2; Domain missing-lit #1, #2, #3, #5 | Add paragraph in §3.2 covering cetuximab establishment + RTOG 1016/De-ESCALaTE; add §3.2 footnote on IO+CRT failures (KEYNOTE-412, JAVELIN HN 100) that explain why cisplatin remains backbone; add Strojan 2016 to §3.3 as the 200 mg/m² cumulative-dose anchor | §3.2; §3.3 |
| M2 | **§4 citation-to-claim mismatches** — Karasawa 2015 cited for both AKI rate AND non-completion rate (two different endpoints); §1 line 110 conflates these | Domain concern #1 | Separate "AKI 20–30%" (Karasawa 2015) from "cycle non-completion 40%" (cite Bernier 2004, Strojan 2016) | §1 lines 110–114; §3.3 lines 331–333 |
| M3 | **SIOPEL 6 framing incomplete** — missing Freyer 2017 (COG ACCL0431) + FDA Pedmark approval 2022 + STS antitumor antagonism caveat that explains why adult HNSCC adoption hasn't occurred | Domain concern #3; Domain missing-lit #4 | Expand §4.2 STS paragraph: cite Freyer 2017 alongside Brock 2018; mention FDA Pedmark approval (Sep 2022); state the antagonism concern explicitly | §4.2 lines 474–482 |
| M4 | **midsleep − 7h dosing rule lacks derivation and is internally inconsistent** — §7.5 claims most patients fall 10am–6pm but for late chronotypes (midsleep 3am) the calculation yields 8pm | Methodology weakness #4; DA-MINOR #4 | Provide derivation with explicit phase-translation citations; show worked example for early/intermediate/late chronotypes; reconcile distribution with feasibility claim using simulated MCTQ data; cite explicitly | §7.1 lines 1067–1071; §7.5 lines 1135–1138; Table 4 chronotype row |
| M5 | **§7 biomarker panel under-specified** — tumor BMAL1/PER2 IHC has no validated antibody/scoring; serial timed urines need inpatient collection unspecified; 3-time-point PBL clock genes requires overnight phlebotomy unaddressed | Methodology weakness #5 | Specify antibody clones, scoring system (Allred or H-score), pathologist blinding, CAP/CLIA validation step; confirm institutional capacity for serial urines; downgrade biomarkers to "if validated assay available" where appropriate | §7.4 lines 1110–1123 |
| M6 | **§7 eligibility too permissive** — eGFR ≥55 instead of CrCl by Cockcroft-Gault (overestimates in cachectic HNSCC); no baseline audiometry (yet ototoxicity is a secondary endpoint); no HPV stratification (mandatory in any modern oropharynx trial); no PS=2 exclusion rationale; no pregnancy testing | Domain concern #5 | Specify CrCl by Cockcroft-Gault; require baseline audiometry; stratify by p16/HPV; state contraception/pregnancy requirements; document PS=2 exclusion rationale | Table 4 population row |
| M7 | **BMAL1 paradox framing conflates host vs tumor** — Li 2022 + Peng 2019 actually concordant on tumor side (both suggest BMAL1 promotes cisplatin sensitivity in HNSCC/NPC); only Zha 2020 is host-side and is a single-laboratory result | Perspective concern #1 | Reframe §5.5 as "two-tissue asymmetry with tumor-side concordance"; state explicitly that Zha 2020 awaits independent replication; update Table 2 BMAL1/ARNTL row; update Conclusion accordingly | §5.5 lines 728–758; Table 2 BMAL1 row; §8 lines 1235–1239 |
| M8 | **Tumor-clock biology underweighted as MECHANISM rather than confounder** — host–tumor clock asymmetry is precisely what creates the therapeutic window; current treatment is defensive | Perspective concern #2 | Add new subsection or expand §5.6 on tumor–host clock asymmetry as a positive mechanism; add "host–tumor clock contrast" biomarker objective to Table 4 | §5.6; Table 4 biomarker row |
| M9 | **Competing toxicity-reduction strategies not benchmarked** — STS, amifostine, proton therapy, IMRT/parotid-sparing, gabapentinoids, intensive hydration/mannitol/Mg all absent | DA-MAJOR #4; Domain practice-relevance | Add a paragraph (could sit in §7 or §8) explicitly benchmarking chronotherapy against established and emerging toxicity-reduction strategies; clarify what chronotherapy adds that these don't | §7 or §8 |
| M10 | **Sex × timing interaction analysis plan missing** — sex listed as stratifier but no formal interaction test power calculation | Methodology weakness #3 | Add pre-specified interaction test with honest power statement ("descriptive only" if underpowered); add DSMB-mandated interim safety review of female stratum; specify enrolment caps if needed | Table 4 stratification + analysis sections |
| M11 | **Scope balance — §2 + §5 mechanistically dense for Oral Oncology readers** | EIC concern #3 | Trim §2.2 (transporters) and §2.3 (NER/apoptosis) by ~30% each; cross-reference Table 1 rather than re-narrating in §4 | §2.2, §2.3 |
| M12 | **§3.3 weekly-vs-3-weekly debate doesn't connect to chronotherapy thesis** | EIC concern #4 | Add closing sentence in §3.3 noting weekly schedules afford more timing-intervention windows (6–7 vs 3); strengthen §7 stratification-by-schedule rationale | §3.3 closing |
| M13 | **References.bib: Hooven2009 entry has wrong authors** (listed VTE/anticoagulation authors, not chronobiology) | Perspective bibliographic concern | Replace Hooven2009 with the correct primary reference for "cancer-patient circadian disruption" (candidates: Lévi 1997, Mormont 2003, Innominato 2014) OR fix the author/title of Hooven entry | references.bib lines 943–954 |
| M14 | **References.bib: Sassa2010, Okyar2011, Seto2016, Okabe2014 still marked [Verify volume/pages]** | Perspective bibliographic concern | Obtain PDFs from codex_survey or alternative sources; complete bib entries | references.bib |

### TIER 3 — MINOR (notable, recoverable)

| # | Issue | Source | Action |
|---|---|---|---|
| m1 | Abstract under-sells trial design (final sentence too generic) | EIC concern #5 | Rewrite final 3 sentences to specify Grade ≥3 mucositis/nephrotoxicity primary endpoint, sex + CFI stratification |
| m2 | "Up to 40% of cancer survivors" CIPN figure (line 542) inappropriate for HNSCC cumulative doses (200–300 mg/m²) | Domain concern #4 | Note HNSCC cumulative doses below classical neuropathy threshold; severe CIPN less of an issue than nephro/oto/mucosal in this population |
| m3 | XPA and OCT2 may have non-congruent phase relationships to chronotype | Perspective concern #4 | Add one sentence in §7.1 acknowledging midsleep-7h is a pragmatic compromise weighted toward OCT2/nephrotoxicity |
| m4 | Gut microbiome circadian effects on mucositis not mentioned | Perspective concern #5 | Add one sentence in §5.4 + row in Table 2 acknowledging microbial circadian rhythms |
| m5 | Missing chronobiology references: Qian 2021 (chrono-ICI), Sulli/Lam/Panda 2019 (tumor clock review), Ruben 2018 (human tissue clock atlas), Thaiss 2014 (microbiome circadian) | Perspective missing-lit #1, #2, #3, #4 | Add 3–5 cross-disciplinary citations |
| m6 | HR 0.546 (line 294) and JCOG1008 HR 0.69 / CI 0.37–1.27 statistical reporting could be tightened | Methodology stats issue | Add non-inferiority margin for JCOG1008; flag HR 0.546 as a Bernier-pooled marginal-CRT effect (not a timing-related estimate) |

---

## Consensus on what's working

All 5 reviewers identified the **BMAL1/ARNTL paradox subsection (§5.5)** as a genuine intellectual contribution, the **mouse-to-human translation caveat (§6.3)** as honestly handled, and the **mechanism-to-translation arc** (§4 → §5 → §7) as the manuscript's structural strength. The **toxicity-first endpoint choice** in §7 is widely praised. The **circadian-integrity stratification** (CFI-based) is recognized as novel and addresses the Hooven critique constructively.

---

## Path forward

The conceptual contribution is publishable. The manuscript should:

1. **Resolve the 6 CRITICAL items first** — these affect the paper's defensibility and cannot be deferred.
2. **Address the 14 MAJOR items systematically** — these are credibility issues that reviewers will flag at any journal.
3. **Address Minor items in a single editing pass** at the end.

Estimated effort: 2–3 days of focused revision for an experienced HNSCC clinician-author + 1 day for figure rendering.

After revision: → Stage 6 (re-review verification) → Stage 7 (final integrity check) → Stage 8 (finalize).
