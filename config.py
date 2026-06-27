DATA_PATH = "data/raw/sales.csv"
PROCESSED_DIR = "data/processed/"
LOG_PATH = "logs/pipeline.log"
OUTPUT_FILE = "cleaned_sales.csv"


REVENUE_THRESHOLD = 100.0
SAMPLE_DATA_SIZE = 10000


DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "sales_db",
    "user": "admin",
    "password": "admin",
}
