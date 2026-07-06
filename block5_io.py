# block5_io.py
from pyspark.sql import SparkSession

# 1. Boot up Manager
spark = SparkSession.builder.appName("FileIO").master("local[*]").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

# 2. READ: Load the raw JSON data
print("\n=== READING RAW JSON ===")
users_df = spark.read.json("users.json")
users_df.show()

# 3. WRITE: Save the DataFrame as a Parquet file
# mode("overwrite") ensures we don't get an error if we run this script twice
print("\n=== WRITING PARQUET TO DISK ===")
users_df.write.mode("overwrite").parquet("output_data/users_parquet")

print("Success! Check your project folder for the 'output_data' folder.")

# 4. Clock out
spark.stop()