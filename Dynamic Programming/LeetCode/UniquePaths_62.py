def uniquePaths(m, n):
    """
    TC: O(m * n) | SC: O(m * n)
    """
    # board = [[0 for _ in range(n)] for _ in range(m)]
    # board[0][0] = 1

    # for i in range(m):
    #     for j in range(n):
    #         if i == 0 and j == 0:
    #             continue
    #         if j - 1 < 0:
    #             board[i][j] = board[i - 1][j]
    #         elif i - 1 < 0:
    #             board[i][j] = board[i][j - 1]
    #         else:
    #             board[i][j] = board[i - 1][j] + board[i][j - 1]
    
    # return board[m - 1][n - 1]

    board = [[1 for _ in range(n)] for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            board[i][j] = board[i - 1][j] + board[i][j - 1]
                
    return board[m - 1][n - 1]

print(uniquePaths(3, 3))