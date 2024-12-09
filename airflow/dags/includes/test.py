import requests
import pandas as pd
import logging

def get_data():
    """
    A function that gets the data from the api and then 
    turns the extracted data into a Pandas DataFrame
    """
    url = 'https://rickandmortyapi.com/api/character'
    
    response = requests.get(url)
    logging.info("fetching data...")
    #return response

    if response.status_code == 200:
        # Parse JSON response
        data = response.json()['info']
        profiles_data = pd.DataFrame(data)
        logging.info(f"Data turned into a Dataframe with {profiles_data.shape[0]}\
        , records and {profiles_data.shape[1]} columns")
        return profiles_data
    
print(get_data())