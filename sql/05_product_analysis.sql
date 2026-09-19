-- 05_product_analysis.sql
-- Product category performance.

USE retailpulse;

SELECT
    product_category,
    SUM(quantity) AS total_units_sold,
    SUM(sales_amount) AS category_revenue,
    SUM(profit_amount) AS category_profit
FROM sales
GROUP BY product_category
ORDER BY category_revenue DESC;
