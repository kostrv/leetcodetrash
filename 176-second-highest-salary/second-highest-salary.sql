-- SELECT salary AS SecondHighestSalary FROM
-- (SELECT 
--     id,
--     salary, 
--     DENSE_RANK() OVER(ORDER BY salary DESC) AS salary_rank 
-- FROM Employee e
-- )t
-- WHERE salary_rank = 2



-- SELECT salary AS SecondHighestSalary
-- FROM Employee
-- ORDER BY salary DESC 
-- LIMIT 1,1

SELECT MAX(salary) AS SecondHighestSalary

FROM Employee

WHERE salary < (

    SELECT MAX(salary)

    FROM Employee

)