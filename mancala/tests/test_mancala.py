__author__ = 'robby'

import unittest
import pytest

from .. import mancala


def get_game(board_size=4):
    return mancala.Mancala(board_size=board_size)


def test_mancala_constructor():
    assert get_game().board == [2, 2, 2, 2]

    #make sure we can't make odd sized boards
    with pytest.raises(mancala.IllegalBoardSizeError):
        get_game(board_size=5)

    assert get_game(board_size=8).board == [2, 2, 2, 2, 2, 2, 2, 2]



def test_move():
    game = get_game()
    player = 1
    square = 1

    game.move(player, square)
    expected = [0, 3, 2, 3]
    assert expected == game.board

    game.move(player, square)
    assert expected == game.board

    square = 2
    expected = [1, 0, 3, 4]
    game.move(player, square)
    assert expected == game.board

    player = 2
    square = 1
    expected = [2, 1, 0, 5]
    game.move(player, square)
    assert expected == game.board

    square = 2
    expected = [3, 2, 2, 1]
    game.move(player, square)
    assert expected == game.board

    game.board = [0, 6, 2, 0]
    square = 1
    game.move(player, square)
    expected = [1, 7, 0, 0]
    assert expected == game.board

    square = 1
    game.board = [3, 0, 5, 0]
    game.move(player, square)
    expected = [5, 1, 1, 1]
    assert expected == game.board


def test_get_move_to_position():
    game = get_game()
    last_square = 0

    expected = 1
    assert expected == mancala.Mancala._get_move_to_position(game.board, last_square)

    last_square = 1
    expected = 3
    assert expected == mancala.Mancala._get_move_to_position(game.board, last_square)

    last_square = 3
    expected = 2
    assert expected == mancala.Mancala._get_move_to_position(game.board, last_square)

    last_square = 2
    expected = 0
    assert expected == mancala.Mancala._get_move_to_position(game.board, last_square)

# @pytest.skip()
def test_move_board_size_six():
    game = get_game(board_size=6)
    game.move(1, 2)
    expected = [2, 0, 3, 2, 2, 3]
    assert expected == game.board

    game.move(2, 1)
    expected = [3, 1, 3, 0, 2, 3]
    assert expected == game.board

    game.move(1, 1)
    expected = [0, 2, 4, 0, 2, 4]
    assert expected == game.board

def test_simulate_move():
    board = get_game().board
    player = 1
    square = 1

    updated_board = mancala.Mancala.simulate_move(board, player, square)
    expected = [0, 3, 2, 3]
    assert expected == updated_board

    updated_board = mancala.Mancala.simulate_move(updated_board, player, square)
    assert expected == updated_board

    square = 2
    expected = [1, 0, 3, 4]
    updated_board = mancala.Mancala.simulate_move(updated_board, player, square)
    assert expected == updated_board

    player = 2
    square = 1
    expected = [2, 1, 0, 5]
    updated_board = mancala.Mancala.simulate_move(updated_board, player, square)
    assert expected == updated_board

    square = 2
    expected = [3, 2, 2, 1]
    updated_board = mancala.Mancala.simulate_move(updated_board, player, square)
    assert expected == updated_board

    square = 2
    player = 1
    updated_board = [1, 6, 1, 0]
    expected = [2, 1, 3, 2]
    updated_board = mancala.Mancala.simulate_move(updated_board, player, square)
    assert expected == updated_board

def test_get_position():
    board = get_game().board
    assert mancala.Mancala._get_square_position(board, 1, 1) == 0
    assert mancala.Mancala._get_square_position(board, 1, 2) == 1
    assert mancala.Mancala._get_square_position(board, 2, 1) == 2
    assert mancala.Mancala._get_square_position(board, 2, 2) == 3

def test_get_position_board_size_six():
    board = get_game(board_size=6).board
    assert mancala.Mancala._get_square_position(board, 1, 1) == 0
    assert mancala.Mancala._get_square_position(board, 1, 2) == 1
    assert mancala.Mancala._get_square_position(board, 1, 3) == 2
    assert mancala.Mancala._get_square_position(board, 2, 1) == 3
    assert mancala.Mancala._get_square_position(board, 2, 2) == 4
    assert mancala.Mancala._get_square_position(board, 2, 3) == 5


def test_game_over():
    game = get_game()
    assert not game.game_over(game.board), "Initial game state should not be a game over"

    game.board = [0, 0, 2, 2]
    assert game.game_over(game.board), "Player 1 with 0 in each position should be a game over"

    game.board = [2, 2, 0, 0]
    assert game.game_over(game.board), "Player 2 with 0 in each position should be a game over"

    # assert

def test_utility():
    board = [2, 2, 2, 2]
    expected = 4

    player = 1
    assert expected == mancala.Mancala.utility(board, player)

    player = 2
    assert expected == mancala.Mancala.utility(board, player)

    expected = 3
    board = [0, 3, 0, 3]
    assert expected == mancala.Mancala.utility(board, player)

    expected = 2
    board = [2, 0, 0, 3]
    player = 1
    assert expected == mancala.Mancala.utility(board, player)

def test_get_actions():
    board = [2, 0, 1, 3, 0, 0]
    expected = [1, 3]
    assert expected == mancala.Mancala.actions(board, 1)

    expected = [1]
    assert expected == mancala.Mancala.actions(board, 2)

    board = [0,5,3,0]
    expected = [1]
    assert expected == mancala.Mancala.actions(board, 2)


def test_sort_actions():
    board = [2, 2, 2, 2]
    player = 1
    expected = [1, 2]
    assert expected == mancala.Mancala.sorted_actions(board, player)

    player = 2
    expected = [2, 1]
    assert expected == mancala.Mancala.sorted_actions(board, player)

    board = [2, 2, 2, 3, 2, 1]
    expected = [3, 2, 1]
    assert expected == mancala.Mancala.sorted_actions(board, player)

    board = [2, 2, 2, 3, 0, 1]
    expected = [3, 1]
    assert expected == mancala.Mancala.sorted_actions(board, player)

    board = [0, 2, 6, 0]
    player = 2
    expected = [1]
    assert expected == mancala.Mancala.sorted_actions(board, player)

    board = [0, 2, 6, 1]
    expected = [2, 1]
    assert expected == mancala.Mancala.sorted_actions(board, player)

    board = [0, 4, 1, 3, 0 ,4]
    expected = [1, 3]
    assert expected == mancala.Mancala.sorted_actions(board, player)

    board = [0, 4, 1, 3, 0 ,4]
    expected = [3, 2]
    player = 1
    assert expected == mancala.Mancala.sorted_actions(board, player)

if __name__ == '__main__':
    unittest.main()
