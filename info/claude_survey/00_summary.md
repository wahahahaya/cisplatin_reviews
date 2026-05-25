# Claude Literature Survey — Summary

**Project:** Cisplatin Chronotherapy in OSCC/HNSCC — *Oral Oncology* Review
**Date:** 2026-05-24
**Author:** Claude (preliminary survey, awaiting user_survey for consolidation)

---

## 1. What this folder contains

Three files documenting Claude's preliminary literature evaluation **before** writing the manuscript:

| File | Purpose |
|---|---|
| `00_summary.md` | This file — high-level coverage status and instructions for the user |
| `01_already_downloaded.md` | Annotated inventory of all 47 PDFs already in `info/user_download/`, grouped by manuscript section, with assessment of relevance and intended use |
| `02_recommended_new_papers.md` | Additional candidate papers identified via targeted PubMed/web searches, split by priority (High/Medium/Low) and download necessity (Must-have / Nice-to-have / Reference-only) |

---

## 2. Critical reminder — NO downloads by Claude

Per user instruction: Claude has **not downloaded any papers**. All recommendations in `02_recommended_new_papers.md` are evaluations only. The user will decide which to download and place into `info/user_download/`.

---

## 3. Coverage status at a glance

| Manuscript section | Current PDFs | Coverage status | Need additions? |
|---|---:|---|---|
| §1 Introduction | 2 | Sufficient | No |
| §2 Cisplatin chemistry / DNA damage | 6 | **Partial** | Yes — 2 to 3 mechanistic anchors |
| §3 OSCC/HNSCC clinical pathways | 4 | **Insufficient** | Yes — 6 to 8 landmark trials |
| §4 Organ-specific toxicity | 8 | Sufficient | Optional — 2 to 3 prevention papers |
| §5 Circadian timing gates | 13 | Excellent | No |
| §6 Chronotherapy clinical/preclinical evidence | 10 | Excellent | No |
| §7 Trial design / circadian monitoring | 9 | Sufficient | Optional — 1 to 2 newer wearable papers |

**Headline finding:** Sections 5, 6, 7 (the chronotherapy and circadian half of the manuscript) are exceptionally well-covered by the 47 PDFs already downloaded. The gap is concentrated in **Section 3** (clinical landmark trials for OSCC/HNSCC treatment pathways) and modest in **Section 2** (foundational mechanism reviews).

---

## 4. Why Section 3 is the biggest gap

`prompt.md` Section 3 needs to explain where cisplatin enters OSCC/HNSCC treatment pathways: definitive CRT, postoperative high-risk CRT, induction TPF, larynx preservation, weekly vs 3-weekly dosing. The current PDFs cover the weekly-vs-3-weekly axis well (Noronha 2018, Szturz 2017, Kiyota 2022) and risk stratification (Bernier 2005), but do not yet include the **landmark phase III trials** that define standard of care and must be cited:

- Cooper 2004 (RTOG 9501) — postoperative CRT
- Bernier 2004 (EORTC 22931) — postoperative CRT
- Adelstein 2003 — definitive CRT for unresectable disease
- Forastiere 2003 (RTOG 91-11) — larynx preservation
- Posner 2007 (TAX 324) — TPF induction
- Vermorken 2007 (TAX 323) — TPF induction
- Pignon 2009 (MACH-NC update) — meta-analysis

These are foundational citations for any HNSCC review and are essential for credibility with *Oral Oncology* reviewers.

---

## 5. Next steps (per user's plan)

1. **User reviews** `02_recommended_new_papers.md` and decides which to download.
2. **User performs parallel survey** (the user mentioned doing their own search) and deposits findings in `info/user_survey/` (folder to be created by the user).
3. **Claude consolidates** `claude_survey/` + `user_survey/` + final PDF inventory into the master `reference/reference.md` evidence inventory.
4. **Claude begins manuscript writing** in `full_paper/` per the `prompt.md` writing sequence (mechanism → toxicity → clinical → circadian → evidence → future direction → intro/conclusion).

---

## 6. Quality flags

Following the user's preprompt rule to avoid mega journals and predatory journals:
- All 47 currently-downloaded papers are from established, high-quality journals (NEJM, JCO, PNAS, Cancer, Nat Rev Cancer, Lancet Oncol, Chronobiol Int, Mol Pharmacol, Cell Death Dis, etc.).
- All new candidates proposed in `02_recommended_new_papers.md` are from comparable-quality outlets (NEJM, JCO, Chem Rev, ESMO Open, Kidney Int, J Clin Oncol).
- No mega journals (Scientific Reports, PLOS ONE, Heliyon, etc.) are recommended.
