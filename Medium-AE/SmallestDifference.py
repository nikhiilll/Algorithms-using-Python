def smallestDifference(arrayOne, arrayTwo):
    """
    TC: O(nlogn + mlogm) | SC: O(1)
    """
    arrayOne.sort()
    arrayTwo.sort()
    pointerOne, pointerTwo = 0, 0
    num1, num2 = 0, 0
    smallestDiff = float('inf')

    while pointerOne < len(arrayOne) and pointerTwo < len(arrayTwo):

        diff = abs(arrayOne[pointerOne] - arrayTwo[pointerTwo])
        if diff == 0:
            return [arrayOne[pointerOne], arrayTwo[pointerTwo]]
        elif diff < smallestDiff:
            num1 = arrayOne[pointerOne]
            num2 = arrayTwo[pointerTwo]
            smallestDiff = diff
        
        if arrayOne[pointerOne] < arrayTwo[pointerTwo]:
            pointerOne += 1
        else:
            pointerTwo += 1
    
    return[num1, num2]
        
print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))
        
        
        


