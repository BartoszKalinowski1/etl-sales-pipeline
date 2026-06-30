# ETL Sales Pipeline

Modular ETL pipeline that processes raw sales data, validates it through an automated quality framework, loads it into a PostgreSQL database, and is orchestrated end-to-end by Apache Airflow — all running in Docker.

Built to demonstrate core Data Engineering skills: pipeline design, data quality validation, automated testing, containerized infrastructure, and workflow orchestration.

## What it does

1. **Generate** — creates 10,000+ sample sales records with intentional data issues (duplicates, nulls, negative values)
2. **Extract** — reads raw CSV data into a Pandas DataFrame
3. **Transform** — removes duplicates, nulls, and invalid records; calculates revenue and segments customers
4. **Quality Check** — validates the cleaned data before loading
5. **Load** — inserts raw and cleaned data into PostgreSQL; aggregates customer segments via SQL
6. **Orchestrate** — the full pipeline runs as an Airflow DAG (`extract → transform → quality_check → load`), scheduled daily

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
├── dags/
│   └── etl_sales_dag.py    # Airflow DAG orchestrating the full pipeline
├── tests/                  # pytest test suite (covers all transform and quality logic)
├── data/
│   └── raw/                # Generated sample data
├── main.py                 # Standalone pipeline entrypoint (no Airflow)
├── config.py                # Paths and DB connection config (env-var aware)
├── schema.sql               # PostgreSQL schema (3 tables: raw, clean, segments)
├── queries.sql               # SQL used by the load step
├── docker-compose.yml        # PostgreSQL service with auto schema init
├── create_sample_data.py     # Sample data generator
└── requirements.txt

## Tech stack

| Tool | Purpose |
|---|---|
| Python, Pandas, NumPy | Data processing and transformation |
| psycopg2 | PostgreSQL connection and bulk insert |
| PostgreSQL 15 | Target database |
| Docker, Docker Compose | Containerized database environment |
| Apache Airflow | Pipeline orchestration and scheduling |
| pytest | Automated testing |

## How to run

### Option A — standalone (no Airflow)

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

### Option B — orchestrated with Airflow

**1. Start the database** (same as above)
```bash
docker-compose up -d
```

**2. Run Airflow** with this repository mounted as a volume (see `dags/etl_sales_dag.py` for the expected mount path `/opt/airflow/etl_pipeline`).

**3. Trigger the DAG** `etl_sales_pipeline` from the Airflow UI (`localhost:8080`) or CLI. The DAG sets `DB_HOST=host.docker.internal` automatically so it can reach the PostgreSQL container from inside Airflow.

### Verify the data
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
- **`customer_segments`** — customer-level aggregates (`total_orders`, `total_revenue`) produced by a single SQL `INSERT INTO ... SELECT GROUP BY`

## Notes

`config.py` reads the database host from the `DB_HOST` environment variable, defaulting to `localhost`. This lets the exact same codebase run unmodified both as a standalone script (`python main.py`) and as an Airflow DAG inside Docker (`host.docker.internal`), without any code duplication.