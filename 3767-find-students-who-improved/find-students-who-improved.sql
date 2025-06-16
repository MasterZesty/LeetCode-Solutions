# Write your MySQL query statement below
with score_date as
(
select 
student_id,
min(exam_date) as first_date,
max(exam_date) as last_date,
subject
from
scores
group by
student_id,
subject
),

improvement_studens as (
select 
a.student_id,
a.subject,
b.score as first_score,
c.score as latest_score,
case when c.score > b.score then 1 else 0 end as flag_improvement
from score_date a
left join scores b
on a.student_id = b.student_id and a.subject=b.subject and a.first_date=b.exam_date
left join scores c
on a.student_id = c.student_id and a.subject=c.subject and a.last_date=c.exam_date
)

select 
student_id,
subject,
first_score,
latest_score
from
improvement_studens
where 
flag_improvement = 1
order by student_id, subject