def kadanesAlgorithm(array):
    """
    TC: O(n) | SC: O(1)
    """
    maxSoFar = float("-inf")
    sumSoFar = 0

    for num in array:
        sumSoFar = max(num, sumSoFar + num)
        if sumSoFar > maxSoFar:
            maxSoFar = sumSoFar
    
    return maxSoFar
    