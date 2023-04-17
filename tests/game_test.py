import unittest
from models.game import Game
from models.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.tokido = Player("Tokido")
        self.punk = Player("Punk")
        self.game1 = Game(self.tokido, self.punk)

    def test_game_win_gives_three_points(self):
        expected_value = 3
        actual_value = self.tokido.points
        self.game1.result(self.tokido)
        self.assertEqual(expected_value, actual_value)

    def test_game_loss_gives_zero_points(self):
        expected_value = 0
        actual_value = self.punk.points
        self.game1.result()
        self.assertEqual(expected_value, actual_value)