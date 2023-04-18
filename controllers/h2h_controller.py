from flask import Blueprint, Flask, redirect, render_template, request

import repositories.player_repository as player_repository
import repositories.game_repository as game_repository

headtohead_blueprint = Blueprint('h2h', __name__)

# INDEX
@headtohead_blueprint.route('/h2h')
def head_to_head():
    players = player_repository.select_all()
    return render_template('h2h/index.html', players=players)

# SHOW
@headtohead_blueprint.route('/h2h/<p1_id>/<p2_id>')
def show_head_to_head(p1_id, p2_id):
    games = game_repository.select_head_to_head(p1_id, p2_id)
    return render_template('h2h/show.html', games=games)

@headtohead_blueprint.route('/h2h', methods=['POST'])
def post_h2h():
    player_one_id = request.form['player_one_id']
    player_two_id = request.form['player_two_id']
    return redirect('/h2h/' + player_one_id + '/' + player_two_id)