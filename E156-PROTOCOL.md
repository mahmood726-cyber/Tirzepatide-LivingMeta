# E156 Protocol — `Tirzepatide-LivingMeta`

This repository is the source code and dashboard backing a cluster of E156 micro-papers on the [E156 Student Board](https://mahmood726-cyber.github.io/e156/students.html).

**2 papers share this repo.** Each is listed below with its own title, estimand, dataset, 156-word body, and submission metadata (authorship, ethics, references, target journal, etc.). Students claiming any of these papers should use the body + metadata for their specific paper number and submit separately.

## Papers in this repo

| Paper # | Title |
| ---: | :--- |
| `[363]` | Tirzepatide CV/Obesity: A Transparent Living Meta-Analysis v13 |
| `[435]` | Tirzepatide in Cardiometabolic Disease: Living Meta-Analysis |

---

## `[363]` Tirzepatide CV/Obesity: A Transparent Living Meta-Analysis v13

**Type:** living-ma  |  ESTIMAND: RR  
**Data:** SURMOUNT-series RCTs deployed; ~3,148 patients across currently ingested trials

### 156-word body

Can a browser-based transparent living meta-analysis reproduce published pooled estimates for tirzepatide in cardiometabolic disease? The v13 app ingested SURMOUNT-series RCTs from ClinicalTrials.gov cross-checked against PubMed and OpenAlex, with 3,148 patients across currently extracted trials. DerSimonian-Laird random-effects pooling with HKSJ correction ran in-browser on the logged risk ratio, with cumulative, provenance, QA, and cross-validation engines logging every step. The pooled risk ratio was concordant with the Lim 2026 SURMOUNT pooled benchmark within lockdown tolerance, and estimates update live as trials are ingested. Cross-validation against R metafor and Python scipy scripts reproduced the pooled point estimate, and leave-one-out plus REML-versus-HKSJ sensitivity preserved direction. A transparent browser-native pipeline matches benchmark pooled effects for tirzepatide in cardiometabolic disease without server-side computation while surfacing every provenance decision. The app inherits CT.gov and PubMed coverage gaps.

### Submission metadata

```
Corresponding author: Mahmood Ahmad <mahmood.ahmad2@nhs.net>
ORCID: 0000-0001-9107-3704
Affiliation: Tahir Heart Institute, Rabwah, Pakistan

Links:
  Code:      https://github.com/mahmood726-cyber/Tirzepatide-LivingMeta
  Protocol:  https://github.com/mahmood726-cyber/Tirzepatide-LivingMeta/blob/main/E156-PROTOCOL.md
  Dashboard: https://mahmood726-cyber.github.io/tirzepatide_livingmeta/

References (topic pack: heterogeneity / prediction interval):
  1. Higgins JPT, Thompson SG. 2002. Quantifying heterogeneity in a meta-analysis. Stat Med. 21(11):1539-1558. doi:10.1002/sim.1186
  2. IntHout J, Ioannidis JP, Rovers MM, Goeman JJ. 2016. Plea for routinely presenting prediction intervals in meta-analysis. BMJ Open. 6(7):e010247. doi:10.1136/bmjopen-2015-010247

Data availability: No patient-level data used. Analysis derived exclusively
  from publicly available aggregate records. All source identifiers are in
  the protocol document linked above.

Ethics: Not required. Study uses only publicly available aggregate data; no
  human participants; no patient-identifiable information; no individual-
  participant data. No institutional review board approval sought or required
  under standard research-ethics guidelines for secondary methodological
  research on published literature.

Funding: None.

Competing interests: MA serves on the editorial board of Synthēsis (the
  target journal); MA had no role in editorial decisions on this
  manuscript, which was handled by an independent editor of the journal.

Author contributions (CRediT):
  [STUDENT REWRITER, first author] — Writing – original draft, Writing –
    review & editing, Validation.
  [SUPERVISING FACULTY, last/senior author] — Supervision, Validation,
    Writing – review & editing.
  Mahmood Ahmad (middle author, NOT first or last) — Conceptualization,
    Methodology, Software, Data curation, Formal analysis, Resources.

AI disclosure: Computational tooling (including AI-assisted coding via
  Claude Code [Anthropic]) was used to develop analysis scripts and assist
  with data extraction. The final manuscript was human-written, reviewed,
  and approved by the author; the submitted text is not AI-generated. All
  quantitative claims were verified against source data; cross-validation
  was performed where applicable. The author retains full responsibility for
  the final content.

Preprint: Not preprinted.

Reporting checklist: PRISMA 2020.

Target journal: ◆ Synthēsis (https://www.synthesis-medicine.org/index.php/journal)
  Section: Methods Note — submit the 156-word E156 body verbatim as the main text.
  The journal caps main text at ≤400 words; E156's 156-word, 7-sentence
  contract sits well inside that ceiling. Do NOT pad to 400 — the
  micro-paper length is the point of the format.

Manuscript license: CC-BY-4.0.
Code license: MIT.

SUBMITTED: [ ]
```

---

## `[435]` Tirzepatide in Cardiometabolic Disease: Living Meta-Analysis

**Type:** living-ma  |  ESTIMAND: OR for at least 5 percent body weight loss  
**Data:** 4 RCTs (SURMOUNT-1/-2/-3/-4), 3,148 patients (pooled-arms subset)

### 156-word body

Does tirzepatide, a dual GIP and GLP-1 receptor agonist, achieve clinically meaningful weight reduction across obesity, type 2 diabetes, and weight maintenance settings? Four randomized placebo-controlled phase 3 trials with a pooled-arms subset of 3,148 patients with obesity, with or without diabetes, compared tirzepatide 5/10/15 mg weekly against placebo over 36 to 88 weeks. DerSimonian-Laird random-effects meta-analysis pooled odds ratios for at least 5 percent weight loss with HKSJ correction. The pooled odds ratio was 22.94 (95% CI 12.46-42.23), with substantial heterogeneity (I-squared 89%) reflecting dose-dependent effects across the 5 to 15 mg dose range. Mean weight reductions ranged from 15 to 21 percent across the highest dose arms. Tirzepatide produces the largest documented pharmacologic weight reduction approaching the lower end of bariatric surgery outcomes. Cardiovascular outcome trials remain pending, gastrointestinal tolerability and dose escalation logistics affect persistence, and weight regain following discontinuation is substantial.

### Submission metadata

```
Corresponding author: Mahmood Ahmad <mahmood.ahmad2@nhs.net>
ORCID: 0000-0001-9107-3704
Affiliation: Tahir Heart Institute, Rabwah, Pakistan

Links:
  Code:      https://github.com/mahmood726-cyber/Tirzepatide-LivingMeta
  Protocol:  https://github.com/mahmood726-cyber/Tirzepatide-LivingMeta/blob/main/E156-PROTOCOL.md
  Dashboard: https://mahmood726-cyber.github.io/tirzepatide_livingmeta/

References (topic pack: heterogeneity / prediction interval):
  1. Higgins JPT, Thompson SG. 2002. Quantifying heterogeneity in a meta-analysis. Stat Med. 21(11):1539-1558. doi:10.1002/sim.1186
  2. IntHout J, Ioannidis JP, Rovers MM, Goeman JJ. 2016. Plea for routinely presenting prediction intervals in meta-analysis. BMJ Open. 6(7):e010247. doi:10.1136/bmjopen-2015-010247

Data availability: No patient-level data used. Analysis derived exclusively
  from publicly available aggregate records. All source identifiers are in
  the protocol document linked above.

Ethics: Not required. Study uses only publicly available aggregate data; no
  human participants; no patient-identifiable information; no individual-
  participant data. No institutional review board approval sought or required
  under standard research-ethics guidelines for secondary methodological
  research on published literature.

Funding: None.

Competing interests: MA serves on the editorial board of Synthēsis (the
  target journal); MA had no role in editorial decisions on this
  manuscript, which was handled by an independent editor of the journal.

Author contributions (CRediT):
  [STUDENT REWRITER, first author] — Writing – original draft, Writing –
    review & editing, Validation.
  [SUPERVISING FACULTY, last/senior author] — Supervision, Validation,
    Writing – review & editing.
  Mahmood Ahmad (middle author, NOT first or last) — Conceptualization,
    Methodology, Software, Data curation, Formal analysis, Resources.

AI disclosure: Computational tooling (including AI-assisted coding via
  Claude Code [Anthropic]) was used to develop analysis scripts and assist
  with data extraction. The final manuscript was human-written, reviewed,
  and approved by the author; the submitted text is not AI-generated. All
  quantitative claims were verified against source data; cross-validation
  was performed where applicable. The author retains full responsibility for
  the final content.

Preprint: Not preprinted.

Reporting checklist: PRISMA 2020.

Target journal: ◆ Synthēsis (https://www.synthesis-medicine.org/index.php/journal)
  Section: Short Meta-Analysis — submit the 156-word E156 body verbatim as the main text.
  The journal caps main text at ≤400 words; E156's 156-word, 7-sentence
  contract sits well inside that ceiling. Do NOT pad to 400 — the
  micro-paper length is the point of the format.

Manuscript license: CC-BY-4.0.
Code license: MIT.

SUBMITTED: [ ]
```


---

_Auto-generated from the workbook by `C:/E156/scripts/create_missing_protocols.py`. If something is wrong, edit `rewrite-workbook.txt` and re-run the script — it will overwrite this file via the GitHub API._