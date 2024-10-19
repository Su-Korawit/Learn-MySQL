-- Show all of table

-- SELECT *
-- FROM product;

-- Show only the desired column

-- SELECT title, is_necessary
-- FROM product; 

-- Show only data with the required values

-- SELECT *
-- FROM product
-- WHERE is_necessary = 1;

SELECT *
FROM product
-- WHERE price >= 1000;
-- WHERE price > 1000 and price < 5000
-- WHERE title LIKE "%โปรเจค%";

-- ORDER BY title ASC;   -- First TO End
ORDER BY create_at DESC  -- NEW TO OLD
-- LIMIT 2;                 
LIMIT 2 OFFSET 1; 		 -- Skip Row (Start at 0)