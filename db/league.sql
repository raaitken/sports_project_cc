DROP TABLE games;
DROP TABLE players;

CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    points INT
);

CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    player_one_id INT NOT NULL REFERENCES players(id),
    player_two_id INT NOT NULL REFERENCES players(id)
);