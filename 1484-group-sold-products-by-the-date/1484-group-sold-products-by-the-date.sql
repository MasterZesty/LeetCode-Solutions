# Write your MySQL query statement below
select sell_date, count(distinct product) as num_sold, GROUP_CONCAT(distinct product) as 'products' from Activities group by sell_date;

#  learned how GROUP_CONCAT works and use case