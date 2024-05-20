SELECT
    b.booking_id,
    b.starts_at:: DATE,
    b.apartment_id,
    concat(c.first_name, ' ', c.last_name) AS customer_name
FROM bookings b
    RIGHT JOIN customers c ON b.customer_id = c.customer_id
ORDER BY customer_name ASC
LIMIT 10;