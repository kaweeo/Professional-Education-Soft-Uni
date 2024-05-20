SELECT
    apartment_id,
    booked_for,
    first_name,
    country
FROM bookings b
    JOIN customers c USING (customer_id)
WHERE c.job_type = 'Lead'
;
