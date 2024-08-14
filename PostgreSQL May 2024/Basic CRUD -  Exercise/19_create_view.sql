CREATE VIEW view_company_chart AS
SELECT full_name AS "Full Name", job_title AS "Job Title"
FROM company_chart
WHERE manager_id = 184;

-- CREATE VIEW
-- 	view_company_chart
-- AS
-- SELECT
-- 	"Full Name",
-- 	"Job Title"
-- FROM
-- 	company_chart
-- WHERE
-- 	"Manager ID" = 184;
