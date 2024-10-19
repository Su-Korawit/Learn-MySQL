UPDATE product
SET is_necessary = 0
-- WHERE id = 0
WHERE price < 500;

SELECT *
FROM product;