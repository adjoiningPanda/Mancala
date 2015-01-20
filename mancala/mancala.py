__author__ = 'robby'


HUMAN = 1
MINIMAX = 2
AND_OR = 3

import player.human_player
import player.minimax_player
import player.and_or_player

import prettytable

from read_int import read_int


class IllegalBoardSizeError(StandardError):
    pass


class Mancala(object):
    def __init__(self, board_size=4, pebbles_per_square=2):
        if board_size % 2 != 0:
            raise IllegalBoardSizeError("Board size must be an even number")

        self.board = [pebbles_per_square] * board_size

    def __str__(self):
        table_headers = ['Player'] + [str(i) for i in xrange(1, (len(self.board) / 2) + 1)]
        table = prettytable.PrettyTable(table_headers)

        split = Mancala._get_board_split_position(self.board)
        row_one = self.board[:split]
        row_two = self.board[split:]

        table.add_row(['Player 1'] + row_one)
        table.add_row(['Player 2'] + row_two)

        return table.__str__()


    @staticmethod
    def _get_board_split_position(board):
        """
        :param board:
        :return: Middle position of the board
        """
        split_point = len(board) / 2
        return split_point

    @staticmethod
    def _get_square_position(board, player_number, square):
        """
        Gets the true square position in the board array for square and player_number
        :param board: array of pebbles
        :param player_number: which player's position is needed
        :param square: square (1...len(board))
        :return: index of true square position
        """
        return (square - 1) + (Mancala._get_board_split_position(board) * (player_number - 1))

    @staticmethod
    def _get_move_to_position(board, move_square):
        """
        Returns the index of the board array that will get updated when move_square is moved
        :param board: Array of pebbles
        :param move_square:  Which square is being moved
        :return: Index of board array that will be updated when move_square is moved
        """
        move_to_position = 0
        split = Mancala._get_board_split_position(board)

        if move_square == split:
            move_to_position = move_square - split
        elif move_square == split - 1:
            move_to_position = move_square + split
        elif move_square < split:
            move_to_position = move_square + 1
        elif move_square > split:
            move_to_position = move_square - 1

        return move_to_position

    def move(self, player_number, square):
        """
        Update board array based on which square player_number has moved
        :param player_number:
        :param square:
        :return: None
        """
        self.board = Mancala.simulate_move(self.board, player_number, square)
        return

    @staticmethod
    def simulate_move(board, player_number, square):
        """
        Simulate player_number's move on board with selection square.
        :param board:
        :param player_number:
        :param square:
        :return: The board representation after the move has been made
        """
        state = board[:]
        position = Mancala._get_square_position(state, player_number, square)
        pebbles = state[position]
        state[position] -= pebbles

        for i in xrange(pebbles):
            move_to_position = Mancala._get_move_to_position(state, position)
            state[move_to_position] += 1
            position = move_to_position

        return state

    @staticmethod
    def game_over(board):
        """

        :param board:
        :return: Boolean representing if the game is over
        """
        board_split_position = Mancala._get_board_split_position(board)
        return sum(board[:board_split_position]) == 0 or sum(board[board_split_position:]) == 0

    @staticmethod
    def _get_player_row_ranges(board, player_number):
        """
        Return the lower and upper bounds of indexes for player_number on board
        :param board:
        :param player_number:
        :return: (lower_range, upper_range)
        """

        split = Mancala._get_board_split_position(board)
        if player_number == 1:
            lower_range = 0
            upper_range = split
        else:
            lower_range = split
            upper_range = len(board)
        return lower_range, upper_range

    @staticmethod
    def utility(board, player_number):
        """
        Gets the utility value of board for player_number. This is the sum of pebbles in the player's row.
        :param board:
        :param player_number:
        :return: utility
        """

        lower_range, upper_range = Mancala._get_player_row_ranges(board, player_number)
        return sum(board[lower_range:upper_range])

    @staticmethod
    def actions(board, player_number):
        """
        Returns a list of actions available to player_number on board. Actions are "1 based" squares
        :param board:
        :param player_number:
        :return:
        """
        lower_range, upper_range = Mancala._get_player_row_ranges(board, player_number)
        return [index + 1 for index, pebbles in enumerate(board[lower_range:upper_range]) if pebbles != 0]

    @staticmethod
    def announce_winner(board):
        """
        Prints winner of the game
        :param board:
        :return:
        """
        board_split_position = Mancala._get_board_split_position(board)
        winner = 2 if sum(board[:board_split_position]) == 0 else 1

        print
        print("Game over - Player {0} wins!".format(winner))

        return

    @staticmethod
    def sorted_actions(board, player_number):
        """
        Returns a list of actions sorted by the minimum number of pebbles. If the player_number is 2, then
        the list is sorted from the right side (ei.e., prefers values on the right).

        E.g.

        2 2
        2 2

        Player 1 would return: [1, 2]
        Player 2 would return: [2, 1]

        :param board:
        :param player_number:
        :return:
        """
        lower_index, upper_index = Mancala._get_player_row_ranges(board, player_number)
        row = [square if square > 0 else float('inf') for square in board[lower_index:upper_index]]

        if player_number == 2:
            row.reverse()

        min_pebbles = []
        number_of_choices = len(row) - row.count(float('inf'))

        while len(min_pebbles) < number_of_choices:
            min_pebble = min(row)
            index = row.index(min_pebble)
            min_pebbles.append(index)
            row[index] = float('inf')

        if player_number == 2:
            min_pebbles = [len(row) - index for index in min_pebbles]
        else:
            min_pebbles = [index + 1 for index in min_pebbles]

        return min_pebbles


