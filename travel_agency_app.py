# THIS CONTAINS:

# A: Code that extracts the data ffrom the API
# B: Code that loads the raw data to s3

# THis is the part of the fulfillment of the C/CD implementation where this app will be built as an image using a dockerfile

# Retrieving data from the API
# Import libraries and packages
import requests
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(message)')

def get_data():
    """
        A function that  extracts the data from the API
        and then turns it  into a pandas DataFrame
    """

    url = "https://restcountries.com/v3.1/all"

    response = requests.get(url)
    logging.info("Fetching data from the API...")

    if response.status_code == 200:
        # Parse JSON response
        data = response.json()

        # Convert JSON data to Pandas DataFrame
        profiles_data = pd.DataFrame(data)
        logging.info(f"Successfuly turned into a Pandas DataFrame\
                     {profiles_data.shape[0]} records and {profiles_data.shape[1]} columns")
        return profiles_data
    
print(get_data())


###############################################################################
# Creating a connection to connect to AWS
# Import necessary libraries and packages
import boto3
from airflow.models import Variable

def create_session():
    """Initialize and return a Boto3 session using Airflow variables."""
    aws_access_key_id = Variable.get("aws_access_key_id")
    aws_secret_access_key = Variable.get("aws_secret_access_key")
    region_name = "af-south-1"

    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region_name
    )

    return session

print(create_session())


###############################################################################
# Loading the raw data into an s3 bucket
from io import BytesIO

def upload_to_s3():
    """
        Uploading data into an s3 bucket with a fixed file name
    """
    data = get_data()

    if data.empty:
        print('DataFrame is empty. No data to return')
        return
    
    bucket_name = 'travel-agency-bucket'
    file_key = 'raw_data/data.parquet'

    # Convert DataFrame to bytes
    buffer = BytesIO()
    data.to_parquet(buffer, index=False)
    buffer.seek(0)

    # upload file to s3
    s3_client = create_session().client('s3')
    s3_client.put_object(bucket_name, file_key, Body=buffer.getvalue())

    print(f"Data successfully uploaded to s3://{bucket_name}/{file_key}")

upload_to_s3()

