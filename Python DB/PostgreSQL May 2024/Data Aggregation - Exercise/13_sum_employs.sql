SELECT count(CASE WHEN department_id = 1 THEN 1 END) AS "Engineering",
       count(CASE WHEN department_id = 2 THEN 1 END) AS "Tool Design",
       count(CASE WHEN department_id = 3 THEN 1 END) AS "Sales",
       count(CASE WHEN department_id = 4 THEN 1 END) AS "Marketing",
       count(CASE WHEN department_id = 5 THEN 1 END) AS "Purchasing",
       count(CASE WHEN department_id = 6 THEN 1 END) AS "Research and Development",
       count(CASE WHEN department_id = 7 THEN 1 END) AS "Production"
FROM employees;


--
-- SELECT CASE
--     WHEN department_id = 1 THEN 'Engineering'
--     WHEN department_id = 2 THEN 'Tool Design'
--     WHEN department_id = 3 THEN 'Sales'
--     WHEN department_id = 4 THEN 'Marketing'
--     WHEN department_id = 5 THEN 'Purchasing'
--     WHEN department_id = 6 THEN 'Research and Development'
--     WHEN department_id = 7 THEN 'Production'
--     END AS department_name,
--     COUNT(*)
-- FROM employees
-- GROUP BY department_id
-- ;