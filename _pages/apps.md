---
layout: page
title: applications
description: R/Shiny tools for toxicology, PFAS pharmacokinetics, and lead exposure modeling.
permalink: /apps/
nav: true
nav_order: 4
---

NTES maintains a small set of concise, open-source R/Shiny tools used for data exploration and exposure/toxicokinetic modeling. Below are short summaries with links to the public code and deployment (where available). Screenshots are placeholders — replace with preferred screenshots if you have them.

---

## OEHHA Data Explorer

An R/Shiny dashboard for searching, filtering, and exporting harmonized chemical data (regulatory values, toxicology, production, and biomonitoring). Designed for quick triage and data exports.

- **Demo:** [https://oehha.shinyapps.io/OEHHA-Data-Explorer_v1-0/](https://oehha.shinyapps.io/OEHHA-Data-Explorer_v1-0/)
- **Code:** [https://github.com/ScottCoffin/OEHHA-Data-Explorer](https://github.com/ScottCoffin/OEHHA-Data-Explorer)
- **Screenshot:** <img src="/assets/img/data_explorer_logo-800.png" srcset="/assets/img/data_explorer_logo-480.png 480w, /assets/img/data_explorer_logo-800.png 800w, /assets/img/data_explorer_logo-1400.png 1400w" sizes="(max-width:800px) 100vw, 800px" alt="Data Explorer screenshot">

---

## PFAS TK / PK App

Point-and-click interface to run PBPK and simpler TK simulations for PFAS, compare models to measurements, and export time-series results for analysis.

- **Demo:** [https://oehha.shinyapps.io/PFAS_TK/](https://oehha.shinyapps.io/PFAS_TK/)
- **Code:** [https://github.com/ScottCoffin/PFOS_PBPK_fork](https://github.com/ScottCoffin/PFOS_PBPK_fork)
- **Screenshot:** <img src="/assets/img/PFAS_pk_app-800.png" srcset="/assets/img/PFAS_pk_app-480.png 480w, /assets/img/PFAS_pk_app-800.png 800w, /assets/img/PFAS_pk_app-1400.png 1400w" sizes="(max-width:800px) 100vw, 800px" alt="PFAS TK/PK app screenshot">

---

## Leggett+ Lead PBPK

Modern R implementation of the Leggett age-structured lead PBPK model with scenario templates for occupational and environmental exposures and exportable results.

- **Demo:** [https://oehha.shinyapps.io/LeggettPlus/](https://oehha.shinyapps.io/LeggettPlus/)
- **Code:** [https://github.com/ScottCoffin/Leggett-\_lead_PBPK](https://github.com/ScottCoffin/Leggett-_lead_PBPK)

- **Screenshot:** _coming soon_

---

## Access & Notes

- Some `shinyapps.io` deployments are restricted to OEHHA staff; contact `NTES@oehha.ca.gov` for access requests.
- To contribute: open an issue or pull request in the linked GitHub repository; each repo contains a README with local quick-start instructions.

---
