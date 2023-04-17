DROP TABLE IF EXISTS games;
DROP TABLE IF EXISTS players;

CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    points INT
);

CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    player_one_id INT NOT NULL,
    player_two_id INT NOT NULL,
    player_one_result INT NOT NULL,
    player_two_result INT NOT NULL,
    date TIMESTAMP
);