# Bucket 3: Circadian Molecular Nodes — Annotated Bibliography
*Generated: 2026-05-23 | Agent: Bucket 3 subagent (compiled by orchestrator from agent report)*

---

## XPA / NER

### Kang T-H, Reardon JT, Kemp M, Sancar A. (2009). Circadian oscillation of nucleotide excision repair in mammalian brain. *PNAS*, 106(8), 2864–2867. DOI: 10.1073/pnas.0812638106. PMID: 19164551.
**Extraction:**
- Molecule: XPA; NER activity
- Tissue: Cerebral cortex (mouse brain)
- Model: Mouse; dual-incision NER activity assays at multiple circadian time points (ZTs)
- Circadian evidence: NER activity oscillates with a robust 24-h rhythm; peak in late afternoon/evening (~ZT12–14, ~5 pm in LD 12:12), nadir in early morning (~ZT0–2, ~5 am); driven by circadian oscillation of XPA mRNA and protein
- Cisplatin-specific: Partial — demonstrated with UV-CPD lesions; authors state rhythm applies to cisplatin adducts since NER is the sole repair pathway for both
- Key finding: Founding paper establishing that NER activity in mouse brain oscillates in a circadian manner, peaking in the afternoon and nadiring in early morning. Because all tissues examined except testis show the same rhythm, the finding generalises to cisplatin-treating organs including kidney, liver, and (by implication) oral/mucosal epithelia.
- Limitation: UV-CPD used as lesion substrate (not cisplatin adducts directly); no HNSCC data; mouse model only; brain tissue, though authors state rhythm is universal
- Relevance to review: Provides the foundational mechanistic basis for why cisplatin chronotherapy should work — the DNA-repair capacity removing cisplatin-DNA adducts is lowest in early morning and highest in the late afternoon. Underpins the rationale for afternoon/evening cisplatin dosing to spare normal tissues.

---

### Kang T-H, Lindsey-Boltz LA, Reardon JT, Sancar A. (2010). Circadian control of XPA and excision repair of cisplatin-DNA damage by cryptochrome and HERC2 ubiquitin ligase. *PNAS*, 107(11), 4890–4895. DOI: 10.1073/pnas.0915085107. PMID: 20304803.
**Extraction:**
- Molecule: XPA; CRY1/2; HERC2 ubiquitin ligase
- Tissue: Liver (primary); testis (negative control); kidney, skin, brain also confirmed
- Model: Mouse; dual-incision repair assay using cisplatin-DNA substrates; Cry1−/−Cry2−/− knockout mice
- Circadian evidence: XPA protein oscillates in liver: zenith ~ZT12 (~5 pm), nadir ~ZT0 (~5 am). Cisplatin-adduct removal in liver extracts mirrors this rhythm. Rhythm abolished in Cry1−/−Cry2−/− mice. Testis lacks XPA oscillation and shows constitutively high repair.
- Cisplatin-specific: Yes — Pt-GG intrastrand adducts directly measured
- Key finding: Definitive mechanistic paper. XPA oscillation is controlled at two levels: (1) transcriptional activation by CLOCK/BMAL1 via E-box in XPA promoter, suppressed by CRYs; (2) post-translational proteolysis via HERC2 E3 ubiquitin ligase. At nadir, CRY proteins suppress XPA transcription AND HERC2 degrades residual XPA protein — dual suppression maximises vulnerability. Tissue-generality (brain, liver, kidney, skin — all except testis) confirms universal relevance.
- Limitation: Mechanistic work in mouse liver; no HNSCC or oral mucosa-specific data; no patient data
- Relevance to review: **Primary mechanistic citation for the XPA-circadian-cisplatin nexus.** Essential for Sections 2 and 5.

---

