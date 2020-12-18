def houseRobber2(nums):

    if not nums:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        return max(houseRobber(nums, 0, len(nums) - 1), houseRobber(nums, 1, len(nums)))

def houseRobber(nums, start, end):

    robCurrentHouse, notRobCurrentHouse = 0, 0

    for i in range(start, end):
        robCurrentHouse, notRobCurrentHouse = notRobCurrentHouse + nums[i], max(robCurrentHouse, notRobCurrentHouse)
    
    return max(robCurrentHouse, notRobCurrentHouse)

print(houseRobber2([1,2,3,1]))