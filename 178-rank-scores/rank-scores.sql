# Write your MySQL query statement below

with ranked_score as (
select
score,
DENSE_RANK() OVER(ORDER BY score DESC) as "rank"
from
Scores
)

select
*
from
ranked_score 
order by score  desc