SELECT v.driver_id,
       v.vehicle_type,
       concat(first_name, ' ', last_name) AS driver_name
FROM campers c
         JOIN vehicles v ON v.driver_id = c.id
;