### Yang Y, Adebali O, Wu G, Selby CP, Chiou Y-Y, Rashid N, Hu J, Hogenesch JB, Sancar A. (2018). Cisplatin-DNA adduct repair of transcribed genes is controlled by two circadian programs in mouse tissues. *PNAS*, 115(21), E4777–E4785. DOI: 10.1073/pnas.1804493115. PMID: 29735688.
**Extraction:**
- Molecule: XPA/NER (genome-wide); transcription-coupled NER (TC-NER) vs. global genome NER (GG-NER)
- Tissue: Kidney and liver (mouse)
- Model: Mouse; ZT0/ZT8/ZT16 time points; XR-seq at single-nucleotide resolution; cisplatin in vivo
- Circadian evidence: Two distinct circadian programs: (1) GG-NER peaks at ZT0 (dawn); (2) TC-NER repair dictated by each gene's phase of transcription. Two-program model.
- Cisplatin-specific: Yes — cisplatin administered in vivo; XR-seq captures platinum adduct excision genome-wide
- Key finding: GG-NER and TC-NER sub-pathways are independently clock-regulated. Time-of-day effects on cisplatin-DNA adduct clearance differ depending on whether target sequence is bulk chromatin or actively transcribed circadian gene.
- Limitation: Mouse kidney and liver only; no HNSCC or oral mucosa; no tumour data
- Relevance to review: Most detailed mechanistic picture of clock-controlled cisplatin-adduct repair at genome-wide resolution. Supports dosing-time optimisation rationale.

---

### Sancar A, Lindsey-Boltz LA, Gaddameedhi S, Selby CP, Ye R, Chiou Y-Y, Kemp MG, Hu J, Lee JH, Ozturk N. (2015). Circadian clock, cancer, and chemotherapy. *Biochemistry*, 54(2), 110–123. DOI: 10.1021/bi5007354. PMID: 25302769.
**Extraction:**
- Molecule: XPA; CRY1/2; PER1/2; BMAL1/CLOCK; p53/p73; NF-κB (review scope)
- Tissue: Multiple (review)
- Model: Review article synthesising mouse and human data
- Key finding: Comprehensive Sancar-group review synthesising circadian control of NER (XPA), DNA damage checkpoints (CRY), and apoptosis (p73/NF-κB) as they relate to cancer and chemotherapy. Argues cisplatin chronotherapy is mechanistically justified but clinically underutilised.
- Limitation: Review; no new primary data; no HNSCC data; predates some recent clinical evidence
- Relevance to review: Best single Sancar-group overview for the molecular rationale section. Essential citation for framing Section 5.

---

### Sancar A, Van Gelder RN. (2021). Clocks, cancer, and chronochemotherapy. *Science*, 371(6524), eabb0738. DOI: 10.1126/science.abb0738. PMID: 33414192. [verify PMID]
**Extraction:**
- Key finding: High-visibility Science review critically evaluating chronochemotherapy clinical trials. Molecular evidence supporting time-of-day dosing is strong, but clinical trials have not shown improved outcomes — primarily because trials did not synchronise drug timing to individual patient circadian phase.
- Limitation: Review; HNSCC not addressed; sceptical of current clinical evidence without patient-level clock synchronisation
- Relevance to review: Essential for the "clinical delivery constraints and rationale" framing. Provides authoritative perspective on the translational gap.

---

## ERCC1–XPF

*(No standalone high-tier paper specifically addressing circadian oscillation of ERCC1–XPF independent of the broader NER rhythm was identified. ERCC1–XPF is discussed within Kang/Sancar papers as a mandatory 3′ endonuclease in every NER reaction, co-regulated temporally with XPA. Evidence gap — see inaccessible list.)*

---

## OCT2 / SLC22A2

