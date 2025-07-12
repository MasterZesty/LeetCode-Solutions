# Write your MySQL query statement below
with cte as (
select
sale_id,
product_id,
year,
quantity,
price,
dense_rank() over(partition by product_id order by year) as rn
from sales
)

select
product_id,
year as first_year,
sum(quantity) as quantity,
price
from cte
where rn=1
group by
product_id,
year,
quantity,
price

-- select * from cte where rn = 1