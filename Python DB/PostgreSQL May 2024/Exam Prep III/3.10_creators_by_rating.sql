SELECT c.last_name,
       CEIL(AVG(bg.rating)) AS average_rating,
       p.name               AS publisher_name
FROM creators c
         JOIN creators_board_games cbg ON c.id = cbg.creator_id
         JOIN board_games bg ON cbg.board_game_id = bg.id
         JOIN publishers p ON bg.publisher_id = p.id
WHERE p.name = 'Stonemaier Games'
GROUP BY c.last_name, p.name
ORDER BY average_rating DESC;