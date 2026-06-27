from src.extract import extract_data
from src.transform import transform_data
from src.quality_checks import check_quality
from src.load import load_raw, load_clean, load_segments
import logging
import os
from config import DATA_PATH, LOG_PATH
from create_sample_data import generate_sample_data

os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_PATH),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

logger.info("ETL pipeline started")

logger.info("Generating sample data")
generate_sample_data()

logger.info("Starting extraction step")

try:
    raw_df = extract_data(DATA_PATH)
    logger.info(f"Raw data extracted. Shape: {raw_df.shape}")
except Exception:
    logger.exception("Extraction failed")
    raise

logger.info("Extraction completed")

logger.info("Starting transformation step")

try:
    cleaned_df = transform_data(raw_df)
    logger.info(f"Transform completed. Shape: {cleaned_df.shape}")
except Exception:
    logger.exception("Transformation failed")
    raise


logger.info("Running data quality checks")

if check_quality(cleaned_df):
    logger.info("Starting load step")
    try:
        load_raw(raw_df)
        load_clean(cleaned_df)
        load_segments()
        logger.info("Loading completed")
        logger.info(f"ETL pipeline finished successfully. "
                    f"Rows={len(cleaned_df)} | columns={cleaned_df.shape[1]} | "
                    f"Data loss={len(raw_df) - len(cleaned_df)}")
    except Exception:
        logger.exception("Loading failed")
        raise
else:
    logger.error("Pipeline finished with error - quality checks "
                 "failed. Data was not loaded.")
