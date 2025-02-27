# This is the Dockerfile for the the image build during the CI/CD process

# Use Python base Image
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy the necessary files from tthe current directory into /app in the container
COPY travel_agency_app.py /app
COPY app_requirements.txt /app/

# Installl the needed packages specified in the requirements.txt file
RUN pip install --no-cache-dir -r app_requirements.txt

# Set the environment variable for AWS region (optional but good practice)
ENV AWS_DEFAULT_REGION=af-south-1

# Make port 80 available to the world outside this container )if nneeded)
EXPOSE 8080

# Run upload_to_s3.py when the container launches
CMD ["python", "travel_agency_app.py"] 