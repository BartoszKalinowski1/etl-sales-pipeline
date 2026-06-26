CREATE SCHEMA IF NOT EXISTS sales;
SET search_path TO sales;

CREATE TABLE sales_raw(
    order_id INT PRIMARY KEY,
    customer_id INT,
    product TEXT,
    quantity INT,
    order_date DATE,
    region TEXT,
    price NUMERIC
);

CREATE TABLE sales_clean(
    order_id INT PRIMARY KEY,
    customer_id INT,
    product TEXT,
    quantity INT,
    order_date DATE,
    region TEXT,
    price NUMERIC,
    revenue NUMERIC,
    category TEXT
);

CREATE TABLE customer_segments(
    customer_id INT PRIMARY KEY,
    total_orders INT,
    total_revenue NUMERIC,
    category TEXT
);