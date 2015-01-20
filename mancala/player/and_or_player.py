__author__ = 'robby'

import computer_player
import mancala
import collections

INFINITY = float('inf')
#named tuple representing an and-or search tree node
Node = collections.namedtuple('Node', 'state action player utility')


class AndOrPlayer(computer_player.ComputerPlayer):
    def __init__(self, player, plys=4, move_automatically=False):
        super(AndOrPlayer, self).__init__(player, plys=plys, move_automatically=move_automatically)
        self.type = 'and-or-graph-search'

    def _take_turn(self, board):
        action = and_or_graph_search(board, self.player, self.plys)
        return mancala.Mancala.simulate_move(board, self.player, action)


def append_state(graph, parent_node, child):
    """
    Appends child to parent_node in graph
    :param graph: Current graph state
    :param parent_node:
    :param child:
    :return:
    """
    if str(parent_node) in graph:
        graph[str(parent_node)].append(child)
    else:
        graph[str(parent_node)] = [child]


def get_next_moving_player(player):
    """
    Returns the next moving player based on the input player

    :param player: Current player
    :return: 1 or 2
    """
    return 2 if player == 1 else 1


def and_or_graph_search(problem, player, plys):
    """
    Run the and_or_graph_search algorithm and return the first action from the final plan
    :param problem: The initial mancala board state
    :param player: Which player is planning
    :param plys: Number of plys to search
    :return:
    """
    plan = []
    path = {}
    next_moving_player = get_next_moving_player(player)
    final_plan = or_search(problem, path, next_moving_player, plan, plys)
    return final_plan.pop(0)


def propagate_action(path, state, comparsion_function):
    """
    Selects the action to propagate based on the state, current path, and comparison function
    :param path: Graph of the search tree
    :param state: State to search for in graph to use for heuristic comparisons
    :param comparsion_function: Comparison function (either min or max)
    :return: action to propagate
    """
    nodes = path[parent(path, state)]
    heuristics = [utility for state, action, each_player, utility in nodes]
    value = comparsion_function(heuristics)
    return nodes[heuristics.index(value)].action


def parent(graph, child):
    """
    Returns the parent for child in graph. The child is the game state, not the child node
    e.g.

    { '[2, 2, 2, 2]' : ([?, ?, ?, ?], action, player, value) }
    '[2, 2, 2, 2]' is the parent of [?, ?, ?, ?]
    :param graph:
    :param child:
    :return:
    """
    for key in graph.keys():
        for each_child in graph[key]:
            if each_child.state == child:
                return key


def or_search(state, path, next_moving_player, plan, plys):
    """

    :param state:
    :param problem:
    :param path:
    :param next_moving_player: Must be set to the opposite of the the planning player, intially
    :return:
    """

    moving_player = get_next_moving_player(next_moving_player)
    state = state[:]
    if plys > 0:
        plys -= 1
    else:
        return propagate_action(path, state, max)

    if mancala.Mancala.game_over(state):
        return mancala.Mancala.utility(state, moving_player)

    if str(state) in path:
        return -INFINITY

    for action in mancala.Mancala.actions(state, moving_player):
        result = mancala.Mancala.simulate_move(state, moving_player, action)
        utility = mancala.Mancala.utility(result, moving_player)
        append_state(path, state, Node(state=result, action=action, player=moving_player, utility=utility))

        and_plan = and_search([result], path, moving_player, plan, plys)
        if and_plan != -INFINITY:
            plan.insert(0, action)
            return plan

    return -INFINITY


def and_search(states, path, next_moving_player, plan, plys):
    """

    :param states:
    :param path:
    :param next_moving_player: Player that
    :param plan:
    :param plys:
    :return:
    """
    conditional_plan = []

    if plys > 0:
        plys -= 1
    else:
        return propagate_action(path, states[0], min)

    for state in states:
        or_plan = or_search(state, path, next_moving_player, plan, plys)
        if or_plan == -INFINITY:
            return INFINITY
        else:
            conditional_plan.append(or_plan)

    return conditional_plan
