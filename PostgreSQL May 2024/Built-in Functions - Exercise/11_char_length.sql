SELECT
    CONCAT_WS(' ', mountains.mountain_range, peaks.peak_name)
        AS mountain_information,
    CHAR_LENGTH(CONCAT_WS(' ', mountains.mountain_range, peaks.peak_name))
        AS "Characters Length",
	BIT_LENGTH(CONCAT_WS(' ', mountains.mountain_range, peaks.peak_name))
        AS "Bits of a String"
FROM mountains, peaks
WHERE mountains.id = peaks.mountain_id;