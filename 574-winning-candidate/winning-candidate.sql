# Write your MySQL query statement below
with vote_per_candidate as (
select
a.name,
a.id,
count(b.id) as total_votes
from
vote b
left join 
candidate a
on a.id = b.candidateid
group by candidateid
),

candidate_rn AS (
select
name,
row_number() over(order by total_votes desc) as rn
from
vote_per_candidate
)

select
name
from candidate_rn
where rn=1