# Write your MySQL query statement below
with red_sellers as 
(
select
-- order_id,
sales_id
-- name
from
orders a
inner join company b
on a.com_id = b.com_id and b.name = "RED"
)

select name
from
salesperson
where sales_id not in (select distinct sales_id from red_sellers)