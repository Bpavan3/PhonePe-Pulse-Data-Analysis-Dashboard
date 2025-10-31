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

##  Background & Business Context

The digital payments landscape in India is undergoing a rapid transformation. As per the joint report by Boston Consulting Group (BCG) and PhonePe, India’s digital payments market is expected to grow from approximately **US $3 trillion** today to as much as **US $10 trillion** by 2026, making up about 65 % of all payments by value. :contentReference[oaicite:2]{index=2}

PhonePe launched the “Pulse” open-data initiative to democratize access to aggregated transaction, user and map-level data—enabling developers, analysts and businesses to explore payment trends throughout India. :contentReference[oaicite:4]{index=4}

###  Why This Project Matters

- **Regional insights:** While Tier-1 cities in India are relatively saturated, the largest growth potential lies in Tier-3 to Tier-6 geographies (which contributed to 60-70 % of new digital payment users recently). :contentReference[oaicite:5]{index=5}  
- **Merchant payment digitization:** The number of offline merchants accepting QR-code payments is rising dramatically, fueling growth in merchant and person-to-merchant (P2M) segments.  
- **Embedded finance opportunity:** As payments become ubiquitous, platforms like PhonePe are increasingly moving into adjacent services (investments, insurance, credit) — creating a “payments-plus-finance” ecosystem.  
- **Data-driven decision-making:** Granular datasets from projects like Pulse allow businesses, policy-makers and fintechs to identify underserved areas, plan campaigns and measure impact.

###  How the Project Leverages This Context

This project uses the Pulse dataset to build a full-stack analytics solution:
- Extracting and storing large-scale payments data  
- Building relational models for state, district and brand analysis  
- Visualizing key trends through interactive dashboards (Overview, Top Insights, Users & Brands, Map View)  
- Making insights accessible for business strategy, operations and growth planning  


