SELECT min(avg_area) AS min_average_area
FROM (SELECT avg(area_in_sq_km) AS avg_area
      FROM countries
      GROUP BY continent_code) subquery;



-- SELECT AVG(area_in_sq_km) AS min_average_area
-- FROM countries c
--          JOIN continents ON c.continent_code = continents.continent_code
-- GROUP BY continent_name
-- ORDER BY min_average_area ASC
-- LIMIT 1;
