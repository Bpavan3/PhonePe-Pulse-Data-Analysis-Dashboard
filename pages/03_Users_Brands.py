import streamlit as st, pandas as pd
from sqlalchemy import create_engine, text

st.title("👥 Users & Brands")
engine = create_engine("mysql+pymysql://root:Mpavan%403377@localhost:3306/phonepe")

years = pd.read_sql("SELECT DISTINCT year FROM aggregated_user ORDER BY year", engine)["year"].tolist()
year = st.selectbox("Year", years, index=len(years)-1)

q = text("""
SELECT user_brand, SUM(user_count) AS users
FROM aggregated_user
WHERE year = :y
GROUP BY user_brand
ORDER BY users DESC
LIMIT 15
""")
df = pd.read_sql(q, engine, params={"y": int(year)})

st.dataframe(df, use_container_width=True)
if not df.empty:
    st.bar_chart(df.set_index("user_brand")["users"])
else:
    st.info("No brand data for selected year.")
