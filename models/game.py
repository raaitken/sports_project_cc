class Game:
    def __init__(self, player_one, player_two, p1_result, p2_result, date=None, id=None):
        self.player_one = player_one
        self.player_two = player_two
        self.p1_result = p1_result
        self.p2_result = p2_result
        self.date = date
        self.id = id