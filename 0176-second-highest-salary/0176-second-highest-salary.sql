# Write your MySQL query statement below
/*
ask is to get the second hightest salary. diff ids can have same salary
so some kind of  raning is required and that too considering tie we shoud
assign same rank to same salary 
so appropriate function shoud be dense rank
and dense_rank = 2 desc order salary
*/

WITH salary_rank AS (
    SELECT
        salary,
        DENSE_RANK() OVER (ORDER BY salary DESC) AS d_rnk
    FROM Employee
)

SELECT
    MAX(salary) AS SecondHighestSalary
FROM salary_rank
WHERE d_rnk = 2
