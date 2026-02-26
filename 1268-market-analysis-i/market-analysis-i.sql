-- SELECT buyer_id, join_date, COALESCE(orders_in_2019, 0) AS orders_in_2019
-- FROM (
-- SELECT buyer_id, SUM(CASE WHEN YEAR(order_date) = '2019' THEN 1 ELSE 0 END) as orders_in_2019  
-- FROM Orders
-- GROUP BY buyer_id
-- ) AS t
-- RIGHT JOIN Users u ON u.user_id = t.buyer_id
-- ORDER BY buyer_id ASC



SELECT user_id AS buyer_id, join_date, COALESCE(orders_in_2019, 0) AS orders_in_2019
FROM Users u
LEFT JOIN (
    SELECT buyer_id, SUM(CASE WHEN YEAR(order_date) = '2019' THEN 1 ELSE 0 END) as orders_in_2019  
    FROM Orders
    GROUP BY buyer_id
    ) t ON t.buyer_id = u.user_id
ORDER BY buyer_id ASC
