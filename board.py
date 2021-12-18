from move import Move
from player import Player
from move import Move


class Board:

    EMPTY_CELL = 0

    def __init__(self):
        self.game_board = [[0, 0, 0],
                           [0, 0, 0],
                           [0, 0, 0]]

    def print_board(self):
        print("\nPositions:")
        self.print_board_with_positions()

        print("Board:")
        for row in self.game_board:
            print("|", end="")
            for column in row:
                if column == Board.EMPTY_CELL:
                    print("   |", end="")
                else:
                    print(f" {column} |", end="")
            print()
        print()

    def print_board_with_positions(self):
        print("| 1 | 2 | 3 |")
        print("| 4 | 5 | 6 |")
        print("| 7 | 8 | 9 |")

    def submit_move(self, player, move):
        row = move.get_row()
        column = move.get_column()
        value = self.game_board[row][column]
        if value == Board.EMPTY_CELL:
            self.game_board[row][column] = player.marker
        else:
            print("This position is already taken.  Please enter another one.")

    def check_is_game_over(self, player, last_move):
        if (self.check_row(player, last_move)
                or self.check_column(player, last_move)
                or self.check_diagonal1(player)
                or self.check_diagonal2(player)):
            if player.marker == "X":
                print(f"Game Over Player Won!")
                return "Player"
            if player.marker == "O":
                print(f"Game Over Computer Won!")
                return "Computer"

    def check_row(self, player, last_move):
        row_index = last_move.get_row()
        board_row = self.game_board[row_index]
        return board_row.count(player.marker) == 3

    def check_column(self, player, last_move):
        markers_count = 0
        column_index = last_move.get_column()
        for i in range(3):
            if self.game_board[i][column_index] == player.marker:
                markers_count += 1
        if markers_count == 3:
            return True
        else:
            return False

    def check_diagonal1(self, player):
        markers_count = 0
        for i in range(3):
            if self.game_board[i][i] == player.marker:
                markers_count += 1
        if markers_count == 3:
            return True
        else:
            return False

    def check_diagonal2(self, player):
        markers_count = 0
        index = 2
        for i in range(3):
            if self.game_board[index][i] == player.marker:
                markers_count += 1
            index -= 1
        if markers_count == 3:
            return True
        else:
            return False
