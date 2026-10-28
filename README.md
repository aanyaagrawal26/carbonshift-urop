# CarbonShift — AI and Carbon-Aware Supply Chains

A Streamlit research-review companion and exploratory prototype for a UROP project on AI-driven approaches to carbon-footprint reduction in supply-chain management.

## Run locally in VS Code

Use Python 3.10 or newer. Open this folder in VS Code, choose **Terminal → New Terminal**, and run:

```bash
python3 -m venv .venv
source .venv/bin/activate                 # macOS / Linux
# .venv\Scripts\Activate.ps1             # Windows PowerShell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Open the local address printed in the terminal, usually `http://localhost:8501`. Stop the server with **Control+C** (macOS/Linux) or **Ctrl+C** (Windows). The project forces a light, high-contrast Streamlit theme in `.streamlit/config.toml`; after changing this file, fully stop and restart Streamlit.

## What the app contains

- **Project overview:** research question, current status and navigation to the working modules.
- **Research review:** structured synthesis, proposed framework, evaluation plan and evidence limitations.
- **India grid-emissions explorer:** a five-year chart of official Central Electricity Authority (CEA) grid-emission factors and an interactive calculator that uses electricity-use values you enter.
- **Demand forecasting, route optimization, supplier scoring and warehouse management:** exploratory analysis modules. Unless you upload or provide real operating data, their bundled records are synthetic demonstration data.
- **Sample data:** dataset previews and downloads. All bundled operational samples are synthetic.

The CEA explorer uses the CEA *CO₂ Baseline Database for the Indian Power Sector*, Version 22.0 (August 2026). It uses the published weighted-average factor including renewable generation and adjusted for cross-border electricity transfers, from FY 2021–22 through FY 2025–26. Source, units, formula, and scope are shown in the app and recorded in [`docs/India_CEA_V22_Data_Notes.md`](docs/India_CEA_V22_Data_Notes.md). The latest published value in that series is 0.675 tCO₂/MWh for FY 2025–26. This is an official public reference, not a measurement of your business or supply chain.

## Data and research limitations

The electricity calculator estimates grid electricity CO₂ from user-entered kWh and the selected CEA national factor. It does not provide live meter data, company-specific supplier factors, marginal avoided emissions, lifecycle emissions, or a complete Scope 2 inventory. For company-specific or live outputs, connect or upload your own dated, unit-labeled operational dataset and document the boundary and factor selection.

Other module outputs remain exploratory until tested with relevant real data. The app is not independently validated or compliance-ready. It should not be used for procurement or operational decisions without further testing. The supplied literature-review PDFs do not include a complete, traceable bibliography, so the research page avoids presenting unsupported performance or carbon-saving claims as established findings.

## Project structure

```text
app.py                              Streamlit application shell and grouped navigation
.streamlit/config.toml              Light theme and accessible color tokens
pages/                              Streamlit pages
  Project_Overview.py               Compact project home page
  Dashboard.py                       CEA India factor chart and user-input calculator
  Research.py                        Evidence synthesis and proposed evaluation
  Demand_Forecasting.py              Exploratory forecasting module
  Router_Optimizer.py                Exploratory routing module
  Supplier_Scoring.py                Exploratory supplier module
  Warehouse_Management.py            Exploratory warehouse module
  Data_Download.py                   Synthetic sample data and previews
data/india_cea_grid_emission_factors_v22.csv  Official reference series used in the dashboard
docs/India_CEA_V22_Data_Notes.md     Source, calculation, and scope notes
docs/                                Supplied project PDFs and research notes
assets/style.css                     Shared high-contrast visual theme
utils/                               Data, visualization and interface utilities
models/                              Forecasting and optimization modules
```

## Licence

MIT. See [LICENSE](LICENSE).
