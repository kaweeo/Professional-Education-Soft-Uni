SELECT first_name || ' ' || last_name AS full_name,
       age,
       hire_date
FROM players
WHERE SUBSTRING(first_name, 1, 1) = 'M'
-- WHERE first_name LIKE 'M%'
ORDER BY age DESC, full_name;
