from datetime import datetime
from airflow.decorators import dag, task
import sys
import os
os.environ["DB_HOST"] = "host.docker.internal"
sys.path.insert(0, "/opt/airflow/etl_pipeline")
sys.path.insert(0, "/opt/airflow/etl_pipeline/src")


@dag(start_date=datetime(2026, 1, 1), schedule="@daily", catchup=False)
def etl_sales_pipeline():
    @task
    def extract():
        from extract import extract_data
        df = extract_data("/opt/airflow/etl_pipeline/data/raw/sales.csv")
        return df.to_json()

    @task
    def transform(raw_json):
        import pandas as pd
        from transform import transform_data
        df = pd.read_json(raw_json)
        clean_df = transform_data(df)
        return clean_df.to_json()

    @task
    def run_quality_checks(clean_json):
        import pandas as pd
        from quality_checks import check_quality
        df = pd.read_json(clean_json)
        if not check_quality(df):
            raise ValueError("Quality check failed")
        return clean_json

    @task
    def load(clean_json):
        import pandas as pd
        from load import load_clean, load_segments
        df = pd.read_json(clean_json)
        load_clean(df)
        load_segments()

    raw = extract()
    clean = transform(raw)
    checked = run_quality_checks(clean)
    load(checked)


etl_sales_pipeline()
