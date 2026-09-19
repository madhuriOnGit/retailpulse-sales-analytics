-- 07_regional_analysis.sql
-- Regional business analysis.

USE retailpulse;

SELECT
    region,
    channel,
    SUM(sales_amount) AS regional_channel_sales,
    SUM(profit_amount) AS regional_channel_profit
FROM sales
GROUP BY region, channel
ORDER BY region, regional_channel_sales DESC;
