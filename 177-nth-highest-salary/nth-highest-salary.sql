CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
WITH salary_rank AS (
    SELECT
        salary,
        DENSE_RANK() OVER (ORDER BY salary DESC) AS d_rnk
    FROM Employee
)

SELECT
    MAX(salary) AS SecondHighestSalary
FROM salary_rank
WHERE d_rnk = N
  );
END