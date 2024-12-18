CREATE TABLE search_results (
    id SERIAL PRIMARY KEY,
    address_name VARCHAR(50),
    full_name VARCHAR(100),
    level_of_bill VARCHAR(20),
    make VARCHAR(30),
    condition CHAR(1),
    category_name VARCHAR(50)
);

CREATE OR REPLACE PROCEDURE sp_courses_by_address(address_name VARCHAR(100))
AS
$$
BEGIN
    TRUNCATE TABLE search_results;

    INSERT INTO search_results (address_name, full_name, level_of_bill, make, condition, category_name)
    SELECT
        a.name AS address_name,
        c2.full_name AS full_name,
        CASE
            WHEN c1.bill <= 20 THEN 'Low'
            WHEN c1.bill <= 30 THEN 'Medium'
            ELSE 'High'
        END AS level_of_bill,
        c3.make AS car_make,
        c3.condition AS car_condition,
        cat.name AS category_name
    FROM
        addresses a
        JOIN courses c1 ON a.id = c1.from_address_id
        JOIN clients c2 ON c1.client_id = c2.id
        JOIN cars c3 ON c1.car_id = c3.id
        JOIN categories cat ON c3.category_id = cat.id
    WHERE
        a.name = address_name
    ORDER BY
        c3.make,
        c2.full_name;
END;
$$
LANGUAGE plpgsql;