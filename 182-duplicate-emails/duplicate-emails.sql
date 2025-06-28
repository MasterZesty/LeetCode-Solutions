# Write your MySQL query statement below

with duplicate_emails as (
select
email,
row_number() over(partition by email order by email) as rn
from 
person
)

select email from duplicate_emails
where rn = 2