# Azure Databricks Auto Loader to Unity Catalog Ingestion Pipeline

![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Databricks](https://img.shields.io/badge/databricks-%23FF3621.svg?style=for-the-badge&logo=databricks&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)

## Project Overview

This project demonstrates an end-to-end data ingestion pipeline built on **Azure Databricks** and **Unity Catalog**. The pipeline ingests raw CSV files dynamically from **Azure Data Lake Storage Gen2 (ADLS Gen2)** using Databricks **Auto Loader (`cloudFiles`)** and populates a **Bronze Delta Lake table** with schema inference and incremental loading.

The entire workflow is orchestrated via **Databricks Workflows (Jobs)**, parameterized using **Databricks Widgets**, and secured via **OAuth 2.0 Service Principal authentication**.

---

## Architecture & Data Flow

```text
[ ADLS Gen2 (CSV Storage) ]
            │
            │ (OAuth 2.0 / Service Principal / Unity Catalog External Location)
            ▼
[ Databricks Auto Loader (cloudFiles) ]
            │ (Schema Inference & Evolution)
            ▼
[ Unity Catalog ] ──> [ Bronze Delta Table ]
