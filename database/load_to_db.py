from app_files.data_processing import load_data
from database.db_connection import engine

def load_excel_to_db():
    df = load_data()
    df.to_sql("sales_data", con=engine, if_exists="replace", index=False)

if __name__ == "__main__":
    load_excel_to_db()