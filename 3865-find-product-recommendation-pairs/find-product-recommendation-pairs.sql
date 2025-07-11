# Write your MySQL query statement below
with cte as (
select
a.user_id,
a.product_id as product1_id,
b.product_id as product2_id,
c.category as product1_category,
d.category as product2_category
from ProductPurchases a
left join ProductInfo c
on a.product_id = c.product_id
left join ProductPurchases b
on a.user_id = b.user_id and a.product_id < b.product_id
left join ProductInfo d
on b.product_id = d.product_id
where b.product_id is not null
)

select
product1_id,
product2_id,
product1_category,
product2_category,
count(distinct user_id) as customer_count
from cte
group by
product1_id,
product2_id,
product1_category,
product2_category
having customer_count >=3
order by customer_count desc, product1_id, product2_id