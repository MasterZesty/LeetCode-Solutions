# Write your MySQL query statement below
select
s.student_id,
s.student_name,
t.subject_name,
SUM(CASE WHEN e.subject_name IS NOT NULL THEN 1 ELSE 0 END) AS attended_exams 
from
students s
INNER join subjects t
on 1 = 1
left join Examinations e
on e.student_id = s.student_id AND t.subject_name = e.subject_name 
group by
s.student_id,
t.subject_name
order by
student_id,
subject_name