# Databricks notebook source
# MAGIC %md
# MAGIC ### This is an example
# MAGIC This notebook creates a dataframe with some sample data that can be used for a quick visualization.

# COMMAND ----------

data = [[1, "Elia"], [2, "Teo"], [3, "Fang"]]
sdf = spark.createDataFrame(data, schema="id LONG, name STRING")
display(sdf)

# COMMAND ----------


