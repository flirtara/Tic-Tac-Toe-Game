from unittest import TestCase
# try:
#     from unittest.mock import patch
# except ImportError:
#     from mock import patch

from player import Player

VALID_MOVES = (1, 2, 3, 4, 5, 6, 7, 8, 9)


class PlayerTest(TestCase):

    def test_create_player_is_human(self):
        # Test if it is the human
        player_human = Player(True)
        self.assertEqual(True, player_human.is_human)

        # Test if it is the computer
        player_computer = Player(False)
        self.assertEqual(False, player_computer.is_human)

    def test_create_player_marker(self):
        # Test human marker
        player_human = Player(True)
        self.assertEqual("X", player_human.marker)

        # Test computer marker
        player_computer = Player(False)
        self.assertEqual("O", player_computer.marker)

    def test_computer_get_move(self):
        # Test Computer returns a move.
        player_computer = Player(False)
        move = player_computer.get_move()
        self.assertIn(move.value, VALID_MOVES)

