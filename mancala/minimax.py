'''
Created on Dec 4, 2014

@author: fmz0001
'''

def alpha_beta_search(state, plys):
    v = -float("inf")
    a = None
    alpha = -float("inf")
    beta = float("inf")

    states = []
    states.append(state)
    for action in ACTIONS(state):
        state_prime = RESULT(state, action)
        v_prime = MIN(state_prime, alpha, beta, plys, states)
        if v_prime > v:
            v = v_prime
            a = action
        if v >= beta:
            return a
        elif v > a:
            a = v 
            
    return a
        
        
def ACTIONS(state):
    pass

def RESULT(state, action):
    pass

def UTILITY(state):
    pass

def TERMINAL_TEST(state):
    pass
'''
Created on Dec 4, 2014

@author: fmz0001
'''

def alpha_beta_search(state, plys):
    v = -float("inf")
    a = None
    alpha = -float("inf")
    beta = float("inf")

    states = []
    states.append(state)
    for action in ACTIONS(state):
        state_prime = RESULT(state, action)
        v_prime = MIN(state_prime, alpha, beta, plys, states)
        if v_prime > v:
            v = v_prime
            a = action
        if v >= beta:
            return a
        elif v > a:
            a = v

    return a


def ACTIONS(state):
    pass

def RESULT(state, action):
    pass

def UTILITY(state):
    pass

def TERMINAL_TEST(state):
    pass

def MIN(state, alpha, beta, plys, states):

    if plys > 0:
        plys = plys - 1
    else:
        return UTILITY(state)

    if state not in states:
        states.append(state)
        if TERMINAL_TEST(state):
            return UTILITY(state)
        v = float("inf")
        for action in ACTIONS(state):
            state_prime = RESULT(state, action)
            v_prime = MAX(state_prime, alpha, beta, plys, states)
            if v_prime < v:
                v = v_prime
            if v <= alpha:
                return v_prime
            elif v < beta:
                beta = v
        return v
    else:
        return float("inf")

def MAX(state, alpha, beta, plys, states):

    if plys > 0:
        plys = plys - 1
    else:
        return UTILITY(state)

    if state not in states:
        states.append(state)
        if TERMINAL_TEST(state):
            return UTILITY(state)
        v = -float("inf")
        for action in ACTIONS(state):
            state_prime = RESULT(state, action)
            v_prime = MIN(state_prime, alpha, beta, plys, states)
            if v_prime > v:
                v = v_prime
            if v >= beta:
                return v
            elif v > alpha:
                alpha = v
        return v
    else:
        return -float("inf")

def MIN(state, alpha, beta, plys, states):
        
    if plys > 0:
        plys = plys - 1
    else:
        return UTILITY(state)
    
    if state not in states:
        states.append(state)
        if TERMINAL_TEST(state):
            return UTILITY(state)
        v = float("inf")
        for action in ACTIONS(state):
            state_prime = RESULT(state, action)
            v_prime = MAX(state_prime, alpha, beta, plys, states)
            if v_prime < v:
                v = v_prime
            if v <= alpha:
                return v_prime
            elif v < beta:
                beta = v 
        return v 
    else:
        return float("inf")

def MAX(state, alpha, beta, plys, states):

    if plys > 0:
        plys = plys - 1
    else:
        return UTILITY(state)
    
    if state not in states:
        states.append(state)
        if TERMINAL_TEST(state):
            return UTILITY(state)
        v = -float("inf")
        for action in ACTIONS(state):
            state_prime = RESULT(state, action)
            v_prime = MIN(state_prime, alpha, beta, plys, states)
            if v_prime > v:
                v = v_prime
            if v >= beta:
                return v 
            elif v > alpha:
                alpha = v
        return v 
    else:
        return -float("inf") 
        