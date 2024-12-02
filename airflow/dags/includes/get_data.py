import requests
import pandas as pd
import logging

# def get_data():
#     """
#     A function that gets the data from the api and then 
#     turns the extracted data into a Pandas DataFrame
#     """
#     url = 'https://restcountries.com/v3.1/all'
    
#     response = requests.get(url)
#     logging.info("fetching data...")

#     if response.status_code == 200:
#         # Parse JSON response
#         data = response.json()
#     profiles_data = pd.DataFrame(data)
#     logging.info(f"Data turned into a Dataframe with {profiles_data.shape[0]}\
#     , records and {profiles_data.shape[1]} columns")
#     return data

# print(get_data())


# def get_data():
#     """
#     A function that gets the data from the API and then 
#     turns the extracted data into a Pandas DataFrame.
#     """
#     url = 'https://restcountries.com/v3.1/all'

#     logging.info("Fetching data...")

#     # Use with context manager to handle response
#     with requests.get(url) as response:
#         if response.status_code == 200:
#             # Parse JSON response
#             data = response.json()
#             profiles_data = pd.DataFrame(data)
#             logging.info(f"Data turned into a DataFrame with {profiles_data.shape[0]} records and {profiles_data.shape[1]} columns")
#             return profiles_data
#         else:
#             logging.error(f"Failed to fetch data: {response.status_code}")
#             return None

# print(get_data())

# response = requests.get('https://ll.thespacedevs.com/2.0.0/launch/upcoming/')
# print(response.json())

# response = requests.get('https://restcountries.com/v2/all')
# print(response.json())

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get("https://restcountries.com/v3.1/all", headers=headers)

if response.status_code == 200:
    print(response.json()[:2])  # Prints first two countries for brevity
else:
    print(f"Failed with status code: {response.status_code}")



