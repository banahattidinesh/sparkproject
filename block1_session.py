# block1_session.py
from pyspark.sql import SparkSession

# Initialize a local Spark Session
# 'local[*]' tells Spark to use all available CPU cores on your machine
spark = SparkSession.builder \
    .appName("EcommerceTrafficAnalysis") \
    .master("local[*]") \
    .config("spark.sql.shuffle.partitions", "10") \
    .getOrCreate()

# Verify the session is active by printing its properties
print("======= SPARK SESSION DETAILS =======")
print(f"Application Name: {spark.sparkContext.appName}")
print(f"Master URL: {spark.sparkContext.master}")
print(f"Spark Version: {spark.version}")
print("=====================================")

# Stop the session to free up local resources
print(spark.conf.get("spark.sql.shuffle.partitions"))
spark.stop()