class Player:
    def __init__(self, name, points=0, id=None):
        self.name = name
        self.id = id
        self.points = points

    def win(self):
        self.points += 3