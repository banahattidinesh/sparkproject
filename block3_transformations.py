# block3_transformations.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# 1. Boot up Manager and silence warnings
spark = SparkSession.builder.appName("Transformations").master("local[*]").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

# 2. Load the data
df = spark.read.csv("logs.csv", header=True, inferSchema=True)

# 3. TRANSFORMATIONS: Filter for purchases, group by user_id, and count
print("\n=== USER PURCHASE COUNTS ===")
purchase_counts_df = df.filter(col("action") == "purchase") \
                       .groupBy("user_id") \
                       .count()

# 4. ACTION: Show the results (Spark does the work here!)
purchase_counts_df.show()

# 5. Clock out
spark.stop()