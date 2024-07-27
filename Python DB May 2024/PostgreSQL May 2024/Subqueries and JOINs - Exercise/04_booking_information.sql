SELECT
    b.booking_id,
    a.name AS apartment_owner,
    a.apartment_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name
FROM apartments AS a
         FULL JOIN bookings b on b.booking_id = a.booking_id
         FULL JOIN customers c on b.customer_id = c.customer_id
ORDER BY booking_id ASC, apartment_owner, customer_name
;