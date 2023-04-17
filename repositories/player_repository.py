from db.run_sql import run_sql
from models.player import Player
from models.game import Game

def save(player):
    sql = "INSERT INTO players (name, points, games_played, wins, losses) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [player.name, player.points, player.games_played, player.wins, player.losses]
    results = run_sql(sql, values)
    id = results[0]['id']
    player.id = id

def select_all():
    players = []
    sql = "SELECT * FROM players"
    results = run_sql(sql)
    for result in results:
        player = Player(result['name'], result['points'], result['games_played'], result['wins'], result['losses'], result['id'])
        players.append(player)
    
    return players

def select(id):
    player = None
    sql = "SELECT * FROM players WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        player = Player(result['name'], result['points'], result['games_played'], result['wins'], result['losses'], result['id'])
    
    return player

def delete_all():
    sql = "DELETE FROM players"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM players WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(player):
    sql = "UPDATE players SET (name, points, games_played, wins, losses) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [player.name, player.points, player.games_played, player.wins, player.losses, player.id]
    run_sql(sql, values)

def select_games_of_player(id):
    games = []
    sql = "SELECT * FROM games WHERE player_one_id = %s OR player_two_id = %s"
    values = [id, id]
    results = run_sql(sql, values)
    for result in results:
        player_one = select(result['player_one_id'])
        player_two = select(result['player_two_id'])
        game = Game(player_one, player_two, result['player_one_result'], result['player_two_result'])
        games.append(game)

    return games

def select_table():
    players = []
    sql = "SELECT * FROM players ORDER BY points DESC, games_played ASC"
    results = run_sql(sql)
    for result in results:
        player = Player(result['name'], result['points'], result['games_played'], result['wins'], result['losses'], result['id'])
        players.append(player)
    
    return players