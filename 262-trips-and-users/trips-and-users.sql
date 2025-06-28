# Write your MySQL query statement below
with cte as (
select
id,
case when a.status in ("cancelled_by_driver", "cancelled_by_client") then 1 else 0 end as is_cancelled,
client_id,
driver_id,
city_id,
status,
request_at
from
trips a
left join users b
on a.client_id = b.users_id
left join users c
on a.driver_id = c.users_id
where
b.banned != "Yes"
and c.banned != "Yes"
-- and a.status in ("cancelled_by_driver", "cancelled_by_client")
)


, cte2 as (
select
request_at as Day,
sum(is_cancelled) over(partition by request_at order by request_at) as n_cancelled,
count(id) over(partition by request_at order by request_at) as n_total
from 
cte
where request_at between "2013-10-01" and "2013-10-03"
)


select
distinct
Day,
round(n_cancelled / n_total, 2) as 'Cancellation Rate'
from cte2