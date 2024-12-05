import requests
import pandas as pd
import logging

def get_data():
    """
    A function that gets the data from the api and then 
    turns the extracted data into a Pandas DataFrame
    """
    url = 'https://restcountries.com/v3.1/all'
    
    response = requests.get(url)
    logging.info("fetching data...")

    if response.status_code == 200:
        # Parse JSON response
        data = response.json()
        profiles_data = pd.DataFrame(data)
        logging.info(f"Data turned into a Dataframe with {profiles_data.shape[0]}\
        , records and {profiles_data.shape[1]} columns")
        return profiles_data
    else:
        logging.error(f"Failed to fetch data. Status code: {response.status_code}")
        return data

# Print the data or DataFrame
# data_frame = get_data()
# if data_frame is not None:
#     print(data_frame.head())  # Display the first few rows of the DataFrame



