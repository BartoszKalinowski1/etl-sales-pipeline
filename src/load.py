import os
import logging
from config import OUTPUT_FILE

logger = logging.getLogger(__name__)


def load_data(df, path):
    os.makedirs(path, exist_ok=True)
    output_path = os.path.join(path, OUTPUT_FILE)
    try:
        df.to_csv(output_path, index=False)
        logger.info(f"Data loaded to: {output_path}")
    except Exception:
        logger.exception("Failed to load data")
        raise
