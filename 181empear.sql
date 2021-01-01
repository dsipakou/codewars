# Write your MySQL query statement below
SELECT t2.Name as Employee from Employee t1, Employee t2 
WHERE t1.Id = t2.ManagerId AND t1.Salary < t2.Salary
