import logging

logger = logging.getLogger(__name__)


def check_quality(df):
    logger.info("Starting data quality checks")
    if not count_null(df):
        return False
    if not check_df_length(df):
        return False
    if not check_price_values(df):
        return False
    if not check_revenue_column(df):
        return False
    if not check_revenue_values(df):
        return False
    if not check_duplicates(df):
        return False
    logger.info("Quality check passed. Data is ready for loading.")
    return True


def count_null(df):
    count = df.isnull().sum().sum()
    if count > 0:
        logger.error(f"Quality check failed - found {count} null values.")
        return False
    return True


def check_df_length(df):
    if len(df) == 0:
        logger.error("Quality check failed - DataFrame is empty.")
        return False
    return True


def check_price_values(df):
    if df["price"].dtype != float:
        logger.error(
            "Quality check failed - price column is not in float format.")
        return False
    return True


def check_revenue_values(df):
    if df["revenue"].dtype != float:
        logger.error(
            "Quality check failed - revenue column is not in float format.")
        return False
    return True


def check_duplicates(df):
    if df.duplicated().any():
        logger.error("Quality check failed - duplicate rows found.")
        return False
    return True


def check_revenue_column(df):
    if "revenue" not in df.columns:
        logger.error("Quality check failed - revenue column is missing.")
        return False
    return True