def read_pebbles():
    """
    Read number of players from board

    :return:
    """
    pebbles_per_square = 0
    while pebbles_per_square <= 0:
        error_message = "Must enter an integer > 0"
        pebbles_per_square = read_int("Number of pebbles per square: ", error_message)

        if pebbles_per_square <= 0:
            print error_message

    return pebbles_per_square

def play(board_size=4, plys=4, move_automatically=False):
    """
    Main loop for mancala.

    :param board_size: Board size (must be even)
    :param plys: Number of plys AI player(s) should use
    :param move_automatically: If the AI should move automatically or not
    :return: None
    """
    game = Mancala(board_size=board_size, pebbles_per_square=read_pebbles())
    player_one = read_player('1', plys, move_automatically)
    player_two = read_player('2', plys, move_automatically)

    while not game.game_over(game.board):
        for player in [player_one, player_two]:
            print player
            print("Game state\n{0}".format(game))
            board = player.take_turn(game.board)
            game.board = board

            if game.game_over(game.board):
                break

    Mancala.announce_winner(game.board)
    print game
    print

    return


def read_player(player_number, plys, move_automatically):
    """
    Read in the player_number and create Player object based on user input
    :param player_number:
    :param plys:
    :param move_automatically:
    :return: Player object
    """
    message = 'Player {0} selection: '.format(player_number)
    error_message = 'Must enter integer between 1 and 3'

    selected_player = None

    print ("1 - Human Player")
    print ("2 - Mancala AI (minimax)")
    print ("3 - Mancala AI (and-or-graph search)")
    print

    valid_input = [1, 2, 3]
    while selected_player not in valid_input:
        selected_player = read_int(message, error_message)

        if selected_player not in valid_input:
            print(error_message)

    return _get_player_type(selected_player, player_number, plys, move_automatically)


def _get_player_type(selected_player, player_number, plys, move_automatically):
    """
    Return player object based on input variables.
    :param selected_player: Integer constant representing a player type
    :param player_number: The player number that the player represents
    :param plys: Number of plys (for AI)
    :param move_automatically:  If the AI should move automatically.
    :return: Player object
    """
    player_type = None

    if selected_player == HUMAN:
        player_type = player.human_player.HumanPlayer(player_number)
    elif selected_player == MINIMAX:
        player_type = player.minimax_player.MinimaxPlayer(player_number, plys=plys,
                                                          move_automatically=move_automatically)
    elif selected_player == AND_OR:
        player_type = player.and_or_player.AndOrPlayer(player_number, plys=plys, move_automatically=move_automatically)

    return player_type


def read_number_of_squares():
    """
    Read desired number of square per player
    :return: number of squares per player
    """
    board_size = 1
    while board_size <= 1:
        error_message = "Must enter a number > 1"
        board_size = read_int("Squares per player (number > 1): ", error_message)

        if board_size <= 1:
            print(error_message)

    return board_size


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Play Mancala - or just watch some AI duke it out')
    parser.add_argument("-p", "--plys", dest="plys", type=int,
                        default=4,
                        help="Number of plys the AI player(s) should use")
    parser.add_argument("-a", "--auto", dest="move_automatically",
                        default=False, action="store_true",
                        help="Enable automatic movement for the computer players")

    args = parser.parse_args()

    print
    play(board_size=read_number_of_squares() * 2, plys=args.plys, move_automatically=args.move_automatically)

# if __name__ == "__main__":
#     board = [2,2,2,2]
#     player = player.and_or_player.AndOrPlayer(player=1, move_automatically=True, plys=8)
#     print player.take_turn(board)
#     pass
