CREATE OR REPLACE FUNCTION fn_stadium_team_name(
    stadium_name VARCHAR(30)
)
    RETURNS TABLE
            (
                team_name VARCHAR
            )
AS
$$
BEGIN
    RETURN QUERY (SELECT teams.name
                  FROM teams
                           JOIN public.stadiums s ON teams.stadium_id = s.id
                  WHERE s.name = stadium_name
                  ORDER BY teams.name);
END;
$$
    LANGUAGE plpgsql;


-- SELECT fn_stadium_team_name('BlogXS')