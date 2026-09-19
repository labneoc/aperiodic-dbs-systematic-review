# Data Extraction Protocol

Data extraction was performed by a single reviewer (L.S.M.P.) in two stages. Study identification, screening, and eligibility decisions were managed in Parsif.al. Records retained after screening were transferred to a structured spreadsheet (`extraction/extraction_data.xlsx`), organized into four categories described below.

---

## Category 1 — Bibliographic and Descriptive

| Field | Description |
|-------|-------------|
| ID | Sequential numeric identifier assigned during extraction. |
| Title | Full article title as published. |
| DOI | Digital Object Identifier. |
| Abstract | Full abstract as published. |
| Signal type | Recording modality: LFP, MER/SPK, EEG, ECoG, sEEG, or combination. |

---

## Category 2 — Methodological Characteristics

| Field | Description |
|-------|-------------|
| Metric used | Aperiodic estimation method and derived parameters (e.g., FOOOF/specparam — exponent and offset; IRASA; custom log-log fit; avalanche transition matrix). |
| Fitting range (Hz) | Frequency range used for aperiodic fitting (e.g., "2–50 Hz"). Coded "NR" if not reported. |
| Frequency exclusions | Specific bands excluded during fitting to avoid oscillatory peak contamination (e.g., "13–60 Hz excluded in first pass"). Coded "None" when authors explicitly confirm no exclusions; "NR" when not addressed. |
| Fit quality reported | Whether a goodness-of-fit statistic was reported: "Yes (R²>0.XX)" with value; "Yes" without value; or "No". |
| Artifact rejection reported | Whether a formal artifact rejection protocol and/or quantitative rejection rate was reported: "Yes (X±Y% excluded)"; "Yes, no rate"; or "No — visual inspection only". |
| Washout protocol | Duration and type of medication/stimulation washout prior to recording. For non-PD/medication studies, the equivalent (e.g., antiepileptic drug status) or "N/A". |

---

## Category 3 — Cohort and Design Characteristics

| Field | Description |
|-------|-------------|
| N (sample size) | Number of patients in the main analysis. If multiple N values apply (e.g., baseline vs. follow-up), the primary N is reported with others in parentheses. |
| Age (mean ± SD or range) | Age at recording or surgery. Reported as available in the source. |
| Sex (M/F) | Biological sex breakdown as reported by authors. |
| Anatomical target | Brain structure(s) from which signals were recorded (e.g., STN, GPi, habenula, ANT). |
| Pathology | Clinical diagnosis: PD, dystonia, essential tremor, epilepsy, depression, TRD, or combination. |
| Recording context | "Intraoperative" (during DBS surgery); "Chronic sensing" (implanted IPG, ambulatory); "Cross-species" (includes animal arm). |
| Temporal design | "Cross-sectional" (single time point); "Longitudinal" (multiple visits over time); "Bidirectional/within-session" (ON/OFF contrast within the same session). |
| Number of centers | Number of hospitals or institutions contributing data. |
| Follow-up duration | Time from surgery/intervention to final recording or assessment. "N/A" for acute intraoperative studies. |

---

## Category 4 — Outcome and Synthesis Fields

| Field | Description |
|-------|-------------|
| Clinical scale | Disease-specific outcome instrument used (e.g., MDS-UPDRS-III, HAMD-17, BFMDRS, TWSTRS, seizure frequency). |
| Medication effect | Whether and how levodopa (or equivalent) modulated the aperiodic signal. |
| Spatial discrimination | Whether the aperiodic metric contributed to anatomical localization or contact selection. |
| Direction of aperiodic change | How the exponent/offset changed with the primary intervention: "↑ (steeper)" = more inhibition; "↓ (flatter)" = more excitation; "No significant change". Coded "N/A" for purely correlational designs without manipulation. |
| Beta vs. aperiodic comparison | "Yes" if the study formally compared aperiodic and periodic (beta) metrics against the same outcome; "No" otherwise. |
| Incremental value demonstrated | "Yes" if the study showed aperiodic parameters add information beyond periodic alone; "No" if not tested or no gain; "N/A" if the comparison design does not apply. |
| E/I manipulation type | Experimental modulator: "Pharmacological" (levodopa, other drugs); "Stimulation" (DBS ON/OFF); "Disease state" (between-group comparison); combination. "N/A" if no E/I manipulation tested. |
| Criticality framework invoked | "Yes" only if the study's own authors explicitly invoke neural criticality, scale-free dynamics as a signature of a critical point, or avalanches as evidence of criticality. "No" otherwise — this codes the authors' framing, not the reviewer's interpretation. |
| Main findings | Qualitative and quantitative summary of the study's principal results relevant to the four research questions. |
| Clinical correlation | The practical conclusion regarding the relationship between aperiodic parameters and clinical outcome measures, with specific statistics where reported. |
| RQ1–RQ4 classification | Each study classified against each research question as: "Yes" (formally tested, unambiguous positive); "Partial" (tested but qualified or complementary); "No" (formally tested null or negative); "N/A" (question not addressed by this study's design). |

---

## NOS Scoring Fields

| Field | Description |
|-------|-------------|
| Selection (0–4 ★) | Stars awarded for the four Selection domain criteria (see `extraction/nos_criteria.md`). |
| Comparability (0–2 ★) | Stars awarded for the two Comparability domain criteria. |
| Outcome (0–3 ★) | Stars awarded for the three Outcome domain criteria. |
| Total (0–9 ★) | Sum of all three domain scores. |

---

## Notes on Cohort Overlap

Two instances of confirmed cohort overlap were identified and documented:

1. **IDs 09 and 11** (Joshi et al. 2025 and Joshi et al. 2026): same 9 patients
   from Case Western Reserve University. Retained as separate extraction units
   because they address distinct research questions. Shared patients counted
   once in aggregate N.

2. **IDs 04 and 24** (Gerster et al. 2025 and Wiest et al. 2023b): the Oxford
   sub-dataset in Gerster et al. (n=17) overlaps with Wiest et al. 2023b.
   Both retained; shared patients counted once in aggregate N.

---

## Extraction Tool

Parsif.al (https://parsif.al) was used for screening and eligibility decisions. The full extraction spreadsheet is at `extraction/extraction_data.xlsx`.