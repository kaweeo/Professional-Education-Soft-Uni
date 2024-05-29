SELECT o.name      AS owner,
       COUNT(a.id) AS count_of_animals
FROM animals a
         JOIN owners o ON o.id = a.owner_id
GROUP BY o.id, o.name
ORDER BY count_of_animals DESC,
         owner ASC
LIMIT 5;