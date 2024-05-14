CREATE TABLE Mountains (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE Peaks (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    mountain_id INT,
    CONSTRAINT fk_mountains_peaks
                   FOREIGN KEY (mountain_id)
                   REFERENCES Mountains(id)
);
