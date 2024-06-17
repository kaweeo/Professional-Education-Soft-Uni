SELECT co.first_name || ' ' || co.last_name AS coach_full_name,
       p.first_name || ' ' || p.last_name   AS player_full_name,
       teams.name                           AS team_name,
       sd.passing,
       sd.shooting,
       sd.speed
FROM coaches co
         JOIN public.players_coaches pc ON co.id = pc.coach_id
         JOIN players p ON pc.player_id = p.id
         JOIN skills_data sd on p.skills_data_id = sd.id
         JOIN teams ON p.team_id = teams.id
ORDER BY coach_full_name, player_full_name DESC;
