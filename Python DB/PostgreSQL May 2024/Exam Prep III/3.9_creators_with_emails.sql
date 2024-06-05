SELECT c.first_name || ' ' || c.last_name AS full_name,
       c.email,
       MAX(bg.rating)
FROM creators c
         JOIN public.creators_board_games cbg on c.id = cbg.creator_id
         JOIN board_games bg on cbg.board_game_id = bg.id
GROUP BY full_name, c.email
HAVING c.email LIKE ('%.com')
ORDER BY full_name;