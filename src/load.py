import os
import logging

logger = logging.getLogger(__name__)


def load_data(df, path):
    os.makedirs(path, exist_ok=True)
    output_path = os.path.join(path, "cleaned_sales.csv")
    try:
        df.to_csv(output_path, index=False)
        logger.info(f"Data loaded to: {output_path}")
    except Exception:
        logger.exception("Failed to load data")
        raise
