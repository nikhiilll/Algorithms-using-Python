def spiralTraverse(array):
    """
    TC: O(n) | SC: O(n)
    """
    result = []
    startRow, endRow = 0, len(array) - 1
    startColumn, endColumn = 0, len(array[0]) - 1

    while startRow <= endRow and startColumn <= endColumn:

        for col in range(startColumn, endColumn + 1):
            result.append(array[startRow][col])
        
        for row in range(startRow + 1, endRow + 1):
            result.append(array[row][endColumn])
        
        for col in reversed(range(startColumn, endColumn)):
            if startRow == endRow:
                break

            result.append(array[endRow][col])

        for row in reversed(range(startRow + 1, endRow)):

            if startColumn == endColumn:
                break

            result.append(array[row][startColumn])
        
        startRow += 1
        endRow -= 1
        startColumn += 1
        endColumn -= 1
    
    return result