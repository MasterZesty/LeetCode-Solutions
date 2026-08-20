# Write your MySQL query statement below
with recursive cte as (
  select 1 as num
  union all
  select num + 1 as num from cte where num < (select max(customer_id) from Customers)
)

select 
a.num as ids 
from cte a
left join customers b
on b.customer_id  = a.num
where b.customer_id is null