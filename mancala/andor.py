'''
Created on Dec 4, 2014

@author: fmz0001
'''

global plan

def andOrGraphSearch(problem):
    global plan
    
    plan = []
    orSearch(problem.INITIAL_STATE, problem, [])
    
def orSearch(state, problem, path):
    global plan
    
    if problem.GOAL_TEST(state):
        return plan
    
    if state in path:
        return False
    
    for action in problem.ACTIONS(state):
        path = path.insert(0, state)
        plan = andSearch(RESULTS(state, action), problem, path)
        if plan != False:
            plan = plan.insert(0, action)
            return plan
        return False
    
def RESULTS(state, action):
    pass
    
def andSearch(states, problem, path):
    global plan
    conditionalPlan = []
    
    i = 0 
    for s in states:
        plan[i] = orSearch(s, problem, path)
        if plan[i] is False:
            return False
        else:
            conditionalPlan.append((s,plan[i]))
        
        i = i + 1
            
    return conditionalPlan
        
    
        
        
    
    