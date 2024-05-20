SELECT
    country_code,
    mountain_range,
    peak_name,
    elevation
FROM
    mountains_countries mc
    JOIN mountains m ON mc.mountain_id = m.id
    JOIN peaks p ON p.mountain_id = m.id
WHERE country_code = 'BG' AND elevation > 2835
ORDER BY elevation DESC
;
