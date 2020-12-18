def minFallingPathSum(A):
    """
    TC: O(row*column) | SC: O(1)
    """
    if not A:
        return 0

    rows = len(A)
    columns = len(A[0])

    for row in range(1, rows):
        for column in range(columns):
            if column - 1 < 0:
                A[row][column] = min(A[row][column] + A[row - 1][column], A[row][column] + A[row - 1][column + 1])
            elif column + 1 >= columns:
                A[row][column] = min(A[row][column] + A[row - 1][column], A[row][column] + A[row - 1][column - 1])
            else:
                A[row][column] = min(A[row][column] + A[row - 1][column], A[row][column] + A[row - 1][column + 1], A[row][column] + A[row - 1][column - 1])
    
    return min(A[-1])


print(minFallingPathSum([[-51,-35,74],[-62,14,-53],[94,61,-10]]))



