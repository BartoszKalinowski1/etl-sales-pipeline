import os
import pandas as pd
from src.load import load_data
from config import OUTPUT_FILE


def test_load_data(tmp_path):
    df = pd.DataFrame({
        "order_id": [1, 2, 3],
        "customer": ["Ania", "Tomek", "Kasia"],
        "price": [100.50, 20.00, 50.00],
        "quantity": [1, 3, 2]
    })
    test_path = tmp_path
    load_data(df, test_path)

    output_file = os.path.join(test_path, OUTPUT_FILE)
    assert os.path.exists(output_file)
