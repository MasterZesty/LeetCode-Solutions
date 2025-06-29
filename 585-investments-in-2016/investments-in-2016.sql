# Write your MySQL query statement below
with cte as 
(
select
pid,
tiv_2015,
tiv_2016,
count(concat(lat,lon)) over(partition by concat(lat, lon)) as count_dup,
count(tiv_2015) over(partition by tiv_2015) as count_2015
from
insurance
)

select
round(sum(tiv_2016), 2) as tiv_2016 
from
cte
where
count_dup = 1
and count_2015 > 1
-- group by 
-- tiv_2016 