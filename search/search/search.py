# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm. Graph Search la de khong search lai state da co

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    actions = list()
    fringeStack = util.Stack()
    ###############################################################################################
    #Cach code cu nay voi phan depth first search thi khong sao vi luc nao no cung tim left most  #
    #fringe.push(([problem.getStartState()], list()))                                             #
    #while not fringe.isEmpty():                                                                  #  
    #    states, current_act = fringe.pop()                                                       #
    #    if (problem.isGoalState(states[len(states)-1])):                                         #  
    #        actions = current_act                                                                #
    #        break                                                                                #
    #    successors = problem.getSuccessors(states[len(states)-1])                                #
    #    for successor in successors:                                                             #
    #        if successor[0] not in states:                                                       #
    #            fringe.push((states+[successor[0]], current_act+[successor[1]]))                 #
    ###############################################################################################
    existed_states = list()
    fringeStack.push((problem.getStartState(), actions))
    
    while not fringeStack.isEmpty():
        currentState, currentActions = fringeStack.pop()
        if problem.isGoalState(currentState):
            return currentActions
        # check if State in closed set or not because Graph search require this
        if currentState not in existed_states:
            existed_states.append(currentState)
            successors = problem.getSuccessors(currentState)
            for child in successors:
                # successor, action, stepCost
                s, a, sc = child
                actions = currentActions + [a]
                fringeStack.push((s, actions))
    return actions

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    actions = list()
    fringeQueue = util.Queue() 
    ###############################################################################################
    #Cach code cu nay van se bi lap khi expand node: vi du: trong queue co: [B, A] [C,A], [C,B,A] #
    #fringe.push(([problem.getStartState()], list()))                                             #
    #while not fringe.isEmpty():                                                                  #  
    #    states, current_act = fringe.pop()                                                       #
    #    if (problem.isGoalState(states[len(states)-1])):                                         #  
    #        actions = current_act                                                                #
    #        break                                                                                #
    #    successors = problem.getSuccessors(states[len(states)-1])                                #
    #    for successor in successors:                                                             #
    #        if successor[0] not in states:                                                       #
    #            fringe.push((states+[successor[0]], current_act+[successor[1]]))                 #
    ###############################################################################################
    existed_states = list()
    fringeQueue.push((problem.getStartState(), actions))
    
    while not fringeQueue.isEmpty():
        currentState, currentActions = fringeQueue.pop()
        if problem.isGoalState(currentState):
            return currentActions
        if currentState not in existed_states:
            existed_states.append(currentState)
            successors = problem.getSuccessors(currentState)
            for child in successors:
                # successor, action, stepCost
                s, a, sc = child
                actions = currentActions + [a]
                fringeQueue.push((s, actions))
    return actions

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    actions = list()
    existed_states = list()
    fringePriority = util.PriorityQueue() #  stack nay se luu lai toan bo state va step o moi lan search (add them state vao list cua state da co), add them act vao list cua act da co
    fringePriority.push((problem.getStartState(), actions), 0)
    while not fringePriority.isEmpty():
        currentState, currentActions = fringePriority.pop()
        if (problem.isGoalState(currentState)):
            return currentActions 
        if currentState not in existed_states:
            existed_states.append(currentState)
            successors = problem.getSuccessors(currentState)
            for child in successors:
                s, a ,sc = child
                actions = currentActions + [a]
                fringePriority.update((s, actions), problem.getCostOfActions(currentActions) + sc)
    return actions

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    ### Khong the su dung dc PriorityQueueWithFunc? Khong hieu ###
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    actions = list()
    existed_states = list()
    fringePQWithFunc = util.PriorityQueue()
    fringePQWithFunc.push((problem.getStartState(), actions),0)
    while not fringePQWithFunc.isEmpty():
        currentState, currentActions = fringePQWithFunc.pop()
        if (problem.isGoalState(currentState)):
            return currentActions 
        if currentState not in existed_states:
            existed_states.append(currentState)
            successors = problem.getSuccessors(currentState)
            for child in successors:
                s, a ,sc = child
                actions = currentActions + [a]
                fringePQWithFunc.update((s, actions), problem.getCostOfActions(currentActions) + sc + heuristic(s, problem))
    return actions

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
