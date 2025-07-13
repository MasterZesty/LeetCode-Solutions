# Write your MySQL query statement below

with cte as (
select
delivery_id,
customer_id,
order_date,
customer_pref_delivery_date,
row_number() over(partition by customer_id order by order_date asc ) as rn
from
delivery
)

select 
round(SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) / SUM(rn) *100, 2) as immediate_percentage
 from cte
 where rn = 1
-- where order_date = customer_pref_delivery_date