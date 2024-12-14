# Netflix TV Shows & Movies Dataset EDA

This project performs Exploratory Data Analysis (EDA) on the Netflix TV Shows & Movies dataset using PySpark. The analysis includes basic dataset information, content type distribution, yearly content production, top countries producing content, and rating distribution.

## Getting Started

### Prerequisites

- Docker
- PySpark
- Jupyter Notebook

### Setup

1. **Install Docker**: Download and install Docker from here.
2. **Pull the PySpark Docker Image**: Open your terminal and run:
   ```bash
   docker pull jupyter/pyspark-notebook
   ```
3. **Run the Docker Container**: Start the container with:
   ```bash
   docker run -it --rm -p 8888:8888 jupyter/pyspark-notebook
   ```
   This will start a Jupyter Notebook server. Access it by navigating to `http://localhost:8888` in your web browser.

### Dataset
Go to Kaggle (https://www.kaggle.com/datasets/shivamb/netflix-shows)

Download the Netflix TV Shows & Movies dataset and place it in the project directory. The dataset should be named `netflix_titles.csv`.

### Running the Analysis

1. **Open Jupyter Notebook**: Navigate to `http://localhost:8888` and open a new notebook.
2. **Copy the Python Code**: Use the provided Python code to perform EDA on the dataset.


### Results

The analysis includes:
1. **Basic Dataset Information**: Schema and total number of records.
2. **Content Type Distribution**: Distribution of movies and TV shows.
3. **Yearly Content Production**: Number of movies and TV shows produced each year.
4. **Top 10 Countries Producing Content**: Countries with the highest content production.
5. **Rating Distribution**: Distribution of content ratings.

