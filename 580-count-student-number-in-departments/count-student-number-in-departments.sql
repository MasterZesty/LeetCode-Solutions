# Write your MySQL query statement below
with dept_count as (
select
dept_id,
count(student_id) as student_number
from
Student
group by
dept_id
)

select
d.dept_name,
IFNULL(c.student_number, 0) as student_number
from
Department d
LEFT JOIN dept_count c
on d.dept_id = c.dept_id
order by 
student_number DESC, dept_name ASC