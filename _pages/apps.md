---
layout: page
title: NTES Applications
description: R/Shiny tools for toxicology, PFAS pharmacokinetics, and lead exposure modeling.
permalink: /apps/
nav: true
nav_order: 4
---

NTES develops and maintains a suite of interactive R/Shiny applications to support chemical hazard assessment, exposure modeling, and data exploration. Each tool is open-source, reproducible, and designed for both OEHHA staff and external collaborators.

---

## 🌐 OEHHA Data Explorer

**Unify and interrogate thousands of chemicals across regulatory, toxicological, exposure, and production data streams.**

The OEHHA Data Explorer is an R/Shiny dashboard that brings together federal, state, and academic datasets so analysts can subset chemicals, visualize data availability, review screening values, and download harmonized tables. Whether you're assessing a new chemical or tracking production trends, this tool streamlines access to critical information.

### Quick Links
- 🚀 **[Launch Latest Stable Release](https://oehha.shinyapps.io/OEHHA-Data-Explorer_v1-0/)**
- 🌙 **[Launch Nightly Build (Internal Preview)](https://oehha.shinyapps.io/OEHHA-Data-Explorer/)** — Updates automatically; may include experimental features.
- 📦 **[GitHub Repository](https://github.com/ScottCoffin/OEHHA-Data-Explorer)**

### Key Features
- **Data Richness & Ranking** — Summarize coverage across data streams and identify gaps with percentile-based richness scores.
- **Physico-Chemical Properties** — Inspect OPERA-predicted properties from the NTP Integrated Chemical Environment (ICE).
- **Toxicity Values** — Retrieve toxicity reference values and modeled points of departure from EPA CompTox and published literature.
- **ADME** — Explore absorption, distribution, metabolism, and excretion parameters.
- **In Vitro & In Vivo** — Review high-throughput assay activity and animal/human toxicology results.
- **In Silico** — Investigate molecular docking and QSAR descriptors.
- **Cancer, DART, Sensitization & Irritation** — Track evaluations and assay results for specialized toxicity endpoints.
- **Production & Use** — Compare U.S. production volumes, California emissions, and reported chemical uses.
- **Exposure** — Review California biomonitoring and NTP exposure data.
- **Listing Status** — Monitor Proposition 65 designations over time.

### Quick Start (Local)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ScottCoffin/OEHHA-Data-Explorer.git
   cd OEHHA-Data-Explorer
   ```

2. **Install dependencies:**
   ```r
   # In R, install required packages (listed at top of app.R)
   install.packages(c("shiny", "shinydashboard", "tidyverse", "plotly", "DT", ...))
   ```

3. **Run the app:**
   ```r
   shiny::runApp("app.R")
   # For GitHub Codespaces or remote access:
   # shiny::runApp("app.R", host = "0.0.0.0", port = 8080)
   ```

4. **Navigate:** Begin on the "Start Here" tab to define your chemical set; use remaining tabs to explore data.

### Deployment & Access
- **Stable release** deployments are published to `shinyapps.io` alongside GitHub Releases.
- **Nightly build** refreshes automatically from `main` branch; internal preview only.
- ⚠️ All `shinyapps.io` instances require OEHHA credentials and are restricted to OEHHA staff.

### For Contributors
See the repository README for:
- Data acquisition scripts (NTP, CompTox, CDR, CARB, Papyrus, biomonitoring, etc.)
- Data processing and ranking pipeline
- Deployment notes and GitHub Actions workflow
- Contributing guidelines and issue templates

---

## 🧪 OEHHA PFAS PK Modelling Application

**Simulate and visualize pharmacokinetics (PK) of PFAS across species, model types, and exposure scenarios.**

The PFAS PK app provides a unified, point-and-click interface for PBPK and simple TK simulations. Fully editable parameter tables, transparent model selection, and reproducible exports make it easy to compare modeled vs. measured concentrations, run what-ifs, and document assumptions for peer review.

### Quick Links
- 🚀 **[Launch Development Deployment](https://oehha.shinyapps.io/PFAS_TK/)** (internal testing)
- 📦 **[GitHub Repository](https://github.com/ScottCoffin/PFOS_PBPK_fork)**

### Key Features
- **Experiment Table (Editable):** Define PFAS, species, sex, model type, dose, interval, exposure duration, and sampling time. Upload CSV/XLSX templates for bulk entry.
- **Model Availability & Nudges:** See which model types are supported for each PFAS/species/sex combination. App suggests preferred models but never changes your inputs.
- **Parameter Editors:**
  - Simple TK (single/two-compartment, biphasic) — inline edits; auto-calc half-life or volume of distribution where derivable.
  - MassTransferPBPK (Fischer 2025, Mouse/Male) — parameter table auto-loads PFAS rows in use; edits honored at runtime.
  - PBPK (PFOS, Chou & Lin 2019) — species/sex-specific parameter grids when PBPK rows present.
- **Results & Downloads:**
  - Concentration–time curves (multi-model, multi-compartment interactive plots).
  - Modeled vs. measured scatter (log–log with ±3× guide lines).
  - Summary stats: Cmax, AUC (mg·hr/L), CTWA.
  - One-click CSV/XLSX/HTML export.
- **TK Data Explorer:** Full curated toxicokinetic dataset with sources, units, and filters.

### Quick Start (Local)

1. **Install R and packages:**
   ```r
   install.packages(c(
     "shiny", "shinydashboard", "plotly", "DT", "ggplot2", "mrgsolve",
     "dplyr", "purrr", "rhandsontable", "readr", "readxl", "tidyverse",
     "cols4all", "shinyjs", "shinythemes", "shinycssloaders", "openxlsx"
   ))
   ```

2. **Clone and run:**
   ```bash
   git clone https://github.com/ScottCoffin/PFOS_PBPK_fork.git
   cd PFOS_PBPK_fork
   ```
   ```r
   shiny::runApp("app.R")
   ```

3. **Add your experiment:** Use the experiment table to define PFAS, species, model, and exposure. Or upload a CSV template.

4. **Explore results:** Run simulations, view time-series plots, and export data for further analysis.

### Models Supported
- **PBPK (PFOS):** Chou & Lin (2019); Mouse, Rat, Monkey, Human.
- **MassTransferPBPK:** Fischer et al. (2025); Mouse/Male; permeability & active transport mechanisms.
- **Simple TK:** Single/two-compartment and biphasic models for other PFAS.

### For Contributors
- Model implementations in `models/` (mrgsolve RDS files).
- Parameter datasets in `Additional files/Datasets/`.
- Validation table and deployment history included.
- Feature requests and bug reports welcome via GitHub Issues.

---

## ⚛️ Leggett+ Lead PBPK

**Model age-specific lead kinetics across occupational and environmental exposures.**

The Leggett+ model is an extension of the 1993 age-specific lead kinetic model, refined by OEHHA to better represent occupational exposures, update physiological transfer coefficients, and provide a modern R implementation with an interactive Shiny UI. Includes scenario templates, sensitivity analysis workflows, and comprehensive verification materials.

### Quick Links
- 🚀 **[Launch Shiny App](https://oehha.shinyapps.io/LeggettPlus/)**
- 📦 **[GitHub Repository](https://github.com/ScottCoffin/Leggett-_lead_PBPK)**

### Key Features
- **Scenario Templates:**
  - Occupational (continuous airborne exposure)
  - Occupational + Retirement (staged exposure with retirement phase)
  - Pulse (discrete events overlaid on background exposure)
- **Person-Specific Inputs:** Body weight, breathing rates (occupational & non-occupational), starting age, initial blood lead level (BLL).
- **Exposure Inputs:** Airborne concentrations (µg/m³), daily intakes (µg/day), working hours per week.
- **Interactive Results:**
  - Time-series plots by compartment (facet by group, log/linear Y-axis).
  - Summary table for any user-specified time point.
  - Model parameters and compartment diagram (Advanced tab).
- **Export Options:**
  - Interactive plots (self-contained HTML)
  - Time-series data (CSV)
  - Parameters and summary tables (copy, CSV, Excel)

### Quick Start (Local)

1. **Install packages:**
   ```r
   install.packages(c("shiny", "bslib", "DT", "tidyverse", "plotly"))
   ```

2. **Clone and navigate:**
   ```bash
   git clone https://github.com/ScottCoffin/Leggett-_lead_PBPK.git
   cd Leggett-_lead_PBPK
   ```

3. **Run the app:**
   ```r
   shiny::runApp("Pb_Leggett_Plus")
   ```

4. **Design a scenario:** Select scenario type, enter person and exposure parameters, then click "Initiate Simulation."

### Model Details
- Based on the 1993 Leggett age-specific model with OEHHA refinements.
- Compartments: Plasma, Bone (trabecular and cortical), Soft tissue, and target organs.
- Implementations: Both matrix-based and ODE-based (matching original MATLAB code).
- Verification scripts and reference scenarios included in `scripts/`.
- Sensitivity analysis workflow available in `Sensitivity analysis/`.

### For Contributors
- Report bugs or request features via GitHub Issues with reproduction steps and screenshots.
- Sensitivity analysis code and verification materials are available for validation and regression testing.
- See repository README for detailed compartment architecture and mathematical background.

---

## 📞 Contact & Support

For questions about any NTES application:
- **Email:** [NTES@oehha.ca.gov](mailto:NTES@oehha.ca.gov) or [Scott.Coffin@oehha.ca.gov](mailto:Scott.Coffin@oehha.ca.gov)
- **GitHub:** Open an issue in the respective repository with a clear description, reproduction steps, and any relevant data exports.
- **Deployment Issues:** Contact NTES via email for production problems or urgent matters.

---

## 🔗 Additional OEHHA Resources

- [CalEnviroScreen 4.0](https://oehha.ca.gov/calenviroscreen/report/calenviroscreen-40) — Environmental justice screening tool.
- [OEHHA Main Website](https://oehha.ca.gov) — Regulatory guidance, air toxics, water quality standards, and more.

