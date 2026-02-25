# Write your MySQL query statement below

-- SELECT DISTINCT salary AS SecondHighestSalary 
-- FROM Employee
-- ORDER BY salary DESC 
-- LIMIT 1, 1

SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (
    SELECT MAX(salary)
    FROM Employee
)


-- SELECT salary AS SecondHighestSalary FROM (
--     SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS salary_rank
--     FROM Employee
-- ) T
-- WHERE salary_rank = 2