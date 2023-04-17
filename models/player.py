class Player:
    def __init__(self, name, points=0, games_played=0, wins=0, losses=0, id=None):
        self.name = name
        self.id = id
        self.points = points
        self.games_played = games_played
        self.wins = wins
        self.losses = losses

    def win(self):
        self.points += 3
        self.games_played += 1
        self.wins += 1

    def lose(self):
        self.games_played += 1
        self.losses += 1