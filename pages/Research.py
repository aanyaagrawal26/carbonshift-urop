import pandas as pd
import streamlit as st

from utils.ui import apply_theme


def main() -> None:
    apply_theme()
    st.title("Research review")
    st.caption("A concise map of what the supplied review says, what it proposes, and what evidence is still needed.")

    st.info("The project documents describe a literature-review stage and an exploratory prototype. They do not provide a complete bibliography or validated emissions-reduction results.")

    synthesis_tab, framework_tab, evaluation_tab, evidence_tab = st.tabs(
        ["Literature synthesis", "Proposed framework", "Evaluation plan", "Evidence & limits"]
    )

    with synthesis_tab:
        st.subheader("Three strands in the supplied review")
        evidence = pd.DataFrame([
            {"Theme": "Carbon accounting", "What the review says": "Scope and value-chain boundaries matter; indirect emissions are difficult to measure where data is distributed across suppliers and tiers.", "Implication": "Document boundary, activity data, factor source, unit and period."},
            {"Theme": "AI for operations", "What the review says": "Forecasting, inventory, routing, loading and scheduling are common application areas.", "Implication": "An efficiency gain alone does not establish an emissions reduction."},
            {"Theme": "AI for explicit carbon reduction", "What the review says": "A smaller body of work includes emissions in planning and discusses IoT or blockchain as possible data enablers.", "Implication": "Treat carbon as an explicit objective and make assumptions traceable."},
        ])
        st.dataframe(evidence, width="stretch", hide_index=True)
        st.caption("This is a synthesis of the supplied literature-review PDF, not a new systematic review. The source document does not cite individual claims.")
        st.subheader("Working research question")
        st.markdown(
            "How can predictive analytics and operational optimization be linked to transparent emissions estimates while balancing carbon, cost and service across selected supply-chain functions?"
        )

    with framework_tab:
        st.subheader("Proposed decision flow")
        st.caption("A conceptual direction for future work—not a validated integrated model.")
        flow = pd.DataFrame([
            {"Stage": "1 · Inputs", "Examples": "Demand, routes, loads, supplier data, facility energy", "Output": "Documented activity data"},
            {"Stage": "2 · Predict", "Examples": "Demand or operational forecasts", "Output": "Expected needs with forecast error"},
            {"Stage": "3 · Optimize", "Examples": "Carbon, cost and service constraints", "Output": "Comparable decision scenarios"},
            {"Stage": "4 · Account", "Examples": "Baseline, factors, boundary and uncertainty", "Output": "Transparent outcome report"},
        ])
        st.dataframe(flow, width="stretch", hide_index=True)
        st.warning("The repository contains separate exploratory modules for demand, routing, supplier scoring and warehouses. It does not establish full Scope 1, Scope 2 or Scope 3 coverage.")

    with evaluation_tab:
        st.subheader("What a defensible evaluation should report")
        evaluation = pd.DataFrame([
            {"Module": "Demand forecasting", "Comparison": "Naïve / seasonal-naïve baseline vs candidate model", "Measures": "MAE, RMSE, defined percentage metric; chronological holdout or rolling-origin validation"},
            {"Module": "Route planning", "Comparison": "Operational or shortest-distance route under equivalent constraints", "Measures": "Distance, fuel/energy, kg CO₂e, cost and service feasibility; vehicle and load assumptions"},
            {"Module": "Supplier assessment", "Comparison": "Documented criteria and weights; independent outcomes if available", "Measures": "Data completeness, sensitivity and bias; no accuracy score without ground truth"},
            {"Module": "Warehouse operations", "Comparison": "Current energy/throughput case vs specified intervention scenario", "Measures": "kWh, kg CO₂e, throughput, boundary, factor source, period and uncertainty"},
            {"Module": "Integrated scenario", "Comparison": "Same demand/service assumptions with carbon-aware decisions on vs off", "Measures": "Carbon, cost, service, assumptions, sensitivity and trade-offs"},
        ])
        st.dataframe(evaluation, width="stretch", hide_index=True)
        with st.expander("Carbon-factor reporting checklist"):
            st.markdown(
                "- State activity data and functional unit (for example, vehicle-km, litres, tonne-km or kWh).\n"
                "- Define organizational, product and time boundaries.\n"
                "- Cite each factor’s source/version, geography, year, gas coverage and unit.\n"
                "- Explain allocation and uncertainty; convert consistently to kg CO₂e."
            )

    with evidence_tab:
        st.subheader("Reference and evidence audit")
        st.markdown(
            "- The work summary says **six papers** were analyzed but does not list title, authors, year, venue or DOI.\n"
            "- The literature-review PDF names concepts such as the GHG Protocol, LCA, IoT and blockchain but has no in-text citations or reference list.\n"
            "- The previous prototype page contained named papers, model scores and company case studies that are not supported by the supplied documents; they have not been carried forward as evidence.\n"
            "- Add full references and connect every claim to its source before formal review. If calling the work systematic, document databases, search dates and inclusion criteria."
        )
        st.subheader("Current scope")
        scope = pd.DataFrame([
            {"Supported by the archive": "Literature synthesis; exploratory software modules; a proposed integrated direction."},
            {"Not established": "Validated reduction percentages; industry-wide accuracy; independently verified cases; complete value-chain inventory; compliance-ready carbon accounting."},
        ])
        st.dataframe(scope, width="stretch", hide_index=True)
        st.caption("The prototype’s emission factors mix functional units and several lack a traceable source, geography, period or boundary. Audit them before quantitative use.")


if __name__ == "__main__":
    main()
