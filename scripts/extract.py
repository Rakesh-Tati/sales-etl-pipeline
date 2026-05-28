from datetime import date
import pandas as pd
import logging
from scripts import logging_config


def extract_data(file_path):

    try:
        data = pd.read_csv(file_path)
        data["updated_at"] = pd.to_datetime(data["updated_at"])
        logging.info("Data extracted from CSV file")

        with open("watermark.txt", "r") as f:
            last_watermark = f.read().strip()
        last_watermark_date = pd.to_datetime(last_watermark)

        incremental_data = data[data["updated_at"] > last_watermark_date]
        if incremental_data.empty:
            logging.info("No new records found")
            return None

        logging.info("Incremental data extracted successfully")
        return incremental_data
    except Exception as e:
        logging.error(f"Extraction error: {e}")
        return None
