import pandas as pd

EXCEL_PATH = "data/Superstore_data.xlsx"

def load_data():
    df = pd.read_excel(EXCEL_PATH,engine="openpyxl")
    

    # VERY IMPORTANT (fixes hidden Excel issues)
    df.columns = df.columns.str.strip()

    # Force datetime conversion
    df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    errors="coerce"
    )
    print(df["Order Date"].head(30))
    return df


def compute_kpis(df):

    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    # Drop rows where Order Date failed to parse
    df = df.dropna(subset=["Order Date"])

    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    avg_order_value = df["Sales"].mean()

    
    #  More stable way (without .dt.to_period)
    df["YearMonth"] = df["Order Date"].dt.strftime("%Y-%m")

    monthly_sales = (
        df.groupby("YearMonth")["Sales"]
        .sum()
        .reset_index()
    )
    #monthly_sales["Order Date"] = monthly_sales["Order Date"].astype(str)

    category_sales = df.groupby("Category")["Sales"].sum().reset_index()
    region_sales = df.groupby("Region")["Sales"].sum().reset_index()

    return (
        total_sales,
        total_profit,
        avg_order_value,
        monthly_sales,
        category_sales,
        region_sales,
    )

#df=load_data()
#compute_kpis(df)