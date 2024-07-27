DELETE
FROM board_games
WHERE publisher_id IN (SELECT id
                       FROM publishers
                       WHERE address_id IN (SELECT id
                                            FROM addresses
                                            WHERE town LIKE 'L%'));

DELETE
FROM publishers
WHERE address_id IN (SELECT id
                     FROM addresses
                     WHERE town LIKE 'L%');

DELETE
FROM addresses
WHERE town LIKE 'L%';


--
-- ALTER TABLE board_games
--     DROP constraint "fk_board_games_publishers";
--
-- DELETE
-- FROM addresses
-- WHERE town LIKE 'L%';