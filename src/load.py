import pandas as pd
import os


def load_data(df, path):
    if not os.path.exists(path):
        print(f"\nPath {path} does not exist. Creating ...")
        os.makedirs(path)
    output_path = os.path.join(path, "cleaned_sales.csv")
    df.to_csv(output_path, index=False)
    print(f"\nData loaded to {output_path}")
