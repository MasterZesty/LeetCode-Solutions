# Write your MySQL query statement below
-- Gaps and Islands in SQL: Techniques & Examples : https://www.red-gate.com/simple-talk/databases/sql-server/t-sql-programming-sql-server/introduction-to-gaps-and-islands-analysis/#related-content
 with ds as (
 select
 log_id,
 log_id - ROW_NUMBER() OVER(ORDER BY log_id) as island_qty
 from
 logs
)


select 
min(log_id) as start_id,
max(log_id) as end_id
 from ds
 group by
 island_qty
