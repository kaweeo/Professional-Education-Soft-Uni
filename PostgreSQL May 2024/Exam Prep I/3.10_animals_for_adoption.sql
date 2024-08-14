SELECT name AS animal,
       EXTRACT(YEAR FROM birthdate) AS birth_year,
       animal_type
FROM animals a
         JOIN animal_types at on at.id = a.animal_type_id
WHERE at.animal_type <> 'Birds'
  AND a.birthdate > DATE '2022-01-01' - INTERVAL '5 years'
  AND a.owner_id IS NULL
ORDER BY name;