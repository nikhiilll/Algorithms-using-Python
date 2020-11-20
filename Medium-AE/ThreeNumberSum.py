def threeNumberSum(array, targetSum):
    """
    TC: O(n^2) | SC: O(n)
    """
    sortedArray = sorted(array)
    result = []
    n = len(array)

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:

            if sortedArray[left] + sortedArray[right] + sortedArray[i] == targetSum:
                result.append([sortedArray[i], sortedArray[left], sortedArray[right]])
                left += 1
                right -= 1
            elif sortedArray[left] + sortedArray[right] + sortedArray[i] > targetSum:
                right -= 1
            else:
                left += 1
    
    return result

print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))

