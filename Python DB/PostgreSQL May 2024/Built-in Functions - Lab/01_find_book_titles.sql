SELECT title
FROM books
WHERE starts_with(title, 'The')
ORDER BY id;

-- SELECT title
-- FROM books
-- WHERE substr(title, 1, 3) = 'The'
-- ORDER BY id;

-- SELECT title
-- FROM books
-- WHERE title LIKE 'The %'
-- ORDER BY id;

-- SELECT title
-- FROM books
-- WHERE LEFT(title, 1, 3) = 'The'
-- ORDER BY id;