# Files to update in labneoc/aperiodic-dbs-systematic-review

Generated against the final submitted manuscript. Copy these over the existing
repository contents; nothing here deletes anything.

## 1. ADD  supplementary/PRISMA_2020_checklist.docx
   The folder README documents this file but it was not in the repository.
   Both the Methods and the Data Accessibility Statement promise it.
   All 27 items (42 entries with sub-items), located by section name.

## 2. REPLACE  README.md
   The previous version was out of date against the submitted manuscript:
     - said "34 reports included (33 unique studies)"  ->  32 reports, 31 studies
     - listed 4 authors, omitting Artur Pedro M. Neto
     - gave the lead author as "Letícia S. M. Pereira"  ->  "Letícia S. Mangrich"
   Also adds analysis/ to the structure table and a registration note.

## 3. ADD  analysis/
   The Data Accessibility Statement promises "the analysis and simulation code";
   the repository contained none. Adds the fitting-window simulation code
   (fixed seed, reproduces the published values), its two output tables,
   Figure 5, and a README.

## 4. REPLACE  figures/prisma_flowchart.png  and ADD  figures/prisma_flowchart.pdf
   The stored PNG was 881 x 940 px (124 dpi at full column width), below print
   resolution. Replaced by a vector redraw plus a 300 dpi raster.

## 5. REPLACE  supplementary/README.md
   Updated notes, including which checklist items were recorded as not performed.

---

## Resolved: the pre-screening count discrepancy

`screening/prisma_counts.md` documented 104 automated duplicates plus 1 record
removed manually for date ineligibility, giving 138 screened, whereas the
manuscript reported 105 duplicates and 0 removed for other reasons.

**The repository was correct.** The manuscript and its Figure 3 have now been
corrected to 104 duplicates and 1 record removed for other reasons, so the two
are consistent. `screening/prisma_counts.md` needs no change, and the
`figures/prisma_flowchart.*` files supplied here carry the corrected numbers.
