# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below
​
-- You have to deleted duplicates emails, by keeping unique emails with smallest id .
-- 1)  So , it is clear that we have to use ' DELETE ' command
-- Syntax for delete command is
-- " delete from tablename where condition"
-- and condition for deletion is duplicate emails and greater id
​
​
-- 2) We have to one email to other emails of the same table
-- from here we are able to figure out that we have to use join concept
​
# Note:
# A DELETE statement can include JOIN operations.
# It can contain zero, one, or multiple JOIN operations.
# The DELETE removes records that satisfy the JOIN conditions.
​
#-------------------------------------------------------------------------------
# DELETE tablename1
#   FROM tablename1
#   JOIN tablename2 ON columnName3 = columnName4
#  WHERE condition
​
# --------------------------------------------------------------------------------
​
​
delete p1 from Person p1
join Person p2
where p1.email = p2.email and p1.id > p2.id;