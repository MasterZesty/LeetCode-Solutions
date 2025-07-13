# Write your MySQL query statement below

WITH cte AS (
select distinct
EXTRACT(YEAR_MONTH FROM trans_date) as month,
country,
count(id) over(partition by country, EXTRACT(YEAR_MONTH FROM trans_date) order by country, EXTRACT(YEAR_MONTH FROM trans_date)) as trans_count,
sum(amount) over(partition by country, EXTRACT(YEAR_MONTH FROM trans_date) order by country, EXTRACT(YEAR_MONTH FROM trans_date)) as trans_total_amount,
SUM(CASE WHEN state = "approved" THEN 1 ELSE 0 END ) over(partition by country, EXTRACT(YEAR_MONTH FROM trans_date) order by country, EXTRACT(YEAR_MONTH FROM trans_date)) as approved_count,
sum(CASE WHEN state = "approved" THEN amount ELSE 0 END ) over(partition by country, EXTRACT(YEAR_MONTH FROM trans_date) order by country, EXTRACT(YEAR_MONTH FROM trans_date)) as approved_total_amount
from
transactions
)

select
CONCAT(SUBSTR(month, 1, 4), '-', SUBSTR(month, 5, 2)) as month,
country,
trans_count,
approved_count,
trans_total_amount,
approved_total_amount
from cte