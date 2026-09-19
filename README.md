# RetailPulse — End-to-End Retail Analytics Platform

RetailPulse is an end-to-end retail analytics project designed to analyze sales transactions, customer behavior, product performance, inventory patterns, and regional sales trends.

The project demonstrates a complete analytics workflow from raw data generation and data cleaning to SQL analysis, cloud data warehousing, and interactive Power BI dashboards.

## Tech Stack

- Python
- Pandas
- NumPy
- SQL
- Snowflake
- Power BI
- Excel
- Git & GitHub

## Project Architecture

Raw Data
↓
Python / Pandas
↓
Data Cleaning & Transformation
↓
SQL Analytics
↓
Snowflake Data Warehouse
↓
Power BI
↓
Interactive Dashboards

## Current Progress

- [x] Project structure
- [x] Python environment setup
- [x] Synthetic customer data generation
- [x] Synthetic product data generation
- [x] Synthetic store data generation
- [ ] Transaction data generation
- [ ] Data exploration
- [ ] Data cleaning
- [ ] Data transformation
- [ ] SQL analysis
- [ ] Snowflake data warehouse
- [ ] Power BI data model
- [ ] Power BI dashboards
- [ ] Business insights

## Dataset

The project will use a synthetic retail dataset containing approximately:

- 10,000+ customers
- 2,000+ products
- 500+ stores
- 100,000+ transactions
- 24 months of historical data

The dataset will intentionally contain real-world data-quality issues such as missing values, duplicate records, invalid IDs, inconsistent categories, incorrect dates, and outliers.

## Project Structure

```text
retailpulse-sales-analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
├── src/
├── sql/
├── dashboard/
├── reports/
│
├── README.md
├── requirements.txt
└── .gitignore