CREATE OR REPLACE PROCEDURE sp_retrieving_holders_with_balance_higher_than(
    searched_balance NUMERIC
)
AS
$$
DECLARE
    holder RECORD;   -- type RECORD (think of it like a row, запис*)
BEGIN
    FOR holder IN
        SELECT concat_ws(' ', ah.first_name, ah.last_name) AS full_name,
               sum(balance)                                AS total_balance
        FROM account_holders ah
                 JOIN accounts a ON ah.id = a.account_holder_id
        GROUP BY full_name
        HAVING sum(balance) > searched_balance
        ORDER BY full_name
        LOOP
            RAISE NOTICE '% - %', holder.full_name, holder.total_balance;
        END LOOP;
END;
$$
    LANGUAGE plpgsql;

--
CALL sp_retrieving_holders_with_balance_higher_than(200000);
