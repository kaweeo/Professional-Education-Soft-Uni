INSERT INTO coaches (first_name, last_name, salary, coach_level)
SELECT p.first_name         AS first_name,
       p.last_name          AS last_name,
       p.salary * 2         AS salary,
       length(p.first_name) AS coach_level
FROM players p
WHERE p.hire_date < '2013-12-13 07:18:46'