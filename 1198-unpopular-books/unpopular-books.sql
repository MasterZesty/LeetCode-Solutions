# Write your MySQL query statement below
with ds_books as (
select
a.order_id,
b.book_id,
coalesce(a.quantity, 0) as quantity,
a.dispatch_date,
b.name,
b.available_from
from books b
left join orders a
on a.book_id = b.book_id
where
b.available_from < DATE_SUB('2019-06-23', INTERVAL 1 MONTH)
-- AND ( 
--     (dispatch_date >= DATE_SUB('2019-06-23', INTERVAL 1 YEAR)
--     AND dispatch_date < '2019-06-23')
--  or dispatch_date is null
--  )
),

unpop_books as (
select
book_id,
name,
SUM(
CASE
    WHEN dispatch_date >= DATE_SUB('2019-06-23', INTERVAL 1 YEAR) THEN quantity
    WHEN dispatch_date is null then 0
    WHEN dispatch_date < DATE_SUB('2019-06-23', INTERVAL 1 YEAR) OR dispatch_date > '2019-06-23' then 0
END
) AS copies_sold
from
ds_books
group by
book_id,
name
having
copies_sold < 10
)

select
book_id,
name
from
unpop_books