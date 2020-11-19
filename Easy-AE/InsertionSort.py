def insertionSort(array):

    n = len(array)
    if n == 0 or n == 1:
        return array
    
    for pivot in range(0, n - 1):
        element = pivot + 1
        for i in range(pivot, -1, -1):
            if array[element] < array[i]:
                array[element], array[i] = array[i], array[element]
                element = i
    
    return array
"""
TC: O(n^2) | SC: O(1)
"""
print(insertionSort([2, 1]))
