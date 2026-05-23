# Stage 1 — RESEARCH (Launch)

**Date:** 2026-05-23
**Mode:** lit-review (user-confirmed)
**Strategy:** 5 parallel general-purpose subagents, one per literature bucket from prompt.md

## Subagent assignments

| Bucket | Topic | Search query budget | Output (bibliography) | Output (inaccessible) |
|---|---|---|---|---|
| 1 | OSCC/HNSCC cisplatin clinical use | 15–25 queries | `info/bucket1_clinical_use.md` | `reference/bucket1_inaccessible.md` |
| 2 | Cisplatin toxicity mechanisms (6 organs) | 20–30 queries | `info/bucket2_toxicity_mechanisms.md` | `reference/bucket2_inaccessible.md` |
| 3 | Circadian molecular nodes | 25–35 queries | `info/bucket3_circadian_nodes.md` | `reference/bucket3_inaccessible.md` |
| 4 | Chronotherapy clinical evidence (OSCC pilot + NPC RCT verification) | 15–25 queries | `info/bucket4_chronotherapy_evidence.md` | `reference/bucket4_inaccessible.md` |
| 5 | Chronotype assessment + trial design | 20–30 queries | `info/bucket5_monitoring_trial_design.md` | `reference/bucket5_inaccessible.md` |

## Quality directives passed to every agent

- Avoid mega journals (Scientific Reports, PLOS ONE, PeerJ, Heliyon, low-tier MDPI / Frontiers)
- Avoid predatory journals (Beall's list, OMICS, etc.); prefer MEDLINE/SCIE-indexed
- Prefer landmark journals: NEJM/JCO/Lancet Oncology/Oral Oncology/Head & Neck/Annals of Oncology/IJROBP/Kidney International/JASN/Hearing Research/PNAS/Cell/Nat Rev series/Chronobiology Int/J Pineal Res
- Do not fabricate citations; mark uncertain numbers with [verify]
- Extract specific data items per bucket (defined in prompt.md Data Collection Plan)

## Key verification targets

- Bucket 1: MACH-NC meta-analyses; Bernier 2004 EORTC 22931; Cooper 2004 RTOG 9501; Forastiere 2003 RTOG 91-11; Noronha 2018 JCO weekly vs 3-weekly
- Bucket 2: Manohar & Leung 2017 nephrotox review; Sonis 2004 NRC pathobiology of mucositis; MASCC/ISOO 2020 mucositis guidelines
- Bucket 3: Kang & Sancar 2009 PNAS (XPA oscillation); BMAL1 nephroprotection (Bonny/Nikkanen); ARNTL silencing NPC cisplatin resistance (Sun Yat-sen group)
- Bucket 4: OSCC crossover pilot (n=9, DCF, 19:30 evening); NPC phase II RCT (n=148, chronomodulated)
- Bucket 5: Mormont 2000 dichotomy I<O; Innominato actigraphy chronotherapy; Roenneberg MCTQ; Lewy DLMO

## Status

Launched in background (5 parallel agents). Awaiting completion notifications.
