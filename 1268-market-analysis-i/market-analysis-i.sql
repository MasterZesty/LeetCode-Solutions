select
a.user_id as buyer_id,
a.join_date,
count(b.order_id) as orders_in_2019
from users a
left join orders b
on a.user_id = b.buyer_id and  year(b.order_date)='2019'
group by
a.user_id