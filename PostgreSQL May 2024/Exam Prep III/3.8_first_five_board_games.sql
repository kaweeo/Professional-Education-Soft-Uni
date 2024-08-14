SELECT bg.name,
       bg.rating,
       c.name AS category_name
FROM board_games bg
         JOIN players_ranges pr on pr.id = bg.players_range_id
         JOIN categories c on c.id = bg.category_id
WHERE rating > 7.00
  AND (bg.name ILIKE '%a%' OR (bg.rating > 7.50 AND min_players <= 5 AND max_players >= 2))
ORDER BY bg.name, bg.rating DESC
LIMIT 5;