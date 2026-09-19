-- 01_database_setup.sql
-- Create the database schema for the retail analytics project.

CREATE DATABASE IF NOT EXISTS retailpulse;
USE retailpulse;

CREATE TABLE IF NOT EXISTS sales (
    order_id VARCHAR(50) PRIMARY KEY,
    order_date DATE,
    region VARCHAR(50),
    channel VARCHAR(50),
    product_category VARCHAR(50),
    customer_segment VARCHAR(50),
    quantity INT,
    unit_price DECIMAL(10,2),
    discount_percent DECIMAL(5,2),
    sales_amount DECIMAL(12,2),
    profit_amount DECIMAL(12,2),
    profit_margin DECIMAL(5,3)
);

CREATE TABLE IF NOT EXISTS customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_segment VARCHAR(50),
    region VARCHAR(50),
    customer_name VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_category VARCHAR(50),
    product_name VARCHAR(100),
    unit_price DECIMAL(10,2)
);
