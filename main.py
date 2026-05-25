from src.extract import extract_data
from src.transform import transform_data
from src.quality_checks import check_quality
from src.load import load_data
import logging
import os

os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/pipeline.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

logger.info("ETL pipeline started")

data_path = "data/raw/sales.csv"

logger.info("Starting extraction step")

try:
    raw_df = extract_data(data_path)
    logger.info(f"Raw data extracted. Shape: {raw_df.shape}")
except Exception as e:
    logger.error(f"Extraction failed: {e}")
    raise

logger.info("Extraction completed")

logger.info("Starting transformation step")

try:
    cleaned_df = transform_data(raw_df)
    logger.info(f"Transform completed. Shape: {cleaned_df.shape}")
except Exception as e:
    logger.error(f"Transformation failed: {e}")
    raise

processed_dir = "data/processed/"

logger.info("Running data quality checks")

if check_quality(cleaned_df):
    logger.info("Starting load step")
    try:
        load_data(cleaned_df, processed_dir)
        logger.info("Loading completed")
        logger.info(f"ETL pipeline finished successfully. Final shape of "
                    f"cleaned data: {cleaned_df.shape}")
    except Exception as e:
        logger.error(f"Loading failed: {e}")
        raise
else:
    logger.error("Pipeline finished with error - quality checks "
                 "failed. Data was not loaded.")
