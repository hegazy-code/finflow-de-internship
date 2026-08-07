# FinFlow — Financial Data Engineering Pipeline

An end-to-end data engineering pipeline for processing, transforming, validating, and analyzing large-scale financial transaction data.

## What it does

FinFlow ingests raw financial transaction data and runs it through a full ETL pipeline: cleaning and validating records, converting storage from CSV to Parquet for performance, loading it into a star-schema data warehouse, and running SQL-based analytics — including fraud detection features — on top.

## Features

- **Ingestion** — reads and validates raw transaction data
- **Transformation** — CSV → Parquet conversion for faster, smaller storage
- **Data Warehouse** — star-schema design for analytical queries
- **Data Quality** — automated validation checks on every run
- **Analytics** — SQL-based fraud detection and feature engineering
- **Performance** — optimized for large transaction volumes using DuckDB

## Tech Stack

Python · SQL · DuckDB · Pandas · Parquet

## Getting Started

```bash
git clone https://github.com/hegazy-code/finflow-de-internship.git
cd finflow-de-internship
pip install -r requirements.txt
python db_setup.py
```

## Status

Actively developed as part of ongoing data engineering practice.

## License

MIT — see [LICENSE](LICENSE).
