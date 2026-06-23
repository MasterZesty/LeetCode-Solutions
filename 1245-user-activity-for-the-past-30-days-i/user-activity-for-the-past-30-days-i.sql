# Write your MySQL query statement below
select
activity_date as day,
count(distinct user_id) as active_users
from
activity
where activity_date BETWEEN DATE_SUB("2019-07-27", INTERVAL 29 DAY) and "2019-07-27"
group by
activity_date