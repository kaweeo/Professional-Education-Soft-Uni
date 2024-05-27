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
