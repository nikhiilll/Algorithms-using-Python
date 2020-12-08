def boggleBoard(board, words):
    
    result = []

    for word in words:
        findIfWordExists(board, word, result)
    
    return result


def findNeighbours(board, row, column, visited):

    neigbours = []

    if row - 1 > -1 and column - 1 > -1 and not visited[row - 1][column - 1]:
        neigbours.append([row - 1, column - 1])
    
    if row - 1 > -1 and not visited[row - 1][column]:
        neigbours.append([row - 1, column])

    if row - 1 > -1 and column + 1 < len(board[0]) and not visited[row - 1][column + 1]:
        neigbours.append([row - 1, column + 1])

    if column + 1  < len(board[0]) and not visited[row][column + 1]:
        neigbours.append([row, column + 1])

    if row + 1 < len(board) and column + 1 < len(board[0]) and not visited[row + 1][column + 1]:
        neigbours.append([row + 1, column + 1])

    if row + 1 < len(board) and not visited[row + 1][column]:
        neigbours.append([row + 1, column])
    
    if row + 1 < len(board) and column - 1 > -1 and not visited[row + 1][column - 1]:
        neigbours.append([row + 1, column - 1])
    
    if column - 1 > -1 and not visited[row][column - 1]:
        neigbours.append([row, column - 1])
    
    return neigbours


def findIfWordExists(board, word, result):

    wordLength = len(word)
    counter = 0
    visited = [[False for _ in row] for row in board]

    for row in range(len(board)):
        for column in range(len(row)):

            if not visited[row][column]:

                visited[row][column] = True
                
                if board[row][column] == word[counter]:
                    counter += 1
                    if counter == wordLength - 1:
                        result.add(word)
                        return
                    
                    neighbours = findNeighbours(board, row, column, visited)

                    for neighbour in neighbours:
                        x = neighbour[0]
                        y = neighbour[1]

                        if not visited[x][y]:
                            visited[x][y] = 1
                            if board[x][y] == word[counter]:


                else:
                    counter = 0