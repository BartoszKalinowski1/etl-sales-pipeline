from src.extract import extract_data

data_path = "data/raw/sales.csv"
raw_df = extract_data(data_path)
print("raw data extracted:\n")
print(raw_df)
