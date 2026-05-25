# Session State — Oral Review Project

**Last saved:** 2026-05-25
**Phase:** Stage 1 (evidence gathering) ✅ CLOSED → Stage 2 (academic-paper planning) ⏵ ENTERING

---

## What has been completed

### Step 1 — Setup ✅ (2026-05-24)
- `CLAUDE.md` created
- `info/need.md` moved to `info/user_download/need.md`

### Step 2 — PDF Inventory ✅ (2026-05-24)
- 47 curated PDFs in `info/user_download/`

### Step 3 — Coverage Assessment ✅ (2026-05-24)
- Section 3 (clinical pathways) identified as biggest gap
- Sections 5 & 6 (circadian / chronotherapy) excellent

### Step 4 — Targeted Literature Searches ✅ (2026-05-24)
- 12 search topics covered

### Step 5 — claude_survey/ created ✅ (2026-05-24)
- `00_summary.md`, `01_already_downloaded.md`, `02_recommended_new_papers.md`

### Step 6 — codex_survey/ integration ✅ (2026-05-25)
- User-delivered: ≈748 PDFs across `01_usable_for_study_broad/` and `03_manual_screen_title_abstract/`
- Screened at title-level; 25 high-value unique papers identified
- Consolidated into `reference/reference.md`
- Logged in `log/stage1_consolidation_2026-05-25.md`

### Step 7 — Master reference inventory ✅ (2026-05-25)
- `reference/reference.md` built; sections, sources, gaps, conceptual limitations documented
- Directories `reference/`, `log/`, `full_paper/`, `figure/` created

---

## Current state: Stage 2 ENTERING ⏵

Stage 2 = **academic-paper `plan` mode** (Socratic chapter-by-chapter outline). The ars-pipeline next invokes `ars-plan`.

---

## Persistent gaps awaiting user action (do NOT block Stage 2 planning)

Tier 1 (MUST for §3 — landmark phase-III trials, none yet obtained):
- Cooper 2004 NEJM (RTOG 9501) — PMID 15128893
- Bernier 2004 NEJM (EORTC 22931) — PMID 15128894
- Adelstein 2003 JCO — PMID 12506176
- Forastiere 2003 NEJM (RTOG 91-11) — PMID 14645636
- Posner 2007 NEJM (TAX 324) — PMID 17960013
- Vermorken 2007 NEJM (TAX 323) — DOI 10.1056/NEJMoa071028
- Pignon 2009 Radiother Oncol (MACH-NC) — PMID 19446902

Tier 2 (HIGH/NICE):
- Jamieson & Lippard 1999 Chem Rev — PMID 11749487
- Brock 2018 NEJM SIOPEL 6 — PMID 29924955
- Herrstedt 2023 ESMO Open (partially substituted by codex_survey Aapro 2016 NEPA)

Strategy for Stage 2: planning agent may begin §1, §2, §4, §5, §6, §7 freely; for §3, draft outline with placeholder citations and ask user whether to (a) pause for downloads or (b) write text first and fill Section-3 citations during Stage 4 integrity check.

---

## Key files reference

| File | Purpose |
|---|---|
| `prompt.md` | MASTER blueprint — read first every session |
| `preprompt.md` | Folder conventions |
| `CLAUDE.md` | Claude Code guidance |
| `reference/reference.md` | Consolidated evidence inventory (BUILT 2026-05-25) |
| `log/stage1_consolidation_2026-05-25.md` | Stage 1 closure log |
| `info/user_download/` | 47 curated PDFs + need.md |
| `info/claude_survey/` | Claude's preliminary survey (3 files) |
| `info/codex_survey/` | Broad survey, ≈748 PDFs (mostly archived; 25 promoted to reference inventory) |
| `full_paper/` | LaTeX manuscript (Stage 3 output) |
| `figure/` | Image-generation prompts (Stage 3 output) |

---

## Next operator action

Invoke `ars-plan` (academic-paper `plan` mode) to begin Socratic chapter-by-chapter outline.
First planning question proposed for the user: handling of §3 landmark trial gap (download now vs draft now + fill at Stage 4 integrity check).
