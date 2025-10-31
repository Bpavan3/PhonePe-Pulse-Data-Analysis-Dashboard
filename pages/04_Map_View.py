# pages/04_Map_View.py — Bubble map version (no GeoJSON needed)

import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
import plotly.express as px

st.title(" India Bubble Map — UPI Transactions by State (No GeoJSON)")

ENGINE = create_engine("mysql+pymysql://root:Mpavan%403377@localhost:3306/phonepe")

# ---- Year/Quarter filters ----
years = pd.read_sql("SELECT DISTINCT year FROM aggregated_transaction ORDER BY year", ENGINE)["year"].tolist()
if not years:
    st.error("No data found in aggregated_transaction.")
    st.stop()

year = st.selectbox("Year", years, index=len(years)-1)
quarter = st.selectbox("Quarter", [1,2,3,4], index=0)

# ---- Pull state totals ----
q = text("""
SELECT state, SUM(txn_amount) AS total_amount
FROM aggregated_transaction
WHERE year=:y AND quarter=:q
GROUP BY state;
""")
df = pd.read_sql(q, ENGINE, params={"y": int(year), "q": int(quarter)})

if df.empty:
    st.info("No data for the selected period.")
    st.stop()

# ---- Normalize names to Title Case ----
df["state"] = df["state"].str.title()
df = df.replace({
    "Andaman & Nicobar Islands": "Andaman & Nicobar Island",
    "Nct Of Delhi": "Delhi",
    "Dadra & Nagar Haveli & Daman & Diu": "Dadra and Nagar Haveli and Daman and Diu"
})

# ---- State centroids (approx) for bubble placement ----
centroids = {
    "Andaman & Nicobar Island": (11.7401, 92.6586),
    "Andhra Pradesh": (15.9129, 79.7400),
    "Arunachal Pradesh": (28.2180, 94.7278),
    "Assam": (26.2006, 92.9376),
    "Bihar": (25.0961, 85.3131),
    "Chandigarh": (30.7333, 76.7794),
    "Chhattisgarh": (21.2787, 81.8661),
    "Dadra And Nagar Haveli And Daman And Diu": (20.3974, 72.8328),
    "Delhi": (28.6139, 77.2090),
    "Goa": (15.2993, 74.1240),
    "Gujarat": (22.2587, 71.1924),
    "Haryana": (29.0588, 76.0856),
    "Himachal Pradesh": (31.1048, 77.1734),
    "Jammu & Kashmir": (33.7782, 76.5762),
    "Jharkhand": (23.6102, 85.2799),
    "Karnataka": (15.3173, 75.7139),
    "Kerala": (10.8505, 76.2711),
    "Ladakh": (34.1526, 77.5770),
    "Lakshadweep": (10.5667, 72.6417),
    "Madhya Pradesh": (22.9734, 78.6569),
    "Maharashtra": (19.7515, 75.7139),
    "Manipur": (24.6637, 93.9063),
    "Meghalaya": (25.4670, 91.3662),
    "Mizoram": (23.1645, 92.9376),
    "Nagaland": (26.1584, 94.5624),
    "Odisha": (20.9517, 85.0985),
    "Puducherry": (11.9416, 79.8083),
    "Punjab": (31.1471, 75.3412),
    "Rajasthan": (27.0238, 74.2179),
    "Sikkim": (27.5330, 88.5122),
    "Tamil Nadu": (11.1271, 78.6569),
    "Telangana": (18.1124, 79.0193),
    "Tripura": (23.9408, 91.9882),
    "Uttar Pradesh": (26.8467, 80.9462),
    "Uttarakhand": (30.0668, 79.0193),
    "West Bengal": (22.9868, 87.8550),
    "Andaman And Nicobar Islands": (11.7401, 92.6586),  # extra alias
}

# ---- Attach lat/lon to each row; drop states without a centroid ----
df["lat"] = df["state"].map(lambda s: centroids.get(s, (None, None))[0])
df["lon"] = df["state"].map(lambda s: centroids.get(s, (None, None))[1])
df = df.dropna(subset=["lat", "lon"])

st.subheader(f"State totals — {year} Q{quarter}")
st.dataframe(df[["state","total_amount"]].sort_values("total_amount", ascending=False),
             use_container_width=True)

# ---- Bubble map ----
fig = px.scatter_geo(
    df,
    lat="lat",
    lon="lon",
    hover_name="state",
    size="total_amount",
    size_max=40,
    projection="natural earth",
    title=f"UPI Transaction Amount — {year} Q{quarter} (bubble size = amount)"
)

# Focus on India region
fig.update_geos(
    lataxis_showgrid=True, lonaxis_showgrid=True,
    center=dict(lat=22.0, lon=79.0),  # India center-ish
    projection_scale=3.2                # zoom
)

st.plotly_chart(fig, use_container_width=True)
