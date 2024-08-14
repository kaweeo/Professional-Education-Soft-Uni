UPDATE cars
SET condition = 'C'
WHERE year <= 2010
  AND (mileage >= 800000 OR mileage IS NULL)
  AND make <> 'Mercedes-Benz';