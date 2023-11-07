# kayrros-api

## Power CO2 API
This project deploys a simple API using Flask that provides the latest value of Europe's CO2 emissions in megatons (MT) for the power industry. The data is fetched from CarbonWatch.


## Prerequisites

Before getting started, make sure you have the following tools and dependencies installed:

    - Terraform for infrastructure provisioning.
    - Python 3.8 for running the API locally.

## Terraform Configuration

1) Create an Elastic Beanstalk application
2) Configure the application to use Python 3.8 and the Flask web framework
3) Upload the API code to the application
4) Launch the application

## Running the API Locally

Run the API locally for testing

The API will be accessible at http://127.0.0.1:5000/power/europe.

## API Endpoint

    Endpoint: /power/europe
    HTTP Method: GET
    Description: Returns the latest value of Europe's CO2 emissions in megatons (MT) for the power industry.

## Author
KRAIM Abdellah
