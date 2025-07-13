# Write your MySQL query statement below
with 

cte1 AS (
    SELECT visited_on, SUM(amount) AS amount
    FROM Customer
    GROUP BY visited_on
),

cte as 
(
select
visited_on,
sum(amount) over(order by visited_on range between interval 6 day preceding and current row) as amount,
round( avg(amount) over(order by visited_on range between interval 6 day preceding and current row), 2) as average_amount,
ROW_NUMBER() OVER (ORDER BY visited_on) AS rn
-- RANGE BETWEEN INTERVAL '1' DAY PRECEDING AND CURRENT ROW
from
cte1

)

select 
visited_on,
amount,
average_amount
 from cte
where rn >= 7
order by visited_on
