def bubbleSort(array):

    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
        
    return array
"""
TC: O(n^2) | SC: O(1)
"""
def bubbleSort2(array):

    isSorted = False
    counter = 0

    while not isSorted:
        isSorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                isSorted = False
        counter += 1
        
    return array

print(bubbleSort2([8, 5, 2, 9, 5, 6, 3]))