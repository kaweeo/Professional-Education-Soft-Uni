CREATE OR REPLACE FUNCTION fn_count_employees_by_town(town_name VARCHAR(20))
    RETURNS INT AS
$$
DECLARE
    employee_count INTEGER;
BEGIN
    SELECT count(*)
    INTO employee_count
    FROM employees
             JOIN public.addresses a ON employees.address_id = a.address_id
             JOIN towns t USING (town_id)
    WHERE t.name = town_name;
    RETURN employee_count;
END;

$$ LANGUAGE plpgsql;


SELECT *
FROM fn_count_employees_by_town('Sofia') AS count;


