CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
    SELECT distinct salary FROM (
        SELECT salary, DENSE_RANK() OVER( ORDER BY salary DESC) AS row_num FROM Employee
    ) as ranked_salary
    WHERE row_num = N
  );
END