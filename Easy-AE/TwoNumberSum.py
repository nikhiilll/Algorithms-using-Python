def twoNumberSum(array, targetSum):
    """
    TC: O(n2), SC: O(1)
    """
    n = len(array)
    for num1 in range(n - 1):
        for num2 in range(num1 + 1, n):
            if array[num1] + array[num2] == targetSum:
                return ([array[num1], array[num2]])
    
    return ([])

ans = twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)
print(ans)


def twoNumberSum2(array, targetSum):
    """
    TC: O(nlogn) -- Because of the sorting
    SC: O(n)
    """
    n = len(array)
    sortedArray = sorted(array)
    leftPtr, rightPtr = 0, n - 1

    while leftPtr < rightPtr and leftPtr < n and rightPtr > 0:
        if sortedArray[leftPtr] + sortedArray[rightPtr] < targetSum:
            leftPtr += 1
        elif sortedArray[leftPtr] + sortedArray[rightPtr] > targetSum:
            rightPtr -= 1
        else:
            return ([sortedArray[leftPtr], sortedArray[rightPtr]])
    
    return ([])

ans = twoNumberSum2([3, 5, -4, 8, 11, 1, -1, 6], 10)
print(ans)



