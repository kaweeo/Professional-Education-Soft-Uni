CREATE TABLE IF NOT EXISTS monasteries
(
    "id"             SERIAL PRIMARY KEY,
    "monastery_name" VARCHAR(255),
    "country_code"   CHAR(2) REFERENCES countries (country_code)
);

INSERT INTO monasteries (monastery_name, country_code)
VALUES ('Rila Monastery "St. Ivan of Rila"', 'BG'),
       ('Bachkovo Monastery "Virgin Mary"', 'BG'),
       ('Troyan Monastery "Holy Mother''s Assumption"', 'BG'),
       ('Kopan Monastery', 'NP'),
       ('Thrangu Tashi Yangtse Monastery', 'NP'),
       ('Shechen Tennyi Dargyeling Monastery', 'NP'),
       ('Benchen Monastery', 'NP'),
       ('Southern Shaolin Monastery', 'CN'),
       ('Dabei Monastery', 'CN'),
       ('Wa Sau Toi', 'CN'),
       ('Lhunshigyia Monastery', 'CN'),
       ('Rakya Monastery', 'CN'),
       ('Monasteries of Meteora', 'GR'),
       ('The Holy Monastery of Stavronikita', 'GR'),
       ('Taung Kalat Monastery', 'MM'),
       ('Pa-Auk Forest Monastery', 'MM'),
       ('Taktsang Palphug Monastery', 'BT'),
       ('Sümela Monastery', 'TR');

ALTER TABLE countries
    ADD COLUMN three_rivers BOOLEAN DEFAULT false;

UPDATE countries
SET three_rivers = TRUE
WHERE country_code IN (SELECT cr.country_code
                       FROM countries_rivers cr
                                JOIN rivers r ON cr.river_id = r.id
                       GROUP BY cr.country_code
                       HAVING count(r.id) > 3);

SELECT monastery_name AS monastery,
       country_name   AS country
FROM monasteries
         JOIN countries USING (country_code)
WHERE NOT countries.three_rivers
ORDER BY monastery_name;
