class Game:
    def __init__(self, player_one, player_two, date, result, id=None):
        self.player_one = player_one
        self.player_two = player_two
        self.date = date
        self.result = result
        self.id = id