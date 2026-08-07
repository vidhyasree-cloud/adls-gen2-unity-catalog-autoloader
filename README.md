# End-to-End Data Ingestion from ADLS Gen2 to Unity Catalog Bronze Layer using Databricks Auto Loader

![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Databricks](https://img.shields.io/badge/databricks-%23FF3621.svg?style=for-the-badge&logo=databricks&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)

# Project Overview

This project implements an end-to-end, automated cloud data ingestion pipeline using **Azure Databricks** and **Unity Catalog**. The solution dynamically ingests healthcare dataset CSV files (`patient_data_2025_02_21.csv`) from **Azure Data Lake Storage Gen2 (ADLS Gen2)** into a managed **Unity Catalog Bronze Delta table** using Databricks **Auto Loader (`cloudFiles`)**.

The workflow is fully parameterized using **Databricks Widgets** (no hardcoded catalog/table paths) and automated using **Databricks Jobs** running on an optimized **Job Cluster**.

---

## Architecture & Data Flow

```text
[ Azure ADLS Gen2 (raw Container) ]
            │
            │ (OAuth 2.0 / Service Principal Authentication)
            ▼
[ Databricks Auto Loader (cloudFiles) ]  <── (Dynamic Parameters via Widgets)
            │
            ▼
┌──────────────────────────────────────────────────────────────┐
│                        Unity Catalog                         │
│  Catalog: testdbforproject                                   │
│  Schema:  bronze                                             │
│  Table:   patient_data (Delta Format)                        │
│  Volume:  metadata_files (Auto Loader Schema & Checkpoints)  │
└──────────────────────────────────────────────────────────────┘
            │
            ▼
[ Databricks Job & Automated Job Cluster Execution ]
