def fourNumberSum(array, targetSum):
    """
    TC: O(n^3) | SC: O(h), h->number of pairs * 4
    """
    result = []
    n = len(array)
    array.sort()

    for firstNum in range(n - 3):
        for secondNum in range(firstNum + 1, n - 2):

            leftPtr = secondNum + 1
            rightPtr = n - 1

            while leftPtr < rightPtr:
                currentSum = array[firstNum] + array[secondNum] + array[leftPtr] + array[rightPtr]
                print(array[firstNum], array[secondNum], array[leftPtr], array[rightPtr])
                if currentSum > targetSum:
                    rightPtr -= 1
                elif currentSum < targetSum:
                    leftPtr += 1
                else:
                    result.append([array[firstNum], array[secondNum], array[leftPtr], array[rightPtr]])
                    rightPtr -= 1
                    leftPtr += 1
    
    return result

def fourNumberSum2(array, targetSum):
    """
    TC: Worst -> O(n^3), Average -> O(n^2)
    SC: O(n^2)
    """
    result = []
    pairs = {}

    for i in range(1, len(array) - 1):

        for j in range(i + 1, len(array)):
            currentSum =  array[i] + array[j]
            diff = targetSum - currentSum
            if diff in pairs:
                for pair in pairs[diff]:
                    result.append(pair + ([array[i], array[j]]))

        for k in range(0, i):
            currentSum = array[i] + array[k]
            if currentSum not in pairs:
                pairs[currentSum] = [[array[i], array[k]]]
            else:
                pairs[currentSum].append([array[i], array[k]])
    
    return result

print(fourNumberSum2([7, 6, 4, -1, 1, 2], 16))
