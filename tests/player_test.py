import unittest
from models.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.daigo = Player("Daigo Umehara")
        self.justin = Player("Justin Wong")

    def test_player_has_name(self):
        expected_value = 'Daigo Umehara'
        actual_value = self.daigo.name
        self.assertEqual(expected_value, actual_value)
    
    def test_player_starts_with_zero_points(self):
        expected_value = 0
        actual_value = self.justin.points
        self.assertEqual(expected_value, actual_value)