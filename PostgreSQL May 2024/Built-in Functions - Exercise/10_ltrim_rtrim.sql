SELECT
    LTRIM(peak_name, 'M') as "left_trim",
    RTRIM(peak_name, 'm') as "right_trim"
FROM peaks;

