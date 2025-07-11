# Write your MySQL query statement below
with cte as (
select
a.user_id,
a.product_id,
b.category,
a.quantity*b.price as amount
from ProductPurchases a
inner join ProductInfo b
on a.product_id = b.product_id

)
, cte2 as (
select distinct
a.user_id,
a.product_id as product_id_c1,
a.category as category1,
-- b.user_id,
b.product_id as product_id_c2,
b.category as category2
 from cte a
left join cte b
on a.user_id = b.user_id AND a.product_id  != b.product_id
 and a.category < b.category -- Ensures each product pair is only counted once (avoids duplicate and reverse pairs like A-B and B-A).
)

select
category1,
category2,
COUNT(DISTINCT user_id) as customer_count
from cte2
where category2 is not null
group by
category1,
category2
having COUNT(DISTINCT user_id) >=3
order by customer_count desc, category1, category2