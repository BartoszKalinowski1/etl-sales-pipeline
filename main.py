from src.extract import extract_data
from src.transform import transform_data
from src.quality_checks import check_quality
from src.load import load_data

data_path = "data/raw/sales.csv"
raw_df = extract_data(data_path)
print("\nRaw data extracted:\n")
print(raw_df)
cleaned_df = transform_data(raw_df)
print("\nData after cleaning process:\n")
print(cleaned_df)
processed_dir = "data/processed/"
if check_quality(cleaned_df):
    load_data(cleaned_df, processed_dir)
    print("\nETL pipeline finished successfully.\n")
else:
    print("Pipeline finished with error - quality checks "
          "failed. Data was not loaded.")
