import pandas as pd
import streamlit as st

from utils.data_loader import load_csv_data
from utils.ui import apply_theme


DATASETS = [
    ("Demand", "sample_demand_data.csv", "Monthly product demand and a simple reference forecast."),
    ("Suppliers", "supplier_data.csv", "Synthetic supplier attributes for exploring weighted criteria."),
    ("Warehouses", "warehouse_data.csv", "Synthetic energy, space and inventory attributes."),
    ("Transport", "transportation_routes.csv", "Synthetic routes and illustrative fuel/emissions fields."),
]

DICTIONARY = pd.DataFrame(
    [
        ("Demand", "date", "Month of observation."),
        ("Demand", "product_category", "Synthetic product group."),
        ("Demand", "actual_demand", "Synthetic historical unit demand."),
        ("Demand", "forecast_demand", "Synthetic comparison value; not a trained forecast."),
        ("Demand", "price", "Synthetic price value; currency is not defined."),
        ("Demand", "promotion_flag", "Synthetic binary indicator for a promotion."),
        ("Demand", "seasonality", "Synthetic seasonal adjustment index."),
        ("Suppliers", "carbon_footprint", "Synthetic directional score only; not measured emissions."),
        ("Suppliers", "energy_efficiency", "Synthetic score (higher is treated as better)."),
        ("Suppliers", "renewable_energy", "Synthetic share-like value; no supplier records support it."),
        ("Suppliers", "cost_score", "Synthetic relative score; no currency or cost data."),
        ("Suppliers", "delivery_reliability", "Synthetic percentage-like score."),
        ("Suppliers", "certifications", "Synthetic category label; not verified certification."),
        ("Warehouses", "energy_consumption_kwh", "Synthetic monthly energy use in kWh."),
        ("Warehouses", "square_meters", "Synthetic facility area."),
        ("Warehouses", "storage_capacity", "Synthetic capacity in arbitrary units."),
        ("Warehouses", "inventory_turnover", "Synthetic turnover indicator."),
        ("Warehouses", "energy_source", "Synthetic energy-source category."),
        ("Transport", "distance_km", "Synthetic route distance in kilometres."),
        ("Transport", "baseline_fuel_l", "Illustrative fuel baseline calculated from distance."),
        ("Transport", "optimized_fuel_l", "Illustrative value generated from an assumed reduction."),
        ("Transport", "emissions_kg_co2", "Illustrative conversion only; factor is not sourced or validated."),
    ],
    columns=["Dataset", "Field", "Meaning / caveat"],
)


def main() -> None:
    apply_theme()
    st.title("Sample data")
    st.caption("Preview or download the deterministic demo datasets used by the prototype.")
    st.warning("All bundled records are synthetic. Scores and emissions-like values are illustrative, not observed or validated measurements.")

    tabs = st.tabs([item[0] for item in DATASETS] + ["Data dictionary"])
    for (label, filename, description), tab in zip(DATASETS, tabs[: len(DATASETS)]):
        with tab:
            data = load_csv_data(filename)
            st.subheader(label)
            st.caption(description)
            st.caption(f"{len(data):,} records · {len(data.columns)} fields · first 8 rows shown")
            st.dataframe(data.head(8), width="stretch", height=320, hide_index=True)
            st.download_button(
                f"Download {label.lower()} CSV",
                data=data.to_csv(index=False).encode("utf-8"),
                file_name=filename,
                mime="text/csv",
                key=f"download_{label.lower()}",
            )

    with tabs[-1]:
        st.subheader("Field definitions and caveats")
        st.dataframe(DICTIONARY, width="stretch", height=480, hide_index=True)
        st.caption("The generated examples do not define a consistent, research-grade emissions boundary or verified supplier data source.")


if __name__ == "__main__":
    main()
