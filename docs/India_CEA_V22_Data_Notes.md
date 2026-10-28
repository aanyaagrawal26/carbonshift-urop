# India grid-emissions reference data

The dashboard's public benchmark series is taken from the Central Electricity Authority (CEA), Government of India, *CO₂ Baseline Database for the Indian Power Sector*, Version 22.0, published August 2026. The release adds FY 2025–26 data. The official user guide is available at [CEA Version 22.0 user guide](https://cea.nic.in/api/cdm-report-version/view-pdf/en/82); the [CEA database page](https://cea.nic.in/cdm-co2-baseline-view?mappingId=234&lang=en) lists the database releases.

The application uses Appendix C, Table B: the weighted-average emission rate including renewable energy generation and including cross-border electricity transfers. Values (tCO₂/MWh) are FY 2021–22: 0.711; FY 2022–23: 0.716; FY 2023–24: 0.727; FY 2024–25: 0.710; FY 2025–26: 0.675. The FY 2025–26 summary table also reports 0.675 tCO₂/MWh. CEA describes this weighted average as total grid-connected CO₂ emissions divided by net electricity generation. The report says the Excel workbook contains additional precision; this project uses the published report values.

The interactive estimate uses:

`estimated grid CO₂ (t) = electricity use (kWh) / 1,000 × CEA factor (tCO₂/MWh)`

Because 1 t/MWh is numerically equal to 1 kg/kWh, the UI also displays the equivalent factor in kgCO₂/kWh. Estimates are location-based national grid-generation averages for direct grid electricity CO₂, not company-specific supplier data, marginal avoided emissions, lifecycle emissions, or a complete Scope 2 inventory. A comparison is meaningful only when baseline and scenario kWh refer to comparable periods and boundaries. Users should follow the factor and method required by their research protocol for formal reporting.

The CSV in `data/india_cea_grid_emission_factors_v22.csv` is the dashboard's bundled extract. Other operational demonstration datasets remain synthetic until replaced by user-provided data.
