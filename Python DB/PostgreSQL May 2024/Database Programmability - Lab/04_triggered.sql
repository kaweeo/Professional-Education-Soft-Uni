CREATE TABLE deleted_employees
(
    employee_id   SERIAL PRIMARY KEY,
    first_name    VARCHAR(20),
    last_name     VARCHAR(20),
    middle_name   VARCHAR(20),
    job_title     VARCHAR(50),
    department_id INT,
    salary        NUMERIC(19, 4)
);

CREATE OR REPLACE FUNCTION log_deleted_employee()
    RETURNS TRIGGER AS
$$
BEGIN
    INSERT INTO deleted_employees (employee_id, first_name, last_name, middle_name, job_title, department_id,
                                   salary)
    VALUES (OLD.employee_id, OLD.first_name, OLD.last_name, OLD.middle_name, OLD.job_title, OLD.department_id,
            OLD.salary);
    RETURN OLD;
END
$$
    LANGUAGE plpgsql;

CREATE TRIGGER after_employee_delete
    AFTER DELETE
    ON employees
    FOR EACH ROW
EXECUTE FUNCTION log_deleted_employee();
