DROP TABLE IF EXISTS games;
DROP TABLE IF EXISTS players;

CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    points INT,
    games_played INT,
    wins INT,
    losses INT
);

CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    player_one_id INT REFERENCES players(id) ON DELETE CASCADE,
    player_two_id INT REFERENCES players(id) ON DELETE CASCADE,
    player_one_result INT NOT NULL,
    player_two_result INT NOT NULL
);