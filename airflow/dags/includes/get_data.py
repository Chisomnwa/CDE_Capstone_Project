import requests
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def get_data():
    """
    Fetch data from the API and return as a Pandas DataFrame.
    """
    url = 'https://restcountries.com/v3.1/all'

    try:
        response = requests.get(url)
        logging.info("Fetching data from the API...")

        if response.status_code == 200:
            # Parse JSON response
            data = response.json()

            # Convert JSON data to Pandas DataFrame
            profiles_data = pd.DataFrame(data)
            logging.info(
                f"Data successfully turned into a DataFrame with {profiles_data.shape[0]} records and {profiles_data.shape[1]} columns."
            )
            return profiles_data
        else:
            logging.error(f"Failed to fetch data. Status code: {response.status_code}")
            return None
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return None

# Fetch and display data
if __name__ == "__main__":
    data_frame = get_data()
    if data_frame is not None:
        print(data_frame.head())  # Display the first few rows of the DataFrame
    else:
        print("No data available.")
