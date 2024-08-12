# Write your MySQL query statement below

with ranked_score as (
select score, DENSE_RANK() OVER(ORDER BY score DESC) AS rnk FROM Scores
)

select score, rnk as "rank" from ranked_score