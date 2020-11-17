def productSumHelper(depth, arr):

    sum = 0
    if not arr:
        return 0
    else:
        for num in arr:
            if type(num) == int:
                sum += num
            else:
                sum += productSumHelper(depth + 1, num)
        return depth * sum
            
"""
TC: O(n) | SC: O(d)
"""

def productSum(array):

    return productSumHelper(1, array)

inp = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
print(productSum(inp))

