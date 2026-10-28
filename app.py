import streamlit as st

from utils.ui import apply_theme


st.set_page_config(
    page_title="CarbonShift | UROP workspace",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_theme(show_notice=False)

pages = {
    "Workspace": [
        st.Page("pages/Project_Overview.py", title="Project overview", icon=":material/home:", default=True),
        st.Page("pages/Research.py", title="Research review", icon=":material/article:"),
        st.Page("pages/Dashboard.py", title="India grid emissions", icon=":material/bolt:"),
    ],
    "Analysis tools": [
        st.Page("pages/Demand_Forecasting.py", title="Demand forecasting", icon=":material/trending_up:"),
        st.Page("pages/Router_Optimizer.py", title="Route optimizer", icon=":material/local_shipping:"),
        st.Page("pages/Supplier_Scoring.py", title="Supplier scoring", icon=":material/factory:"),
        st.Page("pages/Warehouse_Management.py", title="Warehouse management", icon=":material/warehouse:"),
    ],
    "Data": [
        st.Page("pages/Data_Download.py", title="Sample data", icon=":material/download:"),
    ],
}

navigation = st.navigation(pages, position="sidebar")
navigation.run()
