def longestIncreasingSubsequence(nums):

    lisArray = [0 for _ in nums]
    lisArray[0] = 0
    maxSubsequenceLength = 0
    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[i] > nums[j]:
                lisArray[i] = max(lisArray[i], lisArray[j] + 1)
                maxSubsequenceLength = max(maxSubsequenceLength, lisArray[i])
    
    return maxSubsequenceLength + 1

print(longestIncreasingSubsequence([0,1,0,3,2,3]))
