# Write your MySQL query statement below
with player_first_login as (
select
player_id,
min(event_date) as first_login
from
activity
group by
player_id
)

, cte2 as (
select 
a.*,
fl.first_login,
DATEDIFF(a.event_date, fl.first_login) AS interval_diff,
dense_rank() over(partition by player_id order by event_date) as drnk
from activity a
inner join player_first_login fl
on a.player_id = fl.player_id
)

, cte3 as (
select 
count(distinct case when drnk = 2 and interval_diff = 1 then player_id end) * 1.0 as no_of_next_day_logins,
count(distinct player_id) as total_players
from cte2
)

select
round(no_of_next_day_logins/total_players, 2) as fraction
from cte3

-- select * from cte2