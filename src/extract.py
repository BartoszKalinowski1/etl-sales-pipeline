import pandas as pd
import os
import logging

logger = logging.getLogger(__name__)


def extract_data(path):
    if not os.path.exists(path):
        logger.error(f"File not found: {path}")
        raise FileNotFoundError(f"File not found: {path}")
    try:
        df = pd.read_csv(path)
    except pd.errors.ParserError as e:
        logger.error(f"Error parsing CSV file: {path}. Error:{e}")
        raise
    logger.info(f"Data extracted from: {path}. Shape: {df.shape[0]} rows and "
                f"{df.shape[1]} columns.")
    return df
