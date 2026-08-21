# Write your MySQL query statement below
with success_cte as (
select
'succeeded' as period_state,
success_date,
DATE_SUB(success_date, INTERVAL ROW_NUMBER() OVER(ORDER BY success_date) DAY) as grp
from
Succeeded
where
success_date between '2019-01-01' AND '2019-12-31'
),

fail_cte as (
select
'failed' as period_state,
fail_date,
DATE_SUB(fail_date, INTERVAL ROW_NUMBER() OVER(ORDER BY fail_date) DAY) as grp
from
Failed
where
fail_date between '2019-01-01' AND '2019-12-31'
)

, report_stg as (
select
period_state,
min(success_date) as start_date,
max(success_date) as end_date
 from success_cte
 group by
grp
union all
select
period_state,
min(fail_date) as start_date,
max(fail_date) as end_date
 from fail_cte
 group by
grp
)


select
period_state,
start_date,
end_date
from
report_stg
order by start_date