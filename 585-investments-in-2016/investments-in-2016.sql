
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE tiv_2015 IN (
    -- Условие 1: tiv_2015 должен повторяться
    SELECT tiv_2015 
    FROM Insurance 
    GROUP BY tiv_2015 
    HAVING COUNT(*) > 1
)
AND (lat, lon) IN (
    -- Условие 2: локация должна быть уникальной (встречается только 1 раз)
    SELECT lat, lon 
    FROM Insurance 
    GROUP BY lat, lon 
    HAVING COUNT(*) = 1
);


-- SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
-- FROM (
--     SELECT 
--         tiv_2016,
--         COUNT(*) OVER(PARTITION BY tiv_2015) AS count_tiv_2015,
--         COUNT(*) OVER(PARTITION BY lat, lon) AS count_location
--     FROM Insurance
-- ) AS sub
-- WHERE count_tiv_2015 > 1 AND count_location = 1;