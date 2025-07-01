# Write your MySQL query statement below
with cte as 
(
select
a.user_id,
b.name,
count(movie_id) as no_of_movies
from
MovieRating a
left join Users b
on a.user_id = b.user_id
group by
user_id
)

, cte2 as 
(
select
name,
row_number() over(order by no_of_movies desc, name asc) as rnk
from
cte
)


, cte3 as (
select
a.movie_id,
b.title,
avg(rating) as avg_rating
from movierating a
inner join movies b
on a.movie_id = b.movie_id and a.created_at between "2020-02-01" and "2020-02-29"
group by
a.movie_id
)

, cte4 as 
(
select
title,
avg_rating,
row_number() over(order by avg_rating desc, title asc) as rnk
from
cte3
)

select name as results from cte2 where rnk = 1
union all
select title as results from cte4 where rnk = 1