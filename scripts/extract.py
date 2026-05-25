import pandas as pd

def extract_data(file_path):
    
    try:
        data = pd.read_csv(file_path)
        print(f"Data successfully extracted from {file_path}")
        return data
    except Exception as e:
        print(f"An error occurred while extracting data: {e}")
        return None