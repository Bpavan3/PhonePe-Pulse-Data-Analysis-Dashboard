import streamlit as st

st.set_page_config(
    page_title="PhonePe Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("PhonePe Transaction Insights Dashboard")

st.markdown("""
Welcome to the **PhonePe Pulse Data Dashboard**

Use the menu on the left to explore:

- **Overview** – State-wise UPI transactions  
- **Top Insights** – Top states & districts  
- **Users & Brands** – Mobile brand usage trends  
- **Map View** – India UPI heatmap by state  

Enjoy exploring!
""")
