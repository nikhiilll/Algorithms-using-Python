def combinationSum4(nums, target):

    combArray = [0 for _ in range(target + 1)]
    combArray[0] = 1
    

    for i in range(1, target + 1):
        for num in nums:
            if num <= i:
                combArray[i] += combArray[i - num]
    
    return combArray[-1]

print(combinationSum4([1, 2, 3], 4))