def zigzagTraverse(array):
    """
    TC: O(n) | SC: O(n)
    """
    row, col = 0, 0
    noRows = len(array) - 1
    noCols = len(array[0]) - 1
    result = []
    goingDown = True

    while isInBounds(row, col, noRows, noCols):

        result.append(array[row][col])
        if goingDown:
            
            if col == 0 or row == noRows:
                goingDown = False
                if row == noRows:
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1
        else:
            if row == 0 or col == noCols:
                goingDown = True
                if col == noCols:
                    row += 1
                else:
                    col += 1
            else:
                row -= 1
                col += 1

    
    return result

def isInBounds(row, col, noRows, noCols):
    return row >= 0 and row <= noRows and col >= 0 and col <= noCols

array = [[1, 3, 4, 10], [2, 5, 9, 11], [6, 8, 12, 15], [7, 13, 14, 16]]
print(zigzagTraverse(array))