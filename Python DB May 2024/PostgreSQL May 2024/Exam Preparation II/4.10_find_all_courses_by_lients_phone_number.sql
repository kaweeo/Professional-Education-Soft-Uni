CREATE OR REPLACE FUNCTION fn_courses_by_client(
    IN phone_num VARCHAR(20),
    OUT num_courses INT
)
AS
$$
BEGIN
    SELECT COUNT(c2.id)
    INTO num_courses
    FROM clients c1
             JOIN courses c2 ON c1.id = c2.client_id
    WHERE c1.phone_number = phone_num;
END;
$$
    LANGUAGE plpgsql;