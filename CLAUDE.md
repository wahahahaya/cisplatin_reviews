# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Identity

This is an academic manuscript project, not a software project. The goal is a focused review article for **Oral Oncology** titled:

> *Cisplatin Timing in Oral and Head-and-Neck Cancer: Organ-Specific Toxicity Mechanisms, Clinical Delivery Constraints, and the Rationale for Chronotherapy*

The central thesis: cisplatin toxicity is organ-specific, pathway-specific, and potentially time-dependent — making chronotype-aware scheduling a testable toxicity-sparing strategy.

## Directory Structure

```
/Users/arlen/Desktop/oral_review/
├── prompt.md              — Full manuscript blueprint (READ FIRST on every session)
├── preprompt.md           — Folder conventions and workflow rules
├── info/
│   ├── need.md            — Papers requiring user download (prioritized list)
│   └── user_download/     — PDFs provided by user; read these before any literature search
├── reference/
│   └── reference.md       — Literature inventory, inaccessible papers, evidence gaps
├── figure/
│   └── figure.md          — Image-generation prompts for Figures 1 and 2
├── full_paper/            — LaTeX manuscript output
└── log/                   — Step-by-step pipeline logs
```

Create any missing folders before writing to them.

## Mandatory First Step Each Session

1. Read `prompt.md` for the full manuscript blueprint.
2. Check `info/need.md` to know what papers the user has or needs.
3. Read all PDFs available in `info/user_download/` before doing any broad literature search.
4. Review `reference/reference.md` for the current evidence inventory and gaps.

## Literature Workflow

**User-curated literature first.** Do not run broad literature searches for areas already covered by PDFs in `info/user_download/`. Perform targeted searches only to fill weak, missing, outdated, or low-quality evidence areas.

After any literature work, update `reference/reference.md` with:
- Papers reviewed, usable count, inaccessible count
- References grouped by manuscript section
- Evidence gaps
- Papers the user must download (title, authors, year, DOI/PMID, reason)

Avoid mega journals (Scientific Reports, PLOS ONE) and predatory journals.

## Manuscript Targets

| Component | Target |
|---|---:|
| Main text | 4,500–5,000 words |
| References | 80–110 |
| Figures | 2 |
| Tables | 3 |
| Abstract | 180–220 words |

## Claims Calibration

**Safe to claim:** cisplatin remains important in OSCC/HNSCC; toxicities are organ-specific and mechanistically explainable; XPA/NER provides a plausible circadian–DNA-repair link; OCT2 is relevant to nephro/ototoxicity; existing chronotherapy evidence is hypothesis-generating; toxicity reduction is a more defensible endpoint than survival benefit.

**Do not claim:** evening cisplatin is universally optimal; chronotherapy is ready for clinical use; chronotherapy improves survival in OSCC/HNSCC; OSCC tumor XPA rhythm is already proven; country-specific practice can be generalized without supporting evidence.

## Output Conventions

- **Manuscript:** LaTeX format in `full_paper/`
- **Figures:** image-generation prompts (not rendered images) in `figure/figure.md`
- **Logs:** record every step — files created/modified, literature reviewed, inaccessible papers, current status, next step — in `log/`
- **Language:** user-facing dialogue in Traditional Chinese (zh-TW); all paper content in English
