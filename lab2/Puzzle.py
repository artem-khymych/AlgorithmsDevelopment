from datetime import *
from memory_profiler import memory_usage

class Puzzle:
    puzzleSolution=[1,2,3,4,5,6,7,8,0]
    time = datetime.now()
    mem = memory_usage()
    movesCount=0
    def __init__(self,state,parent,move,pathCost):
        self.parent=parent
        self.state=state
        self.move=move
        if parent:
            self.pathCost = parent.pathCost + pathCost
        else:
            self.pathCost = pathCost
        Puzzle.movesCount+=1

    def isSolved(self):
        if self.state == self.puzzleSolution:
            return True
        return False

    def findPosibleMoves(self,x, y):
        posibleMoves = ['Up', 'Down', 'Left', 'Right']
        if x == 0:
            posibleMoves.remove('Up')
        elif x == 2:
            posibleMoves.remove('Down')
        if y == 0:
            posibleMoves.remove('Left')
        elif y == 2:
            posibleMoves.remove('Right')
        return posibleMoves

    def generateChild(self):
        children = []
        zeroPos = self.state.index(0)
        zeroX = int(zeroPos / 3)
        zeroY = int(zeroPos % 3)

        posibleMoves = self.findPosibleMoves(zeroX, zeroY)

        for move in posibleMoves:
            childState = self.state.copy()
            if move == 'Up':
                childState[zeroPos], childState[zeroPos - 3] = childState[zeroPos - 3],childState[zeroPos]
            elif move == 'Down':
                childState[zeroPos], childState[zeroPos + 3] = childState[zeroPos + 3],childState[zeroPos]
            elif move == 'Left':
                childState[zeroPos], childState[zeroPos - 1] = childState[zeroPos - 1],childState[zeroPos]
            elif move == 'Right':
                childState[zeroPos], childState[zeroPos + 1] = childState[zeroPos + 1],childState[zeroPos]
            children.append(Puzzle(childState, self,move, 1))
        return children

    def findSolution(self):
        solutionLog = []
        solutionLog.append(self.move)
        path = self
        while path.parent != None:
            path = path.parent
            solutionLog.append(path.move)
        solutionLog = solutionLog[:-1]
        solutionLog.reverse()
        return solutionLog
    def printSolutionLog(self,solutionLog, startState):
        print(str(startState[0:3]) + '\n' + str(startState[3:6]) + '\n' + str(startState[6:9]))
        print("\t|\n\tV")

        for move in solutionLog:
            zeroPos = startState.index(0)
            if move == 'Up':
                startState[zeroPos], startState[zeroPos - 3] = startState[zeroPos - 3], startState[zeroPos]
                print(str(startState[0:3]) + '\n' + str(startState[3:6]) + '\n' + str(startState[6:9]))
                print("\t|\n\tV")
            elif move == 'Down':
                startState[zeroPos], startState[zeroPos + 3] = startState[zeroPos + 3], startState[zeroPos]
                print(str(startState[0:3]) + '\n' + str(startState[3:6]) + '\n' + str(startState[6:9]))
                print("\t|\n\tV")
            elif move == 'Left':
                startState[zeroPos], startState[zeroPos - 1] = startState[zeroPos - 1], startState[zeroPos]
                print(str(startState[0:3]) + '\n' + str(startState[3:6]) + '\n' + str(startState[6:9]))
                print("\t|\n\tV")
            elif move == 'Right':
                startState[zeroPos], startState[zeroPos + 1] = startState[zeroPos + 1], startState[zeroPos]
                print(str(startState[0:3]) + '\n' + str(startState[3:6]) + '\n' + str(startState[6:9]))
                print("\t|\n\tV")