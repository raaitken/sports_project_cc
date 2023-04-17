from flask import Blueprint, Flask, redirect, render_template, request
import pdb

from models.game import Game
import repositories.game_repository as game_repository
import repositories.player_repository as player_repository

games_blueprint = Blueprint('games', __name__)

# INDEX
@games_blueprint.route('/games')
def games():
    games = game_repository.select_all()
    return render_template('games/index.html', games=games)

# NEW
@games_blueprint.route('/games/new')
def new_game():
    players = player_repository.select_all()
    return render_template('games/new.html', players=players)

# CREATE
@games_blueprint.route('/games', methods=['POST'])
def create_game():
    player_one_id = request.form['player_one_id']
    player_two_id = request.form['player_two_id']
    p1_result = request.form['p1_result']
    p2_result = request.form['p2_result']
    player_one = player_repository.select(player_one_id)
    player_two = player_repository.select(player_two_id)
    new_game = Game(player_one, player_two, p1_result, p2_result)
    player = new_game.result()
    player_repository.update(player[0])
    player_repository.update(player[1])
    game_repository.save(new_game)
    return redirect('/games')

# DELETE
@games_blueprint.route('/games/<id>/delete', methods=['POST'])
def delete_game(id):
    game_repository.delete(id)
    return redirect('/games')