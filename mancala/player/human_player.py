__author__ = 'robby'

import player

# from ..mancala import mancala
import mancala
from read_int import read_int


class HumanPlayer(player.Player):

    def take_turn(self, board):
        square = None
        upper_square_number = len(board) / 2
        error_message = "Must enter an integer between 1 and {0}".format(upper_square_number)
        while not square:
            square = read_int("Select a square (1 - {0}): ".format(upper_square_number), error_message)

            if board[square] == 0:
                print("Must select square with pebbles in it.")

            if square not in xrange(1, upper_square_number):
                print(error_message)


        return mancala.Mancala.simulate_move(board, int(self.player), square)