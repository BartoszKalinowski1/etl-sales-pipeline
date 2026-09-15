import os

DATA_PATH = "data/raw/sales.csv"
LOG_PATH = "logs/pipeline.log"


REVENUE_THRESHOLD = 100.0
SAMPLE_DATA_SIZE = 10000


DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", 5432)),
    "dbname": os.getenv("DB_NAME", "sales_db"),
    "user": os.getenv("DB_USER", "admin"),
    "password": os.getenv("DB_PASSWORD", "admin"),
}
