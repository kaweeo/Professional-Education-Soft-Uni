SELECT
    a.name AS name,
    a.country AS country,
    b.booked_at:: DATE AS booking

FROM apartments a
    LEFT JOIN bookings b on b.booking_id = a.booking_id
LIMIT 10;