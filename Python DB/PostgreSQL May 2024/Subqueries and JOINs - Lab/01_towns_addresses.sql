SELECT a.town_id,
       t.name as town_name,
       address_text
FROM addresses a
         JOIN towns t ON a.town_id = t.town_id
WHERE t.name = 'San Francisco'
   OR t.name = 'Sofia'
   OR t.name = 'Carnation'
ORDER BY town_id, address_id
;