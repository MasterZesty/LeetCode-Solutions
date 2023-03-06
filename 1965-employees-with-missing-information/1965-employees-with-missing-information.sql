# Write your MySQL query statement below
with t as ((select a.employee_id as employee_id,COALESCE(a.name,'NA') as name,COALESCE(b.salary,'NA') as salary from Employees a left join Salaries b on a.employee_id=b.employee_id)
union
(select a.employee_id as employee_id,COALESCE(b.name,'NA') as name,COALESCE(a.salary,'NA') as salary from Salaries a left join Employees b on a.employee_id=b.employee_id))
select employee_id from t where name='NA' or salary='NA' order by employee_id ;
