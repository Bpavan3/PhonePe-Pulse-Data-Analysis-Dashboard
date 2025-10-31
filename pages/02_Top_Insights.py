import streamlit as st, pandas as pd
from sqlalchemy import create_engine, text

st.title("🏆 Top Insights")
engine = create_engine("mysql+pymysql://root:Mpavan%403377@localhost:3306/phonepe")

years = pd.read_sql("SELECT DISTINCT year FROM aggregated_transaction ORDER BY year", engine)["year"].tolist()
year = st.selectbox("Year", years, index=len(years)-1)
quarter = st.selectbox("Quarter", [1,2,3,4], index=0)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.subheader("Top 10 States by Amount")
    q1 = text("""
      SELECT name AS state, amount
      FROM top_map
      WHERE entity_type='state' AND year=:y AND quarter=:q
      ORDER BY amount DESC
      LIMIT 10
    """)
    df_states = pd.read_sql(q1, engine, params={"y": int(year), "q": int(quarter)})
    st.dataframe(df_states, use_container_width=True)
    if not df_states.empty:
        st.bar_chart(df_states.set_index("state")["amount"])
    else:
        st.info("No data for the selected period.")

with col2:
    st.subheader("Top 10 Districts by Registered Users")
    q2 = text("""
      SELECT state, name AS district, registered_users
      FROM top_user
      WHERE year=:y AND quarter=:q
      ORDER BY registered_users DESC
      LIMIT 10
    """)
    df_dist = pd.read_sql(q2, engine, params={"y": int(year), "q": int(quarter)})
    st.dataframe(df_dist, use_container_width=True)
    if not df_dist.empty:
        st.bar_chart(df_dist.set_index("district")["registered_users"])
    else:
        st.info("No data for the selected period.")
