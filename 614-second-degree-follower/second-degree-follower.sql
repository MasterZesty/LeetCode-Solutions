# Write your MySQL query statement below
/*
we need to calculate for partuclar user how any folowers he has and how many people he follows
*/
with ds_user_followers as
(
SELECT
followee as user,
count(follower) as no_of_followers
from
follow
group by
followee
),

ds_user_followee as
(
SELECT
follower as user,
count(followee) as no_of_followees
from
follow
group by
follower
)

select coalesce(a.user, b.user) as follower, no_of_followers as num  from ds_user_followee a
left join ds_user_followers b
on a.user = b.user 
where no_of_followees >= 1 and no_of_followers >= 1
order by follower
