# Netflix Dataset EDA Project

# Import required libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, avg, max, min, year
from pyspark.sql.types import StructType, StructField, StringType, FloatType, IntegerType, DateType

def create_spark_session():
    """
    Create and return a Spark session
    """
    return SparkSession.builder \
        .appName("Netflix Dataset EDA") \
        .getOrCreate()

def load_netflix_dataset(spark, file_path):
    """
    Load Netflix dataset with predefined schema
    """
    # Define schema for the Netflix dataset
    netflix_schema = StructType([
        StructField("show_id", StringType(), True),
        StructField("type", StringType(), True),
        StructField("title", StringType(), True),
        StructField("director", StringType(), True),
        StructField("cast", StringType(), True),
        StructField("country", StringType(), True),
        StructField("date_added", DateType(), True),
        StructField("release_year", IntegerType(), True),
        StructField("rating", StringType(), True),
        StructField("duration", StringType(), True),
        StructField("listed_in", StringType(), True),
        StructField("description", StringType(), True)
    ])
    
    # Load dataset with defined schema
    return spark.read.csv(file_path, header=True, schema=netflix_schema)

def perform_eda(netflix_df):
    """
    Perform Exploratory Data Analysis on Netflix Dataset
    """
    print("1. Basic Dataset Information:")
    netflix_df.printSchema()
    print(f"\nTotal number of records: {netflix_df.count()}")
    
    print("\n2. Content Type Distribution:")
    netflix_df.groupBy("type").agg(count("*").alias("count")).show()
    
    print("\n3. Yearly Content Production:")
    yearly_content = netflix_df.groupBy("release_year", "type") \
        .agg(count("*").alias("content_count")) \
        .orderBy("release_year", "type")
    yearly_content.show(20)
    
    print("\n4. Top 10 Countries Producing Content:")
    country_content = netflix_df.groupBy("country") \
        .agg(count("*").alias("content_count")) \
        .orderBy(col("content_count").desc()) \
        .limit(10)
    country_content.show()
    
    print("\n5. Rating Distribution:")
    rating_distribution = netflix_df.groupBy("rating") \
        .agg(count("*").alias("count")) \
        .orderBy(col("count").desc())
    rating_distribution.show()
    
    print("\n6. Genres Analysis:")
    # Explode listed_in to get individual genres
    from pyspark.sql.functions import explode, split
    genre_analysis = netflix_df.select(explode(split(col("listed_in"), ", ")).alias("genre")) \
        .groupBy("genre") \
        .agg(count("*").alias("count")) \
        .orderBy(col("count").desc()) \
        .limit(15)
    genre_analysis.show()

def main():
    # Create Spark Session
    spark = create_spark_session()
    
    # Load Netflix Dataset (replace with your actual dataset path)
    netflix_df = load_netflix_dataset(spark, "netflix_titles.csv")
    
    # Perform EDA
    perform_eda(netflix_df)
    
    # Stop Spark Session
    spark.stop()

if __name__ == "__main__":
    main()

