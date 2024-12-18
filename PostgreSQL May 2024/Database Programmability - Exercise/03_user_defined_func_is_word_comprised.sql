CREATE OR REPLACE FUNCTION fn_is_word_comprised(
    set_of_letters VARCHAR(50),
    word VARCHAR(50)
)
    RETURNS BOOLEAN
AS
$$
BEGIN
    RETURN trim(lower(word), lower(set_of_letters)) = '';
END
$$
    LANGUAGE plpgsql;


-- Solution using WHILE LOOP
--
CREATE OR REPLACE FUNCTION fn_is_word_comprised(
    IN set_of_letters VARCHAR(50),
    IN word VARCHAR(50),
    OUT result BOOLEAN
) AS
$$
DECLARE
    len_of_word INT;
    idx         INT := 1;
    letter      CHAR(1);
    counter     INT := 0;
BEGIN
    -- Check length of the word
    len_of_word := (SELECT length(word));

    -- Loop though all letters using variable idx
    WHILE idx <= len_of_word
        LOOP
            letter := (SELECT substring(word FROM idx FOR 1));
            IF (SELECT POSITION(lower(letter) IN lower(set_of_letters)) > 0) THEN
                counter := counter + 1;
            END IF;
            idx = idx + 1;
        END LOOP;

    -- Check if counter of founded letters is equal to length of word
    IF counter = len_of_word THEN
        result := TRUE;
    ELSE
        result := FALSE;
    END IF;
END
$$
    LANGUAGE plpgsql;

--
-- Solution using FOR LOOP
--
CREATE OR REPLACE FUNCTION fn_is_word_comprised(
    set_of_letters VARCHAR(50),
    word VARCHAR(50)
)
    RETURNS BOOLEAN AS
$$
DECLARE
    idx    INT;
    letter VARCHAR;
BEGIN
    FOR idx IN 1..length(word)
        LOOP
            letter := substring(lower(word), idx, 1);
            IF position(letter IN lower(set_of_letters)) = 0 THEN
                RETURN FALSE;
            END IF;
        END LOOP;

    RETURN TRUE;
END;
$$
    LANGUAGE plpgsql;

SELECT fn_is_word_comprised('bobr', 'Rob')


