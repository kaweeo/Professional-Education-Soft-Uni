CREATE OR REPLACE FUNCTION fn_difficulty_level(
    IN level INT,
    OUT difficulty_level VARCHAR
) AS
$$
BEGIN
    IF level <= 40 THEN
        difficulty_level := 'Normal Difficulty';
    ELSEIF level between 41 AND 60 THEN
        difficulty_level := 'Nightmare Difficulty';
    ELSE
        difficulty_level := 'Hell Difficulty';
    END IF;
END;
$$
    LANGUAGE plpgsql;

SELECT
    user_id,
    level,
    cash,
    fn_difficulty_level(level)
FROM
    users_games
ORDER BY user_id ASC;