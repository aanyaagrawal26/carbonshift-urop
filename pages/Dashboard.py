from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from utils.ui import apply_theme


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "india_cea_grid_emission_factors_v22.csv"
CEA_GUIDE_URL = "https://cea.nic.in/api/cdm-report-version/view-pdf/en/82"
CEA_DATABASE_URL = "https://cea.nic.in/cdm-co2-baseline-view?mappingId=234&lang=en"
INK = "#1f3029"
MUTED = "#586b60"
FOREST = "#245b45"
GOLD = "#d19839"
GRID = "#dce4dd"


@st.cache_data(show_spinner=False)
def load_factors() -> pd.DataFrame:
    factors = pd.read_csv(DATA_PATH)
    factors["factor_tco2_per_mwh"] = pd.to_numeric(factors["factor_tco2_per_mwh"])
    return factors


def factor_history_chart(factors: pd.DataFrame) -> go.Figure:
    years = factors["financial_year"].tolist()
    values = factors["factor_tco2_per_mwh"].tolist()
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=years,
            y=values,
            mode="lines+markers+text",
            name="CEA weighted average",
            line=dict(color=FOREST, width=3),
            marker=dict(color=FOREST, size=10, line=dict(color="#ffffff", width=2)),
            text=[f"{value:.3f}" for value in values],
            textposition="top center",
            textfont=dict(color=INK, size=12),
            hovertemplate="FY %{x}<br>%{y:.3f} tCO₂/MWh<extra></extra>",
        )
    )
    fig.update_layout(
        height=330,
        margin=dict(l=20, r=20, t=35, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Arial, sans-serif", color=INK, size=13),
        showlegend=False,
        yaxis=dict(
            title="tCO₂ per MWh",
            range=[0.64, 0.75],
            tickformat=".3f",
            tickfont=dict(color=INK),
            title_font=dict(color=INK),
            gridcolor=GRID,
            zeroline=False,
        ),
        xaxis=dict(
            title="Financial year",
            tickfont=dict(color=INK),
            title_font=dict(color=INK),
            showgrid=False,
            linecolor=GRID,
        ),
    )
    return fig


def comparison_chart(baseline_t: float, scenario_t: float) -> go.Figure:
    fig = go.Figure(
        go.Bar(
            x=["Baseline", "Proposed scenario"],
            y=[baseline_t, scenario_t],
            marker_color=["#94a89b", FOREST],
            text=[f"{baseline_t:.3f} t", f"{scenario_t:.3f} t"],
            textposition="outside",
            textfont=dict(color=INK, size=13),
            hovertemplate="%{x}<br>%{y:.3f} tonnes CO₂<extra></extra>",
        )
    )
    max_y = max(baseline_t, scenario_t, 0.01)
    fig.update_layout(
        height=300,
        margin=dict(l=18, r=18, t=35, b=15),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Arial, sans-serif", color=INK, size=13),
        showlegend=False,
        yaxis=dict(
            title="Estimated grid electricity CO₂ (tonnes)",
            range=[0, max_y * 1.25],
            tickfont=dict(color=INK),
            title_font=dict(color=INK),
            gridcolor=GRID,
            zeroline=False,
        ),
        xaxis=dict(tickfont=dict(color=INK), showgrid=False, linecolor=GRID),
    )
    return fig


def main() -> None:
    apply_theme()
    factors = load_factors()
    latest = factors.iloc[-1]

    st.title("India grid-emissions explorer")
    st.caption(
        "Explore the Central Electricity Authority’s published grid-emissions trend, "
        "then calculate an estimate from electricity use that you enter."
    )
    st.info(
        "This page uses real public CEA reference factors. Your project’s operational "
        "emissions are not prefilled or measured by this prototype."
    )

    top1, top2, top3 = st.columns(3)
    top1.metric("Latest CEA grid factor", f"{latest['factor_tco2_per_mwh']:.3f} tCO₂/MWh")
    top2.metric("Latest reporting year", f"FY {latest['financial_year']}")
    top3.metric("History in this release", f"{len(factors)} fiscal years")

    st.subheader("Published Indian grid factor")
    st.plotly_chart(factor_history_chart(factors), width="stretch", config={"displayModeBar": False})
    st.caption(
        "Weighted-average factor including renewable generation and adjusted for cross-border electricity transfers. "
        "This is a national grid-generation average, not a supplier-specific or marginal factor."
    )

    st.subheader("Estimate from your electricity data")
    st.markdown(
        "Enter electricity use for two comparable periods. The same selected-year factor is applied to both, "
        "so the comparison reflects your activity change rather than a change in the grid factor."
    )
    left, right = st.columns([0.9, 1.1], gap="large")
    with left:
        with st.container(border=True):
            years = factors["financial_year"].tolist()
            selected_year = st.selectbox(
                "CEA factor year",
                options=years,
                index=len(years) - 1,
                format_func=lambda year: f"FY {year}",
                help="Select the fiscal-year grid factor used for both calculations.",
            )
            baseline_kwh = st.number_input(
                "Baseline electricity use (kWh)",
                min_value=0.0,
                value=None,
                step=100.0,
                format="%.0f",
                placeholder="Enter your measured kWh",
                help="Use a measured bill, meter record, or documented dataset for the period.",
            )
            scenario_kwh = st.number_input(
                "Scenario electricity use (kWh)",
                min_value=0.0,
                value=None,
                step=100.0,
                format="%.0f",
                placeholder="Enter your comparison kWh",
                help="Enter actual or explicitly modeled electricity use for a comparable period.",
            )
            selected_factor = float(
                factors.loc[factors["financial_year"] == selected_year, "factor_tco2_per_mwh"].iloc[0]
            )
            st.caption(f"Selected factor: {selected_factor:.3f} tCO₂/MWh = {selected_factor:.3f} kgCO₂/kWh.")

    with right:
        if baseline_kwh is None or scenario_kwh is None:
            st.info("Enter both kWh values to calculate and graph your comparison. No activity data are prefilled.")
        else:
            baseline_t = float(baseline_kwh) / 1000.0 * selected_factor
            scenario_t = float(scenario_kwh) / 1000.0 * selected_factor
            avoided_t = baseline_t - scenario_t
            st.plotly_chart(
                comparison_chart(baseline_t, scenario_t),
                width="stretch",
                config={"displayModeBar": False},
            )

    if baseline_kwh is not None and scenario_kwh is not None:
        m1, m2, m3 = st.columns(3)
        m1.metric("Baseline estimate", f"{baseline_t:,.3f} t CO₂")
        m2.metric("Scenario estimate", f"{scenario_t:,.3f} t CO₂")
        m3.metric("Baseline − scenario", f"{avoided_t:,.3f} t CO₂")

    with st.expander("Source, data, and calculation"):
        st.markdown(
            f"**Primary source:** [CEA CO₂ Baseline Database, Version 22.0 user guide (August 2026)]({CEA_GUIDE_URL})  \n"
            f"**Official release page:** [CEA database and version downloads]({CEA_DATABASE_URL})"
        )
        st.write(
            "The chart uses the published weighted-average grid emission rate including renewable generation and "
            "cross-border electricity transfers, from Appendix C, Table B. CEA reports FY 2025–26 as 0.675 tCO₂/MWh. "
            "The report notes that the downloadable workbook contains additional precision."
        )
        st.code("Estimated grid CO₂ (tonnes) = electricity use (kWh) ÷ 1,000 × factor (tCO₂/MWh)", language="text")
        st.write(
            "This calculation estimates grid electricity CO₂ only. It is not a full lifecycle footprint or a formal "
            "Scope 2 inventory. Use the factor and boundary required by your research protocol for reporting."
        )
        st.dataframe(
            factors[["financial_year", "factor_tco2_per_mwh"]].rename(
                columns={
                    "financial_year": "Financial year",
                    "factor_tco2_per_mwh": "Weighted-average factor (tCO₂/MWh)",
                }
            ),
            width="stretch",
            hide_index=True,
        )
        st.download_button(
            "Download the CEA reference series (CSV)",
            data=DATA_PATH.read_bytes(),
            file_name="india_cea_grid_emission_factors_v22.csv",
            mime="text/csv",
        )


if __name__ == "__main__":
    main()