### Oda M, Koyanagi S, Tsurudome Y, Kanemitsu T, Matsunaga N, Ohdo S. (2014). Renal circadian clock regulates the dosing-time dependency of cisplatin-induced nephrotoxicity in mice. *Molecular Pharmacology*, 85(5), 715–722. DOI: 10.1124/mol.113.090365. PMID: 24567546.
**Extraction:**
- Molecule: OCT2 (SLC22A2); PPARα; CLOCK/BMAL1 (regulatory)
- Tissue: Kidney (proximal tubule)
- Model: Mouse (ICR); in vivo cisplatin at multiple ZTs; Slc22a2 knockout; renal DNA-platinum adduct measurement; PPARα promoter-binding assays
- Circadian evidence: OCT2 (Slc22a2) mRNA and protein exhibit significant time-dependent oscillation in mouse kidney. CLOCK-PPARα-OCT2 axis drives rhythmic OCT2 protein levels.
- Cisplatin-specific: Yes — OCT2 mediates basolateral cisplatin uptake into proximal tubule cells
- Key finding: OCT2 oscillates in mouse kidney; peak OCT2 = maximal cisplatin uptake, maximal renal DNA adducts, maximal nephrotoxicity. CLOCK-PPARα-OCT2 axis is the molecular mechanism of dosing-time-dependent nephrotoxicity. Slc22a2 knockout abolishes time-of-day nephrotoxicity difference.
- Limitation: Mouse model only; no human kidney data; no HNSCC relevance; ZT values require translation to human circadian phase
- Relevance to review: **Provides the mechanistic transporter link for nephrotoxicity chronotherapy rationale.** Key citation for Section 4 (nephrotoxicity) and Section 5 (OCT2 node).

---

## CTR1 / SLC31A1

