# Write your MySQL query statement below

SELECT IFNULL((select salary as SecondHighestSalary from employee where salary <> (select max(salary) from employee) order by salary desc  limit 1), NULL) as SecondHighestSalary