def jumpGame(nums):
    """
    TC: O(n^2) | SC: O(n)
    """
    # isReachable = [False for num in nums]
    # isReachable[0] = True

    # for i in range(len(nums) - 1):
    #     if isReachable[i]:
    #         for jumpLength in range(1, nums[i] + 1):
    #             if jumpLength + i < len(nums):
    #                 isReachable[jumpLength + i] = True
    #             if isReachable[-1]:
    #                 return True
    
    # return isReachable[-1]

    maxJump = 0

    for i in range(len(nums)):
        if i > maxJump:
            return False
        maxJump = max(maxJump, i + nums[i])
    
    return True

print(jumpGame([3,2,1,0,4]))