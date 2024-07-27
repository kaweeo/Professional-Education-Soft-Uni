SELECT full_name,
       COUNT(car_id) AS count_of_cars,
       SUM(bill)     AS total_sum
FROM clients
         JOIN courses ON clients.id = courses.client_id
-- WHERE full_name LIKE '_a%'
WHERE substring(clients.full_name FROM 2 FOR 1) = 'a'
GROUP BY full_name
HAVING count(clients.id) > 1;