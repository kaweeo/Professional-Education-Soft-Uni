SELECT r.start_point,
       r.end_point,
       r.leader_id,
       concat(c.first_name, ' ', c.last_name) AS leader_name
FROM routes r
         JOIN campers c ON r.leader_id = c.id
;