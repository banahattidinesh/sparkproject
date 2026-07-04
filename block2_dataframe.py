# block2_dataframe.py
from pyspark.sql import SparkSession

# 1. Boot up the Manager
spark = SparkSession.builder.appName("DataFrameIntro").master("local[*]").getOrCreate()

# 2. Tell Spark to SILENCE all warnings and only show us fatal ERRORs
spark.sparkContext.setLogLevel("ERROR")

# 3. Read the massive (mock) CSV file into a DataFrame
# header=True tells Spark the first row contains column names
# inferSchema=True tells Spark to guess if a column is a number, text, etc.
df = spark.read.csv("logs.csv", header=True, inferSchema=True)

# 4. Investigate the Structure (Schema) of the DataFrame
print("\n=== DATAFRAME SCHEMA ===")
df.printSchema()

# 5. Look at the actual data inside
print("\n=== DATAFRAME PREVIEW ===")
# calculate total number of rows and print it
total_events = df.count()
print(f"\nTotal events: {total_events}")

# show only the `user_id` and `action` columns for analysts
print("\n=== USER ACTIONS PREVIEW (user_id, action) ===")
df.select("user_id", "action").show(20, truncate=False)


# 6. Clock out
spark.stop()