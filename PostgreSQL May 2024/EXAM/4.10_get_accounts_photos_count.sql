CREATE OR REPLACE FUNCTION udf_accounts_photos_count(
    IN account_username VARCHAR(30),
    OUT num_photos INT
)
AS
$$
BEGIN
    SELECT COUNT(p.id)
    INTO num_photos
    FROM accounts a
             JOIN accounts_photos ap ON a.id = ap.account_id
             JOIN photos p ON ap.photo_id = p.id
    WHERE a.username = account_username;
END;
$$
    LANGUAGE plpgsql;