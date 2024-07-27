SELECT name,
       phone_number,
       REPLACE(TRIM(LEADING 'Sofia, ' FROM address), 'Sofia, ', '') AS address
FROM volunteers v
         JOIN volunteers_departments vd on vd.id = v.department_id
    AND vd.department_name = 'Education program assistant'
WHERE address LIKE '%Sofia%'
ORDER BY name;