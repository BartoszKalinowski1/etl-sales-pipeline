import pandas as pd
from src.transform import delete_duplicated_records, delete_null_customer_records, \
    delete_negative_price_records, delete_negative_quantity_records, create_revenue_column, \
    segment_customers_by_revenue, transform_data


def test_delete_duplicated_records():
    df = pd.DataFrame({
        "order_id": [1, 2, 3, 3, 4, 5, 6],
        "customer": ["Ania", "Tomek", "Kasia", "Kasia", "Marek", "Ola", None],
        "price": [100.50, 20.00, 50.00, 50.00, -10.00, 300.00, 50.0],
        "quantity": [1, 3, 2, 2, 1, 1, 2]
    })
    result = delete_duplicated_records(df)

    assert result.duplicated().sum() == 0
    assert len(result) < len(df)


def test_delete_null_customer_records():
    df = pd.DataFrame({
        "order_id": [1, 2, 3, 3, 4, 5, 6],
        "customer": ["Ania", "Tomek", "Kasia", "Kasia", "Marek", "Ola", None],
        "price": [100.50, 20.00, 50.00, 50.00, -10.00, 300.00, 50.0],
        "quantity": [1, 3, 2, 2, 1, 1, 2]
    })
    result = delete_null_customer_records(df)

    assert result["customer"].isna().sum() == 0
    assert len(result) < len(df)


def test_delete_negative_price_records():
    df = pd.DataFrame({
        "order_id": [1, 2, 3, 3, 4, 5, 6],
        "customer": ["Ania", "Tomek", "Kasia", "Kasia", "Marek", "Ola", None],
        "price": [100.50, 20.00, 50.00, 50.00, -10.00, 300.00, 50.0],
        "quantity": [1, 3, 2, 2, 1, 1, 2]
    })
    result = delete_negative_price_records(df)

    assert (result["price"].astype(float) > 0).all()
    assert len(result) == len(df) - 1


def test_delete_negative_quantity_records():
    df = pd.DataFrame({
        "order_id": [1, 2, 3, 3, 4, 5, 6],
        "customer": ["Ania", "Tomek", "Kasia", "Kasia", "Marek", "Ola", None],
        "price": [100.50, 20.00, 50.00, 50.00, -10.00, 300.00, 50.0],
        "quantity": [1, 3, 2, 2, -1, 1, 2]
    })
    result = delete_negative_quantity_records(df)

    assert (result["quantity"] < 0).sum() == 0
    assert len(result) == len(df) - 1


def test_create_revenue_column():
    df = pd.DataFrame({
        "order_id": [1, 2, 3, 3, 4, 5, 6],
        "customer": ["Ania", "Tomek", "Kasia", "Kasia", "Marek", "Ola", None],
        "price": [100.50, 20.00, 50.00, 50.00, 10.00, 300.00, 50.0],
        "quantity": [1, 3, 2, 2, 1, 1, 2]
    })
    result = create_revenue_column(df)

    assert "revenue" in result.columns
    assert (result["revenue"] == result["price"] * result["quantity"]).all()
    assert len(result) == len(df)
    assert result["revenue"].iloc[0] == 100.50


def test_segment_customers_by_revenue():
    df = pd.DataFrame({
        "order_id": [1, 2, 3, 3, 4, 5, 6],
        "customer": ["Ania", "Tomek", "Kasia", "Kasia", "Marek", "Ola", None],
        "price": [100.50, 20.00, 50.00, 50.00, 10.00, 300.00, 50.0],
        "quantity": [1, 3, 2, 2, 1, 1, 2]
    })
    df["revenue"] = df["price"] * df["quantity"]
    result = segment_customers_by_revenue(df)

    assert "category" in result.columns
    assert result.loc[result["revenue"] > 100, "category"].eq("High").all()
    assert result.loc[result["revenue"] <= 100, "category"].eq("Low").all()


def test_trasnform_data_end_to_end():
    df = pd.DataFrame({
        "order_id": [1, 2, 3, 3, 4, 5, 6],
        "customer": ["Ania", "Tomek", "Kasia", "Kasia", "Marek", "Ola", None],
        "price": ["100.50", "20.00", "50.00", "50.00", "-10.00", "300.00", "50.0"],
        "quantity": [1, 3, 2, 2, 1, 1, 2]
    })
    result = transform_data(df)

    assert result.duplicated().sum() == 0
    assert result["customer"].isna().sum() == 0
    assert (result["price"] > 0).all()
    assert (result["quantity"] > 0).all()
    assert "revenue" in result.columns
    assert "category" in result.columns
