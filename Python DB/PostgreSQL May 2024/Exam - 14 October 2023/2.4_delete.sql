-- Delete related records from players_coaches table
DELETE
FROM public.players_coaches
    USING public.players
WHERE players.id = players_coaches.player_id
  AND players.hire_date < '2013-12-13 07:18:46';

-- Delete records from players table
DELETE
FROM public.players
WHERE hire_date < '2013-12-13 07:18:46';



-- DELETE
-- FROM coaches
-- WHERE id IN (SELECT coach_id
--              FROM players_coaches
--              WHERE player_id IN (SELECT id
--                                  FROM players
--                                  WHERE hire_date < '2013-12-13 07:18:46'));
--
-- DELETE
-- FROM players_coaches
-- WHERE player_id IN (SELECT id
--                     FROM players
--                     WHERE hire_date < '2013-12-13 07:18:46');
--
--
--
-- DELETE
-- FROM players
-- WHERE hire_date < '2013-12-13 07:18:46';