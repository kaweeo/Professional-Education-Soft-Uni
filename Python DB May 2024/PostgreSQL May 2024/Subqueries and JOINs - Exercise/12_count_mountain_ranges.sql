SELECT
    country_code,
    count(mountain_range) AS mountain_range_count
FROM mountains m
         JOIN public.mountains_countries mc ON m.id = mc.mountain_id
WHERE country_code = 'US' OR country_code = 'RU' OR country_code = 'BG'
GROUP BY country_code
ORDER BY mountain_range_count DESC;