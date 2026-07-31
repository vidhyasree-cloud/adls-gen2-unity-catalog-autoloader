# adls-gen2-unity-catalog-autoloader

# Azure Databricks Auto Loader Project

## Project Overview

This project demonstrates an end-to-end data ingestion pipeline using Azure Databricks Auto Loader to ingest CSV files from Azure Data Lake Storage Gen2 into a Unity Catalog Bronze Delta table.

---

## Technologies Used

- Azure Databricks
- Azure Data Lake Storage Gen2
- Unity Catalog
- Delta Lake
- PySpark
- Databricks Widgets
- Databricks Jobs
- OAuth Authentication

---

## Project Architecture

(Add your architecture image here after uploading.)

---

## Project Flow

1. Upload CSV into ADLS Gen2
2. Authenticate using Azure App Registration
3. Read files using Auto Loader
4. Infer schema
5. Store checkpoints in Unity Catalog Volume
6. Load data into Bronze Delta Table
7. Execute using Databricks Job

---

## Features

- Auto Loader (cloudFiles)
- OAuth Authentication
- Unity Catalog
- Bronze Delta Table
- Parameterized Notebook
- Databricks Widgets
- Job Cluster
- Delta Lake

---

## Challenges

- DBFS Mount Disabled
- UC Volume Not Found
- Azure CPU Quota Exceeded

---

## Outcome

Successfully implemented an end-to-end Auto Loader pipeline for incremental ingestion from Azure Data Lake Storage Gen2 into Unity Catalog.
