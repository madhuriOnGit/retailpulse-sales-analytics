-- 02_data_quality.sql
-- Validate data quality checks for sales data.

USE retailpulse;

SELECT COUNT(*) AS total_rows,
       COUNT(DISTINCT order_id) AS unique_orders,
       COUNT(CASE WHEN sales_amount IS NULL THEN 1 END) AS null_sales_amounts,
       COUNT(CASE WHEN quantity <= 0 THEN 1 END) AS invalid_quantities,
       COUNT(CASE WHEN unit_price <= 0 THEN 1 END) AS invalid_unit_prices
FROM sales;

SELECT *
FROM sales
WHERE quantity <= 0 OR unit_price <= 0 OR sales_amount IS NULL;
