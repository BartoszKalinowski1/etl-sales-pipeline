# ETL Sales Pipeline

Modular ETL pipeline that processes raw sales data and loads it into a PostgreSQL database running in Docker.

Built to demonstrate core Data Engineering skills: pipeline design, data quality validation, automated testing, and containerized database infrastructure.

## What it does

1. **Generate** — creates 10,000+ sample sales records with intentional data issues (duplicates, nulls, negative values)
2. **Extract** — reads raw CSV data into a Pandas DataFrame
3. **Transform** — removes duplicates, nulls, and invalid records; calculates revenue and segments customers
4. **Quality Check** — validates the cleaned data before loading
5. **Load** — inserts raw and cleaned data into PostgreSQL; aggregates customer segments via SQL

## Results

| Table | Rows | Description |
|---|---|---|
| `sales.sales_raw` | 10,100 | Raw data, unmodified |
| `sales.sales_clean` | 9,703 | After deduplication and validation |
| `sales.customer_segments` | 3,644 | Aggregated per customer via SQL GROUP BY |

Data loss of ~397 records caught and removed by the quality framework.

## Repository structure
etl-sales-pipeline/

├── src/

│   ├── extract.py          # CSV ingestion

│   ├── transform.py        # Cleaning and feature engineering

│   ├── quality_checks.py   # Validation before load

│   └── load.py             # PostgreSQL insertion via psycopg2

├── tests/                  # pytest test suite (covers all transform and quality logic)

├── data/

│   └── raw/                # Generated sample data

├── main.py                 # Pipeline entrypoint

├── config.py               # Paths and DB connection config

├── schema.sql              # PostgreSQL schema (3 tables: raw, clean, segments)

├── queries.sql             # SQL used by the load step

├── docker-compose.yml      # PostgreSQL service with auto schema init

├── create_sample_data.py   # Sample data generator

└── requirements.txt

## Tech stack

| Tool | Purpose |
|---|---|
| Python, Pandas, NumPy | Data processing and transformation |
| psycopg2 | PostgreSQL connection and bulk insert |
| PostgreSQL 15 | Target database |
| Docker, Docker Compose | Containerized database environment |
| pytest | Automated testing |

## How to run

**1. Start the database**
```bash
docker-compose up -d
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the pipeline**
```bash
python main.py
```

**4. Verify the data**
```bash
docker exec -it etl-sales-pipeline-db-1 psql -U admin -d sales_db
```
```sql
SELECT COUNT(*) FROM sales.sales_raw;
SELECT COUNT(*) FROM sales.sales_clean;
SELECT COUNT(*) FROM sales.customer_segments;
```

## Run tests
```bash
pytest
```

## Database schema

Three-layer model reflecting the pipeline stages:

- **`sales_raw`** — raw data loaded before any transformation
- **`sales_clean`** — validated and enriched records (+ `revenue`, `category`)
- **`sales_segments`** — customer-level aggregates (`total_orders`, `total_revenue`) produced by a single SQL `INSERT INTO ... SELECT GROUP BY`