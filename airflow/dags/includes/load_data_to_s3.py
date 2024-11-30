# Import the necesary LIbraries and Packages
import pandas as pd
import awswrangler as wr
import boto3


def load_data_to_s3():
    """
    This function loads data into Amazon s3
    
    """
    session = boto3.Session(
        aws_access_key_id=Variable.get('access_key')
    )


    session = boto3.Session(
        aws_access_key_id=Variable.get('access_key'),
        aws_secret_access_key=Variable.get('secret_key'),
        region_name='eu-central-1'
    ) # A session stores your configuration state and allows you 
      # to create  service clients and resources. innit?