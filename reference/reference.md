# Consolidated Evidence Inventory — Oral Oncology Review

**Manuscript:** Cisplatin Timing in Oral and Head-and-Neck Cancer — Organ-Specific Toxicity Mechanisms, Clinical Delivery Constraints, and the Rationale for Chronotherapy
**Built:** 2026-05-25
**Sources merged:** `info/user_download/` (47 PDFs, named-citation format) + `info/claude_survey/` (3 markdown survey files) + `info/codex_survey/` (≈750 PDFs across `01_usable_for_study_broad/` and `03_manual_screen_title_abstract/`).
**Status:** Stage 1 (evidence gathering) closed; manuscript ready to enter Stage 2 (planning).

---

## 1. Headline summary

| Metric | Count |
|---|---:|
| PDFs in `user_download/` (core, curated) | 47 |
| PDFs in `codex_survey/` (broad screen) | ≈748 |
| Codex_survey papers judged high-value, unique additions | ≈25 |
| Total usable references after consolidation | ≈72 |
| Target reference budget per `prompt.md` | 80–110 |
| Residual reference slots available | 8–38 |

**Net result:** evidence base is dense for Sections 2 (mechanism), 4 (organ-specific toxicity), 5 (circadian gates), 6 (chronotherapy), and 7 (monitoring). The persistent shortfall is **Section 3 landmark phase-III trials**, which neither survey closed.

---

## 2. Coverage status per manuscript section

| § | Topic | user_download | + codex_survey | Coverage | Action |
|---|---|---:|---:|---|---|
| 1 | Introduction framing | 2 | 0 | Sufficient | — |
| 2 | Cisplatin chemistry / DNA damage | 6 | +2 (XPA mechanism, adduct methodology) | Partial → **Improved** | Jamieson 1999 Chem Rev still missing (user to obtain) |
| 3 | OSCC/HNSCC treatment pathways | 4 | +4 (nedaplatin alternative, intra-arterial route, recent oral CRT) | **Insufficient** | Landmark NEJM/JCO trials still missing (see §5 below) |
| 4 | Organ-specific toxicity | 8 | +9 (nephro mechanism, antioxidant review, mucositis clinical, antiemetic modernisation) | Excellent | Brock 2018 NEJM still missing; Aapro 2016 NEPA now covers antiemetic update |
| 5 | Circadian timing gates | 13 | +6 (XPA-NER, MDR rhythm, HIF1/Per2, sex-dependent transporter, circadian medicine framework) | Excellent | Saturated |
| 6 | Chronotherapy clinical / preclinical | 10 | +5 (Seto 2016 dosing-time × cisplatin neurotoxicity, melatonin × cisplatin protective combos, Damato 2021 temozolomide) | Excellent | Saturated |
| 7 | Trial design / circadian monitoring | 9 | +1 (continuous-temperature wearable) | Excellent | Saturated |

---

## 3. References grouped by manuscript section

Format: `[source] file/citation — manuscript use`. **Source codes:** `[UD]` = `info/user_download/`; `[CS-01]` = `info/codex_survey/01_usable_for_study_broad/`; `[CS-03]` = `info/codex_survey/03_manual_screen_title_abstract/`; `[GAP]` = recommended but not yet obtained (user to download).

### §1 — Introduction

- `[UD]` Kelland 2007, *Nat Rev Cancer* (Platinum-based cancer chemotherapy) — opening framing
- `[UD]` Karasawa & Steyger 2015, *Toxicol Lett* (Cisplatin nephro/ototoxicity) — toxicity-as-barrier framing

### §2 — Cisplatin chemistry and DNA damage

- `[UD]` Pabla & Dong 2008, *Kidney Int* — DNA-damage → p53/PUMA/BAX canonical reference
- `[UD]` Breglio 2017, *Nat Commun* — tissue retention (also §4)
- `[UD]` Yoshizawa 2007, *Oncol Rep* — ATP7B / OSCC efflux
- `[UD]` Kang 2009, *PNAS* — XPA/NER rhythmic regulation (also §5)
- `[UD]` Kang 2010, *PNAS* — XPA rhythm × cisplatin
- `[UD]` Yang 2018, *PNAS* — NER chronopharmacology
- `[CS-01]` Li 2011 — XPA-mediated regulation of global NER (mechanism deepening)
- `[CS-01]` Pieck 2008 — oxaliplatin DNA adduct formation in WBC (adduct-detection methodology)
- `[GAP]` Jamieson & Lippard 1999, *Chem Rev* (PMID 11749487) — 1,2-d(GpG) intrastrand crosslink chemistry foundational ref **(user to download — paywall ACS)**
- `[GAP]` Burger 2011, *Drug Resist Updat* — CTR1 / OCT2 / ATP7 transporter overview (nice-to-have)

