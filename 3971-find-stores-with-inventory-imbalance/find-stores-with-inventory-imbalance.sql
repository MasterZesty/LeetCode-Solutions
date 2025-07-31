# Write your MySQL query statement below

with inv_imbal as (
select
a.store_id,
store_name,
location,
first_value(product_name) over(partition by store_id order by price desc) as most_exp_product,
first_value(product_name) over(partition by store_id order by price asc) as cheapest_product,
first_value(quantity) over(partition by store_id order by price desc) as most_exp_product_quantity,
first_value(quantity) over(partition by store_id order by price asc) as cheapest_product_quantity,
count(inventory_id) over(partition by store_id) as num_of_distinct_products,
row_number() over(partition by store_id order by inventory_id ) as rn
from
inventory a
inner join stores b
on a.store_id = b.store_id
)

select
store_id,
store_name,
location,
most_exp_product,
cheapest_product,
round(cheapest_product_quantity/most_exp_product_quantity, 2) as imbalance_ratio
from
inv_imbal
where
num_of_distinct_products >= 3 and rn = 1 and most_exp_product_quantity  < cheapest_product_quantity
order by imbalance_ratio desc, store_name asc