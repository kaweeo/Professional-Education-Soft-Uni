CREATE VIEW "view_initials" AS
SELECT LEFT(employees.first_name, 2) AS "initial",
       employees.last_name
FROM employees
ORDER BY last_name;