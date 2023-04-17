from db.run_sql import run_sql
from models.game import Game
from models.player import Player
import repositories.player_repository as player_repository

def save(game):
    sql = "INSERT INTO games (player_one_id, player_two_id, player_one_result, player_two_result) VALUES (%s, %s, %s, %s) RETURNING id, date"
    values = [game.player_one.id, game.player_two.id, game.p1_result, game.p2_result]
    results = run_sql(sql, values)
    id = results[0]['id']
    # Not returning date from database
    date = results[0]['date']
    game.id = id
    game.date = date


def select_all():
    games = []
    sql = "SELECT * FROM games"
    results = run_sql(sql)
    for result in results:
        player_one = player_repository.select(result['player_one_id'])
        player_two = player_repository.select(result['player_two_id'])
        game = Game(player_one, player_two, result['player_one_result'], result['player_two_result'], result['date'], result['id'])
        games.append(game)
    return games

def delete_all():
    sql = "DELETE FROM games"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM games WHERE id = %s"
    values = [id]
    run_sql(sql, values)