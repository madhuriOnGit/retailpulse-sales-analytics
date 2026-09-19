-- 04_customer_analysis.sql
-- Customer segmentation analysis.

USE retailpulse;

SELECT
    customer_segment,
    COUNT(DISTINCT order_id) AS total_orders,
    SUM(sales_amount) AS segment_sales,
    AVG(sales_amount) AS avg_order_value
FROM sales
GROUP BY customer_segment
ORDER BY segment_sales DESC;
