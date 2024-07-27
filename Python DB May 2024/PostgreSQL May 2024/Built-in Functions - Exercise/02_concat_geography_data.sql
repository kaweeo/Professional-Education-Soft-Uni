CREATE OR REPLACE view view_continents_countries_currencies_details AS

SELECT
    CONCAT(continents.continent_name, ': ', continents.continent_code) AS continent_details,
    CONCAT_WS(' - ', countries.country_name, countries.capital, countries.area_in_sq_km, 'km2') AS country_information,
    CONCAT(currencies.description, ' (', currencies.currency_code, ')') AS currencies
FROM continents, countries, currencies
WHERE
    continents.continent_code = countries.continent_code
    AND
    currencies.currency_code = countries.currency_code
ORDER BY country_information, currencies;


-- CREATE OR REPLACE VIEW
-- 	view_continents_countries_currencies_details
-- AS SELECT
-- 	CONCAT(con.continent_name, ': ', con.continent_code) AS "Continent Details",
-- 	CONCAT_WS(' - ', cou.country_name, cou.capital, cou.area_in_sq_km, 'km2') AS "Country Information",
-- 	CONCAT(cur.description, ' (', cur.currency_code, ')') AS "Currencies"
-- FROM
-- 	continents AS con,
-- 	countries AS cou,
-- 	currencies AS cur
-- WHERE
-- 	con.continent_code = cou.continent_code
-- 		AND
-- 	cou.currency_code = cur.currency_code
-- ORDER BY
-- 	"Country Information" ASC,
-- 	"Currencies" ASC;