1# Write your MySQL query statement below
2with cte as
3(
4SELECT
5name,
6continent,
7row_number() over(partition by continent order by name) as rn
8from student
9)
10
11select
12max(case when continent= 'America' then name end) as America,
13max(case when continent= 'Asia' then name end) as Asia,
14max(case when continent= 'Europe' then name end) as Europe
15from
16cte
17group by rn