CREATE OR REPLACE FUNCTION fn_cash_in_users_games(
    game_name VARCHAR(50)
)
    RETURNS TABLE
            (
                total_cash NUMERIC
            )
AS
$$
BEGIN
    RETURN QUERY
        SELECT ROUND(SUM(cash):: numeric, 2) AS total_cash
        FROM (SELECT cash,
                     ROW_NUMBER() OVER (ORDER BY users_games.cash DESC) AS row_num
              FROM users_games
                JOIN games ON users_games.game_id = games.id
              WHERE games.name = game_name) AS subquery
        WHERE row_num % 2 = 1;
end;
$$ LANGUAGE plpgsql;

SELECT fn_cash_in_users_games('Love in a mist');
SELECT fn_cash_in_users_games('Delphinium Pacific Giant');


-- Soltuins #2 

CREATE OR REPLACE FUNCTION fn_cash_in_users_games(
	game_name VARCHAR(50)
) RETURNS TABLE (
	total_cash NUMERIC
)
AS 
$$
BEGIN
	RETURN QUERY
	WITH ranked_games AS (
		SELECT
			cash,
			ROW_NUMBER() OVER (ORDER BY cash DESC) AS row_num
		FROM
			users_games AS ug
		JOIN
			games AS g
		ON 
			ug.game_id = g.id
		WHERE
			g.name = game_name
	)
	
	SELECT
		ROUND(SUM(cash), 2) AS total_cash
	FROM
		ranked_games AS rg
	WHERE
		rg.row_num % 2 <> 0;
END;
$$
LANGUAGE plpgsql;
