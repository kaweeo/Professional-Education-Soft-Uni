CREATE OR REPLACE FUNCTION fn_full_name(first_name VARCHAR(50), last_name VARCHAR(50))
RETURNS VARCHAR(100) AS
    $$
        BEGIN
            IF first_name IS NULL AND last_name IS NULL THEN
                RETURN NULL;
            ELSEIF first_name IS NULL THEN
                RETURN INITCAP(last_name);
            ELSEIF last_name IS NULL THEN
                RETURN INITCAP(first_name);
            ELSE
                RETURN INITCAP(first_name) || ' ' || INITCAP(last_name);
            END IF;
        END
    $$ LANGUAGE plpgsql;

SELECT fn_full_name('Kalin', NULL);

-- SOLUTION #2
--
-- CREATE OR REPLACE FUNCTION fn_full_name(
--     IN first_name VARCHAR,
--     IN last_name VARCHAR,
--     OUT full_name VARCHAR
-- ) AS
-- $$
-- BEGIN
--     full_name := initcap(first_name) || ' ' || initcap(last_name);
-- END
-- $$
--     LANGUAGE plpgsql;
--
-- SELECT fn_full_name('Kalin', NULL);
