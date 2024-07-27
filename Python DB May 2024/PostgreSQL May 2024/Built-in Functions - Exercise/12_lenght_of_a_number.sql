SELECT
    population,
    LENGTH(CAST(population AS varchar)) AS "length"
FROM countries;