from PuzzleWithHeuristic import *
import sys
from datetime import *
def RBFS_search(initial_state):

    node=search(PuzzleWithHeuristic(state=initial_state, parent=None, move=None, pathCost=0),fLimit=maxsize)
    node=node[0]
    return node.findSolution()

def search(node, fLimit):
    successors=[]
    if (PuzzleWithHeuristic.mem[0] > 1024*1024*1024 or (datetime.now()-PuzzleWithHeuristic.time).seconds > 1800):
        print("no solution")
        sys.exit()

    if node.isSolved():
        return node,None
    children=node.generateChild()
    if not len(children):
        return None, maxsize
    count=-1
    for child in children:
        if child not in PuzzleWithHeuristic.visited:
            PuzzleWithHeuristic.visited.append(child)
        count+=1
        successors.append((child.evaluationFunction,count,child))


    while len(successors):
        PuzzleWithHeuristic.movesCount += 1
        successors.sort()
        bestNode=successors[0][2]
        if bestNode.evaluationFunction > fLimit:
            return None, bestNode.evaluationFunction
        alternative=successors[1][0]
        result,bestNode.evaluationFunction=search(bestNode,min(fLimit,alternative))
        successors[0]=(bestNode.evaluationFunction,successors[0][1],bestNode)

        if result is not None:
            break

    return result,None