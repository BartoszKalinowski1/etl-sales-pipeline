from src.extract import extract_data
from src.transform import transform_data

data_path = "data/raw/sales.csv"
raw_df = extract_data(data_path)
print("\nRaw data extracted:\n")
print(raw_df)
cleaned_df = transform_data(raw_df)
print("\nData after cleaning process:\n")
print(cleaned_df)
