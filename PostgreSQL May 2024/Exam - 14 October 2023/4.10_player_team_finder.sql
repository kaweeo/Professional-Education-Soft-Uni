CREATE OR REPLACE PROCEDURE sp_players_team_name(
    IN player_name VARCHAR(50),
    OUT team_name VARCHAR(45)
)
AS
$$
BEGIN
    IF (SELECT t.id
        FROM players p
                 LEFT JOIN teams t ON p.team_id = t.id
        WHERE (p.first_name || ' ' || p.last_name) = player_name) IS NULL THEN
        team_name := 'The player currently has no team';
    ELSE
        team_name := (SELECT t.name
                      FROM players p
                               LEFT JOIN teams t ON p.team_id = t.id
                      WHERE (p.first_name || ' ' || p.last_name) = player_name);
    END IF;
END ;
$$
    LANGUAGE plpgsql;

