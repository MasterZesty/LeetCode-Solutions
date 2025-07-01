# Write your MySQL query statement below
with cte as (
select
id,
LEAD(id, 1) over(order by id) as second_id,
LEAD(id, 2) over(order by id) as third_id,
people as first_people,
LEAD(people, 1) OVER (ORDER BY id) AS second_people,
LEAD(people, 2) OVER (ORDER BY id) AS third_people
from
stadium
)
-- where
-- people >= 100
-- and (select people from stadium where id = id + 1) >= 100
-- and (select people from stadium where id = id + 2) >= 100
, cte2 as (
select id
from
cte
where
first_people >= 100
and second_people >= 100
and third_people >= 100
union all
select second_id as id
from
cte
where
first_people >= 100
and second_people >= 100
and third_people >= 100
union all
select third_id as id
from
cte
where
first_people >= 100
and second_people >= 100
and third_people >= 100
)


select id, visit_date, people
from
stadium
where
id in (select distinct id from cte2)
order by visit_date