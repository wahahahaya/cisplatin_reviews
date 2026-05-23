# Pipeline Initialization Log

**Date:** 2026-05-23
**Pipeline:** academic-pipeline v3.7.0 (ARS Full)
**Project:** Cisplatin Chronotherapy in OSCC/HNSCC — Targeted Mini-Review for *Oral Oncology*
**User Email:** a870128rlen@gmail.com

---

## Source materials

- `prompt.md` — Manuscript Blueprint (read, 1299 lines). Provides:
  - Working title, target journal (*Oral Oncology*), article type (Review/targeted mini-review)
  - Mechanical limits: ≤5,000 words / ≤7 figures+tables / ≤120 refs
  - Practical target: 4,500–5,000 words, 80–110 refs, 2 figures, 3 tables, abstract 180–220 words
  - Central thesis + core argument (6-step logic)
  - Full 8-section structure with target word counts per section
  - 3 pre-specified tables (organ toxicity, circadian nodes, chronotherapy evidence)
  - 2 figure blueprints (mechanism+organ map; chronotype-aware framework)
  - Data collection plan: 5 literature buckets with search concepts and extraction items
  - Claims calibration (safe vs. avoid)
  - Presubmission inquiry text
  - Writing sequence and final word budget

## Directory structure created

```
/Users/arlen/Desktop/oral_review/
├── prompt.md              (source blueprint)
├── reference/             (literature search outputs; reference.md for inaccessible papers)
├── info/                  (user-uploaded full-text PDFs/notes)
├── figure/                (figure.md with prompts for image-gen AI)
├── full_paper/            (LaTeX manuscript output)
└── log/                   (this directory — pipeline run logs)
```

## Pipeline stages planned

1. RESEARCH (deep-research) — literature search across 5 buckets
2. WRITE (academic-paper full mode) — LaTeX draft
3. INTEGRITY (pre-review) — references, citations, data, originality, claims, 7-mode failure checklist
4. REVIEW (5-reviewer panel) — full peer review
5. REVISE — incorporate reviewer roadmap
6. RE-REVIEW — verification of revisions
7. RE-REVISE — if needed
8. FINAL INTEGRITY — from-scratch verification, 100% pass required
9. FINALIZE — LaTeX → PDF via XeLaTeX
10. PROCESS SUMMARY — bilingual process record

## User-specified protocols

- Avoid mega journals (Scientific Reports, PLOS ONE, etc.) and predatory journals.
- For papers Claude cannot access, write title+authors+DOI to `reference/reference.md` so user can download manually.
- Generate image-gen prompts in `figure/figure.md` for figures requested.
- All paper output in LaTeX format under `full_paper/`.
- User will deposit reference PDFs in `info/` as they obtain them.
- Log every step's process and outcome to this `log/` directory.

## Language convention

- User-facing dialogue: Traditional Chinese (zh-TW)
- Paper content: English (target *Oral Oncology* is an English-language journal)
- Process record at Stage 6: bilingual
