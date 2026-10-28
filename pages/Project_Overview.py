from pathlib import Path

import streamlit as st

from utils.ui import apply_theme


PROJECT_ROOT = Path(__file__).resolve().parents[1]


MODULES = [
    ("pages/Research.py", "Research review", "Evidence, gaps and the evaluation path", "01", "violet"),
    ("pages/Dashboard.py", "India grid emissions", "CEA factors and a transparent kWh calculator", "02", "cyan"),
    ("pages/Demand_Forecasting.py", "Demand forecasting", "Predictive signals for lower overproduction", "03", "amber"),
    ("pages/Router_Optimizer.py", "Route optimizer", "Explore lower-emission delivery routes", "04", "coral"),
    ("pages/Supplier_Scoring.py", "Supplier scoring", "Compare cost, service and carbon criteria", "05", "lime"),
    ("pages/Warehouse_Management.py", "Warehouse management", "Review energy, capacity and efficiency", "06", "blue"),
    ("pages/Data_Download.py", "Sample data", "Preview and download the demo records", "07", "pink"),
]


def main() -> None:
    apply_theme()

    st.markdown(
        """
        <section class="hero-panel">
          <div class="hero-orbit orbit-one"></div>
          <div class="hero-orbit orbit-two"></div>
          <div class="hero-copy">
            <div class="hero-kicker"><span class="pulse-dot"></span> UROP · research workspace</div>
            <h1>Make every supply-chain decision<br><em>visible in carbon.</em></h1>
            <p>CarbonShift connects prediction, operational choices and transparent emissions estimates in one focused workspace.</p>
            <div class="hero-tags"><span>AI-assisted</span><span>Evidence-led</span><span>India-aware</span></div>
          </div>
          <div class="hero-signal" aria-hidden="true">
            <div class="signal-ring ring-a"></div><div class="signal-ring ring-b"></div>
            <div class="signal-core"><strong>CO₂</strong><small>decision layer</small></div>
          </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="prototype-ribbon"><span class="status-dot"></span><strong>Research prototype</strong>'
        '<span>Demo records are synthetic. Public benchmarks are labeled where used.</span></div>',
        unsafe_allow_html=True,
    )

    stats = st.columns(4, gap="small")
    for column, value, label, accent in zip(
        stats,
        ["4", "7", "5", "22.0"],
        ["decision areas", "working modules", "CEA years", "CEA release"],
        ["violet", "cyan", "amber", "lime"],
    ):
        with column:
            st.markdown(f'<div class="stat-card stat-{accent}"><strong>{value}</strong><span>{label}</span></div>', unsafe_allow_html=True)

    left, right = st.columns([1.25, 0.75], gap="large")
    with left:
        st.markdown('<div class="section-kicker">THE NORTH STAR</div>', unsafe_allow_html=True)
        st.markdown('<h2 class="display-heading">From signals to <span>smarter moves.</span></h2>', unsafe_allow_html=True)
        st.markdown(
            '<p class="lead-copy">How can prediction and operational optimization make carbon visible alongside cost and service in supply-chain decisions?</p>',
            unsafe_allow_html=True,
        )
    with right:
        with st.container(border=True):
            st.markdown("**What this workspace is**")
            st.write("A literature review companion and exploratory interface—not a validated emissions-reduction system.")
            st.caption("Evidence status: no empirical carbon-reduction result is validated in the supplied files.")

    st.markdown('<div class="section-kicker module-kicker">EXPLORE THE WORKSPACE</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="display-heading compact">Choose a lens. Follow the signal.</h2>', unsafe_allow_html=True)

    for row_start in range(0, len(MODULES), 2):
        columns = st.columns(2, gap="large")
        for column, (page, label, description, number, accent) in zip(columns, MODULES[row_start:row_start + 2]):
            with column:
                st.markdown(
                    f'<div class="module-card module-{accent}"><div class="module-number">{number}</div>'
                    f'<div><div class="module-title">{label}</div><div class="module-description">{description}</div></div></div>',
                    unsafe_allow_html=True,
                )
                st.page_link(page, label=f"Open {label}")

    with st.expander("Review context and source documents"):
        summary_tab, gap_tab, files_tab = st.tabs(["Literature position", "Evidence gaps", "Documents"])
        with summary_tab:
            st.write(
                "The supplied review discusses carbon accounting and value-chain boundaries, AI for supply-chain operations, and approaches that place emissions explicitly in planning. Its proposed direction connects prediction, operational optimization and transparent carbon reporting."
            )
        with gap_tab:
            st.markdown(
                "- The six reviewed papers are not identified in the work summary.\n"
                "- The literature-review PDF does not include in-text citations or a reference list.\n"
                "- Generated data and model outputs are demonstrations, not evidence of operational impact.\n"
                "- Emission factors need traceable sources, units, geography and boundaries."
            )
        with files_tab:
            report = PROJECT_ROOT / "docs" / "UROP Work Summary Report 1.pdf"
            review = PROJECT_ROOT / "docs" / "literature Review UROP.pdf"
            c1, c2 = st.columns(2)
            with c1:
                if report.exists():
                    st.download_button("Work summary PDF", report.read_bytes(), file_name=report.name, mime="application/pdf")
            with c2:
                if review.exists():
                    st.download_button("Literature review PDF", review.read_bytes(), file_name=review.name, mime="application/pdf")


if __name__ == "__main__":
    main()
