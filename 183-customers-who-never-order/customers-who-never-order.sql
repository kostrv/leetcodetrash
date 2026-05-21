# Write your MySQL query statement below

-- SELECT name AS Customers FROM customers
-- WHERE id NOT IN (SELECT customerID FROM orders)


SELECT name AS Customers
FROM customers c
LEFT JOIN orders o ON c.id = o.customerID
WHERE o.id IS NULL