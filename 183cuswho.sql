# Write your MySQL query statement below
SELECT c.Name as Customers FROM Customers as c
LEFT JOIN Orders as o ON o.CustomerId = c.Id
WHERE o.CustomerId is NULL
