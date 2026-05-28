import requests
import pandas as pd
import logging
from scripts import logging_config


def extract_api_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()
        df = pd.DataFrame(data)
        logging.info(f"Data successfully extracted from API at {api_url}")
        return df
    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred while extracting data from API: {e}")
        return None
