# Import libraries and packages

import pandas as pd
import awswrangler as wr

from airflow.models import Variable

from transformed_data import get_country_data

def write_to_redshif(data: pd.DataFrame, schema: str, table_name: str):
    """
    Write a Pandas DataFrame to Amazon Redshift.

    :param data: Pandas DataFrame containing the data to upload
    :param schema: Schema in Redshift
    :param table:name: Table name in Redshift
    """

    data = get_country_data()
    # Verify that the DataFrame is not empty
    if data.empty:
        print("The DataFrame is empty. No data to write to Redshift.")
        return
    
    # Redshift connection parameters
    redshift_cluster = Variable.get("redshift_cluster") # Replace with your Redshift cluster info
    redshift_database = Variable.get("redshift_database")
    redshift_user = Variable.get("redshift_user")
    redshift_password = Variable.get("redshift_password")
    redshift_role = Variable.get("redshift_role")

    # Connect to Redsgift and load data
    wr.redshift.to_sql(
        df=data,
        schema=schema,
        table=table_name,
        con=wr.redshift.get_cpnnection(
            cluster_id=redshift_cluster,
            database=redshift_database,
            user=redshift_user,
            password=redshift_password,
            role=redshift_role 
        ),
        mode="overwrite",
        index=False
    )
    print(f"Data successfully written to Redshift table {schema}.{table_name}")
    
