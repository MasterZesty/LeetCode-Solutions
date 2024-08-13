# Write your MySQL query statement below
with emp_dept_ds as
(
select d.name as Department, e.name as Employee, e.salary as Salary,
DENSE_RANK() OVER(PARTITION BY d.name ORDER BY e.salary DESC) as salary_rnk
from Employee e left join Department d
on e.departmentId = d.id
)

select Department, Employee, Salary from emp_dept_ds where salary_rnk = 1