### §3 — OSCC/HNSCC treatment pathways

- `[UD]` Bernier (Cooper) 2005, *Head Neck* — pooled high-risk indications (ENE, +margin)
- `[UD]` Noronha 2018, *JCO* — weekly vs q3wk cisplatin (87% OSCC)
- `[UD]` Szturz 2017, *Oncologist* — weekly vs q3wk meta-analysis
- `[UD]` Kiyota 2022, *JCO* — JCOG1008 weekly postop non-inferiority
- `[CS-01]` Kuwahara 2009 — nedaplatin replacement in definitive CRT (alternative regimen)
- `[CS-01]` Homma 2013 — superselective intra-arterial cisplatin + RT (special route)
- `[CS-01]` Patil 2020 — chemoradiation in unresectable oral cavity cancer
- `[CS-01]` Banerjee 2022 — prospective concurrent CRT comparison
- `[GAP]` **Cooper 2004 NEJM** (RTOG 9501) — postop CRT pivotal trial **(MUST — user to download)**
- `[GAP]` **Bernier 2004 NEJM** (EORTC 22931) — postop CRT pivotal trial **(MUST)**
- `[GAP]` **Adelstein 2003 JCO** — definitive CRT for unresectable disease **(MUST)**
- `[GAP]` **Forastiere 2003 NEJM** (RTOG 91-11) — larynx preservation **(MUST)**
- `[GAP]` **Posner 2007 NEJM** (TAX 324) — TPF induction **(MUST)**
- `[GAP]` **Vermorken 2007 NEJM** (TAX 323) — TPF induction **(MUST)**
- `[GAP]` **Pignon 2009 Radiother Oncol** (MACH-NC) — meta-analysis gold standard **(MUST)**
- `[GAP]` Lacas 2021 PMC8386522 — MACH-NC update (open access; recommended)

### §4 — Organ-specific cisplatin toxicity

#### 4.1 Nephrotoxicity
- `[UD]` Pabla & Dong 2008 (cross-listed §2)
- `[UD]` Manohar & Leung 2018, *J Nephrol* — updated review with incidence
- `[UD]` Karasawa 2015 (cross-listed §1)
- `[CS-01]` Uehara 2011 — comparative cisplatin vs nedaplatin nephrotoxicity mechanism
- `[CS-01]` Kidera 2014 — clinical risk factors (Japanese cohort)
- `[CS-01]` Ali 2021 — platinum compound molecular toxicity review
- `[CS-01]` Tolouian 2022 — antioxidants and cisplatin nephrotoxicity update
- `[CS-01]` Watanabe 2003 — continuous GSH depletion model (mechanism)

#### 4.2 Ototoxicity
- `[UD]` Breglio 2017 (cross-listed §2)
- `[UD]` Karasawa 2015 (cross-listed §1/§4.1)
- `[CS-01]` Araújo 2019 — melatonin protective against cisplatin ototoxicity (cross-listed §6)
- `[GAP]` Brock 2018 NEJM SIOPEL 6 — sodium thiosulfate otoprotection **(nice-to-have)**

#### 4.3 Mucositis
- `[UD]` Sonis 2004, *Nat Rev Cancer* — 5-phase mucositis model
- `[UD]` Lalla 2014, *Cancer* — MASCC/ISOO guideline
- `[CS-01]` Nicolatou-Galitis 2010 — oral mucositis / pain / xerostomia in HNC
- `[CS-01]` El-Kady 2025 — melatonin oral gel for oral mucositis (cross-listed §6)

#### 4.4 Nausea / vomiting
- `[UD]` Basch 2011, *JCO* — ASCO antiemetic guideline (older)
- `[CS-01]` Aapro 2016 — NEPA fixed netupitant/palonosetron (modernises Basch)
- `[CS-01]` Schwartzberg 2019 — NEPA oral formulation
- `[GAP]` Herrstedt 2023 ESMO Open — 2023 MASCC/ESMO antiemetic update **(nice-to-have)**

#### 4.5 Peripheral neuropathy
- `[UD]` Park 2013, *CA Cancer J Clin* — mechanism + clinical review
- `[CS-01]` Seto 2016 — dosing-time × cisplatin-induced peripheral neuropathy ★ (cross-listed §6)

### §5 — Circadian timing gates

