import pandas as pd

def transform_data(df):
    try:
        # Example transformation: Remove rows with missing values
        df.dropna(inplace=True)
        df.drop_duplicates(inplace=True)
        df["bonus"] = df["amount"] * 2  # Example of creating a new column
        print("Data successfully transformed")
        return df
    except Exception as e:
        print(f"An error occurred while transforming data: {e}")
        return None