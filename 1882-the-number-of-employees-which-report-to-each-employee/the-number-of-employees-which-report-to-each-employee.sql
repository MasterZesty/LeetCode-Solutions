# Write your MySQL query statement below
with cte as (
select
distinct
reports_to,
count(employee_id) over(partition by reports_to order by reports_to) as reports_count,
avg(age) over(partition by reports_to order by reports_to) as average_age
from
employees
where reports_to is not null
)

select
b.employee_id,
b.name,
a.reports_count,
round(a.average_age) as average_age
from cte a
inner join employees b
on a.reports_to = b.employee_id
order by employee_id