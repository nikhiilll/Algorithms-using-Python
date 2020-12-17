def climbingStairs(n):
    """
    TC: O(n) | SC: O(n)
    """
    noOfWays = [1 for _ in range(n + 1)]

    for i in range(2, n + 1):
        noOfWays[i] = noOfWays[i - 1] + noOfWays[i - 2]
    
    return noOfWays[-1]

    """
    This can also be solved like the Fibonacci sequence using two vairables. That would reduce the space complexity to constant.
    TC: O(n) | SC: O(1)
    """
