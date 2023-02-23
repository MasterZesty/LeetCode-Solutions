# Write your MySQL query statement below
with temp as (select customer_number, count(order_number) as num_of_order from Orders group by customer_number) 
select customer_number from temp order by num_of_order desc limit 1;