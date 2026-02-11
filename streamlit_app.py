import streamlit as st
import pandas as pd
import plotly.express as px
from database.db_connection import engine
from app_files.data_processing import compute_kpis

st.set_page_config("SalesPulse Dashboard", layout="wide")

st.title("SalesPulse -> Sales Analytics Dashboard")

def fetch_sales_data():
    query = "SELECT * FROM sales_data"
    return pd.read_sql(query, engine)

df = fetch_sales_data()

total_sales, total_profit, avg_order_value, monthly_sales, category_sales, region_sales = compute_kpis(df)

# KPI CARDS
col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Total Profit", f"${total_profit:,.0f}")
col3.metric("Avg Order Value", f"${avg_order_value:,.2f}")

st.divider()

# LINE CHART – Monthly Sales
fig1 = px.line(
    monthly_sales,
    x="YearMonth",   
    y="Sales",
    title="Monthly Sales Trend"
)
st.plotly_chart(fig1, width="stretch")

# PIE CHART – Category Sales
fig2 = px.pie(
    category_sales,
    names="Category",
    values="Sales",
    title="Sales Distribution by Category"
)
st.plotly_chart(fig2, width="stretch")

# BAR CHART – Region Sales
fig3 = px.bar(
    region_sales,
    x="Region",
    y="Sales",
    title="Sales by Region"
)
st.plotly_chart(fig3, width="stretch")
