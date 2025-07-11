# Write your MySQL query statement below
with cte as (
select
id,
student,
CASE WHEN id % 2 != 0 THEN id + 1 ELSE id - 1 END AS logic_id
from
seat
)

select
a.id,
coalesce(b.student, a.student ) as student
from cte a
left join seat b
on a.logic_id = b.id
order by id