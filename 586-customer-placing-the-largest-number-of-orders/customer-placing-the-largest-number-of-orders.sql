# Write your MySQL query statement below
with customer_orders as (
select
customer_number,
COUNT(order_number) as no_of_orders
from
orders
group by
customer_number
),

customer_order_ranked as 
(
select
customer_number,
DENSE_RANK() OVER (ORDER BY no_of_orders DESC) as d_rnk
FROM
customer_orders
)

select
customer_number 
from
customer_order_ranked
where d_rnk = 1