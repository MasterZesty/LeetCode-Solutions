# Write your MySQL query statement below
with review_no as (
select
employee_id,
NTH_VALUE(rating, 1) over w as latest_reviw_rating,
NTH_VALUE(rating, 2) over w as second_latest_reviw_rating,
NTH_VALUE(rating, 3) over w as third_latest_reviw_rating,
row_number() over(partition by employee_id) as rn
from
performance_reviews
window w as (partition by employee_id order by review_date desc range between unbounded preceding and unbounded following)
)

select
review_no.employee_id ,
emp.name,
latest_reviw_rating - third_latest_reviw_rating as improvement_score
from 
review_no
inner join employees emp
on emp.employee_id = review_no.employee_id
where rn = 1 
and latest_reviw_rating is not null
and second_latest_reviw_rating is not null
and third_latest_reviw_rating is not null
and latest_reviw_rating > second_latest_reviw_rating
and second_latest_reviw_rating > third_latest_reviw_rating
order by improvement_score desc, name asc