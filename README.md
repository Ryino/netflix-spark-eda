# Netflix Dataset EDA with PySpark

## Project Overview
This project performs Exploratory Data Analysis (EDA) on the Netflix TV Shows & Movies dataset using PySpark.

## Requirements
- Apache Spark
- PySpark
- Python 3.7+

## Setup and Running
1. Ensure Docker is installed
2. Pull Spark Python image: 
   `docker pull apache/spark-py`
3. Run the script:
   `docker run --rm -v $(pwd):/app apache/spark-py spark-submit /app/netflix_eda.py`

## Analysis Performed
1. Basic Dataset Information
2. Content Type Distribution
3. Yearly Content Production
4. Top Producing Countries
5. Rating Distribution
6. Genres Analysis

## Dataset
Ensure netflix_titles.csv is in the same directory as the script.
"""