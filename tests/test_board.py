from unittest import TestCase
from board import Board
from player import Player
from move import Move


EMPTY_GAME_BOARD = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]

POSITIONS_GAME_BOARD = ["| 1 | 2 | 3 |",
                        "| 4 | 5 | 6 |",
                        "| 7 | 8 | 9 |"]


class BoardTest(TestCase):

    def test_create_board(self):
        # Test creation of initial empty board.
        my_board = Board()
        self.assertEqual(my_board.game_board, EMPTY_GAME_BOARD)

    def test_print_board_with_positions(self):
        pass

    def test_print_board(self):
        pass

    def test_submit_move_as_player(self):
        # Test Human Submit Move
        my_board = Board()
        player = Player()
        move = Move(6)
        my_board.submit_move(player, move)
        self.assertEqual(my_board.game_board[1][2], player.marker)

    def test_submit_move_as_computer(self):
        # Test Computer Submit Move
        my_board = Board()
        player = Player(False)
        move = Move(7)
        my_board.submit_move(player, move)
        self.assertEqual(my_board.game_board[2][0], player.marker)

    def test_check_row1(self):

        my_board = Board()
        player = Player()
        # Row 1 Win
        my_board.game_board = [["X", "X", "X"], [0, "O", "O"], [0, 0, 0]]
        move = Move(2)
        self.assertTrue(my_board.check_row(player, move))

    def test_check_row2(self):
        # Test if player won by row 2
        my_board = Board()
        player = Player()
        my_board.game_board = [["O", "O", 0], ["X", "X", "X"], [0, 0, 0]]
        move = Move(6)
        self.assertTrue(my_board.check_row(player, move))

    def test_check_row3(self):
        # Test if player won by row 3
        my_board = Board()
        player = Player()
        my_board.game_board = [["O", "O", 0], [0, 0, 0], ["X", "X", "X"]]
        move = Move(7)
        self.assertTrue(my_board.check_row(player, move))

    def test_check_column1(self):
        # Test if player won by column 1
        my_board = Board()
        player = Player(False)
        my_board.game_board = [["O", 0, "X"], ["O", "X", 0], ["O", 0, 0]]
        move = Move(7)
        self.assertTrue(my_board.check_column(player, move))

    def test_check_column2(self):
        # Test if player won by column 2
        my_board = Board()
        player = Player(False)
        my_board.game_board = [["X", "O", "X"], ["X", "O", 0], [0, "O", 0]]
        move = Move(5)
        self.assertTrue(my_board.check_column(player, move))

    def test_check_column3(self):
        # Test if player won by column 2
        my_board = Board()
        player = Player(False)
        my_board.game_board = [["X", 0, "O"], ["X", 0, "O"], ["X", 0, "O"]]
        move = Move(3)
        self.assertTrue(my_board.check_column(player, move))

    def test_check_diagonal1(self):
        # Test if player won by diagonal1
        my_board = Board()
        player = Player()
        my_board.game_board = [["X", "O", "O"], [0, "X", 0], [0, 0, "X"]]
        self.assertTrue(my_board.check_diagonal1(player))

    def test_check_diagonal2(self):
        # Test if player won by column
        my_board = Board()
        player = Player(False)
        my_board.game_board = [[0, 0, "O"], ["X", "O", 0], ["O", "X", 0]]
        self.assertTrue(my_board.check_diagonal2(player))

    def test_check_is_game_over_row_win(self):
        my_board = Board()
        player = Player()
        my_board.game_board = [["X", "X", "X"], [0, "O", "O"], [0, 0, 0]]
        move = Move(2)
        self.assertEqual(my_board.check_is_game_over(player, move), "Player")

    def test_check_is_game_over_column_win(self):
        my_board = Board()
        player = Player(False)
        my_board.game_board = [["X", "O", "X"], ["X", "O", 0], [0, "O", 0]]
        move = Move(5)
        self.assertEqual(my_board.check_is_game_over(player, move), "Computer")

    def test_check_is_game_over_diagonal1_win(self):
        my_board = Board()
        player = Player()
        my_board.game_board = [["X", "O", "O"], [0, "X", 0], [0, 0, "X"]]
        move = Move(9)
        self.assertEqual(my_board.check_is_game_over(player, move), "Player")

    def test_check_game_over_diagonal2_win(self):
        my_board = Board()
        player = Player(False)
        my_board.game_board = [[0, 0, "O"], ["X", "O", 0], ["O", "X", 0]]
        move = Move(7)
        self.assertEqual(my_board.check_is_game_over(player, move), "Computer")

    def test_check_is_tie(self):
        my_board = Board()
        my_board.game_board = [["X", "X", "O"],
                               ["O", "X", "X"],
                               ["X", "O", "O"]]
        self.assertTrue(my_board.check_is_tie())

    def test_check_is_not_tie(self):
        my_board = Board()
        my_board.game_board = [["X", "X", "O"],
                               ["O", "X", "X"],
                               ["X", 0, "O"]]
        self.assertFalse(my_board.check_is_tie())

    def test_reset_board_success(self):
        my_board = Board()
        my_board.game_board = [["X", "X", "O"],
                               ["O", "X", "X"],
                               ["X", "O", "O"]]
        my_board.rest_board()
        self.assertEqual(my_board.game_board, EMPTY_GAME_BOARD)
