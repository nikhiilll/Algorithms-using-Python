def minNumberOfJumps(array):
    """
    TC: O(n^2) | SC: O(n)
    """
    # jumpArray = [float("inf") for _ in range(len(array))]
    # jumpArray[0] = 0
    # longestJump = array[0]

    # for i in range(1, len(array)):

    #     longestJump = max(longestJump, array[i])
        
    #     for j in range(max(0, i - longestJump), i):
    #         if i <= j + array[j]:
    #             jumpArray[i] = min(jumpArray[i], jumpArray[j] + 1)
    
    # return jumpArray[-1]

    """
    TC: O(n) | SC: O(1)
    """

    if len(array) == 1:
        return 0

    jumps = 0
    maxReach = array[0]
    steps = array[0]

    for i in range(1, len(array) - 1):
        maxReach = max(maxReach, i + array[i])
        steps -= 1

        if steps == 0:
            steps = maxReach - i
            jumps += 1
    
    return jumps + 1

print(minNumberOfJumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]))