import pandas as pd
from sqlalchemy import create_engine
import logging
from scripts import logging_config


def load_data(db_path, df):
    conn = None
    try:
        engine = create_engine(db_path)
        conn = engine.connect()
        logging.info("Loading data into database")
        df.to_sql("sales", conn, if_exists="append", index=False)
        logging.info("Data loaded successfully")
    except Exception as e:
        logging.error(f"Load error: {e}")
    finally:
        if conn is not None:
            conn.close()
