import pandas as pd


def transform_data(df):
    if df.duplicated().sum() > 0:
        print(f"\nFound {df.duplicated().sum()} duplicated records."
              " Deleting ...")
    df = df.drop_duplicates()
    if df["customer"].isna().sum() > 0:
        print(f"\nFound {df['customer'].isna().sum()} records with null "
              "customer. Deleting ...")
    df = df[~df["customer"].isna()]
    if df["price"].dtype != float:
        print("\nPrice column is not in float format. Converting ...")
    df["price"] = df["price"].astype(float)
    negative_prices = df["price"] < 0
    if negative_prices.sum() > 0:
        print(f"\nFound {negative_prices.sum()} negative price record. "
              "Deleting ...")
        df = df[df["price"] > 0]
    if df["quantity"].dtype != int:
        print("\nQuantity column is not in integer format. Converting ...")
    df["quantity"] = df["quantity"].astype(int)
    print("\nCreating revenue column ...")
    df["revenue"] = df["price"] * df["quantity"]
    return df
