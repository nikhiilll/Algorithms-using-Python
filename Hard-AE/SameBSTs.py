def sameBsts(arrayOne, arrayTwo):
    """
    TC: O(n^2) | SC: O(n^2)
    """
    if len(arrayOne) != len(arrayTwo):
        return False
    
    if arrayOne[0] != arrayTwo[0]:
        return False
    
    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True
    
    smallerArrayOne = getSmaller(arrayOne)
    smallerArrayTwo = getSmaller(arrayTwo)
    biggerArrayOne = getBigger(arrayOne)
    biggerArrayTwo = getBigger(arrayTwo)

    return sameBsts(smallerArrayOne, smallerArrayTwo) and sameBsts(biggerArrayOne, biggerArrayTwo)

def getSmaller(array):

    result = []

    for i in range(1, len(array)):
        if array[i] < array[0]:
            result.append(array[i])
    
    return result

def getBigger(array):

    result = []

    for i in range(1, len(array)):
        if array[i] >= array[0]:
            result.append(array[i])
    
    return result