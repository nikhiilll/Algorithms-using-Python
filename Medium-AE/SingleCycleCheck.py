def hasSingleCycle(array):
    """
    TC: O(n^2) | SC: O(n)
    """
    n = len(array)

    if n < 2:
        return False
    
    for i in range(n):

        visited = [False] * n
        startIndex = i
        visited[startIndex] = True
        nextIndex = i + array[i]

        while True:

            if nextIndex > n - 1:
                nextIndex = nextIndex % n
            elif nextIndex < 0:
                nextIndex = nextIndex % n

            if nextIndex == startIndex and all(visited):
                return True
          
            if visited[nextIndex]:
                break
            else:
                visited[nextIndex] = True
                
            nextIndex = nextIndex + array[nextIndex]

    return False

def hasSingleCycle2(array):
    """
    TC: O(n) | SC: O(1)
    """
    noOfElementsVisited = 0
    currentIndex = 0

    while noOfElementsVisited < len(array):

        if noOfElementsVisited > 0 and currentIndex == 0:
            return False
        
        noOfElementsVisited += 1
        nextIndex = currentIndex + array[currentIndex]

        if nextIndex < 0 or nextIndex >= len(array):
            nextIndex = nextIndex % len(array)
        
        currentIndex = nextIndex
    
    return currentIndex == 0


print(hasSingleCycle2([2, 3, 1, -4, -4, 2]))


