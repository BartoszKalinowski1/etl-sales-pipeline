INSERT INTO sales_raw(order_id, customer_id, product, quantity, order_date, region, price)
VALUES (%s, %s, %s, %s, %s, %s, %s);

INSERT INTO sales_clean(order_id, customer_id, product, quantity, order_date, region, price, revenue, category)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);

INSERT INTO customer_segments(customer_id, total_orders, total_revenue, category)
SELECT customer_id,
    COUNT(DISTINCT order_id) as total_orders,
    SUM(revenue) as total_revenue,
    category
FROM sales_clean
GROUP BY customer_id, category;