import pandas as pd
import logging
from scripts import logging_config


def transform_data(df):
    try:
        logging.info("Transformation started")

        df.dropna(inplace=True)
        logging.info("null values removed")

        df.drop_duplicates(inplace=True)
        logging.info("Duplicates removed")

        df["bonus"] = df["amount"] * 1.10 # Add a bonus column with a 10% increase
        logging.info("Bonus column created")

        logging.info("Transformation completed successfully")
        return df
    except Exception as e:
        logging.error(f"Transformation error: {e}")
        return None
