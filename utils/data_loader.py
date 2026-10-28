from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"


@st.cache_data(show_spinner=False)
def load_sample_demand_data() -> pd.DataFrame:
    """Generate reproducible sample demand data for demonstration."""
    rng = np.random.default_rng(42)
    dates = pd.date_range(start="2023-01-01", end="2024-01-01", freq="MS")
    base_demand = [100, 120, 130, 110, 150, 140, 160, 170, 180, 160, 140, 120, 130]
    actual_demand = [d * rng.uniform(0.8, 1.2) for d in base_demand[: len(dates)]]
    forecast_demand = [d * rng.uniform(0.9, 1.1) for d in actual_demand]
    return pd.DataFrame(
        {
            "date": dates,
            "actual_demand": actual_demand,
            "forecast_demand": forecast_demand,
            "product_category": rng.choice(
                ["Electronics", "Clothing", "Food", "Furniture"], len(dates)
            ),
        }
    )


def load_csv_data(source) -> pd.DataFrame:
    """Load an uploaded CSV or project sample; generate a known demo set if absent."""
    if hasattr(source, "read"):
        if hasattr(source, "seek"):
            source.seek(0)
        return pd.read_csv(source)

    file_name = Path(str(source)).name
    data_path = DATA_DIR / file_name
    if data_path.is_file():
        return pd.read_csv(data_path)
    return generate_sample_data(file_name)


@st.cache_data(show_spinner=False)
def generate_sample_data(file_name: str) -> pd.DataFrame:
    """Generate a deterministic sample dataset based on its filename."""
    name = Path(file_name).name.lower()
    if "demand" in name:
        return generate_demand_data()
    if "supplier" in name:
        return generate_supplier_data()
    if "warehouse" in name:
        return generate_warehouse_data()
    if "transport" in name:
        return generate_transportation_data()
    return pd.DataFrame()


@st.cache_data(show_spinner=False)
def generate_demand_data() -> pd.DataFrame:
    """Generate reproducible monthly sample demand data."""
    rng = np.random.default_rng(43)
    dates = pd.date_range(start="2023-01-01", end="2024-06-01", freq="MS")
    products = ["Electronics", "Clothing", "Food", "Furniture"]
    data = []
    for date in dates:
        for product in products:
            base_demand = rng.integers(500, 2000)
            actual_demand = base_demand * rng.uniform(0.8, 1.2)
            forecast_demand = actual_demand * rng.uniform(0.9, 1.1)
            data.append(
                {
                    "date": date.strftime("%Y-%m-%d"),
                    "product_category": product,
                    "actual_demand": int(actual_demand),
                    "forecast_demand": int(forecast_demand),
                    "price": round(rng.uniform(50, 500), 2),
                    "promotion_flag": rng.choice([0, 1], p=[0.7, 0.3]),
                    "seasonality": round(rng.uniform(0.7, 1.3), 2),
                }
            )
    return pd.DataFrame(data)


@st.cache_data(show_spinner=False)
def generate_supplier_data() -> pd.DataFrame:
    """Generate reproducible sample supplier data."""
    rng = np.random.default_rng(44)
    locations = [
        "Germany", "USA", "Canada", "Sweden", "Netherlands", "Denmark",
        "Finland", "France", "Norway", "UK",
    ]
    certifications = ["ISO 14001", "ISO 50001", "B Corp", "None"]
    suppliers = []
    for i in range(1, 16):
        suppliers.append(
            {
                "supplier_id": f"SUP_{i:03d}",
                "name": f"Supplier {i}",
                "location": rng.choice(locations),
                "carbon_footprint": rng.integers(60, 100),
                "energy_efficiency": rng.integers(75, 98),
                "renewable_energy": rng.integers(50, 95),
                "cost_score": rng.integers(75, 95),
                "delivery_reliability": rng.integers(90, 100),
                "certifications": rng.choice(certifications, p=[0.4, 0.2, 0.2, 0.2]),
                "lead_time_days": rng.integers(14, 28),
                "minimum_order": rng.integers(500, 2000),
            }
        )
    return pd.DataFrame(suppliers)


@st.cache_data(show_spinner=False)
def generate_warehouse_data() -> pd.DataFrame:
    """Generate reproducible sample warehouse data."""
    rng = np.random.default_rng(45)
    locations = [
        "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
        "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose",
    ]
    energy_sources = ["Grid", "Mixed", "Solar"]
    warehouses = []
    for i, location in enumerate(locations, 1):
        warehouses.append(
            {
                "warehouse_id": f"WH_{i:03d}",
                "location": location,
                "energy_consumption_kwh": rng.integers(8000, 15000),
                "square_meters": rng.integers(4000, 6000),
                "storage_capacity": rng.integers(8000, 12000),
                "inventory_turnover": round(rng.uniform(7.0, 10.5), 1),
                "energy_source": rng.choice(energy_sources, p=[0.5, 0.3, 0.2]),
                "solar_panels": rng.choice(["Yes", "No"], p=[0.6, 0.4]),
                "avg_temperature": rng.integers(16, 26),
                "operational_hours": rng.choice([12, 16, 24], p=[0.3, 0.4, 0.3]),
            }
        )
    return pd.DataFrame(warehouses)


@st.cache_data(show_spinner=False)
def generate_transportation_data() -> pd.DataFrame:
    """Generate reproducible sample transportation route data."""
    rng = np.random.default_rng(46)
    route_pairs = [
        ("New York", "Los Angeles", 4500),
        ("Chicago", "Houston", 1750),
        ("San Francisco", "Seattle", 1300),
        ("Miami", "Atlanta", 1050),
        ("Denver", "Dallas", 1100),
        ("Boston", "Washington", 650),
        ("New York", "Chicago", 1270),
        ("Los Angeles", "Phoenix", 600),
        ("Seattle", "Portland", 280),
        ("Atlanta", "Nashville", 400),
    ]
    routes = []
    for i, (origin, destination, distance) in enumerate(route_pairs, 1):
        baseline_fuel = distance * 0.3
        optimized_fuel = baseline_fuel * rng.uniform(0.75, 0.90)
        emissions = optimized_fuel * 2.5
        routes.append(
            {
                "route_id": f"R_{i:03d}",
                "origin": origin,
                "destination": destination,
                "distance_km": distance,
                "baseline_fuel_l": int(baseline_fuel),
                "optimized_fuel_l": int(optimized_fuel),
                "emissions_kg_co2": int(emissions),
                "transport_mode": "Truck",
                "typical_duration_hours": max(4, int(distance / 80)),
                "cargo_capacity_kg": 10000,
            }
        )
    return pd.DataFrame(routes)
