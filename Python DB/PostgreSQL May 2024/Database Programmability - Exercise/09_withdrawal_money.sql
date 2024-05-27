CREATE OR REPLACE PROCEDURE sp_withdraw_money(
    account_id INT,
    money_amount NUMERIC
)
AS
$$
DECLARE
    current_balance NUMERIC;
BEGIN
    IF (SELECT balance < money_amount accounts FROM accounts WHERE id = account_id) IS NULL THEN
        RETURN;
    ELSE
        current_balance := (SELECT balance FROM accounts WHERE id = account_id);
        IF current_balance < money_amount THEN
            RAISE NOTICE 'Insufficient balance to withdraw %', money_amount;
            RETURN;
        ELSE
            UPDATE accounts SET balance = balance - money_amount WHERE id = account_id;
        END IF;
    END IF;
    COMMIT;
END;
$$
    LANGUAGE plpgsql;