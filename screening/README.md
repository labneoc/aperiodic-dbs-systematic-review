# screening/

This folder contains the eligibility criteria, screening decisions, and PRISMA flow counts for the systematic review.

---

## Files

| File | Contents |
|------|----------|
| `screening_criteria.md` | Inclusion (I1–I4) and exclusion (E1–E4) criteria with operational definitions |
| `screening_decisions.csv` | Decision log for all 138 screened records |
| `prisma_counts.md` | PRISMA 2020 flow counts, stage by stage |

---

## How to Read the CSV

The `screening_decisions.csv` file has four columns:

| Column | Values |
|--------|--------|
| `title` | Article title as screened |
| `decision` | `include` or `exclude` |
| `inclusion_criteria` | `ALL` for included records (= I1 + I2 + I3 + I4 all met); blank for excluded |
| `exclusion_reason` | `E1`, `E2`, `E3`, or `E4` for excluded records; blank for included |

**Inclusion logic:** a record was retained only if all four inclusion criteria (I1–I4) were met and no exclusion criterion (E1–E4) applied.

---

## Exclusion Codes

| Code | Criterion |
|------|-----------|
| E1 | Outside DBS scope / no quantitative neural signal analysis / purely mathematical |
| E2 | Secondary literature / conference paper / abstract-only / preprint |
| E3 | Single-case report (N = 1) |
| E4 | Animal model without direct human biomarker correlation |

---

## Tool

Screening was managed in **Parsif.al** (https://parsif.al).