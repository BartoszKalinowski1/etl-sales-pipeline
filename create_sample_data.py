import pandas as pd
import numpy as np
import os
from config import DATA_PATH, SAMPLE_DATA_SIZE
from datetime import datetime, timedelta


def generate_sample_data():
    np.random.seed(42)

    products = {
        "Laptop": (2000, 5000),
        "Phone": (800, 2500),
        "Headphones": (100, 600),
        "Monitor": (500, 2000),
        "Keyboard": (50, 300),
        "Mouse": (30, 200),
        "Webcam": (80, 400),
        "SSD": (150, 600),
    }
    product_names = list(products.keys())

    start_date = datetime(2023, 1, 1)
    end_date = datetime(2026, 1, 1)
    date_range = (end_date - start_date).days

    df = pd.DataFrame({
        "order_id": range(1, SAMPLE_DATA_SIZE + 1),
        "customer_id": np.random.randint(1000, 5000, SAMPLE_DATA_SIZE),
        "product": np.random.choice(product_names, SAMPLE_DATA_SIZE),
        "quantity": np.random.randint(1, 6, SAMPLE_DATA_SIZE),
        "order_date": [
            (start_date + timedelta(days=int(d))).strftime("%Y-%m-%d")
            for d in np.random.randint(0, date_range, SAMPLE_DATA_SIZE)
        ],
        "region": np.random.choice(("North", "South", "East", "West"), SAMPLE_DATA_SIZE, p=[0.3, 0.2, 0.3, 0.2])
    })
    df["price"] = df["product"].apply(
        lambda p: round(np.random.uniform(*products[p]), 2)
    )

    null_idx = np.random.choice(df.index, size=int(
        SAMPLE_DATA_SIZE * 0.02), replace=False)
    df.loc[null_idx, "price"] = np.nan

    neg_idx = np.random.choice(
        df.index, size=int(SAMPLE_DATA_SIZE * 0.01), replace=False)
    df.loc[neg_idx, "quantity"] = -1

    duplicate_idx = np.random.choice(
        df.index, size=int(SAMPLE_DATA_SIZE * 0.01), replace=False)
    duplicates = df.iloc[duplicate_idx]
    df = pd.concat([df, duplicates], ignore_index=True)

    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    df.to_csv(DATA_PATH, index=False)
    print("Sample data (with null values and duplicates) created at "
          f"'{DATA_PATH}'")
