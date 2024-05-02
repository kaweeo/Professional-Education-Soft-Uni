SELECT
    first_name,
    last_name,
    extract(YEAR from born) AS born
FROM authors;