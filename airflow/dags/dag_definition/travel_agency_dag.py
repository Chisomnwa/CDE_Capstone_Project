from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from includes.get_data import get_data
from includes.load_data_to_s3 import upload_to_s3
from includes.load_data_to_redshift import write_to_redshift
from datetime import datetime, timedelta

# default_args = {
#     'owner': 'chisom',
#     'depends_on_past': False,
#     'email_on_failure': False,
#     'email_on_retry': False,
#     'retries': 1,
# }

default_args = {
    'owner': 'chisom',
    'start_date': datetime(2024, 12, 5),
    'retries': 2,
    'retry_delay': timedelta(seconds=3),
    'execution_timeout': timedelta(minutes=10),
}


with DAG(
    dag_id="travel_agency",
    default_args=default_args,
    description="A DAG to extract data from an API, store it in S3, and write to Redshift.",
    default_view="graph",
    schedule_interval="@daily",
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:
    
    # Task 1: Extract data
    extract_data = PythonOperator(
        task_id="extract_data",
        python_callable=get_data
    )

    # Task 2: Upload raw data to S3
    upload_raw_data_to_s3 = PythonOperator(
        task_id="upload_to_s3",
        python_callable=upload_to_s3
    )

    # Task 3: Write data to Redshift
    write_data_to_redshift = PythonOperator(
        task_id="write_to_redshift",
        python_callable=write_to_redshift,
        op_args=["extracted_data", "public", "countries_table"]
    )

    # Task dependencies
    extract_data >> upload_raw_data_to_s3 >> write_data_to_redshift
