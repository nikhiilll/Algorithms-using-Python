def findThreeLargestNumbers(array):
    
    large1, large2, large3 = float('-inf'), float('-inf'), float('-inf')

    for num in array:
        if num >= large3:
            if num >= large1:
                large3 = large2
                large2 = large1
                large1 = num
            elif num >= large2:
                large3 = large2
                large2 = num
            else:
                large3 = num
    
    return [large3, large2, large1]
"""
TC: O(n) | SC: O(1)
"""
print(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))