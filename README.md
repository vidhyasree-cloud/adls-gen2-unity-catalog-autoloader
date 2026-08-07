# Azure Databricks Real-Time Healthcare Data Ingestion Pipeline

![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Databricks](https://img.shields.io/badge/databricks-%23FF3621.svg?style=for-the-badge&logo=databricks&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)

## Project Overview

This project demonstrates an end-to-end data engineering pipeline designed to ingest **real-time healthcare data** into a **Medallion Architecture** managed by **Azure Databricks** and **Unity Catalog**. 

Using **Databricks Auto Loader (`cloudFiles`)**, the pipeline streams raw CSV data from **Azure Data Lake Storage Gen2 (ADLS Gen2)** incrementally into a **Unity Catalog Bronze Delta table** with zero manual hardcoding. The notebook is fully parameterized using **Databricks Widgets** and orchestrated with **Databricks Jobs** running on dedicated **Job Clusters**.

---

##  Architecture & Data Flow

```text
[ Real-Time Healthcare Data ] 
              │
              ▼
  [ Source: ADLS Gen2 Storage ]
              │
              │ (OAuth 2.0 / Service Principal / Unity Catalog External Location)
              ▼
  [ Databricks Auto Loader Logic ]  <── (Dynamic Parameters via Widgets / No Hardcoded Paths)
              │
              ▼
┌─────────────────────────────────────────────────────────────┐
│                       Unity Catalog                         │
│  ┌─────────────────┐                                        │
│  │  Bronze Layer   │ ──> (Raw Data - Incremental Stream)    │
│  └─────────────────┘                                        │
└─────────────────────────────────────────────────────────────┘
              │
              ▼
  [ Databricks Workflows / Job Cluster Orchestration ]
