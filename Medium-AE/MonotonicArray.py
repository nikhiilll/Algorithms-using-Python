def isIncreasing(array):

    firstElement = 0
    nextElement = 1

    while nextElement < len(array):
        if array[firstElement] > array[nextElement]:
            return False
        firstElement += 1
        nextElement += 1
    
    return True

def isDecreasing(array):

    firstElement = 0
    nextElement = 1

    while nextElement < len(array):
        if array[firstElement] < array[nextElement]:
            return False
        firstElement += 1
        nextElement += 1
    
    return True

def isMonotonic(array):
    """
    TC: O(n) | SC: O(1)
    """
    if not array or len(array) == 1:
        return True

    return (isIncreasing(array) or isDecreasing(array))

