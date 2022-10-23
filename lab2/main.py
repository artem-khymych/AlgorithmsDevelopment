from BFS import *
from RBFS import *



startState=[1,3,7,
            5,0,2,
            4,8,6]


bfs=BFS_search(startState)
print('moves:', bfs)
Puzzle.printSolutionLog(Puzzle,bfs,startState)

time = datetime.now()
mem = memory_usage()

rbfs=RBFS_search(startState)
print('moves:', rbfs)
PuzzleWithHeuristic.printSolutionLog(PuzzleWithHeuristic,rbfs,startState)
