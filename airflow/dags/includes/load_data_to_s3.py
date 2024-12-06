import awswrangler as wr

from get_data import get_data
from aws import session
import logging

# from includes.aws import session
# from includes.get_data import get_data


# def upload_to_s3():
#     """
#     Uploads a pandas dataframe to an s3 bucket using AWS Wrangler.

#     :param data: pandas DataFrame to upload
#     :param bucket_name: Name of the S3 bucket
#     :param file_key: Path/key for the file in the bucket
#     """

#     # creating a variable to save outr extraxted data
#     data = get_data()

#     # Verify that the dataFrame is not empty
#     if data.empty:
#         print("The DataFrame is empty. No data to upload.")
#         return

#     bucket_name = "s3://chisomnwa-bucket"
#     file_key = "raw_data.parquet"

#     # Upload the Dataframe as a Parquet file to s3
#     wr.s3.to_parquet(
#         df=data,
#         path=f"{bucket_name}/{file_key}",
#         index=False,
#         boto3_session=session(),
#         dataset=True,
#         mode='overwrite'
#     )

#     print(f"Data Successfully uploaded to {bucket_name}/{file_key}")



# def upload_to_s3():
#     logging.info("Starting the upload to S3 process.")
#     data = get_data()

#     if data.empty:
#         logging.error("The DataFrame is empty. No data to upload.")
#         return

#     logging.info("Data fetched successfully. Preparing to upload to S3.")

#     bucket_name = "s3://chisomnwa-bucket"
#     file_key = "raw_data.parquet"

#     try:
#         wr.s3.to_parquet(
#             df=data,
#             path=f"{bucket_name}/{file_key}",
#             index=False,
#             boto3_session=session(),
#             dataset=True,
#             mode="overwrite",
#         )
#         logging.info(f"Data successfully uploaded to {bucket_name}/{file_key}")
#     except Exception as e:
#         logging.error(f"Failed to upload to S3: {e}")


data = get_data()
if data.empty:
    print("No data was fetched. Please check the API endpoint or response.")
else:
    print(data.head())  # Display the first few rows to confirm.