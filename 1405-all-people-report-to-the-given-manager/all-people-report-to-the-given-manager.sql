# Write your MySQL query statement below
select
a.employee_id
-- ,
-- a.manager_id as N,
-- b.manager_id as N_2,
-- c.manager_id as N_3
from
employees a -- first manager
left join employees b -- second manager
on a.manager_id = b.employee_id
left join employees c -- third manager
on b.manager_id = c.employee_id
where
c.manager_id = 1
and a.employee_id <> c.manager_id
