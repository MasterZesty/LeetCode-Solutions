# Write your MySQL query statement below
with dist_point as (
select
-- p1.x,
-- p1.y,
-- p2.x,
-- p2.y,
SQRT((POW(p1.x-p2.x, 2) + POW(p1.y-p2.y, 2))) as distance
from
point2d p1
join
point2d p2
ON
p1.x != p2.x or p1.y != p2.y
)

select
ROUND(min(distance),2) as shortest 
from
dist_point