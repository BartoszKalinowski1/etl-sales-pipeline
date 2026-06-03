import pandas as pd
from src.quality_checks import count_null, check_df_length, check_price_values, \
    check_revenue_values, check_duplicates, check_revenue_column


def test_count_null_returns_true_when_no_nulls():
    df_without_null = pd.DataFrame({
        "order_id": [1, 2, 3, 3, 4, 5],
        "customer": ["Ania", "Tomek", "Kasia", "Kasia", "Marek", "Ola"],
        "price": ["100.50", "20.00", "50.00", "50.00", "-10.00", "300.00"],
        "quantity": [1, 3, 2, 2, 1, 1]
    })
    assert count_null(df_without_null) is True


def test_count_null_returns_false_when_nulls_exist():
    df_with_null = pd.DataFrame({
        "order_id": [1, 2, 3, 3, 4, 5, 6],
        "customer": ["Ania", "Tomek", "Kasia", "Kasia", "Marek", "Ola", None],
        "price": ["100.50", "20.00", "50.00", "50.00", "-10.00", "300.00", "50.0"],
        "quantity": [1, 3, 2, 2, 1, 1, 2]
    })
    assert count_null(df_with_null) is False


def test_check_df_length_returns_true_when_not_empty():
    df = pd.DataFrame({
        "order_id": [1, 2, 3, 3, 4, 5],
        "customer": ["Ania", "Tomek", "Kasia", "Kasia", "Marek", "Ola"],
        "price": ["100.50", "20.00", "50.00", "50.00", "-10.00", "300.00"],
        "quantity": [1, 3, 2, 2, 1, 1]
    })
    assert check_df_length(df) is True


def test_check_df_length_returns_false_when_empty():
    df = pd.DataFrame({})
    assert check_df_length(df) is False


def test_check_price_values_returns_true_when_prices_float():
    df = pd.DataFrame({
        "price": [100.50, 20.00, 50.00, 50.00, -10.00, 300.00],
    })
    assert check_price_values(df) is True


def test_check_price_values_returns_false_when_prices_not_float():
    df = pd.DataFrame({
        "price": ["100.50", "20.00", "50.00", "50.00", "-10.00", "300.00"],
    })
    assert check_price_values(df) is False


def test_check_revenue_values_returns_true_when_revenue_float():
    df = pd.DataFrame({
        "revenue": [100.50, 20.00, 50.00, 50.00, -10.00, 300.00],
    })
    assert check_revenue_values(df) is True


def test_check_revenue_values_returns_false_when_revenue_not_float():
    df = pd.DataFrame({
        "revenue": ["100.50", "20.00", "50.00", "50.00", "-10.00", "300.00"],
    })
    assert check_revenue_values(df) is False


def test_check_duplicates_returns_true_when_no_duplicates():
    df = pd.DataFrame({
        "order_id": [1, 2, 3, 4, 5, 6],
        "customer": ["Ania", "Tomek", "Kasia", "Marek", "Ola", None],
        "price": ["100.50", "20.00", "50.00", "-10.00", "300.00", "50.0"],
        "quantity": [1, 3, 2, 1, 1, 2]
    })
    assert check_duplicates(df) is True


def test_check_duplicates_returns_false_when_duplicates():
    df = pd.DataFrame({
        "order_id": [1, 2, 3, 3, 4, 5, 6],
        "customer": ["Ania", "Tomek", "Kasia", "Kasia", "Marek", "Ola", None],
        "price": ["100.50", "20.00", "50.00", "50.00", "-10.00", "300.00", "50.0"],
        "quantity": [1, 3, 2, 2, 1, 1, 2]
    })
    assert check_duplicates(df) is False


def test_check_revenue_column_returns_true_when_revenue_is_in_columns():
    df = pd.DataFrame({
        "order_id": [1, 2, 3, 3, 4, 5, 6],
        "customer": ["Ania", "Tomek", "Kasia", "Kasia", "Marek", "Ola", None],
        "price": [100.50, 20.00, 50.00, 50.00, -10.00, 300.00, 50.0],
        "quantity": [1, 3, 2, 2, 1, 1, 2],
        "revenue": [100.50, 60.00, 100.00, 100.00, -10.00, 300.00, 100.0]
    })
    assert check_revenue_column(df) is True


def test_check_revenue_column_returns_false_when_revenue_not_in_columns():
    df = pd.DataFrame({
        "order_id": [1, 2, 3, 3, 4, 5, 6],
        "customer": ["Ania", "Tomek", "Kasia", "Kasia", "Marek", "Ola", None],
        "price": [100.50, 20.00, 50.00, 50.00, -10.00, 300.00, 50.0],
        "quantity": [1, 3, 2, 2, 1, 1, 2]
    })
    assert check_revenue_column(df) is False
