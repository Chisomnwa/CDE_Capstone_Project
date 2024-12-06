# Importing the necessary libraries

import pandas as pd
import requests
import logging

# getting the data - a test
# url = 'https://restcountries.com/v3.1/all'
# response = requests.get(f"{url}")
# df = pd.DataFrame(response.json())
# print(df.head())

def get_country_data():
    """
    A function that gets the data from the API and extacts the required attributes
    for predictive nalytics
    """
    url = 'https://restcountries.com/v3.1/all'

    response = requests.get(url)
    logging.info("Fetching data... ")

    if response.status_code == 200:
        # Parse JSON response
        data = response.json()

        # Extract the required attributes
        extracted_data = []
        for country in data:
            extracted_data.append({
                "country_name": country.get("name", {}).get("common"),
                "independence": country.get("independent"),
                "un_member": country.get("unMember"),
                "start_of_week": country.get("Start0fWeek"),
                "official_name": country.get("name", {}).get("official"),
                "common_native_name": next(iter(country.get("name", {}).get("nativeName", {}).values()), {}).get("common"),
                "currency_code": next(iter(country.get("currencies", {}).keys()), None),
                "currency_name": next(iter(country.get("currencies", {}).values()), {}).get("name"),
                "currency_symbol": next(iter(country.get("currencies", {}).values()), {}).get("symbol"),
                "country_code": f"{country.get('idd', {}).get('root', '')}{country.get('idd', {}).get('suffixes', [None])[0]}",
                "capital": next(iter(country.get("capital", [None])), None),
                "region": country.get("region"),
                "sub_region": country.get("subregion"),
                "languages": ", ".join(country.get("languages", {}).values()),
                "area": country.get("area"),
                "population": country.get("population"),
                "continents": ", ".join(country.get("country", [])),
            })


        # turn them into  pandas Dataframe
        countries_data = pd.DataFrame(extracted_data)
        logging.info(f"Extracted {countries_data.shape[0]} records and {countries_data.shape[1]} columns.")
        return countries_data
    else:
        logging.error(f"Failed to fetch data, statys code: {response.status_code}")
        return pd.DataFrame()


