import pandas
import logging
from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data

logging.basicConfig(level=logging.INFO, filename="logs/pipeline.log")
logging.info("Starting ETL pipeline")

try:
    # Step 1: Extract data
    df = extract_data("data/raw/sales.csv")

    if df is not None and not df.empty:
        # Step 2: Transform data
        transformed_data = transform_data(df)
        transformed_data.to_csv(
            "data/processed/processed_sales.csv", index=False
        )  # Save transformed data to CSV
        transformed_data.to_json(
            "data/processed/processed_sales.json",
            orient="records",
            lines=True,
            date_format="iso",
        )  # Save transformed data to JSON

        if transformed_data is not None and not transformed_data.empty:
            # Step 3: Load data into database
            load_data("sqlite:///sales.db", transformed_data)
            latest_date = transformed_data["updated_at"].max()
            with open("watermark.txt", "w") as f:
                f.write(str(latest_date.date()))
            logging.info("Pipeline completed successfully")
except Exception as e:
    logging.error(f"An error occurred in the main process: {e}")
