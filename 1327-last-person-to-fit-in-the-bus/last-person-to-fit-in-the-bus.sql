# Write your MySQL query statement below
with cte as (
select
person_id,
person_name,
turn,
sum(weight) over(order by turn asc) as running_sum_of_weight
from
queue
)

select person_name from cte where turn = (select max(turn) from cte where running_sum_of_weight <= 1000)
