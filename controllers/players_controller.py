from flask import Blueprint, Flask, redirect, render_template, request

from models.player import Player
import repositories.player_repository as player_repository
import repositories.game_repository as game_repository

players_blueprint = Blueprint('players', __name__)

# INDEX
@players_blueprint.route('/players')
def players():
    players = player_repository.select_all()
    return render_template('players/index.html', players=players)

# SHOW
@players_blueprint.route('/players/<id>')
def show_player(id):
    games = game_repository.select_games_of_player(id)
    player = player_repository.select(id)
    return render_template('players/show.html', games=games, player=player)

# NEW
@players_blueprint.route('/players/new')
def new_player():
    return render_template('/players/new.html')

# CREATE
@players_blueprint.route('/players', methods=['POST'])
def create_player():
    name = request.form['name']
    new_player = Player(name)
    player_repository.save(new_player)
    return redirect('/players')                           

# EDIT
@players_blueprint.route('/players/<id>/edit')
def edit_player(id):
    player = player_repository.select(id)
    return render_template('players/edit.html', player=player)

# UPDATE
@players_blueprint.route('/players/<id>', methods=['POST'])
def update_player(id):
    name = request.form['name']
    player = Player(name, id)
    player_repository.update(player)
    return redirect('/players')

# DELETE
@players_blueprint.route('/players/<id>/delete', methods=['POST'])
def delete_player(id):
    player_repository.delete(id)
    return redirect('/players')