## Azure-based-Car-Sales-Analytics-Project
##  This project demonstrates a complete data analytics pipeline for car sales using Microsoft Azure services. It covers data ingestion, transformation, SQL-based analysis, and dashboarding with Power BI. The goal is to extract insights from raw CSV data and deliver interactive visualizations for business decision-making.
# 📦 Data Source
The dataset car_data.csv contains detailed car sales records 
It is stored in Azure Blob Storage and used as the input for both ETL pipelines.
# ETL Pipeline – Option 1: Azure Data Factory
This pipeline uses Azure Data Factory to:
    Ingest the CSV file from Blob Storage

    Apply basic transformations (filtering, sorting, renaming)

    Load the cleaned data into an Azure SQL Database table (CarSaless)

    Schedule and monitor pipeline runs
# ETL Pipeline – Option 2: Azure Databricks & Spark

This notebook-based pipeline uses Azure Databricks to:

    Read and clean the CSV data using PySpark

    Normalize columns, remove duplicates, and enrich data 
    Extract top-selling models and transmission trends

    Load the final dataset securely into Azure SQL using JDBC and secrets vault

# SQL Analytics with Azure Data Studio

Using Azure Data Studio, several queries were executed to analyze:

    Sales trends by month and region

    Average prices by model, brand, and transmission

    Customer segmentation by gender and income

    Dealer performance and revenue potential
# Power BI Dashboard
The final dashboard was built in Power BI, connected directly to the Azure SQL Database. It includes:

    KPIs: Total Sales, Average Price, Revenue

    Charts: Sales by Brand, Transmission Type, Monthly Trends

    Slicer: Filter by car model for dynamic insights

## 🛠️ Tools Used

Azure Blob Storage	:
Hosting raw CSV data
Azure Data Factory	:
Low-code ETL pipeline
Azure Databricks	:
Advanced data transformation with Spark
Azure SQL Database	:
Centralized data storage and querying
Azure Data Studio	:
SQL-based analysis and exploration
Power BI	:
Interactive dashboard and visualization
  
