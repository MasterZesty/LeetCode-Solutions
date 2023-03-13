# Write your MySQL query statement below
with temp as (select account,SUM(amount) as balance from Transactions  group by account)
select a.name as name ,b.balance as balance from Users a left join temp b on a.account=b.account where b.balance>10000;