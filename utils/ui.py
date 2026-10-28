from pathlib import Path

import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parents[1]


@st.cache_data(show_spinner=False)
def _load_css() -> str:
    """Read the shared stylesheet once per app session instead of on every rerun."""
    css_path = PROJECT_ROOT / "assets" / "style.css"
    return css_path.read_text(encoding="utf-8") if css_path.exists() else ""


def apply_theme(show_notice: bool = True) -> None:
    """Apply the shared visual system and a consistent prototype-status note."""
    css = _load_css()
    if css:
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

    if show_notice:
        st.markdown(
            '<div class="prototype-ribbon"><span class="status-dot"></span>'
            '<strong>Research prototype</strong><span>Operational demo data are synthetic; public benchmarks are labeled where used.</span></div>',
            unsafe_allow_html=True,
        )


def page_header(kicker: str, title: str, description: str) -> None:
    """Render a consistent editorial page heading."""
    st.markdown(
        f'<div class="page-heading"><div class="eyebrow">{kicker}</div>'
        f'<h1>{title}</h1><p>{description}</p></div>',
        unsafe_allow_html=True,
    )


def section_label(number: str, title: str, subtitle=None) -> None:
    """Render a numbered section heading for the research narrative."""
    extra = f'<p>{subtitle}</p>' if subtitle else ""
    st.markdown(
        f'<div class="section-label"><span>{number}</span><div><h2>{title}</h2>{extra}</div></div>',
        unsafe_allow_html=True,
    )
