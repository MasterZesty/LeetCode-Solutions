# Write your MySQL query statement below
select
employee_id
from
employees
where salary < 30000
and manager_id not in (select distinct employee_id from employees where employee_id is not null)
order by employee_id