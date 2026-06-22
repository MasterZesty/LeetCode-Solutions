# Write your MySQL query statement below
with cte as
(
SELECT
name,
continent,
row_number() over(partition by continent order by name) as rn
from student
)

select
max(case when continent= 'America' then name end) as America,
max(case when continent= 'Asia' then name end) as Asia,
max(case when continent= 'Europe' then name end) as Europe
from
cte
group by rn