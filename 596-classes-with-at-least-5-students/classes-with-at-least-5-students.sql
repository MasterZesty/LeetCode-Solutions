# Write your MySQL query statement below
with cte as (
select
class,
count(student) as no_of_student_in_class
from
courses
group by
class
)

select class from cte
where no_of_student_in_class >= 5