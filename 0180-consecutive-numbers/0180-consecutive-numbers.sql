# Write your MySQL query statement below

with grp_t as 
(

select id, num,
( id + 1 - row_number() over(partition by num order by id) ) as grp
from Logs

)

 
select distinct num as ConsecutiveNums
from grp_t
group by grp, num
having count(grp) >= 3