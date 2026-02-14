# SalesPulse-Enterprise-Sales-Analytics-Dashboard
SalesPulse is an enterprise-style sales analytics dashboard built using Streamlit and MySQL. 
It ingests raw CSV data into a relational database, performs KPI analysis using Pandas, and visualizes insights through an interactive dashboard.
The project simulates a real-world analytics pipeline from data storage to business decision-making.


# SalesPulse is an end-to-end Enterprise Sales Analytics Dashboard built using:
- Python
- Streamlit
- Pandas & NumPy
- Plotly
- SQLite (Database Integration)
- SQLAlchemy (ORM)

# Problem Statement:- 
Business stakeholders often struggle to derive actionable insights from raw sales data stored in Excel files. 
While analysts perform ad-hoc analysis locally, there is no centralized analytics system that:

- Processes standardized sales data
- Stores computed metrics persistently
- Exposes insights via APIs
- Presents KPIs through an interactive dashboard

This project aims to bridge the gap between data analysis and production analytics systems.


# Project Objective

The objective of SalesPulse is to build an enterprise-style analytics pipeline that:

- Cleans and standardizes raw sales data
- Stores structured data in a relational database
- Computes business-critical KPIs
- Visualizes performance trends using an interactive dashboard
- Enables data-driven strategic decisions

 # Key KPIs Delivered
 
 **1) Revenue KPIs**
- Total Sales Revenue
- Monthly Sales Trend

**2)  Profitability KPIs**
- Total Profit
- Region-wise Profit Performance

**3) Product Performance KPIs**
- Sales by Product Category
- Category Contribution %
- Top Performing Categories

# Architecture:-

Excel Dataset
↓
Data Cleaning & Transformation (Pandas)
↓
SQLite Database Storage (SQLAlchemy ORM)
↓
KPI Computation
↓
Streamlit Dashboard
↓
Interactive Plotly Visualizations

