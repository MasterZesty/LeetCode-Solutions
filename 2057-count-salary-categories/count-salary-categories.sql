# Write your MySQL query statement below


with sal_cat as (
select
account_id,
income,
CASE 
    WHEN income < 20000 THEN "Low Salary"
    WHEN income >= 20000 AND income <= 50000 THEN "Average Salary"
    WHEN income > 50000 THEN "High Salary"
END AS category
from
accounts
),

category_ds as (
select "Low Salary" as category
union
select "Average Salary" as category
union
select "High Salary" as category
)

, sal_cat_count as (
select
category,
count(category) as accounts_count
from sal_cat
group by
category
)

select a.category, coalesce(b.accounts_count,0) as accounts_count from category_ds a left join sal_cat_count b
on a.category = b.category