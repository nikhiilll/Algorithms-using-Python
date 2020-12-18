def houseRobber(nums):
    """
    TC: O(n^2) | SC: O(n)
    """ 
    # if not nums:
    #     return 0

    # robberies = [num for num in nums]
    # maxRobbery = float("-inf")
    # for i in range(0, len(nums)):
    #     for j  in range(i - 1):
    #         robberies[i] = max(robberies[i], robberies[j] + nums[i])
            
    #     maxRobbery = max(maxRobbery, robberies[i])
    
    # return maxRobbery

    """
    TC: O(n) | SC: O(n)
    """
    if not nums:
        return 0

    robberies = [0] + [num for num in nums]

    for i in range(2, len(nums) + 1):
        robberies[i] = max(robberies[i - 1], robberies[i - 2] + nums[i - 1])
    
    return robberies[-1]

print(houseRobber([2, 1]))
