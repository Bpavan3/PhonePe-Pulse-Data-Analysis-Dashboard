# PhonePe Pulse Data Analysis Dashboard

An end-to-end analytics project using the PhonePe Pulse dataset — ETL to MySQL + interactive Streamlit dashboard.

## Features
- ETL: JSON → Pandas → **MySQL**
- Analytical SQL (state/district/type/brands)
- Streamlit pages: **Overview**, **Top Insights**, **Users & Brands**, **Map View (bubble, offline)**

## Tech
Python • Pandas • SQLAlchemy • MySQL • Streamlit • Plotly

## Run locally
```bash
git clone https://github.com/Bpavan3/PhonePe-Pulse-Data-Analysis-Dashboard.git
cd PhonePe-Pulse-Data-Analysis-Dashboard
pip install -r requirements.txt
streamlit run Home.py
