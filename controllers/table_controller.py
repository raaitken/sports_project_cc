from flask import Blueprint, Flask, redirect, render_template, request

from models.player import Player
import repositories.player_repository as player_repository

table_blueprint = Blueprint('table', __name__)

# INDEX
@table_blueprint.route('/table')
def table():
    players = player_repository.select_table()
    return render_template('table/index.html', players=players)