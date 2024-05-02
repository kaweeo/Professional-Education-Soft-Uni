SELECT id,
       (height * side) / 2 as area
FROM triangles
ORDER BY id;