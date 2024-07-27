SELECT c1.id,
       c1.make,
       c1.mileage,
       COUNT(c2.id) AS count_of_courses,
       ROUND(AVG(c2.bill), 2) AS average_bill
FROM cars c1
         LEFT JOIN courses c2 ON c1.id = c2.car_id
GROUP BY 
       c1.id
HAVING 
       COUNT(c2.id) <> 2
ORDER BY 
       count_of_courses DESC, 
       c1.id;
