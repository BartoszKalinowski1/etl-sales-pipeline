import os

DATA_PATH = "data/raw/sales.csv"
LOG_PATH = "logs/pipeline.log"


REVENUE_THRESHOLD = 100.0
SAMPLE_DATA_SIZE = 10000


DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": 5432,
    "dbname": "sales_db",
    "user": "admin",
    "password": "admin",
}
