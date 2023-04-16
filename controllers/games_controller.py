from flask import Blueprint, Flask, redirect, render_template, request

from models.game import Game
import repositories.game_repository as game_repository
import repositories.player_repository as player_repository

games_blueprint = Blueprint('games', __name__)

# INDEX
@games_blueprint.route('/games')
def games():
    games = game_repository.select_all()
    return render_template('games/index.html', games=games)