# Screening Criteria

Eligibility was determined using the Population, Intervention, Comparison, Outcomes, and Study Design (PICOS) framework. Criteria were applied at the title/abstract screening stage. All decisions were made by a single reviewer (L.S.M.P.) and logged in `screening_decisions.csv`.

---

## Inclusion Criteria

| Code | Criterion |
|------|-----------|
| **I1** | Primary studies analyzing the aperiodic (1/f) or non-oscillatory component of electrophysiological signals. |
| **I2** | Investigation of movement disorders, psychiatric disorders or epilepsy in the context of DBS. |
| **I3** | Use of complexity, fractality, entropy, or non-extensive statistics metrics to characterize brain dynamics. |
| **I4** | Studies published between 2021 and 2026. |

A record was retained if it met all four inclusion criteria (I1–I4) and none of the exclusion criteria below.

---

## Exclusion Criteria

| Code | Criterion |
|------|-----------|
| **E1** | Studies with interventions outside the scope of conventional DBS, purely clinical studies without quantitative neural signal analysis, or purely mathematical studies without application to real data. |
| **E2** | Secondary literature (reviews, editorials), conference papers, oral presentations, abstract-only publications, or preprints not peer-reviewed. |
| **E3** | Single-case reports (N = 1). |
| **E4** | Experimental models used strictly in animals without direct correlation with human biomarkers. |

---

## Operational Notes

- **I1 vs I3 distinction:** I1 covers spectral parameterization of the aperiodic component (FOOOF/specparam, IRASA, log-log linear fit). I3 covers complexity and fractal metrics applied to the same signals (DFA, multifractal analysis, Tsallis entropy, avalanche analysis) when they do not produce a standard 1/f exponent but quantify related scale-free dynamics.

- **E2 preprint rule:** Preprints were excluded unless a peer-reviewed version was identified and available within the search window.

- **E4 animal model rule:** Cross-species studies including both animal and human data were retained if the human component was substantive and separately reported (e.g., Wiest et al. 2023, eLife — ID24).

- **Duplicate handling:** When a preprint and its published version both appeared in the search results, only the published peer-reviewed version was retained. When two records described the same patient cohort but addressed distinct research questions, both were retained as separate extraction units with a cohort overlap note (see extraction data, 09 and 11).