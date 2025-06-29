# Write your MySQL query statement below
select
id,
case 
when p_id is null then 'Root'
when id not in ( select distinct p_id from tree WHERE p_id IS NOT NULL) then 'Leaf'
else 'Inner'
end as type
from
tree