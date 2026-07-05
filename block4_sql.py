# block4_sql.py
from pyspark.sql import SparkSession

# 1. Boot up Manager and silence warnings
spark = SparkSession.builder.appName("SparkSQL").master("local[*]").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

# 2. Load the data
df = spark.read.csv("logs.csv", header=True, inferSchema=True)

# 3. SPARK SQL SETUP: Turn the DataFrame into a queryable SQL table
df.createOrReplaceTempView("traffic_logs")

# 4. EXECUTING SQL: Let's find out how many times each page was visited
print("\n=== SQL RESULTS: PAGE VISITS ===")
sql_query = """
    SELECT page, COUNT(*) as total_visits 
    FROM traffic_logs 
    GROUP BY page 
    ORDER BY total_visits DESC
"""
result_df = spark.sql(sql_query)

# 5. ACTION: Show the results
result_df.show()

# 6. Clock out
spark.stop()