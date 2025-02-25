# CDE CAPSTONE PROJECT - Travel Agency Data Platform

## Introduction
In response to the **CDE cohort-1** capstone project requirement, I created this project which integrates all the key concepts and tools learned during the Bootcamp program.

The project demonstrates the development of a robust Data Platform capable of ingesting, transforming, and storing data for predictive analytics. The tools and services utilized in this project includes `Docker`, `Airflow`, `Terraform`, `AWS Services` (like Amazon s3. Redshift, ECR), and `dbt`.

## Overview

The goal of this project is to build a scalable and efficient data pipeline for a travel agency, enabling their Data Science team to analyze curated data for predictive analytics. The pipeline is designed to:

* Extract raw data from the Country [REST API](https://restcountries.com/v3.1/all).

* Load the data into an AWS S3 Data Lake in Parquet format.

* Transform the data into a curated dataset containing specific fields relevant for analysis.

* Load the transformed data into Amazon Redshift table.

* Use dbt to model the data into Fact and Dimension tables for efficient querying.

* incorporate CI/CD pipelines to automate code quality checks, build processes, and deployments, ensuring best practices and streamlined workflows.


## Methodology

Now, to the methodoly used to complete this project.

* **Docker** was used to host **Airflow**, which is the orchestration tool used in this project.

* The entire dataset was extacted from the Country REST API and stored in parquet format in **Amazon S3** for future extensibility.

* The revelant columns were extracted from the raw data and loaded into a **Redshift** table whci was used as the Data Warehouse/Database.

* **dbt** was used to model the transformed dta into Fact and Dimension tables.

* **Terraform** was used as an Infrastructure as Code to provision all the resources used in AWS.

## Project Architecture
### Overview
The data pipeline is designed to seamlessly integrate data ingestion, transformation, and storage. Below is a high-level description of the architecture:

* **Data Ingestion**: Data is stored in Amazon S3 bucket.

* **Infrastructure Setup**: Terraform provisions the AWS VPC, IAM roles, Redshift clusters, and other necessary resources.

* **ETL Orchestration**: Apache Airflow orchestrates the ETL process, including loading data into Redshift and triggering dbt models.

* **Data Transformation**: dbt structures raw data into analytics-ready formats.

* **Output**: Transformed data is stored in Redshift and can be accessed by BI tools or queried directly.

## Architectural Diagram

![image](https://github.com/Chisomnwa/CDE_Capstone_Project/blob/main/Travel%20Agency%20Platform%20Architecture.png)

![piggy_bank](piggy_bank.jpg)

