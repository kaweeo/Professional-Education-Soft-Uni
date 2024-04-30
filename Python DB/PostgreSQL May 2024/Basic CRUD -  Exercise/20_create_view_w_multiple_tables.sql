CREATE VIEW view_addresses AS
SELECT
    CONCAT(employees.first_name, ' ', employees.last_name) AS "full_name",
    employees.department_id,
    CONCAT(addresses.number, ' ', addresses.street) AS "address"
FROM employees, addresses
WHERE employees.address_id = addresses.id;