*(No paper meeting quality criteria was identified specifically addressing circadian oscillation of CTR1/SLC31A1. CTR1's role in cisplatin uptake is established but circadian regulation was not found in MEDLINE-tier literature at this search depth. Documented as evidence gap.)*

---

## BMAL1 / ARNTL

### Zha M, Tian T, Xu W, Liu S, Jia J, Wang L, Yan Q, Li N, Yu J, Huang L. (2020). The circadian clock gene Bmal1 facilitates cisplatin-induced renal injury and hepatization. *Cell Death & Disease*, 11(6), 479. DOI: 10.1038/s41419-020-2655-1. PMID: 32522976.
**Extraction:**
- Molecule: BMAL1 (ARNTL); E-box-driven transcription; apoptotic pathway
- Tissue: Kidney (in vivo mouse; in vitro human HK-2 proximal tubule cells)
- Model: Mouse cisplatin-treated in vivo; HK-2 human renal tubular cells; BMAL1 gain- and loss-of-function; RNA-seq
- Circadian evidence: BMAL1 is induced by cisplatin stimulation. Gain-of-function aggravates apoptosis; loss-of-function is protective.
- Cisplatin-specific: Yes — cisplatin-specific nephrotoxicity model
- Key finding: **Counter-intuitively, BMAL1 FACILITATES rather than protects against cisplatin-induced renal injury.** Cisplatin induces BMAL1 expression → BMAL1 drives injury-promoting gene expression → aggravates tubular apoptosis. BMAL1 knockdown reduces nephrotoxicity.
- Limitation: Cell Death & Disease (Nature Publishing Group — acceptable); no chronotherapy timing experiment; no HNSCC data; human data limited to HK-2 cell line
- Relevance to review: Documents the BMAL1 paradox — this is the kidney side of the tissue-context-specific BMAL1 effect. Must be reconciled with the NPC ARNTL data (opposite direction).

---

### Peng H, Zhang J, Zhang P-P, Chen L, Tang L-L, Yang X-J, He Q-M, Wen X, Sun Y, Liu N, Li Y-Q, Ma J. (2019). ARNTL hypermethylation promotes tumorigenesis and inhibits cisplatin sensitivity by activating CDK5 transcription in nasopharyngeal carcinoma. *Journal of Experimental & Clinical Cancer Research*, 38(1), 11. DOI: 10.1186/s13046-018-0997-7. PMID: 30621723.
**Extraction:**
- Molecule: ARNTL (BMAL1); CDK5; promoter CpG methylation
- Tissue: Nasopharyngeal carcinoma (NPC) — cell lines (CNE-1, CNE-2, SUNE-1, HNE-1, NPC-039, C666-1) and patient tumour specimens
- Model: Human NPC cell lines; NPC patient tumour vs. non-cancerous tissue; xenograft mouse model
- Circadian evidence: ARNTL is epigenetically silenced (promoter hypermethylation) in NPC. Restoration of ARNTL suppresses proliferation and sensitises NPC cells to cisplatin.
- Cisplatin-specific: Yes — cisplatin sensitivity directly measured
- Key finding: ARNTL/BMAL1 silencing by promoter methylation → CDK5 upregulation → cisplatin resistance + tumourigenesis. Restoring ARNTL sensitises NPC cells to cisplatin. Identifies ARNTL as both a therapeutic target and chemosensitivity biomarker in head-and-neck cancer.
- Limitation: NPC is distinct from OSCC (EBV-associated; different biology); all data cell-line and xenograft; no patient-level pharmacological outcome
- Relevance to review: **Closest available paper linking BMAL1/ARNTL directly to cisplatin resistance in a head-and-neck cancer.** Essential for Section 5 BMAL1 node discussion.

---

### Tang Q, Cheng B, Xie M, Chen Y, Zhao J, Zhou X, Chen L. (2017). Circadian clock gene Bmal1 inhibits tumorigenesis and increases paclitaxel sensitivity in tongue squamous cell carcinoma. *Cancer Research*, 77(2), 532–544. DOI: 10.1158/0008-5472.CAN-16-1322. PMID: 27821487.
**Extraction:**
- Molecule: BMAL1; paclitaxel sensitivity; proliferation/apoptosis
- Tissue: Tongue squamous cell carcinoma (TSCC) — human specimens, cell lines, mouse xenografts
- Cisplatin-specific: No — paclitaxel sensitivity, not cisplatin
- Key finding: BMAL1 acts as tumour suppressor in TSCC. Loss promotes tumourigenesis; restoration increases paclitaxel sensitivity.
- ⚠️ DATA INTEGRITY FLAG: An Editor's Note was published by *Cancer Research* (2025) citing concerns about image duplication in this paper. Findings should be treated as [verify] until correction/retraction status confirmed. **Do not rely on quantitative data. Consider omitting or citing only with explicit caveat.**
- Relevance to review: Provides (tongue) OSCC-specific BMAL1 evidence, but must not be cited without confirming integrity status.

---

### Li H, Li M, Chen K, Li Y, Yang Z, Zhou Z. (2022). The circadian clock gene ARNTL overexpression suppresses oral cancer progression by inducing apoptosis via activating autophagy. *Medical Oncology*, 39(12), 244. DOI: 10.1007/s12032-022-01832-7. PMID: 36180647.
**Extraction:**
- Molecule: ARNTL (BMAL1); autophagy; apoptosis
- Tissue: OSCC — HN6 human oral squamous carcinoma cell line
- Key finding: First paper showing ARNTL overexpression induces apoptosis via autophagy in oral cancer. Establishes ARNTL as tumour suppressor in OSCC, consistent with NPC finding.
- Limitation: Single cell line (HN6) only; Medical Oncology is lower-tier; no cisplatin data; no circadian oscillation
- Relevance to review: Most directly OSCC-specific ARNTL paper. Supports extrapolation from NPC ARNTL-cisplatin resistance finding to oral cavity cancer.

---

## PER / CRY

### Lee JH, Sancar A. (2011). Circadian clock disruption improves the efficacy of chemotherapy through p73-mediated apoptosis. *PNAS*, 108(26), 10668–10672. DOI: 10.1073/pnas.1106284108. PMID: 21628572.
**Extraction:**
- Molecule: CRY1/CRY2; p73; oxaliplatin (platinum class)
- Key finding: CRY mutation in p53-null cancer cells upregulates p73 → sensitises to apoptosis from platinum compounds. CRY proteins normally suppress p73; removing CRY allows p73 to drive apoptosis in response to platinum adducts.
- Relevance: Key for CRY/p53/p73 apoptosis node. Highly relevant to cisplatin resistance in TP53-mutant HNSCC.

---

### Lee JH, Sancar A. (2011). Regulation of apoptosis by the circadian clock through NF-κB signaling. *PNAS*, 108(29), 12036–12041. DOI: 10.1073/pnas.1108125108. PMID: 21690409.
**Extraction:**
- Molecule: CRY1; BMAL1; NF-κB; extrinsic apoptosis pathway
- Key finding: CRY1 competes with NF-κB for BMAL1 binding; when CRY is high, NF-κB anti-apoptotic signalling is suppressed. Circadian clock gates extrinsic apoptosis via NF-κB.
- Relevance: NF-κB drives inflammatory cytokines in mucosal epithelia; its circadian gating by CRY means inflammatory amplification of cisplatin mucosal injury is clock-regulated.

---

### Liu H, Gong X, Yang K. (2020). Overexpression of the clock gene Per2 suppresses oral squamous cell carcinoma progression by activating autophagy via the PI3K/AKT/mTOR pathway. *Journal of Cancer*, 11(12), 3655–3664. DOI: 10.7150/jca.42771. PMCID: PMC7150464.
**Extraction:**
- Molecule: PER2; PI3K/AKT/mTOR; autophagy
- Tissue: OSCC — SCC-9, CAL27 cell lines; mouse xenograft
- Cisplatin-specific: No — no chemotherapy administered
- Key finding: PER2 functions as tumour suppressor in OSCC by activating autophagy through suppression of PI3K/AKT/mTOR. First demonstration of PER2-autophagy regulation in OSCC.
- Limitation: Single cell lines; Journal of Cancer is lower-tier; no cisplatin data; no circadian oscillation measured
- Relevance to review: Most directly OSCC-relevant PER2 paper. PI3K/AKT/mTOR–PER2 axis in OSCC mechanistically linked to cisplatin resistance.

---

### Zhang Q, Zhao X, Liu H, et al. (2020). Circadian Clock Protein PERIOD2 Suppresses the PI3K/Akt Pathway and Promotes Cisplatin Sensitivity in Ovarian Cancer. *Cancer Management and Research*, 12, 11513–11524. DOI: 10.2147/CMAR.S278903. PMID: 33244267.
**Extraction:**
- Molecule: PER2; PI3K/AKT; MDR1; caspase-3
- Tissue: Ovarian cancer (SKOV3, SKOV3/DDP cisplatin-resistant cell lines)
- Cisplatin-specific: Yes — cisplatin-specific resistance and sensitivity endpoints
- Key finding: PER2 loss via promoter hypermethylation confers cisplatin resistance in ovarian cancer by activating PI3K/AKT/MDR1 and suppressing apoptosis.
- Limitation: Ovarian cancer, not HNSCC; lower-tier journal; in vitro/xenograft only
- Relevance to review: Provides mechanistic link between clock-gene epigenetic silencing and cisplatin resistance via PI3K/AKT — general principle applicable to HNSCC.

---

### Dakup PP, Porter KI, Little AA, Gajula RP, Zhang H, Skornyakov E, Kemp MG, Van Dongen HPA, Gaddameedhi S. (2018). The circadian clock regulates cisplatin-induced toxicity and tumor regression in melanoma mouse and human models. *Oncotarget*, 9(18), 14524–14538. DOI: 10.18632/oncotarget.24539. PMID: 29581861.
**Extraction:**
- Molecule: PER1/PER2; cisplatin-DNA adducts; immune response
- Tissue: Skin (melanoma tumour); blood; kidney
- Key finding: PM cisplatin showed enhanced cisplatin-DNA adduct removal and lower renal toxicity vs. AM. Time-of-day effect abolished in Per1/2-null mice. Clock integrity required for chronotherapy benefit.
- ⚠️ Journal quality concern: *Oncotarget* was removed from MEDLINE indexing. **Use with explicit caveat; consider demoting to supplementary reference.**
- Relevance: Important in vivo proof-of-principle that PER1/2 integrity determines cisplatin chronotherapy efficacy; cancer-immune component is novel.

---

## GSH / GCLC (redox)

### Li X-M, Metzger G, Filipski E, Boughattas N, Lemaigre G, Hecquet B, Filipski J, Lévi F. (1997). Pharmacologic modulation of reduced glutathione circadian rhythms with buthionine sulfoximine: relationship with cisplatin toxicity in mice. *Toxicology and Applied Pharmacology*, 143(2), 281–290. DOI: 10.1006/taap.1997.8086. PMID: 9144445.
**Extraction:**
- Molecule: Reduced glutathione (GSH); buthionine sulfoximine (BSO); GCLC (implied)
- Tissue: Liver, jejunum, colon (24-h rhythm confirmed); bone marrow (no significant rhythm); kidney (GSH negligible)
- Model: Male B6D2F1 mice (n=560); 6 time-points 4-h apart; BSO to ablate GSH rhythm; cisplatin toxicity by survival analysis
- Circadian evidence: Significant 24-h rhythm of GSH in liver, jejunum, and colon. BSO abolished the 24-h cisplatin toxicity rhythm, demonstrating GSH circadian rhythm is a major determinant of cisplatin toxicity variation.
- Cisplatin-specific: Yes — cisplatin toxicity is the direct endpoint
- Key finding: Foundational paper demonstrating circadian variation in hepatic/gastrointestinal GSH is a primary driver of time-of-day variation in cisplatin lethality. Provides a redox mechanism complementary to NER/XPA.
- Limitation: Mouse model; lethality endpoint; kidney GSH negligible so mechanism is primarily hepatic/GI; 1997 publication
- Relevance to review: Establishes GSH as a circadian-regulated detoxification buffer for cisplatin.

---

## Mucosal Proliferation Rhythms

### Bjarnason GA, Jordan RCK, Wood PA, Li Q, Lincoln DW, Sothern RB, Hrushesky WJM, Ben-David Y. (2001). Circadian expression of clock genes in human oral mucosa and skin: association with specific cell-cycle phases. *American Journal of Pathology*, 158(5), 1793–1801. DOI: 10.1016/S0002-9440(10)64135-1. PMID: 11337377.
**Extraction:**
- Molecule: hCLOCK, hTIM, hPER1, hCRY1, hBMAL1; cell-cycle markers (p53/G1, cyclin E/S-phase, thymidylate synthase/S-phase)
- Tissue: Human oral mucosa and skin biopsy specimens
- Model: Human healthy volunteers; serial biopsies at multiple circadian time points; IHC and ISH
- Circadian evidence: All five clock genes show circadian profiles in oral mucosa. hPER1 peak coincides with G1-phase marker p53 peak; S-phase markers peak later (~early afternoon).
- Key finding: First demonstration in humans that clock genes oscillate in oral mucosa with a phase associating with specific cell-cycle phases. Oral mucosa demonstrates autonomous circadian clock gene oscillation linked to cell-cycle phase.
- Limitation: No chemotherapy; healthy volunteers; small sample; 2001 publication
- Relevance to review: **Foundational paper linking oral mucosal clock gene expression to cell-cycle timing in humans.** Key citation for mucosal proliferation circadian node.

---

### Bjarnason GA, Cooper BJ, Alon N, Minoo P, et al. (2021). Genes relevant to tissue response to cancer therapy display diurnal variation in mRNA expression in human oral mucosa. *Journal of Circadian Rhythms*, 19(1), 3. DOI: 10.5334/jcr.213. PMID: 34221066.
**Extraction:**
- Molecule: PER3, CIART, TEF, PER1, PER2, CRY2, ARNTL (circadian genes); WEE1 (cell cycle/therapy response — only therapy-response gene with significant diurnal variation)
- Tissue: Human oral mucosa (healthy volunteers)
- Model: 11 healthy volunteers; RNA-seq at 6 time-points every 4 h over 24 h
- Key finding: 7/16 circadian-regulation genes show significant diurnal variation. Of 118 cell-cycle/therapy-response genes, **only WEE1** achieves significant diurnal variation — a relatively negative finding for therapy-specific circadian biology in oral mucosa.
- Limitation: Journal of Circadian Rhythms (MEDLINE-indexed, lower-tier); healthy volunteers only; n=11; no cisplatin data
- Relevance to review: Most current human oral mucosa transcriptome-level circadian dataset. The finding that most therapy-response genes do NOT show significant diurnal variation is an important **honest gap** — clock genes oscillate robustly in oral mucosa but downstream cisplatin-relevant effectors (NER genes, GSH synthesis, apoptosis) may not.

---

## Inflammatory Rhythms

*(See Lee JH & Sancar 2011 PMID 21690409 — NF-κB circadian gating by CRY1 — under PER/CRY section above.)*

**Additional note:** NF-κB drives inflammatory cytokines (TNF-α, IL-6, IL-1β) in mucosal epithelia during cisplatin-induced mucositis. Circadian gating of NF-κB by CRY means inflammatory amplification of cisplatin mucosal injury is clock-regulated.

---

## p53–PUMA/BAX

*(See Lee JH & Sancar 2011 PMID 21628572 — CRY-p73 apoptosis — under PER/CRY section above.)*

**Additional note:** In TP53-mutant HNSCC (one of the most common driver mutations in this cancer type), p73 activation by platinum compounds may be the dominant apoptotic route, making the CRY-p73 axis particularly relevant.

---

## Summary Statistics

| Subsection | Papers fully extracted | Papers abstract-only | Evidence gap flagged |
|---|---|---|---|
| XPA / NER | 4 (PMID 19164551, 20304803, 29735688, 25302769) + 1 review (33414192) | 0 | OSCC/HNSCC-specific XPA oscillation = NONE |
| ERCC1–XPF | 0 (discussed within XPA papers) | 0 | Gap — no standalone circadian ERCC1 paper |
| OCT2 / SLC22A2 | 1 (PMID 24567546) | 0 | No human kidney data; no HNSCC data |
| CTR1 / SLC31A1 | 0 | 0 | Gap — no circadian CTR1 papers found |
| BMAL1 / ARNTL | 4 (PMID 32522976, 30621723, 27821487⚠️, 36180647) | 1 (Chen 2023) | OSCC BMAL1/cisplatin = indirect only |
| PER / CRY | 5 (PMID 21628572, 21690409, 29581861⚠️, 33244267, PMC7150464) | 0 | No OSCC cisplatin+PER data |
| GSH / GCLC | 1 (PMID 9144445) | 0 | Kidney GSH negligible; no OSCC data |
| Mucosal proliferation | 2 (PMID 11337377, 34221066) | 0 | Healthy volunteers only; no cisplatin |
| Inflammatory | Shared with PER/CRY | — | — |
| p53–PUMA/BAX | Shared with PER/CRY | — | — |

**Key honest gap:** There is **no OSCC/HNSCC-specific circadian-cisplatin evidence** at a high-tier level. All mechanistic XPA/NER, OCT2, and GSH data come from mouse kidney/liver models. ARNTL/cisplatin resistance data is in NPC (not OSCC). PER2 and ARNTL functional data in OSCC exist but without cisplatin endpoints. The Bjarnason oral mucosa papers confirm clock gene oscillation in human oral mucosa but find minimal diurnal variation in downstream therapy-response genes. The honest conclusion: the molecular rationale is strong by mechanism extrapolation, but direct OSCC/HNSCC circadian-cisplatin evidence is absent from the high-tier literature as of May 2026.
