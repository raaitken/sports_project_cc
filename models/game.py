class Game:
    def __init__(self, player_one, player_two, p1_result, p2_result, date=None, id=None):
        self.player_one = player_one
        self.player_two = player_two
        self.p1_result = p1_result
        self.p2_result = p2_result
        self.date = date
        self.id = id

    def result(self):
        if self.p1_result > self.p2_result:
            self.player_one.win()
            self.player_two.lose()
            return [self.player_one, self.player_two]
        elif self.p1_result < self.p2_result:
            self.player_two.win()
            self.player_one.lose()
            return [self.player_one, self.player_two]
