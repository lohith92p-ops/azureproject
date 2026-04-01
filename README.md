# azureproject
##Spotify Data Pipeline (ADF + Databricks)

### Overview
End-to-end data pipeline built using Azure services to ingest, process, and transform Spotify data into analytics-ready datasets using the Medallion Architecture.

### Architecture

Bronze → Silver → Gold

Bronze: Raw data ingestion (ADF → ADLS)
Silver: Cleaned + incremental processing using Delta Live Tables (CDC)
Gold: Aggregated business tables for reporting

### Tech Stack
Azure Data Factory
Azure Databricks (Delta Live Tables)
PySpark
Delta Lake
ADLS Gen2
GitHub

### Pipeline Flow
ADF ingests raw data into Bronze layer
Databricks DLT processes data into Silver (with CDC)
Gold layer generates business-level insights

### Key Features
Incremental processing with Auto CDC
Data quality checks using DLT expectations
Scalable streaming + batch processing
Modular pipeline design

### Summary
Production-style data pipeline demonstrating modern lakehouse architecture using Azure and Databricks.


