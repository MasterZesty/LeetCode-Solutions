# Write your MySQL query statement below
select emp_id,event_day as day,SUM(out_time - in_time) as total_time from Employees group by emp_id,event_day;