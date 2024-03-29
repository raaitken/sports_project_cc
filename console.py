import pdb

from models.player import Player
import repositories.player_repository as player_repository

from models.game import Game
import repositories.game_repository as game_repository

game_repository.delete_all()
player_repository.delete_all()

player_1 = Player("Daigo Umehara")
player_repository.save(player_1)

player_2 = Player("Punk")
player_repository.save(player_2)

player_3 = Player("Tokido")
player_repository.save(player_3)

player_4 = Player("Justin Wong")
player_repository.save(player_4)

game_1 = Game(player_4, player_1, 1, 3)
game_repository.save(game_1)

results = player_repository.select_all()
games = game_repository.select_all()

for result in results:
    print(result.__dict__)

for game in games:
    print(game.__dict__)