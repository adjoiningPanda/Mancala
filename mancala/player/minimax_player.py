__author__ = 'robby'

import computer_player
import mancala
import random
import time

INFINITY = float("inf")

class MinimaxPlayer(computer_player.ComputerPlayer):
    """
    Class representing the minimax AI player
    """
    def __init__(self, player, plys=3, move_automatically=False):
        super(MinimaxPlayer, self).__init__(player, plys=plys, move_automatically=move_automatically)
        self.type = 'minimax'

    def _take_turn(self, board):
        return mancala.Mancala.simulate_move(board, self.player, alpha_beta_search(board, self.plys, self.player))


def get_next_moving_player(player):
    """
    Returns the next moving player based on the input player

    :param player: Current player
    :return: 1 or 2
    """
    return 2 if player == 1 else 1


def alpha_beta_search(state, plys, player):
    """
    Returns an action based on the given player, state, and plys.

    :param state: State planning for
    :param plys: Number of plys to search
    :param player: Player planning their action
    :return: action
    """
    v = -INFINITY
    action = None
    alpha = -INFINITY
    beta = INFINITY

    states = [state]
    actions = mancala.Mancala.sorted_actions(state, player)
    for each_action in mancala.Mancala.sorted_actions(state, player):
        state_prime = mancala.Mancala.simulate_move(state, player, each_action)
        v_prime = _min(state_prime, alpha, beta, plys, states, player)
        if v_prime > v:
            v = v_prime
            action = each_action
        if v >= beta:
            return action
        elif v > alpha:
            alpha = v

    if action is None:
        random.seed(time.time())
        return actions[random.randint(0, len(actions) - 1)]
    else:
        return action



def _min(state, alpha, beta, plys, states, player):
    """

    :param state:
    :param alpha:
    :param beta:
    :param plys:
    :param states:
    :param player:
    :return: utility value of the state being searched
    """
    moving_player = get_next_moving_player(player)

    if plys > 0:
        plys -= 1
    else:
        return mancala.Mancala.utility(state, moving_player)

    if state not in states:
        states.append(state)

        if mancala.Mancala.game_over(state):
            return mancala.Mancala.utility(state, moving_player)

        v = INFINITY

        for action in mancala.Mancala.sorted_actions(state, moving_player):
            state_prime = mancala.Mancala.simulate_move(state, moving_player, action)
            v_prime = _max(state_prime, alpha, beta, plys, states, moving_player)
            if v_prime < v:
                v = v_prime
            if v <= alpha:
                return v_prime
            elif v < beta:
                beta = v
        return v

    else:
        return INFINITY


def _max(state, alpha, beta, plys, states, player):
    """

    :param state:
    :param alpha:
    :param beta:
    :param plys:
    :param states:
    :param player:
    :return: utility value of the state being searched
    """
    moving_player = get_next_moving_player(player)

    if plys > 0:
        plys -= 1
    else:
        return mancala.Mancala.utility(state, moving_player)

    if state not in states:
        states.append(state)
        if mancala.Mancala.game_over(state):
            return mancala.Mancala.utility(state, moving_player)

        v = -INFINITY

        for action in mancala.Mancala.sorted_actions(state, moving_player):
            state_prime = mancala.Mancala.simulate_move(state, moving_player, action)
            v_prime = _min(state_prime, alpha, beta, plys, states, moving_player)
            if v_prime > v:
                v = v_prime
            if v >= beta:
                return v
            elif v > alpha:
                alpha = v
        return v
    else:
        return -INFINITY

