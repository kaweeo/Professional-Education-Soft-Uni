SELECT
    c.id,
    c.first_name || ' ' || c.last_name AS creator_name,
    c.email
FROM
    creators c
LEFT JOIN public.creators_board_games cbg on c.id = cbg.creator_id
WHERE creator_id IS NULL
ORDER BY creator_name;