class Player:
    def __init__(self, name, points=0, games_played = 0, id=None):
        self.name = name
        self.id = id
        self.points = points
        self.games_played = games_played

    def win(self):
        self.points += 3
        self.games_played += 1

    def lose(self):
        self.games_played += 1