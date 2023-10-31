# Write your MySQL query statement below

with direct_report as (
    select managerId , count(id) as direct_reports from employee
group by managerId
)

select a.name from employee a left join direct_report b
on 
a.id = b.managerId 
where b.direct_reports >= 5