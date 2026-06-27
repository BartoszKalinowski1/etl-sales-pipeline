import logging
from config import DB_CONFIG
import psycopg2
from psycopg2.extras import execute_values

logger = logging.getLogger(__name__)


def get_connection():
    return psycopg2.connect(**DB_CONFIG)


def load_raw(df):
    sql = """
        INSERT INTO sales.sales_raw(order_id, customer_id, product, quantity,
              order_date, region, price)
        VALUES %s
        ON CONFLICT (order_id) DO NOTHING;
    """

    rows = [tuple(row) for row in df[["order_id", "customer_id", "product",
                                      "quantity", "order_date", "region", "price"]].itertuples(index=False)]
    try:
        with get_connection() as conn:
            with conn.cursor() as curr:
                execute_values(curr, sql, rows)
        logger.info(f"Loaded {len(rows)} columns into sales_raw")
    except Exception:
        logger.exception("Failed to load raw data")
        raise


def load_clean(df):
    sql = """
    INSERT INTO sales.sales_clean(order_id, customer_id, product, 
                                  quantity, order_date, region, price, revenue, category)
    VALUES %s
    ON CONFLICT (order_id) DO NOTHING;
    """
    rows = [tuple(row) for row in df[["order_id", "customer_id", "product",
                                      "quantity", "order_date", "region", "price", "revenue", "category"]].itertuples(index=False)]
    try:
        with get_connection() as conn:
            with conn.cursor() as curr:
                execute_values(curr, sql, rows)
        logger.info(f"Loaded {len(rows)} rows into sales_clean.")
    except Exception:
        logger.exception("Failed to load clean data.")
        raise


def load_segments():
    sql = """
        INSERT INTO sales.customer_segments(customer_id, total_orders, total_revenue, category)
        SELECT customer_id,
            COUNT(DISTINCT order_id) as total_orders,
            SUM(revenue) as total_revenue,
            category
        FROM sales.sales_clean
        GROUP BY customer_id, category
        ON CONFLICT (customer_id) DO NOTHING;
    """
    try:
        with get_connection() as conn:
            with conn.cursor() as curr:
                curr.execute(sql)
        logger.info("Customer segments loaded.")
    except Exception:
        logger.exception("Failed to load customer segments.")
        raise
