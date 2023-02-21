# Write your MySQL query statement below
select w1.id from Weather w1, Weather w2 where
w1.Temperature > w2.Temperature AND DATEDIFF(w1.recordDate , w2.recordDate) = 1


# Definition and Usage
# The DATEDIFF() function returns the number of days between two date values.

# Syntax
# DATEDIFF(date1, date2)