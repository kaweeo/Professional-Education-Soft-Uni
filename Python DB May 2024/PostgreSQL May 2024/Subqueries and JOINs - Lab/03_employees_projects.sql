SELECT
    employee_id,
    concat(first_name, ' ', last_name),
     project_id,
     p.name AS project_name
FROM employees e
    JOIN employees_projects ep USING (employee_id)
    JOIN projects p USING (project_id)
    JOIN departments d USING (department_id)
WHERE p.project_id = 1
;