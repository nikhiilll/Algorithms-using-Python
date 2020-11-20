def moveElementToEnd(array, toMove):
    """
    TC: O(n) | SC: O(1)
    """
    endPointer = len(array) - 1
    if not array:
        return array
        
    while array[endPointer] == toMove and endPointer > -1:
        endPointer -= 1
        if endPointer == 0:
            return array
    
    startPointer = 0
    while startPointer < endPointer:
        while array[endPointer] == toMove and startPointer < endPointer:
            endPointer -= 1
        if array[startPointer] == toMove:
            array[startPointer], array[endPointer] = array[endPointer], array[startPointer]
            endPointer -= 1
        startPointer += 1
    
    return array

print(moveElementToEnd([5, 1, 2, 5, 5, 3, 4, 6, 7, 5, 8, 9, 10, 11, 5, 5, 12], 5))