SELECT b.id,
       b.name,
       b.release_year,
       c.name AS category_name
FROM board_games b
         JOIN categories c ON c.id = b.category_id
WHERE c.name = 'Strategy Games'
   OR c.name = 'Wargames'
ORDER BY release_year DESC;
