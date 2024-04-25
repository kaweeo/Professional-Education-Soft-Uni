-- ALTER TABLE minions_info
--
-- ADD COLUMN email VARCHAR(20),
-- ADD COLUMN equipped BOOLEAN DEFAULT False;


ALTER TABLE minions_info

    ADD COLUMN email VARCHAR(20),
    ADD COLUMN equipped BOOLEAN NOT NULL;
