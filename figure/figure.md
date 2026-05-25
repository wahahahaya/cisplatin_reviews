# Figure Generation Prompts
**Manuscript:** Cisplatin Timing in Oral and Head-and-Neck Cancer
**Journal:** Oral Oncology
**Stage:** 3 (manuscript complete) — figures ready for illustration
**Date:** 2026-05-25

---

## General style notes for both figures

- **Style:** Scientific diagram / schematic illustration — no photographs, no 3D rendering
- **Dimensions:** 180 mm wide (full column) × appropriate height; 300 dpi minimum for print
- **Color palette:** Restrained — use 3–4 colors consistently across panels:
  - Blue (#2C6FAC) for cisplatin/platinum species and molecular clock positive arm
  - Red/coral (#C0392B) for DNA damage, apoptosis, toxicity
  - Green (#27AE60) for repair, protection, clock-informed safe windows
  - Orange/amber (#E67E22) for circadian phase markers and timing annotations
  - Light grey (#F5F5F5) for backgrounds/compartments
- **Typography:** All labels in sans-serif (Helvetica/Arial equivalent), min 7 pt
- **Panel labels:** Bold uppercase letters — (A), (B), (C) — top-left corner of each panel
- **No decorative elements** — purely functional scientific schematic
- **Format:** Vector (SVG or AI) with fallback 300 dpi PNG; CMYK color space for print

---

## Figure 1 — Cisplatin mechanism of action, organ-specific toxicity, and circadian gates

**Manuscript reference:** Referenced in §2 and §4; cross-referenced from §5
**Label in LaTeX:** `\label{fig:mechanism}`
**Caption in manuscript:** "Cisplatin mechanism of action and organ-specific toxicity pathways."

### Panel layout

Three vertically stacked or side-by-side panels sharing a common left-to-right flow.

---

### Panel (A): Cisplatin cellular entry, DNA adduct formation, and NER/apoptosis decision

**Spatial organization:** Linear left-to-right flow within one cell cross-section

**Elements to include:**

1. **Cisplatin molecule** — square-planar Pt(II) with two Cl⁻ and two NH₃ ligands; label "Cisplatin"
2. **Aquation step** — arrow showing loss of Cl⁻ in cytoplasm, producing mono-aquo species; label "Aquation (low Cl⁻ cytoplasm)"
3. **Transporters (cell membrane)** — two membrane proteins:
   - CTR1/SLC31A1 (influx, left side) — label "CTR1 influx"
   - OCT2/SLC22A2 (also influx in renal proximal tubule context) — label "OCT2 influx"
   - ATP7B (efflux, right side) — label "ATP7B efflux"
4. **Nucleus** — oval compartment with double membrane
5. **DNA adduct** — within nucleus, show helix with platinum bridge at adjacent guanines; label "1,2-d(GpG) adduct (65–70% of adducts)"
6. **NER pathway fork** — from the adduct, two branches:
   - **Upper fork (repair):** XPA → RPA → TFIIH → dual incision → DNA polymerase gap-fill → ligation; label "NER repair (XPA-dependent)"
   - **Lower fork (apoptosis):** ATR → Chk1 → p53 → BAX/PUMA → Caspase 3/7; label "Apoptosis cascade"
7. **Clock annotation box** — dashed orange box overlaid on the XPA step: "XPA peaks ZT10, nadir ZT22 (5–10× amplitude)"
8. **Mitochondria** — small oval in cytoplasm receiving some platinum; label "Pt accumulation → ROS → mtDNA damage"

---

### Panel (B): Organ-specific toxicity pathways (4 tissue compartments)

**Spatial organization:** Four horizontal bands representing kidney, cochlea, oral mucosa, and DRG neurons

**Kidney band:**
- Proximal tubular cell schematic
- OCT2 on basolateral membrane (labeled) taking up cisplatin
- Mitochondria → ROS → caspase 2 activation → AKI
- Arrow: "40% of patients; OCT2 expression circadian (ZT14 peak)"
- Color: blue uptake arrow → red injury marker

**Cochlea band:**
- Simplified cochlear cross-section (oval window, stria vascularis, OHC row)
- Platinum retention in stria vascularis (highlighted in blue)
- Label: "Platinum retained months–years post-treatment (Breglio 2017)"
- OHC loss arrow labeled: "SNHL 40–80% adults; irreversible"
- Note: "STS otoprotection in paediatric trials (Brock 2018)"

**Oral mucosa band:**
- Stratified squamous epithelium cross-section (3–4 cell layers)
- S-phase cells in basal layer highlighted in red during "proliferative peak"
- NF-κB → IL-1β/TNF-α → ulceration cascade (simplified)
- Label: "Mucositis ~100% with concurrent CRT; proliferation rhythmic (Bjarnason 2001)"
- Clock annotation: "TS activity peak ~13:27 → maximal cisplatin vulnerability"

**DRG neuron band:**
- Large neuron cell body with no BBB barrier (annotated "no blood-nerve barrier")
- Platinum accumulation → oxidative stress → axonal length markers
- Label: "Sensory neuropathy >350 mg/m² cumulative; 'coasting' effect"

---

### Panel (C): Circadian clock gates — how clock time modulates injury risk

**Spatial organization:** 24-hour circular clock diagram with superimposed oscillating traces

**Elements to include:**

1. **Outer ring:** 24-hour clock face, labeled in 4-hour intervals (ZT0 = lights-on / subjective morning)
2. **Inner oscillating curves (5 traces, color-coded):**
   - Blue solid: **OCT2 protein level** — peaks ZT14, nadir ~ZT2; label "OCT2 (renal uptake)"
   - Blue dashed: **XPA protein level** — peaks ZT10, nadir ZT22; label "XPA (NER capacity)"
   - Orange: **GSH level** — trough during resting phase; label "Glutathione (redox buffer)"
   - Green: **Mucosal proliferation (TS activity)** — peak ~ZT5–6 (mid-subjective day); label "Mucosal S-phase"
   - Red: **BMAL1 mRNA** — peak early subjective night, trough early day; label "BMAL1 (core clock)"
3. **Shaded zone:** Amber/orange shaded sector at ZT6–10 labeled "HIGH TOXICITY WINDOW (OCT2 high + XPA low)"
4. **Shaded zone:** Green shaded sector at ZT14–20 labeled "LOWER TOXICITY WINDOW (OCT2 declining + XPA rising)"
5. **BMAL1 paradox annotation:** Small annotation box near the BMAL1 curve: "BMAL1: pro-injury in kidney; tumour-suppressive in OSCC; complex tissue specificity"
6. **Clock gene feedback loop** (small inset): CLOCK + BMAL1 → PER/CRY → HERC2-XPA degradation; 2-box feedback diagram

---

## Figure 2 — Chronotype-aware cisplatin scheduling: rationale and trial framework

**Manuscript reference:** Referenced in §7
**Label in LaTeX:** `\label{fig:framework}`
**Caption in manuscript:** "Proposed framework for chronotype-aware cisplatin chronotherapy in OSCC/HNSCC."

### Panel layout

Three panels arranged left to right or top row / bottom row.

---

### Panel (A): The chronotype problem — why fixed-clock dosing is inadequate

**Spatial organization:** Two-part panel

**Left half — Fixed clock-time dosing:**
- 24-hour clock showing a single fixed infusion time (e.g., 9:00 a.m. marked with a lightning bolt)
- Below: distribution of 10–12 patient icons with their individual midsleep points (represented as colored dots on a horizontal timeline)
- Early chronotypes (midsleep 01:00–02:00): green dots — fixed 9 a.m. dose falls in their low-toxicity window
- Late chronotypes (midsleep 03:30–05:00): red dots — fixed 9 a.m. dose falls in their high-toxicity window
- Label: "One fixed time: suboptimal for 40–50% of patients"

**Right half — Chronotype-adjusted dosing:**
- Same distribution of patient icons, now each with a personalized infusion time calculated from their midsleep
- All dots green
- Label: "Chronotype-adjusted: low-toxicity window for each patient"
- Note: "Assessed by Munich Chronotype Questionnaire + 7-day actigraphy"

---

### Panel (B): Personalised circadian phase estimation — tools and integration

**Spatial organization:** Three-column layout showing measurement tools and how they converge

**Column 1 — Patient input:**
- Icon: questionnaire (MCTQ)
- Icon: wrist actigraphy device
- Icon: skin temperature wearable
- Label: "Pre-treatment chronotype assessment (7-day run-in)"

**Column 2 — Circadian phase estimation:**
- Actigraphy trace (rest–activity rhythm with midpoint marked)
- Temperature trace (distal–proximal gradient, nocturnal peak)
- Clock gene expression curve (peripheral blood leukocytes, PER1 + BMAL1)
- Convergence arrow → "Individual midsleep midpoint (MSFsc)"

**Column 3 — Scheduled cisplatin delivery:**
- Formula box: "Infusion time = MSFsc − 7 hours"
- 24-hour clock showing individualized delivery time
- Example: "Early type: 8:00 a.m. | Intermediate: 12:30 p.m. | Late: 4:30 p.m."
- Annotation: "Targets low-OCT2 / high-XPA window for each patient"

---

### Panel (C): Proposed phase II trial schema

**Spatial organization:** CONSORT-style flow diagram (simplified, not full CONSORT)

**Flow elements (top to bottom):**

1. **Eligibility box:** "Stage III–IVA OSCC/HNSCC; concurrent cisplatin + RT planned; ECOG 0–1; eGFR ≥55"
2. **Run-in box:** "7-day actigraphy + MCTQ + temperature wearable → Circadian function index (CFI)"
3. **Stratification diamond:** "CFI intact vs disrupted | Sex | Cisplatin schedule (q3wk vs weekly) | Tumour site"
4. **Randomisation box:** "1:1 randomisation" with two arms branching:
   - **Arm A (Standard):** "Fixed institutional cisplatin time (SOC)"
   - **Arm B (Chronotype-adjusted):** "Cisplatin at MSFsc − 7 h"
5. **During treatment (both arms):** "Continuous actigraphy + temperature wearable | Serial urinary Pt | PBL clock genes"
6. **Primary endpoint box:** "Grade ≥3 mucositis OR Grade ≥3 nephrotoxicity (cycles 1–2)"
7. **Secondary endpoints box:** "Emesis | Ototoxicity | Neuropathy | Cumulative dose | RT interruptions | QoL"
8. **Exploratory box:** "BMAL1/PER2 IHC | Biomarker-timing correlation | CFI as moderator"
9. **Sample size note:** "80 per arm; 80% power; 25% absolute risk reduction; α = 0.10 one-sided"

**Color scheme:**
- Arm A (Standard): grey flow boxes
- Arm B (Chronotype-adjusted): green flow boxes
- Endpoints: blue boxes
- Stratification/randomisation: amber/orange

---

## Submission format

| Item | Requirement |
|---|---|
| Format | EPS or TIFF; 300 dpi minimum |
| Width | 180 mm (full page) or 85 mm (single column) |
| Color mode | CMYK (print) |
| Font embedding | All fonts embedded |
| File naming | `Figure1_mechanism.eps`, `Figure2_framework.eps` |
| Separate legend | Full figure legend in `main.tex` captions (already written as stubs) |

---

## Suggested software

- Adobe Illustrator (vector, preferred for final submission)
- BioRender (rapid draft; export to Illustrator for annotation polish)
- Python + matplotlib + schematic (for Panel C trial flow: use a library like `matplotlib.patches`)

---

*Prompts last updated: 2026-05-25. Coordinate with main.tex figure captions before final submission.*
