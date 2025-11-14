---
layout: page
title: NTES Applications
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
- **Screenshot:** ![Data Explorer](/assets/img/1.jpg)

---

## PFAS TK / PK App

Point-and-click interface to run PBPK and simpler TK simulations for PFAS, compare models to measurements, and export time-series results for analysis.

- **Demo:** [https://oehha.shinyapps.io/PFAS_TK/](https://oehha.shinyapps.io/PFAS_TK/)
- **Code:** [https://github.com/ScottCoffin/PFOS_PBPK_fork](https://github.com/ScottCoffin/PFOS_PBPK_fork)
- **Screenshot:** ![PFAS TK](/assets/img/2.jpg)

---

## Leggett+ Lead PBPK

Modern R implementation of the Leggett age-structured lead PBPK model with scenario templates for occupational and environmental exposures and exportable results.

- **Demo:** [https://oehha.shinyapps.io/LeggettPlus/](https://oehha.shinyapps.io/LeggettPlus/)
- **Code:** [https://github.com/ScottCoffin/Leggett-_lead_PBPK](https://github.com/ScottCoffin/Leggett-_lead_PBPK)
- **Screenshot:** ![Leggett Plus](/assets/img/3.jpg)

---

## Access & Notes

- Some `shinyapps.io` deployments are restricted to OEHHA staff; contact `NTES@oehha.ca.gov` for access requests.
- To contribute: open an issue or pull request in the linked GitHub repository; each repo contains a README with local quick-start instructions.

---

If you'd like, I can (1) replace the placeholder screenshots with specific images from the repo, (2) update the code links to use the `OEHHA-NTES` organization (where available), or (3) add one-line install/run instructions under each app.
