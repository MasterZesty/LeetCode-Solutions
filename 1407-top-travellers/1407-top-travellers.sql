# Write your MySQL query statement below
# Users
# Rides

with temp as (SELECT a.name as name,COALESCE(b.travelled_distance,0) as travelled_distance FROM Users a left join  (select user_id, sum(distance) as travelled_distance from Rides group by user_id) b on a.id=b.user_id)
select name, travelled_distance from temp order by travelled_distance desc,name asc;