-- 03_sales_analysis.sql
-- Sales performance overview.

USE retailpulse;

SELECT
    order_date,
    SUM(sales_amount) AS total_sales,
    SUM(profit_amount) AS total_profit,
    AVG(profit_margin) AS avg_profit_margin
FROM sales
GROUP BY order_date
ORDER BY order_date;

SELECT
    region,
    SUM(sales_amount) AS revenue,
    SUM(profit_amount) AS profit,
    ROUND(AVG(profit_margin), 3) AS avg_margin
FROM sales
GROUP BY region
ORDER BY revenue DESC;
