SELECT concat(address, ' ', address_2) AS apartment_address,
       booked_for                      AS nights
FROM apartments a
         JOIN public.bookings b on b.booking_id = a.booking_id
ORDER BY a.apartment_id ASC;