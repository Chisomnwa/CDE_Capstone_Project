# CDE Capstone Project

# Introduction
This project automates the deployment of a data pipeline integrating **AWS Redshift** for data storage, **Apache Airflow** for orchestration, and **dbt** for data transformation. Infrastructure provisioning is managed with **Terraform** to ensure scalable and replicable deployments. This pipeline processes raw data from an **S3 bucket**, transforms it using dbt, and stores it in Redshift for downstream analytics.

## Goals:
* Automate infrastructure provisioning.

* Enable efficient ETL workflows using Airflow.

* Provide analytics-ready data in Redshift.

# Project Architecture
## Overview
The data pipeline is designed to seamlessly integrate data ingestion, transformation, and storage. Below is a high-level description of the architecture:

* **Data Ingestion**: Data is stored in Amazon S3 buckets.

* **Infrastructure Setup**: Terraform provisions the AWS VPC, IAM roles, Redshift clusters, and other necessary resources.

* **ETL Orchestration**: Apache Airflow orchestrates the ETL process, including loading data into Redshift and triggering dbt models.

* **Data Transformation**: dbt structures raw data into analytics-ready formats.

* **Output**: Transformed data is stored in Redshift and can be accessed by BI tools or queried directly.

## Architectural Diagram
(Include this diagram once created using a tool like Lucidchart or draw.io.)

# Features
* **Terraform Automation**: Scalable provisioning of AWS infrastructure.

* **Redshift Integration**: Centralized data storage for analytics.

* **Airflow DAGs**: Seamless orchestration of ETL processes.
dbt Models: Efficient data transformation and schema design.

# Setup Instructions
## Prerequisites:
* AWS Account with sufficient IAM permissions.

* Installed tools: Terraform, Apache Airflow, dbt, AWS CLI, Python (with virtualenv).
----

1. Clone the Repository:

        `git clone <repository_url>`

        `cd <repository_directory>`

2.  Configure AWS Credentials:

    Ensure your AWS CLI is configured with the required credentials:

        `aws configure`

3. Infrastructure Provisioning:

    Navigate to the **Architecture directory** and run the following commands:

        `terraform init`
        `terraform fmt`
        `terraform validate`
        `terraform apply`

4. Start Airflow:

    Set up Airflow and deploy the DAGs:

    * cd into the **airflow directory**.

    * Download docker-compose.yaml file using

        `curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.10.3/docker-compose.yaml'`

    * Create your Dockerfile, .env file, and your requirements.txt file.

    * set up your DAG.

    * In the terminal run `docker-compose up -d` to start up your containers.

    * Go to your localhost:8080 to view and run your dag.

    PS: Place the DAG files in the dags folder and configure Airflow connections for Redshift and S3.

5. Run dbt Models:

    Navigate to your dbt project folder and execute:

        `dbt run`

# Challenges and Solutions

* **Challenge 1**: Terraform Variable Errors

    **Solution**: Refactored variable definitions and ensured proper passing of values between modules.

* **Challenge 2**: Airflow Redshift Connection

    **Solution**: Configured Redshift connection settings in Airflow with accurate credentials and endpoint details.

* **Challenge 3**: dbt Execution Errors

    **Solution**: Debugged errors using dbt logs and ensured proper schema configurations in dbt_project.yml.

# Future Improvements
**Monitoring**: Implement AWS CloudWatch for pipeline monitoring and alerting.

**Scaling**: Extend the pipeline to integrate AWS Glue for more complex ETL processes


