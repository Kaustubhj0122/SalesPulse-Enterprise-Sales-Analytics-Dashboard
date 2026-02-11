from sqlalchemy import create_engine

engine = create_engine("sqlite:///salespulse.db", echo=False)
