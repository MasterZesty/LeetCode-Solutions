# Write your MySQL query statement below
with 
es as (select id,name from employees)
,

eu as (select id,unique_id from employeeuni)


select eu.unique_id,es.name from es left join eu on es.id=eu.id