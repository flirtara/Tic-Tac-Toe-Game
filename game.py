from board import Board
from player import Player


class TicTacToeGame:

    def start(self):
        print("**************************")
        print("  Welcome to Tic-Tac-Toe  ")
        print("**************************")

        board = Board()
        player = Player()
        computer = Player(False)

        board.print_board()
        # Ask the user if he/she would like to play another round?
        while True:
            # Main Game
            while True:
                player_move = player.get_move()
                board.submit_move(player, player_move)
                board.print_board()

                if board.check_is_tie():
                    print("It is a Tie!  Try again.")
                    break
                elif board.check_is_game_over(player, player_move):
                    print("Congrats \U0001F44F You Won the Game!")
                    break
                else:
                    computer_move = computer.get_move()
                    board.submit_move(computer, computer_move)
                    board.print_board()

                    if board.check_is_game_over(computer, computer_move):
                        print(" \U0001F62E Sorry, the Computer won.  Try again.")
                        break
            play_again = input("Would you like to play again? [Y/n]: ").upper()

            if play_again == "N":
                print("Bye! Come back soon. \U0001F44B ")
                break
            elif play_again == "Y":
                self.start_new_round(board)
            else:
                print("Your input was not valid.")
                print("I assume you do not want to play again.")
                print("Bye! Come back soon. \U0001F44B ")
                break

    def start_new_round(self, board):
        print("**************************")
        print("        New Round         ")
        print("**************************")
        board.reset_board()
        board.print_board()


game = TicTacToeGame()
game.start()
