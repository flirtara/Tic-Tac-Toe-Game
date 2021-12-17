from unittest import TestCase
from unittest.mock import patch

from player import Player


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

    # def test_get_player_move(self):
    #     # Test human valid move
    #     player_human = Player(True)
    #     human_move = player_human.get_move()
    #     self.assertEqual(4, human_move.value)
    #
    #     # Test computer move
    #     # player_computer = Player(False)
    #     # computer_move = player_computer.get_move()
    #     # self.assertEqual(9, computer_move.value)