- `[UD]` Sancar 2015, *Biochemistry* — framework (XPA, CRY-p73, NF-κB)
- `[UD]` Sancar & Van Gelder 2021, *Science* — balanced contemporary perspective
- `[UD]` Kang 2009 / Kang 2010 / Yang 2018 (cross-listed §2) — XPA-NER core papers
- `[UD]` Oda 2014, *Mol Pharmacol* — OCT2 renal circadian oscillation (linchpin)
- `[UD]` Zha 2020, *Cell Death Dis* — BMAL1 paradox in renal injury
- `[UD]` Peng 2019, *J Exp Clin Cancer Res* — ARNTL hypermethylation × cisplatin resistance (NPC)
- `[UD]` Li 2022, *Med Oncol* — ARNTL/BMAL1 OSCC tumor-suppressor
- `[UD]` Li 1997, *Toxicol Appl Pharmacol* — GSH/redox rhythm (foundational)
- `[UD]` Lee & Sancar 2011a, *PNAS* — CRY/p73 axis
- `[UD]` Lee & Sancar 2011b, *PNAS* — clock-controlled NF-κB / apoptosis
- `[UD]` Bjarnason 2001, *Am J Pathol* — first human oral mucosa clock-gene rhythms
- `[UD]` Gu 2021, *J Circadian Rhythms* — diurnal therapy-response genes oral mucosa
- `[UD]` Yang 2021, *J Biol Chem* — clock × carcinogenesis background
- `[CS-01]` Sassa 2010 — circadian oscillation of multidrug resistance gene (transporter rhythm)
- `[CS-01]` Okyar 2011 — strain- and sex-dependent circadian changes in Abcc2 (sex stratification mechanism)
- `[CS-01]` Okabe 2014 — HIF1 impact on Per2 circadian (hypoxia-clock interaction)
- `[CS-01]` Nakagawa 2008 — circadian modulation of DNA synthesis
- `[CS-01]` Rana 2010 — circadian rhythm and malignancy review
- `[CS-01]` Kramer 2022 — foundations of circadian medicine (modern framework)

### §6 — Chronotherapy clinical / preclinical evidence

- `[UD]` Tsuchiya 2018, *Chronobiol Int* — OSCC-specific cisplatin chronotherapy ★ KEY
- `[UD]` Zhang 2018, *Chronobiol Int* — NPC chronotherapy phase II RCT ★ KEY
- `[UD]` Printezi 2022, *Lancet Oncol* — chronomodulated systematic review
- `[UD]` Abusamak 2025, *Int J Cancer* — HNC chronotherapy systematic review (most recent)
- `[UD]` Marcu 2024, *Expert Rev Anticancer Ther* — RCT design considerations (cross-listed §7)
- `[UD]` Giacchetti 2006, *JCO* — chronomodulated FOLFOX (counter-evidence; sex-specific harm)
- `[UD]` Innominato 2020, *Cancer Med* — sex-dependent irinotecan chronotherapy
- `[UD]` Koritala 2022, *Toxicol Appl Pharmacol* — preclinical cisplatin chronotherapy (mammary)
- `[UD]` Lévi 1997, *Lancet* — historical foundational chronotherapy CRC
- `[UD]` Mormont & Lévi 2003, *Cancer* — principles primer (cross-listed §5)
- `[CS-01]` Seto 2016 — dosing-time × cisplatin peripheral neurotoxicity ★ (cross-listed §4.5)
- `[CS-01]` Hooven 2009 — "Does the clock make the poison?" conceptual paper
- `[CS-01]` Zema 2018 — melatonin synergises cisplatin chemotherapeutic effect
- `[CS-01]` Araújo 2019 — melatonin protection from cisplatin ototoxicity (cross-listed §4.2)
- `[CS-01]` Zhuo 2022 — melatonin protection from cisplatin cardiotoxicity
- `[CS-01]` El-Kady 2025 — melatonin oral gel for cisplatin oral mucositis (cross-listed §4.3)
- `[CS-01]` Damato 2021 — temozolomide chronotherapy retrospective in glioblastoma (concept extension)

### §7 — Trial design and circadian monitoring

- `[UD]` Cash 2018, *Psychooncology* — HNSCC actigraphy × OS ★ KEY
- `[UD]` Roenneberg 2003, *J Biol Rhythms* — MCTQ chronotype tool
- `[UD]` Innominato 2014, *Ann Med* — circadian timing system framework
- `[UD]` Innominato 2012, *Int J Cancer* — actigraphy during chemo (CRC validation)
- `[UD]` Mormont 2000, *Clin Cancer Res* — rest-activity prognostic anchor
- `[UD]` Ortiz-Tudela 2016, *BMC Cancer* — circadian robustness measurement
- `[UD]` Lévi 2020, *Cancers* — wearable / tele-monitoring feasibility
- `[UD]` Amidi & Wu 2022, *Front Oncol* — disruption-symptom link
- `[UD]` Marcu 2024 (cross-listed §6)
- `[CS-01]` Liu 2025 — continuous temperature data from wearable devices

