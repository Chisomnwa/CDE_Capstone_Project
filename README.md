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

Having carefully assessed the requirements, **Docker** was used to host **Airflow*, which served as the orchestration tool for this project. 
The dataset was extracted from the Country REST API and stored in Parquet format in **Amazon S3**  to ensure future extensibility. 
Relevant columns were then selected from the raw data and loaded into a **Redshift**  table,
which functioned as the Data Warehouse. **dbt** was utilized to model the transformed data into `Fact` and `Dimension tables`, enabling efficient querying. 
Additionally, **Terraform** was employed as an Infrastructure as Code (IaC) tool to provision all necessary AWS resources.

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


## Tools and Services Used and their Functions

* **Terraform**: To avoid manually creating the resources which was used for this project, Terraform was used for Infrastructure as Code (IaC) to provision and manage cloud resources like AWS S3, Redshift, IAM roles, and VPC. This ensures scalability, consistency, and reproducibility in infrastructure deployment.

* **Docker**: Docker was used to containerize Airflow by building from an Apache Airflow Image found [here](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html). A `Dockerfile` and a `requirement.txt` file were used to enhance the base image provided by Airflow to include `awswrangler` package.

* **Airflow**: Airflow which is an open-source technology was used as an orchestration tool to automate and manage the ETL pipeline. It had dag dependencies on the worker nodes set up to trigger at a scheduled interval which can be accesses on the web server GUI.

* **AWS Service**: Because of its accessibility and compatibility with terraform, and ease of use, AWS cloud was chosen as the preferred cloud provider. An IAM with the necessary policies (using the principle of least-privilege) was provisoned and was used by Airflow for accessing the Data Lake (s3 bucket) and Data Warehouse (Redshift), using the access keys and secret access key parameters saved in the SSM parameter store. 

    Under AWS Services also, **Amazon ECR** was used to store the Docker image, which contains the codes for extracting the data from the API and uploading the raw data to the s3 bucket Data Lake.

* **dbt**: which stands for Data Build Tool was utilized for transforming the raw data and modeling it into Fact and Dimension tables in Redshift. It also helps to ensure data quality, modularity, and version control, making it easier to mantain analytics-ready datasets.

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


# Power Point presentation
To have a view of the project's data architecture and understand the ***Why** for the choice of tools 🛠️,
you can access the power point slides [here](https://github.com/Chisomnwa/CDE_Capstone_Project/blob/main/Travel_Agency_Project_Slides.pdf).

