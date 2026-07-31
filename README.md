# Azure Databricks Auto Loader Project

## Project Overview

This project demonstrates an end-to-end data ingestion pipeline using Azure Databricks Auto Loader to ingest CSV files from Azure Data Lake Storage Gen2 (ADLS Gen2) into a Unity Catalog Bronze Delta table.

## Technologies Used

- Azure Databricks
- Azure Data Lake Storage Gen2 (ADLS Gen2)
- Unity Catalog
- Delta Lake
- PySpark
- Auto Loader (cloudFiles)
- Databricks Widgets
- Databricks Jobs
- OAuth Authentication

## Key Features

- Secure OAuth authentication using Azure App Registration.
- Incremental file ingestion using Auto Loader.
- Parameterized notebook using Databricks widgets.
- Bronze Delta table created in Unity Catalog.
- Job and Job Cluster configured for automated execution.

## Challenges

- DBFS mount not available.
- Unity Catalog Volume configuration.
- Azure CPU quota exceeded during Job Cluster creation.

## Documentation

The complete project report is available in this repository.

## Note

The Azure resources used for this project were deleted after testing and documentation to avoid unnecessary cloud costs.
