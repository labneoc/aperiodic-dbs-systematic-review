# Database-Specific Notes

## PubMed
- Uses [tiab] field tag for title/abstract searching
- MeSH terms added for "Deep Brain Stimulation", "Subthalamic Nucleus",
  "Microelectrodes", "Electroencephalography", and "Electrocorticography"
- Date filter applied via interface: 2021/01/01–2026/12/30

## Embase
- Uses :ti,ab,kw field tag
- Controlled vocabulary (/exp) added for core concepts
- Truncation with * supported natively
- Date filter applied via py (publication year) field within the string

## Scopus
- Uses TITLE-ABS-KEY() function
- Truncation with * supported natively
- Date filter applied via PUBYEAR operator outside the main block

## IEEE Xplore
- No field-tag syntax; searches full record by default
- No truncation operator available — each term entered explicitly
- Date filter applied via interface range: 2021–2026
- Lowest yield (n=4); expected given engineering focus of the database