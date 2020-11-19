def selectionSort(array):

    n = len(array)

    for i in range(n - 1):
        small = i
        for j in range(i + 1, n):
            if array[j] < array[small]:
                small = j
        array[i], array[small] = array[small], array[i]
    
    return array

print(selectionSort([8, 5, 2, 9, 5, 6, 3]))