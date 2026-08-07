# ==============================================================================
# Mount poit creation :
# ==============================================================================
storage_account = "autoldrstorage"

spark.conf.set(f"fs.azure.account.auth.type.{storage_account}.dfs.core.windows.net", "OAuth")

spark.conf.set(
    f"fs.azure.account.oauth.provider.type.{storage_account}.dfs.core.windows.net",
    "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider"
)

spark.conf.set(
    f"fs.azure.account.oauth2.client.id.{storage_account}.dfs.core.windows.net",
    "f552a57f-2b78-4829-8c6c-80bdc310b2fb"
)

spark.conf.set(
    f"fs.azure.account.oauth2.client.secret.{storage_account}.dfs.core.windows.net",
    "Ywb8Q~7vQEHhfBqsPEvcegpvrrxddhSaJaZwycvE"
)

spark.conf.set(
    f"fs.azure.account.oauth2.client.endpoint.{storage_account}.dfs.core.windows.net",
    "https://login.microsoftonline.com/eb501460-42a3-4ba4-84d3-bac8285bd9dd/oauth2/token"
)
# Databricks notebook source
# ==============================================================================
# Step 1: Authentication & ADLS Gen2 Read Test (Batch Verification)
# ==============================================================================
# Initial test to verify reading the raw CSV file directly using ABFSS protocol
df_test = (
    spark.read
    .format("csv")
    .option("header", "true")
    .option("inferSchema", "true")
    .load("abfss://raw@autoloaderstoragea.dfs.core.windows.net/patient_data_2025_02_21.csv")
)

display(df_test)


# ==============================================================================
# Step 2: Auto Loader Ingestion Pipeline (Initial Hardcoded Setup)
# ==============================================================================
from pyspark.sql.functions import input_file_name

# Target Bronze Delta Table path in Unity Catalog
bronze_table_path = "testdbforproject.bronze.patient_data"

# ADLS Gen2 Source Location
input_path = "abfss://raw@projectautoloaderstorage.dfs.core.windows.net/"

# Unity Catalog Volume metadata paths
schema_location = "/Volumes/testdbforproject/bronze/metadata_files/schema/patient_data"
checkpoint_path = "/Volumes/testdbforproject/bronze/metadata_files/checkpoints/patient_data"

# Dynamic file inclusion check based on table existence
if spark.catalog.tableExists(bronze_table_path):
    includeExistingFiles = "false"
else:
    includeExistingFiles = "true"

# Read stream using Databricks Auto Loader (cloudFiles)
df_autoloader = (
    spark.readStream
    .format("cloudFiles")
    .option("cloudFiles.format", "csv")
    .option("cloudFiles.inferSchema", "true")
    .option("cloudFiles.schemaLocation", schema_location)
    .option("cloudFiles.includeExistingFiles", includeExistingFiles)
    .load(input_path)
    .withColumn("source_file", input_file_name())
)

# Write stream to Unity Catalog Bronze Table
(
    df_autoloader.writeStream
    .format("delta")
    .outputMode("append")
    .option("checkpointLocation", checkpoint_path)
    .trigger(once=True)
    .toTable(bronze_table_path)
    .awaitTermination()
)


# ==============================================================================
# Step 3: Parameterized Auto Loader Pipeline (Databricks Widgets)
# ==============================================================================
# Define Databricks Widgets for dynamic parameters
dbutils.widgets.text("catalog_name", "")
dbutils.widgets.text("schema_name", "")
dbutils.widgets.text("table_name", "")

# Get runtime widget values
catalog_name = dbutils.widgets.get("catalog_name")
schema_name = dbutils.widgets.get("schema_name")
table_name = dbutils.widgets.get("table_name")

# Dynamic paths built from widgets
bronze_table_path = f"{catalog_name}.{schema_name}.{table_name}"
input_path = "abfss://raw@projectautoloaderstorage.dfs.core.windows.net/"

schema_location = "/Volumes/testdbforproject/bronze/metadata_files/schema/patient_data"
checkpoint_path = f"/Volumes/{catalog_name}/{schema_name}/metadata_files/checkpoints/{table_name}"

# Check table existence dynamically
if spark.catalog.tableExists(bronze_table_path):
    includeExistingFiles = "false"
else:
    includeExistingFiles = "true"

# Parameterized Auto Loader Stream Read
df_parameterized = (
    spark.readStream
    .format("cloudFiles")
    .option("cloudFiles.format", "csv")
    .option("cloudFiles.inferSchema", "true")
    .option("cloudFiles.schemaLocation", schema_location)
    .option("cloudFiles.includeExistingFiles", includeExistingFiles)
    .load(input_path)
    .withColumn("source_file", input_file_name())
)

# Parameterized Stream Write to Unity Catalog Bronze Table
(
    df_parameterized.writeStream
    .format("delta")
    .outputMode("append")
    .option("checkpointLocation", checkpoint_path)
    .trigger(once=True)
    .toTable(bronze_table_path)
    .awaitTermination()
)
