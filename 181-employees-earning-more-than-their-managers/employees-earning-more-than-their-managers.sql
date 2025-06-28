# Write your MySQL query statement below
with stg as
(
select
emp.name as emp_name,
emp.salary as emp_sal,
mgr.salary as mgr_sal
from employee emp
inner join employee mgr
on emp.managerid = mgr.id
)

select emp_name as Employee  from stg 
where 
emp_sal > mgr_sal