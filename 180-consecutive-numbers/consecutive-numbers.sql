# Write your MySQL query statement below
with cte as 
(
select
num,
lead(num,1) over(order by id) as next_num1,
lead(num,2) over(order by id) as next_num2
from
logs
)


select distinct num as ConsecutiveNums  from cte where num = next_num1 and num = next_num2