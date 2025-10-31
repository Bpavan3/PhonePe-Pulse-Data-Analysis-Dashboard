import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

st.title("📍 Overview")

engine = create_engine("mysql+pymysql://root:Mpavan%403377@localhost:3306/phonepe")

years = pd.read_sql("SELECT DISTINCT year FROM aggregated_transaction ORDER BY year", engine)["year"].tolist()
year = st.selectbox("Year", years, index=len(years)-1)
quarter = st.selectbox("Quarter", [1,2,3,4], index=0)

q = text("""
SELECT state, SUM(txn_amount) AS total_amount, SUM(txn_count) AS total_count
FROM aggregated_transaction
WHERE year=:y AND quarter=:q
GROUP BY state
ORDER BY total_amount DESC
""")
df = pd.read_sql(q, engine, params={"y": int(year), "q": int(quarter)})

st.subheader(f"State-wise Transactions ({year} Q{quarter})")
st.dataframe(df, use_container_width=True)
if not df.empty:
    st.bar_chart(df.set_index("state")["total_amount"])
else:
    st.info("No data for the selected period.")
