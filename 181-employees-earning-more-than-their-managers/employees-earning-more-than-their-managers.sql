-- SELECT name
-- FROM Employee 
-- WHERE managerId is not null AND salary > (SELECT salary FROM Employee WHERE id = managerId)


SELECT e1.name AS Employee 
FROM Employee e1 
LEFT JOIN Employee e2 ON e2.id = e1.managerId 
WHERE e2.salary < e1.salary