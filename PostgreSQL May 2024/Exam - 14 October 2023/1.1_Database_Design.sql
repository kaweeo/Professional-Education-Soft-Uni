CREATE TABLE IF NOT EXISTS towns
(
    id   SERIAL PRIMARY KEY,
    name VARCHAR(45) NOT NULL
);

CREATE TABLE IF NOT EXISTS stadiums
(
    id       SERIAL PRIMARY KEY,
    name     VARCHAR(45) NOT NULL,
    capacity INT         NOT NULL CHECK ( capacity > 0 ),
    town_id  INT         NOT NULL,
    CONSTRAINT fk_stadiums_towns FOREIGN KEY (town_id)
        REFERENCES towns (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS teams

(
    id          SERIAL PRIMARY KEY,
    name        VARCHAR(45) NOT NULL,
    established DATE        NOT NULL,
    fan_base    INT         NOT NULL DEFAULT 0 CHECK ( fan_base >= 0 ),
    stadium_id  INT         NOT NULL,
    CONSTRAINT fk_teams_stadiums FOREIGN KEY (stadium_id)
        REFERENCES stadiums (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS coaches

(
    id          SERIAL PRIMARY KEY,
    first_name  VARCHAR(10)    NOT NULL,
    last_name   VARCHAR(20)    NOT NULL,
    salary      NUMERIC(10, 2) NOT NULL DEFAULT 0 CHECK ( salary >= 0 ),
    coach_level INT            NOT NULL DEFAULT 0 CHECK ( coach_level >= 0 )
);

CREATE TABLE IF NOT EXISTS skills_data

(
    id        SERIAL PRIMARY KEY,
    dribbling INT DEFAULT 0 CHECK ( dribbling >= 0 ),
    pace      INT DEFAULT 0 CHECK ( pace >= 0 ),
    passing   INT DEFAULT 0 CHECK ( passing >= 0 ),
    shooting  INT DEFAULT 0 CHECK ( shooting >= 0 ),
    speed     INT DEFAULT 0 CHECK ( speed >= 0 ),
    strength  INT DEFAULT 0 CHECK ( strength >= 0 )
);

CREATE TABLE IF NOT EXISTS players

(
    id             SERIAL PRIMARY KEY,
    first_name     VARCHAR(10)    NOT NULL,
    last_name      VARCHAR(20)    NOT NULL,
    age            INT            NOT NULL DEFAULT 0 CHECK ( age >= 0 ),
    position       CHAR(1)     NOT NULL,
    salary         NUMERIC(10, 2) NOT NULL DEFAULT 0 CHECK ( salary >= 0 ),
    hire_date      TIMESTAMP,
    skills_data_id INT            NOT NULL,
    CONSTRAINT fk_players_skills_data FOREIGN KEY (skills_data_id)
        REFERENCES skills_data (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    team_id        INT,
    CONSTRAINT fk_players_teams FOREIGN KEY (team_id)
        REFERENCES teams (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS players_coaches
(
    player_id INT,
    CONSTRAINT fk_players_coaches_players FOREIGN KEY (player_id)
        REFERENCES players (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    coach_id  INT,
    CONSTRAINT fk_players_coaches_coaches FOREIGN KEY (coach_id)
        REFERENCES coaches (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);



