from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data 

try:
    # Step 1: Extract data
    df = extract_data("data/raw/sales.csv")
    
    if df is not None and not df.empty:
        # Step 2: Transform data
        transformed_data = transform_data(df)
        transformed_data.to_csv("data/processed/transformed_data.csv", index=False)  # Save transformed data to CSV
        transformed_data.to_json("data/processed/transformed_data.json", orient="records", lines=True)  # Save transformed data to JSON
        
        if transformed_data is not None and not transformed_data.empty:
            # Step 3: Load data into database
            load_data("postgresql://postgres:sql%40123@localhost:5432/sales", transformed_data)
            print("Pipeline completed successfully")
except Exception as e:
    print(f"An error occurred in the main process: {e}")