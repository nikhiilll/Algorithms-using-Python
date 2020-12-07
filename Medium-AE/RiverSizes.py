import time

def findRiver(matrix, row, column, visited):

    if matrix[row][column] == 0 or visited[row][column]:
        return 0
    
    visited[row][column] = True
    
    rightRow, rightColumn = row, column + 1
    downRow, downColumn = row + 1, column
    upRow, upColumn = row - 1, column
    leftRow, leftColumn = row, column - 1
    downRiverSize, rightRiverSize, leftRiverSize, upRiverSize = 0, 0, 0, 0

    if rightRow < len(matrix) and rightColumn < len(matrix[0]) and not visited[rightRow][rightColumn]:
        rightRiverSize = findRiver(matrix, rightRow, rightColumn, visited)
    if downRow < len(matrix) and downColumn < len(matrix[0]) and not visited[downRow][downColumn]:
        downRiverSize = findRiver(matrix, downRow, downColumn, visited)
    if upRow > -1 and upColumn > -1 and not visited[upRow][upColumn]:
        upRiverSize = findRiver(matrix, upRow, upColumn, visited)
    if leftRow > -1 and leftColumn > -1 and not visited[leftRow][leftColumn]:
        leftRiverSize = findRiver(matrix, leftRow, leftColumn, visited)
    
    return (1 + rightRiverSize + downRiverSize + upRiverSize + leftRiverSize)


def riverSizes(matrix):

    visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    rivers = []
    rows = len(matrix)
    columns = len(matrix[0])

    for row in range(rows):
        for column in range(columns):

            if visited[row][column]:
                continue

            if matrix[row][column] == 0:
                continue
            else:
                rivers.append(findRiver(matrix, row, column, visited))
    
    return rivers

matrix = [
  [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0]
]
startTime = time.time()
print(riverSizes(matrix))
print(time.time() - startTime)


def getUnvisitedNeighbours(matrix, i, j, visited):

    unvisitedNeighbours = []

    if i > 0 and not visited[i - 1][j]:
        unvisitedNeighbours.append([i - 1, j])
    if i < len(matrix) - 1 and not visited[i + 1][j]:
        unvisitedNeighbours.append([i + 1, j])
    if j > 0 and not visited[i][j - 1]:
        unvisitedNeighbours.append([i, j - 1])
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
        unvisitedNeighbours.append([i, j + 1])
    
    return unvisitedNeighbours



def traverseNodes(matrix, row, column, visited, rivers):

    currentRiverSize = 0
    nodesToExplore = [[row, column]]

    while nodesToExplore:
        currentNode = nodesToExplore.pop()
        i = currentNode[0]
        j = currentNode[1]

        if visited[i][j]: 
            continue
        
        visited[i][j] = True

        if matrix[i][j] == 0:
            continue

        currentRiverSize += 1
        unvisitedNeighbours = getUnvisitedNeighbours(matrix, i, j, visited)
        for neighbour in unvisitedNeighbours:
            nodesToExplore.append(neighbour)
        
    if currentRiverSize > 0:
        rivers.append(currentRiverSize)




def riverSizes2(matrix):

    visited = [[False for _ in matrix[0]] for _ in matrix]
    rivers = []

    for row in range(len(matrix)):
        for column in range(len(matrix[0])):

            if visited[row][column]:
                continue

            traverseNodes(matrix, row, column, visited, rivers)
    
    return rivers

matrix = [
  [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0]
]
startTime = time.time()
print(riverSizes2(matrix))
print(time.time() - startTime)