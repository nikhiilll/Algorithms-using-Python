def minimumPathSum(grid):

    for i in range(1, len(grid)):
        grid[i][0] += grid[i - 1][0]

    for j in range(1, len(grid[0])):
        grid[0][j] += grid[0][j - 1]

    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            print(grid)
            grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])

    return grid[-1][-1]

print(minimumPathSum([[1,3,1],[1,5,1],[4,2,1]]))