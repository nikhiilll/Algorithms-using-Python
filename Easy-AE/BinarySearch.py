def binarySearch(array, target):

    low, high = 0, len(array) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1

print(binarySearch([1, 5, 23, 111], 120))