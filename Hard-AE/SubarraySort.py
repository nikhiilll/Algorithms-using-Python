def subarraySort(array):
    """
    TC: O(n) | SC: O(1)
    """
    minOutOfOrder = float("inf")
    maxOutOfOrder = float("-inf")

    for i in range(len(array)):

        num = array[i]
        if isOutOfOrder(i, num, array):
            minOutOfOrder = min(minOutOfOrder, num)
            maxOutOfOrder = max(maxOutOfOrder, num)

    if minOutOfOrder == float("inf"):
        return [-1, -1]

    leftIndex = 0
    while minOutOfOrder >= array[leftIndex]:
        leftIndex += 1
    rightIndex = len(array) - 1
    while maxOutOfOrder <= array[rightIndex]:
        rightIndex -= 1
    
    return [leftIndex, rightIndex]


def isOutOfOrder(i, num, array):

    if i == 0:
        return num > array[i + 1]
    elif i == len(array) - 1:
        return num < array[i - 1]
    else:
        return num < array[i - 1] or num > array[i + 1]

print(subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))