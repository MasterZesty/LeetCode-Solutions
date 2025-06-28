# Write your MySQL query statement below
with top_n_earners as (
select
e.id,
e.name,
d.name as department,
e.salary,
# row_numer() -- cannot use this
# rank() -- skip the numbering or gaps
# dense_rank -- will provide rank without gaps
dense_rank() over(partition by e.departmentid order by e.salary desc) as top_sal_n
from
employee e
left join department d
on e.departmentid = d.id
)


select department, name as employee, salary from top_n_earners
where top_sal_n <= 3
-- order by salary