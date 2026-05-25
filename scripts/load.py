import pandas as pd
from sqlalchemy import create_engine

def load_data(db_path, df):
    conn = None
    try:
        engine = create_engine(db_path)
        conn = engine.connect()
        df.to_sql("sales_data", conn, if_exists="replace", index=False)
        print(f"Data successfully loaded into database at {db_path}")
    except Exception as e:
        print(f"An error occurred while loading data: {e}")
    finally:
        if conn is not None:
            conn.close()