# Write your MySQL query statement below
with cte as (
select
stock_name,
operation,
operation_day,
CASE WHEN operation = "Buy" THEN price*-1 ELSE price end as price
from
stocks
)


select
 stock_name,
 sum(price) as capital_gain_loss 
from cte
group by
stock_name