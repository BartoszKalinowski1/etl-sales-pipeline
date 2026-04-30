import pandas as pd
import os

os.makedirs('data/raw', exist_ok=True)
data = {
    "order_id": [1, 2, 3, 3, 4, 5, 6],
    "customer": ["Ania", "Tomek", "Kasia", "Kasia", "Marek", "Ola", None],
    "price": ["100.50", "20.00", "50.00", "50.00", "-10.00", "300.00", "50.0"],
    "quantity": [1, 3, 2, 2, 1, 1, 2]
}
df = pd.DataFrame(data)
df.to_csv("data/raw/sales.csv", index=False)
print("Sample data (with null values and duplicates) created at "
      "'data/raw/sales.csv'")
