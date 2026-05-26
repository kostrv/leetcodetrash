
-- SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016 
-- FROM Insurance
-- WHERE pid IN 
-- (
--     SELECT pid
--     FROM Insurance 
--     GROUP BY lat, lon
--     HAVING COUNT(*) = 1
-- )
-- GROUP BY tiv_2015 


SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM (
    SELECT 
        tiv_2016,
        COUNT(*) OVER(PARTITION BY tiv_2015) AS count_tiv_2015,
        COUNT(*) OVER(PARTITION BY lat, lon) AS count_location
    FROM Insurance
) AS sub
WHERE count_tiv_2015 > 1 AND count_location = 1;