
-- CREATE DATABASE IF NOT EXISTS customer_shopping;
-- USE customer_shopping;


-- USE customer_shopping;

-- SELECT COUNT(*) AS total_rows
-- FROM shopping_data;

-- SELECT *
-- FROM shopping_data
-- LIMIT 5;


-- USE customer_shopping;

-- SELECT COUNT(*) AS total_rows
-- FROM shopping_data;



-- SELECT
--     Category,
--     COUNT(*) AS total_purchases,
--     ROUND(AVG(`Purchase Amount (USD)`), 2) AS avg_purchase
-- FROM shopping_data
-- GROUP BY Category
-- ORDER BY total_purchases DESC;


-- SELECT COUNT(*) AS total_rows
-- FROM shopping_data;


-- SELECT
--     Gender,
--     COUNT(*) AS total_purchases,
--     ROUND(AVG(`Purchase Amount (USD)`), 2) AS avg_purchase
-- FROM shopping_data
-- GROUP BY Gender
-- ORDER BY total_purchases DESC;


-- SELECT
--     `Payment Method`,
--     COUNT(*) AS total_purchases,
--     ROUND(AVG(`Purchase Amount (USD)`), 2) AS avg_purchase
-- FROM shopping_data
-- GROUP BY `Payment Method`
-- ORDER BY total_purchases DESC;



-- SELECT
--     `Discount Applied`,
--     COUNT(*) AS total_purchases,
--     ROUND(AVG(`Purchase Amount (USD)`), 2) AS avg_purchase
-- FROM shopping_data
-- GROUP BY `Discount Applied`;



-- SELECT
--     Season,
--     COUNT(*) AS total_purchases,
--     ROUND(AVG(`Purchase Amount (USD)`), 2) AS avg_purchase
-- FROM shopping_data
-- GROUP BY Season
-- ORDER BY total_purchases DESC;



-- SELECT
--     Location,
--     COUNT(*) AS total_purchases,
--     ROUND(AVG(`Purchase Amount (USD)`), 2) AS avg_purchase
-- FROM shopping_data
-- GROUP BY Location
-- ORDER BY total_purchases DESC
-- LIMIT 10;









