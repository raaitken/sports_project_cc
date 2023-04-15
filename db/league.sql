DROP TABLE IF EXISTS games;
DROP TABLE IF EXISTS players;

CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    points INT
);

CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    player_one_id INT NOT NULL REFERENCES players(id),
    player_two_id INT NOT NULL REFERENCES players(id),
    date TIMESTAMP NOT NULL,
    result INT NOT NULL REFERENCES players(id)
);