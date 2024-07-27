CREATE OR REPLACE FUNCTION fn_creator_with_board_games(
    IN first_name_creator VARCHAR(30),
    OUT total_number_creators INT
)
AS
$$
BEGIN
    SELECT COUNT(board_game_id)
    INTO total_number_creators
    FROM creators
             JOIN public.creators_board_games cbg on creators.id = cbg.creator_id
    WHERE creators.first_name = first_name_creator
    GROUP BY creators.first_name;

    IF total_number_creators IS NULL THEN
        total_number_creators := 0;
    END IF;

END;

$$
    LANGUAGE plpgsql;


SELECT fn_creator_with_board_games('Bruno');