---

## 4. Inaccessible / not-yet-obtained papers (residual gaps)

These are the priority items that neither `user_download/` nor `codex_survey/` provides; manuscript credibility depends on closing or substituting.

| Tier | Citation | Why required | Substitute possible? |
|---|---|---|---|
| Tier 1 (MUST for §3) | Cooper 2004 NEJM (RTOG 9501) | Postop CRT pivotal trial | No — must cite |
| Tier 1 | Bernier 2004 NEJM (EORTC 22931) | Postop CRT pivotal trial | No — must cite |
| Tier 1 | Adelstein 2003 JCO | Definitive CRT standard | No — must cite |
| Tier 1 | Forastiere 2003 NEJM (RTOG 91-11) | Larynx preservation | No — must cite |
| Tier 1 | Posner 2007 NEJM (TAX 324) | TPF induction | No — must cite |
| Tier 1 | Vermorken 2007 NEJM (TAX 323) | TPF induction | No — must cite |
| Tier 1 | Pignon 2009 Radiother Oncol (MACH-NC) | Meta-analysis gold standard | Partial via Lacas 2021 update only |
| Tier 2 (HIGH for §2) | Jamieson & Lippard 1999 Chem Rev | Adduct chemistry foundational | Partial via Pieck 2008 |
| Tier 2 (NICE for §4.2) | Brock 2018 NEJM (SIOPEL 6) | Sodium thiosulfate otoprotection | None — would have to drop §4.2 prevention paragraph |
| Tier 2 (NICE for §4.4) | Herrstedt 2023 ESMO Open | 2023 MASCC/ESMO antiemetic update | Partial via Aapro 2016 NEPA |
| Tier 3 (REF-ONLY) | Kimura 2018 / Yamamoto 2022 (Mg preloading); McDonald 2005 DRG; recent wearable ML reviews | Enrichment only | Substitutable |

**Recommendation:** Tier 1 are non-negotiable. Tier 2 strongly recommended. Tier 3 optional.

---

## 5. Residual evidence gaps (conceptual, not paper-count)

Even with codex_survey added, the manuscript draft must explicitly acknowledge these conceptual gaps in conclusions/limitations:

1. **No OSCC-tumor XPA rhythm proof.** Bjarnason 2001 and Gu 2021 cover normal oral mucosa; OSCC tumor circadian repair rhythm remains unproven.
2. **No HNSCC cisplatin chronotherapy RCT.** Tsuchiya 2018 and Zhang 2018 are the closest; Abusamak 2025 systematic review confirms scarcity.
3. **Sex stratification under-tested in HNSCC chronotherapy.** Giacchetti 2006 + Innominato 2020 (CRC) flag the issue; HNSCC-specific sex × time data absent.
4. **Wearable circadian phase estimation lacks HNSCC validation.** Lévi 2020 and Cash 2018 are partial; no HNSCC-specific DLMO / temperature / actigraphy validation cohort.
5. **OCT2 transporter rhythm direct human proof.** Oda 2014 is rodent; human OCT2 / SLC22A2 oscillation in renal cortex is inferred, not measured.

---

## 6. Quality flags

- All `user_download/` PDFs are from established journals (NEJM, JCO, PNAS, Nat Commun, Nat Rev Cancer, Lancet Oncol, Chronobiol Int, etc.).
- High-value codex_survey selections (Seto 2016, Sassa 2010, Okyar 2011, Okabe 2014, Uehara 2011, Kidera 2014, Aapro 2016, Kramer 2022) are from reputable specialist journals (*J Pharm Sci*, *Chronobiol Int*, *Cell Death Differ*, *Eur J Cancer*, *Cancer Sci*, *Cell Metab*, etc.). None are mega- or predatory-journal red flags.
- ≈70% of codex_survey contents are off-topic (broad oncology supportive care, antiemetic phase-II trials in non-HNSCC sites, herbal cisplatin protectants). These are NOT promoted to reference list to keep total within 80–110 cap and to maintain *Oral Oncology* reviewer credibility.

---

## 7. Hand-off to Stage 2 (academic-paper planning)

This inventory is the evidence substrate for the manuscript writing sequence per `prompt.md`:
mechanism (§2) → toxicity (§4) → clinical (§3) → circadian (§5) → evidence (§6) → future direction (§7) → intro/conclusion (§1/§8).

The Stage 2 planning agent should:
1. Confirm Tier-1 Section 3 gap with the user before drafting §3 (the section depends on these citations).
2. Use the per-section reference clusters above to anchor each chapter outline.
3. Carry the "residual conceptual gaps" (§5 above) into the Discussion / Limitations subsection.
4. Respect the 80–110 reference cap when integrating codex_survey supplements.
