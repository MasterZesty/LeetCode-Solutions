# Write your MySQL query statement below
with clean_ds as (
select
distinct
customer_id,
product_key
from customer
),

cte as (
select
customer_id,
product_key,
dense_rank() over(partition by customer_id order by product_key) as drnk
from
clean_ds
)

select distinct customer_id from cte where drnk = (select count(product_key) from product)
-- select * from cte