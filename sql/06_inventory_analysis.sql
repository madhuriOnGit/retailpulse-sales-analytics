-- 06_inventory_analysis.sql
-- Inventory and stock movement insights.

USE retailpulse;

SELECT
    product_category,
    SUM(quantity) AS units_sold,
    ROUND(AVG(unit_price), 2) AS avg_unit_price,
    ROUND(SUM(sales_amount), 2) AS sales_value
FROM sales
GROUP BY product_category
ORDER BY units_sold DESC;
