CREATE TABLE employees (
    id serial PRIMARY KEY,
    first_name VARCHAR(30),
    last_name VARCHAR(50),
    hiring_date DATE DEFAULT '2023-01-01',
    salary NUMERIC(10, 2),
    devices_number INT2
);
