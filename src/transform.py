import numpy as np
import logging
from config import REVENUE_THRESHOLD

logger = logging.getLogger(__name__)


def transform_data(df):
    df = delete_duplicated_records(df)
    df = delete_null_customer_records(df)
    if df["price"].dtype != float:
        logger.info("Price column is not in float format. Converting ...")
        df["price"] = df["price"].astype(float)
    df = delete_negative_price_records(df)
    df = delete_negative_quantity_records(df)
    df = create_revenue_column(df)
    df = segment_customers_by_revenue(df)
    return df


def delete_duplicated_records(df):
    if df.duplicated().sum() > 0:
        logger.info(f"Found {df.duplicated().sum()} duplicated records."
                    " Deleting ...")
    return df.drop_duplicates()


def delete_null_customer_records(df):
    if df["customer"].isna().sum() > 0:
        logger.info(f"Found {df['customer'].isna().sum()} records with null "
                    "customer. Deleting ...")
    return df[~df["customer"].isna()]


def delete_negative_price_records(df):
    negative_prices = df["price"] < 0
    if negative_prices.sum() > 0:
        logger.info(f"Found {negative_prices.sum()} negative price record. "
                    "Deleting ...")
    return df[df["price"] > 0]


def delete_negative_quantity_records(df):
    negative_quantities = df["quantity"] < 0
    if negative_quantities.sum() > 0:
        logger.info(f"Found {negative_quantities.sum()} negative quantity record. "
                    "Deleting ...")
    return df[df["quantity"] > 0]


def create_revenue_column(df):
    logger.info("Creating revenue column ...")
    df["revenue"] = df["price"] * df["quantity"]
    return df


def segment_customers_by_revenue(df):
    logger.info("Segmenting orders ...")
    df["category"] = np.where(df["revenue"] > REVENUE_THRESHOLD, "High", "Low")
    return df
