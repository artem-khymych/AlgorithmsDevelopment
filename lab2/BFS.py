import sys
from queue import Queue
from Puzzle import Puzzle
from datetime import *


def BFS_search(initialState):
    startNode = Puzzle(initialState, None, None, 0)
    if startNode.isSolved():
        return startNode.findSolution()
    q = Queue()
    q.put(startNode)
    visited = []

    while not(q.empty()):
        if (Puzzle.mem[0] > 1024 * 1024 * 1024 or (datetime.now() - Puzzle.time).seconds > 1800):
            print("no solution")
            sys.exit()

        node=q.get()
        visited.append(node.state)
        children=node.generateChild()
        for child in children:
            if child.isSolved():
                return child.findSolution()
            q.put(child)
    return