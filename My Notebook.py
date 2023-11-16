# Databricks notebook source
# MAGIC %md
# MAGIC ### This is an example
# MAGIC This notebook creates a dataframe with some sample data that can be used for a quick visualization.

# COMMAND ----------

data = [[1, "Elia"], [2, "Teo"], [3, "Fang"], [4, "Alladio"]]
sdf = spark.createDataFrame(data, schema="id LONG, name STRING")
display(sdf)

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS customers_bronze;
# MAGIC COPY INTO customers_bronze
# MAGIC     FROM 'dbfs:/mnt/dbacademy-datasets/get-started-with-data-engineering-on-databricks/v01/'
# MAGIC     FILEFORMAT = CSV
# MAGIC     FORMAT_OPTIONS ('inferSchema' = 'true', 'header' = 'true')
# MAGIC     COPY_OPTIONS ('mergeSchema' = 'true')
