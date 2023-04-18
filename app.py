from flask import Flask, render_template
from controllers.players_controller import players_blueprint
from controllers.games_controller import games_blueprint
from controllers.table_controller import table_blueprint
from controllers.h2h_controller import headtohead_blueprint
import repositories.player_repository as player_repository
import repositories.game_repository as game_repository

app = Flask(__name__)

app.register_blueprint(players_blueprint)
app.register_blueprint(games_blueprint)
app.register_blueprint(table_blueprint)
app.register_blueprint(headtohead_blueprint)

@app.route('/')
def home():
    players = player_repository.select_table()
    games = game_repository.select_all()
    last_five_games = games[-5:]
    return render_template('index.html', players=players, games=games, recent_games=last_five_games)

if __name__ == '__main__':
    app.run(debug=True)