def getInvCount(arr):
    inv_count = 0
    empty_value = -1
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    return inv_count

def isSolvable(puzzle):

    inv_count = getInvCount([j for sub in puzzle for j in sub])


    return (inv_count % 2 == 0)




puzzle = [[2, 3, 8], [5, 1, 4], [6, 0, 7]]
if (isSolvable(puzzle)):
    print("Solvable")
else:
    print("Not Solvable")