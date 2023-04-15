import pdb

from models.player import Player
import repositories.player_repository as player_repository

player_repository.delete_all()

player_1 = Player("Daigo Umehara")
player_repository.save(player_1)

player_2 = Player("Punk")
player_repository.save(player_2)

player_3 = Player("Tokido")
player_repository.save(player_3)

player_4 = Player("Justin Wong")
player_repository.save(player_4)

results = player_repository.select_all()

for result in results:
    print(result.__dict__)