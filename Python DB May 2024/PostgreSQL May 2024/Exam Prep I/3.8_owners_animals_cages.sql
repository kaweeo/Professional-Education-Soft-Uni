SELECT
    o.name || ' - ' || a.name AS "owners - animals",
    o.phone_number,
    ac.cage_id
FROM animals a
    JOIN animal_types t on a.animal_type_id = t.id
        JOIN owners o on o.id = a.owner_id
            JOIN animals_cages ac on a.id = ac.animal_id
WHERE animal_type = 'Mammals'
ORDER BY o.name ASC, a.name DESC;