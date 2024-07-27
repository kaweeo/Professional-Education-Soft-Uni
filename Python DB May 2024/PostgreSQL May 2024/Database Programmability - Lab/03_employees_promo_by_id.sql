CREATE OR REPLACE procedure sp_increase_salary_by_id(id INT)
AS

$$
BEGIN
    UPDATE employees
    SET salary = salary * 1.05
    WHERE employee_id = id;
END;
$$
    LANGUAGE plpgsql;

CALL sp_increase_salary_by_id(17);