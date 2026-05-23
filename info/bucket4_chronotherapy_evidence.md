# Bucket 4: Cisplatin Chronotherapy Evidence — Annotated Bibliography
*Generated: 2026-05-23 | Agent: Bucket 4 subagent (compiled by orchestrator from agent report)*

---

## ⚠️ Verification Status of Key Studies (from prompt.md)

### OSCC Crossover Pilot — STATUS: **CONFIRMED** ✓

**Citation:**
Tsuchiya Y, Ushijima K, Noguchi T, et al. (2018). Influence of a dosing-time on toxicities induced by docetaxel, cisplatin and 5-fluorouracil in patients with oral squamous cell carcinoma; a cross-over pilot study. *Chronobiology International*, 35(2), 289–294. https://doi.org/10.1080/07420528.2017.1392551. PMID: 29144178.

**Extraction:**
- Study type: Clinical crossover pilot
- Cancer type: OSCC (oral squamous cell carcinoma)
- Sample size: n ≈ 9 [verify — not stated in abstract, requires full text]
- Timing intervention: Morning (10:30) vs evening (18:30) cisplatin — **NOTE: prompt.md states 19:30; agent found 18:30 in abstract; full-text verification needed**
- Regimen: DCF (docetaxel, cisplatin, 5-fluorouracil) induction chemotherapy
- Main finding: Grades of nausea, vomiting, and neutropenia were all lower with evening (18:30) than morning (10:30) dosing
- Limitation: Very small sample; abstract-only access; no efficacy endpoint; single-center
- Relevance: Only published OSCC clinical chronotherapy study; directly relevant; hypothesis-generating

---

### NPC Phase II RCT — STATUS: **CONFIRMED** ✓

**Citation:**
Zhang PX, Jin F, Li ZL, et al. (2018). A randomized phase II trial of induction chemotherapy followed by cisplatin chronotherapy versus constant rate delivery combined with radiotherapy. *Chronobiology International*, 35(2), 240–248. https://doi.org/10.1080/07420528.2017.1397684. PMID: 29215933.

**Extraction:**
- Study type: Randomized phase II clinical trial
- Cancer type: Locoregionally advanced NPC (nasopharyngeal carcinoma)
- Sample size: n = 148
- Timing intervention: Chronomodulated cisplatin (peak delivery 16:00) vs flat constant-rate infusion
- Regimen: Induction cisplatin + radiotherapy
- Main findings:
  - Nausea: 66.7% (chrono) vs 79.5% (control), p < 0.05
  - Vomiting: 47.9% vs 71.2%, p < 0.05
  - Oral mucositis: 73.9% vs 87.7%, p < 0.05
- Survival: No difference in 2-year OS, PFS, or DMFS
- Limitation: NPC ≠ OSCC (different EBV-related biology, different radiation field); underpowered for survival; single timing approach (does not adjust for individual chronotype); no circadian biomonitoring
- Relevance: Largest clinical RCT of cisplatin chronotherapy in any HN cancer; supports mucositis and GI toxicity as primary endpoints; cannot be directly extrapolated to OSCC

---

## Preclinical: XPA/NER Circadian Foundation

### Kang/Sancar et al. 2010 (PNAS)
- PMID: 20304803
- Key mechanistic foundation: XPA circadian regulation by cryptochrome controls cisplatin-DNA adduct repair
- Must-cite for Section 5 of the manuscript (circadian molecular nodes)
- [Full extraction to be added once full text confirmed — see bucket3_circadian_nodes.md]

---

## Preclinical: Cisplatin Time-of-Day Mouse Studies

*[Full bibliography pending full-text access — agent identified ~18 papers total including preclinical cisplatin ZT toxicity studies, clock-disruption jet-lag models, and rest-activity cohort studies. Full bibliography available once papers obtained via info/ folder.]*

Key landmark to confirm:
- Lévi FA group: early cisplatin chronoFLO mouse models
- Tox Appl Pharmacol: jet-lag abolishes cisplatin chronotherapy benefit

---

## Key Counter-Evidence

### EORTC Phase III Colorectal RCT (Lévi et al.)
- n = 564, colorectal cancer, large randomized trial
- Finding: No overall OS benefit from chronomodulated chemotherapy
- CRITICAL: Adverse sex-specific effect in women (chronoFLO reduced survival in women)
- Limitation: Not cisplatin-specific; not HNSCC; methodology of chronomodulation differs from targeted cisplatin timing
- Relevance: **This must be cited as major counter-evidence in Section 6** — the review must honestly acknowledge it

---

## Summary of Evidence Strength

| Evidence tier | Available? | Strength | Key limitation |
|---|---|---|---|
| OSCC clinical trial | YES (n≈9, pilot) | Very weak | Tiny sample, abstract only |
| NPC phase II RCT | YES (n=148) | Modest | NPC ≠ OSCC; no survival benefit |
| Other HN RCT | NOT FOUND | — | Gap |
| Preclinical mechanistic | YES (mouse ZT models, XPA/NER) | Moderate | Non-HNSCC models |
| Clock-disruption preclinical | YES | Moderate | Preclinical only |
| HNSCC circadian biomarker data | MINIMAL/NONE | Gap | Must state as honest gap |

---

## Inaccessible / Needs Full Text

*(Consolidated with `reference/bucket4_inaccessible.md`)*

| # | Title / Description | Authors | Year | Journal | DOI/PMID | Priority |
|---|---|---|---|---|---|---|
| 1 | OSCC crossover pilot (full text needed to confirm n, exact hours, quantitative toxicity grades) | Tsuchiya Y et al. | 2018 | Chronobiol Int | 10.1080/07420528.2017.1392551 / PMID 29144178 | HIGH |
| 2 | NPC RCT (full text needed for complete efficacy data table) | Zhang PX et al. | 2018 | Chronobiol Int | 10.1080/07420528.2017.1397684 / PMID 29215933 | HIGH |
| 3 | EORTC phase III colorectal chronomodulated chemotherapy | Lévi FA et al. | 2011 | Lancet Oncol | [verify DOI] | HIGH (counter-evidence) |
