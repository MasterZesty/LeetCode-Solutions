# Write your MySQL query statement below
with price_product  as (
select
b.product_id,
a.purchase_date,
a.units,
b.price,
a.units*b.price as selling_price
from prices b
left join unitssold a
on a.product_id = b.product_id and purchase_date between start_date and end_date
)

select
product_id,
COALESCE( ROUND( sum(selling_price) / NULLIF(sum(units), 0), 2) , 0) as average_price
 from 
price_product
group by
product_id