SELECT d.first_name,
       d.last_name,
       c.make,
       c.model,
       c.mileage
FROM cars c
         JOIN
     cars_drivers cd ON c.id = cd.car_id
         JOIN
     drivers d ON d.id = cd.driver_id
WHERE c.mileage IS NOT NULL
ORDER BY c.mileage DESC, d.first_name;
