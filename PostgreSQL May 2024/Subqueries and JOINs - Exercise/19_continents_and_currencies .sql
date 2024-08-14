CREATE VIEW continent_currency_usage AS
SELECT
    continent_code,
    currency_code,
    COUNT(*) AS currency_usage
FROM (
    SELECT
        continent_code,
        currency_code,
        DENSE_RANK() OVER (PARTITION BY continent_code ORDER BY currency_code) AS rank
    FROM countries
) subquery
GROUP BY
    continent_code,
    currency_code
HAVING
    COUNT(*) > 1
ORDER BY
    currency_usage DESC;
