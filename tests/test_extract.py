from src.extract import extract_data
import os


def test_extract_data():
    test_file = "test_data.csv"
    test_data = "id,name,price\n1,Product A,10.0\n2,Product B,20.0\n3,Product C,30.0"
    with open(test_file, "w") as f:
        f.write(test_data)

    df = extract_data(test_file)

    assert df.shape == (3, 3)
    assert list(df.columns) == ["id", "name", "price"]
    assert df["id"].tolist() == [1, 2, 3]
    assert df["name"].tolist() == ["Product A", "Product B", "Product C"]
    assert df["price"].tolist() == [10.0, 20.0, 30.0]

    os.remove(test_file)
